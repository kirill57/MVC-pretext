"""Compare diagnostics by semantic object, allowing line and sibling shifts."""
from pathlib import Path
from collections import Counter
import json, re
from lxml import etree as E

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
ID='{http://www.w3.org/XML/1998/namespace}id'
def records(report,treefile):
    tree=E.parse(str(treefile))
    out=[];unresolved=[]
    parsed=[line.split('\t') for line in report.read_text(encoding='utf-8-sig').splitlines()]
    parsed=[c for c in parsed if len(c)==5]
    ordered_counts=Counter()
    remappings=[]
    for cols in parsed:
        file,xpath,lineno,rule,message=cols
        source=file.replace('\\','/')
        if '/source/' in source:source='source/'+source.split('/source/',1)[1]
        nodes=tree.xpath(xpath)
        if not nodes:
            unresolved.append(xpath)
            continue
        node=nodes[0]
        # Jing's line is correct, but its reported XPath in these two files
        # sometimes points into the preceding paragraph. The complete set of
        # direct-subsection diagnostics matches every direct subsection, in order.
        # Normalize to those IDs only after checking that one-to-one condition.
        if (rule=='schema' and message.startswith('error: element "subsection" not allowed')
            and source.endswith(('sec-17-the-exterior-derivative-of-a-2-form.xml',
                                 'sec-17-the-rule-d-squared-equals-zero.xml'))):
            section_id=E.parse(str(ROOT/source)).getroot().get(ID)
            section=tree.xpath('//*[@xml:id=$id]',id=section_id)[0]
            actual=section.findall('subsection')
            related=[c for c in parsed if c[0]==file and c[3]==rule and c[4]==message]
            assert len(actual)==len(related), 'Ambiguous diagnostic normalization'
            index=ordered_counts[source];ordered_counts[source]+=1
            corrected=actual[index]
            if tree.getpath(node)!=tree.getpath(corrected):
                remappings.append({'reported_xpath':xpath,'semantic_object':corrected.get(ID),
                                   'reason':'ordered full direct-subsection diagnostic set; assembled start tag checked'})
            node=corrected
        anchor=node
        while anchor is not None and not anchor.get(ID):anchor=anchor.getparent()
        semantic=anchor.get(ID) if anchor is not None else '(root)'
        # The semantic object's relative descendant path distinguishes repeated
        # diagnostics inside the same object, without global sibling positions.
        if anchor is not None:
            base=tree.getpath(anchor)
            relative=tree.getpath(node)[len(base):]
        else:relative=tree.getpath(node)
        key=(source,semantic,relative,rule,message)
        out.append(key)
    return Counter(out),unresolved,remappings
a,au,ar=records(ROOT/'audit/logical-order-round2/evidence/baseline-validation-report.txt',HERE/'baseline-expanded.xml')
b,bu,br=records(HERE/'validation-report.txt',HERE/'validated-assembled.xml')
def rows(c):return [dict(zip(['file','semantic_object','relative_path','rule','message'],key),count=n) for key,n in c.items()]
data={'baseline':a.total(),'current':b.total(),'inherited':(a&b).total(),
      'removed_or_relocated':rows(a-b),'new_or_relocated':rows(b-a),
      'unresolved_baseline':au,'unresolved_current':bu,
      'baseline_locator_normalizations':ar,'current_locator_normalizations':br}
(HERE/'diagnostic-comparison.json').write_text(json.dumps(data,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in data.items() if k not in ['removed_or_relocated','new_or_relocated']},indent=2))
print('Removed/relocated:',sum((a-b).values()),'New/relocated:',sum((b-a).values()))
