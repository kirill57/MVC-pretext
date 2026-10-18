"""Migrate inherited structural markup without changing math or graphics.

Run only after content editors finish. A snapshot in logs preserves the input;
the receipt checks all semantic IDs and all math/graphics text before and after.
"""
from collections import Counter
from pathlib import Path
import argparse
import hashlib
import json
import re
from lxml import etree as E

ROOT=Path(__file__).resolve().parents[1]
ID='{http://www.w3.org/XML/1998/namespace}id'
XI='{http://www.w3.org/2001/XInclude}include'
EXCLUDED={'m','md','mrow','latex-image','asymptote','sageplot','pre','c','cd','program','input','output','macros','latex-image-preamble','shortdescription'}
CHARACTERS={'\u2014':'mdash','\u2013':'ndash','\u201c':'lq','\u201d':'rq','\u2018':'lsq','\u2019':'rsq'}
ALT_OVERRIDES={
 'fig-c2s1-multiplication-by-i':'Multiplication by i rotates a vector through a right angle in the complex plane.',
 'c2s4-fig-dot-product-angle':'Two vectors enclose an angle measured using their dot product and lengths.',
 'c2s5-fig-first-cross-product':'Two perpendicular vectors in the horizontal plane have an upward cross product.',
 'c2s6-fig-signed-area-2x2':'The parallelogram spanned by two column vectors has signed area eleven.',
 'c3s5-fig-cramer-oblique-projections':'Parallel projections of b locate its two scaled column-vector components, which sum to b.',
 'c3s5-fig-cramer-two-shears':'Two area-preserving shears replace one scaled component by b while fixing the other column direction.',
 'c3s6-fig-rotated-ellipse':'Rotating the coordinate axes removes the cross term from an ellipse equation.',
 'c4s2-fig-circle-4costheta':'A polar circle with radius four times cosine theta is tangent to the origin.',
 'c4s4-fig-paraboloid':'An elliptic paraboloid opens upward from its vertex at the origin.',
 'c4s4-fig-double-cone':'A double cone has upper and lower nappes meeting at the origin.',
 'c4s4-fig-hyperboloid-one':'A connected hyperboloid of one sheet narrows at its central circular waist.',
 'c4s4-fig-hyperboloid-two':'A hyperboloid of two sheets has separated upper and lower components.',
 'c4s4-fig-saddle':'A saddle rises along the x direction and falls along the y direction.',
 'c8s5-fig-fold-map':'Squaring the first coordinate folds the two halves of the input plane onto the same half-plane.',
 'c8s7-fig-fold-curve':'The curve where the product of the input coordinates is one quarter marks a collapsed area scale.',
 'c10s4-fig-reverse-order-triangle':'The triangular region lies between the diagonal and the bottom edge of the unit square.',
 'c10s5-fig-polar-rectangle':'A small annular sector has radial width delta r and angular side approximately r times delta theta.',
 'c10s5-fig-shifted-disk':'A unit disk centered one unit to the right of the origin has polar boundary r equals two cosine theta.',
 'c11s2-fig-tetrahedron':'A tetrahedron in the positive octant is bounded by the coordinate planes and a sloping plane.',
 'c11s3-fig-polar-rectangle':'The angular side of a small annular sector scales with its distance from the origin.',
 'c11s5-fig-inertia-distance':'Distance to the vertical axis is the radial distance used in the moment of inertia.',
 'c13s6-fig-punctured-plane-loop':'A counterclockwise loop encloses the missing origin where the angular form is singular.',
 'c15s2-fig-area-scale-factor':'Two surface tangent vectors span the parallelogram whose area gives the local area scale.',
 'c17s1-fig-differential-level-curves':'Parallel level lines of the affine temperature approximation accompany its gradient vector.',
 'c18s4-fig-rectangle-changing-curl':'Opposite boundary contributions combine to measure the varying circulation density inside a rectangle.',
}


def sources(path,seen=None):
    seen=set() if seen is None else seen
    path=path.resolve()
    if path in seen:return
    seen.add(path)
    yield path
    for n in E.parse(str(path)).iter(XI):
        yield from sources(path.parent/n.get('href'),seen)


def wrap(n,tag):
    p=n.getparent();i=p.index(n);w=E.Element(tag)
    w.text='\n';w.tail=n.tail;n.tail='\n'
    p.remove(n);w.append(n);p.insert(i,w)
    return w


def unwrap(n):
    p=n.getparent();i=p.index(n)
    assert not (n.text or '').strip(),('text in wrapper',n.tag)
    children=list(n)
    for c in children:
        n.remove(c);p.insert(i,c);i+=1
    if children:children[-1].tail=n.tail
    p.remove(n)


def signature(tree):
    return {'ids': sorted(n.get(ID) for n in tree.iter() if n.get(ID)),
      'math_graphics':[(n.tag,''.join(n.itertext())) for n in tree.iter()
                       if n.tag in ('m','md','latex-image','asymptote','interactive')],
      'image_sources':[n.get('source') for n in tree.iter('image')]}


def plain_caption(image):
    figure=next((x for x in image.iterancestors() if x.tag=='figure'),None)
    if figure is not None and figure.get(ID) in ALT_OVERRIDES:
        return ALT_OVERRIDES[figure.get(ID)]
    caption=figure.find('caption') if figure is not None else None
    if caption is None:
        caption=next((x.find('title') for x in image.iterancestors() if x.find('title') is not None),None)
    if caption is None:return 'Geometric illustration accompanying the surrounding explanation.'
    # The visible caption retains its full accessible MathJax expressions.
    # Alt text gives a short prose identifier rather than raw TeX source.
    text=''.join(caption.itertext())
    text=re.sub(r'\\(?:mathbf|vect|mathbb|mathrm|operatorname|text)\{([^{}]*)\}',r'\1',text)
    names={'theta':'theta','phi':'phi','rho':'rho','pi':'pi','alpha':'alpha','beta':'beta','gamma':'gamma','Delta':'Delta','times':' times ','wedge':' wedge ','partial':'partial ','nabla':'gradient '}
    for command,name in names.items():text=text.replace('\\'+command,name)
    text=re.sub(r'\\[a-zA-Z]+',' ',text)
    text=re.sub(r'[{}^_\\]',' ',text)
    text=' '.join(text.split())
    text=re.sub(r'\s*\(Interactive:.*','',text,flags=re.I)
    if len(text)>122:text=text[:119].rsplit(' ',1)[0]+'...'
    return text


def character_markup(tree,counts):
    # Iterate original text/tail slots, so newly inserted character elements
    # cannot be visited twice. Do not touch executable or mathematical text.
    slots=[]
    for n in tree.iter():
        if not isinstance(n.tag,str):continue
        if n.tag not in EXCLUDED and not any(a.tag in EXCLUDED for a in n.iterancestors()):
            if n.text and any(c in n.text for c in CHARACTERS):slots.append((n,False,n.text))
        parent=n.getparent()
        if parent is not None and parent.tag not in EXCLUDED and not any(a.tag in EXCLUDED for a in parent.iterancestors()):
            if n.tail and any(c in n.tail for c in CHARACTERS):slots.append((n,True,n.tail))
    for n,tail,text in slots:
        parts=re.split('(['+''.join(CHARACTERS)+'])',text)
        if tail:
            parent=n.getparent();index=parent.index(n)+1;n.tail=parts[0]
        else:
            parent=n;index=0;n.text=parts[0]
        for i in range(1,len(parts),2):
            c=E.Element(CHARACTERS[parts[i]]);c.tail=parts[i+1]
            parent.insert(index,c);index+=1;counts['character_markup']+=1


def migrate(tree):
    counts=Counter()
    # A text table is a block, not an inline part of a paragraph.
    for p in list(tree.xpath('//p[tabular]')):
        assert len(p)==1 and not (p.text or '').strip() and not (p[0].tail or '').strip()
        assert not p.attrib
        unwrap(p);counts['table_paragraph_unwrapped']+=1
    for s in list(tree.xpath('//warning/statement')):
        unwrap(s);counts['warning_statement_unwrapped']+=1
    # Display math and ordinary lists belong inside paragraphs.
    for n in list(tree.iter()):
        if n.tag in ('md','ol','ul','dl') and n.getparent() is not None and n.getparent().tag!='p':
            wrap(n,'p');counts['paragraph_for_'+n.tag]+=1
    # Reviews consisting only of several exercise divisions need one genuine
    # opening subdivision. Retain all exercise containers and their numbering.
    for n in list(tree.iter()):
        if n.tag=='section' and n.find('exercises') is not None and n.find('subsection') is None:
            intro=n.find('introduction')
            if intro is not None:
                intro.tag='subsection';intro.set(ID,n.get(ID)+'-recap')
                title=E.Element('title');title.text='Review of the main ideas';intro.insert(0,title)
                counts['review_recap_subdivision']+=1
    # The nested practice collection is one exercises division with subgroups.
    for n in tree.xpath('//subsection[@xml:id="c4s6-subsec-practice"]',namespaces={'xml':'http://www.w3.org/XML/1998/namespace'}):
        n.tag='exercises'
        for c in n:
            if c.tag=='exercises':c.tag='subexercises'
        counts['practice_exercise_subgroups']+=1
    metadata={'title','shorttitle','subtitle','author','objectives','outcomes','introduction','conclusion','exercises','references','solutions','reading-questions','printout'}
    for n in list(tree.iter()):
        if n.tag not in ('chapter','appendix','section','subsection'):continue
        divs=[i for i,c in enumerate(n) if c.tag in ('section','subsection','subsubsection')]
        if not divs:continue
        lead=[c for i,c in enumerate(n) if i<min(divs) and isinstance(c.tag,str) and c.tag not in metadata]
        trailing=[c for i,c in enumerate(n) if i>max(divs) and isinstance(c.tag,str) and c.tag not in metadata]
        middle=[c for i,c in enumerate(n) if min(divs)<i<max(divs) and isinstance(c.tag,str) and c.tag not in metadata and c.tag not in ('section','subsection','subsubsection')]
        assert not middle,('unexpected interleaved narrative',n.get(ID))
        for tag,items in [('introduction',lead),('conclusion',trailing)]:
            if not items:continue
            holder=n.find(tag)
            if holder is None:
                holder=E.Element(tag);holder.text='\n';holder.tail=items[-1].tail
                n.insert(n.index(items[0]),holder)
            for c in items:n.remove(c);holder.append(c)
            counts[tag+'_wrapper']+=1
    for image in tree.iter('image'):
        if image.find('description') is None and image.find('shortdescription') is None and image.get('decorative')!='yes':
            alt=E.Element('shortdescription');alt.text=plain_caption(image);alt.tail='\n'
            image.insert(0,alt);counts['image_alt_added']+=1
        short=image.find('shortdescription')
        if short is not None and len(''.join(short.itertext()))>125:
            text=' '.join(''.join(short.itertext()).split())
            short.text=text[:119].rsplit(' ',1)[0]+'...';counts['alt_shortened']+=1
    character_markup(tree,counts)
    return counts


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--apply',action='store_true')
    args=parser.parse_args();changes=[];total=Counter()
    backup=ROOT/'logs/full-audit-2026-10-17/pre-markup'
    for path in sources(ROOT/'source/main.ptx'):
        raw=path.read_bytes();tree=E.fromstring(raw).getroottree();before=signature(tree)
        counts=migrate(tree)
        if not counts:continue
        after=signature(tree)
        assert before['math_graphics']==after['math_graphics'],('math/graphics changed',path)
        assert before['image_sources']==after['image_sources'],('image source changed',path)
        assert set(before['ids'])<=set(after['ids']),('ID lost',path)
        new=E.tostring(tree,encoding='UTF-8',xml_declaration=True).replace(b'\r\n',b'\n')+b'\n'
        if raw.count(b'\r\n') > raw.count(b'\n') / 2:
            new=new.replace(b'\n',b'\r\n')
        E.fromstring(new)
        rel=path.relative_to(ROOT)
        if args.apply:
            target=backup/rel;target.parent.mkdir(parents=True,exist_ok=True)
            if not target.exists():target.write_bytes(raw)
            path.write_bytes(new)
        changes.append({'file':rel.as_posix(),'operations':dict(counts),
                        'before_sha256':hashlib.sha256(raw).hexdigest(),
                        'after_sha256':hashlib.sha256(new).hexdigest(),
                        'math_graphics_preserved':True,'retained_ids_preserved':True})
        total.update(counts)
    receipt={'applied':args.apply,'files':len(changes),'operations':dict(total),'changes':changes}
    if args.apply:
        out=ROOT/'audit/full-audit-2026-10-17/markup-migration.json';out.parent.mkdir(parents=True,exist_ok=True)
        out.write_text(json.dumps(receipt,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in receipt.items() if k!='changes'},indent=2))


if __name__=='__main__':main()
