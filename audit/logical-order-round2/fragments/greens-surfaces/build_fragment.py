from pathlib import Path
from lxml import etree as E
import json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
AUDIT=ROOT/'audit/logical-order-round2'
SNAP='9a9d110af839b539fe598de66ecc4320a4126af4'
INDEX=json.loads((AUDIT/'id-index.json').read_text(encoding='utf-8'))
INV=json.loads((AUDIT/'inventory.json').read_text(encoding='utf-8'))
TASKS=json.loads((AUDIT/'task-inventory.json').read_text(encoding='utf-8'))
X='{http://www.w3.org/XML/1998/namespace}id'
def assigned(p):return any('/ch'+c+'-' in p for c in ('14','15'))
def ev(key,lines=None):
 d={k:v for k,v in INDEX[key].items() if k in ('snapshot','path','sha256','lines','xml_id','node_id','section_id','section_order','occurrence','xpath')}
 if lines:d['lines']=list(lines)
 return d
SUP={}
def support(k,xmlid,lines=None):SUP[k]=ev(xmlid,lines)
support('ENTRY','how-to-read',(29,43))
support('CROSSAREA','c2s5-thm-length-of-cross-product')
support('CROSSNORMAL','c2s5-thm-cross-product-normal-to-plane')
support('WEDGE','c2s7-def-wedge-linear-measurements')
support('GRID','c5s2-def-regular-grid-point')
support('VECTOR_DERIV','c7s5-def-differentiability-transformation')
support('VECTOR_PARTIAL','c7s5-parametrized-surface')
support('CHAIN','c8s2-thm-matrix-chain-rule')
support('IFT','c8s5-thm-inverse-function')
support('EVT','c6s4-thm-extreme-value-theorem')
support('MIXED','c9s3-thm-equality-of-mixed-partials')
support('FUBINI','c10s3-thm-fubini-rectangles')
support('POLAR','c10s5-thm-double-integrals-polar')
support('AREA_PULL','c12s5-def-pullback-area-form')
support('VOLUME_PULL','c12s5-subsec-pulling-back-volume-elements')
support('WORK','c13s3-def-work-integral')
support('WORK_REVERSE','c13s3-thm-reparametrization-work')
support('PULL1','c13s4-def-pullback-1-form')
support('WORK_FTC','thm-c13s5-ftli')
support('PARAM_LEMMA','c13s6-lem-parameter-integral')
support('CURL_PRIOR','c13s6-def-closed-1form-space')
support('POTENTIAL','c13s6-thm-curl-test-simply-connected')
support('PLANE_D_PRIOR','c13s8-exterior-derivative-thread',(166,200))
support('RECT_CIRC','sec-14-circulation-around-a-small-rectangle',(18,110))
support('SCALAR_CURL','c14s1-def-scalar-curl-plane')
support('ORIENT2','c14s1-def-positive-orientation')
support('CANCEL2','sec-14-circulation-around-a-small-rectangle',(361,381))
support('GREEN','c14s2-thm-green-circulation')
support('SING2','c14s2-singularity',(199,235))
support('JUMP2','c14s2-jump')
support('AREA_GREEN','c14s2-area',(313,331))
support('ANNULUS','c14s2-holes')
support('FLUX2','c14s3-subsec-outward-normal',(90,134))
support('DIV2','c14s3-def-divergence-plane')
support('GREEN_FLUX','c14s3-thm-green-flux-form')
support('SING_FLUX2','c14s3-subsec-why-hypotheses')
support('PLANE_D','c14s4-def-exterior-derivative-plane-1-form')
support('FORM_CHOICE','c14s4-subsec-1-form-on-boundary',(35,68))
support('GREEN_FORM','c14s4-thm-greens-for-1-forms')
support('FTC_PATTERN','sec-14-green-s-theorem-in-differential-form-language',(390,447))
support('RECT_PROOF','c14s5-subsec-proof-rectangle')
support('EDGE_CANCEL','c14s5-subsec-two-rectangles-disappearing-edge',(145,174))
support('TELESCOPE','c14s5-subsec-many-rectangles',(243,306))
support('TYPEI','c14s5-type-i-complete-proof')
support('GREEN_SCOPE','c14s5-proof-scope')
support('SHOELACE','c14s7-ex-shoelace')
support('PROJECT_SAMPLE','c14s7-ex-grp-project',(269,279))
support('SURFACE_INTRO','c15s1-subsec-two-parameters-make-a-surface',(20,35))
support('PARAMSURF','c15s1-def-parametric-surface')
support('SURF_PARTIAL','c15s1-def-tangent-vectors-from-a-parametrization')
support('REGULAR','c15s1-def-smooth-regular-surface-patch')
support('NORMAL_ORDER','c15s1-subsec-normal-direction-from-the-cross-product',(181,248))
support('TANGENT','c15s1-thm-tangent-plane-to-a-parametrized-surface')
support('CONE_SPHERE','c15s1-subsec-why-the-hypotheses-matter',(450,517))
support('AREA_SCALE','c15s2-subsec-rectangle-to-parallelogram',(18,43))
support('AREA_SURF','c15s2-subsec-surface-area-from-parametrization',(90,108))
support('SCALAR_SURF','c15s2-def-scalar-surface-integral')
support('DENSITY_SURF','c15s2-ex-cylindrical-shell-mass')
support('GRAPH_AREA','c15s2-subsec-surface-area-of-graphs')
support('SPHERE_AREA','c15s2-subsubsec-sphere')
support('MULTIPLICITY','c15s2-subsec-parametrizations-count-too-much',(357,379))
support('ORIENT3','c15s3-def-orientation-surface')
support('MOBIUS_PREP','c15s3-subsec-two-normal-directions',(101,118))
support('NORMAL_FLUX','c15s3-subsec-flux-signed-flow',(139,166))
support('FLUX3','c15s3-def-flux-integral')
support('FLUX_PARAM','c15s3-thm-flux-parametrized-surface')
support('OUTWARD','c15s3-def-outward-orientation')
support('CYL_FLUX','c15s3-subsec-flux-side-cylinder')
support('FLUX_FORM','c15s4-def-flux-2-form')
support('SHADOWS','c15s4-shadows-of-surface-patch',(128,196))
support('PULL2','c15s4-pullback-to-parameter-domain',(217,278))
support('FORM_INT','c15s4-def-surface-integral-2-form')
support('GRAPH_FLUX','c15s4-graphs-and-flux-formula')
support('CURL3','c15s5-def-curl')
support('CURL_D','c15s5-subsec-paddle-wheel',(113,142))
support('BOUNDARY3','c15s5-def-compatible-boundary-orientation')
support('STOKES','c15s5-thm-stokes')
support('STOKES_PROOF','c15s5-thm-stokes',(333,378))
support('DIV3','c15s6-def-divergence')
support('BOX_FLUX','c15s6-subsec-flux-out-of-a-small-box',(15,98))
support('DIV_D','c15s6-subsec-divergence-in-form-language')
support('FACE_CANCEL','c15s6-subsec-the-divergence-theorem',(291,306))
support('DIV_THM','c15s6-thm-divergence-theorem')
support('SPHERE_SOURCE','c15s6-subsec-why-the-hypotheses-matter',(581,647))
support('CURL_GRAD','c15s7-thm-curl-of-gradient')
support('DIV_CURL','c15s7-thm-divergence-of-curl')
support('DSQUARED','c15s7-subsec-single-fact-d-squared',(242,300))
support('TOPOLOGY','c15s7-subsec-potentials-topology',(322,365))
support('MOBIUS','c15s8-nonorientable-surface',(18,89))
support('SKILL_EXAMPLE','c15s9-worked-easier-surface')
support('CLOSE_EXAMPLE','c15s9-worked-close-surface')
ROWS={}
def row(k,outline,support,verdict='supported',note=''):
 ROWS[k]={'outline':outline,'support':support.split(),'verdict':verdict,'note':note}
row('checkpoint-14-1-opposite-sides','Constant pushes integrate with opposite traversal signs and cancel; differences between opposite sides detect variation. In the displayed field the surviving total is 3hk.','RECT_CIRC WORK_REVERSE')
row('checkpoint-14-1-why-scalar','A plane has one fixed normal axis, so one signed scalar records circulation per oriented area; three-dimensional directions are only a preview here.','SCALAR_CURL RECT_CIRC')
row('checkpoint-14-1-interior-cancellation','Every shared edge is traversed twice in opposite directions with the same field; the uncanceled edges are exactly all external and hole boundaries.','CANCEL2 ORIENT2 WORK_REVERSE')
row('checkpoint-14-2-two-faces','Sum local circulation balances: interior edges cancel, leaving the positively oriented whole boundary; the area integral adds circulation densities.','GREEN CANCEL2')
row('checkpoint-14-2-hidden-curl','The disk contains the origin where alpha is undefined, so the C1 neighborhood hypothesis fails; remove a disk and include its oppositely oriented inner circle.','SING2 GREEN')
row('checkpoint-14-2-inner-boundary','The annulus has two boundary components; keeping the region on the left makes the inner direction clockwise and its integral -2pi.','ANNULUS ORIENT2')
row('checkpoint-14-3-zero-div-meaning','Zero divergence means zero first-order net outflow density, not zero velocity; constant motion and (-y,x) are examples.','DIV2')
row('checkpoint-14-3-same-theorem','Choose P=-N and Q=M in circulation Green: Q_x-P_y=M_x+N_y and P dx+Q dy=M dy-N dx.','GREEN GREEN_FLUX FLUX2')
row('checkpoint-14-3-hidden-source','A jump invalidates C1 and a singularity invalidates definition on the closed region; either permits boundary flux not represented by the ordinary divergence where computed.','GREEN_FLUX JUMP2 SING2')
row('checkpoint-14-4-form-chooses-measurement','M dx+N dy pairs with the tangent; M dy-N dx pairs with the outward normal times ds under positive orientation.','FORM_CHOICE FLUX2')
row('checkpoint-14-4-why-hypotheses-bite','d alpha=0 holds only on the punctured plane. A disk filling the circle contains the missing origin, so GREEN cannot be used there.','GREEN SING2')
row('checkpoint-14-4-one-sentence-many-dimensions','FTC integrates df on an interval to its signed endpoint values; Green integrates d omega on a plane region to omega on its oriented boundary. Degree increases, geometry is not differentiated.','FTC_PATTERN GREEN ENTRY')
row('checkpoint-14-5-edge-cancel-orientation','The common edge has the same integrand and opposite bounds/orientation for its two neighboring rectangles, hence opposite integrals.','EDGE_CANCEL WORK_REVERSE')
row('checkpoint-14-5-telescoping-analogy','Internal endpoint values in sum(f_i-f_{i-1}) cancel as shared oriented edges do in the rectangle sum; outer/inner boundary edges remain.','TELESCOPE')
row('checkpoint-14-5-hypotheses-role','A hole creates an unpaired boundary edge; a jump or undefined field prevents applying each local formula across the defect. Cancellation never removes a missing rim.','JUMP2 SING2 ANNULUS TELESCOPE')
row('checkpoint-14-6-singularity-domain','Alpha is not C1 on an open neighborhood of the closed disk because it is undefined at its center; the boundary integral is still valid and equals 2pi.','GREEN SING2')
row('checkpoint-14-6-hole-extra-boundary','The missing hole creates a genuine boundary component whose integral cannot be removed just by subtracting its area; for x dy, outer 4pi plus inner -pi equals 3pi.','ANNULUS AREA_GREEN')
row('checkpoint-14-6-jump-hidden-edge','Q_x=0 only off the jump; no C1 field on the rectangle exists. The top/bottom and left give 0, right gives 1, so ignoring the discontinuity loses that boundary balance.','JUMP2 GREEN')
row('c14s7-proj-1','Insert the ordered sampled coordinates into one half the absolute cyclic cross-product sum. No particular data set is supplied, so this is a symbolic algorithm rather than a missing numerical answer.','SHOELACE PROJECT_SAMPLE')
row('c14s7-proj-2','On each time interval of length h, bound the error between integral x dy and the chord trapezoid by 2 Mx My h^2, using bounds on the continuous coordinate velocities from EVT. Sum to obtain error <=2 Mx My T max(h), tending to zero for equally spaced sampling. More points need not improve monotonically.','SHOELACE PROJECT_SAMPLE WORK EVT ENTRY','supported discovery','This bounded-velocity proof needs no compactness finite-subcover theorem and no numerical-analysis theorem.')
row('c14s7-proj-3','Parametrize the edge x=xi+t(xj-xi), y=yi+t(yj-yi). Integral x dy=(xi+xj)(yj-yi)/2. Summing leaves the cross terms because sum(xj yj-xi yi)=0.','WORK SHOELACE')
row('c14s7-proj-4','xy prime-yx prime=6+6 cos(t)-4 cos(t)^3. The odd-cosine terms integrate to zero, giving area 6pi. The curve is regular and simple: equal y gives opposite cosines, whose x difference is 6 cos(t), except at the identical points.','AREA_GREEN WORK ENTRY')
for k,o,s in [
('1','Curl is y+1; integral over [0,3]x[0,2] is 12.','GREEN FUBINI'),
('2','Curl is 2; unit disk area gives 2pi.','GREEN AREA_GREEN'),
('3','Divergence of (x+y,2x-y) is 1-1=0; total outward flux is 0.','GREEN_FLUX'),
('4','d(x dy)=dx wedge dy; annulus area is pi(9-1)=8pi. Inner boundary is clockwise.','GREEN ANNULUS AREA_GREEN'),
('5','d omega=(2x-2y) dx wedge dy. Over [0,1]x[0,2] the two contributions are 2 and -4, total -2.','PLANE_D GREEN FUBINI'),
('6','Disk contains undefined origin; the closed annulus 1/4<=r^2<=1 has a neighborhood avoiding it, so Green applies with both rims.','GREEN SING2 ANNULUS'),
('7','The clockwise area-form integral is minus unsigned enclosed area, so area=8.','AREA_GREEN WORK_REVERSE'),
('8','Choose omega=5x dy, giving d omega=5 dx wedge dy and positive boundary integral 5 Area(R) under GREEN hypotheses.','PLANE_D GREEN')]:row('c14s7-prac-'+k,o,s)
row('checkpoint-15-1-two-numbers-three-numbers','Two independent parameter changes describe motion on the local sheet; the three output coordinates locate that sheet in space. Arbitrary maps can degenerate, addressed later by regularity.','SURFACE_INTRO','supported local introduction')
row('checkpoint-15-1-order-of-the-cross-product','Swapping the ordered tangent vectors changes the cross product to its negative: it chooses the opposite normal side of the same tangent plane.','NORMAL_ORDER CROSSNORMAL')
row('checkpoint-4-5-two-tangents-and-cross-product','Freeze each parameter to get its coordinate-curve velocity. Under C1 regularity the independent vectors span the tangent plane, and their nonzero cross product is normal.','SURF_PARTIAL REGULAR CROSSNORMAL')
row('checkpoint-15-1-why-regularity-is-needed','A zero cross product alone diagnoses this chart. At the sphere pole an alternate graph chart has independent tangents; at the cone apex three generator directions are independent and cannot lie in any single tangent plane.','CONE_SPHERE')
row('checkpoint-15-2-why-cross-product-length','The cross product encodes oriented parallelogram area; its norm keeps nonnegative area while discarding the normal direction.','AREA_SCALE CROSSAREA')
row('checkpoint-15-2-why-density-times-dS','Each small patch contributes its own density times area; summing first cannot preserve varying density. Only constant density can be pulled outside.','SCALAR_SURF DENSITY_SURF')
row('checkpoint-15-2-counting-with-multiplicity','The parameter domain sweeps each cylinder point twice, so its integral counts 2 copies. Restrict theta to one 2pi interval for the geometric area.','MULTIPLICITY AREA_SURF')
row('checkpoint-4-5-choosing-an-orientation','Following a continuous unit normal once around a Mobius strip returns its negative at the same point, contradicting a single-valued consistent normal.','ORIENT3 MOBIUS_PREP')
row('checkpoint-15-3-tangent-zero-flux','Under the stated pointwise tangency, no fluid crosses the surface even though fluid moves along it. This is stronger than merely zero total flux.','NORMAL_FLUX')
row('checkpoint-15-3-mobius-no-side','Signed flux needs a global positive normal side; the Mobius return reversal assigns contradictory signs at the same point.','FLUX3 ORIENT3 MOBIUS_PREP')
row('c4s6-ex-d6','r_theta=(-2 sin theta,2 cos theta,0), r_z=(0,0,1); cross=(2 cos theta,2 sin theta,0), radial outward.','SURF_PARTIAL CROSSNORMAL CYL_FLUX')
row('checkpoint-15-3-zero-net-flux-meaning','Zero total outward flux allows inward and outward contributions to cancel; a constant vertical field enters a box bottom and leaves the top.','FLUX3 OUTWARD')
row('checkpoint-15-4-three-shadows','The three independent coordinate-plane signed areas are the components of the normal area vector in R3; one projection loses tilts with zero projection.','SHADOWS WEDGE')
row('checkpoint-15-4-orientation-sign','Changing normal replaces ordered area by its negative. Flux distinguishes crossings in the designated positive direction from opposite crossings.','FORM_INT ORIENT3 FLUX3')
row('checkpoint-15-4-form-vs-cross-product','Each coefficient multiplies its particular oriented coordinate shadow; the sum exposes the three signed area measurements bundled in the dot-cross expression.','SHADOWS FLUX_FORM')
row('checkpoint-15-5-three-components','The x,y,z curl components measure circulation density in oriented yz,zx,xy planes respectively; a spatial wheel can have any normal direction.','CURL3 CURL_D SCALAR_CURL')
row('checkpoint-15-5-why-surface-free','Each admissible oriented spanning surface has curl flux equal to the same boundary work integral by Stokes. Hypotheses and matching orientation are essential.','STOKES')
row('checkpoint-15-5-same-story','FTC, Green and Stokes equate interior derivative accumulation with boundary accumulation; d raises integrand degree by one, while the boundary lowers geometric dimension.','STOKES GREEN FTC_PATTERN')
row('checkpoint-15-6-zero-divergence-meaning','Divergence records net outward flux per infinitesimal volume, not speed; (-y,x,0) has divergence zero and can be nonzero.','DIV3 BOX_FLUX')
row('checkpoint-15-6-why-interior-faces-cancel','A shared face has the same field and opposite outward normals for the two boxes, so its two flux integrals are negatives.','FACE_CANCEL FLUX3')
row('checkpoint-15-6-flux-without-opening-box','The divergence theorem equates the total local source density with one boundary flux; positive and negative local sources may cancel, so it does not recover their separate distribution.','DIV_THM')
row('checkpoint-15-7-paddle-wheel','The work FTC gives f(final)-f(initial)=0 on the closed loop. For the paddle-wheel interpretation the disk circulation is zero at every scale, so its local circulation per area is zero. No use of the following curl-gradient theorem is necessary.','WORK_FTC CURL3')
row('checkpoint-15-7-two-ingredients','Antisymmetry turns the two mixed terms into (f_yx-f_xy) dx wedge dy; equality of mixed partials then kills the coefficient. Without either ingredient that cancellation fails.','DSQUARED WEDGE MIXED')
row('checkpoint-15-7-curl-versus-potential','The omitted z-axis prevents the encircling loop from contracting within the domain; the explicit loop integral 2pi contradicts the zero-loop integral of any global potential.','TOPOLOGY WORK_FTC POTENTIAL')
row('checkpoint-15-8-mobius-area-vs-flux','The norm area density is invariant under normal reversal; signed flux requires a continuous global normal and fails on the Mobius identification.','MOBIUS SCALAR_SURF FLUX3')
row('checkpoint-15-8-hidden-singularity','Divergence theorem needs C1 on a neighborhood of the solid closure. The radial field is undefined at its interior origin, though smooth on the sphere.','DIV_THM SPHERE_SOURCE')
row('checkpoint-15-8-orientation-match','Upward disk orientation induces counterclockwise boundary; clockwise pairs with downward instead. Reversing just one side changes the sign.','BOUNDARY3 STOKES')
for k,o,s in [
('fluid-1','r=(x,y,g); r_x=(1,0,g_x),r_y=(0,1,g_y), cross=(-g_x,-g_y,1), upward.','GRAPH_FLUX'),
('fluid-2','Ordinary partial differentiation gives g_x=(pi/5)cos(pi x)sin(pi y), g_y=(pi/5)sin(pi x)cos(pi y).','SURF_PARTIAL ENTRY'),
('fluid-3','Integral on the unit square of -g_x-(1/2)g_y+2-g/4 with respect to dx dy.','GRAPH_FLUX FUBINI'),
('fluid-4','-g_x and -(1/2)g_y are horizontal wind through tilted coordinate shadows; 2-g/4 is vertical velocity through the upward xy shadow.','GRAPH_FLUX SHADOWS'),
('fluid-5','The derivative terms integrate to zero by boundary values g(0,y)=g(1,y)=g(x,0)=g(x,1)=1. Integral g=1+4/(5pi^2); flux=7/4-1/(5pi^2). Exact integration avoids any numerical-method prerequisite.','GRAPH_FLUX FUBINI ENTRY'),
('gauss-1','On radius a sphere E dot n=kq/a^2; multiply by area 4pi a^2 to get 4pi kq.','SPHERE_SOURCE SPHERE_AREA'),
('gauss-2','The a^-2 field factor and a^2 area factor cancel, leaving 4pi kq independent of a>0.','SPHERE_SOURCE'),
('gauss-3','The field is undefined at the origin in the full ball; it is not C1 on a neighborhood of the closure.','DIV_THM SPHERE_SOURCE'),
('gauss-4','Divergence is zero on b<=r<=a. Shell outward flux is outer radial-outward flux minus inner radial-outward flux, so those radial-outward fluxes agree.','DIV_THM SPHERE_SOURCE'),
('gauss-5','Substitute k=1/(4pi epsilon0) into 4pi kq to obtain q/epsilon0. Physics constants are supplied; no electromagnetism course needed.','SPHERE_SOURCE ENTRY'),
('practice-1','Use r(s,theta)=(s cos theta,s sin theta,s), 0<=s<=3. Norm cross=sqrt(2)s; area=int_0^2pi int_0^3 sqrt(2)s ds dtheta=9pi sqrt(2). The apex is a boundary degeneracy, handled by truncation or the scalar integral boundary convention.','AREA_SURF CONE_SPHERE POLAR'),
('practice-2','dS=sqrt(1+4r^2) r dr dtheta; scalar integral=2pi int_0^1(4-r^2)sqrt(1+4r^2)r dr. With u=1+4r^2 the result is pi(175sqrt(5)-41)/60.','GRAPH_AREA POLAR ENTRY'),
('practice-3','div(x,0,z)=2; cylinder volume=pi(2)^2*5=20pi, so flux=40pi.','DIV_THM FUBINI'),
('practice-4','Side r(theta,z) gives integrand 4cos^2 theta, hence20pi. Top gives z=5 times disk area4pi=20pi; bottom z=0 gives0. Total40pi.','FLUX_PARAM CYL_FLUX OUTWARD ENTRY'),
('practice-5','For F=(yz,zx,xy), every curl component cancels (x-x,y-y,z-z), and each same-coordinate partial is zero; curl=0, divergence=0.','CURL3 DIV3'),
('practice-6','Curl(0,xz,0)=(-x,0,z), then divergence=-1+0+1=0.','CURL3 DIV3'),
('practice-7','Curl(-y,x,z)=(0,0,2); upward triangle area1/2 gives work1.','STOKES CURL3'),
('practice-8','Curl(z,x,y)=(1,1,1). Upward graph z=1-x-y has area vector(1,1,1); triangular base area1/2 gives3/2. Boundary order (0,0,1)->(1,0,0)->(0,1,0)->(0,0,1); each edge work1/2, total3/2.','STOKES GRAPH_FLUX WORK'),
('practice-9','dPhi=3 dx wedge dy wedge dz; unit ball volume4pi/3 gives outward flux4pi.','DIV_D DIV_THM'),
('practice-10','Mobius normal changes sign after one circuit; signed flux lacks a consistent global sign, while scalar area uses a norm and survives.','MOBIUS SCALAR_SURF'),
('practice-11','r(t)=(3cos t,3sin t,0); A=(-sin t/3,cos t/3,0), dot r prime=1. Integral0..2pi is2pi.','WORK TOPOLOGY'),
('practice-12','On radius5, G dot n=1/25 and area100pi, giving4pi. The origin makes full-ball divergence theorem inadmissible.','SPHERE_SOURCE DIV_THM')]:row('c15s9-'+k,o,s)

selected=[t for t in TASKS if assigned(t['path'])]
extra_map={
('c14s2-jump',176):('Right-edge integral is 1; the other three edge integrals are zero. This is the displayed worked calculation.','JUMP2','worked calculation'),
('c14s6-a-jump-inside-is-a-hidden-edge',322):('Right edge Q=1 contributes 1, the other edges contribute 0; this is the worked jump example.','JUMP2','worked calculation'),
('c15s2-subsubsec-sphere',322):('r_phi=(a cos(phi)cos(theta),a cos(phi)sin(theta),-a sin(phi)), r_theta=(-a sin(phi)sin(theta),a sin(phi)cos(theta),0); norm cross=a^2 sin(phi).','SURF_PARTIAL CROSSAREA','worked calculation'),
('c15s7-subsec-gradient-no-rotation',28):('For grad T=(2xy,x^2+z,y+3), curl=(1-1,0-0,2x-2x)=0.','CURL3','worked calculation'),
('c15s9-skill-checklist',148):('Differentiate the parametrization, cross the two vectors and take its norm. Checklist capability, no independent data.','AREA_SURF','review directive'),
('c15s9-skill-checklist',151):('Check the sign of the cross product against the requested normal; reverse order if needed. Checklist capability.','ORIENT3 FLUX_PARAM','review directive'),
('c15s9-skill-checklist',154):('Integrate f(r) norm(r_u cross r_v) over the parameter domain with once coverage. Checklist capability.','SCALAR_SURF','review directive'),
('c15s9-skill-checklist',157):('Integrate F(r) dot(r_u cross r_v); graph formula is -P g_x-Q g_y+R. Checklist capability.','FLUX_PARAM GRAPH_FLUX','review directive'),
('c15s9-skill-checklist',163):('Compute coordinate curl and check Stokes hypotheses/compatible boundary. Checklist capability.','CURL3 STOKES','review directive'),
('c15s9-skill-checklist',166):('Compute P_x+Q_y+R_z and check closed outward boundary/C1 neighborhood. Checklist capability.','DIV3 DIV_THM','review directive'),
('c15s9-worked-easier-surface',192):('Curl(-y,x,z)=(0,0,2); flux through radius2 upward disk is8pi. Already included by worked subsection.','CURL3 STOKES','duplicate worked calculation'),
}
out=[]
for t in selected:
 k=t['xml_id'] or t['nearest_id']+':L'+str(t['lines'][0])
 if k in ROWS:r=ROWS[k]
 elif t['xml_id']=='c15s3-subsec-cylinder-normal-practice':r={'outline':'Umbrella containing c4s6-ex-d6; see its individual witness.','support':['CYL_FLUX'],'verdict':'umbrella duplicate','note':''}
 elif t['xml_id']=='c15s9-worked-easier-surface':r={'outline':'Choose upward radius2 disk at z=3; curl=(0,0,2), hence work=8pi.','support':['STOKES','CURL3'],'verdict':'worked review problem','note':''}
 elif t['xml_id']=='c15s9-worked-close-surface':r={'outline':'Close the radius3 hemisphere with downward disk. Divergence4 times half-ball volume18pi gives72pi; bottom disk dot product is0.','support':['DIV_THM','FLUX3'],'verdict':'worked review problem','note':''}
 else:
  o,s,v=extra_map[(t['nearest_id'],t['lines'][0])];r={'outline':o,'support':s.split(),'verdict':v,'note':''}
 evidence={z:t[z] for z in ('path','lines','xml_id','nearest_id','section_id','node_id','xpath','section_order')}
 out.append({'task_id':k,'source':evidence,**r,'support_evidence':[SUP[s] for s in r['support']]})
# Three skill-list items were not selected by the scanner. They remain visible review obligations.
for line,o,s in [(145,'Choose a two-parameter map and differentiate its components, holding the other parameter fixed.','PARAMSURF SURF_PARTIAL'),(160,'For F=(P,Q,R), write Phi=P dy wedge dz+Q dz wedge dx+R dx wedge dy.','FLUX_FORM'),(169,'Check orientability, matching boundary direction, all boundary components, regular once coverage, and C1 field neighborhood.','REGULAR STOKES DIV_THM MOBIUS')]:
 source=ev('c15s9-skill-checklist',(line,line));out.append({'task_id':'c15s9-skill-checklist:L'+str(line),'source':source,'outline':o,'support':s.split(),'verdict':'review directive','note':'Additional list item omitted by imperative scanner.','support_evidence':[SUP[a] for a in s.split()]})
for line,o,s in [(114,'Check that the region remains on the left of each directed boundary component.','ORIENT2 GREEN'),(115,'Include every hole boundary with clockwise orientation, as well as the outer counterclockwise boundary.','ANNULUS GREEN'),(116,'Require the coefficients and first derivatives on an open neighborhood of the closed region; inspect jumps and singularities.','GREEN JUMP2 SING2'),(117,'Check that the boundary is a finite collection of piecewise smooth simple curves before using the ordinary integral statement.','GREEN GREEN_SCOPE')]:
 source=ev('c14s7-checklist',(line,line));out.append({'task_id':'c14s7-checklist:L'+str(line),'source':source,'outline':o,'support':s.split(),'verdict':'review directive','note':'Checklist table row, no separate numerical assessment.','support_evidence':[SUP[a] for a in s.split()]})
assert len([t for t in selected if t['role']=='exercise'])==len(ROWS),(len(ROWS),len(selected))
def dump(name,data):(HERE/name).write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
dump('task-witnesses.json',{'snapshot':SNAP,'scope':'Chapters14-15','count':len(out),'witnesses':out})
md=['# Exercise and task witnesses: Chapters 14–15','','Each selected source candidate has an explicit individual disposition; seven additional review-list/table items are included. All tagged exercises are solved or outlined. Worked imperatives and umbrella duplicates are distinguished from assessments. Numerical alternatives in the screen project do not create a prerequisite gap because exact integration works. No rendered review is claimed.','','| Task / exact source | Outline | Available support IDs | Verdict |','|---|---|---|---|']
for r in out:md.append('| '+r['task_id']+' ('+r['source']['path']+':'+str(r['source']['lines'][0])+') | '+r['outline'].replace('|','\\|')+' | '+', '.join(SUP[k]['xml_id']+':'+str(SUP[k]['lines'][0])+'-'+str(SUP[k]['lines'][1]) for k in r['support'])+' | '+r['verdict']+' |')
(HERE/'exercise-checks.md').write_text('\n'.join(md)+'\n',encoding='utf-8')
coverage=[]
for sec in INV['sections']:
 if not assigned(sec['path']):continue
 tree=E.parse(str(ROOT/sec['path']))
 unresolved=[]
 if sec['id']=='sec-14-green-s-theorem-in-differential-form-language':unresolved=['GS-01 theorem-restatement closure hypothesis; awaiting independent classification challenge']
 if sec['id']=='sec-14-why-green-s-theorem-is-true':unresolved=['Root U03 proof-support dependency: c13s6-lem-parameter-integral uses an unsupplied finite-subcover principle; formula remains a previously stated lemma']
 coverage.append({'section_id':sec['id'],'path':sec['path'],'lines':sec['lines'],'sha256':sec['sha256'],'semantic_read':True,'support_verified':not unresolved,'task_witnesses_complete':True,'graphics_review':{'source':True,'rendered':False,'count':len(tree.findall('.//figure')),'limitation':'All code/caption/visible labels read; no image clipping or interactive behavior certification.'},'tagged_exercises':len(tree.findall('.//exercise')),'hints':len(tree.findall('.//hint')),'solutions':len(tree.findall('.//solution')),'unresolved':unresolved,'independent_challenge_complete':False})
dump('coverage.json',{'snapshot':SNAP,'section_count':len(coverage),'sections':coverage,'wrappers':[ev('ch14-greens-theorem'),ev('ch15-surfaces-flux-curl-divergence')],'scope_note':'All16 sections plus both wrappers semantically read from source. Source read is separate from support closure. Earlier supports checked locally or independently by assigned source owner; root U03 is explicitly inherited. Global completeness and rendered review are not claimed.'})
roles=['first_mention','first_informal_explanation','first_formal_definition_or_statement','first_required_calculation','first_required_proof_use','first_required_task','first_sufficient_support']
caps=[]
def cap(cid,description,rolekeys,scope='First roles within Chapters14–15; earlier support nodes shown where known, not a claim of global first occurrence.'):
 assert len(rolekeys)==7
 caps.append({'capability_id':cid,'description':description,'scope':scope,'roles':{r:(SUP[k] if k else None) for r,k in zip(roles,rolekeys)},'null_meaning':'No such role established in this bounded pass; null is not absence from the book.'})
cap('gs.green-circulation','Apply Green to C1 field on neighborhood of closed bounded region with all finite oriented boundary curves.',['RECT_CIRC','CANCEL2','GREEN','GREEN','RECT_PROOF','GREEN','GREEN'])
cap('gs.plane-flux','Translate outward flux to M dy-N dx and integrate divergence.',['FLUX2','FLUX2','FLUX2','FLUX2',None,'DIV2','FLUX2'])
cap('gs.plane-exterior-derivative','Use explicit coordinate d(P dx+Q dy), not later general graded derivative.',['PLANE_D_PRIOR','PLANE_D_PRIOR','PLANE_D_PRIOR','PLANE_D','GREEN_FORM','FORM_CHOICE','PLANE_D_PRIOR'])
cap('gs.green-proof-typeI','Prove variable-boundary Green using parameter-integral differentiation, FTC, chain rule and cancellation.',['TYPEI','TYPEI','PARAM_LEMMA','TYPEI','TYPEI',None,'PARAM_LEMMA'])
caps[-1]['support_limitation']='The cited lemma is stated earlier, but its claimed proof depends on root U03 finite-cover support. Do not interpret its presence as a fully closed proof graph.'
cap('gs.shoelace','Derive polygon area by line integration and approximate smooth measured boundaries.',['AREA_GREEN','AREA_GREEN','SHOELACE','SHOELACE',None,'SHOELACE','SHOELACE'])
cap('gs.regular-parametric-tangent-plane','Use C1 total differentiability plus rank2 to obtain local sheet tangent plane.',['GRID','GRID','REGULAR','NORMAL_ORDER','TANGENT','REGULAR','VECTOR_DERIV'])
cap('gs.scalar-surface-integral','Integrate a scalar density with nonnegative cross-product norm and once coverage.',['AREA_SCALE','AREA_SCALE','SCALAR_SURF','AREA_SURF',None,'AREA_SCALE','SCALAR_SURF'])
cap('gs.surface-orientation','Choose continuous normal and distinguish nonorientability, boundary orientation and sign.',['NORMAL_ORDER','NORMAL_ORDER','ORIENT3','NORMAL_ORDER','STOKES_PROOF','MOBIUS_PREP','ORIENT3'])
cap('gs.surface-flux','Compute signed crossing by dot with oriented area vector.',['NORMAL_FLUX','NORMAL_FLUX','FLUX3','NORMAL_FLUX','FLUX_PARAM','NORMAL_FLUX','FLUX_PARAM'])
cap('gs.flux-2-form','Evaluate and pull back three coordinate signed shadows.',['FLUX_FORM','SHADOWS','FLUX_FORM','PULL2','PULL2','SHADOWS','PULL2'])
cap('gs.space-exterior-derivative-1','Use local curl-coordinate definition and prove the C2 patch naturality identity.',['CURL_PRIOR','CURL_D','CURL_D','CURL_D','STOKES_PROOF','CURL3','CURL_D'])
cap('gs.stokes-surface','Use supplied classical Stokes with compactness, compatible boundary and C1 neighborhood.',['STOKES','BOUNDARY3','STOKES','STOKES','STOKES_PROOF','STOKES','STOKES'])
cap('gs.divergence-flux-form','Take the explicitly defined local d of a space flux2form and obtain divergence volume form.',['BOX_FLUX','BOX_FLUX','DIV_D','DIV_D',None,'DIV3','DIV_D'])
cap('gs.divergence-theorem','Use supplied outward boundary/volume theorem on bounded solid closure with C1 field nearby.',['FACE_CANCEL','FACE_CANCEL','DIV_THM','DIV_THM',None,'DIV_THM','DIV_THM'])
cap('gs.vector-identities','Under C2, cancel mixed partials in curl grad and div curl; avoid assuming converses on holes.',['CURL_GRAD','DSQUARED','CURL_GRAD','CURL_GRAD','DIV_CURL','DSQUARED','MIXED'])
task_first={
'gs.green-circulation':'checkpoint-14-2-two-faces',
'gs.plane-flux':'checkpoint-14-3-zero-div-meaning',
'gs.plane-exterior-derivative':'checkpoint-14-4-form-chooses-measurement',
'gs.shoelace':'c14s7-proj-1',
'gs.regular-parametric-tangent-plane':'checkpoint-4-5-two-tangents-and-cross-product',
'gs.scalar-surface-integral':'checkpoint-15-2-why-cross-product-length',
'gs.surface-orientation':'checkpoint-15-1-order-of-the-cross-product',
'gs.surface-flux':'checkpoint-15-3-tangent-zero-flux',
'gs.flux-2-form':'checkpoint-15-4-three-shadows',
'gs.space-exterior-derivative-1':'checkpoint-15-5-three-components',
'gs.stokes-surface':'checkpoint-15-5-why-surface-free',
'gs.divergence-flux-form':'checkpoint-15-6-zero-divergence-meaning',
'gs.divergence-theorem':'checkpoint-15-6-flux-without-opening-box',
'gs.vector-identities':'checkpoint-15-7-paddle-wheel'}
for c in caps:
 if c['capability_id'] in task_first:c['roles']['first_required_task']=ev(task_first[c['capability_id']])
# Concrete worked-calculation locations are distinct from available theorem statements.
for cid,key,lines in [
('gs.green-circulation','c14s2-triangle',(18,84)),
('gs.plane-flux','c14s3-subsec-outward-normal',(20,88)),
('gs.scalar-surface-integral','c15s2-ex-cylinder-side-area',None),
('gs.stokes-surface','c15s5-subsec-first-stokes-circular-wire',(165,225)),
('gs.divergence-theorem','c15s6-subsec-outward-flux-through-a-sphere',None),
('gs.vector-identities','c15s7-subsec-gradient-no-rotation',(20,43))]:
 next(c for c in caps if c['capability_id']==cid)['roles']['first_required_calculation']=ev(key,lines)
later={'gs.green-circulation':['STOKES'],'gs.plane-flux':['FLUX3'],'gs.plane-exterior-derivative':['CURL_D','DIV_D'],'gs.green-proof-typeI':['STOKES_PROOF'],'gs.regular-parametric-tangent-plane':['TANGENT'],'gs.scalar-surface-integral':['FORM_INT'],'gs.surface-orientation':['BOUNDARY3'],'gs.surface-flux':['FLUX_FORM'],'gs.flux-2-form':['DIV_D'],'gs.space-exterior-derivative-1':['DIV_D']}
general={'gs.green-circulation':'GREEN','gs.plane-flux':'GREEN_FLUX','gs.plane-exterior-derivative':'PLANE_D','gs.green-proof-typeI':'TYPEI','gs.shoelace':'SHOELACE','gs.regular-parametric-tangent-plane':'TANGENT','gs.scalar-surface-integral':'SCALAR_SURF','gs.surface-orientation':'ORIENT3','gs.surface-flux':'FLUX_PARAM','gs.flux-2-form':'PULL2','gs.space-exterior-derivative-1':'STOKES_PROOF','gs.stokes-surface':'STOKES','gs.divergence-flux-form':'DIV_D','gs.divergence-theorem':'DIV_THM','gs.vector-identities':'CURL_GRAD'}
for c in caps:
 old=c.pop('roles');c['diagnostic_roles']=old
 candidates=[old[r] for r in ('first_required_calculation','first_required_proof_use','first_required_task') if old[r]]
 first=min(candidates,key=lambda e:(e.get('section_order',0),e['lines'][0])) if candidates else None
 c.update({'concept_id':c['capability_id'],'name':c['description'],'type':'capability','confidence':'confirmed within indicated bounded route','first_mention':old['first_mention'],'first_concrete_explanation':old['first_informal_explanation'],'first_formal_definition':old['first_formal_definition_or_statement'],'first_demonstrated_computation':old['first_required_calculation'],'first_justified_general_rule':SUP[general[c['capability_id']]],'first_required_use':first,'later_generalizations':[SUP[k] for k in later.get(c['capability_id'],[])] or None,'rules_available':[c['description']],'prerequisite_concepts':[]})
 if c['capability_id'] in ('gs.green-circulation','gs.green-proof-typeI','gs.shoelace','gs.stokes-surface','gs.divergence-theorem','gs.vector-identities'):c['first_formal_definition']=None
 c['general_rule_status']='Supplied theorem rather than full general proof' if c['capability_id'] in ('gs.green-circulation','gs.stokes-surface','gs.divergence-theorem') else ('Claimed local proof inherits ROOT-03' if c['capability_id']=='gs.green-proof-typeI' else 'Definition, direct local algebra, or verified argument at indicated scope')
dump('concepts.json',{'snapshot':SNAP,'concepts':caps,'role_warning':'The seven top-level roles match the controlling brief; diagnostic_roles retains additional task/proof distinctions. Some roles coincide at a local introduction. First required use is the earliest evidenced calculation, proof use or task within the stated bounded route. Not a global first-occurrence certification outside this worker scope.'})
edges=[]
for r in out:
 for k in r['support']:edges.append({'from':SUP[k]['xml_id'],'to':r['task_id'],'kind':'learning','scope':'earlier or local available support for the stated task outline','from_evidence':SUP[k],'to_evidence':r['source'],'conditional':False})
proof=[]
def pe(a,b,scope,status='verified local argument'):
 proof.append({'from':SUP[a]['xml_id'],'to':SUP[b]['xml_id'],'kind':'proof','scope':scope,'status':status,'from_evidence':SUP[a],'to_evidence':SUP[b]})
pe('FUBINI','RECT_PROOF','Interchange finite rectangular integrals of continuous partials.');pe('ENTRY','RECT_PROOF','Apply one-variable FTC on opposite sides.')
pe('PARAM_LEMMA','TYPEI','Differentiate H(x)=integral_g(x)^h(x)Q(x,y)dy; endpoint chain terms.','root U03 support gap in earlier lemma proof')
pe('ENTRY','TYPEI','FTC for variable endpoint terms and integrate H prime.');pe('WORK_REVERSE','TELESCOPE','Shared oriented edges have opposite integrals.')
pe('VECTOR_DERIV','TANGENT','Full vector remainder o(norm(h,k)) gives all tangent increments, not just two coordinate curves.')
pe('IFT','REGULAR','Nonzero2x2minor gives local inverse of two output coordinates and graph for third.')
pe('SCALAR_SURF','FLUX_PARAM','Multiply unit normal by unsigned area density; exact algebra suffices after definition.')
pe('WEDGE','PULL2','Expand two pulled-back covectors and cancel repeated factors; equals cross-product components.')
pe('GREEN','STOKES_PROOF','Apply supplied Green to C1 pulled-back 1-form on compact parameter domain.')
pe('CHAIN','STOKES_PROOF','Differentiate A=F(r) dot r_u and B=F(r) dot r_v.')
pe('MIXED','STOKES_PROOF','C2 parametrization makes r_uv=r_vu, leaving curl dot cross product.')
pe('FORM_INT','STOKES_PROOF','Translate pulled-back coefficient integral to oriented surface2form integral.')
pe('MIXED','CURL_GRAD','Three mixed derivative differences vanish.');pe('MIXED','DIV_CURL','Six second derivatives cancel in three pairs.')
dump('graphs.json',{'snapshot':SNAP,'support_registry':SUP,'learning_edges':edges,'proof_edges':proof,'supplied_roots':[{'evidence':SUP[k],'scope':s} for k,s in [('GREEN','Full finite piecewise smooth-boundary theorem supplied; finite simple cases proved, general approximation explicitly only a sketch.'),('STOKES','Full compact piecewise smooth statement accepted; C2 finite-patch class independently proved.'),('DIV_THM','General curved-boundary theorem supplied; box cancellation is only mechanism/sketch.'),('IFT','Earlier inverse theorem explicitly supplied.'),('EVT','Earlier extrema theorem explicitly supplied; does not supply finite covers.')]],'missing_supports':[{'finding':'GS-01','target':SUP['GREEN_FORM'],'missing':'Explicit closed R or neighborhood of closure in the standalone restatement; inherited-context defense recorded.'},{'finding':'root U03','target':SUP['TYPEI'],'missing':'Finite-subcover principle inside earlier PARAM_LEMMA proof; no duplicate root finding.'}],'cycle_check':'No local proof cycle: coordinate surface naturality uses chain rule/mixed partials and the supplied Green theorem; it does not assume generalized Stokes or later naturality.'})
print(json.dumps({'sections':len(coverage),'tagged_exercises':len(ROWS),'candidate_rows':len(selected),'total_task_rows':len(out),'capabilities':len(caps),'learning_edges':len(edges),'proof_edges':len(proof)}))
