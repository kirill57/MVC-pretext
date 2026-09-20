# MVC-pretext: prerequisite audit and pedagogical rewrite instructions for Codex

## 1. Assignment and editorial decision

Revise the active PreTeXt textbook so that a reader following its actual reading order can understand each required explanation and complete each required exercise using previously taught material, explicitly declared course prerequisites, or a self-contained explanation supplied at the point of use.

The central correction is Section 4.5. Keep it a lesson about **describing surfaces with parameters**, not a premature lesson about differentiating surfaces, constructing normal fields, or integrating differential forms.

Preserve the book's eventual development toward differential forms and generalized Stokes. Do not turn this assignment into a wholesale removal of differential forms, a replacement textbook, or a global chapter reorder.

### Repository and inspected baseline

- Repository: `kirill57/MVC-pretext`.
- Inspected main-branch commit: `328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8`.
- Active book entry point: `source/main.ptx`.
- Actual Section 4.5 path: `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-parametric-surfaces.xml`.
- The user's `sectionsource` spelling is not the active directory name in this snapshot.
- Audit date: September 20, 2026.

This instruction file records repository-wide search reconnaissance and targeted close readings. It is **not** a claim that every paragraph, exercise, or figure in all twenty chapters has already been audited. Complete the coverage ledger described below before claiming a book-wide audit.

If your local checkout differs from the inspected commit, record its HEAD and compare the affected passages. Reconfirm findings against the actual checkout; do not overwrite newer corrections to reproduce this baseline.

### Operational boundaries

Work in the existing local checkout. Do not commit, push, open a pull request, merge, or otherwise modify the remote repository. Do not discard unrelated local changes. Report the final local diff for the author's review.

Read applicable repository instructions, including `CONVERSION-PLAN.md` and `CONVERSION-AGENT.md`. This assignment authorizes pedagogical revision of the active XML, rather than mechanically reproducing the original LaTeX. Nevertheless:

- Keep `multivariable_calculus/` and the original archive read-only.
- Do not hand-edit generated HTML, generated LaTeX, or rendered image assets.
- Edit source XML/PTX and source graphics; regenerate affected outputs through the established build system.
- Preserve section-level XML IDs and the existing chapter order.
- Preserve the current Chapter 5 sequence: curvature, torsion/Frenet frame, special coordinates, then review.
- Use small, independently reviewable patches and verify each logical patch before expanding its scope.

## 2. What counts as a prerequisite problem

Classify each candidate before changing it.

**A. Required dependency gap.** A proof, calculation, definition, or required exercise needs a concept or operation that has not been explained sufficiently. Correct it by moving the dependent material, supplying a short sufficient local explanation, or rewriting the task using available tools.

**B. Local sequencing defect.** The necessary material is in the same section but appears after a checkpoint that expects the reader to use it. Usually move or rewrite the checkpoint, not the entire section.

**C. Optional preview.** A brief forward-looking remark motivates later study without being needed for the current argument or assessment. Such previews may remain. Prefer ordinary language over an accumulation of unexplained symbols.

**D. Legitimate early introduction.** A later chapter develops a concept further, but an earlier section already teaches the special case needed there. Preserve this. A chapter title is not evidence of first introduction.

**E. Declared postponed proof.** A theorem is stated precisely and its proof explicitly deferred. This is an editorial choice, not automatically an error. Verify that the promised proof actually exists, provide an exact reference, and distinguish using a stated theorem from claiming to have proved it.

**F. Proof-dependency cycle or mathematical overstatement.** These are not merely notation problems. Repair the logical argument or its hypotheses.

Do not prohibit examples before formal definitions. A worked example may introduce an object concretely before naming it formally. The objection is to unexplained notation or a task that asks the reader to supply reasoning that the exposition has not made available.

## 3. Reader contract and first sufficient introductions

Assume algebra, trigonometry, and the declared single-variable calculus prerequisites. Do not silently assume prior multivariable calculus, differential geometry, exterior algebra, or advanced integration theorems.

Verify the frontmatter's actual prerequisite statement and align it with the following progression. Do not erase legitimate single-variable reasoning merely because Chapter 7 teaches partial derivatives.

| Material | Existing sufficient introduction or intended home |
|---|---|
| Coordinates, vectors, dot/cross products, determinants | Chapters 1–3, with the local definitions actually provided there |
| Parametrizations, parameter domains, images, coordinate grids | Chapter 4; no surface differentiation required |
| Differentiation of vector-valued curves | Section 5.2 |
| Partial derivatives | Section 7.1 |
| Directional derivatives and a first gradient definition | Section 7.2, not first in Chapter 9 |
| Total derivative and scalar differentials | Sections 7.3–7.4 |
| Surface partial-derivative shorthand as Jacobian columns | Section 7.5, after a short explicit bridge |
| Chain rule and coordinate-change derivatives | Chapter 8 |
| Multiple integrals and substitution | Chapters 10–12 |
| Scalar line integrals versus work integrals | Sections 13.2–13.3 |
| Elementary curl tests and closed 1-forms | Section 13.6, where these are defined locally |
| Plane exterior derivative as a special-case reformulation | Section 14.4, with a local definition before operational use |
| Systematic regular surface patches and tangent planes | Section 15.1 |
| Surface area | Section 15.2 |
| Surface orientation and flux | Section 15.3 |
| Flux 2-forms; systematic exterior algebra and pullbacks | Section 15.4 and Chapter 16 |
| General exterior derivative; generalized Stokes | Chapters 17–18 |

The elementary constant-coordinate-form lesson in Section 2.7 may remain. Its existence does not license unexplained vector wedges, pullback operations, or integration theory in every early chapter.

## 4. Baseline findings and prescribed actions

The source references at the end are pinned to the inspected commit. XML IDs are more stable than displayed exercise numbers.

### A01 — Section 4.5: surface calculus in a before-calculus chapter

**Classification:** required dependency gap relative to the chapter's stated purpose; high priority. Sources S01–S03.

The subsection `c4s5-subsec-tangent-directions` defines `r_u` by holding the other parameter fixed and differentiating. Thus it is inaccurate to say the symbols are completely undefined. The real problem is that the section immediately expects vector differentiation, tangent-vector interpretation, and regularity before their planned development.

Affected material includes:

- `checkpoint-4-5-two-tangents-and-cross-product`, which also uses “regular point” before the local regularity definition;
- `c4s5-ex-tangent-directions-cylinder`;
- `c4s5-fig-cylinder-tangent-directions`, including caption and Asymptote labels;
- `c4s5-def-regular-point`;
- `c4s5-ex-regularity-cone-tip`;
- `c4s5-subsec-orientation-preview` and its derivative-based calculations;
- `checkpoint-4-5-choosing-an-orientation`;
- `c4s5-def-orientation-informal`.

Rewrite Section 4.5 according to Section 5 below. Merge its calculus content into existing later treatments rather than appending duplicate explanations.

### A02 — Section 4.6: calculus remains in the review

**Classification:** required dependency gap; high priority. Source S04.

Exercise `c4s6-ex-d6` asks for `r_theta cross r_z` on a cylinder and asks whether it points inward or outward. A Section 4.5-only patch leaves this problem behind.

Move the original mathematical task to the appropriate Chapter 15 exercise context, preserving its existing ID on the moved exercise. Put a new, genuinely geometric exercise in the Chapter 4 review using a new ID. Suggested replacement: compare the points represented at angles 0 and 2pi, identify the repeated edge, and describe the two families of grid curves.

Retain the existing sphere-comparison visual project. It already asks suitable questions about domains, circles, meridians, repeated points, and collapsed parameter edges.

### A03 — Section 4.5: vectors and covectors are conflated

**Classification:** unsupported notation/type change; high priority. Sources S01 and S05.

Section 4.5 appeals to `a wedge b = -b wedge a` for vectors as though this were the same object introduced in Chapter 2. Section 2.7 actually defines coordinate 2-forms such as `(dx wedge dy)(a,b)` and their evaluation on vectors. Those are not the vector bivector `a wedge b`.

Remove the vector-wedge detour from Section 4.5. In the later surface-orientation lesson use the already taught cross-product identity when appropriate. Do not replace every wedge by a cross product: that would be wrong for differential forms.

### A04 — Section 4.5: line-integral sign claim is overbroad

**Classification:** mathematical overstatement; high priority. Sources S01 and S13.

The text says reversing a closed curve changes the sign of “a line integral.” Distinguish:

- work/1-form integral: reverses sign under reversal of traversal;
- scalar arc-length integral: unchanged under reversal of traversal;
- surface flux: reverses sign when the chosen normal is reversed;
- scalar surface integral: unchanged by normal orientation.

Remove the integral discussion from Section 4.5. Check Sections 13.2–13.3 and 15.2–15.3 for an explicit, correct comparison and consistent captions, examples, exercises, and summaries. Do not retain an inaccurate statement as a preview.

### A05 — Section 2.7: a checkpoint precedes the notation it asks about

**Classification:** local sequencing defect; medium priority. Source S05.

`checkpoint-2-7-alternating-forces-zero` asks about `dx wedge dx` before the coordinate measurements and wedge definition appear.

Preferred repair: at its current location ask only why an alternating real-valued bilinear map satisfies `B(v,v)=0`. Put the `dx wedge dx` version after `c2s7-def-wedge-product-dx-dy`, if it adds instructional value. Do not create two identical checkpoints.

Also review `checkpoint-2-7-why-alternating-for-integration`. A required early checkpoint should be solvable from signed-area algebra, not from a theory of oriented integration that has not been developed. Recast it in terms of reversing an ordered pair of vectors, or move the integration question later.

Keep the elementary algebra of constant forms. If later expansions require a rule not actually stated here, add only the short algebraic rule needed: for linear scalar measurements alpha and beta,

`(alpha wedge beta)(a,b) = alpha(a) beta(b) - alpha(b) beta(a)`.

Explain the object types and derive distributivity and the swap rule. Do not introduce bundles, general exterior powers, or a general theory of differential forms here.

### A06 — Section 3.4: differential/measure notation is doing work too early

**Classification:** pedagogical prerequisite burden; medium priority. Source S06.

`c3s4-subsec-change-of-variables` uses differentials, wedge substitution, and an ordinary area-element formula. This is more than the preceding finite-vector determinant geometry requires.

Preferred repair: keep an exact finite-parallelogram calculation and the distinction between signed scaling by `det A` and ordinary scaling by `abs(det A)`. Explain images of the finite edge vectors; no infinitesimal notation is necessary. Merge the differential/pullback derivation into Section 12.5, which already treats it.

Keep at most a brief verbal pointer to the later substitution theorem. Do not move the basic determinant geometry out of Chapter 3.

### A07 — Section 3.4: local proof-dependency cycle

**Classification:** proof-dependency issue; high priority, subject to verifying any earlier independent justification. Sources S06–S07.

The proof idea for `c3s4-thm-volume-scaling-space` invokes

`det[Aa, Ab, Ac] = det(A) det[a,b,c]`.

The later `c3s4-thm-determinant-product` uses geometric volume scaling to justify determinant multiplicativity. As presented locally, the two justifications lean on each other. Do not describe this as a false determinant theorem. The problem is the proof organization.

Find and cite any genuinely independent earlier argument. Otherwise supply one. A short available route in dimension three is:

1. Set `B(a,b,c) = det[Aa, Ab, Ac]`.
2. Verify from the explicit determinant formula that B is trilinear and alternating.
3. Expand the three vectors in the standard basis. Terms with repeated basis vectors vanish; the remaining six terms give
   `B(a,b,c) = B(e1,e2,e3) det[a,b,c]`.
4. Since `B(e1,e2,e3) = det A`, the scaling identity follows independently.
5. Apply the identity to the columns of the second matrix to obtain multiplicativity.
6. Interpret the result as volume scaling.

The planar argument is the two-input version. Check the theorem's dimensional scope: a proof only for dimensions two and three does not establish a statement for square matrices of arbitrary size. Either provide the general proof at a suitable level or explicitly delimit the current theorem and later generalization. Never silently weaken a statement needed by a later chapter without tracing those uses.

### A08 — Section 7.2: checkpoint placement, not a missing Chapter 9 prerequisite

**Classification:** local sequencing improvement; medium priority. Source S08.

`checkpoint-7-2-gradient-dot-product` precedes `c7s2-def-gradient` and the general gradient-formula theorem with its hypotheses. Move the required checkpoint after the definition and justified formula, or make its current version explicitly about the worked example only.

Preserve the existing independent proof of the directional-derivative formula using coordinate increments and the one-variable Mean Value Theorem. Replacing it with the multivariable chain rule would create a new dependency on Chapter 8.

Preserve the warning example showing that existence of partial derivatives at one point does not suffice for the gradient directional-derivative formula.

### A09 — Section 7.5: make the derivative bridge explicit after removing 4.5

**Classification:** consequential repair needed to avoid a new gap. Source S09.

`c7s5-parametrized-surface` already identifies the columns of a 3-by-2 Jacobian as `s_u` and `s_v` and writes a tangent-plane approximation. This is a legitimate place for surface derivative notation, because vector derivatives, partial derivatives, and the total derivative are now available.

Before the first operational use, explicitly connect the notations:

`r_u(u0,v0) = (x_u,y_u,z_u)(u0,v0) = (d/du) r(u,v0) evaluated at u=u0`.

Give the analogous equation for v. Explain that a small increment Delta u produces approximately `Delta u r_u`, not the vector `r_u` independently of the increment size. State the differentiability/continuous-partial assumptions needed for the local linear approximation.

Use a short backward reference to Section 4.5 for the parameter grid and to the appropriate derivative sections for the operation. Do not add the entire orientation/flux theory here. Keep the systematic surface-regularity discussion in Section 15.1.

### A10 — Sections 4.4 and 8.4: distinguish preview cleanup from actual dependency failures

**Classification:** scope/notation cleanup, not necessarily an invalid argument. Sources S10–S11.

Section 4.4 ends with gradient notation, flux, and 2-form language as a forward preview. Replace this cluster with one plain-language statement about later finding slopes and measuring surfaces. Retain its useful algebraic level-set and slicing examples.

Section 8.4 legitimately uses gradients: Section 7.2 already defines them. It also computes Jacobian stretching and writes area/volume forms. Do not relocate the valid chain-rule or Jacobian computations. Make the main explanation work through the derivative matrix and its determinant. A forms comparison may remain if the algebra used has actually been taught; ordinary integral-transformation rules belong with Chapters 10–12 and should not be silently assumed.

Preserve the correct spherical sign: in the coordinate order `(rho, theta, phi)`, with phi measured down from the positive z-axis, the signed Jacobian is `-rho^2 sin(phi)`. The ordinary volume scale is its absolute value. Reordering to `(rho, phi, theta)` reverses the sign. Do not change a correct sign to make it resemble an unsigned textbook formula.

### A11 — Section 12.5: introduce the pullback symbol before its first integral

**Classification:** local notation-order improvement. Source S12.

The first example writes an integral containing `T^*(dx wedge dy)` before the following subsection explains the pullback notation. Explain `T^*` at its first occurrence, or defer that displayed notation until after the explanation. The geometric example can still precede the general definition.

Do not move the whole section to Chapter 16: Section 12.5 gives its own concrete area-form pullback definition. Make equalities between source and target coordinate forms explicit as pullback/substitution statements, not literal equalities of covectors living in different domains.

### A12 — Section 13.6: proof deferral and hidden supporting lemmas

**Classification:** declared postponed proof plus a supporting-lemma audit, not a confirmed undefined-curl problem. Source S14.

Curl and closed 1-forms are explicitly defined in this section. Preserve those introductions.

`c13s6-thm-curl-test-simply-connected` is stated before its proof, with a paragraph pointing toward later Green and Stokes theorems. Verify the actual later proof, provide precise references, and record the dependency. Do not label an intuitive remark about shrinking loops as a complete proof in three dimensions.

The rectangle-potential proof differentiates an integral depending on a parameter. Locate an earlier adequate justification. If none exists, add a short supporting lemma with continuity hypotheses and a proof appropriate to the book, or a precise reference to a previously established result. Search absence alone does not certify that no justification exists.

Also correct wording suggesting simple connectivity is necessary for an individual curl-free field to have a potential. It is a sufficient domain hypothesis guaranteeing the conclusion for all such fields, not a necessary condition for each particular field.

### A13 — Section 14.4: special-case exterior derivative is legitimate

**Classification:** local exposition-order improvement; retain the mathematical bridge. Source S15.

The section locally defines

`d(P dx + Q dy) = (Q_x - P_y) dx wedge dy`.

It is therefore not automatically dependent on Chapter 17. Put a short explanation of `omega`, `d omega`, and the oriented-region integral before the opening compact theorem notation is expected to carry meaning. Keep the general formal definition later if desired.

Do not invoke an unproved general exterior-derivative product rule as the justification of the local formula. Present the coordinate expansion as verification of the locally defined plane operation, or establish the limited rule actually used.

## 5. Detailed replacement architecture for Section 4.5

### 5.1 Intended outcomes

A student should be able to evaluate a two-parameter formula, distinguish its parameter domain from its image, construct elementary parametrizations, identify coordinate curves, and detect repeated parameter values by direct substitution.

No required outcome here should involve differentiation, regularity, normal-vector formulas, area elements, line integrals, flux, or wedge manipulation.

### 5.2 Suggested subsections

1. **Two parameters locate a point on a surface.** Keep the cylinder with angle and height. Show several parameter pairs and their image points. Explain the distinction between two input numbers and three output coordinates.
2. **Parameter domain and image.** Keep the map notation and explicit domain restrictions. Compare a whole cylinder, a half-cylinder, and a shorter band using the same formula. Explain that changing the domain changes the image or the number of times it is covered.
3. **Graphs and planes as parametrized surfaces.** Keep `(u,v,f(u,v))` and `P + u a + v b`. For a plane, state that a and b are independent. Verify equations by substitution, not differentiation.
4. **Coordinate grids.** Hold one parameter fixed. Use circles and vertical lines on the cylinder, and latitude/meridian curves on the sphere. Distinguish a coordinate curve from its tangent vector.
5. **Repeated points, seams, and collapsed edges.** Keep the sphere's seam and pole examples. Repeated parameter values or a collapsed coordinate curve do not by themselves prove that the geometric surface is singular. The sphere is the key warning. Do not introduce the regularity test here.
6. **Choosing a useful parametrization and checking it.** Give a small set of exercises involving coverage, parameter restrictions, point evaluation, and coordinate curves. Finish with one verbal look-ahead to the derivative and surface-integration sections.

Retain good existing examples and figures. Do not pad the replacement merely to match the original word count.

### 5.3 Mathematical safeguards

Do not claim that every continuous two-parameter map has a genuinely two-dimensional surface as its image. A map can collapse to a curve or point. Explain that the current examples describe sheets and that later regularity conditions identify nondegenerate differentiable patches. Do not insert an advanced topological definition to solve an elementary exposition problem.

Similarly, do not claim that every level set is a smooth surface, or that a few isolated traces uniquely determine an arbitrary surface. Keep assertions tied to the stated examples and the quadric families being studied.

The statement that two parameters are needed should concern the ordinary surface-coordinate descriptions used in the chapter; it should not purport to rule out all possible continuous space-filling maps.

### 5.4 Replacement assessment examples

Use or adapt these without derivative notation:

- For `r(theta,z)=(2 cos theta,2 sin theta,z)`, find the point with `theta=pi/3`, `z=2`.
- Restrict the domain to describe the half-cylinder with `y >= 0` and height between 1 and 4. State a suitable angular interval explicitly.
- For `r(u,v)=(u,v,uv)`, describe the two families of coordinate curves using fixed values of u and v.
- Verify the sphere equation from its parametrization using `sin^2 + cos^2 = 1`.
- Explain which parameter edges represent the same meridian and which edges collapse to a pole.
- Give two different parameter domains using the same cylinder formula that produce the same image but different repetitions.

Provide correct hints/solutions where the book's existing exercise convention requires them. “Show why” questions must not hide a demand for an as-yet-untaught theorem.

## 6. Relocation and ID handling

| Current content | Destination and treatment |
|---|---|
| Parameter evaluation, domains, graphs, grids, sphere repetitions | Remain in 4.5 |
| First interpretation of surface partials as coordinate-curve derivatives | Short explicit bridge in 7.5 |
| Detailed cylinder tangent calculation, regularity, tangent planes, cone comparison | Merge into 15.1; avoid repeating material already there |
| Derivative-labelled cylinder normal figure | Move with its calculus explanation to 15.1 or 15.3; regenerate and inspect |
| Continuous normal choices and Möbius discussion | 15.3, after the orientation definition |
| Oriented surface forms and parameter-order wedge interpretation | 15.4/16 where the required meanings are available |
| Blanket line-integral sign statement | Remove; ensure the correct distinction in 13.2–13.3 |
| Chapter 4 review D6 cross-product exercise | Move to Chapter 15; replace in Chapter 4 with a new geometric task |
| Chapter 3 coordinate-change wedge derivation | Merge into 12.5 rather than duplicating it |

Preserve each old ID on the same substantive mathematical object when moving it. Update all inbound references. When merging duplicate content, record the old-to-new semantic mapping and preserve a useful substantive legacy anchor if the format supports it; do not create empty anchors or attach an old calculus ID to an unrelated elementary exercise just to silence the build.

Keep every section root ID stable. Preserve source-figure IDs when the same figure moves. New replacement material receives new unique IDs. Verify links into figures, definitions, examples, exercises, hints, solutions, and chapter reviews, not only links between sections.

## 7. Complete the book-wide audit before claiming coverage

### 7.1 Reconstruct actual reading order

Follow `xi:include` recursively from `source/main.ptx`, resolving paths relative to the containing file. Do not infer order from directory listing, filename sort, XML ID numbers, or conversion comments.

Inspect chapter introductions, all active sections, required reviews/projects, frontmatter prerequisite statements, and appendices that are used to justify prerequisites. A reference appendix is not automatically assigned background. Record the active status of any file not included in the book.

Create `PREREQUISITE_COVERAGE.md` with one row per active section. Use statuses such as `fully reviewed`, `partially reviewed`, and `not yet reviewed`, with the reviewed aspects listed. Do not use `clean` to mean merely that a keyword search returned nothing.

### 7.2 Build a concept and notation register

For each significant concept record:

- its precise meaning and object type;
- the first explanatory introduction;
- the first definition and, where relevant, the first justification;
- the first required calculation or assessment;
- later generalizations that are not prerequisites for the initial special case.

Distinguish a scalar derivative from a vector derivative, a vector wedge from a covector wedge, a differential from a measure element, a scalar line integral from a work integral, a local chart defect from a geometric singularity, and a Jacobian matrix from its determinant.

### 7.3 Use searches to generate candidates, not verdicts

Search active student-facing text and source graphics for derivative subscripts, partial signs, gradient/Hessian/Jacobian language, tangent and normal claims, regularity, area/volume elements, integral signs, work/circulation/flux, curl/divergence, wedge, pullback, exterior derivative, Stokes, exact/closed, inverse/implicit functions, and phrases such as “as we know” or “recall.”

Inspect surrounding definitions and the actual prerequisite path for every candidate. Distinguish labels in rendered graphics from harmless internal graphics variables and library calls. Private Asymptote implementation using `surface` or `normal` is not itself a student prerequisite; visible unexplained derivative labels are.

Inspect exercises, hints, solutions, review tables, figure captions, alt text, and chapter objectives. A topic moved out of the prose must not remain required by any of these.

### 7.4 Trace proofs as well as vocabulary

Record independent input lemmas. Detect local and multi-section cycles. Track postponed proofs to their actual endpoints. Particular additional checks include:

- hypotheses of differentiability before interpreting a Jacobian as a local approximation;
- product/chain rules before their use in proofs;
- higher partial derivatives and symmetry before Hessian arguments;
- conditions for exchanging limits, derivatives, and integrals;
- multivariable substitution before invoking it as a proof of its own Jacobian factor;
- topology assumptions in conservative-field and Stokes arguments;
- linear algebra beyond the stated dimension;
- general exterior-derivative rules before using them as explanations of the introductory special cases.

These are audit targets, not claims that each defect has been found.

### 7.5 Maintain an evidence-backed ledger

Create `PREREQUISITE_AUDIT.md` with columns:

`ID | section/order | source path and line range | XML ID | exact required skill | earlier sufficient support | classification | severity | proposed action | implemented action | verification | unresolved limitation`.

Carry A01–A13 forward, reconfirming each against local HEAD. Add newly discovered findings. Separate confirmed findings, editorial choices, candidates awaiting verification, and protected non-findings. An earlier local definition counts as support even if the book has a later chapter named after the same subject.

## 8. Implementation sequence

1. Record HEAD, dirty-tree state, active order, and baseline build status. Inspect existing instructions and identify source-of-truth paths.
2. Complete a focused dependency pass for Chapters 2–4 and their direct downstream uses in 7.5, 12.5, and Chapter 15. Prepare the relocation/ID map.
3. Strengthen the existing destination passages and the short 7.5 derivative bridge. Remove duplicated exposition when merging. Keep source/destination changes as one coherent local patch when necessary to avoid dangling references.
4. Rewrite 4.5, replace/move 4.6 D6, and repair the adjacent 4.4 preview and Chapter 4 objectives/conclusion as needed.
5. Correct the 2.7 and 7.2 checkpoint ordering, the Chapter 3 proof/notation issues, and the first-use notation in 12.5 and 14.4. Verify postponed-proof/supporting-lemma questions in 13.6 before claiming they are resolved.
6. Finish the full active-book audit and implement additional confirmed small repairs. For a genuinely large proposed curricular redesign outside this assignment, document the proposal and leave the global structure unchanged.
7. Run technical validation and perform a fresh student-path reread of the modified material. Produce the final local report and stop without committing or pushing.

Do not mechanically move everything that occurs before Chapter 16 into Chapter 16. That would damage the book's carefully staged special-case development.

## 9. Validation and acceptance criteria

### Pedagogical acceptance

- Every required Section 4.5/4.6 task is answerable using the available geometry, algebra, and trigonometry.
- No required surface derivative, derivative-defined regularity, flux calculation, line-integral rule, or wedge manipulation remains in Chapter 4.
- Captions and rendered labels satisfy the same condition.
- Section 7.5 remains understandable after removing the old 4.5 calculus explanation.
- Later surface lessons retain the useful mathematics and do not acquire duplicate cylinder explanations or competing definitions.
- Definitions and sufficient hypotheses precede required generic checkpoints; worked examples may still motivate definitions.
- Legitimate early special cases remain, and any postponed proof has an honest status and precise supporting reference.
- Each confirmed audit finding is resolved or explicitly reported as unresolved.

### Mathematical acceptance

Check the scalar/work integral sign distinction; vector/covector types; derivative scaling of small increments; independence and smoothness assumptions for tangent-plane claims; parameter seams versus genuine singularities; correct spherical Jacobian sign; and noncircular determinant proofs with correct dimensional scope.

Do not substitute “smooth surface” for “regular parametrization” without checking the implication being asserted. A singular parametrization of a sphere does not make the sphere singular.

### PreTeXt and rendering acceptance

Use the repository's configured build targets and installed version. The documented commands include:

```sh
xmllint --noout --xinclude source/main.ptx
pretext build web
pretext generate latex-image
pretext generate asy
pretext view web
```

Verify command availability and target names before running. `xmllint` here checks XML well-formedness and inclusion, not full PreTeXt schema validity. Run the project's schema-validation mechanism if available. Record missing tooling honestly rather than claiming validation succeeded.

Check unique XML IDs, resolved XIncludes, valid and semantically correct cross-references, statement wrappers, displayed math, and the required `figure -> image -> latex-image/asymptote` structure. Preserve macros and escape source graphics correctly. Use the project's existing supported XML vocabulary for optional remarks; do not invent an unsupported element or attribute.

Regenerate affected graphics and inspect every moved/changed figure at its new location. Verify labels, captions, direction arrows, scale/visibility, and interactive rendering. A successful build alone does not verify pedagogical placement or visual correctness.

Compare warnings and failures to the baseline. Report all new warnings/errors and any pre-existing failures affecting confidence. Inspect representative neighboring and destination pages, not only 4.5. Do not commit generated build products.

### Deliverables in the local checkout

1. Corrected XML/PTX/source-graphics files.
2. `PREREQUISITE_AUDIT.md` with evidence and dispositions.
3. `PREREQUISITE_COVERAGE.md` with actual complete/partial coverage.
4. `PREREQUISITE_RELOCATION_MAP.md` mapping moved blocks and IDs to destinations.
5. `PREREQUISITE_REWRITE_REPORT.md` with changed files, preserved special-case introductions, validation commands/results, unresolved items, and a diff summary.

The final agent response must distinguish completed edits from proposed follow-up edits, and source inspection from successful build/render inspection. State that no commit or push was made.

## 10. Pinned source references

Each reference points to the inspected repository snapshot. Section-specific XML IDs above identify the relevant blocks within these files.

- **S01. [Section 4.5](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-parametric-surfaces.xml)** — `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-parametric-surfaces.xml`.

- **S02. [Chapter 4 include order and title](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch04-curves-coordinates-surfaces/ch04-curves-coordinates-surfaces.ptx)** — `source/chapters/ch04-curves-coordinates-surfaces/ch04-curves-coordinates-surfaces.ptx`.

- **S03. [Book include order](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/main.ptx)** — `source/main.ptx`.

- **S04. [Section 4.6, including exercise c4s6-ex-d6](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-chapter-review-and-visual-projects.xml)** — `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-chapter-review-and-visual-projects.xml`.

- **S05. [Section 2.7](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch02-vector-products/sections/sec-2-alternating-products-a-first-glimpse-of-forms.xml)** — `source/chapters/ch02-vector-products/sections/sec-2-alternating-products-a-first-glimpse-of-forms.xml`.

- **S06. [Section 3.4](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch03-linear-functions-matrices/sections/sec-3-determinants-of-linear-transformations.xml)** — `source/chapters/ch03-linear-functions-matrices/sections/sec-3-determinants-of-linear-transformations.xml`.

- **S07. [Section 2.6 determinant geometry](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch02-vector-products/sections/sec-2-determinants-and-signed-volume.xml)** — `source/chapters/ch02-vector-products/sections/sec-2-determinants-and-signed-volume.xml`.

- **S08. [Section 7.2 gradient definition and independent proof](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-directional-derivatives.xml)** — `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-directional-derivatives.xml`.

- **S09. [Section 7.5 surface Jacobian](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-the-jacobian-matrix.xml)** — `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-the-jacobian-matrix.xml`.

- **S10. [Section 4.4 ending previews](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-quadric-surfaces-and-level-surfaces.xml)** — `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-quadric-surfaces-and-level-surfaces.xml`.

- **S11. [Section 8.4 coordinate changes](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch08-chain-rule-coordinate-changes/sections/sec-8-coordinate-changes.xml)** — `source/chapters/ch08-chain-rule-coordinate-changes/sections/sec-8-coordinate-changes.xml`.

- **S12. [Section 12.5 pullback notation](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml)** — `source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml`.

- **S13. [Chapter 13 include order](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch13-vector-fields-line-integrals/ch13-vector-fields-line-integrals.ptx)** — `source/chapters/ch13-vector-fields-line-integrals/ch13-vector-fields-line-integrals.ptx`.

- **S14. [Section 13.6 curl definitions and postponed proof](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml)** — `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml`.

- **S15. [Section 14.4 plane exterior derivative](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-in-differential-form-language.xml)** — `source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-in-differential-form-language.xml`.

- **S16. [Section 15.1 existing destination](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml)** — `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml`.

- **S17. [Chapter 15 include order](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/source/chapters/ch15-surfaces-flux-curl-divergence/ch15-surfaces-flux-curl-divergence.ptx)** — `source/chapters/ch15-surfaces-flux-curl-divergence/ch15-surfaces-flux-curl-divergence.ptx`.

- **S18. [Conversion agent technical conventions](https://github.com/kirill57/MVC-pretext/blob/328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8/CONVERSION-AGENT.md)** — `CONVERSION-AGENT.md`.
