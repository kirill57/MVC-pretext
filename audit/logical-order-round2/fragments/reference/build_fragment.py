from pathlib import Path
from lxml import etree as E
import json,hashlib
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
AUDIT=ROOT/'audit/logical-order-round2'
SNAP='9a9d110af839b539fe598de66ecc4320a4126af4'
INDEX=json.loads((AUDIT/'id-index.json').read_text(encoding='utf-8'))
INV=json.loads((AUDIT/'inventory.json').read_text(encoding='utf-8'))
TASKS=json.loads((AUDIT/'task-inventory.json').read_text(encoding='utf-8'))
X='{http://www.w3.org/XML/1998/namespace}id'
def assigned(p):return 'ch09-' in p or any('/app'+c+'-' in p for c in 'ABCDE')
def ev(key,lines=None):
 d={k:v for k,v in INDEX[key].items() if k in ('snapshot','path','sha256','lines','xml_id','node_id','section_id','section_order','occurrence','xpath')}
 if lines:d['lines']=list(lines)
 return d
SUP={
 'ENTRY':ev('how-to-read',(29,43)),
 'DOT':ev('c2s4-algebraic-definition-and-first-examples',(53,76)),
 'QUAD':ev('c3s6-subsec-form-to-matrices',(14,83)),
 'QUADSIGN':ev('c3s6-thm-2x2-quadratic-form-test'),
 'GRAD':ev('c7s2-subsec-gradient-formula',(163,305)),
 'STEEPEST':ev('c7s2-thm-steepest'),
 'CHAIN':ev('c8s1-thm-chain-rule-curve'),
 'IFT2':ev('c8s6-thm-ift-plane-curve'),
 'IFT3':ev('c8s6-thm-ift-surface'),
 'IFTWARN':ev('c8s6-why-the-hypotheses-matter',(477,541)),
 'IVT':ev('c8s5-thm-inverse-function'),
 'EVTEARLY':ev('c6s4-thm-extreme-value-theorem'),
 'LEVEL':ev('c9s1-subsec-gradient-normal-level-curve',(109,185)),
 'SURFACE':ev('c9s1-thm-gradient-normal-level-surface'),
 'FLOW':ev('c9s1-subsec-orthogonality-flow-lines-contours',(340,391)),
 'EXTREMA':ev('c9s2-def-local-max-min'),
 'SADDLE':ev('c9s2-saddle-points',(113,212)),
 'FERMAT':ev('c9s2-thm-fermat',(229,262)),
 'CRITICAL':ev('c9s2-def-critical-point'),
 'BOUNDARY':ev('c9s2-ex-interior'),
 'HESSINTRO':ev('c9s3-subsec-summit-we-already-met'),
 'PARTIAL2':ev('c9s3-def-second-partial-derivatives'),
 'MIXED':ev('c9s3-thm-equality-of-mixed-partials',(219,254)),
 'MIXFAIL':ev('c9s3-ex-mixed-partials-can-fail'),
 'HESS':ev('c9s3-def-hessian-matrix-two-variables'),
 'TAYLORINTRO':ev('c9s3-subsec-quadratic-approximation',(463,478)),
 'TAYLOR':ev('c9s3-thm-second-order-approximation',(576,643)),
 'QDEFINITE':ev('c9s4-def-definite-indefinite'),
 'QBOUND':ev('c9s4-thm-second-derivative-test',(321,348)),
 'DISCRIM':ev('c9s4-two-variable-determinant-shortcut',(193,248)),
 'TEST':ev('c9s4-thm-second-derivative-test'),
 'NONCRITICAL':ev('c9s4-why-critical-point-condition'),
 'DEGENERATE':ev('c9s4-degenerate-hessians',(523,583)),
 'CONSTRAINTGEOM':ev('c9s5-subsec-why-gradient-perpendicular',(135,166)),
 'KERNEL':ev('c9s5-subsec-why-gradient-perpendicular',(186,201)),
 'LAGRANGE':ev('c9s5-thm-lagrange-one-constraint'),
 'LAGRANGE2':ev('c9s5-thm-lagrange-two-constraints'),
 'SINGULAR':ev('c9s5-ex-constraint-gradient-nonvanishing'),
 'PLANE':ev('c9s5-ex-closest-point-on-plane'),
 'EVT':ev('c9s5-thm-extreme-value'),
 'COURTYARD':ev('c9s5-ex-semicircular-courtyard'),
 'MULTIPLIER':ev('c9s5-subsec-interpreting-the-multiplier',(623,659)),
 'ENDPOINT':ev('c9s6-multiplier-misses-endpoint',(134,168)),
 'RECTANGLE':ev('c9s7-subsec-worked-rectangle'),
 'ELLIPSE':ev('c9s7-subsec-worked-constraint'),
 'LS':ev('c9s7-subsec-least-squares'),
 'BOX':ev('c9s7-subsec-container'),
}
ROWS={}
def row(key,outline,support,verdict='supported',note=''):
 ROWS[key]={'outline':outline,'support':support.split(),'verdict':verdict,'note':note}
row('checkpoint-9-1-gradient-perp-level-curve','Differentiate f(r(t))=c; chain rule gives grad f dot r prime=0, and a nonzero gradient is perpendicular to the tangent.','CHAIN LEVEL GRAD')
row('checkpoint-9-1-gradient-normal-tangent-plane','For a regular level surface with nonzero gradient, all tangent vectors lie in ker dF, a plane with equation grad F(p) dot (x-p)=0. As written F=z^2 at z=0 has a smooth plane but gradient zero; no normal direction follows.','CHAIN IFT3','scope-gap REF-01','The later SURFACE theorem supplies the omitted nonzero hypothesis; it is not supplied in this checkpoint.')
row('checkpoint-9-1-steepest-path-crosses-contours','At a nonstationary point velocity is parallel to plus/minus grad f; level tangents are orthogonal. The dot-product maximum over unit directions is norm grad f.','LEVEL STEEPEST FLOW')
row('checkpoint-9-2-zero-gradient-not-enough','For x^2-y^2 the gradient is zero at 0, but x-axis values rise and y-axis values fall. First order does not classify.','SADDLE')
row('checkpoint-9-2-why-gradient-zero','Freeze all but xi; the one-variable slice has an interior extremum so its derivative f_xi is zero. Do this for every i.','FERMAT ENTRY')
row('checkpoint-9-2-why-boundary-separate','The increasing direction can leave the allowed domain; x on the disk peaks at (1,0) with nonzero gradient. Fermat requires an interior point.','BOUNDARY FERMAT')
row('checkpoint-9-3-symmetry-from-equal-mixed-partials','The two off-diagonal entries are equal exactly when reflection across the diagonal leaves the 2x2 Hessian unchanged. No theorem about equality of mixed partials is needed to answer this conditional question.','QUAD HESSINTRO')
row('checkpoint-9-3-what-the-hessian-captures','Second partials record change of slope; their quadratic expression distinguishes bending up/down and mixed-direction behavior even when linear slope vanishes.','PARTIAL2 HESS HESSINTRO')
row('checkpoint-9-3-hessian-as-second-order-term','Multiply (u,v)H(u,v)^T to obtain f_xx u^2+(f_xy+f_yx)uv+f_yy v^2; C2 gives equal mixed entries and the displayed local Taylor model.','QUAD MIXED TAYLORINTRO')
row('checkpoint-9-4-quadratic-decides','For a positive definite q on the unit circle, EVT gives m>0 and homogeneity gives q(h)>=m norm(h)^2. TAYLOR makes the remainder less than m norm(h)^2/4; negative q is analogous. For indefinite q choose two fixed opposite-sign directions.','TAYLOR QDEFINITE EVTEARLY QUADSIGN','supported discovery','Full proof outline reconstructs the bound with already supplied EVT; the source asks an intuitive explanation and later QBOUND makes it explicit.')
row('checkpoint-9-4-delta-and-fxx','Completing the square gives A(u+Bv/A)^2+(Delta/A)v^2. Delta>0 makes both coefficients share the sign of A; A chooses minimum versus maximum.','DISCRIM')
row('checkpoint-9-4-why-zero-is-inconclusive','x^4+y^4 has a strict minimum whereas x^4-y^4 changes sign; both have zero Hessian. A null quadratic direction leaves higher-order behavior unreported.','DEGENERATE')
row('checkpoint-9-5-gradients-parallel','At a regular planar constraint, both gradients annihilate its tangent and the nonzero constraint gradient spans the normal line. But g=(x^2+y^2-1)^2 defines a smooth circle with grad g=0; f=x has a constrained maximum at (1,0), so no lambda works.','CONSTRAINTGEOM IFT2 IFTWARN','scope-gap REF-01','The nonzero-gradient hypothesis arrives explicitly in the paragraph after the checkpoint and in LAGRANGE.')
row('checkpoint-9-5-compactness-attains-extrema','If extrema exist and the list exhausts interior, regular-boundary and endpoint/singular candidates, comparison captures them. Compactness alone does not assert the list is finite or exhaustive.','EVT LAGRANGE FERMAT')
row('checkpoint-9-5-what-lambda-measures','In the displayed circle family M(c)=10 sqrt(c), M prime(c)=5/sqrt(c)=lambda at the maximizing branch; lambda measures marginal best value per unit constraint level. This requires a differentiable extremizing branch in a general problem.','MULTIPLIER ENTRY','supported in displayed family','Do not read the explanatory answer as a theorem that every optimal-value function is differentiable.')
row('checkpoint-9-6-zero-gradient-no-extremum','The smooth saddle x^2-y^2 has vanishing first-order change but increases on one axis and decreases on the other.','SADDLE')
row('checkpoint-9-6-multiplier-misses-boundary','The line segment has tangent (1,0) at its endpoints; at x=1 only the decreasing direction remains feasible. The restriction f(t,0)=t has a one-sided endpoint maximum without derivative zero. Corners require checking each feasible piece.','ENDPOINT FERMAT','misleading hint REF-02','Prompt is answerable from the segment example; its hint wrongly directs attention to nonexistence of a tangent.')
row('checkpoint-9-6-unequal-mixed-partials','The mixed-partial theorem requires existence nearby and continuity at the point; unequal values imply at least one of these hypotheses fails. For the given rational example continuity fails.','MIXED MIXFAIL')
cc={
'gradient-normal':('Differentiate the constant level relation; chain rule yields orthogonality at a regular point.','LEVEL CHAIN'),
'tangent-line':('f_x(a,b)(x-a)+f_y(a,b)(y-b)=0 at the regular smooth level curve.','LEVEL IFT2'),
'tangent-plane':('F_x(a,b,c)(x-a)+F_y(a,b,c)(y-b)+F_z(a,b,c)(z-c)=0 at the regular smooth level surface.','SURFACE IFT3'),
'interior-extremum':('Each coordinate slice has an interior extremum; each partial is zero.','FERMAT'),
'not-guarantee':('Use x^2-y^2: opposite signs on axes despite zero gradient.','SADDLE'),
'hessian-info':('The Hessian stores all second partials and the quadratic part governing changes of slope.','HESS TAYLOR'),
'discriminant':('Delta is the determinant of the symmetric 2x2 Hessian; its sign distinguishes definite, indefinite, and degenerate quadratic parts.','DISCRIM'),
'positive-definite':('h^T H h>0 for every nonzero h; together with C2 critical-point hypotheses this gives strict local minimum.','QDEFINITE TEST'),
'require-critical':('Otherwise a linear term dominates: x+x^2+y^2 is not minimal at zero despite H=2I.','NONCRITICAL'),
'zero-discriminant':('The Hessian has a null direction and x^4 plus/minus y^4 show different higher-order classifications.','DEGENERATE'),
'constrained-condition':('Only tangent derivatives must vanish; both objective and regular constraint gradients are normal to allowed motion.','LAGRANGE'),
'singular-constraint':('If grad g=0, lambda grad g cannot equal a nonzero objective gradient even when the feasible set has an extremum.','SINGULAR'),
'endpoints-corners':('Two-sided tangent motion used by Fermat is unavailable, so extrema on these boundary pieces require direct checks.','ENDPOINT FERMAT'),
'differential-form':('dg(v)=0 for an allowed tangent implies df(v)=lambda dg(v)=0; both covectors annihilate allowed first-order motions.','KERNEL LAGRANGE')}
for k,(v,s) in cc.items():row('c9s7-cc-'+k,v,s)
sk={
'tangent-line':('grad f(1,1)=(3,3), giving x+y=2.','LEVEL'),
'tangent-plane':('grad F(1,1,sqrt(2))=(2,4,6sqrt(2)); plane x+2y+3sqrt(2)z=9.','SURFACE'),
'h-critical':('Solve 4-2x=0,-1-4y=0: (2,-1/4). H=diag(-2,-4), Delta=8, strict maximum.','FERMAT TEST'),
'f-critical':('Solve 3x^2-3=0,2y-2=0: (1,1) minimum and (-1,1) saddle, with H=diag(6x,2).','FERMAT TEST'),
'q-origin':('H=[[2,4],[4,2]], Delta=-12: saddle.','TEST'),
's-origin':('H=[[2,1],[1,4]], Delta=7 and A=2: strict minimum.','TEST'),
'x4-plus-y2':('H(0)=diag(0,2), Delta=0. Direct nonnegativity and equality only at zero prove strict minimum.','DEGENERATE'),
'x4-minus-y2':('H(0)=diag(0,-2), Delta=0; x-axis positive, y-axis negative: saddle.','DEGENERATE'),
'disk':('No interior critical point. On circle radius3, normals give points plus/minus(3/sqrt(2),3/sqrt(2)); values plus/minus3sqrt(2).','LAGRANGE EVT COURTYARD'),
'rectangle':('Write f=(x-1)^2+y^2-1. Minimum -1 at(1,0); maximum7 at(-1,2),(3,2); edge endpoints/critical points exhaust the rectangle.','RECTANGLE EVT'),
'circle-lagrange':('Solve (3,4)=lambda(2x,2y), x^2+y^2=25: points(3,4),(-3,-4), values25,-25.','LAGRANGE EVT'),
'ellipse-xy':('Equations y=2lambda x and x=8lambda y force lambda=plus/minus1/4; x=plus/minus2sqrt(2), y=plus/minus sqrt(2). Matching signs maximize xy=4; opposite signs minimize xy=-4.','LAGRANGE EVT ELLIPSE'),
'plane-closest':('Minimize x^2+y^2+z^2: 2(x,y,z)=lambda(1,1,1), sum6 gives (2,2,2). Orthogonal decomposition shows all other feasible points have larger squared distance.','LAGRANGE PLANE DOT'),
'sphere-largest':('A maximizing point is radius5 in direction(1,2,2): (5/3,10/3,10/3), value15; multiplier/EVT checks both antipodes.','LAGRANGE EVT'),
'curve-two-constraints':('The constraint gives y=-x and 2x^2+z^2=9. Thus -3<=z<=3, with extrema (0,0,plus/minus3); alternatively the two-multiplier equations produce these points.','LAGRANGE2 EVT ENTRY'),
'parabola-constraint':('Reduce f to x^2+x^4: derivative2x(1+2x^2)=0 only at0, a global minimum. grad g=(-2x,1) never zero. grad h=2(y-x^2)(-2x,1)=0 on the same parabola, so the multiplier theorem for h has no guarantee.','LAGRANGE SINGULAR IFTWARN ENTRY'),
'segment':('The smooth-line equation (1,0)=lambda(0,1) has no solution. Direct endpoint values give max1 at(1,0), min-1 at(-1,0).','ENDPOINT'),
'abs-value':('Both summands are nonnegative, so zero is strict minimum. The x difference quotient of abs(x) has different one-sided limits; gradient is undefined.','CRITICAL ENTRY'),
'classify-origin':('Gradient zero; H=diag(2,-2), determinant-4, hence saddle (also opposite signs on axes).','TEST'),
'x4-y4-4xy':('Stationarity gives y=x^3 and x=y^3, hence x^9=x with real solutions0,plus/minus1. Points(0,0),(1,1),(-1,-1). H=[[12x^2,-4],[-4,12y^2]]; det-16 at0 gives saddle, det128 at other two and A12 give strict minima.','FERMAT TEST ENTRY'),
'exponential':('Product rule makes gradient vanish at0; H(0)=2I so strict local minimum. Direct positivity of exp(x+y)(x^2+y^2) gives unique global minimum0.','FERMAT TEST ENTRY'),
'complete-square':('f=(x+y-3)^2+(y+3)^2-18; unique minimum-18 at(6,-3). H=[[2,2],[2,4]], Delta4 confirms.','QUAD TEST ENTRY'),
'mixed-partials':('Axis difference quotients give F_x(0,y)=-y and F_y(x,0)=x, so F_xy(0)=-1,F_yx(0)=1. Their nearby continuity fails.','MIXFAIL MIXED'),
'zero-hessian-min':('x^4+y^4 at0 has all second partials zero and is positive elsewhere.','DEGENERATE'),
'zero-hessian-saddle':('x^4-y^4 at0 has zero Hessian and takes both signs arbitrarily near0.','DEGENERATE')}
for k,(v,s) in sk.items():row('c9s7-sk-'+k,v,s)

# Mechanical task-candidate dispositions: worked paragraphs and generic reference imperatives.
row('n018196','Worked segment problem: endpoint values -1 and1; multiplier equation has no interior solution.','ENDPOINT','worked task, supported')
row('c9s7-subsec-worked-free-critical','Gradient equations give (1,2) minimum and(-1,2) saddle; H=diag(6x,2).','FERMAT TEST','worked task, supported')
row('c9s7-subsec-worked-rectangle','Complete squares or inspect four edges: min-6 at(2,1), max0 at(0,0),(0,2).','FERMAT EVT ENTRY','worked task, supported')
row('n018364','Compare the already displayed interior/edge values: -6 is least and0 greatest.','RECTANGLE','duplicate instruction inside worked task')
row('c9s7-subsec-worked-constraint','Multipliers on x^2+4y^2=16 give points plus/minus(2sqrt(2),sqrt(2)) and values plus/minus4sqrt(2).','LAGRANGE EVT','worked task, supported')
row('n018372','Same ellipse calculation as c9s7-subsec-worked-constraint.','LAGRANGE EVT','duplicate worked-task prompt')
row('c9s7-subsec-least-squares','E=sum(mx_i+b-y_i)^2; normal equations14m+6b=18,6m+4b=9 give m=b=9/10; H=[[28,12],[12,8]], Delta80. Residual(-1,-2,7,-4)/10 is orthogonal to(1,1,1,1) and(0,1,2,3).','LS FERMAT TEST DOT','scaffolded project, supported')
row('n018627','Report components separately witnessed in LS-deliverable rows below.','LS','project hand-in instruction')
row('c9s7-subsec-container','Set A=xy+2xz+2yz and xyz32. Multiplier equations yield x=y=2z, then(4,4,2). For a=sqrt(xy), A>=a^2+128/a; derivative sign changes only at a4, establishing global minimum48.','BOX LAGRANGE ENTRY','scaffolded project, supported')
row('n018659','Same minimization as c9s7-subsec-container; global lower bound reduces all positive dimensions, not just square bases.','BOX LAGRANGE ENTRY','duplicate project prompt')
row('n018723','Report components separately witnessed in BOX-deliverable rows below.','BOX','project hand-in instruction')
row('n042278','Generic algorithm: find roots of ax^2+bx+c using the displayed quadratic formula, then test signs on complementary intervals. No concrete exercise is posed.','ENTRY','not an assessment; reference checklist')
row('n043776','Names the radial and angular components in the displayed local unit basis; no field is supplied to decompose.','ENTRY','not an assessment; formula setup')
row('n043788','Names the cylindrical basis components; no field is supplied to decompose.','ENTRY','not an assessment; formula setup')
row('n043800','Names the spherical basis components; no field is supplied to decompose.','ENTRY','not an assessment; formula setup')

selected=[t for t in TASKS if assigned(t['path'])]
missing=[]; tasks=[]
for t in selected:
 key=t['xml_id'] or t['node_id']
 if key not in ROWS:missing.append(key);continue
 r=ROWS[key].copy();r.update({k:t[k] for k in ('node_id','path','lines','xml_id','section_id','role','student_status')});r['task_key']=key
 r['support_evidence']=[SUP[s] for s in r['support']];tasks.append(r)
assert not missing,missing
assert len([t for t in tasks if t['role']=='exercise'])==57

manual=[
 ('LS-deliverable-plot',(859,859),'Plot four supplied coordinate points and the line y=0.9x+0.9.','ENTRY LS'),
 ('LS-deliverable-E',(860,865),'Write the four squared vertical residual terms given at lines752-759.','LS'),
 ('LS-deliverable-normal-equations',(866,871),'Differentiate E in m,b to obtain14m+6b=18 and6m+4b=9.','LS FERMAT'),
 ('LS-deliverable-solution',(872,877),'Elimination gives20m=18 and then b=0.9.','LS ENTRY'),
 ('LS-deliverable-Hessian',(878,878),'H=[[28,12],[12,8]], determinant80>0 and first entry28>0.','LS TEST'),
 ('LS-deliverable-residual',(879,884),'Residual(-1,-2,7,-4)/10; dot1=(-1-2+7-4)/10=0; dotx=(-2+14-12)/10=0.','LS DOT'),
 ('LS-deliverable-explanation',(885,885),'Every change of fitted values is dm*x+db*1; bilinearity makes residual perpendicular to it. Squared-error expansion then proves the minimum.','LS DOT'),
 ('BOX-deliverable-diagram',(1031,1031),'Draw an open-top rectangular prism and label positive side lengths x,y,z.','ENTRY BOX'),
 ('BOX-deliverable-area',(1032,1037),'Add base xy and side areas2xz+2yz.','BOX ENTRY'),
 ('BOX-deliverable-volume',(1038,1043),'Multiply dimensions to write xyz=32.','BOX ENTRY'),
 ('BOX-deliverable-equations',(1044,1044),'grad A=(y+2z,x+2z,2x+2y)=lambda(yz,xz,xy).','BOX LAGRANGE'),
 ('BOX-deliverable-square',(1045,1050),'Multiply first multiplier equation by x and second by y, subtract; 2z(x-y)=0 and z>0 give x=y.','BOX ENTRY'),
 ('BOX-deliverable-height',(1051,1056),'With x=y=a, third equation gives lambda=4/a; first yields a=2z.','BOX ENTRY'),
 ('BOX-deliverable-dimensions',(1057,1057),'Constraint a^3/2=32 gives a4,z2; area48.','BOX ENTRY'),
 ('BOX-deliverable-comparison',(1058,1058),'With no top, increasing the square base saves side material until x=2z, so height is half the base side.','BOX'),
]
reviewpath=INDEX['sec-9-chapter-review-and-applications']['path']
for key,lines,outline,support in manual:
 tasks.append({'task_key':key,'node_id':None,'path':reviewpath,'lines':list(lines),'xml_id':None,'section_id':'sec-9-chapter-review-and-applications','role':'untagged_project_deliverable','student_status':'required_if_project_assigned','outline':outline,'support':support.split(),'support_evidence':[SUP[s] for s in support.split()],'verdict':'scaffolded, supported','note':'Student-facing hand-in list; retained separately from parent project.'})
(HERE/'task-witnesses.json').write_text(json.dumps({'snapshot':SNAP,'tasks':tasks},indent=2),encoding='utf-8')
md=['# Chapter 9 and Appendices A-E: task dependency witnesses','',f'Snapshot: `{SNAP}`. Fresh source reading precedes old-disposition comparison. Every one of 57 tagged Chapter 9 exercises is covered, plus all 15 untagged project hand-in items and all 15 additional root inventory candidates (worked/duplicate instructions and four non-assessment reference imperatives). Appendices A-E have no concrete required task sets. The outlines establish methods and support; they are not a full pedagogical solution manual.','', 'Support IDs below resolve to exact snapshot/path/XML-ID/line evidence in `task-witnesses.json` and `graphs.json`. ENTRY is the declared algebra/trigonometry/single-variable calculus contract; no ODE, probability or numerical prerequisite is silently imported.','', '| Task / source-line identity | Solution or dependency witness | Exact support IDs | Verdict |','|---|---|---|---|']
for t in tasks:
 loc=t['xml_id'] or f"{t['path']}:{t['lines'][0]} ({t['task_key']})"
 md.append('| '+loc+' | '+t['outline'].replace('|','\\|')+' | '+', '.join(s+':'+SUP[s]['xml_id'] for s in t['support'])+' | '+t['verdict']+(' — '+t['note'] if t['note'] else '')+' |')
md+=['','## Fully checked high-risk reasoning','','- **Positive-definite domination:** the reconstructed witness for checkpoint-9-4-quadratic-decides uses the already supplied EVT on the closed interval/circle, not a later finite-subcover theorem. The later proof at c9s4-thm-second-derivative-test makes the same bound explicit.','- **Mixed partials:** F_x(0,y)=-y and F_y(x,0)=x give the exact values -1 and +1. This says nothing against mixed-partial equality under its continuity hypotheses.','- **Nonlinear critical equations:** x^9=x has precisely the three real solutions 0,+1,-1 since x(x^8-1)=0; no complex roots are relevant. Hessian determinants are -16 and128.','- **Regular versus singular parabola representation:** y=x^2 is smooth; h=(y-x^2)^2 has zero gradient throughout that curve. Failure of the theorem for h does not assert the geometric parabola is singular.','- **Global box minimum:** for every positive x,y, write a=sqrt(xy). Then x+y>=2a and A>=a^2+128/a. This last function decreases for0<a<4 and increases for a>4 because A prime=2(a^3-64)/a^2. Equality at x=y=4,z=2 yields global area48. The task does not need AM-GM, compactness, a numerical optimizer, or an unproved symmetry assertion.','- **Least-squares global minimum:** setting changes dm,db about(0.9,0.9) gives E-E_min=14dm^2+12dm db+4db^2, positive for nonzero changes (det20). E_min=0.7. Orthogonal residual expands the same square exactly.','- **Counterexamples to underqualified checkpoints:** F=z^2 has zero gradient on the perfectly smooth plane z=0. For g=(x^2+y^2-1)^2 and f=x, the point(1,0) is a constrained maximum but grad g=0 and grad f=(1,0), so no multiplier is possible.','- **Endpoint:** f(t,0)=t on[-1,1] has derivative1 at the maximum endpoint in its smooth extension. A one-sided feasible maximum does not activate Fermat; the tangent direction still exists.','']
(HERE/'exercise-checks.md').write_text('\n'.join(md),encoding='utf-8')

learning=[]
for t in tasks:
 for s in t['support']:
  learning.append({'use':{'task_key':t['task_key'],'path':t['path'],'xml_id':t['xml_id'],'lines':t['lines'],'node_id':t['node_id']},'capability_support_id':s,'support':SUP[s],'scope':t['student_status'],'availability':t['verdict'],'note':t['note']})
proof_specs=[
 ('c9s1-thm-gradient-normal-level-curve',['CHAIN','IFT2'],'Chain rule proves normality conditional on a smooth nonzero tangent; IFT supplies local existence under C1 regularity.'),
 ('c9s1-thm-gradient-normal-level-surface',['CHAIN','IFT3'],'Scalar IFT gives graph; graph tangent vectors span ker dF. Nonzero gradient required.'),
 ('c9s2-thm-fermat',['ENTRY'],'One-variable Fermat on coordinate slices; total differential equivalence separately requires differentiability.'),
 ('c9s3-thm-equality-of-mixed-partials',['ENTRY','PARTIAL2'],'Labeled proof idea: twice apply one-variable MVT to rectangle increment; continuity at target supplies limiting equality.'),
 ('c9s3-thm-second-order-approximation',['CHAIN','ENTRY','MIXED'],'Labeled proof idea with explicit integral remainder and uniform entrywise Hessian bound; no finite-cover lemma needed.'),
 ('c9s4-thm-second-derivative-test',['TAYLOR','DISCRIM','EVTEARLY'],'Unit-circle minimum is positive and remainder is uniformly smaller; indefinite case uses two fixed directions.'),
 ('c9s5-thm-lagrange-one-constraint',['IFT2','IFT3','CHAIN','KERNEL','FERMAT'],'IFT identifies local tangent kernel; every tangent is realized by graph curves. Kernel inclusion handles df=0.'),
 ('c9s5-thm-lagrange-two-constraints',['IVT','CHAIN','FERMAT'],'Precisely stated theorem supplied for use. Geometric motivation only; full joint-constraint parametrization proof is not written locally.'),
 ('c9s5-thm-extreme-value',['EVTEARLY'],'Restates an explicitly supplied theorem; earlier statement includes nonempty set.'),
]
proof=[{'result':ev(k),'supports':[SUP[s] for s in ss],'scope':note} for k,ss,note in proof_specs]
graphs={'snapshot':SNAP,'support_registry':SUP,'learning_edges':learning,'proof_edges':proof,'supplied_roots':[{'evidence':SUP['EVTEARLY'],'scope':'continuous function on nonempty closed bounded subset of Rn; supplied, not proved in book'}, {'evidence':SUP['IVT'],'scope':'C1 local inverse under nonsingular derivative; existence supplied, inverse derivative formula proved from chain rule'},{'evidence':ev('appC-eig-symmetric-matrices'),'scope':'real symmetric finite-dimensional spectral theorem supplied in reference, no local proof promised'},{'evidence':ev('appE-gstokes-the-theorem'),'scope':'compact oriented piecewise smooth manifold/region; C1 form on neighborhood, induced boundary orientation; supplied summary'}],'missing_supports':[{'finding':'REF-01','tasks':['checkpoint-9-1-gradient-normal-tangent-plane','checkpoint-9-5-gradients-parallel'],'status':'not absent theory: later/local and earlier C8 support exists, but the tasks omit a required nonzero hypothesis'},{'finding':'REF-02','task':'checkpoint-9-6-multiplier-misses-boundary','status':'support exists in one-variable Fermat and worked endpoint; hint gives wrong reason'}], 'graph_ceiling':'Task-level learning edges and theorem-level proof edges for this partition. Cross-chapter proof closure depends on root integration; no claim of book-wide acyclicity.'}
(HERE/'graphs.json').write_text(json.dumps(graphs,indent=2),encoding='utf-8')

def concept(cid,name,scope,roles,rules,prereq=None,confidence='confirmed within indicated route'):
 result={'concept_id':cid,'name':name,'scope':scope,'type':'capability','confidence':confidence,'rules_available':rules,'prerequisite_concepts':prereq or []}
 names=['first_mention','first_concrete_explanation','first_formal_definition','first_demonstrated_computation','first_justified_general_rule','first_required_use','later_generalizations']
 for field,val in zip(names,roles):
  result[field]=[ev(x) for x in val] if isinstance(val,list) else ev(val) if val else None
 return result
concepts=[
 concept('gradient.level_normal','Gradient normal to regular levels','C1 scalar functions; nonzero gradient and smooth regular level near point. Global first mention before this partition is not asserted.', ['c7s2-subsec-contour-maps','c7s2-subsec-contour-maps',None,'c9s1-subsec-contour-line-on-a-hill','c9s1-thm-gradient-normal-level-curve','checkpoint-9-1-gradient-perp-level-curve',['c9s1-thm-gradient-normal-level-surface']],['Differentiate constant level along a curve; nonzero normal defines tangent hyperplane.']),
 concept('optimization.fermat','Interior extremum gives zero partials','Rn, all first partials exist; df=0 requires total differentiability.', ['c9s2-hill-highest-nearby','c9s2-hill-highest-nearby','c9s2-def-critical-point','c9s2-hill-highest-nearby','c9s2-thm-fermat','checkpoint-9-2-why-gradient-zero',['c9s5-thm-lagrange-one-constraint']],['Coordinate slices and one-variable Fermat.']),
 concept('hessian.entries','Compute and interpret Hessian','First calculus-capable explanation in Ch9; earlier Chapter3 Hessian is explicitly a preview.', ['c3s6-subsec-hessian-preview','c9s3-subsec-summit-we-already-met','c9s3-def-hessian-matrix-two-variables','c9s3-subsec-summit-we-already-met','c9s3-thm-equality-of-mixed-partials','checkpoint-9-3-symmetry-from-equal-mixed-partials',['appC-qf-connection-to-hessians']],['Differentiate partials again; C2 symmetry; matrix multiplication available earlier.']),
 concept('taylor.uniform_quadratic','Uniform second-order approximation','C2 near a point in R2; exact integral remainder bounds all directions.', ['c9s3-subsec-quadratic-approximation','c9s3-subsec-quadratic-approximation',None,'c9s3-ex-minimum-through-quadratic-part','c9s3-thm-second-order-approximation','checkpoint-9-3-hessian-as-second-order-term',['c9s4-thm-second-derivative-test']],['Segment chain rule, twice FTC, entrywise continuity yields o(norm(h)^2).']),
 concept('optimization.hessian_test','Read definiteness and dominate remainder','R2 C2 critical points; no classification if determinant0.', ['c9s4-reading-the-quadratic-part','c9s4-reading-the-quadratic-part','c9s4-def-definite-indefinite','c9s4-reading-the-quadratic-part','c9s4-thm-second-derivative-test','checkpoint-9-4-quadratic-decides',['appC-qf-second-derivative-test']],['Complete squares; EVT on q(cos theta,sin theta) supplies positive lower bound.']),
 concept('optimization.lagrange_one','One-constraint multiplier condition','C1 near p, regular defining function; necessary condition only.', ['c9s5-subsec-circular-walking-path','c9s5-subsec-circular-walking-path',None,'c9s5-subsec-circular-walking-path','c9s5-thm-lagrange-one-constraint','checkpoint-9-5-gradients-parallel',['c9s5-thm-lagrange-two-constraints']],['Allowed tangent kernel; linear-functional decomposition gives df=lambda dg.']),
 concept('optimization.least_squares','Least-squares fit with residual geometry','Four fixed data points; algebra, derivatives and R4 dot products; no probability assumptions.', ['c9s7-subsec-least-squares','c9s7-subsec-least-squares',None,'c9s7-subsec-least-squares',None,'c9s7-subsec-least-squares',None],['Squared error defined locally; derivatives give normal equations; Hessian and residual prove unique global fit.']),
 concept('reference.single_variable_differential','Evaluate differential on an increment','Appendix A reference route; local operational meaning, not prior multivariable entry assumption.', ['appA-deriv-differential-notation','appA-deriv-differential-notation',None,'appA-deriv-differential-notation',None,None,None],['dx(h)=h; df_x(h)=f prime(x)h; compare values, not a covector with scalar delta f.']),
 concept('reference.series','Read convergent series and Taylor polynomials','Appendix A local reference route; formulas supplied, no tasks require additional convergence theory.', ['appA-series-sequences','appA-series-series','appA-series-series','appA-series-common-taylor-series','appA-series-taylors-theorem-with-remainder',None,None],['Partial sums define convergence; Taylor remainder supplied with n+1 derivatives.']),
 concept('reference.complex_rotations','Compute complex products as rotations','Appendix B independent reference route using entry algebra/trig.', ['appB-cplx-subsec-complex-numbers','appB-cplx-subsec-complex-numbers','appB-cplx-subsec-complex-numbers','appB-cplx-subsec-multiplication','appB-cplx-subsec-multiplication-in-polar-form',None,['appB-euler-euler-form','subsec-appB-roots-nth-roots-of-a-complex-number']],['i^2=-1, multiplication formula, trig polar form; Euler notation supplied.']),
 concept('reference.row_reduction','Solve linear systems by elementary row operations','Appendix C reference route; no assigned numerical task.', ['appC-row-linear-systems','appC-row-elementary-row-operations','appC-row-reduced-row-echelon-form',None,'appC-row-consistency-test',None,['appC-inv-by-row-reduction']],['Three reversible row operations, pivots/free variables, consistency and null space.']),
 concept('reference.spectral','Use symmetric-matrix diagonalization','Real finite-dimensional matrices; supplied spectral theorem in reference, not a locally proved result.', ['appC-eig-definition','appC-eig-definition','appC-eig-definition',None,'appC-eig-symmetric-matrices',None,['appC-qf-eigenvalue-test','appC-qf-diagonalization']],['Eigenpairs solve singular system; real symmetric matrix has orthonormal eigenbasis; formula A=QDQ^T.']),
 concept('reference.coordinate_metric','Read scalar line/area/volume factors','Appendix D route; wrapper states derivatives, regular once-covering coordinate patches, pullback abbreviation and unsigned measures.', ['appD-polar-small-displacement','appD-polar-unit-vectors','appD-elem-scale-factors','appD-polar-unit-vector-derivatives','appD-elem-scale-factors',None,['appD-elem-parametric-surface','appD-elem-spherical-surface-elements']],['Scale h_i=norm(r_ui); ds is unsigned; orientation signs belong to forms.']),
 concept('reference.curvilinear_operators','Use grad/div/curl/Laplacian coordinate formulas','Appendix D reference; displayed unit-basis components, sufficient derivative regularity and coordinate singularity restrictions.', ['appD-vecop-cartesian-coordinates','appD-vecop-polar-coordinates',None,None,'appD-vecop-spherical-coordinates',None,None],['Supplied formulas; components are local orthonormal components; exclude r=0,rho=0,sin(phi)=0 when denominators appear.']),
 concept('reference.wedge','Expand coordinate wedge products','Appendix E reference route; 1/2/3 forms in R3, graded products stated generally.', ['subsec-appE-forms-2-forms-plane','appE-wedge-basic-antisymmetry',None,'appE-wedge-two-1-forms-in-the-plane','appE-wedge-graded-sign-rule',None,['appE-wedge-three-1-forms-in-space']],['Distributivity; repeated coordinate differential vanishes; swaps of two1-forms change sign; k,l degrees give(-1)^(kl).']),
 concept('reference.pullback','Rewrite forms in parameter variables','Appendix E reference; derivatives and integration coverage supplied in wrapper.', ['appE-pull-meaning','appE-pull-meaning',None,'appE-pull-along-a-curve','appE-pull-of-coordinate-area-forms',None,['appE-pull-under-a-coordinate-change']],['Substitute coefficient functions and differentials; wedge determinants; integrals with compatible once-covering orientation.']),
 concept('reference.exterior_derivative','Apply d by coordinate formulas','Appendix E C1 for d; C2 for d squared; no distributional extension.', ['appE-extd-main-idea','appE-extd-derivative-of-a-0-form',None,'appE-extd-derivative-of-a-plane-1-form','appE-extd-product-rule',None,['appE-extd-exterior-derivative-squared','appE-trans-vector-identities-d-squared-zero']],['Coordinate grad/curl/div formulas; degree+1; signed Leibniz; d squared0 under declared regularity.']),
 concept('reference.stokes','Use generalized Stokes summary','Compact oriented piecewise smooth M; form C1 on open neighborhood, degree dim M-1; induced boundary orientation.', ['appE-gstokes-the-theorem','appE-gstokes-degree-matching',None,'appE-gstokes-fundamental-theorem-of-calculus','appE-gstokes-the-theorem',None,['appE-gstokes-divergence-theorem']],['Supplied theorem; FTC/Green/Stokes/divergence examples are specializations, no new general proof claimed.']),
]
(HERE/'concepts.json').write_text(json.dumps({'snapshot':SNAP,'role_scope_note':'Chapter 9 concepts include verified earlier supports. reference.* entries record roles within the appendix reading route, not a claim to global first occurrence; null means absent/not applicable or outside this partition, never proof of book-wide absence. Supplied general rules are labeled in scope/rules and graphs.','concepts':concepts},indent=2),encoding='utf-8')

sections=[s for s in INV['sections'] if assigned(s['path'])]
coverage=[]
for s in sections:
 t=E.parse(str(ROOT/s['path']))
 figs=t.findall('.//figure')
 unresolved=[]
 if s['id']=='sec-9-the-gradient-and-level-sets':unresolved=['REF-01 checkpoint lacks nonzero-gradient hypothesis']
 if s['id']=='sec-9-constrained-optimization-and-lagrange-multipliers':unresolved=['REF-01 checkpoint lacks regular defining-function hypothesis']
 if s['id']=='sec-9-warning-examples':unresolved=['REF-02 endpoint hint misidentifies missing hypothesis']
 coverage.append({'section_id':s['id'],'path':s['path'],'lines':s['lines'],'sha256':s['sha256'],'snapshot':SNAP,'order':s['order'],'occurrence':s['occurrence'],'ancestry':s['ancestry'],'inventoried':True,'mechanically_scanned':True,'semantic_read':True,'support_verified':not unresolved,'support_scope':'All prose/formulas/reference rules and tasks in this section semantically read; supplied theorem boundaries honored. No claim of global proof certification.','task_witnesses_complete':True,'task_count_tagged':len(t.findall('.//exercise')),'task_witness_rows':len([r for r in tasks if r['section_id']==s['id']]),'independent_challenge_completed':False,'graphics_review':{'source':True,'rendered':False,'figure_ids':[x.get(X) for x in figs],'note':'All visible labels and geometric source code read; no rendered visual inspection. No graphics in appendix sections.' if not figs else 'All5 Chapter9 figures were inspected in source, including displayed gradients, tangent labels and decision-flow conditions. Rendered collision/clipping unverified.'},'unresolved':unresolved})
wrappers=[]
for f in INV['files']:
 if (assigned(f['path']) and f['path'].endswith('.ptx')) or f['path'] in ('source/main.ptx','source/frontmatter.ptx','source/backmatter.ptx','source/docinfo.ptx'):
  wrappers.append({'path':f['path'],'sha256':f['sha256'],'snapshot':SNAP,'lines':[1,f['lines']],'semantic_read':True,'support_verified':True,'graphics_review':'not applicable; tables read; docinfo macros are infrastructure not instruction','unresolved':['Visible preface remains placeholder; editorial completeness, not a mathematical prerequisite finding.'] if f['path']=='source/frontmatter.ptx' else []})
(HERE/'coverage.json').write_text(json.dumps({'snapshot':SNAP,'branch':'main','initial_worktree_status':'?? MVC-pretext-Codex-Ultra-full-logical-audit.md','scope':'Chapter9, AppendicesA-E and their wrappers; main/frontmatter/backmatter/docinfo route wrappers','section_count':len(sections),'tagged_task_count':57,'sections':coverage,'wrappers':wrappers,'remaining':['Independent challenge pending.','No rendered graphic inspection claimed.','Global dependency closure and proof-cycle analysis belong to integration.']},indent=2),encoding='utf-8')
print(json.dumps({'sections':len(sections),'tasks_tagged':57,'witness_rows':len(tasks),'concepts':len(concepts),'learning_edges':len(learning),'proof_edges':len(proof),'wrappers':len(wrappers)}))
