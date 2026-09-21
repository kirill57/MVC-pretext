# Ordered repair plan: first-year core with optional fuller justifications

This proposal now follows [MVC-pretext-first-year-repair-addendum.md](../../MVC-pretext-first-year-repair-addendum.md). **Textbook implementation remains pending.** The addendum calls itself a “revised editorial recommendation, not authorization to modify the repository.” This update changes the planning artifact only; it does not implement or build textbook changes.

Current HEAD was rechecked as `9a9d110af839b539fe598de66ecc4320a4126af4`. Exact audited source locations and hashes remain in [findings-index.json](findings-index.json). Preserve the [original audit proposal](repair-plan-original-audit.md) and the [earlier guided-proof draft](repair-plan-guided-proofs-draft.md) as history. The first-year addendum supersedes that draft's required compactness sequence, required topology exercise, broad decomposition wording, and default assessment of the early triple-wedge connection.

## Instructional contract and four statuses

The core route assumes algebra, trigonometry and single-variable calculus. It does not assume compactness proofs, subsequences, open covers, homotopy, exterior algebra or formal epsilon–delta proof construction. Teach necessary vectors and linear algebra where the book currently develops them. Preserve the Section 5.2 ordinary surface-grid velocities and the later tangent-plane justification; keep Section 4.5 geometric.

| Status | What must be visible to the student |
|---|---|
| Definition | Meaning, inputs, outputs and conventions before operational use. A sufficient worked introduction can do this. |
| Available theorem | Correct statement and usable hypotheses. It may be used even when its proof is optional or omitted. |
| Guided justification | A scoped claim, earlier tools, explicit scaffolding and a checked solution. State precisely which case is proved. |
| Optional connection or proof | Clear enrichment label and navigable references. No core task may depend solely on this material. |

Keep geometric explanations and useful advanced connections. Retain short, accessible proofs that are already sound. Do not replace every proof by an exercise, and do not make a large proof course compulsory merely by dividing it into small parts.

Suggested status wording:

> We will use the following theorem. The guided exercise explains the mechanism for the stated special case. The general theorem is stated without proof on the core route; a fuller optional justification is linked separately.

Use that wording only where it accurately describes the material. If the exercise really proves the full stated claim, say so. A correct statement supplied for use terminates the core proof dependency; a hidden solution or optional definition does not supply a missing operation. Correct false statements and ill-typed formulas directly.

## 1. LO-01: supply the next needed fact, make the analysis project optional

**First source:** `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml`, before `thm-c13s5-path-independence-potential`.

### Core path argument in 13.5

Do not insert the four compactness proof exercises from the earlier draft here. Introduce only the path-subdivision fact needed for polygonal paths, with a geometric explanation: a continuous path on a closed interval can be cut into sufficiently short pieces, each lying in a small ball inside the open domain.

Proposed theorem ID: `c13s5-thm-path-subdivision`. State it for a continuous path `gamma:[a,b] -> D`, where D is open. There is a positive delta such that every nonempty closed subinterval J of length below delta has its image inside an open ball contained in D. Explain continuity at endpoints relative to `[a,b]`, and recall that an open domain leaves a small ball around each of its points. The theorem is supplied for core use. Do not introduce homotopy notation for this path application.

Keep the short argument that each small path segment can be replaced by its straight chord within the same ball. Cite the supplied subdivision theorem. Do not advertise the optional compactness proof as required prior learning or claim EVT alone proves the subdivision fact.

### Parameter integrals in 13.6

**Source/ID:** the neighboring `sec-13-curl-tests-in-the-plane-and-in.xml`, `c13s6-lem-parameter-integral`.

Keep a precise available theorem: q and its partial derivative in the parameter are continuous on a neighborhood of a closed rectangle; the integration interval `[c,d]` is fixed; the parameter value is interior. Then

`H(x)=integral_c^d q(x,t) dt` has derivative `integral_c^d q_x(x,t) dt`.

Explain the mechanism without a required compactness proof: one bound makes the difference-quotient error small for every t at once, and the integral error is at most `(d-c)` times that bound. Supply this uniform-control fact explicitly as part of the justification's stated background. Keep the valid MVT estimate where it remains accessible. Label the fuller analysis proof as optional; pointwise convergence is not a replacement for uniform control.

Prefer one core illustration, `c13s6-ex-parameter-integral-two-routes`, over a general proof assignment. For

`H(x)=integral_0^1 (x t^2 + x^2 t) dt`,

ask students to integrate then differentiate, differentiate the integrand then integrate, and check the hypotheses in words. Checked result: `H(x)=x/3+x^2/2`, and both derivative routes give `1/3+x`. Label this an illustration, not a proof of the general interchange theorem.

### Rectangle subdivision and the fuller potential proof in 17.5

**Source/ID:** `source/chapters/ch17-exterior-derivatives/sections/sec-17-closed-and-exact-forms.xml`, `c17s5-thm-simply-connected-potential`.

Keep the correctly scoped theorem available for use. At the actual rectangle/homotopy application, supply the corresponding subdivision fact: for continuous `H:P -> D`, with P a closed bounded rectangle and D open, some delta ensures that every nonempty closed cell Q contained in P with diameter below delta has H(Q) inside one open ball contained in D. Explain a cell and its diameter. This is not asserted to follow from a finite subcover alone.

Retain the valid radial-potential, continuous-homotopy and polygonal-cancellation proof as an explicitly optional fuller route, with sufficient local explanations of its advanced notions. Preserve semantic theorem IDs and add a separate proof-subsection ID if necessary. Update the 13.6 forward reference to describe its optional destination accurately. Do not replace a continuous contraction with an unjustified embedded spanning surface.

### Fixed-region differentiation in 19.2

**Source/ID:** `source/chapters/ch19-conservation-laws/sections/sec-19-the-continuity-equation.xml`, `c19s2-deriving-the-local-balance-law`.

State the fixed-region version for the already taught bounded integration regions. With continuous density and continuous time derivative on a neighborhood of the relevant closed spatial/time product, differentiate by integrating that time derivative. Use **area** or **volume**, not an undefined general measure. Explain the bound as the region's volume times a common difference-quotient error. The region is fixed; moving regions require additional terms and are not included.

Check the uses in 14.5, 19.4 and 19.5. Each must cite an available statement with the right dimension and hypotheses, not require the optional analysis project. Preserve the existing fixed-domain and regularity qualifications.

### Optional compactness investigation

**Proposed location:** a clearly labeled optional section in Appendix F, `source/appendices/appF-proof-sketches/sections/sec-appF-uniform-control-investigation.xml`, included from `appF-proof-sketches.ptx`. Proposed section ID: `sec-appF-uniform-control-investigation`. This is a planned file, not an existing source or an implementation claim.

Retain the earlier draft's material here as enrichment, with local definitions, announced scaffolding and complete checked solutions:

1. `appF-ex-compact-subsequence`: define subsequences and supply the nested closed interval fact. Guide the nested-box construction, increasing-index selection, convergence and closed-set limit argument.
2. `appF-ex-uniform-continuity`: state the quantifiers, construct the two contradicting sequences, and use the previous result to prove uniform continuity on a closed bounded set.
3. `appF-ex-finite-cover-control`: define an open cover, prove the uniform local cover-radius consequence using a bad-center sequence, and derive a finite subcover using a finite grid. Give the cell-diameter estimate.
4. `appF-ex-path-grid-subdivision`: prove the interval and rectangle subdivision facts through shrinking bad cells and continuity at a subsequential limit. Explain why every point of a sufficiently small cell approaches that same parameter limit.

Keep the nested-interval completeness fact honestly supplied unless separately proved. Optional exercises may depend on named earlier optional exercises; disclose those dependencies. Nothing in the core route requires completing this investigation. The Appendix F introduction should distinguish these complete guided arguments from its existing limited sketches.

**Acceptance:** hide the entire optional investigation and the fuller homotopy proof. Every core potential, parameter-integral and conservation-law task still has a precise theorem, defined notation and a viable solution route.

## 2. LO-04: correct the operator-domain warning without a new regularity hurdle

**Source/ID:** `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-rule-d-squared-equals-zero.xml`, `c17s4-ex-c2-hypothesis`.

Retain the example and its correct mixed-partial arithmetic. Replace the display asserting `d(dg)=2 dx wedge dy` at the origin by `g_yx(0,0)-g_xy(0,0)=2`.

Model explanation:

> This function has a differential, but the coefficients of dg are not continuously differentiable near the origin. Thus our defined exterior derivative cannot be applied to dg there. The scalar difference of mixed partials is 2; it is not a value of d-squared within its stated domain.

Visibly supply the regularity facts used by this explanation. A guided challenge may ask for the two axis mixed-partial calculations and diagnosis of the missing hypothesis. Put the complete estimate establishing continuity of the first derivatives in its checked solution or an optional final part, with a usable hint. Do not require that estimate merely to understand the main warning. Do not introduce distributions.

Check 17.5 and all related review/appendix paraphrases. Preserve the valid C2 identities and elementary mixed-partial calculations elsewhere.

## 3. LO-03 and LO-02: Chapter 11 calculus first, visible optional forms connection

**Sources:** `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml` and `sec-11-spherical-coordinates-in-integrals.xml`.

### Core integral formulas and scoped guided derivations

Keep the tiny-box motivation, correctly stated exact formulas and applications. Explicitly supply the general formulas with continuous-integrand, region and once-coverage hypotheses. Preserve seam, axis and pole qualifications. State which special case each exercise proves; do not describe a ball-volume consistency check as a proof for arbitrary integrands and regions.

For `c11s3-ex-justify-cylindrical-integration`, start with the explicit solid

`x^2+y^2 <= 1, 0 <= z <= 1`.

Let f be continuous on a neighborhood of this closed solid. Give the Cartesian slicing formula, define `G(x,y)=integral_0^1 f(x,y,z) dz`, and apply the already supplied planar polar theorem to G. Supply the elementary continuity fact needed for G if it has not been established. The conclusion proves the cylindrical formula for **every such f on this specified cylinder**, not just for f=1. If using variable vertical limits in an extension, state the needed continuity-of-the-integral fact explicitly.

For `c11s4-ex-justify-spherical-integration`, use the explicit ball `x^2+y^2+z^2 <= R^2`, R positive, and give its cylindrical bounds. The earlier supplied cylindrical theorem makes that starting formula available; the exercise does not depend on proving every cylindrical case. At fixed theta, the `(r,z)` domain is the right half-disk `r>=0, r^2+z^2<=R^2`. Apply planar polar substitution with

`r=rho cos(psi), z=rho sin(psi), -pi/2<=psi<=pi/2`.

Then set `psi=pi/2-phi`, explain reversal of the one-variable bounds, and obtain `0<=phi<=pi`. The unsigned planar factor rho multiplied by the existing r gives `rho^2 sin(phi)`. This proves the spherical formula for **every continuous f on the specified ball**, with the stated neighborhood assumptions. The case f=1 then checks the familiar ball volume.

An optional extension may use an explicitly displayed finite decomposition with all pieces and bounds supplied. Do not ask students to prove that every bounded piecewise-smooth region admits such a decomposition; that claim is not justified by the words “piecewise smooth.” Keep the general supplied theorem and the exercise's proved special case distinct.

### Optional “Oriented-volume connection”

Keep short, clearly labeled connections in `c11s3-subsec-volume-element` and `c11s4-subsec-volume-element`. Before arbitrary triple products, define three covectors as linear scalar measurements on the **same** vector space. Give their determinant evaluation on an ordered triple of vectors. For variable coefficients, explain that this evaluation occurs pointwise at a fixed parameter point.

Declare `(alpha wedge beta) wedge gamma` to mean this particular triple determinant. State the multilinearity and alternating rules used in the displayed calculation. Do not claim that this grouping convention proves the general wedge algebra or associativity in all degrees.

Classify `c11s3-ex-three-measurement-volume` as an **extension exercise** unless the author later explicitly makes this early strand assessed core content. It can derive the local rules from the determinant and verify the cylindrical identity. Provide a checked solution, but keep ordinary integration examples independent of it. Section 12.5 should recall this introduction when developing systematic pullbacks; retain the later forms chapters.

In the optional spherical connection, check all three distinct statements:

- `(rho,phi) -> (r,z)` has signed determinant `-rho`.
- `(rho,phi,theta) -> (x,y,z)` has signed determinant `+rho^2 sin(phi)`.
- Ordinary volume uses an absolute determinant.

If composing the maps, explicitly swap from `(r,z,theta)` to `(r,theta,z)`: that one transposition changes `-rho` to `+rho`, which then multiplies the cylindrical determinant r. Scalar iterated integration order is not an orientation convention.

**Downstream:** check the 11.7 review/project, 12.5 introduction, hints, captions and visible labels. No core item may require an operation defined only in the optional connection. Keep the early 2.7 two-covector lesson and fixed coordinate volume form intact.

## 4. LO-05: circle averaging in the core, global topology optional

**Source/ID:** `source/chapters/ch19-conservation-laws/sections/sec-19-potential-theory-and-harmonic-functions.xml`, `c19s5-thm-no-interior-maximum`.

Keep the correct planar maximum-principle statement with C2 harmonicity, connected-domain and attained-maximum hypotheses. Define harmonic and explain C2 through available derivatives. State the global result for use and explain geometrically why a highest temperature cannot be isolated in an otherwise cooler surrounding region.

Use a short guided exercise, `c19s5-ex-averaging-forces-local-constancy`:

1. A continuous temperature on a circle is everywhere at most M and has average M. A strict deficit at one point persists on an arc of positive length; show that it would make the average smaller.
2. At a maximum point of a harmonic function, apply this argument to **every sufficiently small centered circle**. Conclude constancy on a disk around that point.

This is the local part of the argument. One circle does not establish a whole disk, and one disk does not establish the whole connected domain. Supply the global propagation fact on the core route; do not pretend the local exercise proves it.

Retain the relative-open/relative-closed proof in an optional subsection, proposed ID `c19s5-optional-global-propagation`. Define the relative notions and connectedness there, then prove that the maximum set is nonempty, relatively open and relatively closed and must be the whole connected domain. Provide scaffolding and a checked proof. Preserve a correct existing short argument if it already meets these conditions; no required topology module is needed.

Check the maximum-principle checkpoint and harmonic project against the supplied theorem. The circle-mean derivative separately uses the available parameter-integral result from LO-01. The optional proof must not be the sole source of a required theorem's hypotheses or conclusion.

## 5. Retain the direct correctness repairs — LO-06–09 and LO-14

Exact paths for these existing IDs are in findings-index.json. Repair the statement, nearby explanation, prompt, hint, solution and review consistently.

| Object | Required repair | Diagnostic check |
|---|---|---|
|9.1 `checkpoint-9-1-gradient-normal-tangent-plane` and nearby prose at 239–253|Require a defining function with continuous first partials near the point and nonzero gradient. Explain C1 if necessary.|Compare F=z and G=z^2 on their common zero plane; the first gradient is (0,0,1), the second zero.|
|9.5 `checkpoint-9-5-gradients-parallel` and preceding prose|Require nonzero constraint gradient, but allow the objective gradient to be zero. State proportionality, including multiplier zero.|The squared-circle defining function fails the regularity assumption; zero objective gradient remains a permitted case. Avoid two nonzero “parallel directions” as the universal explanation.|
|9.6 `checkpoint-9-6-multiplier-misses-boundary` hint|Ask which signs of a small parameter change remain feasible.|A segment endpoint can have a tangent line but only one-sided allowed motion; the interior stationary-point test need not hold.|
|6.6 `c6s6-ex-cc-three-conditions`|Qualify the punctured-limit criterion at accumulation points, explaining that other domain points occur arbitrarily nearby.|A function on a singleton is continuous under the relative definition without the book's punctured limit.|
|14.4 `c14s4-thm-greens-for-1-forms`|Explicitly inherit the full taught Green hypotheses: bounded closed region, the stated boundary conditions/orientations, and C1 coefficients on an open neighborhood containing the region **and boundary**.|The open-disk example with coefficients singular on its boundary is excluded. Adding “closed” alone is not a substitute for the neighborhood requirement.|
|18.10 `c18s10-ex-pr-any-surface`|Use a permitted compact oriented spanning surface with the counterclockwise unit circle as induced boundary; verify the form/field is sufficiently regular on a neighborhood of that surface.|For the actual form 3 dx wedge dy, the primitive 3x dy is smooth everywhere. On the circle x=cos(t), y=sin(t), its integral is `3 integral_0^(2pi) cos^2(t) dt=3pi`. The unbounded exterior plane is excluded.|

The addendum itself did not independently verify the last numerical answer. The audit already did, and the displayed primitive/boundary calculation provides the explicit check for the planned repair. Do not generalize surface independence across a singularity or outside the theorem's domain.

## 6. Small notation/navigation edits and a restrained problem workload

Retain the LO-10–13 edits, distinguishing optional pedagogy from necessary correctness:

- **LO-10, optional notation clarity:** in `c3s6-subsec-hessian-preview`, explain that Chapter 9 defines the second-partial entries. Keep the preview dispensable.
- **LO-11, correctness:** in `checkpoint-3-2-basis-determines-all`, state that T is linear and replace “nothing else about T” with “no further values of T.” Keep the nonlinear counterexample.
- **LO-12, correctness:** in `checkpoint-1-5-triangle-equality`, include a zero-vector case or explicitly assume both vectors nonzero. Small size and P3 audit priority do not make this correctness edit dispensable.
- **LO-13, navigation:** link `c20s3-proj-monte-carlo` directly to `appG-numint-monte-carlo-estimate`, with independent uniform coordinate draws explained. Preserve the domain mask and division by total N; no monotonic-convergence claim.

Use new problems only when they repair or illuminate an identified objective. Prefer replacing or consolidating existing prompts:

| Candidate | Placement and decision | Checked outcome |
|---|---|---|
|Same plane, two defining functions|Use as a concrete part or replacement of the affected 9.1 gradient-normal checkpoint.|F=z and G=z^2 have the same zero set; gradients on it are (0,0,1) and (0,0,0). Failure of the gradient test for G does not make the plane singular.|
|One disk, two coverings|Reuse the current repeated-coverage examples/tasks in the integration chapters. Add a new prompt only if the intended early location lacks one.|The r-weighted integrals on angle intervals [0,2pi] and [0,4pi] are pi and 2pi. Repeated interior coverage differs from a seam.|
|Reversal of scalar versus work integrals|Consolidate an existing checkpoint after both operations are defined, rather than duplicate the existing explanations.|For r(t)=(t,0), scalar arc length is 1 both ways; work of (1,0) is 1 forward and -1 backward, because speed is unsigned and velocity directed.|

Do not automatically add every proposed extension or diagnostic problem. The new core workload should remain focused on the two coordinate derivations, the simple parameter-integral comparison, the gradient diagnostic and the local averaging mechanism. More advanced proofs remain optional.

## 7. Implementation acceptance checks, when implementation is authorized

### Learning and proof checks

For every affected core task, record the available definitions, theorem statements and operations, plus a short viable solution route. Give detailed derivations for new or high-risk exercises. Do not reclassify an honestly supplied theorem as an unexplained operation merely because its full proof is omitted.

Apply a **skip test**: hide every optional proof/enrichment passage and its solutions. All core examples and required tasks must remain understandable and solvable from the remaining material and supplied results. Check the Chapter 11 integral route, potential applications, maximum-principle uses and reviews explicitly. Optional tasks may depend on named optional prerequisites, with clear navigation.

For every proof labeled complete, check its actual premises and cycles. For each new proof exercise, solve all parts and verify the exact scope without using the result being justified. Check geometry, signs, endpoints, zero cases and hypotheses separately. An illustration is not promoted to a general proof by a correct numerical answer.

### Source and build checks

Recheck HEAD and the named passages before editing. Preserve unrelated work, original LaTeX/archive sources and semantic IDs for retained content. Record an explicit relocation map for any moved proof; do not silently repurpose an ID. Inspect captions and visible figure labels as well as prose.

Read the current project configuration and verify executable versions before selecting build commands. Current `project.ptx` lists web/print targets and `requirements.txt` pins PreTeXt 2.53.0; those files were reread for this proposal. No new executable/build verification is claimed in this planning update.

Use the configured XML/XInclude/ID checks, relevant audit fixtures and web build. Regenerate and inspect only affected graphics. The earlier audit's 12-fixture result and 1,323-message strict-validation result are historical receipts, not new validation from the addendum or this plan revision.

Compare before/after diagnostics by stable identity: rule/message plus normalized source file and semantic object where available. Keep original line numbers for navigation, but account for line shifts and documented relocations. Report inherited, repaired and newly introduced diagnostics separately; a smaller total alone cannot establish no regressions. State unrun checks explicitly. Do not hand-edit generated output or claim a successful build proves mathematical or pedagogical correctness.

**Definition of an acceptable repaired section:** a first-year student can read the core narrative, understand the notation and assumptions, and complete its required problems without hidden advanced prerequisites. Intuition, supplied theorems, scoped justifications and optional fuller proofs are distinguished honestly. Correctness is not weakened to achieve this pacing.
