# Prerequisite rewrite report

The requested local rewrite and full active-book prerequisite audit are complete. Section4.5 now teaches parametrizations through domains/images, point evaluation, graphs, coordinate grids, seams, repetition and collapsed parameter edges. Required surface calculus is taught later with its dependencies in place. Chapter and section order are preserved.

## Scope and delivered files

- Checkout: `D:/work/sabbatical/2025/Books/MVC-pretext`.
- Baseline/current HEAD: `328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8` (unchanged).
- Initially clean tracked tree; pre-existing untracked `Claude outputs/` and the supplied instruction plan preserved.
- `PREREQUISITE_AUDIT.md`: A01–A13 dispositions, additional findings, protected non-findings, proof ceilings and concept/notation register.
- `PREREQUISITE_COVERAGE.md`:194/194 active sections fully source-reviewed, including49 appendix sections; wrapper/front/backmatter and inactive-template status.
- `PREREQUISITE_RELOCATION_MAP.md`: semantic moves, merged passages, preserved IDs and three retired unreferenced wrappers/table.
- `tools/check_prerequisites.py`: repeatable recursive include/order, ID, cross-reference and graphics-nesting checks; it explicitly does not replace schema validation or pedagogical review.

No commit, push, PR, merge or remote repository mutation was made. Original `multivariable_calculus/` sources and the original archive were not edited. Generated HTML and images were regenerated through PreTeXt; none were hand-edited or added to version control.

## Main corrections

The cylinder derivative example/figure, regularity, cone example and associated tasks now live in15.1. Continuous normal choices and the old4.6 D6 exercise live in15.3. Existing destination passages were merged rather than duplicated. A short7.5 bridge explicitly defines vector partials as coordinate-curve derivatives and scales small increments correctly. The new4.5/4.6 tasks require only previously available geometry, algebra and trigonometry. Independent rereading checked their answers and parameter-domain assumptions.

The audit also repaired checkpoint ordering; independent determinant proofs in3.4 with arbitrary-dimension scope; hidden supporting lemmas; assumptions behind derivative/integral interchange; substitution and parametrization multiplicity; scalar/work/flux signs; vector/covector types; and several incorrect calculations/figure labels in the main text and appendices.13.6 now points to a complete17.5 proof of the simply-connected potential theorem, independently reviewed using local potentials and a continuous homotopy grid.15.1 distinguishes a sphere's coordinate defect from the cone's genuine lack of a tangent plane, and explains local graph coordinates through the inverse theorem.

Legitimate early special cases remain: constant coordinate forms2.7, the gradient7.2, concrete pullbacks8.3/8.7, local curl/closed1-forms13.6, and plane exterior differentiation13.8/14.4. General forms and generalized Stokes retain their later systematic development. Chapter5 keeps its original curvature, Frenet, special-coordinates and review order.

## Validation receipts

Commands below were run from the checkout. The project pins PreTeXt2.48.1 in `requirements.txt`; the globally installed2.37.1 was not substituted for the final build.

| Check | Result / evidence |
|---|---|
| `xmllint --noout --xinclude source/main.ptx` | PASS, exit0. XML parsing and includes only, not schema certification. |
| `python tools/check_prerequisites.py` | PASS:225 active files,194 sections,3498 unique IDs,280 xrefs,0 errors. Two inactive starter templates excluded. |
| Baseline/current section-root sequence comparison | PASS: all194 section root IDs and their recursive order identical. Exactly three retired non-section IDs are documented in the relocation map;25 new IDs. |
| `.cache/prerequisite-venv/Scripts/pretext.exe build web` | PASS, exit0: “Success! Built requested target(s) without errors.” Full build includes asset generation. Receipt `logs/prerequisite-final-build.log`. |
| `.cache/prerequisite-venv/Scripts/pretext.exe validate web` with local Jing | DOES NOT PASS:1066 schema messages +246 validation-plus messages =1312. Receipt `logs/prerequisite-schema-final.log`, detailed `logs/main-validation.txt`. |
| Same schema/validation-plus tools on unmodified HEAD extracted to `.cache/schema-baseline` |1080 schema +247 validation-plus =1327 messages; `logs/prerequisite-schema-baseline.log`. These are pre-existing structural/accessibility warning families, not a successful baseline schema validation. |
| `git -c core.whitespace=cr-at-eol diff --check` | PASS with existing CRLF source endings preserved; no source content changed after the final mathematical review. |
| Independent source cross-checks | Determinant proof, elementary4.5/4.6 student path,7.5 bridge,15.1 tangent/cone reasoning,15.5 C2 coordinate Stokes argument,17.5 potential theorem. |
| Targeted numeric checks | Late reviewer checked repaired appendix examples/algorithms; this is not exhaustive execution of all optional code projects. |

Full schema validation exposes the book's existing mixture of ordinary section paragraphs with subdivisions and missing image descriptions, among other longstanding vocabulary/structure issues. Newly rewritten4.5 and15.3 introductions were wrapped properly; newly introduced literal-dash and xref warnings were removed. The schema message total decreased by15. A relocated/shifted missing-description message may point to unchanged17.4; no claim is made that every remaining warning was repaired. General schema normalization and accessibility completion remain outside this prerequisite rewrite.

The final build warns that schema validation did not pass, then completes successfully. Asset-generation runs also report the dependency's deprecated `fitz` API; the final build retains a Windows temporary-directory cleanup warning (`WinError5` on copied external/images). The cleanup problem was already present in the baseline: global2.37.1 completed conversion but exited1 during cleanup. Pinned2.48.1 records it as a warning and returns0. Generated output exists and was inspected. No destructive cleanup or permission changes were attempted. No new source-level XSL error or deprecation remains in the final build.

This validates the configured **web/HTML** target. The print/PDF target was not built or visually certified.

## Toolchain used

An isolated `.cache/prerequisite-venv` was created from the project's requirements. The dependency was pinned locally to `lxml==6.0.2`: the initially resolved6.1.3 produced Windows file-URI/entity errors during XSL processing. Reproduction starts with:

```powershell
python -m venv .cache/prerequisite-venv
.cache/prerequisite-venv/Scripts/python.exe -m pip install -r requirements.txt
.cache/prerequisite-venv/Scripts/python.exe -m pip install lxml==6.0.2
.cache/prerequisite-venv/Scripts/pretext.exe build web
```

The installed MiKTeX Asymptote2.88 failed in `plain_Label.asy`; PreTeXt's asset command misleadingly reported success while leaving the old cached cylinder. A task-local Ubuntu Asymptote2.87 bundle from official Ubuntu packages was extracted under `.cache/asy-bundle` and invoked through `logs/asy-wrapper.py` / `logs/asy-wrapper.sh`. The Python wrapper converts Windows paths before WSL handles arguments. Ignored local `executables.ptx` points to this wrapper and a task-local official Maven Jing jar (`.cache/jing.jar`). These local build aids remain available for reproduction. The original failure was not counted as a pass; the moved cylinder's regenerated HTML timestamp/size were verified before inspection.

## Graphics and rendered-page inspection

All eleven changed static figures were regenerated with `pretext generate latex-image -x ID --force`, exported from generated SVG to PNG using Inkscape for visual inspection, and checked for mathematical labels, direction arrows, scaling and clipping. Two label-overlap issues found during QA were corrected in source and regenerated. These are the checked IDs:

- `c3s7-fig-input-square-output-parallelogram`
- `c7s5-fig-rubber-sheet`
- `fig-c9s7-decision-path`
- `c10s4-fig-type-i-region`
- `c11s5-fig-inertia-distance`
- `c14s5-fig-staircase-interior-cancel`
- `c17s1-fig-differential-level-curves`
- `c20s1-fig-ellipsoid-traces`
- `c20s1-fig-gradient-contours`
- `c20s2-fig-gradient-descent`
- `c20s3-fig-tray-axis`

The moved `c4s5-fig-cylinder-tangent-directions` was regenerated through `pretext generate asymptote -x c4s5-fig-cylinder-tangent-directions --force`. It was inspected in its new15.1 page; dragging visibly rotates the model. The caption explains that arrows show directions and are scaled for visibility. The unchanged elementary rectangle-to-cylinder picture remains in4.5. No hidden graphics implementation variable was treated as student-facing prerequisite notation.

Browser checks inspected the rewritten4.5 page, the7.5 bridge,12.5's first pullback explanation, and the15.1 destination/caption/math. Representative neighboring/review and orientation/form pages were also checked during integration. MathJax displays mathematics, local links target the intended IDs, and the narrow app viewport supplies horizontal scrolling for long displays. Source reading covers the entire book; rendered-page inspection is representative rather than all-page certification.

## Remaining editorial limits

No confirmed small prerequisite finding remains unimplemented. The author Preface is still a conversion placeholder. EVT, inverse/implicit-function theorems, general substitution and general Green/Stokes/divergence/generalized-Stokes results have explicit supplied-theorem or proof-sketch status where a complete advanced proof is not provided. These honest proof ceilings are listed in the audit, not presented as completed analytic/manifold proofs. The schema/accessibility backlog and untested print target remain as stated above.

## Final local diff

Tracked diff at completion: **156 files changed, 1928 insertions(+), 1291 deletions(-)**. Additionally, the four requested Markdown reports and `tools/check_prerequisites.py` are new untracked deliverables; the pre-existing plan/Claude outputs are excluded from this change summary.

Changed tracked files:

- `publication/publication.ptx`
- `source/appendices/appA-single-variable-review/sections/sec-appA-derivatives-and-linear-approximation.xml`
- `source/appendices/appA-single-variable-review/sections/sec-appA-infinite-series-and-taylor-polynomials.xml`
- `source/appendices/appA-single-variable-review/sections/sec-appA-parametric-and-polar-curves.xml`
- `source/appendices/appA-single-variable-review/sections/sec-appA-the-fundamental-theorem-of-calculus.xml`
- `source/appendices/appC-matrix-algebra/sections/sec-appC-determinants.xml`
- `source/appendices/appC-matrix-algebra/sections/sec-appC-one-page-formula-summary.xml`
- `source/appendices/appC-matrix-algebra/sections/sec-appC-quadratic-forms.xml`
- `source/appendices/appD-coordinate-systems/appD-coordinate-systems.ptx`
- `source/appendices/appD-coordinate-systems/sections/sec-appD-polar-coordinates.xml`
- `source/appendices/appE-differential-forms-quickref/appE-differential-forms-quickref.ptx`
- `source/appendices/appE-differential-forms-quickref/sections/sec-appE-0-forms-1-forms-2-forms-and.xml`
- `source/appendices/appE-differential-forms-quickref/sections/sec-appE-classical-vector-calculus-translated-into-forms.xml`
- `source/appendices/appE-differential-forms-quickref/sections/sec-appE-generalized-stokes-theorem-summary.xml`
- `source/appendices/appE-differential-forms-quickref/sections/sec-appE-wedge-product-rules.xml`
- `source/appendices/appF-proof-sketches/appF-proof-sketches.ptx`
- `source/appendices/appF-proof-sketches/sections/sec-appF-dependency-chart.xml`
- `source/appendices/appF-proof-sketches/sections/sec-appF-differentiability-and-continuous-partial-derivatives.xml`
- `source/appendices/appF-proof-sketches/sections/sec-appF-divergence-theorem.xml`
- `source/appendices/appF-proof-sketches/sections/sec-appF-fubini-s-theorem-and-change-of-variables.xml`
- `source/appendices/appF-proof-sketches/sections/sec-appF-generalized-stokes-theorem.xml`
- `source/appendices/appF-proof-sketches/sections/sec-appF-stokes-theorem.xml`
- `source/appendices/appG-computational-labs/sections/sec-appG-numerical-differentiation-and-the-jacobian.xml`
- `source/appendices/appG-computational-labs/sections/sec-appG-numerical-double-and-triple-integration.xml`
- `source/appendices/appG-computational-labs/sections/sec-appG-simulating-flows-and-conservation-laws.xml`
- `source/chapters/ch01-points-vectors-space/ch01-points-vectors-space.ptx`
- `source/chapters/ch01-points-vectors-space/sections/sec-1-linear-independence-and-bases.xml`
- `source/chapters/ch01-points-vectors-space/sections/sec-1-lines-planes-and-hyperplanes.xml`
- `source/chapters/ch01-points-vectors-space/sections/sec-1-norm-distance-and-spheres.xml`
- `source/chapters/ch01-points-vectors-space/sections/sec-1-vectors-in-the-plane-and-in-space.xml`
- `source/chapters/ch02-vector-products/ch02-vector-products.ptx`
- `source/chapters/ch02-vector-products/sections/sec-2-alternating-products-a-first-glimpse-of-forms.xml`
- `source/chapters/ch02-vector-products/sections/sec-2-chapter-review-and-discovery-problems.xml`
- `source/chapters/ch02-vector-products/sections/sec-2-determinants-and-signed-volume.xml`
- `source/chapters/ch02-vector-products/sections/sec-2-discovery-project-quaternions-and-rotations.xml`
- `source/chapters/ch02-vector-products/sections/sec-2-the-dot-product.xml`
- `source/chapters/ch03-linear-functions-matrices/ch03-linear-functions-matrices.ptx`
- `source/chapters/ch03-linear-functions-matrices/sections/sec-3-determinants-of-linear-transformations.xml`
- `source/chapters/ch03-linear-functions-matrices/sections/sec-3-linear-approximation-as-a-preview-of-the.xml`
- `source/chapters/ch03-linear-functions-matrices/sections/sec-3-quadratic-forms-and-symmetric-matrices.xml`
- `source/chapters/ch04-curves-coordinates-surfaces/ch04-curves-coordinates-surfaces.ptx`
- `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-chapter-review-and-visual-projects.xml`
- `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-cylindrical-and-spherical-coordinates.xml`
- `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-parametric-curves.xml`
- `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-parametric-surfaces.xml`
- `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-polar-coordinates.xml`
- `source/chapters/ch04-curves-coordinates-surfaces/sections/sec-4-quadric-surfaces-and-level-surfaces.xml`
- `source/chapters/ch05-vector-valued-functions/ch05-vector-valued-functions.ptx`
- `source/chapters/ch05-vector-valued-functions/sections/sec-5-arc-length-and-speed.xml`
- `source/chapters/ch05-vector-valued-functions/sections/sec-5-chapter-review-and-applications.xml`
- `source/chapters/ch05-vector-valued-functions/sections/sec-5-curvature-and-normal-direction.xml`
- `source/chapters/ch05-vector-valued-functions/sections/sec-5-derivatives-and-integrals-of-vector-valued-functions.xml`
- `source/chapters/ch05-vector-valued-functions/sections/sec-5-motion-in-special-coordinate-systems.xml`
- `source/chapters/ch05-vector-valued-functions/sections/sec-5-torsion-and-frenet-frame.xml`
- `source/chapters/ch06-functions-limits-continuity/ch06-functions-limits-continuity.ptx`
- `source/chapters/ch06-functions-limits-continuity/sections/sec-6-continuity.xml`
- `source/chapters/ch06-functions-limits-continuity/sections/sec-6-functions-from-rn-to-rm.xml`
- `source/chapters/ch06-functions-limits-continuity/sections/sec-6-graphs-level-curves-and-level-surfaces.xml`
- `source/chapters/ch06-functions-limits-continuity/sections/sec-6-limits-in-several-variables.xml`
- `source/chapters/ch06-functions-limits-continuity/sections/sec-6-warning-examples.xml`
- `source/chapters/ch07-partial-derivatives-jacobian/ch07-partial-derivatives-jacobian.ptx`
- `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-chapter-review-and-applications.xml`
- `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-differentials.xml`
- `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-directional-derivatives.xml`
- `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-sufficient-conditions-and-warning-examples.xml`
- `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-the-jacobian-matrix.xml`
- `source/chapters/ch07-partial-derivatives-jacobian/sections/sec-7-the-total-derivative-as-the-best-linear.xml`
- `source/chapters/ch08-chain-rule-coordinate-changes/ch08-chain-rule-coordinate-changes.ptx`
- `source/chapters/ch08-chain-rule-coordinate-changes/sections/sec-8-chapter-review-and-discovery-problems.xml`
- `source/chapters/ch08-chain-rule-coordinate-changes/sections/sec-8-coordinate-changes.xml`
- `source/chapters/ch08-chain-rule-coordinate-changes/sections/sec-8-implicit-functions.xml`
- `source/chapters/ch08-chain-rule-coordinate-changes/sections/sec-8-inverse-functions.xml`
- `source/chapters/ch08-chain-rule-coordinate-changes/sections/sec-8-the-matrix-chain-rule.xml`
- `source/chapters/ch09-gradient-optimization/ch09-gradient-optimization.ptx`
- `source/chapters/ch09-gradient-optimization/sections/sec-9-chapter-review-and-applications.xml`
- `source/chapters/ch09-gradient-optimization/sections/sec-9-constrained-optimization-and-lagrange-multipliers.xml`
- `source/chapters/ch09-gradient-optimization/sections/sec-9-critical-points.xml`
- `source/chapters/ch09-gradient-optimization/sections/sec-9-second-derivatives-and-the-hessian-matrix.xml`
- `source/chapters/ch09-gradient-optimization/sections/sec-9-the-second-derivative-test.xml`
- `source/chapters/ch10-double-integrals/ch10-double-integrals.ptx`
- `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml`
- `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml`
- `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml`
- `source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml`
- `source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml`
- `source/chapters/ch11-triple-higher-integrals/ch11-triple-higher-integrals.ptx`
- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml`
- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml`
- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml`
- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml`
- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml`
- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml`
- `source/chapters/ch12-change-of-variables/ch12-change-of-variables.ptx`
- `source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml`
- `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml`
- `source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml`
- `source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml`
- `source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml`
- `source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml`
- `source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml`
- `source/chapters/ch13-vector-fields-line-integrals/ch13-vector-fields-line-integrals.ptx`
- `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-chapter-review-and-applications.xml`
- `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml`
- `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml`
- `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml`
- `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-vector-fields.xml`
- `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml`
- `source/chapters/ch14-greens-theorem/ch14-greens-theorem.ptx`
- `source/chapters/ch14-greens-theorem/sections/sec-14-chapter-review-and-applications.xml`
- `source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-circulation-form.xml`
- `source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-flux-form.xml`
- `source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-in-differential-form-language.xml`
- `source/chapters/ch14-greens-theorem/sections/sec-14-warning-examples.xml`
- `source/chapters/ch14-greens-theorem/sections/sec-14-why-green-s-theorem-is-true.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/ch15-surfaces-flux-curl-divergence.ptx`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-chapter-review-and-applications.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-classical-vector-calculus-identities.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-curl-and-stokes-theorem.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-divergence-and-the-divergence-theorem.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-flux-2-forms.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-oriented-surfaces-and-flux.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-surface-area-and-scalar-surface-integrals.xml`
- `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-warning-examples.xml`
- `source/chapters/ch16-differential-forms-wedge/ch16-differential-forms-wedge.ptx`
- `source/chapters/ch16-differential-forms-wedge/sections/sec-16-algebra-of-forms.xml`
- `source/chapters/ch16-differential-forms-wedge/sections/sec-16-integrating-forms.xml`
- `source/chapters/ch16-differential-forms-wedge/sections/sec-16-pullbacks.xml`
- `source/chapters/ch17-exterior-derivatives/ch17-exterior-derivatives.ptx`
- `source/chapters/ch17-exterior-derivatives/sections/sec-17-chapter-review-and-translation-table.xml`
- `source/chapters/ch17-exterior-derivatives/sections/sec-17-closed-and-exact-forms.xml`
- `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-exterior-derivative-of-a-0-form.xml`
- `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-exterior-derivative-of-a-2-form.xml`
- `source/chapters/ch17-exterior-derivatives/sections/sec-17-warning-examples.xml`
- `source/chapters/ch18-generalized-stokes/ch18-generalized-stokes.ptx`
- `source/chapters/ch18-generalized-stokes/sections/sec-18-chapter-review-and-capstone-problems.xml`
- `source/chapters/ch18-generalized-stokes/sections/sec-18-classical-stokes-theorem-as-generalized-stokes.xml`
- `source/chapters/ch18-generalized-stokes/sections/sec-18-green-s-theorem-as-stokes.xml`
- `source/chapters/ch18-generalized-stokes/sections/sec-18-proof-ideas.xml`
- `source/chapters/ch18-generalized-stokes/sections/sec-18-the-divergence-theorem-as-generalized-stokes.xml`
- `source/chapters/ch18-generalized-stokes/sections/sec-18-the-theorem.xml`
- `source/chapters/ch18-generalized-stokes/sections/sec-18-warning-examples.xml`
- `source/chapters/ch19-conservation-laws/ch19-conservation-laws.ptx`
- `source/chapters/ch19-conservation-laws/sections/sec-19-balance-laws-from-flux.xml`
- `source/chapters/ch19-conservation-laws/sections/sec-19-chapter-review-and-modeling-projects.xml`
- `source/chapters/ch19-conservation-laws/sections/sec-19-heat-wave-and-equilibrium-equations.xml`
- `source/chapters/ch19-conservation-laws/sections/sec-19-maxwell-s-equations-as-a-forms-gateway.xml`
- `source/chapters/ch19-conservation-laws/sections/sec-19-potential-theory-and-harmonic-functions.xml`
- `source/chapters/ch19-conservation-laws/sections/sec-19-the-continuity-equation.xml`
- `source/chapters/ch20-capstone-projects/sections/sec-20-differential-forms-projects.xml`
- `source/chapters/ch20-capstone-projects/sections/sec-20-geometry-and-visualization-projects.xml`
- `source/chapters/ch20-capstone-projects/sections/sec-20-integration-projects.xml`
- `source/chapters/ch20-capstone-projects/sections/sec-20-optimization-projects.xml`
- `source/chapters/ch20-capstone-projects/sections/sec-20-writing-projects.xml`
- `source/docinfo.ptx`
- `source/frontmatter.ptx`
