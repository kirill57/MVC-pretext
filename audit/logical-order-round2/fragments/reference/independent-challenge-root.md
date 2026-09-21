# Independent challenge of the root Chapter10–13 records

Reviewer: reference/Green–surface worker. Snapshot `9a9d110af839b539fe598de66ecc4320a4126af4`. This is a bounded adversarial check of the root's findings and selected supported judgments, not a second semantic certification of all30 root sections. Root records were read only after this worker's primary Chapter9/14/15/appendix scope was completed. The source windows below were then independently reread.

## Findings challenge

| Finding | Attempted falsification | Result |
|---|---|---|
| ROOT-01 | Could the coordinate3form definition in2.7, plus ordinary determinant properties, already teach arbitrary triple covector multiplication? Reread `c2s7-def-wedge-linear-measurements:297–317`, its two-factor rules, and `c2s7-def-volume-form-dx-dy-dz:433–446`. Compare11.3:126–148 and11.4:114–127 with12.5:276–300. | **Survives, P2.** The first is a bilinear product of1-input measurements; the second separately defines one fixed coordinate3-input measurement. Neither gives the missing product of an arbitrary2form with a1form.12.5 explicitly supplies the determinant of three covector rows and the grouping convention. The later definition is precisely what the earlier operation needs. The volume formulas themselves remain correct and available. |
| ROOT-02 | Is a boxed formula already a legitimate supplied theorem, making a proof-gap finding an overreach? Read all of11.3 and11.4, including the general cylindrical formula at288–293 and the once-coverage/seam warning at328–334. | **Survives only with root's narrow qualification, P2.** It is inaccurate to say no exact formula or no multiplicity guidance was supplied. Both exist. The defensible issue is that the tiny-box approximation is presented as yielding an exact integration rule without identifying that rule as a supplied special case with the hypotheses and proof ceiling made explicit. The ordinary exercises are solvable using the displayed rule. Either a short slicing derivation or an explicit supplied-special-case paragraph is sufficient; no full general substitution proof is required. Confidence in the mathematical distinction is high; editorial necessity is more contextual than ROOT-01/03. |
| ROOT-03 | Does the earlier EVT or “compact means closed and bounded” gloss supply the finite subdivision/finite-subcover capability? Independently reread13.5:350–396 and13.6:185–215; compare the already audited6.4 EVT and9.5 compactness paragraph. | **Survives, P1 under the campaign's proof-support criterion.** The13.5 proof explicitly invokes finite path subdivision inside balls;13.6 explicitly invokes finitely many covering neighborhoods to choose a common positive increment bound. Neither is the statement of EVT. A proof could derive related compactness consequences from other analysis facts, but those derivations are not written or declared entry preparation. The actual parameter-integral lemma is true under its strong hypotheses; the root correctly does not call its pointwise-sequence probe a counterexample to that lemma. |

For ROOT-02, the coordinate-order sign check is correct: with `(r,z)=(rho sin(phi),rho cos(phi))`, the ordered planar determinant is `-rho`; unsigned area uses `rho`. Multiplying by the cylindrical scalar weight `r` yields `rho² sin(phi)`. In Cartesian space, the triple parameter order `(rho,phi,theta)` has positive determinant `rho² sin(phi)`. The proposed slicing route is noncircular because polar integration and finite Fubini precede Chapter11.

For ROOT-03, later17.5/19.2 occurrences were not independently reread by this reviewer; their challenge belongs to the late-chapter worker's scope. The local13.5/13.6 occurrences alone establish the shared missing-support finding. This fragment does not extend the negative-support search to unread later material.

## Challenged supported judgments

- **Gaussian squeeze:** independently recomputed the inclusions `disk(R) subset square([-R,R]²) subset disk(sqrt(2)R)`. Positivity gives `pi(1-exp(-R²))<=I_R²<=pi(1-exp(-2R²))`; the common limit is pi. Only bounded-domain Fubini is needed before passing to the scalar limit. The root's nonissue is sound.
- **Surface naturality dependency used downstream:** the supplied Green theorem can be used in15.5 despite its general proof ceiling. The15.5 C2 chain-rule calculation is independent of later generalized Stokes. Thus ROOT-03's dependency in14.5 does not create a false circularity or make15.5's coordinate algebra unavailable.
- **Triple-coordinate versus arbitrary triple-wedge:** an11.1 task merely evaluating the fixed Cartesian volume form is supported by2.7. ROOT-01 must remain limited to transforming arbitrary covector expressions in11.3/11.4.
- **Numerical project:** all finite sums and sample centers are locally supplied in `c11s7-project-method-cubes`, `...-cylindrical`, and `...-spherical`. Recomputed the12 displayed entries, shown below. No hidden numerical-analysis theorem is needed to compute and compare these values. The explanation of observed error behavior should remain observational, not a general rate theorem.
- **Probability tasks:** the density/nonnegativity/total-one rule is explicitly local in11.5/11.7; elementary normalization and subregion integration do not require a prior probability course.
- **Documentation correction sent to root:** root proof-status originally said the shoelace endpoint was14.3. The actual explicit endpoint is14.7, `c14s7-ex-shoelace`. This is an audit-artifact correction, not a textbook finding.

## Independently solved high-risk arithmetic

| Source ID | Independent check | Result |
|---|---|---|
| `c11s7-example-wedge` | With h=4-x-y, mass is integral(h+h²/2) on `[0,2]x[0,1]`; area2, average h=5/2, average h²=20/3. | `35/3`, agrees with current root/source. |
| `c11s7-example-round-tank` | `2pi integral_0^2 (1+r)r(3+r/2)dr=2pi(6+28/3+2)`. | `104pi/3`. |
| `c11s7-example-spherical-cone` | Angular integral `2pi(1-cos(pi/3))=pi`; radial integral to2 is4, to1 is1/4. | `C=1/(4pi)`, probability `1/16`. |
| `c12s7-subsec-slanted-window` | Inverse determinant `-1/2`; integrate `u/2` over `[1,3]x[0,2]`. | `4`. |
| `c12s7-subsec-curved-plate` | Forward determinant `2y/x=2v`, inverse `1/(2v)`; integrate `u/(2v)`. | `15ln(3)/4`. |
| `c12s7-subsec-stretched-ball` | Scaling determinant6, spherical radial integral `1/3+1/5`. | `6*4pi*(8/15)=64pi/5`. |
| `c12s7-ex-sk-variable-ceiling-volume` | Directly integrate `x(1+y)` over `[1,2]x[0,1]`. | `(3/2)(3/2)=9/4`. |
| `c11s7-sk-19` | Unit cube integral of x+y+z is3/2; lower-half-z integral is5/8. | `C=2/3`, probability `5/12`. |
| `c12s7-ex-sk-circular-plate-mass` | `2pi integral_0^3(10-r²)r dr`. | `99pi/2`, density remains nonnegative. |

Recomputed numerical results from the literal midpoint/cube formulas using Python standard-library arithmetic:

| N | cube centers | cylindrical midpoint | spherical midpoint |
|---:|---:|---:|---:|
|4|4.000000000000|4.345299907231|4.123340357837|
|8|4.375000000000|4.242763558142|4.172427743049|
|16|4.250000000000|4.207384660632|4.184699589352|
|32|4.212890625000|4.195215959053|4.187767550928|

All agree with the source table rounded to five decimal places. The spherical estimate has the smallest absolute error in these four rows. No source changes were made during this challenge.
