# Proposed repair plan

Pinned source: `9a9d110af839b539fe598de66ecc4320a4126af4`. This is an implementable proposal, **not implementation authorization**. Preserve stable XML IDs for retained mathematical objects and the existing Section5.2 author-directed lesson. The exact source paths, line ranges and hashes for every finding are in [findings-index.json](findings-index.json).

## 1. Supply the shared analysis facts before their first use — LO-01

**Place:** `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml`, immediately before `thm-c13s5-path-independence-potential`.

**Recommended editorial choice:** a short, explicitly supplied compactness toolbox at this course level, followed by actual application explanations. This does not add a real-analysis course to the entry contract. If the author instead wants every ingredient proved in-book, provide elementary nested-interval/box proofs and keep exact earlier links; that is a larger optional structural choice, not required for the minimal repair.

Model passage:

> We use the following standard facts about closed, bounded subsets of Euclidean space. Every cover by open sets has a finite subcover. Every sequence in such a set has a subsequence converging to a point of the set. A continuous function on such a set is uniformly continuous: for a prescribed output tolerance, one input tolerance works at every point. These facts are supplied here without proof. They provide uniform control; the extreme-value theorem alone is not their proof.

Follow this with the exact path/grid consequence rather than expecting the reader to invent it:

> Let H be continuous on a closed interval or rectangle, with values in an open set D. There is a sufficiently fine subdivision such that the image of every subinterval or rectangular cell lies in one open ball contained in D.

Explain the consequence using local target balls and a uniform scale on the compact parameter domain. A finite subcover alone is not literally the subdivision theorem: include the shrinking-neighborhood/Lebesgue-number argument or state this consequence as supplied too. Label all dimensions and hypotheses.

**Update uses:**13.5's polygonal path construction; `c13s6-lem-parameter-integral`;17.5 `c17s5-thm-simply-connected-potential`;19.2 `c19s2-deriving-the-local-balance-law`. The last needs a clearly stated fixed-compact-region version of differentiation under the integral (or a box/Fubini argument), not only the interval lemma. For continuous q and q_x on a neighborhood of a compact product, explicitly bound the integrated difference-quotient error by region measure times the uniform error.

**Retain:** the correct MVT estimate in13.6, local radial potential, continuous homotopy and straight polygon-grid cancellation in17.5, and fixed-region assumptions in19.2. Do not replace the homotopy by an unjustified smooth spanning surface.

**Downstream:** review14.5's moving-boundary derivative,19.4 local potentials/time derivatives and19.5 circle means; give links where the same toolbox is invoked. Add optional support links to the openly limited5.3/10.2 sketches without relabeling them full proofs. Update the old A12/L06/L16 dispositions only in a clearly dated implementation addendum after the repair is actually validated.

**Acceptance:** no claimed proof uses compactness merely as a word for closed-and-bounded while silently importing finite-cover, subsequence or uniform-control results. The repair introduces no dependence on Green, Stokes, or the potential theorem it is supporting.

## 2. Correct the exterior-derivative domain display — LO-04

**File/ID:** `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-rule-d-squared-equals-zero.xml`, `c17s4-ex-c2-hypothesis`.

Retain the example and all correct unequal mixed-partial computations. Replace the display asserting `d(dg)=2 dx wedge dy` at the origin with the scalar coefficient calculation `g_yx(0,0)-g_xy(0,0)=2`.

Model explanation:

> These existing second partials give a coefficient difference of2. But dg does not have C1 coefficients near the origin, so the exterior derivative of dg is not defined there under our definition. This calculation shows why we cannot apply the C2 cancellation theorem; it is not an example of d-squared failing within its stated domain.

Check17.5's exact/closed warning and all review/appendix paraphrases. Preserve the correct C2 proofs and the elementary mixed-partial examples in9.3/13.6/15.7. No distribution theory is needed.

## 3. Finish the Chapter11 integration bridge — LO-03, then LO-02

**Files:** `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml` and `sec-11-spherical-coordinates-in-integrals.xml`.

**Recommended integration repair:** retain the tiny-box geometry as motivation, then give a short derivation from existing slicing/Fubini and polar substitution. State the suitable bounded piecewise smooth regions, continuous integrands and once-coverage conditions explicitly. Preserve existing seam/axis/pole warnings.

For cylindrical coordinates, first integrate in z and apply `c10s5-thm-double-integrals-polar` to the planar shadow. This proves the factor r without invoking the later general3D substitution theorem.

For spherical coordinates, start with the established cylindrical integral, fix theta and apply planar polar substitution in the `(r,z)` half-plane: `r=rho sin(phi)`, `z=rho cos(phi)`. The unsigned planar factor is rho; multiplied by the cylindrical r this is `rho² sin(phi)`. If changing the usual planar angle to phi, explain `psi=pi/2-phi` and the reversed limits. The determinant for `(r,z)` in `(rho,phi)` is `-rho`, whereas the ordered Cartesian spherical triple `(rho,phi,theta)` has determinant `+rho² sin(phi)`. Keep scalar and oriented conventions separate.

**Smallest alternative:** explicitly label the exact cylindrical/spherical formulas as supplied special-case theorems with those hypotheses, and call the tiny-box paragraphs motivation. A complete general limiting proof is not required. Ordinary Chapter11 calculations are already supported by the displayed formulas; do not claim they lack any usable rule.

**Wedge repair:** move the arbitrary triple-wedge comparison paragraphs in `c11s3-subsec-volume-element` and `c11s4-subsec-volume-element` to `c12s5-subsec-pulling-back-volume-elements`, after its three-covector determinant definition and grouping convention. Retain the Chapter11 scalar factors. If the author prefers to keep those comparisons, insert the actual determinant definition/grouping rule before the first triple product; a vague link to2.7 is insufficient.

Check11.7 review explanations and its coordinate-box project,12.5 examples, captions/graphic labels if moved, and any IDs/xrefs associated with the paragraphs. Retain the2.7 early two-covector wedge and coordinate volume form.

## 4. Supply the local topology sentence needed by the maximum principle — LO-05

**File/ID:** `source/chapters/ch19-conservation-laws/sections/sec-19-potential-theory-and-harmonic-functions.xml`, before the proof of `c19s5-thm-no-interior-maximum`.

Model passage:

> A subset A of a region R is relatively open if every point of A has a small neighborhood whose intersection with R stays in A. It is relatively closed if R\A is relatively open. We use the connectedness criterion that a connected region has no nonempty proper subset both relatively open and relatively closed.

Then identify the maximum set, show local constancy using the circle mean, and use continuity for relative closedness. The criterion can be explicitly supplied; avoid passing off the earlier “one piece” picture as a proof. Retain the proof-sketch label and actual planar C2 scope. Check the maximum-principle checkpoint and harmonic project. LO-01 separately supports differentiation of circle means.

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
3. Run the inventory/ID/xref check, the12 triage fixtures, and the configured PreTeXt2.53.0 web build. Compare strict schema validation with this audit's1323-message baseline; do not claim a full pass while the backlog remains.
4. Regenerate only changed graphics through PreTeXt and inspect them in the browser; never hand-edit generated HTML/assets. Inspect moved content, theorem links, captions and visible labels.
5. Report actual source changes and post-repair results separately from this audit. Do not mark these proposed fixes implemented merely because the audit/build scripts pass.
