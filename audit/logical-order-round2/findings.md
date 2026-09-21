# Independent logical-order audit: findings

Inspected `9a9d110af839b539fe598de66ecc4320a4126af4` on `main`. Audit and proposed repairs only; textbook sources are unchanged.

The review establishes **10 required-material/background or scope corrections** (one P1, nine P2) and **four P3 clarity/navigation improvements**, at **20 primary passage occurrences**. The central P1 root is missing compactness support shared by four claimed arguments. These counts group repeated uses of the same missing capability; downstream consumers are not counted again. P3 includes the protected optional Hessian preview.

All194 active sections received a primary semantic reading. Every one of910 formal task elements has a witness; untagged projects and report instructions are also accounted for. This is an audit of learning availability and proof presentation, not a formal certification of all mathematics. See the separate [coverage](scope-and-coverage.md), [task witnesses](exercise-checks.md), and [validation](validation.md).

| ID | Priority | Root cause | Primary occurrences |
|---|---|---|---|
| LO-01 | P1 | Unprovided compactness consequences in claimed proofs | 4 |
| LO-02 | P2 | Three-covector wedge before its rule | 2 |
| LO-03 | P2 | Cylindrical and spherical integration justification bridge | 2 |
| LO-04 | P2 | Exterior derivative displayed outside its stated domain | 1 |
| LO-05 | P2 | Untaught relative connectedness criterion | 1 |
| LO-06 | P2 | Nonzero defining gradient missing from two assessments | 2 |
| LO-07 | P2 | Endpoint hint confuses one-sided feasibility with no tangent | 1 |
| LO-08 | P2 | Continuity review omits accumulation-point condition | 1 |
| LO-09 | P2 | Green restatement drops closure of the region | 1 |
| LO-10 | P3 | Optional Hessian notation preview | 1 |
| LO-11 | P3 | Basis-image checkpoint should retain linearity | 1 |
| LO-12 | P3 | Triangle-equality checkpoint omits zero-vector exception | 1 |
| LO-13 | P3 | Monte Carlo project lacks a direct sampler reference | 1 |
| LO-14 | P2 | Any-surface Stokes exercise omits compactness | 1 |

Severity is separate from confidence. The shared compactness root is P1 because required arguments explicitly presented as proofs lack a supplied premise; the late-chapter worker rated its individual local occurrences P2 because each is modest to repair. Integration retains the higher priority for the shared dependency. The exact formulas/theorems are not thereby false. The inherited-context judgments in LO-03, LO-09, LO-11 and LO-14 have more editorial uncertainty than their literal source observations.

Independent challenges tried to refute both defects and important protected judgments. See [reference against root](fragments/reference/independent-challenge-root.md), [general forms against foundations](fragments/general-forms/challenges-general-v-foundations.md), [foundations against general forms](fragments/foundations/challenges-foundations-v-general.md), [root against reference](fragments/root/challenges-root-v-reference.md), [root against Green/surfaces](fragments/root/challenges-root-v-greens-surfaces.md), and the [additional Stokes exercise challenge](fragments/root/challenge-stokes-exercise.md).

## LO-01 — Unprovided compactness consequences in claimed proofs

Worker records: ROOT-03 / GF-01. Priority P1; categories A/F/H.

- `thm-c13s5-path-independence-potential` — `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml:367–373`.
- `c13s6-lem-parameter-integral` — `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:188–214`.
- `c17s5-thm-simply-connected-potential` — `source/chapters/ch17-exterior-derivatives/sections/sec-17-closed-and-exact-forms.xml:458–468`.
- `c19s2-deriving-the-local-balance-law` — `source/chapters/ch19-conservation-laws/sections/sec-19-the-continuity-equation.xml:128–149`.

- **P1; A/F/H; confirmed local observation; high confidence.** Shared root with seeds U03/U04 and the later compact-solid differentiation step. Compactness is glossed as closed and bounded in `c9s5-subsec-boundary-constraints-compactness`, line 477. That gloss and the supplied extreme-value theorem do not supply finite-subcover or subsequence extraction principles.
- Earliest confirmed occurrence: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml`, `thm-c13s5-path-independence-potential`, lines 367–373. The proof reduces a continuous path to finitely many small pieces lying in open balls, appealing to compactness of its parameter interval. This needs a finite subdivision/Lebesgue-number consequence, not merely pointwise continuity.
- Second occurrence: the neighboring `sec-13-curl-tests-in-the-plane-and-in.xml`, `c13s6-lem-parameter-integral`, lines 188–214. At lines 197–204 a pointwise continuity construction is made uniform by a finite cover of `[c,d]`. The remaining Mean Value Theorem and integral estimate are valid once that principle is supplied.
- Additional occurrences verified by the independent late-chapter reader: Section 17.5's convergent subsequence extraction and Section 19.2's uniform estimate on a fixed compact solid; their exact records are in the general-forms fragment. The Section 19.2 step also extends an interval-integral lemma to a solid and should state that extension explicitly.
- Why P1: these are steps in arguments presented as proofs, rather than computations under an honestly supplied result or an explicitly limited geometric sketch. A required premise is absent. The theorems themselves are not disproved and the gap is repairable.
- Falsification probe: continuous `f_n(t)=n^2 t(1-t)^n` on `[0,1]` tends pointwise to zero, while its integral is `n^2/((n+1)(n+2)) -> 1`. Pointwise control alone cannot replace the uniform estimate. This sequence does not meet the stronger joint-continuity/derivative hypotheses of the parameter lemma and therefore is not a counterexample to that lemma.
- Minimal repair: add a clearly labeled supplied compactness toolbox before the first use, explaining finite-subcover, sufficiently fine path subdivision, uniform continuity on compact sets, and bounded-sequence convergent-subsequence extraction as separate consequences. State the exact Euclidean scope and use explicit references. Explain that these are supplied analysis facts, not new entry prerequisites. Extend the parameter-integral statement to continuous parameter derivatives over fixed compact piecewise smooth planar/solid regions, or give a box/Fubini argument where used.
- Preserve proof ceilings: Section 5.3's length sketch and Section 10.2's informal integrability explanation are not reclassified as full proofs. Their uniformity language deserves the toolbox cross-reference but is not counted as a separate blocking proof occurrence.

### Later occurrences and their exact scope

- **Category/priority/status:** A/F, P2, confirmed local prerequisite gap, high confidence. The mathematical theorems are true; their in-book claimed proofs contain an unavailable supporting premise.
- **Source:** `source/chapters/ch17-exterior-derivatives/sections/sec-17-closed-and-exact-forms.xml`, `c17s5-thm-simply-connected-potential`, lines 458–468: “Their centers have a convergent subsequence in the closed square (apply the bounded-sequence subsequence theorem to the two coordinates).” The ball-potential calculation at 434–448 separately invokes `c13s6-lem-parameter-integral`.
- **Required capability:** Extract a convergent subsequence in a closed bounded square, then turn continuity and openness of the target into one finite square subdivision with each cell image inside a domain ball. This is a uniform compact-domain assertion, not just continuity at an individual point.
- **Actually available:** The foundations worker's complete source pass found boundedness (`c6s4-def-bounded-region`, 465–475), closed regions (`c6s4-def-closed-region`, 477–492), and an explicitly supplied EVT (`c6s4-thm-extreme-value-theorem`, 504–532). These do not supply a bounded-sequence theorem, finite-cover theorem, or the required uniform subdivision inference. The book later uses the word compact for closed/bounded sets; the word itself is not the defect.
- **Cross-scope search witness:** Root's full Ch13 reading found an earlier unsupported occurrence at `thm-c13s5-path-independence-potential`, lines 367–373: a finite subdivision of a continuous path is attributed to compactness. Section 13.6's `c13s6-lem-parameter-integral`, lines 185–215, invokes a finite subcover to make the parameter-difference estimate uniform. These earlier uses are not available proofs of the support. Complete Ch1–8 reading plus root Ch10–15/reference-worker checking supplies the negative-search evidence; this is not a keyword-absence verdict.
- **Additional assigned occurrence:** `source/chapters/ch19-conservation-laws/sections/sec-19-the-continuity-equation.xml`, `c19s2-deriving-the-local-balance-law`, 128–149, uses uniform continuity on a compact spatial set and bounds the integrated difference quotient by `Volume(E)` times a uniform error. The estimate is correct, but the cited interval parameter lemma alone does not establish the compact-solid version without the same supporting uniformity principle. Coordinate-box localization would suffice for deriving the local law; no arbitrary-topology detour is necessary.
- **Independent proof check:** The homotopy itself is merely continuous. The endpoint of the intermediate loops may move. Replace each grid edge by its straight image-endpoint segment; adjacent cells use the identical segment, each cell's segment remains in its convex ball, local potential integrals vanish, internal segments cancel, side paths cancel, and the constant top contributes zero. The bottom arc and polygon replacements have equal local-potential integrals. This reasoning works once uniform subdivision exists. No smooth homotopy or embedded spanning surface is required.
- **Minimal repair:** Add a short shared closed-box compactness/uniform-control toolkit before the first actual use in 13.5, with an explicit link from 13.6, 17.5 and 19.2. One route proves the needed interval/box finite-cover or nested-interval lemma and derives uniform local control. Another explicitly proves bounded-sequence subsequences coordinatewise and the requisite compact-set uniform-continuity consequence. Preserve the local-potential and continuous-grid argument.
- **Downstream impact:** 13.5 polygonal paths; 13.6 rectangle potential; 17.5 global closed-1-form theorem; 19.2 derivative under a fixed spatial integral; 19.4 fixed-surface/box parameter integrations and local potentials; 19.5 circle mean proof; 19.6/20.6 uses of those correctly stated results. Applying a true supplied theorem statement remains distinct from claiming that all of its proof premises were taught.
- **Validation after proposed repair:** Check exact dimensions and neighborhoods in each lemma use; verify 17.5 still allows continuous free contractions, 19.2 still fixes E, and compactness is not silently added to entry prerequisites. Re-run source dependency/ID checks and inspect linked rendered pages. No such post-repair validation has occurred in audit-only mode.
- **Relation to prior:** Confirms U04 and the shared U03 family. Reopens prior A12/L06 “full endpoint” disposition at its supporting-analysis boundary, and L16's interval-to-volume extension. Those repairs improved the proof substantially; their remaining premise was not previously discharged.

Source excerpt for the earliest occurrence: “Compactness of the parameter interval gives a finite subdivision”. Prior A12/L06 endpoint claims are residual at this supporting-premise boundary; prior parameter-lemma and L16 fixed-volume repairs did not supply the missing compactness capability. See LO-01 task routes in13.6,14.5,17.5,19.2/19.4/19.5; these can use correctly supplied statements, but must not be described as completed proofs until repaired. Acceptance: every uniform/subsequence/subdivision step has the stated earlier lemma, correct dimension and neighborhood, and an independent noncircular proof or honest supplied status.

## LO-02 — Three-covector wedge before its rule

Worker records: ROOT-01. Priority P2; categories A/G.

- `c11s3-subsec-volume-element` — `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:126–148`.
- `c11s4-subsec-volume-element` — `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:114–127`.

- **P2; A/G; confirmed local observation; high confidence.** Seed U01, independently reproduced. Two occurrences: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml`, `c11s3-subsec-volume-element`, lines 126–148; and `sec-11-spherical-coordinates-in-integrals.xml`, `c11s4-subsec-volume-element`, lines 114–127 (same directory).
- Reader's task: append `dz` to a two-form expression, or evaluate an arbitrary triple of transformed coordinate covectors by a determinant. These require a rule of type `(V*)^3 -> Alt^3(V)`, not just the fixed coordinate form on three vectors.
- Strongest earlier support: Section 2.7 teaches two-covector wedge and the particular coordinate volume form. Section 7.5 teaches determinant volume scaling; neither supplies this product. The first sufficient rule is `c12s5-subsec-pulling-back-volume-elements`, lines 276–300, including the determinant definition and grouping convention.
- Evidence against a false positive: both early formulas are mathematically correct, and the ordinary cylindrical/spherical integrations use a supplied scalar formula rather than needing to solve a new wedge problem. Thus this is a modest local prerequisite repair, not a claim that every Chapter 11 exercise is blocked.
- Minimal repair: move these two form-comparison paragraphs into Section 12.5, retaining their unsigned coordinate factors in Chapter 11. Alternatively insert the three-covector determinant definition, multilinearity, alternating rule and grouping convention before the first calculation. Do not move a whole general exterior-algebra lesson earlier.
- Downstream review: Chapter 11 form comparisons, Chapter 12.5 volume pullbacks, and the corresponding Appendix D/E formula summaries. Keep the correct early two-wedge/fixed-coordinate-three-form distinction.

Faithful source excerpt: “So” followed by `dx wedge dy wedge dz = r dr wedge dtheta wedge dz`. Existing source/target typing is correct; this finding concerns the missing product/grouping rule. Prior M12 corrected parameter-domain notation but left this broader operation implicit. Acceptance: the early triple manipulation is removed/relocated or preceded by its actual determinant/grouping rule, and all associated task/figure/review references still resolve.

## LO-03 — Cylindrical and spherical integration justification bridge

Worker records: ROOT-02. Priority P2; categories F/H.

- `c11s3-subsec-volume-element` — `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:46–53`.
- `c11s4-subsec-volume-element` — `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:70–85`.

- **P2; F/H; confirmed local observation; high confidence.** Seed U02. The same two Section 11.3/11.4 files: `c11s3-subsec-volume-element`, lines 46–53, and `c11s4-subsec-volume-element`, lines 70–85, move from approximate tiny coordinate boxes to an exact integration formula; the cylindrical formula at lines 288–293 and spherical worked ball at lines 132–146 then use it. The Chapter 11 review's `c11s7-hook-scale-factor`, lines 826–833, says these factors were found from tiny boxes.
- Required inference: local first-order volume approximation implies a substitution theorem for the integral, with once-coverage, continuity/integrability and boundary exceptions controlled. A derivative determinant alone does not prove that inference.
- Strongest earlier support: `c10s5-thm-double-integrals-polar` (precise supplied polar theorem, lines 286–298) and `c11s2-thm-triple-integral-z-simple` (slicing theorem, lines 146–154). The polar discussion supplies a sector-area/error-bound explanation; Chapter 11 has no complete-hypothesis, explicitly supplied-status statement or slicing derivation. Chapter 12's general substitution theorem is later and cannot be the unstated proof here.
- Counterargument tested: a textbook can supply a theorem without proving it. Agreed: ordinary exercises have a formula available, and a clearly stated supplied special-case theorem would suffice. The defect is the unqualified justification/hypothesis transition, not the truth of the factors.
- Minimal repair: derive cylindrical integration by first integrating vertically and then applying the already supplied polar theorem to the planar shadow. Derive spherical integration by fixing theta and applying the same planar polar theorem in the `(r,z)` half-plane: `r=rho sin(phi), z=rho cos(phi)`. The planar unsigned factor is `rho`; the existing cylindrical factor `r` makes `rho^2 sin(phi)`. State continuous integrands, suitable piecewise smooth bounded regions, and once-coverage away from seams/axes/poles. Alternatively state these precise special cases as supplied theorems and call the tiny-box calculation geometric motivation.
- Sign check: in the ordered `(rho,phi)` variables, `det d(r,z)/d(rho,phi)=-rho`. Unsigned integration uses `rho`. The ordered spherical triple `(rho,phi,theta)` has Cartesian determinant `+rho^2 sin(phi)`. Do not conflate these signs.
- Downstream review: Section 11.7 exercises/project and Chapter 12's account of what the earlier argument established. No earlier use needs the full arbitrary-dimensional theorem.

Faithful source excerpt: “So the small piece has volume approximately” followed by “Thus the cylindrical volume element is”. Independent challenge confirmed that11.3 already displays the integral formula and warns about multiplicity at328–334. The finding is limited to justification status and complete hypotheses. It is a residual strengthening of the earlier coordinate-factor treatment. Acceptance: one explicit slicing derivation or precise supplied-special-case statement bridges local volume intuition to exact integration; ordinary task witnesses remain valid and oriented/unsigned factors remain separate.

## LO-04 — Exterior derivative displayed outside its stated domain

Worker records: GF-02. Priority P2; categories G/H.

- `c17s4-ex-c2-hypothesis` — `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-rule-d-squared-equals-zero.xml:126–174`.

- **Category/priority/status:** G/H, P2, confirmed scope/type mismatch, high confidence.
- **Source:** `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-rule-d-squared-equals-zero.xml`, `c17s4-ex-c2-hypothesis`, 126–174, especially 163–168: “at the origin using these existing second partials, we get” followed by `d(dg)=2 dx wedge dy`.
- **Required capability:** Distinguish a formal coefficient difference from an application of the book's classical exterior derivative. `c17s2-def-exterior-derivative-plane-1-form`, 142–160, defines d for C1 coefficient functions.
- **Actually available / complete check:** For `g=xy(x²-y²)/(x²+y²)` off the origin and `g(0,0)=0`, the source correctly computes `g_x(0,y)=-y`, `g_y(x,0)=x`, and hence `g_xy(0,0)=-1`, `g_yx(0,0)=1`. Off the origin, symbolic differentiation gives `g_xy(0,y)=-1` along the punctured y-axis and `g_xy(x,0)=1` along the punctured x-axis, so second derivative continuity fails. The first derivatives are homogeneous of degree one with bounded angular coefficients and extend continuously by zero; dg is a 1-form, but not a C1 1-form near the origin. Therefore the book's defined d cannot be applied to dg there.
- **Attempted refutation:** The prose already says “try to run the formula” and “The theorem did not fail. Its hypothesis failed.” This reduces severity and shows the intended diagnostic is sound. It does not type the unqualified displayed `d(dg)` as a merely formal symbol or extend the earlier operator's domain. The fix is notation/domain clarification, not a claim that the mixed-partial arithmetic is wrong.
- **Minimal repair:** Keep the function and calculations; display `g_yx(0,0)-g_xy(0,0)=2`. Say explicitly that dg is not C1 near the origin and that the classical exterior derivative of dg is not defined there in this book. Do not introduce distributions or describe this as a counterexample to d²=0 within the defined calculus.
- **Downstream impact:** Coordinate wording in 17.5's exact-implies-closed regularity warning (251–269) and any review/quick-reference mention of C2. The actual C2 proofs `c17s4-thm-d-df-zero` and `c17s4-thm-d-domega-zero` remain valid.
- **Validation:** Recheck the operator input types in the revised display and verify the unequal mixed-partial limits remain intact. Source computation independently confirmed with SymPy in this audit.
- **Relation to prior:** U06 reconfirmed. This is a residual local regularity/notation problem, not a recurrence of the earlier Maxwell d4 problem.

## LO-05 — Untaught relative connectedness criterion

Worker records: GF-03. Priority P2; categories A/F.

- `c19s5-thm-no-interior-maximum` — `source/chapters/ch19-conservation-laws/sections/sec-19-potential-theory-and-harmonic-functions.xml:376–401`.

- **Category/priority/status:** A/F, P2, confirmed local support gap, high confidence; theorem is true and proof is explicitly a sketch.
- **Source:** `source/chapters/ch19-conservation-laws/sections/sec-19-potential-theory-and-harmonic-functions.xml`, `c19s5-thm-no-interior-maximum`, 376–401, especially 393–399: the maximum set is “open in R” and “closed in R,” then “connectedness forces it to be all of R.”
- **Required capability:** Understand relative openness/closedness and the fact that a connected domain has no nonempty proper subset that is both. This differs from identifying one versus two pieces in a quadric picture.
- **Actually available/search witness:** Foundations' full Ch1–8 pass found only geometric connected/two-piece examples in `c4s4-ex-hyperboloid-one-sheet` (429–431) and `c4s4-ex-hyperboloid-two-sheets` (453–465), ordinary ambient open/closed sets, and the connected-interval ±vector argument in the torsion proof (reducible to entry IVT). No relative-set criterion is supplied there. The earlier simply connected/path-connected discussions do not themselves state/prove the clopen criterion. The assigned local passage introduces it only as an inference. Reference/root workers checked their intervening ranges.
- **Complete local mathematical check:** Let M be the attained global maximum. Every small surrounding circle has values ≤M and average M. Continuity means a strict deficit at even one circle point persists on an arc, which would make the integral average smaller. Therefore every circle point equals M. Vary the radius to obtain a whole disk. Thus the maximum set is relatively open; continuity makes it relatively closed. The final propagation is valid once the missing criterion is supplied. Mean-value differentiation separately inherits GF-01, but its planar divergence calculation is sound.
- **Minimal repair:** Briefly define the two relative notions and supply the connected-set criterion, or give an elementary propagation proof along polygonal paths with the path-existence step justified. Do not merely replace “connected” by “path connected” and silently assume the new propagation result. Keep the proof-sketch label, planar scope, C2 harmonicity, and boundary-continuity hypotheses.
- **Downstream impact:** `checkpoint-19-5-maximum-principle` can already give the local mean-value intuition; the final global explanation needs the repaired support. The harmonic-function project `c19s6-project-harmonic`, lines 500–506, uses the correct theorem statement and is solvable. Dirichlet energy minimization has a separate integration-by-parts proof and does not depend on the clopen step.
- **Validation:** Check that relative closedness is not accidentally replaced by ambient closedness and that the theorem concerns an attained global maximum in R. Re-read the checkpoint/project explanation after repair.
- **Relation to prior:** U05 confirmed; prior L20 correctly repaired dimensional/regularity scope and supplied a propagation strategy, but the strategy's elementary topology premise remains untaught.

## LO-06 — Nonzero defining gradient missing from two assessments

Worker records: REF-01. Priority P2; categories H/I.

- `checkpoint-9-1-gradient-normal-tangent-plane` — `source/chapters/ch09-gradient-optimization/sections/sec-9-the-gradient-and-level-sets.xml:239–273`.
- `checkpoint-9-5-gradients-parallel` — `source/chapters/ch09-gradient-optimization/sections/sec-9-constrained-optimization-and-lagrange-multipliers.xml:135–184`.

- **Category / priority:** H, with a local B aspect; P2. This is an underqualified assessment, not an absence of the underlying theory.
- **Status / confidence:** confirmed local observation; high confidence in the counterexamples, medium-high in classifying the brief checkpoint omissions as defects rather than inferred contextual hypotheses.
- **Occurrences:** `source/chapters/ch09-gradient-optimization/sections/sec-9-the-gradient-and-level-sets.xml:255–273`, `checkpoint-9-1-gradient-normal-tangent-plane`; and `source/chapters/ch09-gradient-optimization/sections/sec-9-constrained-optimization-and-lagrange-multipliers.xml:168–184`, `checkpoint-9-5-gradients-parallel`.
- **Faithful excerpts:** “Why does that force … to be a normal vector to the whole surface”; “on a smooth curve, why must … be parallel”. Neither checkpoint states that the defining gradient is nonzero.
- **Required capability:** distinguish a smooth geometric level set from a regular defining function, and distinguish an orthogonal zero vector from a usable normal direction.
- **What is available:** Chapter 8 gives the regular implicit-function statements (`c8s6-thm-ift-plane-curve:382–411`, `c8s6-thm-ift-surface:413–433`) and explicitly warns at `c8s6-why-the-hypotheses-matter:536–541` that `(y-x)^3=0` is a smooth line despite a zero gradient. The chain rule (`c8s1-thm-chain-rule-curve:199–247`) proves annihilation of tangent directions. In Chapter 9 the corresponding surface theorem at `304–325` and the multiplier paragraph/theorem at `186–241` restore the missing nonzero conditions, after the affected checkpoints.
- **Search and support disposition:** all Chapter 9 text, hints, examples, tables, graphics source and review tasks were read; the cited Chapter 8 sources were also read. Thus this is not a negative keyword-search claim. Earlier support actually teaches why smoothness of the set alone is insufficient.
- **Witness / counterexample:** take `F(x,y,z)=z^2` and level `F=0`. Its set is the smooth plane `z=0`, but `grad F=0` on it. Being perpendicular to every tangent direction cannot select a normal vector or determine the tangent plane through `grad F dot displacement=0` (which becomes `0=0`). For the multiplier checkpoint, set `g(x,y)=(x^2+y^2-1)^2`, `f(x,y)=x`. The constraint `g=0` is the smooth unit circle and `(1,0)` is its maximum for `f`; `grad g(1,0)=0` and `grad f(1,0)=(1,0)`, so no scalar multiplier exists.
- **Minimal repair:** add “Assume the defining function is C1 near p and its gradient at p is nonzero” before each checkpoint’s question (and make the adjoining general explanatory sentences share that scope). The first hint should say the tangent directions span a plane for a regular smooth level surface. Retain both later theorem statements and the counterexamples already taught.
- **Downstream impact:** reread the two hints, `c9s7-cc-gradient-normal`, `c9s7-cc-tangent-plane`, `c9s7-cc-constrained-condition`, the existing singular-representation exercise `c9s7-sk-parabola-constraint`, and decision-tree figure `fig-c9s7-decision-path`. The figure already says “Regular constraint”; retain it. No new lesson or relocation is needed.
- **Verification:** both squared-defining-function counterexamples must now fall outside the checkpoint hypotheses. The ordinary ellipsoid and circle examples must remain usable. Keep the distinction between singular representation and singular geometric set.
- **Prior relation:** residual scope omission following M04/M05 and the old Chapter 9 “no new defect” coverage dispositions. The kernel proof and the repaired parabola task are correct; this finding does not reopen them.

## LO-07 — Endpoint hint confuses one-sided feasibility with no tangent

Worker records: REF-02. Priority P2; categories G/H.

- `checkpoint-9-6-multiplier-misses-boundary` — `source/chapters/ch09-gradient-optimization/sections/sec-9-warning-examples.xml:179–184`.

- **Category / priority:** G/H; P2.
- **Status / confidence:** confirmed local observation; high confidence about the mathematical distinction, medium-high that the suggestive hint needs correction.
- **Source:** `source/chapters/ch09-gradient-optimization/sections/sec-9-warning-examples.xml:170–186`, `checkpoint-9-6-multiplier-misses-boundary`, especially hint `179–184`.
- **Excerpt:** “it needs a well-defined tangent direction … Ask yourself whether such a direction exists where the allowed set simply stops.”
- **Required capability:** apply the interior-extremum premise of one-variable Fermat along the feasible curve, distinguishing two-sided and one-sided feasible motion.
- **Available support:** the immediately preceding example (`c9s6-multiplier-misses-endpoint:134–168`) has `f=x` on a horizontal line segment. `c9s2-thm-fermat:229–262` and the source’s boundary examples already identify the interior-point condition. No new manifold or tangent-cone theory is needed.
- **Witness:** the segment `r(t)=(t,0)`, `-1<=t<=1`, has the same well-defined tangent line at both endpoints as in its interior. Its smooth extension has derivative `(1,0)` there. Yet `f(r(t))=t` attains an endpoint maximum at `t=1` while its derivative is `1`. The missing hypothesis is an interior point of the feasible parameter interval, where motion is possible in both tangent directions. Corners may add a separate nonunique-tangent issue.
- **Minimal repair:** replace the hint with: “The zero-derivative argument uses an interior point of the feasible curve, so motion in both tangent directions is allowed. At an endpoint only one side is feasible. Why can a one-sided maximum have a nonzero derivative? At a corner, examine the boundary pieces separately.”
- **Downstream impact:** align `c9s7-cc-endpoints-corners` and `c9s7-sk-segment` with this explanation. Keep the already correct worked segment example and endpoint checking in the optimization checklist.
- **Verification:** a student’s answer must explain the horizontal segment example without claiming its tangent disappears at the endpoint. The multiplier theorem’s C1/nonzero-gradient hypotheses alone do not remove a separately imposed segment endpoint restriction.
- **Prior relation:** newly identified within a section previously marked protected/no defect. This does not contradict the old valid conclusions about the multiplier equation or endpoint values.

## LO-08 — Continuity review omits accumulation-point condition

Worker records: FND-01. Priority P2; categories H/I.

- `c6s6-ex-cc-three-conditions` — `source/chapters/ch06-functions-limits-continuity/sections/sec-6-chapter-review-and-discovery-problems.xml:126–133`.

- **Category:** H, with an assessment inconsistency under I. **Priority:** P2. **Status:** confirmed local observation. **Confidence:** high.
- **Location:** `source/chapters/ch06-functions-limits-continuity/sections/sec-6-chapter-review-and-discovery-problems.xml:126–133`, `c6s6-ex-cc-three-conditions`.
- **Excerpt:** “State the three things that must be true for f to be continuous at a point a.”
- **Required capability:** distinguish relative continuity on arbitrary subsets from the book's punctured limit, which is defined only at accumulation points.
- **Earlier/local support search:** 6.3 `c6s3-def-formal-limit-rn`, lines 416–436, explicitly requires an accumulation point. 6.4 `c6s4-def-continuity-at-a-point`, lines 60–76, defines relative continuity and explicitly allows isolated points. The three-condition list immediately after that definition, lines 78–86, is correctly restricted to accumulation points. The review omits that restriction. This is a source comparison, not a lexical-absence inference.
- **Witness:** Let the domain be `{a}` and set `f(a)=7`. For every positive epsilon, any positive delta satisfies the continuity condition: the only domain input is a itself, with output difference zero. The book does not define the punctured limit at a because a is not an accumulation point. Thus the intended condition “the limit exists” is not necessary for continuity as defined in the chapter.
- **Minimal repair:** ask for the three conditions “at an accumulation point a of its domain.” Keep the broader definition of continuity.
- **Downstream checks:** review answer/hint, any summary repeating the three-condition test, and the earlier arbitrary-subset convention. No topology chapter is needed for this repair.
- **Acceptance criterion:** both the isolated-point example and the usual three-condition test at accumulation points agree with the prompt.
- **Relation to prior audit:** residual assessment inconsistency after the successful EA14 repair. `PREREQUISITE_AUDIT.md:46` records accumulation-point limits and isolated continuity as resolved; that judgment remains correct for the definitions, but not for this unqualified review prompt.

## LO-09 — Green restatement drops closure of the region

Worker records: GS-01. Priority P2; categories H.

- `c14s4-thm-greens-for-1-forms` — `source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-in-differential-form-language.xml:201–217`.

- **Category / priority:** H (hypothesis/scope regression), P2. **Status:** confirmed literal statement defect; contextual severity was retained after independent challenge. **Confidence:** high on the counterexample, medium on treating a standalone restatement as an actionable defect in this chapter context.
- **Exact source:** `source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-in-differential-form-language.xml:201–217`, `c14s4-thm-greens-for-1-forms`.
- **Excerpt:** “Let R be a bounded plane region whose boundary consists of finitely many piecewise smooth simple closed curves” and “a C1 1-form on an open region containing R.” The stated region need not include its boundary.
- **Required capability:** recognize that both the boundary integral and Green's identity require coefficients on an open neighborhood of the **closed** integration region, including every boundary component.
- **Earlier supplied support:** `c14s2-thm-green-circulation:86–104` explicitly says bounded **closed** region with finitely many **disjoint** boundary curves, and C1 coefficients on an open neighborhood containing that closed region. `c14s3-thm-green-flux-form:257–275` preserves that condition. Those precise theorems remain legitimate supplied results.
- **Support search and inherited-context defense:** The 14.4 opening at7–31 calls these different formulations of the same theorem and explicitly inherits positive boundary orientation from preceding sections. It does not say all hypotheses of14.2 are inherited or declare that every region in this section is closed. At199 the text introduces a “single statement”; at204 a fresh “Let R” starts its quantified hypothesis. Thus the intended meaning is clear from context, but the boxed restatement is weaker when read on its own. If the author regards all such reformulations as formally inheriting14.2, this is a precision repair rather than a new theorem failure. No missing calculus prerequisite is alleged.
- **Counterexample/witness:** Let R be the open unit disk, let U=R, and let `omega=dx/(1-x²-y²)`. R is bounded with a smooth simple closed boundary; omega is C1 on the open region U containing R, exactly as the restatement requires. But omega is undefined on the entire boundary, so its claimed boundary integral does not exist. The earlier closed-region theorem does not admit this example.
- **Minimal repair:** add “closed” to the region hypothesis and retain “disjoint” from14.2, or explicitly state “under the hypotheses of c14s2-thm-green-circulation” and require the form on a neighborhood of the closure. No chapter reorder or new proof is needed.
- **Downstream impact:** preserve the valid warning examples and source-only figure labels; check the14.4 compact theorem statement, its review summary and appendix restatements for explicit or clearly inherited closure. Existing14.2/14.3 and15.5/15.6 theorem statements already protect the boundary appropriately. The exercise witnesses use those precise earlier theorems, so no task is made impossible by this wording defect.
- **Acceptance criteria:** a direct reader of the reformulated theorem cannot substitute an open disk with a coefficient singular on its boundary. The same positively oriented boundary convention and local exterior derivative definition remain intact.
- **Relation to previous dispositions:** old M21 repaired closure/disjoint scope in14.2 and distinguished finite simple-region proof from the general sketch; M22 aligned14.3. This is a residual consistency issue in14.4, not a reopening of their corrected statements or proof ceilings.

## LO-10 — Optional Hessian notation preview

Worker records: U07. Priority P3; categories C.

- `c3s6-subsec-hessian-preview` — `source/chapters/ch03-linear-functions-matrices/sections/sec-3-quadratic-forms-and-symmetric-matrices.xml:493–555`.

The Section3.6 passage explicitly ends “This is only a preview.” It displays second-partial subscripts before they are taught, but no required task here uses them. Chapter9 supplies the needed definitions before its Hessian work. Classification C/P3, seed U07: protected as a preview, with optional notation clarification. A minimal added sentence is: “The entries of H will be defined in Chapter9; for now, regard H simply as the symmetric matrix describing the quadratic bending.” Retain the earlier quadratic-form lesson and its examples. Verify that required reviews do not import the preview notation; the task witnesses found no such leak. This is an optional refinement, not a recurrence of a blocking dependency.

## LO-11 — Basis-image checkpoint should retain linearity

Worker records: FND-02. Priority P3; categories H/I.

- `checkpoint-3-2-basis-determines-all` — `source/chapters/ch03-linear-functions-matrices/sections/sec-3-linear-transformations-r-n-r-m.xml:241–258`.

- **Category:** H/I. **Priority:** P3. **Status:** confirmed wording observation; limited by strong contextual support. **Confidence:** high about literal wording, medium that a reader would misunderstand it.
- **Location:** `source/chapters/ch03-linear-functions-matrices/sections/sec-3-linear-transformations-r-n-r-m.xml:241–258`, `checkpoint-3-2-basis-determines-all`.
- **Excerpt:** “only the n output vectors … and nothing else about T … enough information to predict T(x) for every possible input”.
- **Required capability:** basis values determine a map only when linearity is known.
- **Earlier/local support search:** the correct theorem `c3s2-thm-determined-by-basis`, lines 191–213, assumes linearity. The immediately preceding `c3s2-ex-without-linearity`, lines 218–235, explicitly gives the counterexample. The checkpoint hint invokes the two linearity rules, so there is no missing theory and no genuine need to move the exercise.
- **Witness:** `I(x,y)=(x,y)` and `N(x,y)=(x²,y)` agree on e1 and e2, but give `(2,0)` and `(4,0)` at `(2,0)`. If T is known linear, expansion `x=sum xj ej` gives `T(x)=sum xj T(ej)` immediately.
- **Minimal repair:** start “Suppose T is linear, and you are told its n basis images.” Remove “nothing else about T,” or qualify it as no further values.
- **Downstream checks:** only the checkpoint wording/hint. Preserve the theorem and explicit counterexample.
- **Acceptance criterion:** a reader can state precisely which assumption excludes N.
- **Relation to prior audit:** newly recorded refinement, not a reopening of the correct matrix/basis development. This is not a required-prerequisite gap.

## LO-12 — Triangle-equality checkpoint omits zero-vector exception

Worker records: FND-03. Priority P3; categories H/I.

- `checkpoint-1-5-triangle-equality` — `source/chapters/ch01-points-vectors-space/sections/sec-1-norm-distance-and-spheres.xml:346–363`.

- **Category:** H/I. **Priority:** P3. **Status:** confirmed local observation. **Confidence:** high.
- **Location:** `source/chapters/ch01-points-vectors-space/sections/sec-1-norm-distance-and-spheres.xml:346–363`, `checkpoint-1-5-triangle-equality`.
- **Excerpt:** equality occurs “exactly when u and v point the same way.”
- **Required capability:** equality includes a zero leg, which has no direction.
- **Earlier/local support search:** the immediately preceding discussion at lines 336–341 already includes the zero-vector case. The later independent proof `c2s4-cor-triangle-inequality`, 2.4 lines 539–554, again covers zero vectors. The checkpoint is the lone narrower paraphrase.
- **Witness:** u=0 and v=(1,0) give `norm(u+v)=norm(u)+norm(v)=1`, although zero does not point any way. In the hiker picture, coincident cabin/lake or lake/lookout is a degenerate straight journey with equality.
- **Minimal repair:** append “or one is zero,” or restrict the two displacements to be nonzero before stating the equality characterization.
- **Downstream checks:** only this checkpoint and any answer paraphrase; preserve the all-dimensional Cauchy–Schwarz proof and exact deferred reference.
- **Acceptance criterion:** both zero-leg cases and positive collinear nonzero legs satisfy the characterization, while opposite nonzero legs do not.
- **Relation to prior audit:** residual checkpoint inconsistency after EA03; `PREREQUISITE_AUDIT.md:35` correctly records that the main statement and later proof were repaired.

## LO-13 — Monte Carlo project lacks a direct sampler reference

Worker records: GF-04. Priority P3; categories I.

- `c20s3-proj-monte-carlo` — `source/chapters/ch20-capstone-projects/sections/sec-20-integration-projects.xml:1035–1128`.

- **Category/priority/status:** I, P3, confirmed navigation improvement; no established blocking mathematical dependency, medium-high confidence.
- **Source:** `source/chapters/ch20-capstone-projects/sections/sec-20-integration-projects.xml`, `c20s3-proj-monte-carlo`, 1035–1064 (independent uniform samples and estimator) and 1120–1128 (generate samples and compute several N). No local pointer to the sampler appears in the project or Ch20 wrapper.
- **Required capability / actual support:** The estimator and zero extension are locally given. Ch10.6 probability density (`c10s6-subsec-probability-density`, 324–387, root's complete reading) teaches region probabilities, not generating independent uniform coordinates. Later `source/appendices/appG-computational-labs/sections/sec-appG-numerical-double-and-triple-integration.xml`, `appG-numint-monte-carlo-estimate`, 189–213, supplies exactly the operational code using two `np.random.uniform` calls and a domain mask. The Appendix G wrapper identifies it as a computational quick reference.
- **Minimal repair:** Add a direct, descriptive xref from the required sampling step to `appG-numint-monte-carlo-estimate`, with one sentence explaining independent coordinate draws in a rectangular box. Optional three-dimensional sampling extends the coordinate recipe directly. Do not add a probability theory chapter or require proof of convergence: the current task asks empirical reliability and comparison.
- **Downstream impact/validation:** Verify the project still divides by total N, evaluates f only inside its domain, and records run-to-run variability without promising monotonic convergence. Update the capstone navigation and keep Appendix G's mask/broadcast safeguards.
- **Relation to prior:** New navigation observation after prior L26/L42 repairs. Their statistical sampling assumptions and domain-restricted computation are substantively correct and retained.

## LO-14 — Any-surface Stokes exercise omits compactness

Worker records: GF-05. Priority P2; categories H/I.

- `c18s10-ex-pr-any-surface` — `source/chapters/ch18-generalized-stokes/sections/sec-18-chapter-review-and-capstone-problems.xml:519–528`.

- **Category/priority/status:** H/I, P2, confirmed task hypothesis gap, high confidence; independently challenged and retained by root after checking wrappers and surface definitions.
- **Source:** `source/chapters/ch18-generalized-stokes/sections/sec-18-chapter-review-and-capstone-problems.xml`, `c18s10-ex-pr-any-surface`,519–528: “Let S be any smooth upward-oriented surface whose boundary is the circle” x²+y²=1,z=0, then asks for the integral of3dx wedge dy.
- **Available support:** `c18s2-thm-generalized-stokes`75–82 and `c18s5-thm-classical-stokes-as-generalized`290–298 expressly require compactness. `c15s1-def-parametric-surface`95–108 allows an arbitrary parameter region D subset R2. Neither the chapter wrapper nor the review introduction supplies a standing all-surfaces-compact convention. The fact that prior worked spanning surfaces are compact does not impose that missing quantifier.
- **Complete witness:** The intended compact upward spanning surface gives3pi, since3dx wedge dy=d(3xdy) and the induced circle is CCW. But S={(x,y,0):x²+y²>=1}, with normal(0,0,1), is a smooth upward-oriented surface with the stated geometric boundary. Its induced circle is clockwise. Its integral is not finite: truncating at radiusR gives3pi(R²-1), tending to infinity. Thus the literal task has no unique finite answer and the stated Stokes theorem cannot be applied.
- **Attempted refutation:** A compactness convention could rescue the exercise. Both this worker and root checked the actual definitions/wrapper/theorem context and found none. The immediately preceding compact hemisphere problem does not restrict a new “any” surface. This is a specific scope omission, not a demand to repeat every routine smoothness convention in all exercises.
- **Minimal repair:** Say “any compact smooth upward-oriented surface” and, for clarity, require its induced boundary orientation to be the counterclockwise unit circle. Retain the intended3pi computation and its purpose: exact-form integral depends only on the oriented boundary under the theorem hypotheses.
- **Downstream impact/validation:** Update this exercise's answer/witness and any same-boundary review paraphrase; compare with the correctly scoped `c18s10-ex-pr-exact-no-boundary`, which already specifies compact S. Verify the exterior-plane probe is excluded while disk/hemisphere examples remain admissible.
- **Relation to prior:** New residual assessment-scope observation, discovered during adversarial checking of an initially supported task witness. The earlier theorem-scope repairs L09/L10 are correct; this review problem did not inherit their full hypotheses.

The late-chapter worker assigned P2 locally; consolidated LO-01 records the shared P1 classification. This is not a claim of full-book correctness: all source figures were read but rendered output was not inspected by this worker, and the independent challenge is separately recorded.

## Protected repairs and remaining uncertainty

The author-directed5.2 lesson is preserved. Its ordinary frozen-parameter velocities, regular parameter points, cone/plane contrast and later full tangent-plane proof form a valid sequence. The2.7 two-covector wedge,3.4 independent determinant proof,7.2 gradient derivation, supplied inverse theorem, Gaussian bounded-limit argument, correct multiplicity warnings, surface naturality, and optional Maxwell Hodge preview survived independent challenge.

No known task is left without an outline or explicit defect disposition. Most figures were read in source only. Rendered5.2 was spot-checked; whole-book image layout and print output were not checked. Subjectively, confidence is high in the listed local evidence and broad source coverage, and moderate that this pass found every subtle prerequisite issue; that estimate is editorial judgment, not numerical or mathematical certification. The old preface placeholder and optional “nonempty” cleanup in9.5 are recorded in the reference fragment but are not inflated into additional logical root causes.