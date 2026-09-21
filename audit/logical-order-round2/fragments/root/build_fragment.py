from pathlib import Path
from collections import Counter
import csv,json
P=Path(__file__).resolve().parents[2]; HERE=Path(__file__).resolve().parent
I=json.loads((P/'id-index.json').read_text(encoding='utf-8')); INV=json.loads((P/'inventory.json').read_text(encoding='utf-8')); T=json.loads((P/'task-inventory.json').read_text(encoding='utf-8')); N=json.loads((P/'nodes.json').read_text(encoding='utf-8'))
SNAP=INV['snapshot']
def selected(path):return any('/ch'+str(k)+'-' in path for k in range(10,14))
def ev(key,lines=None):
 d={k:v for k,v in I[key].items() if k in ['snapshot','path','sha256','lines','xml_id','node_id','section_id','section_order','occurrence','xpath','order']}
 if lines:d['lines']=list(lines)
 return d
def save(name,data):(HERE/name).write_text(json.dumps(data,indent=2,ensure_ascii=False),encoding='utf-8')
rows={}
for k in range(10,14):
 for r in csv.DictReader((HERE/f'ch{k}-witnesses.tsv').open(encoding='utf-8-sig'),delimiter='\t'):
  r['support_evidence']=[ev(x) for x in r.pop('support_ids').split(',')];r['support']=[x['xml_id'] for x in r['support_evidence']];r['verdict']=r.pop('status');rows[r['task_key']]=r
extras={
'c10s8-worked-review-example-drawing-the-region':('x ranges0..2; y ranges x^2..2x; integral of y is32/15.','c10s4-subsec-drawing-the-region'),
'c10s8-worked-review-example-sprinkler':('Integral 2pi integral0..2 (10-r)r dr=104pi/3; divide by4pi gives26/3.','c10s5-thm-double-integrals-polar'),
'c11s7-example-wedge':('Integrate1+z from0..4-x-y, then x0..2,y0..1, obtaining35/3.','c11s2-thm-triple-integral-z-simple'),
'c11s7-example-round-tank':('Integrate(1+r)r over z0..3+r/2,r0..2,theta0..2pi:104pi/3.','c11s3-subsec-choosing-bounds'),
'c11s7-example-spherical-cone':('Angular factor pi and radial integral integral0..2 rho^3 d rho=4 give C=1/(4pi); probability rho<=1 is1/16.','c11s4-subsec-volume-element'),
'c12s7-subsec-slanted-window':('Inverse x=(u+v)/2,y=(u-v)/2 has absolute determinant1/2; integrate u on[1,3]x[0,2] to obtain4.','c12s3-thm-change-of-variables-plane'),
'c12s7-subsec-curved-plate':('u=xy,v=y/x gives inverse determinant1/(2v); mass integral1..4 u du times integral1..3 dv/(2v)=15log(3)/4.','c12s3-thm-change-of-variables-plane'),
'c12s7-subsec-stretched-ball':('Scale x=2u,y=3v,z=w, determinant6, then spherical integral6*4pi integral0..1(1+rho^2)rho^2 d rho=64pi/5.','c12s4-thm-change-of-variables-space')}
for key,(outline,support) in extras.items():rows[key]={'task_key':key,'outline':outline,'support':[support],'support_evidence':[ev(support)],'verdict':'worked example; supported'}
ts=[]
for t in [x for x in T if selected(x['path'])]:
 key=t['task_key'];lookup=t['xml_id'] or key
 if lookup in rows:r=rows[lookup].copy()
 else:
  assert t['kind']=='directive_candidate',(t['node_id'],t['kind'])
  candidates=[(k,v) for k,v in rows.items() if k in I and I[k]['path']==t['path'] and I[k]['lines'][0]<=t['lines'][0]<=I[k]['lines'][1]]
  if candidates:
   k,v=min(candidates,key=lambda kv:I[kv[0]]['lines'][1]-I[kv[0]]['lines'][0]);r={'task_key':key,'outline':'Duplicate/local instruction within '+k+'. '+v['outline'],'support_evidence':v['support_evidence'],'support':v['support'],'verdict':'covered instruction'}
  else:
   k=t['nearest_id'];r={'task_key':key,'outline':'Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: '+t['text'][:350],'support':[k],'support_evidence':[ev(k)],'verdict':'not a separate assessment; local exposition'}
 r.update({k:t[k] for k in ['node_id','path','lines','xml_id','section_id','role','student_status','kind']});r['inventory_task_key']=key;r['candidate_status']=t['kind'];ts.append(r)
 if t['node_id']=='n024554':
  r['outline']='Use the earlier bounded-square Fubini/disk comparison to justify squaring the Gaussian integral; later scaling/normalization parts are not needed for this instruction.'
  r['support']=['c10s7-subsec-gaussian-integral','c12s7-subsubsec-project-part1'];r['support_evidence']=[ev(x) for x in r['support']]
 if t['node_id']=='n026740':
  r['outline']='Parametrize the four rectangle edges in positive orientation and pair -y dx+x dy with their velocities; contributions0,ab,ab,0 sum2ab. Circle/polygon project parts are not prerequisites.'
  r['support']=['c13s3-def-work-integral','c13s4-def-pullback-1-form'];r['support_evidence']=[ev(x) for x in r['support']]
assert all(t['kind']!='formal' or t['task_key'] in rows for t in ts)
manual=[
('c10s8-project-part-4',[(583,585,'Draw4x3 equal cells over[0,8]x[0,6].'),(586,591,'Sum12 readings39.7, multiply by cell area4:158.8.'),(592,598,'1cm*1km^2=10000m^3, so1588000m^3.'),(599,601,'Mean158.8/48=3.30833cm.'),(602,604,'Connect comparable readings in a contour sketch, with maximum near(5,3).'),(605,610,'A peak between sensors can be missed; midpoint data do not bound that error without further information.')],'c10s8-project-estimating-rainfall'),
('c11s7-project-what-to-hand-in',[(793,795,'Describe Cartesian inside-center counting, meridional cylindrical sums and spherical shell sums.'),(796,798,'Use supplied midpoint finite sums at N=4,8,16,32; formulas need only finite loops/arithmetic.'),(799,804,'Subtract4pi/3 from each estimate and take absolute value.'),(805,807,'Compare measured errors for these N; spherical has the smallest errors in displayed table. No universal asymptotic theorem is required.'),(808,813,'Curved coordinate cells match the boundary and reduce partial-cell mismatch.')],'c11s7-project-volume-formulas'),
('c12s7-subsubsec-project-handin',[(943,945,'The definite integral can be evaluated by symmetry and a limit without finding an elementary antiderivative.'),(946,948,'Square bounded integrals and use bounded-square Fubini; squeeze with inscribed/circumscribed disks before taking limits.'),(949,951,'Polar integral over disk radiusR is pi(1-exp(-R^2)); limit pi, positive square root sqrt(pi).'),(952,958,'u=sqrt(a)x gives sqrt(pi/a), a>0.'),(959,964,'Take a=1/(2sigma^2), sigma>0; normalizing constant1/(sigma sqrt(2pi)).'),(965,970,'Squaring makes the integrand exp(-(x^2+y^2)), radial, so polar separates the angle and a one-variable substitution.')],'c12s7-subsec-project-gaussian-integral')]
for container,items,parent in manual:
 if parent not in rows:
  choices=[k for k in rows if 'project' in k and I[k]['path']==I[container]['path']];assert len(choices)==1,choices;parent=choices[0]
 for j,(a,b,outline) in enumerate(items,1):
  ts.append({'task_key':container+'-deliverable-'+str(j),'path':I[container]['path'],'lines':[a,b],'xml_id':None,'section_id':I[container]['section_id'],'node_id':None,'role':'li','kind':'manually_identified_project_deliverable','student_status':'default_required','outline':outline,'verdict':'supported by announced project scaffold','support_evidence':rows[parent]['support_evidence'],'support':rows[parent]['support'],'source_evidence':ev(container,(a,b))})
save('task-witnesses.json',{'snapshot':SNAP,'tasks':ts})
edges=[]
for t in ts:
 for s in t['support_evidence']:
  edges.append({'use':{'snapshot':SNAP,'path':t['path'],'lines':t['lines'],'xml_id':t['xml_id'],'task_key':t['task_key']},'capability':s['xml_id'],'support':s,'assessment_status':t['student_status'],'verdict':t['verdict'],'witness':t['outline'],'local_scaffold':'hint' not in s.get('xpath','')})
concepts=[]
def concept(key,name,type_,support,use,rule,late=None,early=None):
 s=ev(support) if support else None
 concepts.append({'concept_id':key,'name':name,'type':type_,'scope':'Main-text Chapters10-13 route; earliest sufficient support checked in earlier chapters where relevant. Role locations describe this route unless explicitly global.','first_mention':ev(early or support) if (early or support) else None,'first_concrete_explanation':s,'first_formal_definition':s,'first_demonstrated_computation':s,'first_justified_general_rule':s,'first_required_use':ev(use),'later_generalizations':[ev(x) for x in late or []],'rules_available':[rule],'prerequisite_concepts':[],'source_evidence':[x for x in [s,ev(use)] if x],'confidence':'verified','role_note':'A support container may include both explanation and computation; the source range, not a bare title, supplies those roles. A supplied rule is not claimed fully proved.'})
specs=[
('integral.riemann2','Rectangle Riemann sums','scalar function x partition -> scalar approximation','c10s2-subsec-partitions-sample-points','c10s8-project-estimating-rainfall','Weighted sample sum and refinement; no unstated probabilistic sampling.'),
('integral.polar','Polar integral substitution','continuous scalar density -> scalar integral','c10s5-thm-double-integrals-polar','c11s3-subsec-choosing-bounds','Supplied once-covering polar theorem, with sector-area motivation.'),
('integral.slice3','Vertical slicing','continuous scalar function on z-simple solid -> iterated integral','c11s2-thm-triple-integral-z-simple','c11s7-example-wedge','Supplied Fubini/slicing under region hypotheses.'),
('integral.cylindrical','Cylindrical scalar substitution','scalar density -> integral with weight r','c11s3-subsec-choosing-bounds','c11s7-example-round-tank','Formula available; exact integration justification gap ROOT-02.'),
('integral.spherical','Spherical scalar substitution','scalar density -> integral with weight rho^2 sin phi','c11s4-subsec-volume-element','c11s7-example-spherical-cone','Formula available; exact integration justification gap ROOT-02.'),
('wedge.three_covectors','Three arbitrary covectors','(V*)^3 -> Alt^3(V)','c12s5-subsec-pulling-back-volume-elements','c11s3-subsec-volume-element','Determinant definition, multilinearity, alternating/grouping rule; earlier use ROOT-01.'),
('integral.change_variables2','General planar substitution','C1 one-to-one parameter map x density -> equal integrals','c12s3-thm-change-of-variables-plane','c12s7-subsec-slanted-window','Supplied theorem, proof-idea ceiling, absolute Jacobian.'),
('integral.change_variables3','General spatial substitution','C1 one-to-one parameter map x density -> equal integrals','c12s4-thm-change-of-variables-space','c12s7-subsec-stretched-ball','Supplied theorem, proof-idea ceiling, absolute Jacobian.'),
('curve.scalar_integral','Scalar line integral','density x traversed curve -> scalar','c13s2-def-line-integral-scalar-function','checkpoint-13-2-speed-factor-meaning','Speed weight; reversal invariant, repeated traversal counted.'),
('curve.work_integral','Directed work','vector field x oriented traversed curve -> scalar','c13s3-def-work-integral','c13s8-project','Dot velocity, sign reversal.'),
('form.pullback1','Curve pullback of a1-form','1-form on target ->1-form on parameter interval','c13s4-def-pullback-1-form','c13s8-project','Coefficients compose with curve; differentials differentiate parameterization.'),
('potential.ftli','Fundamental theorem of line integrals','C1 potential x curve -> endpoint difference','thm-c13s5-ftli','checkpoint-13-5-closed-loop-zero','Chain rule plus ordinary FTC prove forward implication.'),
('analysis.parameter_integral','Differentiate fixed interval integral','jointly continuous q,q_x -> differentiable parameter integral','c13s6-lem-parameter-integral','c13s6-thm-curl-test-rectangle','Valid lemma, finite-subcover support gap ROOT-03.'),
('potential.plane_rectangle','Closed plane form on rectangle has potential','C1 closed1-form -> local/global rectangular potential','c13s6-thm-curl-test-rectangle','checkpoint-13-6-direction-of-the-arrow','Uses parameter-integral lemma and FTC.'),
('potential.simply_connected','Global plane potential','C1 closed1-form on open simply connected domain -> potential','c13s6-thm-curl-test-simply-connected','checkpoint-13-6-what-the-hole-feels-like','Supplied theorem with proof deferred to17.5; missing compactness premise there.'),
('analysis.finite_subcover','Finite-subcover and path-subdivision principles','open cover of compact Euclidean set -> finite subcover / uniform scale',None,'thm-c13s5-path-independence-potential','No sufficient prior teaching found; ROOT-03. Closed-bounded gloss and EVT do not supply this capability.')]
for args in specs:concept(*args)
save('concepts.json',{'snapshot':SNAP,'concepts':concepts})
proofs=[
('thm-c13s5-ftli','c8s1-thm-chain-rule-curve','ordinary chain rule; integrate derivative by entry FTC'),
('c13s6-thm-curl-test-rectangle','c13s6-lem-parameter-integral','differentiate horizontal/vertical primitive'),
('c13s6-thm-exact-implies-closed-plane','c9s3-thm-equality-of-mixed-partials','C1 coefficients make potential C2'),
('c13s2-thm-scalar-line-integral-reparametrization','c8s1-thm-chain-rule-curve','chain rule and ordinary substitution, absolute speed'),
('thm-c13s5-path-independence-potential',None,'compact-path finite subdivision missing; other difference-quotient steps are local FTC'),
('c13s6-lem-parameter-integral',None,'finite-subcover uniformity missing; remaining MVT estimate valid')]
save('graphs.json',{'snapshot':SNAP,'learning_edges':edges,'proof_edges':[{'result':ev(a),'support':ev(b) if b else None,'inference':c,'status':'supported' if b else 'ROOT-03 missing supplied premise'} for a,b,c in proofs],'supplied_roots':[ev(x) for x in ['c10s5-thm-double-integrals-polar','c11s2-thm-triple-integral-z-simple','c12s3-thm-change-of-variables-plane','c12s4-thm-change-of-variables-space']],'missing_supports':['ROOT-01','ROOT-02','ROOT-03'],'graph_ceiling':'Human-verified capability and task edges; not a formal proof verifier. All source proof arguments were read; explicit edges concentrate on non-entry results and disputed/deferred dependencies.'})
secs=[]
for s in INV['sections']:
 if not selected(s['path']):continue
 problems=[]
 if s['id'] in ['sec-11-cylindrical-coordinates-in-integrals','sec-11-spherical-coordinates-in-integrals']:problems=['ROOT-01','ROOT-02']
 if s['id'] in ['sec-13-conservative-vector-fields-and-exact-1-forms','sec-13-curl-tests-in-the-plane-and-in']:problems=['ROOT-03']
 secs.append({**s,'section_id':s['id'],'inventoried':True,'mechanically_scanned':True,'semantic_read':True,'support_verified':not problems,'support_scope':'Full sequential source read; proof ceilings and missing support are recorded rather than certified away.','task_witnesses_complete':True,'task_witness_rows':sum(t['section_id']==s['id'] for t in ts),'independent_challenge_completed':False,'graphics_review':{'source':True,'rendered':False},'unresolved':problems})
save('coverage.json',{'snapshot':SNAP,'sections':secs,'wrappers':[f for f in INV['files'] if selected(f['path']) and not '/sections/' in f['path']],'remaining':[]})
lines=['# Chapter10–13 task witnesses','','Each row cites the original source task and exact source support. Worked examples and duplicate instructions remain classified separately from assessments.','']
for t in ts:
 lines += [f"## {t['task_key']}",f"Source: `{t['path']}:{t['lines'][0]}–{t['lines'][1]}`; {t['verdict']}.",t['outline'],'Support: '+', '.join(f"`{s['xml_id']}` (`{s['path']}:{s['lines'][0]}–{s['lines'][1]}`)" for s in t['support_evidence']), '']
(HERE/'exercise-checks.md').write_text('\n'.join(lines),encoding='utf-8')
print('ROOT sections',len(secs),'tasks/dispositions',len(ts),'concepts',len(concepts),'learning_edges',len(edges))
