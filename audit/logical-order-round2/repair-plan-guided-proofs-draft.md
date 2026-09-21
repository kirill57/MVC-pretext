# Revised repair plan: intuitive text and guided proof exercises

Pinned source: `9a9d110af839b539fe598de66ecc4320a4126af4`. This is an implementable proposal, **not implementation authorization**. Preserve stable XML IDs for retained mathematical objects and the existing Section5.2 author-directed lesson. The exact source paths, line ranges and hashes for every finding are in [findings-index.json](findings-index.json).

**Implementation status:** the textbook repairs have not been implemented. This revision records the author's preferred route: keep intuitively clear advanced material in the main text and develop its justification in exercises. The [original audit proposal](repair-plan-original-audit.md) is preserved for comparison. The source findings remain valid; the proposed teaching strategy has changed.

## Teaching pattern for the repairs

Keep the geometric explanation, useful advanced connection and precise mathematical statement in the main narrative. Introduce any notation or operation needed to read that statement locally. Follow it with a clearly labeled, multipart justification exercise, including enough intermediate claims and hints to make the proof accessible from the stated prerequisites.

Suggested main-text wording:

> The geometric picture suggests the following rule. Under the stated hypotheses, the rule is valid and may be used in subsequent examples. The guided exercise below develops its justification.

This supplies the theorem for use while honestly assigning its proof to an exercise. It does not describe a completed exercise as a proof already presented. Later arguments should refer to the stated result by ID; an optional challenge or hidden solution must not be the only place a required rule or hypothesis appears. Put indispensable scaffolding in the exercise statement or an announced hint, and provide a checked solution for each new proof exercise.

Retain short proofs that are already clear and complete. The purpose is to repair the identified gaps with accessible exercise routes, not to move every existing proof out of the exposition. Correct false or ill-typed statements directly; a proof exercise cannot repair a missing hypothesis in the statement itself.

## 1. Supply the shared analysis facts before their first use — LO-01

**Place:** `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml`, immediately before `thm-c13s5-path-independence-potential`.

**Preferred route:** retain the intuitive compactness/uniform-control explanation and state exactly the facts used. Add a short sequence of guided proof exercises immediately after it, before the first dependent proof. This does not add a real-analysis course to the entry contract: explain terms such as subsequence and uniform continuity locally, and supply the one-dimensional completeness fact needed by the exercise route.

Model passage:

> On a closed, bounded set, local control can be made uniform. For example, a continuous function admits one input tolerance that works throughout the set for a prescribed output tolerance. A bounded sequence has a convergent subsequence, and its limit remains in the set when the set is closed. An open cover has a finite subcover. We may use these facts below; the following guided exercises explain why they hold in the Euclidean settings we need.

Follow this with the exact path/grid consequence rather than expecting the reader to invent it:

> Let H be continuous on a closed interval or rectangle, with values in an open set D. There is a sufficiently fine subdivision such that the image of every subinterval or rectangular cell lies in one open ball contained in D.

State this subdivision consequence explicitly as well, with interval/rectangle and relative-continuity hypotheses. A finite subcover alone is not literally the subdivision theorem. The exercise sequence should establish the missing uniform scale rather than quietly substituting one claim for another.

**Guided exercise sequence, with proposed new IDs:**

1. `c13s5-ex-compact-subsequence`: explain that a subsequence selects terms with strictly increasing indices. Supply the real-line fact that nested nonempty closed bounded intervals whose lengths tend to zero have exactly one common point. Enclose a bounded sequence in a box; bisect it in every coordinate, choose a subbox containing infinitely many terms, and repeat. Ask the student to select increasing indices, prove convergence to the common point, and show that a closed set contains the limit. Include the last implication as a guided part using the open complement definition, not as an unexplained property of closed sets.
2. `c13s5-ex-uniform-continuity`: if uniform continuity failed on a closed bounded set K, choose `x_n,y_n` in K with distance below `1/n` but output separation at least a fixed positive epsilon. Use the previous exercise to extract a convergent subsequence of `x_n`; show that the corresponding `y_n` converge to the same point. Ask how continuity contradicts the fixed output separation. State the uniform-continuity quantifiers before asking students to negate them.
3. `c13s5-ex-finite-cover-control`: for an open cover of K, prove that some delta works so that each `K intersect B(x,delta)` lies in one member of the cover. If not, choose bad centers with radii `1/n`, extract a convergent subsequence, and use one open cover member around the limit to obtain a contradiction. Then cover a bounding box by finitely many small grid cells and deduce a finite subcover. Give the grid-cell diameter estimate in the prompt.
4. `c13s5-ex-path-grid-subdivision`: let H be continuous on a closed interval or rectangle with image in an open set D. If arbitrarily fine subdivisions had bad cells, choose a point from each bad cell and extract a convergent subsequence in the parameter domain. Choose a ball about the limiting image point lying inside D. Continuity and the shrinking cell diameters force every sufficiently late bad cell's image inside that ball, a contradiction. Ask students to specialize the result first to a path and then to a homotopy rectangle.

The nested-interval fact is explicitly supplied, not silently imported from an analysis course. Keep the exercises in dependency order and include complete checked solutions. Main-text references should cite the stated compactness/subdivision facts and identify these exercises as their justifications. Do not imply that the supplied EVT is a proof of these distinct facts.

**Update uses:**13.5's polygonal path construction; `c13s6-lem-parameter-integral`;17.5 `c17s5-thm-simply-connected-potential`;19.2 `c19s2-deriving-the-local-balance-law`. The last needs a clearly stated fixed-compact-region version of differentiation under the integral (or a box/Fubini argument), not only the interval lemma. For continuous q and q_x on a neighborhood of a compact product, explicitly bound the integrated difference-quotient error by region measure times the uniform error.

Add `c13s6-ex-parameter-integral-justification` after the lemma statement: use MVT to write the difference quotient, use the preceding uniform-continuity result to bound its error independently of the integration variable, and bound the integral error by interval length times that uniform error. At19.2, add a short extension exercise replacing interval length by the measure of the fixed bounded region. State integrability and the neighborhood assumptions explicitly. Retain enough of the current explanation to show why the uniform bound is the decisive step.

**Retain:** the correct MVT estimate in13.6, local radial potential, continuous homotopy and straight polygon-grid cancellation in17.5, and fixed-region assumptions in19.2. Do not replace the homotopy by an unjustified smooth spanning surface.

**Downstream:** review14.5's moving-boundary derivative,19.4 local potentials/time derivatives and19.5 circle means; give links where the same toolbox is invoked. Add optional support links to the openly limited5.3/10.2 sketches without relabeling them full proofs. Update the old A12/L06/L16 dispositions only in a clearly dated implementation addendum after the repair is actually validated.

**Acceptance:** no claimed proof uses compactness merely as a word for closed-and-bounded while silently importing finite-cover, subsequence or uniform-control results. The repair introduces no dependence on Green, Stokes, or the potential theorem it is supporting.

## 2. Correct the exterior-derivative domain display — LO-04

**File/ID:** `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-rule-d-squared-equals-zero.xml`, `c17s4-ex-c2-hypothesis`.

Retain the example and all correct unequal mixed-partial computations. Replace the display asserting `d(dg)=2 dx wedge dy` at the origin with the scalar coefficient calculation `g_yx(0,0)-g_xy(0,0)=2`.

Model explanation:

> These existing second partials give a coefficient difference of2. But dg does not have C1 coefficients near the origin, so the exterior derivative of dg is not defined there under our definition. This calculation shows why we cannot apply the C2 cancellation theorem; it is not an example of d-squared failing within its stated domain.

Check17.5's exact/closed warning and all review/appendix paraphrases. Preserve the correct C2 proofs and the elementary mixed-partial examples in9.3/13.6/15.7. No distribution theory is needed.

Keep the intuitive warning example in the main text. Add a short justification exercise asking students to compute the two axis mixed partials, verify continuity of the first derivatives at the origin, and identify the missing C1 regularity of dg. Supply a bound for the first derivatives in a hint. The main-text display must still be corrected directly; an exercise is not a substitute for using the operator within its defined domain.

## 3. Finish the Chapter11 integration bridge — LO-03, then LO-02

**Files:** `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml` and `sec-11-spherical-coordinates-in-integrals.xml`.

**Preferred integration repair:** retain the tiny-box geometry and exact formulas in the main narrative. State the suitable bounded piecewise smooth regions, continuous integrands and once-coverage conditions explicitly, and say that the formulas may be used. Place the derivations in two guided exercises using existing slicing/Fubini and polar substitution. Preserve existing seam/axis/pole warnings.

For `c11s3-ex-justify-cylindrical-integration`, give a z-simple region and ask students to express its integral by first integrating vertically. Treat the resulting inner integral as a function on the planar shadow and apply `c10s5-thm-double-integrals-polar`. Ask students to identify the factor r and explain why finite decomposition extends the argument to the stated region class. Give the needed continuity/slicing facts explicitly; do not ask for an unprovided general integrability theorem. This justifies the formula without invoking the later general3D substitution theorem.

For `c11s4-ex-justify-spherical-integration`, start with the established cylindrical integral, fix theta and apply planar polar substitution in the `(r,z)` half-plane: `r=rho sin(phi)`, `z=rho cos(phi)`. Guide students through the angle change `psi=pi/2-phi`, its reversed limits, the unsigned planar factor rho, and the existing cylindrical factor r. Their product is `rho² sin(phi)`. Use an explicit spherical box first, then state the extension to finite suitable pieces. An additional sign-check part should compare the `(r,z)` determinant `-rho` with the Cartesian spherical determinant `+rho² sin(phi)` in the ordered variables `(rho,phi,theta)`. Keep scalar and oriented conventions separate.

The supplied statements make the formulas available before students complete the exercises; the exercise labels identify where their justifications are developed. A complete general limiting proof is not required. Ordinary Chapter11 calculations are already supported by the displayed formulas; do not claim they lack any usable rule.

**Preferred wedge repair: keep the comparisons in Chapter11.** Before the first arbitrary triple product in `c11s3-subsec-volume-element`, introduce its geometric meaning as signed volume measured by three linear measurements and give the short determinant definition:

> For linear measurements alpha, beta and gamma, `(alpha wedge beta wedge gamma)(a,b,c)` is the determinant whose rows are their values on a, b and c. We use `(alpha wedge beta) wedge gamma` for the same alternating trilinear measurement.

Supply the multilinearity and alternating rules needed to read the ensuing calculation. Add `c11s3-ex-three-measurement-volume`, asking students to derive these rules from the determinant, recover the coordinate volume form, and verify the cylindrical wedge identity. An extra part can compare the sign after swapping the last two factors. Each part must evaluate forms on vectors rather than identify a form with an unsigned scalar volume.

Keep the spherical comparison too; refer back to this local rule and ask students to verify its determinant coefficient as a guided calculation. Section12.5 can recall this introduction and develop systematic pullback notation. It will no longer be described as the first arbitrary triple-wedge definition. Retain the earlier2.7 two-covector wedge and fixed coordinate volume form without expanding that chapter into general exterior algebra.

Check11.7 review explanations and its coordinate-box project,12.5 examples, all associated captions/graphic labels and IDs/xrefs. Keep the existing advanced connections and adjust the introduction records to match the new local definitions and proof exercises.

## 4. Supply the local topology sentence needed by the maximum principle — LO-05

**File/ID:** `source/chapters/ch19-conservation-laws/sections/sec-19-potential-theory-and-harmonic-functions.xml`, before the proof of `c19s5-thm-no-interior-maximum`.

Model passage:

> A subset A of a region R is relatively open if every point of A has a small neighborhood whose intersection with R stays in A. It is relatively closed if R\A is relatively open. Connected means that R cannot be split into two disjoint, nonempty relatively open pieces. Consequently, a subset that is both relatively open and relatively closed must be empty or all of R. The exercise below turns this statement into the propagation step in the maximum principle.

Retain the intuitive main-text explanation: a point attaining the global maximum forces equality on surrounding circles, and this equality spreads through the connected region. State the maximum principle with its actual hypotheses so it is available for later use.

Add `c19s5-ex-maximum-principle-justification` with four parts:

1. A continuous function on a circle is at most M and has average M. Show that a strict deficit at one point would persist on an arc and make the average smaller.
2. Apply that observation to every sufficiently small circle centered at a maximum point, and conclude that the maximum set contains a neighborhood of the point.
3. Use continuity to prove the maximum set is relatively closed in the domain. Ask students to identify explicitly why the complement is relatively open.
4. If the maximum set were nonempty and proper, it and its complement would give the forbidden split in the definition of connectedness. Conclude constancy throughout the domain.

Provide hints and a complete checked solution. Reference the exercise as the justification rather than labeling the short intuitive paragraph a complete proof. Retain planar C2 scope, and check the existing checkpoint and harmonic project. LO-01 separately supports differentiation of circle means. This gives a concrete exercise route without requiring a topology course.

## 5. Repair the local hypothesis and assessment mismatches — LO-06–09, LO-14

| Exact object | Minimal edit | Required check |
|---|---|---|
|9.1 `checkpoint-9-1-gradient-normal-tangent-plane` and adjoining normal/tangent-plane prose at239–253|State C1 near the point and nonzero gradient, matching `c9s1-thm-gradient-normal-level-surface`.|`F=z²` at z=0 is no longer admitted as a nonzero normal construction.|
|9.5 `checkpoint-9-5-gradients-parallel` and preceding135–166 prose|Keep the defining constraint gradient nonzero before invoking the normal line.|The squared-circle defining function remains the explicit excluded warning case; allow zero objective gradient.|
|9.6 `checkpoint-9-6-multiplier-misses-boundary` hint|Ask whether both signs of a parameter change remain feasible, rather than whether an endpoint has a tangent.|The segment endpoint can have a tangent while Fermat's interior derivative condition fails.|
|6.6 `c6s6-ex-cc-three-conditions`|Add “at an accumulation point of the domain.”|Keep isolated-point relative continuity valid.|
|14.4 `c14s4-thm-greens-for-1-forms`|Restore “bounded closed” and the disjoint boundary-curve condition from14.2, or explicitly inherit its full hypotheses.|Coefficients singular on the boundary of an open disk cannot meet the statement.|
|18.10 `c18s10-ex-pr-any-surface`|Require a compact smooth oriented spanning surface, with the unit circle counterclockwise as induced boundary.|The exterior infinite plane is excluded; Stokes gives the intended3pi.|

Use the source path for each exact ID from findings-index.json. Inspect the matching hint/solution/review wording, not just the theorem box. Preserve mathematically correct adjacent examples and the earlier precise theorem statements.

## 6. Optional clarity and navigation — LO-10–13

- 3.6 `c3s6-subsec-hessian-preview`: say the second-partial entries will be defined in Chapter9; for now H is a symmetric quadratic-bending matrix. Keep this a dispensable preview.
- 3.2 `checkpoint-3-2-basis-determines-all`: begin “Suppose T is linear” and replace “nothing else about T” with “no further values of T.” Retain its preceding nonlinear counterexample.
- 1.5 `checkpoint-1-5-triangle-equality`: include “or one vector is zero,” or explicitly restrict the vectors to be nonzero. Keep the correct earlier statement/later independent proof.
- 20.3 `c20s3-proj-monte-carlo`: add a direct descriptive xref to `appG-numint-monte-carlo-estimate` and a sentence about independent uniform coordinate draws in a rectangular box. Preserve the domain mask and division by total N; make no monotonic-convergence claim.

These are P3 improvements, not reasons to reorganize the book or add new entry prerequisites.

## Validation for a future authorized implementation

1. Recheck HEAD and compare the exact named passages before applying edits. Preserve unrelated work and semantic XML IDs.
2. Repeat the affected task witnesses and adversarial probes. Check the graph for new cycles, optional-to-required leaks, changed dimension/regularity and hidden hint dependencies.
   For each new justification exercise, solve every part using only the earlier statements or explicitly supplied scaffold. Verify that the exercise proves the intended result without assuming it, and that later text cites the stated result rather than an unannounced exercise answer. Check the main-text proof-status labels and all complete solutions together.
3. Run the inventory/ID/xref check, the12 triage fixtures, and the configured PreTeXt2.53.0 web build. Compare strict schema validation with this audit's1323-message baseline; do not claim a full pass while the backlog remains.
4. Regenerate only changed graphics through PreTeXt and inspect them in the browser; never hand-edit generated HTML/assets. Inspect moved content, theorem links, captions and visible labels.
5. Report actual source changes and post-repair results separately from this audit. Do not mark these proposed fixes implemented merely because the audit/build scripts pass.
