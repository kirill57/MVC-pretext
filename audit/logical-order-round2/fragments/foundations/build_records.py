from pathlib import Path
from lxml import etree as E
import json,hashlib,collections
from witness_data import S
ROOT=Path(__file__).resolve().parents[4]
OUT=Path(__file__).parent
SHA='9a9d110af839b539fe598de66ecc4320a4126af4'
nodes=json.loads((ROOT/'audit/logical-order-round2/nodes.json').read_text(encoding='utf8'))
tasks=json.loads((ROOT/'audit/logical-order-round2/task-inventory.json').read_text(encoding='utf8'))
tasks=[t for t in tasks if any('/ch0'+str(i)+'-' in t['path'] for i in range(1,9))]
idx=json.loads((ROOT/'audit/logical-order-round2/id-index.json').read_text(encoding='utf8'))
secs={n['section_order']:n for n in idx.values() if n['role']=='section' and 1<=(n.get('section_order') or 0)<=56}
def ev(n):return {k:n[k] for k in ['snapshot','path','sha256','lines','xml_id','xpath','node_id','section_id','section_order']}
def ref(i):return ev(idx[i])
SUP={}
def refs(sec,*ids):SUP[sec]=list(ids)
refs(7,'def-vector-addition-scalar','def-linear-combination','def-span','def-linear-independence','def-basis','thm-coordinates-in-basis','def-norm','def-distance','def-spheres-balls','def-unit-vector-normalization','def-parametric-equation-line','def-parametric-equation-plane','def-normal-equation-plane','thm-distance-point-to-plane')
refs(16,'def-c2s1-complex-multiplication','thm-c2s1-complex-multiplication-adds-angles','tab-c2s2-quaternion-multiplication','c2s3-thm-product-splits-dot-cross','c2s4-thm-dot-product-and-angle','c2s4-def-projection-onto-line','c2s4-def-work-constant-force','c2s5-thm-length-of-cross-product','c2s5-thm-cross-product-normal-to-plane','c2s5-def-torque','c2s6-def-2x2-determinant','c2s6-def-3x3-determinant','c2s6-thm-scalar-triple-product-signed-volume','c2s6-def-orientation-basis','c2s7-def-bilinear-alternating','c2s7-def-wedge-linear-measurements','c2s7-def-volume-form-dx-dy-dz')
refs(29,'c4s1-def-parametric-curve','c4s1-def-orientation','c4s2-def-polar-coordinates','c4s2-ex-circle-not-centered-origin','c4s3-def-cylindrical-coordinates','c4s3-def-spherical-coordinates','c4s4-ex-elliptic-paraboloid','c4s4-ex-ellipsoid','c4s4-ex-hyperboloid-one-sheet','c4s4-ex-saddle','c4s4-def-level-surface','c4s5-def-parametrized-surface','c4s5-def-grid-curves')
refs(36,'c5s2-thm-componentwise-differentiation','c5s2-thm-fundamental-theorem-vector-valued','c5s3-def-speed','c5s3-thm-arc-length-formula','c5s3-def-unit-tangent-vector','c5s4-thm-curvature-formula-in-space','c5s4-def-tangential-and-normal-acceleration','c5s4add-thm-torsion-from-parameter','c5s5-thm-velocity-in-polar-coordinates','c5s5-thm-acceleration-in-polar-coordinates','c5s5-def-signed-swept-area')
refs(42,'c6s1-def-function-rn-rm','c6s1-def-scalar-vector-field','c6s2-def-level-curve','c6s2-thm-level-curves-horizontal-slices','c6s2-def-level-surface','c6s3-def-formal-limit-rn','c6s3-thm-path-test-nonexistence','c6s3-thm-polar-squeeze-test','c6s3-thm-componentwise-limits','c6s4-def-continuity-at-a-point','c6s4-thm-algebra-of-continuous-functions','c6s4-thm-continuity-of-compositions','c6s4-def-bounded-region','c6s4-def-closed-region','c6s4-thm-extreme-value-theorem')
refs(49,'c7s1-def-partial-derivatives-two-variables','c7s1-def-partial-derivatives-three-variables','c7s2-def-directional-derivative','c7s2-def-gradient','c7s2-thm-gradient-formula','c7s2-thm-steepest','c7s3-def-differentiability-two-variables','c7s3-thm-total-derivative-uses-partials','c7s3-def-tangent-plane-to-graph','c7s4-def-differential-at-a-point','c7s5-def-differentiability-transformation','c7s6-thm-continuous-partials-imply-differentiability','c7s6-thm-jacobian-test-for-differentiability','c2s7-def-wedge-linear-measurements')
refs(56,'c8s1-thm-chain-rule-curve','c8s2-thm-matrix-chain-rule','c8s3-thm-chain-rule-for-differentials','c8s3-subsec-pullback-preview','c8s4-subsec-gradients-non-cartesian','c8s4-subsec-jacobian-determinant','c8s5-thm-inverse-function','c8s6-thm-ift-plane-curve','c8s6-thm-ift-surface','c2s7-def-wedge-linear-measurements','c3s4-def-determinant-general','c3s4-thm-determinant-product')
# Positions below are mathematical support selections, not lexical matches.
GROUPS={
7:[(1,3,[0]),(4,5,[1,2]),(6,8,[3,4,5]),(9,9,[9]),(10,10,[8]),(11,12,[11,12]),(13,13,[0]),(14,18,[6,7,8,9]),(19,20,[10]),(21,25,[11,12]),(26,27,[7,13]),(28,31,[1,2,11,12]),(32,35,[3,4,5]),(36,39,[0,1])],
16:[(1,1,[]),(2,2,[1]),(3,4,[2]),(5,5,[3]),(6,6,[4]),(7,8,[7,8]),(9,10,[10,11,12]),(11,11,[13]),(12,12,[8]),(13,14,[15]),(15,16,[0,1]),(17,17,[2,3]),(18,18,[4]),(19,19,[5]),(20,20,[6]),(21,23,[8]),(24,24,[9]),(25,26,[10]),(27,28,[11,12]),(29,30,[10]),(31,35,[15,7]),(36,37,[3]),(38,40,[14]),(41,41,[8]),(42,42,[16]),(43,43,[]),(44,44,[10]),(45,45,[11,12]),(46,46,[16]),(47,47,[13]),(48,48,[15])],
29:[(1,2,[0,1]),(3,6,[2,3]),(7,8,[4]),(9,12,[5]),(13,13,[4]),(14,14,[6]),(15,15,[7]),(16,16,[8]),(17,17,[9]),(18,18,[10]),(19,24,[11,12])],
36:[(1,5,[0,1]),(6,9,[5]),(10,11,[6]),(12,12,[7]),(13,14,[0]),(15,15,[3]),(16,16,[4]),(17,17,[5]),(18,18,[2,4,5,6,7]),(19,19,[8]),(20,20,[9]),(21,21,[10]),(22,22,[0]),(23,24,[6]),(25,25,[4]),(26,26,[3]),(27,27,[10]),(28,29,[5,7])],
42:[(1,1,[1]),(2,3,[0]),(4,5,[2,3]),(6,7,[5,6,7]),(8,8,[9,5]),(9,9,[12,13,14]),(10,10,[9]),(11,16,[0]),(17,22,[2,3,4]),(23,24,[7,10]),(25,25,[7]),(26,28,[6]),(29,29,[7]),(30,31,[10]),(32,32,[8,7]),(33,33,[9,10]),(34,34,[9,7]),(35,35,[9,6]),(36,36,[11]),(37,38,[12,13,14]),(39,39,[2,3]),(40,41,[6]),(42,42,[9,7]),(43,43,[2,3])],
49:[(1,1,[0]),(2,3,[0,2]),(4,5,[3,4]),(6,7,[6,7]),(8,8,[11]),(9,10,[9]),(11,11,[10]),(12,12,[10]),(13,14,[6,7]),(15,22,[0,1]),(23,24,[3,4]),(25,26,[5]),(27,30,[3,4]),(31,35,[9,8]),(36,38,[6,7,11]),(39,42,[10,8]),(43,45,[10]),(46,47,[13,9]),(48,48,[10]),(49,56,[9,0,1]),(57,57,[2,6,7]),(58,60,[10]),(61,62,[6,7]),(63,63,[9]),(64,64,[13])],
56:[(1,1,[]),(2,2,[0]),(3,3,[1]),(4,5,[2,3]),(6,6,[4]),(7,7,[5]),(8,8,[6]),(9,9,[7]),(10,11,[8]),(12,12,[6]),(13,15,[0]),(16,19,[1]),(20,21,[2]),(22,22,[3]),(23,23,[9]),(24,27,[4]),(28,30,[6]),(31,32,[7]),(33,35,[8]),(36,37,[6,10,11]),(38,38,[0])]
}
support_nodes={}
def local_support(t):
 tree=E.parse(str(ROOT/t['path'])); es=tree.xpath(t['xpath']); e=es[0]
 anc=next((a for a in e.iterancestors() if a.tag in ['subsection','subsubsection','paragraphs','section']),tree.getroot())
 start=anc.sourceline; end=t['lines'][0]-1
 # Scope the exact preceding local teaching; an early discovery prompt can supply its own hint.
 if end<=start:start=t['lines'][0];end=t['lines'][1]
 sid='local-support:'+t['task_key']
 r={**ev(t),'xml_id':anc.get('{http://www.w3.org/XML/1998/namespace}id'),'lines':[start,end],'scope':'preceding local exposition; use only the capability named in the solution outline'}
 support_nodes[sid]=r
 # All self-contained task instructions/data and explicitly offered hints are admissible local scaffolding.
 hid='task-scaffold:'+t['task_key'];support_nodes[hid]={**ev(t),'scope':'task data and supplied hint, not assumed later theory'}
 return [sid,hid]
def selected(t,pos):
 n=t['section_order']; ids=[]
 for lo,hi,js in GROUPS.get(n,[]):
  if lo<=pos<=hi:ids.extend(SUP[n][j] for j in js)
 if n==7 and pos in [32,33]:ids+=['sec-1-linear-independence-and-bases']
 if n==16 and pos==1:ids+=['def-vector-addition-scalar']
 if n==56 and pos==1:ids+=['c7s3-def-differentiability-two-variables']
 if n in [15]:ids+=['tab-c2s2-quaternion-multiplication','c2s3-thm-product-splits-dot-cross','c2s4-def-projection-onto-line','c2s5-thm-length-of-cross-product']
 # Prerequisite facts explicitly needed by chapter-local reasoning.
 if n in [17,18,19,20,21,22,23]:ids+=['thm-coordinates-in-basis','def-linear-independence']
 if n in [31,32,33,34,35]:ids+=['c2s4-thm-basic-algebra-dot-product','c2s5-thm-basic-algebra-cross-product']
 if n in [43,44,45,46,47,48]:ids+=['c6s3-def-formal-limit-rn','c2s4-thm-cauchy-schwarz']
 if n in [50,51,52,53,54,55]:ids+=['c7s3-def-differentiability-scalar-fields-rn','c7s4-def-differential-at-a-point','c3s3-def-matrix-multiplication']
 return list(dict.fromkeys(ids))+local_support(t)+['ENTRY']
counts=collections.Counter();rows=[]
for t in tasks:
 if t['kind']!='formal':continue
 n=t['section_order'];counts[n]+=1;p=counts[n]
 outline=S[n][p-1];sup=selected(t,p)
 verdict='supported'
 if t['task_key']=='c6s6-ex-cc-three-conditions':verdict='FND-01: false without accumulation-point qualification'
 if t['task_key']=='checkpoint-3-2-basis-determines-all':verdict='FND-02: contextual linearity needed; wording refinement'
 if t['task_key']=='checkpoint-1-5-triangle-equality':verdict='FND-03: zero-vector exception omitted'
 rows.append({'task_id':t['task_key'],'kind':'formal','evidence':ev(t),'solution_outline':outline,'support_ids':sup,'verdict':verdict,'checked':True})
assert len(rows)==442
assert all(counts[n]==len(S[n]) for n in S)
def extra_task(key,n,lo,hi,outline,sup,kind='untagged required task'):
 s=secs[n];r={**ev(s),'lines':[lo,hi],'xml_id':key if key in idx else None,'node_id':None}
 rows.append({'task_id':key,'kind':kind,'evidence':r,'solution_outline':outline,'support_ids':sup+['ENTRY'],'verdict':'supported','checked':True})
# Explicit untaged projects: every listed deliverable receives its own witness.
gallery='Choose six equations: cylinder x²+y²=4; bowl z=x²+y²; saddle z=x²-y²; ellipsoid x²/9+y²/4+z²=1; one-sheet x²+y²-z²=1; two-sheet z²-x²-y²=1. For each use the horizontal traces at z=0,1,2 (including empty/point slices) and the already taught sign/shape interpretation; draw those slices and connect according to the full equation.'
extra_task('c4s6-subsec-project-gallery',29,465,501,gallery,['sec-4-quadric-surfaces-and-level-surfaces'])
sphere=[
('domains',570,'r1 rectangle theta[0,2pi],phi[0,pi]; r2/r3 closed disk u²+v²<=a²; r4 rectangle theta[0,2pi],z[-a,a].'),
('circular-grid',571,'r1 fixed phi gives latitude circles; fixed theta gives meridian semicircles. In either graph patch, fixed u or v gives vertical semicircles, including degenerate endpoints. r4 fixed z gives latitude circles and fixed theta gives meridian semicircles.'),
('pole-to-pole',572,'r1 fixed theta and r4 fixed theta run pole to pole. A single upper/lower graph patch cannot do so; its central semicircles reach only its own pole.'),
('repetitions',573,'r1 and r4 repeat theta0/2pi meridian and all angular values at each pole. Each graph patch is injective; upper and lower graphs share their boundary equator.'),
('collapse',574,'r1 edges phi0,pi and r4 edges z=±a collapse to poles; graph parametrizations have no collapsed curve because their first two outputs retain(u,v).'),
('latitude-longitude',575,'Use r1 (or r4) for latitude/longitude because each coordinate family is explicitly a parallel or meridian.'),
('two-graphs',576,'Use r2 and r3, the supplied positive/negative square-root height functions on the disk.')]
for k,l,s in sphere:extra_task('c4s6-sphere:'+k,29,l,l,s,['c4s5-def-grid-curves','sec-4-parametric-surfaces','c4s3-def-spherical-coordinates'])
for k,l,s in [('tables',492,'Include the complex-plane sketch and three left-basis tables computed in checkpoint-c2rot-complex-basis and checkpoint-c2rot-left-basis.'),('planes',494,'Sketch the two perpendicular ordered planes and label the cancelling zero angle and adding 2phi angles.'),('conjugation',496,'Use the explicit conjugation basis calculation: the real/axis plane is fixed, while the perpendicular plane turns 2phi. Thus choose phi=theta/2 and pure imaginary inputs stay pure imaginary.'),('examples',498,'Coordinate example: (1+i)/sqrt2 sends i+2j+3k to i-3j+2k. Tilted example: q=(1+i+j+k)/2 sends the same vector to 3i+j+2k; direct Rodrigues and axial dot-product checks give squared length14 and fixed axial component.'),('instructions',500,'Normalize the nonzero axis u; set q=cos(theta/2)+sin(theta/2)U; encode V; compute q V conjugate(q) in that order; extract the three imaginary coefficients. The preceding derivation proves q is unit and fixes its axis.')]:
 extra_task('c2rot-report:'+k,15,l,l+1,s,['checkpoint-c2rot-left-basis','checkpoint-c2rot-right-basis','checkpoint-c2rot-vector-formula','checkpoint-c2rot-final-tests'])
extra_task('c2rot-optional-axis-through-point',15,505,507,'Translate V=P-A, rotate V by the derived Rodrigues/conjugation formula, and translate back A+Vprime. Points on A+t u remain fixed.',['checkpoint-c2rot-vector-formula','def-affine-lines-planes'],kind='optional untagged task')
extra_task('c8s7-project-second-order-check',56,807,816,'Substitute u=x-y²,v=y-x²: F=(x-2x²y+x^4,y-2xy²+y^4). Dropping degree>=3 leaves(x,y), verifying the stated degree-two inverse approximation without requiring a Taylor theorem.',['c8s5-thm-inverse-function','c8s7-discovery-part3'])
proj=[('jacobian',858,'J=[[1,2v],[2u,1]], determinant1-4uv.'),('wedge',861,'(du+2v dv)wedge(2u du+dv)=(1-4uv)duwedgedv.'),('drawing',867,'Plot v=1/(4u), one branch in each same-sign quadrant, asymptotic to both axes.'),('inverse',874,'Polynomial map is C1, so supplied IFT applies at every point with1-4uv!=0.'),('equal-images',880,'F(1/2+s,1/2-s)=(3/4+s²,3/4+s²), invariant under s->-s; arbitrarily close distinct points collide.'),('interpretation',887,'Determinant and two-form coefficient both describe collapsed first-order area; the exact equal-image calculation separately proves nonlinear failure of local injectivity at(1/2,1/2).')]
for k,l,s in proj:extra_task('c8s7-report:'+k,56,l,l,s,['c8s5-thm-inverse-function','c2s7-def-wedge-linear-measurements','c8s7-discovery-part4'])
exclusions=[]
for t in tasks:
 if t['kind']=='formal':continue
 key=t['task_key']
 if key=='c4s6-subsec-project-gallery':reason='Expanded as required project witness.'
 elif key=='c4s6-subsec-project-sphere':reason='Expanded into seven individual comparison-task witnesses.'
 elif key=='c8s7-discovery-project':reason='Expanded into second-order check and six hand-in witnesses; displayed parts1/2/4 provide local worked scaffolding.'
 elif key=='c4s6-subsec-practice':reason='Container duplicates 24 formal exercises, each checked separately.'
 elif '854:' in key or '740:' in key:reason='Duplicated by c8s7 project deliverables; no independent task omitted.'
 elif '158:' in key and t['section_order']==42:reason='Shared instruction for six natural-domain formal tasks, all individually checked.'
 elif t['section_order']==36 and t['kind']=='directive_candidate':reason='Skill-summary formula, not an additional assessment; corresponding review tasks checked.'
 elif t['section_order']==15:reason='Worked confirmation immediately after conjugation exercise; same calculation checked in that formal task.'
 elif key=='c3s6-subsec-hessian-preview':reason='Explicit optional preview, no required Hessian computation here; retain U07 P3 refinement only.'
 elif key=='subsec-preview-tangent-spaces':reason='Motivational preview, no assessment.'
 elif t['section_order']==31 and t['kind']=='directive_candidate':reason='Expository choice of generic interior parameter pair, not a student task; dedicated grid-normal exercise checked.'
 else:reason='Worked exposition/example or formula table, not an independent assessment. Its mathematics was read and checked with the section.'
 exclusions.append({'task_id':key,'evidence':ev(t),'disposition':reason})
learning=[]
for row in rows:
 for s in row['support_ids']:
  learning.append({'source':s,'target':row['task_id'],'scope':'learning/practice','capability_use':row['solution_outline'],'source_evidence':ref(s) if s in idx else support_nodes.get(s),'target_evidence':row['evidence']})
concepts=[]
for n in nodes:
 if not 1<=(n.get('section_order') or 0)<=56 or n['role'] not in ['definition','theorem','corollary']:continue
 concepts.append({'capability_id':n['xml_id'],'capability':n['text'].split('.')[0][:260], 'first_mention':None,'first_explanation':None,'definition':ev(n) if n['role']=='definition' else None,'first_computation':None,'general_rule':ev(n) if n['role']!='definition' else None,'required_use':[r['task_id'] for r in rows if n['xml_id'] in r['support_ids']],'evidence':ev(n),'scope_note':'This entry identifies the exact definition/rule; null stages are not claims of lexical absence or of first occurrence. Granular cornerstone capabilities are added separately below.'})
def detailed(key,cap,stages,scope):
 d={'capability_id':key,'capability':cap,'scope_note':scope}
 for s in ['first_mention','first_explanation','definition','first_computation','general_rule','required_use']:
  v=stages.get(s);d[s]=[ref(x) for x in v] if isinstance(v,list) else ref(v) if isinstance(v,str) else v
 concepts.append(d)
detailed('FND-COVECTOR-WEDGE-2','Evaluate/distribute wedge of two arbitrary real linear measurements',{'first_mention':'sec-2-alternating-products-a-first-glimpse-of-forms','first_explanation':'c2s7-def-wedge-linear-measurements','definition':'c2s7-def-wedge-linear-measurements','general_rule':'c2s7-def-wedge-linear-measurements','required_use':['c7s7-skj-32','c7s7-skj-33','c8s7-sk-pullback-area-form']},'Two covectors on the same vector space; not arbitrary three-covector wedges or a2-form wedged with a1-form.')
detailed('FND-COORDINATE-3FORM','Evaluate the fixed coordinate volume form on three vectors',{'definition':'c2s7-def-volume-form-dx-dy-dz','first_computation':'ex-c2s8-triple-wedge-compute','required_use':['ex-c2s8-triple-wedge-sign','ex-c2s8-triple-wedge-compute']},'Fixed dx wedge dy wedge dz is determinant evaluation. Does not supply general graded wedge algebra.')
detailed('FND-GRID-GEOMETRY','Freeze one surface parameter and identify whole grid curves',{'definition':'c4s5-def-grid-curves','required_use':['c4s5-ex-saddle-grid','c4s6-ex-d5']},'Geometry-only capability in4.5; no differentiation, tangent or area calculation.')
detailed('FND-GRID-VELOCITY','Differentiate frozen-parameter curves with ordinary one-variable derivatives and take their cross product',{'first_explanation':'c5s2-subsec-surface-grid-velocities','definition':'c5s2-def-regular-grid-point','required_use':['checkpoint-5-2-grid-normal']},'5.2 supplies a regularity lesson with nearby continuity; full tangent-sheet proof explicitly deferred to15.1. Do not replace this lesson by partial-derivative formalism.')
detailed('FND-EVT','Attainment of extrema for nonempty closed bounded domains',{'definition':['c6s4-def-bounded-region','c6s4-def-closed-region'],'general_rule':'c6s4-thm-extreme-value-theorem','required_use':['c6s6-ex-cont-triangle-evt']},'Supplied theorem, explicitly unproved; no finite-cover, subsequence, or connected-domain clopen capability.')
detailed('FND-INVERSE','Existence of a C1 local inverse under a nonzero Jacobian',{'definition':'c8s5-def-local-inverse','general_rule':'c8s5-thm-inverse-function','required_use':['c8s7-sk-system-solvable']},'Supplied existence/smoothness theorem; inverse derivative formula then follows conditionally by chain rule. Applies in generalRn, allowing the4-variable augmented-map task.')
detailed('FND-HESSIAN-PREVIEW','Recognize a displayed second-derivative matrix as future quadratic data',{'first_mention':'c3s6-subsec-hessian-preview','first_explanation':'c3s6-subsec-hessian-preview'},'Explicit preview, no required use here. Derivative subscripts are not yet defined; optional signposting improvement only (U07).')
proof=[]
def pedge(a,b,why,status='proved dependency'):
 proof.append({'source':a,'target':b,'scope':'proof','reason':why,'status':status,'source_evidence':ref(a) if a in idx else None,'target_evidence':ref(b) if b in idx else None})
pedge('c2s6-def-2x2-determinant','c3s4-thm-area-scaling-plane','Direct coordinate expansion, not integration.')
pedge('c2s6-def-3x3-determinant','c3s4-thm-volume-scaling-space','Independent trilinear basis expansion, six signed terms.')
pedge('c3s4-def-determinant-general','c3s4-thm-determinant-product','Permutation/alternating multilinear expansion gives product in everydimension.')
pedge('c3s4-thm-determinant-product','c3s4-cor-determinant-invertibility','Inverseproduct forcesdetnonzero.')
pedge('sec-1-linear-independence-and-bases','c3s4-cor-determinant-invertibility','Exchange lemma at396–408 gives n independent vectors spanningRn, no dimension circularity.')
pedge('c2s4-thm-cauchy-schwarz','c2s4-cor-triangle-inequality','Expand squarednorm and use dotbound.')
pedge('c5s2-thm-differentiation-rules','c5s4-thm-curvature-formula-in-space','Differentiate sigmaT, takecross withvelocity, useorthogonality.')
pedge('c5s4add-thm-frenet-serret','c5s4add-thm-torsion-from-parameter','Only derivativeofN contributes theBcomponent; dividepositive normcrosssquared.')
pedge('ENTRY','c5s4add-thm-torsion-detects-planarity','Continuous ±b-valued function on an interval is constant by one-variable IVT; derivativezero impliesconstant by MVT.')
pedge('ENTRY','c7s2-thm-gradient-formula','Coordinate increments and one-variableMVT prove the gradient formula before Ch8, avoiding a chain-rulecycle.')
pedge('c7s3-def-differentiability-scalar-fields-rn','c8s2-thm-matrix-chain-rule','Compose remainders and use locally supplied finite matrixnormbound.')
pedge('c8s5-thm-inverse-function','c8s6-thm-ift-plane-curve','Augmentedmap(x,F) gives localgraph existence.', 'supplied theorem dependency')
pedge('c8s5-thm-inverse-function','c8s6-thm-ift-surface','Augmentedmap(x,y,F) gives localgraph existence.', 'supplied theorem dependency')
pedge('c5s2-def-regular-grid-point','c15s1-thm-tangent-plane-to-a-parametrized-surface','Explicit deferral of tangent-sheet justification; root auditor verifies destination.', 'deferred proof destination outside assigned scope')
graphs={'snapshot':SHA,'learning_edges':learning,'proof_edges':proof,'support_nodes':support_nodes,'supplied_roots':[{'id':'ENTRY','scope':'algebra, trigonometry, ordinary single-variable limits/continuity/derivatives/MVT/FTC/substitution, as declared by audit reader contract'},{'id':'c6s4-thm-extreme-value-theorem','evidence':ref('c6s4-thm-extreme-value-theorem'),'status':'explicitly supplied without proof'},{'id':'c8s5-thm-inverse-function','evidence':ref('c8s5-thm-inverse-function'),'status':'existence and C1smoothness supplied without proof'}],'missing_supports':[{'capability':'finite-subcover compactness','scope':'Not supplied in Chapters1–8; 6.4 EVT alone insufficient. Root verifies first needed use.'},{'capability':'bounded sequence has convergent subsequence in closed bounded domain','scope':'Not supplied in Chapters1–8; root/sibling verifies later proof use.'},{'capability':'relative open/closed and connected-space clopen criterion','scope':'Not supplied in Chapters1–8; colloquial connected pictures and interval continuity are narrower.'},{'capability':'arbitrary three-covector wedge / graded algebra','scope':'Not supplied by the fixed coordinate3-form definition in2.7; two-covector algebra is supplied.'}]}
def dump(n,obj):(OUT/n).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf8')
dump('concepts.json',concepts);dump('graphs.json',graphs);dump('task-witnesses.json',rows);dump('candidate-dispositions.json',exclusions)
coverage=[]
for n,s in sorted(secs.items()):
 relevant=[r for r in rows if r['evidence']['section_order']==n]
 graphics=[x for x in nodes if x.get('section_order')==n and x.get('role') in ['latex-image','asymptote','image','figure']]
 f=[r['verdict'] for r in relevant if r['verdict'].startswith('FND-')]
 coverage.append({'section_id':s['section_id'],'evidence':ev(s),'semantic_read':True,'support_verified':True,'support_limitations':f+(['5.2 tangent-sheet theorem explicitly deferred; later destination checked by root.'] if n==31 else [])+(['EVT supplied unproved, not a generalcompactness toolkit.'] if n==40 else [])+(['Inverse existence/smoothness supplied unproved.'] if n==54 else []),'task_witnesses_complete':True,'formal_tasks':counts[n],'additional_task_witnesses':len(relevant)-counts[n],'graphics_review':{'source':'read with captions, coordinate formulas, labels, and implementation','rendered':'not reviewed by this worker'},'unresolved':[]})
for path in ['source/main.ptx','source/docinfo.ptx','source/frontmatter.ptx']+[str(p.relative_to(ROOT)).replace('\\','/') for p in sorted((ROOT/'source/chapters').glob('ch0[1-8]*/*.ptx'))]:
 p=ROOT/path;tree=E.parse(str(p));identity=tree.getroot().get('{http://www.w3.org/XML/1998/namespace}id') or path
 coverage.append({'section_id':identity,'path':path,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'semantic_read':True,'support_verified':True,'support_limitations':['Wrapper/order or frontmatter, not a mathematical proof root.'],'task_witnesses_complete':True,'graphics_review':{'source':'none','rendered':'not applicable'},'unresolved':[]})
dump('coverage.json',coverage)
lines=['# Foundations exercise dependency witnesses','',f'Snapshot `{SHA}`. All442 formal tasks have manually written solution witnesses. Required untagged project tasks are expanded below. Support IDs resolve in `graphs.json`/`concepts.json` or the global ID index. `local-support:` is the exact preceding local exposition interval; `task-scaffold:` records given data or a supplied hint. ENTRY is the declared reader contract. A support edge asserts only the capability used in that row, not every claim anywhere in a cited section.','', '| Task and source | Solution witness | Earlier/local support IDs | Verdict |','|---|---|---|---|']
for r in rows:
 e=r['evidence'];loc=f"{e['path']}:{e['lines'][0]}";outline=r['solution_outline'].replace('|','\\|').replace('\n',' ')
 lines.append(f"| `{r['task_id']}` ({loc}) | {outline} | "+'; '.join('`'+s+'`' for s in r['support_ids'])+f" | {r['verdict']} |")
lines+=['','## Candidate dispositions','', '| Candidate | Disposition |','|---|---|']
for e in exclusions:lines.append('| `'+e['task_id']+'` | '+e['disposition']+' |')
(OUT/'exercise-checks.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
print(json.dumps({'sections':len(secs),'formal_witnesses':442,'all_witnesses':len(rows),'candidates_classified':len(exclusions),'concepts':len(concepts),'learning_edges':len(learning),'proof_edges':len(proof)}))
