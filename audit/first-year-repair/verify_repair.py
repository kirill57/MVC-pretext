"""Structural regression checks and exercise-route receipts for this repair.

The manual route annotations below are mathematical review evidence, not an
automatic proof checker. Rendering checks inspect generated HTML, not source only.
"""
from pathlib import Path
from lxml import etree as E
from lxml import html
import hashlib,json,re,subprocess
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
ID='{http://www.w3.org/XML/1998/namespace}id'
base=E.parse(str(HERE/'baseline-expanded.xml'))
current=E.parse(str(ROOT/'source/main.ptx'));current.xinclude()
old_ids={n.get(ID):n for n in base.iter() if n.get(ID)}
new_ids={n.get(ID):n for n in current.iter() if n.get(ID)}
assert not set(old_ids)-set(new_ids), 'A retained semantic ID disappeared'
def signature(n):
    return re.sub(r'\s+',' ',E.tostring(n,encoding='unicode',with_tail=False)).strip()
assert signature(old_ids['sec-4-parametric-surfaces'])==signature(new_ids['sec-4-parametric-surfaces'])
assert signature(old_ids['sec-5-derivatives-and-integrals-of-vector-valued-functions'])==signature(new_ids['sec-5-derivatives-and-integrals-of-vector-valued-functions'])
assert [signature(n) for n in base.xpath('//image')]==[signature(n) for n in current.xpath('//image')]
def title(n):return ''.join(n.find('title').itertext()) if n.find('title') is not None else ''
def optional(n):return any(title(x).startswith('Optional:') for x in [n,*n.iterancestors()])
fold_nodes=[n for n in current.iter() if n.tag in ('aside','paragraphs','exercise','proof') and title(n).startswith('Optional:')]
fold_checks=[]
for n in fold_nodes:
    section=next(a for a in n.iterancestors() if a.tag=='section')
    page=ROOT/'output/web'/f'{section.get(ID)}.html'
    tree=html.parse(str(page))
    found=tree.xpath('//*[@id=$id]',id=n.get(ID))
    assert len(found)==1,(n.get(ID),'missing or duplicated HTML target')
    rendered=found[0]
    assert rendered.tag=='details' and rendered.get('open') is None,n.get(ID)
    assert 'Optional:' in rendered.find('summary').text_content(),n.get(ID)
    fold_checks.append({'id':n.get(ID),'page':page.relative_to(ROOT).as_posix(),'closed_by_default':True})

# Exact changed-exercise routes; fuller solutions are authored in the source.
routes={
'checkpoint-1-5-triangle-equality':('The preceding triangle-equality characterization includes zero vectors.','Zero-length legs identify two stops; otherwise the two displacements are in the same direction.'),
'checkpoint-3-2-basis-determines-all':('The map is explicitly linear; basis expansion and linearity have been taught.','T(x)=sum x_i T(e_i); the retained nonlinear counterexample explains the hypothesis.'),
'c6s6-ex-cc-three-conditions':('Relative continuity and the punctured-limit convention in Chapter 6.','At accumulation points the value exists, the limit exists, and they agree; a singleton is relatively continuous.'),
'checkpoint-9-1-gradient-normal-tangent-plane':('C1 implicit-function theorem, chain rule, gradient and point-normal plane equation.','F=z and G=z^2 have the same plane; only the first gradient is nonzero. The supplied C1/nonzero hypotheses justify the normal construction.'),
'checkpoint-9-5-gradients-parallel':('C1 regular constraint, chain rule along two-sided curves, perpendicular subspace of a plane tangent line.','The nonzero constraint gradient spans the normal line; zero objective gradient uses lambda=0. The squared-circle gradient vanishes and fails the test.'),
'checkpoint-9-6-multiplier-misses-boundary':('One-variable endpoint extrema and feasible parameter intervals.','On r(t)=(t,0), t>=0, f=x has minimum at zero but derivative 1. A tangent exists; two-sided feasible motion does not.'),
'c11s7-sk-27':('Supplied cylindrical formula and its once-coverage condition.','The angular ranges give 4pi and 8pi for the same radius-2 height-1 cylinder; a seam has zero volume, unlike repeated interior coverage.'),
'c11s3-ex-justify-cylindrical-integration':('Cartesian slicing, planar polar theorem, and explicitly supplied continuity of the fixed-interval integral.','Apply polar integration to G(x,y)=integral_0^1 f dz, then substitute its definition. This proves the case for arbitrary continuous f on the specified cylinder.'),
'c11s3-ex-three-measurement-volume':('Optional same-space triple-covector determinant definition; determinant row identities.','Linearity/alternation follow from rows; surviving cylindrical coefficients r cos^2(theta)+r sin^2(theta) sum to r. Optional, without general wedge-associativity claim.'),
'c11s4-ex-justify-spherical-integration':('Supplied cylindrical theorem, fixed-theta slicing, planar polar theorem, one-variable angle substitution.','The meridional half-disk gives factor rho; the old r becomes rho cos(psi). psi=pi/2-phi reverses bounds and gives rho^2 sin(phi), for arbitrary continuous f on the ball.'),
'c13s6-ex-parameter-integral-two-routes':('One-variable polynomial integration and differentiation; the parameter-integral lemma is supplied.','H=x/3+x^2/2; both routes give 1/3+x. Polynomial continuity verifies hypotheses. An illustration only.'),
'checkpoint-13-3-direction-survives':('Earlier scalar line-integral and work-integral definitions.','Both speeds are 1; dot products with (1,0) are 1 and -1. Scalar integrals stay 1, work reverses sign.'),
'c18s10-ex-pr-any-surface':('Stokes for a permitted compact oriented surface; globally smooth primitive 3x dy.','Induced CCW circle integral is 3 integral cos^2(t) dt=3pi. No unsupported any-surface assertion.'),
'c19s5-ex-averaging-forces-local-constancy':('Continuity, integral inequalities, and supplied mean-value property.','A deficit epsilon on an arc of angle ell lowers the mean by epsilon ell/(2pi); every small centered circle gives the whole disk. Global propagation is supplied separately.'),
'checkpoint-19-5-maximum-principle':('Mean-value theorem and available maximum principle with C2 harmonicity and connectedness.','Explain disk constancy by averaging, then invoke the supplied global theorem. Optional relative-topology proof is unnecessary.'),
'appF-ex-compact-subsequence':('Optional local vocabulary and explicitly supplied nested-box completeness.','Finite branching retains infinitely many indices; increasing selection converges within boxes of diameter sqrt(n)L/2^k. Openness of the complement forces the limit into K.'),
'appF-ex-uniform-continuity':('Optional convergent-subsequence exercise.','A violating pair sequence has a subsequence with both inputs tending to the same point, contradicting continuity and a fixed positive output gap.'),
'appF-ex-finite-cover-control':('Optional subsequence result and local open-cover definition.','Bad centers converge; a ball inside the limit-point cover member eventually contains the supposedly bad ball. A grid of diameter below eta extracts a finite subcover.'),
'appF-ex-path-grid-subdivision':('Optional subsequence result, openness and continuity relative to a closed parameter interval/rectangle.','All points of a bad cell approach the same subsequential limit, by its vanishing diameter. Continuity puts the entire image inside one domain ball, a contradiction.')
}
prior=json.loads((ROOT/'audit/logical-order-round2/task-witnesses.json').read_text(encoding='utf-8'))
witnesses={r.get('task_id',r.get('task_key',r.get('xml_id'))):r for r in prior['rows']}
paths=subprocess.check_output(['git','-c','core.safecrlf=false','diff','--name-only'],cwd=ROOT,text=True).splitlines()
paths.append('source/appendices/appF-proof-sketches/sections/sec-appF-uniform-control-investigation.xml')
checks=[];seen=set()
for path in paths:
    if not path.startswith('source/') or not path.endswith('.xml'):continue
    tree=E.parse(str(ROOT/path))
    for n in tree.xpath('//exercise'):
        ident=n.get(ID); live=new_ids[ident]
        changed=ident not in old_ids or signature(live)!=signature(old_ids[ident])
        if ident in routes:
            support,route=routes[ident];basis='current manual check; source solution where provided';seen.add(ident)
        else:
            assert not changed,(ident,'changed exercise without new route')
            assert ident in witnesses,(ident,'missing previous witness')
            w=witnesses[ident]
            support='Previously audited definitions and supplied results; checked against the changed section context and optional-content boundary.'
            route=w.get('solution_outline') or w.get('outline') or w.get('witness') or 'See named prior audit task witness.'
            basis='unchanged prompt; retained audited route, with current optional classification'
        checks.append({'id':ident,'file':path,'line':n.sourceline,
                       'optional':optional(live),'changed_or_new':changed,
                       'available_support':support,'solution_route':route,'basis':basis})
assert seen==set(routes),set(routes)-seen
(HERE/'task-checks.json').write_text(json.dumps(checks,indent=2),encoding='utf-8')

# Disclose cross-references from the retained route into optional material.
# These must be navigation to optional proofs, not sole operational support.
links=[]
for n in current.xpath('//xref'):
    if optional(n):continue
    targets=n.get('ref','').split()
    for target in targets:
        if target in new_ids and optional(new_ids[target]):
            ancestor=n.getparent()
            links.append({'target':target,'context':' '.join(''.join(ancestor.itertext()).split())})
(HERE/'skip-test-links.json').write_text(json.dumps(links,indent=2),encoding='utf-8')
receipt={'retained_ids':len(old_ids),'current_ids':len(new_ids),'retained_ids_lost':0,
         'sections_4_5_and_5_2_unchanged':True,'all_image_source_unchanged':True,
         'fold_checks':fold_checks,'exercise_routes':len(checks),
         'current_manual_exercise_checks':len(routes),
         'core_exercises':sum(not c['optional'] for c in checks),
         'optional_exercises':sum(c['optional'] for c in checks)}
(HERE/'verification.json').write_text(json.dumps(receipt,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in receipt.items() if k!='fold_checks'},indent=2))
print('Folded optional blocks:',len(fold_checks),'Core-to-optional navigation references:',len(links))
