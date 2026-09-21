# Foundations findings, independent second pass

Snapshot: `9a9d110af839b539fe598de66ecc4320a4126af4`. Scope: frontmatter, document information, chapter wrappers, and all 56 sections of Chapters 1–8 in recursive XInclude order. Mathematical judgments were formed from the active source before consulting the corresponding old dispositions. No textbook changes are proposed as already authorized implementation.

## FND-01 — The continuity review drops the accumulation-point condition

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

## FND-02 — A basis-image checkpoint literally removes the necessary linearity assumption

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

## FND-03 — The triangle-equality checkpoint forgets the already supplied zero-vector exception

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

## Cross-scope capability conclusions, not duplicate findings

1. **U03/U04:** Chapters 1–8 do not supply a finite-subcover principle, a bounded-sequence subsequence theorem, or uniform continuity from compactness. Section 6.4 supplies closed/bounded definitions and an explicitly unproved extreme-value theorem. Section 5.3's arc-length proof is openly a proof idea and uses uniformity without constructing a general compactness tool. The root auditor reports a later compact=closed-and-bounded gloss in 9.5; that word-level support must not be confused with finite-cover or subsequence capabilities.
2. **U05:** “connected” in the hyperboloid pictures is descriptive. The torsion theorem's continuous choice between ±b on an interval reduces to ordinary one-variable continuity/IVT. Neither passage teaches relative openness/closedness or the connected-space clopen criterion. The later maximum-principle proof must obtain those capabilities elsewhere or receive a scoped repair.
3. **U07:** the 3.6 Hessian passage is explicitly a preview with no required Hessian task. Undefined second-partial subscripts can be signposted more clearly, but this remains C/P3, not a blocking gap.
4. **U01:** 2.7 supplies arbitrary **two-covector** wedge evaluation and distribution; it separately defines the fixed **coordinate three-form** by a determinant. It does not yet supply arbitrary three-covector expansion or graded wedge algebra. Preserve this distinction in the root graph.

All referenced finding and support locations are tied to file SHA-256 values and the immutable snapshot in the JSON artifacts.
