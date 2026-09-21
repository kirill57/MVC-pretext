# MVC-pretext: first-year undergraduate repair addendum

**Audience:** first-year undergraduate students taking multivariable calculus after single-variable calculus.

**Status:** revised editorial recommendation, not authorization to modify the repository. This addendum reviews the supplied “Revised repair plan: intuitive text and guided proof exercises.” It does not report a new repository audit or a successful build.

**Baseline named by the proposal:** `9a9d110af839b539fe598de66ecc4320a4126af4`. Recheck the actual checkout before a future authorized implementation. The accompanying `findings-index.json`, original audit proposal, test fixtures, and build logs were not supplied with the pasted plan and have not been independently verified in this review.

## 1. Controlling instructional objective

Repair use-before-explanation problems without turning the required course into a proof-based real-analysis or topology course. Preserve geometric intuition, interesting problems, careful statements, useful advanced connections, and short accessible arguments.

Do not assume prior training in compactness proofs, subsequences, open covers, homotopy, exterior algebra, or formal epsilon–delta proof construction. This does not prohibit teaching such ideas. It prohibits treating them as already mastered or introducing a large new theory merely to justify a routine calculus application.

Develop vectors and the necessary linear algebra where the book currently teaches them. Preserve the author's surface-grid lesson in Section 5.2; ordinary derivatives of frozen-parameter curves are available there. Do not reintroduce surface-partial notation into Section 4.5.

This is the MVC course. Do not import the entry requirements or full-proof obligations of the separate graduate AMO project.

### Distinguish four statuses

1. **Definition:** the meaning, inputs, outputs, and conventions of an object or operation. Supply before operational use, either directly or through a sufficient worked introduction.
2. **Available theorem:** a correct statement with usable hypotheses. It may be used whether its proof is immediate, guided, supplementary, or explicitly omitted.
3. **Guided justification:** an exercise that establishes the announced claim from earlier available results and explicitly supplied scaffolding. Provide a checked solution; name the exact scope proved.
4. **Optional connection or proof:** clearly marked enrichment. It cannot be the only source of a rule needed by a core exercise or proof.

An unproved, explicitly supplied theorem is not an unexplained operation. Conversely, calling a passage “intuitive” or “optional” does not excuse false statements or ill-typed formulas.

Do not write “proved below” when the later exercise proves only a special case. Prefer: “We will use the following theorem. The exercise explains the mechanism for [specified case]; the general theorem is stated without proof here.”

## 2. Revise LO-01: do not make a compactness course a prerequisite to potentials

### Required change to the proposal

Do not insert the four proposed compactness proof exercises as a required sequence immediately before `thm-c13s5-path-independence-potential`.

The nested-box subsequence construction, uniform-continuity contradiction, finite-cover/Lebesgue-scale argument, and homotopy-grid subdivision are a substantial proof project. Breaking them into parts does not make their cumulative prerequisite burden negligible.

Retain that material as a separately identified optional investigation or supplementary proof section, with definitions and checked solutions. It need not be deleted. Position and navigation should allow a student to continue the calculus narrative without completing it.

### Main-text replacement

Introduce only the precise fact the next argument uses. Explain its geometric meaning and explicitly supply it as a theorem when its proof is beyond the main route.

For example, a subdivision fact may be stated as follows:

> Let P be a closed bounded interval or rectangle, let D be an open subset of Euclidean space, and let H:P→D be continuous. There is a positive delta such that every nonempty closed cell Q contained in P with diameter smaller than delta has its image H(Q) contained in an open ball lying inside D. Here diameter means the largest distance between two points of the cell. A sufficiently fine subdivision therefore has this property.

Explain “open,” “continuous on P,” and “cell” if not already available. Label the optional proof reference accurately. Do not say finite subcover alone proves this statement.

In Section 13.5, do not introduce homotopy notation merely to establish a statement about paths. Keep any general homotopy treatment with its actual later application or optional proof.

For `c13s6-lem-parameter-integral`, state locally:

- q and its partial derivative in the parameter are continuous on a neighborhood of a closed rectangle;
- the integration interval is fixed;
- the derivative of the integral is the integral of that partial derivative at an interior parameter value.

A useful short explanation is that the difference-quotient error can be made small for every integration-variable value at once; its integral is then bounded by interval length times that error. Either supply the needed uniform-control fact explicitly or point to its optional proof. Do not pretend pointwise convergence alone justifies integration of a limit.

A core application exercise can use

`H(x) = integral from 0 to 1 of (x t^2 + x^2 t) dt`.

Ask students to differentiate after integration, then differentiate the integrand and integrate, compare the answers, and identify why the stated hypotheses hold. Both routes give `H'(x)=1/3+x`. Describe this as an illustration, not a proof of the general interchange theorem.

For Section 19.2, state the corresponding fixed-region result for the already taught class of bounded integration regions. Use “area” or “volume” rather than importing an undefined general measure. Continuous parameter derivatives on a neighborhood of the relevant closed product give an error bounded by the region's volume times a common pointwise error. Do not extend the formula to moving regions without the additional boundary term.

Preserve the valid radial-potential, continuous-homotopy, and polygonal-cancellation arguments in the fuller proof route. Do not replace them by an unjustified embedded spanning surface.

## 3. Chapter 11: keep the calculus derivations; separate their scope from the general theorem

Retain tiny-box motivation, exact integration formulas with stated hypotheses, illustrative calculations, and guided derivations.

### Cylindrical coordinates

For a specified vertically simple solid, write the triple integral as a planar integral of the vertical integral. Apply the already available planar polar substitution theorem to that planar integrand. Identify the factor r.

If continuity of an integral with variable limits is needed, explain or supply the necessary special fact. Do not secretly invoke the later general substitution theorem to justify this derivation.

### Spherical coordinates

Start with the established cylindrical integral. At a fixed azimuth, use planar polar substitution in the meridional (r,z)-half-plane:

`r = rho sin(phi), z = rho cos(phi)`.

The planar unsigned factor is rho; the existing cylindrical factor r becomes rho sin(phi). Their product is rho^2 sin(phi). Explain the angle conversion and reversal of one-variable bounds in the guided exercise.

Start with an explicit region for which all slices and bounds are given. An optional final part may check an explicitly displayed finite decomposition. Do not ask students to prove without support that every bounded piecewise-smooth region admits a finite suitable decomposition. That is not a consequence of merely saying “piecewise smooth.”

The supplied general rule and the exercise's proved special case must have distinct, accurate proof-status wording. Examples checking a ball's volume are tests of consistency, not proofs for all integrands and regions.

### Keep the forms connection, without making it a hidden prerequisite

The author prefers to keep advanced connections visible. Preserve a short, clearly identified “Oriented-volume connection” in Chapter 11. Give the local three-covector determinant definition before manipulating triple wedges, just as the proposal requests.

State that all three linear measurements act on the same vector space, explain evaluation on vectors, and interpret variable-coefficient forms pointwise. Grouped notation `(alpha wedge beta) wedge gamma` may be declared to mean this triple determinant here; do not claim that a general wedge algebra or associativity for all degrees has thereby been proved.

Keep the ordinary-volume derivation independent of this connection. A student following the core integral examples should not have to use wedge products. Unless the author explicitly makes the early forms strand assessed course content, classify the additional triple-wedge proof exercise as extension work. Retain the later systematic forms chapters; this addendum does not authorize their removal or wholesale redesign.

In the fuller connection, check these distinct statements:

- the signed (rho,phi) to (r,z) determinant is -rho;
- the signed (rho,phi,theta) to (x,y,z) determinant is +rho^2 sin(phi);
- ordinary volume uses an absolute determinant.

If deriving one sign from the other, account explicitly for the change from coordinate order (r,theta,z) to (r,z,theta). Do not silently equate an iterated integration order with an orientation convention.

## 4. LO-04: keep the correction; avoid an unnecessary regularity proof burden

Correct `c17s4-ex-c2-hypothesis` directly. Retain the scalar mixed-partial difference of 2, but do not present it as a value of the classical operator d(dg) within the book's C1-form definition.

Explain: g has a differential, but dg does not have continuously differentiable coefficients near the origin. Thus applying the already defined exterior derivative to dg is not permitted there. The example exposes a missing hypothesis, not failure of the identity within its stated domain.

The axis mixed-partial calculations can remain a guided challenge in the forms discussion. A complete estimate proving continuity of the first derivatives can be in the checked solution or optional final part. Supply the needed regularity fact visibly if the main explanation uses it; do not require a first-year reader to reconstruct a general regularity argument just to understand the warning.

Do not introduce distribution theory as a repair.

## 5. LO-05: teach the averaging mechanism before the topology

Keep the precise planar maximum-principle statement and a geometric explanation of the mean-value mechanism. Define harmonic and the required C2 regularity locally or by an earlier sufficient reference.

A suitable guided exercise asks students to show that a continuous temperature on a circle cannot have average M while being everywhere at most M and strictly below M somewhere. Guide the step from a strict deficit at one point to a deficit on an arc of positive length. Then apply the argument to every sufficiently small circle centered at a maximum point to obtain constancy on a disk.

Identify this as the local part of the maximum-principle proof. Do not claim that one circle alone establishes constancy on a disk, or that constancy on one disk alone establishes constancy on the whole region.

The global propagation step may be supplied, with its fuller proof in an optional subsection. The proposal's short definitions of relative openness, relative closedness, and connectedness can remain there. They are not reasons to build a required topology module.

Preserve a correct existing short proof when it is already adequately scaffolded. First-year level does not prohibit proofs; it requires careful selection and pacing.

## 6. Retain the mathematical corrections in LO-06–09 and LO-14

These are not negotiable consequences of the lower target level. Repair hypotheses in statements, surrounding prose, exercise prompts, hints, solutions, and reviews together.

- **9.1:** require a continuously differentiable defining function near the point and a nonzero gradient for the gradient-normal construction. Explain the content of C1 in words when necessary.
- **9.5:** retain a nonzero constraint gradient but allow a zero objective gradient. The conclusion is proportionality, including zero multiplier; avoid “parallel directions” language that assumes two nonzero arrows.
- **9.6:** distinguish a one-sided feasible variation from lack of a tangent. A segment endpoint can have a tangent line while the usual interior stationary-point test does not apply.
- **6.6:** qualify the punctured-limit continuity criterion at accumulation points. Explain that this means other domain points occur arbitrarily nearby. Keep isolated-point relative continuity valid; do not add an abstract topology lesson solely for this exception.
- **14.4:** inherit the full taught Green-theorem hypotheses, including field regularity on an open neighborhood of the region and its boundary, bounded-region scope, and the prescribed boundary conventions. Adding only “closed” is not a substitute for the field-neighborhood hypothesis.
- **18.10:** specify the permitted compact oriented spanning surface, induced boundary orientation, and that the field is defined with the needed regularity on a neighborhood of the surface. Any-surface independence is not valid across singularities or outside the theorem's scope. Recheck the numerical answer against the actual exercise; this addendum has not independently verified the reported 3pi.

For LO-10–13, retain short notation and navigation fixes. In particular, include the zero-vector case in triangle equality and state linearity in a question about determining a map from basis values. These are small edits, but correctness edits should not be classified as dispensable merely because they are small.

## 7. Add a few strong first-year problems instead of a large proof-repair workload

Use new problems only when they repair or illuminate an actual teaching objective. Prefer replacement or consolidation over adding every suggested problem.

### Same surface, different defining functions

After gradients are taught, compare F(x,y,z)=z and G(x,y,z)=z^2 at level zero. Ask students to identify both zero sets, calculate both gradients on the plane, and explain why failure of one gradient test does not make the plane singular.

Checked outcome: both zero sets are z=0; grad F=(0,0,1), while grad G=(0,0,0) there. A regular defining function is sufficient for the normal construction; a poor defining function can fail its hypotheses on a smooth surface.

### One disk, two coverings

After polar integration, compare the parameter rectangles 0<=r<=1 with 0<=theta<=2pi and 0<=theta<=4pi. Both map onto the unit disk. Ask why integrating r over the second rectangle gives twice its area, and distinguish double coverage of the interior from repetition only along the seam.

Checked outcome: the two integrals are pi and 2pi. The larger value counts the same interior twice; it does not mean the geometric disk changed size.

### Reversal does not always reverse an integral

After both scalar and work line integrals are defined, use the segment r(t)=(t,0), 0<=t<=1. Calculate the scalar integral of 1 with respect to arc length and the work integral of the constant field (1,0). Reverse traversal and compare.

Checked outcome: arc length remains 1; work changes from 1 to -1. Require an explanation based on speed versus directed velocity, not a slogan about “all line integrals.”

## 8. Future audit and implementation checks

### Learning audit

Record, for each core exercise, the available definitions, theorem statements, operations, and a viable solution route. Use short statements of why the prerequisites suffice; reserve detailed derivations for high-risk or genuinely new exercises.

Introduce a skip test: hide all optional proof/enrichment passages. Every core example and exercise must still be understandable and solvable from the remaining material and explicitly supplied results. Optional exercises may depend on named optional prerequisites, but must advertise them.

Do not call an acknowledged unproved theorem a use-before-definition defect. Do record unexplained hypotheses, undefined notation, a formula used outside its domain, a core task relying on optional machinery, and a false claim that an illustration proves a general result.

### Mathematical audit

For every text labeled a complete proof, check actual proof dependencies and cycles. A precisely supplied foundational theorem may terminate the required course proof chain. The more detailed supplementary proof route must also be honest about its inputs.

For new proof exercises, solve every part and verify its exact claim. Verify geometric examples, sign conventions, endpoints, zero cases, and assumptions independently. Do not use the theorem being justified inside its own proof exercise.

### Structural and build audit

Preserve semantic IDs for retained content and an explicit relocation map for moved content. Inspect captions and visible labels as well as prose. Preserve original sources and unrelated work.

Reproduce the project's configured commands rather than asserting a particular tool version from memory. The pasted plan reports 12 fixtures and a 1,323-message schema baseline; those are reported numbers, not validation performed in this review.

Compare diagnostics by stable identity (rule/message plus file and semantic object where possible), not by total count alone. One newly introduced error can be hidden by one disappearing old error. Report inherited errors, repaired errors, new errors, and unrun checks separately. A successful build does not establish mathematical or pedagogical correctness.

## 9. Definition of an acceptable repaired section

A student with the stated first-year background can read its core narrative, understand its symbols and assumptions, and complete its required problems without a hidden advanced prerequisite. The section gives a meaningful reason for its formulas, but distinguishes that reason from any proof it does not supply. More ambitious readers have an honest, navigable optional route to additional arguments. No correctness requirement is weakened to achieve this pacing.

**Review uncertainty:** approximately 5% for the mathematical distinctions discussed here and 15% for pedagogical placement without classroom testing. These are subjective estimates, not statistical confidence levels. No claim of current repository or implementation verification is made.
