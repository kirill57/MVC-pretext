# Scope and coverage

Snapshot `9a9d110af839b539fe598de66ecc4320a4126af4`; branch `main`. Initial tracked working tree was clean; the controlling audit brief was the only untracked file. At completion, only that brief and this new audit directory are untracked. No source, old audit report, historical LaTeX/archive, remote, branch or commit was modified.

Actual entry: `source/main.ptx`, expanded in recursive XInclude order, retaining source hashes, original lines, IDs, ancestry and occurrence. The inventory recomputed225 active files:194 sections (145 chapter,49 appendix) plus31 wrappers/frontmatter/backmatter/docinfo files. There are3505 IDs,285 cross-reference records and no parse/include/ID/xref errors. The two inactive source templates are listed in coverage.json; the historical `multivariable_calculus/` tree is excluded.

Entry contract: algebra, trigonometry and single-variable calculus, including limits, continuity, derivative rules, MVT, definite integration, FTC and substitution. No real-analysis/topology/ODE/linear-algebra/exterior-algebra course is assumed. Appendices supply explicit reference routes, not silent earlier lessons. Macro declarations and nonrendered comments do not teach capabilities.

Primary semantic reading: **194/194 sections**, plus all31 nonsection files. Prerequisite-support review records **178 sections without an identified unresolved support limitation**; the remainder retain their specific findings/limitations below. This distinction is intentional:194 read does not mean194 logically verified.

Task coverage: all910 formal task elements have witnesses. All1122 mechanical candidates are either witnessed or explicitly classified; none is silently dropped. The1607 witness/disposition rows also include untagged deliverables and overlapping aliases, so they are not a count of distinct exercises. [Detailed task ledger](task-witnesses.json).

Every figure source/caption/description and visible label code was included in the primary read. Only the5.2 cone figure and adjacent definition/link received a fresh rendered spot-check. Other figures remain source-only; no graphics were regenerated in this audit. Independent challenge covered selected findings and significant protected judgments in every partition; it is not represented as a second full reading of every section. The per-section `independent_challenge_completed` flag remains false where that stronger claim was not earned; `partition_challenge_completed` records the actual narrower check.

The coverage ledger separates inventory, scan, semantic read, support verification, task witness, challenge, rendering and unresolved states. The dependency graphs carry their human-review scope. A successful fixture or build is not a semantic pass.

| Order | Section | Semantic read | Support without open limitation | Tasks | Graphics | Unresolved/support notes |
|---|---|---|---|---|---|---|
| 1 | `sec-1-why-multivariable-calculus-begins-with-geometry` | yes | yes | witnessed | source only |  |
| 2 | `sec-1-vectors-in-the-plane-and-in-space` | yes | yes | witnessed | source only |  |
| 3 | `sec-1-coordinates-and-dimension` | yes | yes | witnessed | source only |  |
| 4 | `sec-1-linear-independence-and-bases` | yes | yes | witnessed | source only |  |
| 5 | `sec-1-norm-distance-and-spheres` | yes | yes | witnessed | source only | FND-03: zero-vector exception omitted |
| 6 | `sec-1-lines-planes-and-hyperplanes` | yes | yes | witnessed | source only |  |
| 7 | `sec-1-chapter-review-and-discovery-problems` | yes | yes | witnessed | source only |  |
| 8 | `sec-2-complex-numbers-as-a-warm-up` | yes | yes | witnessed | source only |  |
| 9 | `sec-2-pure-imaginary-quaternions-and-three-dimensional-vectors` | yes | yes | witnessed | source only |  |
| 10 | `sec-2-the-scalar-and-vector-parts-of-a` | yes | yes | witnessed | source only |  |
| 11 | `sec-2-the-dot-product` | yes | yes | witnessed | source only |  |
| 12 | `sec-2-the-cross-product` | yes | yes | witnessed | source only |  |
| 13 | `sec-2-determinants-and-signed-volume` | yes | yes | witnessed | source only |  |
| 14 | `sec-2-alternating-products-a-first-glimpse-of-forms` | yes | yes | witnessed | source only |  |
| 15 | `sec-2-discovery-project-quaternions-and-rotations` | yes | yes | witnessed | source only |  |
| 16 | `sec-2-chapter-review-and-discovery-problems` | yes | yes | witnessed | source only |  |
| 17 | `sec-3-linear-functions-r-n-r` | yes | yes | witnessed | source only |  |
| 18 | `sec-3-linear-transformations-r-n-r-m` | yes | yes | witnessed | source only | FND-02: contextual linearity needed; wording refinement |
| 19 | `sec-3-matrix-multiplication-as-composition` | yes | yes | witnessed | source only |  |
| 20 | `sec-3-determinants-of-linear-transformations` | yes | yes | witnessed | source only |  |
| 21 | `sec-3-solving-linear-systems` | yes | yes | witnessed | source only |  |
| 22 | `sec-3-quadratic-forms-and-symmetric-matrices` | yes | yes | witnessed | source only |  |
| 23 | `sec-3-linear-approximation-as-a-preview-of-the` | yes | yes | witnessed | source only |  |
| 24 | `sec-4-parametric-curves` | yes | yes | witnessed | source only |  |
| 25 | `sec-4-polar-coordinates` | yes | yes | witnessed | source only |  |
| 26 | `sec-4-cylindrical-and-spherical-coordinates` | yes | yes | witnessed | source only |  |
| 27 | `sec-4-quadric-surfaces-and-level-surfaces` | yes | yes | witnessed | source only |  |
| 28 | `sec-4-parametric-surfaces` | yes | yes | witnessed | source only |  |
| 29 | `sec-4-chapter-review-and-visual-projects` | yes | yes | witnessed | source only |  |
| 30 | `sec-5-vector-valued-functions` | yes | yes | witnessed | source only |  |
| 31 | `sec-5-derivatives-and-integrals-of-vector-valued-functions` | yes | yes | witnessed | source + limited render | 5.2 tangent-sheet theorem explicitly deferred; later destination checked by root. |
| 32 | `sec-5-arc-length-and-speed` | yes | yes | witnessed | source only |  |
| 33 | `sec-5-curvature-and-normal-direction` | yes | yes | witnessed | source only |  |
| 34 | `sec-5-torsion-and-frenet-frame` | yes | yes | witnessed | source only |  |
| 35 | `sec-5-motion-in-special-coordinate-systems` | yes | yes | witnessed | source only |  |
| 36 | `sec-5-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 37 | `sec-6-functions-from-rn-to-rm` | yes | yes | witnessed | source only |  |
| 38 | `sec-6-graphs-level-curves-and-level-surfaces` | yes | yes | witnessed | source only |  |
| 39 | `sec-6-limits-in-several-variables` | yes | yes | witnessed | source only |  |
| 40 | `sec-6-continuity` | yes | yes | witnessed | source only | EVT supplied unproved, not a generalcompactness toolkit. |
| 41 | `sec-6-warning-examples` | yes | yes | witnessed | source only |  |
| 42 | `sec-6-chapter-review-and-discovery-problems` | yes | yes | witnessed | source only | FND-01: false without accumulation-point qualification |
| 43 | `sec-7-partial-derivatives` | yes | yes | witnessed | source only |  |
| 44 | `sec-7-directional-derivatives` | yes | yes | witnessed | source only |  |
| 45 | `sec-7-the-total-derivative-as-the-best-linear` | yes | yes | witnessed | source only |  |
| 46 | `sec-7-differentials` | yes | yes | witnessed | source only |  |
| 47 | `sec-7-the-jacobian-matrix` | yes | yes | witnessed | source only |  |
| 48 | `sec-7-sufficient-conditions-and-warning-examples` | yes | yes | witnessed | source only |  |
| 49 | `sec-7-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 50 | `sec-8-the-chain-rule-along-a-curve` | yes | yes | witnessed | source only |  |
| 51 | `sec-8-the-matrix-chain-rule` | yes | yes | witnessed | source only |  |
| 52 | `sec-8-differentials-and-the-chain-rule` | yes | yes | witnessed | source only |  |
| 53 | `sec-8-coordinate-changes` | yes | yes | witnessed | source only |  |
| 54 | `sec-8-inverse-functions` | yes | yes | witnessed | source only | Inverse existence/smoothness supplied unproved. |
| 55 | `sec-8-implicit-functions` | yes | yes | witnessed | source only |  |
| 56 | `sec-8-chapter-review-and-discovery-problems` | yes | yes | witnessed | source only |  |
| 57 | `sec-9-the-gradient-and-level-sets` | yes | no; see note | witnessed | source only | REF-01 checkpoint lacks nonzero-gradient hypothesis |
| 58 | `sec-9-critical-points` | yes | yes | witnessed | source only |  |
| 59 | `sec-9-second-derivatives-and-the-hessian-matrix` | yes | yes | witnessed | source only |  |
| 60 | `sec-9-the-second-derivative-test` | yes | yes | witnessed | source only |  |
| 61 | `sec-9-constrained-optimization-and-lagrange-multipliers` | yes | no; see note | witnessed | source only | REF-01 checkpoint lacks regular defining-function hypothesis |
| 62 | `sec-9-warning-examples` | yes | no; see note | witnessed | source only | REF-02 endpoint hint misidentifies missing hypothesis |
| 63 | `sec-9-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 64 | `sec-10-from-area-to-volume-by-slicing` | yes | yes | witnessed | source only |  |
| 65 | `sec-10-double-integrals-over-rectangles` | yes | yes | witnessed | source only |  |
| 66 | `sec-10-iterated-integrals-and-fubini-s-theorem` | yes | yes | witnessed | source only |  |
| 67 | `sec-10-double-integrals-over-general-regions` | yes | yes | witnessed | source only |  |
| 68 | `sec-10-double-integrals-in-polar-coordinates` | yes | yes | witnessed | source only |  |
| 69 | `sec-10-applications-of-double-integrals` | yes | yes | witnessed | source only |  |
| 70 | `sec-10-improper-double-integrals` | yes | yes | witnessed | source only |  |
| 71 | `sec-10-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 72 | `sec-11-triple-integrals` | yes | yes | witnessed | source only |  |
| 73 | `sec-11-general-solid-regions` | yes | yes | witnessed | source only |  |
| 74 | `sec-11-cylindrical-coordinates-in-integrals` | yes | no; see note | witnessed | source only | ROOT-01; ROOT-02 |
| 75 | `sec-11-spherical-coordinates-in-integrals` | yes | no; see note | witnessed | source only | ROOT-01; ROOT-02 |
| 76 | `sec-11-applications-of-triple-integrals` | yes | yes | witnessed | source only |  |
| 77 | `sec-11-higher-dimensional-integrals` | yes | yes | witnessed | source only |  |
| 78 | `sec-11-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 79 | `sec-12-the-geometry-of-substitution` | yes | yes | witnessed | source only |  |
| 80 | `sec-12-linear-changes-of-variables` | yes | yes | witnessed | source only |  |
| 81 | `sec-12-nonlinear-changes-of-variables-in-the-plane` | yes | yes | witnessed | source only |  |
| 82 | `sec-12-changes-of-variables-in-space` | yes | yes | witnessed | source only |  |
| 83 | `sec-12-pullbacks-of-area-and-volume-elements` | yes | yes | witnessed | source only |  |
| 84 | `sec-12-warning-examples` | yes | yes | witnessed | source only |  |
| 85 | `sec-12-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 86 | `sec-13-vector-fields` | yes | yes | witnessed | source only |  |
| 87 | `sec-13-line-integrals-of-scalar-functions` | yes | yes | witnessed | source only |  |
| 88 | `sec-13-work-integrals-of-vector-fields` | yes | yes | witnessed | source only |  |
| 89 | `sec-13-differential-1-forms` | yes | yes | witnessed | source only |  |
| 90 | `sec-13-conservative-vector-fields-and-exact-1-forms` | yes | no; see note | witnessed | source only | ROOT-03 |
| 91 | `sec-13-curl-tests-in-the-plane-and-in` | yes | no; see note | witnessed | source only | ROOT-03 |
| 92 | `sec-13-warning-examples` | yes | yes | witnessed | source only |  |
| 93 | `sec-13-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 94 | `sec-14-circulation-around-a-small-rectangle` | yes | yes | witnessed | source only |  |
| 95 | `sec-14-green-s-theorem-circulation-form` | yes | yes | witnessed | source only |  |
| 96 | `sec-14-green-s-theorem-flux-form` | yes | yes | witnessed | source only |  |
| 97 | `sec-14-green-s-theorem-in-differential-form-language` | yes | no; see note | witnessed | source only | GS-01 theorem-restatement closure hypothesis; awaiting independent classification challenge |
| 98 | `sec-14-why-green-s-theorem-is-true` | yes | no; see note | witnessed | source only | Root U03 proof-support dependency: c13s6-lem-parameter-integral uses an unsupplied finite-subcover principle; formula remains a previously stated lemma |
| 99 | `sec-14-warning-examples` | yes | yes | witnessed | source only |  |
| 100 | `sec-14-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 101 | `sec-15-parametric-surfaces-and-tangent-planes` | yes | yes | witnessed | source only |  |
| 102 | `sec-15-surface-area-and-scalar-surface-integrals` | yes | yes | witnessed | source only |  |
| 103 | `sec-15-oriented-surfaces-and-flux` | yes | yes | witnessed | source only |  |
| 104 | `sec-15-flux-2-forms` | yes | yes | witnessed | source only |  |
| 105 | `sec-15-curl-and-stokes-theorem` | yes | yes | witnessed | source only |  |
| 106 | `sec-15-divergence-and-the-divergence-theorem` | yes | yes | witnessed | source only |  |
| 107 | `sec-15-classical-vector-calculus-identities` | yes | yes | witnessed | source only |  |
| 108 | `sec-15-warning-examples` | yes | yes | witnessed | source only |  |
| 109 | `sec-15-chapter-review-and-applications` | yes | yes | witnessed | source only |  |
| 110 | `sec-16-what-is-a-differential-form` | yes | yes | witnessed | source only |  |
| 111 | `sec-16-covectors-and-differentials` | yes | yes | witnessed | source only |  |
| 112 | `sec-16-the-wedge-product` | yes | yes | witnessed | source only |  |
| 113 | `sec-16-algebra-of-forms` | yes | yes | witnessed | source only |  |
| 114 | `sec-16-pullbacks` | yes | yes | witnessed | source only |  |
| 115 | `sec-16-integrating-forms` | yes | yes | witnessed | source only |  |
| 116 | `sec-16-chapter-review-and-translation-table` | yes | yes | witnessed | source only |  |
| 117 | `sec-17-the-exterior-derivative-of-a-0-form` | yes | yes | witnessed | source only |  |
| 118 | `sec-17-the-exterior-derivative-of-a-1-form` | yes | yes | witnessed | source only |  |
| 119 | `sec-17-the-exterior-derivative-of-a-2-form` | yes | yes | witnessed | source only |  |
| 120 | `sec-17-the-rule-d-squared-equals-zero` | yes | no; see note | witnessed | source only | GF-02: formal coefficient calculation displayed as d(dg) although dg is not C1 |
| 121 | `sec-17-closed-and-exact-forms` | yes | no; see note | witnessed | source only | GF-01: homotopy-grid subsequence/uniform-control premise unavailable; parameter lemma also inherits shared missing support |
| 122 | `sec-17-warning-examples` | yes | yes | witnessed | source only |  |
| 123 | `sec-17-chapter-review-and-translation-table` | yes | yes | witnessed | source only |  |
| 124 | `sec-18-boundaries-and-orientation` | yes | yes | witnessed | source only |  |
| 125 | `sec-18-the-theorem` | yes | yes | witnessed | source only |  |
| 126 | `sec-18-the-fundamental-theorem-of-calculus-as-stokes` | yes | yes | witnessed | source only |  |
| 127 | `sec-18-green-s-theorem-as-stokes` | yes | yes | witnessed | source only |  |
| 128 | `sec-18-classical-stokes-theorem-as-generalized-stokes` | yes | yes | witnessed | source only |  |
| 129 | `sec-18-the-divergence-theorem-as-generalized-stokes` | yes | yes | witnessed | source only |  |
| 130 | `sec-18-proof-ideas` | yes | yes | witnessed | source only |  |
| 131 | `sec-18-the-grand-translation-table` | yes | yes | witnessed | source only |  |
| 132 | `sec-18-warning-examples` | yes | yes | witnessed | source only |  |
| 133 | `sec-18-chapter-review-and-capstone-problems` | yes | no; see note | witnessed | source only | GF-05: any-surface task omits compactness; literal exterior-plane surface has divergent integral |
| 134 | `sec-19-balance-laws-from-flux` | yes | yes | witnessed | source only |  |
| 135 | `sec-19-the-continuity-equation` | yes | no; see note | witnessed | source only | GF-01: fixed compact solid uniform-continuity estimate extends interval lemma without the shared supporting compactness result |
| 136 | `sec-19-heat-wave-and-equilibrium-equations` | yes | yes | witnessed | source only |  |
| 137 | `sec-19-maxwell-s-equations-as-a-forms-gateway` | yes | no; see note | witnessed | source only | Inherited GF-01 proof dependency through parameter-integral lemma and closed-1-form theorem; local formulas and stated theorem applications checked |
| 138 | `sec-19-potential-theory-and-harmonic-functions` | yes | no; see note | witnessed | source only | GF-03: relative-open/closed connectedness propagation not supplied; inherited GF-01 parameter lemma proof premise |
| 139 | `sec-19-chapter-review-and-modeling-projects` | yes | yes | witnessed | source only |  |
| 140 | `sec-20-geometry-and-visualization-projects` | yes | yes | witnessed | source only |  |
| 141 | `sec-20-optimization-projects` | yes | yes | witnessed | source only |  |
| 142 | `sec-20-integration-projects` | yes | no; see note | witnessed | source only | GF-04: selected Monte Carlo route lacks pointer to later executable sampling recipe; two illustrative runs were executed, not a convergence proof |
| 143 | `sec-20-vector-calculus-projects` | yes | yes | witnessed | source only |  |
| 144 | `sec-20-differential-forms-projects` | yes | yes | witnessed | source only |  |
| 145 | `sec-20-writing-projects` | yes | yes | witnessed | source only |  |
| 146 | `sec-appA-limits-and-continuity` | yes | yes | witnessed | source only |  |
| 147 | `sec-appA-derivatives-and-linear-approximation` | yes | yes | witnessed | source only |  |
| 148 | `sec-appA-the-fundamental-theorem-of-calculus` | yes | yes | witnessed | source only |  |
| 149 | `sec-appA-substitution-and-integration-by-parts` | yes | yes | witnessed | source only |  |
| 150 | `sec-appA-parametric-and-polar-curves` | yes | yes | witnessed | source only |  |
| 151 | `sec-appA-infinite-series-and-taylor-polynomials` | yes | yes | witnessed | source only |  |
| 152 | `sec-appA-one-page-formula-summary` | yes | yes | witnessed | source only |  |
| 153 | `sec-appB-algebraic-manipulation-and-inequalities` | yes | yes | witnessed | source only |  |
| 154 | `sec-appB-trigonometric-identities` | yes | yes | witnessed | source only |  |
| 155 | `sec-appB-complex-numbers-and-rotations` | yes | yes | witnessed | source only |  |
| 156 | `sec-appB-euler-s-formula` | yes | yes | witnessed | source only |  |
| 157 | `sec-appB-complex-roots-and-geometry` | yes | yes | witnessed | source only |  |
| 158 | `sec-appB-one-page-formula-summary` | yes | yes | witnessed | source only |  |
| 159 | `sec-appC-matrix-operations` | yes | yes | witnessed | source only |  |
| 160 | `sec-appC-row-reduction` | yes | yes | witnessed | source only |  |
| 161 | `sec-appC-determinants` | yes | yes | witnessed | source only |  |
| 162 | `sec-appC-inverse-matrices` | yes | yes | witnessed | source only |  |
| 163 | `sec-appC-eigenvalues-and-eigenvectors` | yes | yes | witnessed | source only |  |
| 164 | `sec-appC-quadratic-forms` | yes | yes | witnessed | source only |  |
| 165 | `sec-appC-one-page-formula-summary` | yes | yes | witnessed | source only |  |
| 166 | `sec-appD-polar-coordinates` | yes | yes | witnessed | source only |  |
| 167 | `sec-appD-cylindrical-coordinates` | yes | yes | witnessed | source only |  |
| 168 | `sec-appD-spherical-coordinates` | yes | yes | witnessed | source only |  |
| 169 | `sec-appD-grad-curl-and-divergence-in-common-coordinates` | yes | yes | witnessed | source only |  |
| 170 | `sec-appD-area-and-volume-elements` | yes | yes | witnessed | source only |  |
| 171 | `sec-appD-one-page-formula-summary` | yes | yes | witnessed | source only |  |
| 172 | `sec-appE-0-forms-1-forms-2-forms-and` | yes | yes | witnessed | source only |  |
| 173 | `sec-appE-wedge-product-rules` | yes | yes | witnessed | source only |  |
| 174 | `sec-appE-pullbacks` | yes | yes | witnessed | source only |  |
| 175 | `sec-appE-exterior-derivative-formulas` | yes | yes | witnessed | source only |  |
| 176 | `sec-appE-classical-vector-calculus-translated-into-forms` | yes | yes | witnessed | source only |  |
| 177 | `sec-appE-generalized-stokes-theorem-summary` | yes | yes | witnessed | source only |  |
| 178 | `sec-appE-one-page-formula-summary` | yes | yes | witnessed | source only |  |
| 179 | `sec-appF-differentiability-and-continuous-partial-derivatives` | yes | yes | witnessed | source only |  |
| 180 | `sec-appF-equality-of-mixed-partials` | yes | yes | witnessed | source only |  |
| 181 | `sec-appF-fubini-s-theorem-and-change-of-variables` | yes | yes | witnessed | source only |  |
| 182 | `sec-appF-green-s-theorem` | yes | yes | witnessed | source only |  |
| 183 | `sec-appF-stokes-theorem` | yes | yes | witnessed | source only |  |
| 184 | `sec-appF-divergence-theorem` | yes | yes | witnessed | source only |  |
| 185 | `sec-appF-generalized-stokes-theorem` | yes | yes | witnessed | source only |  |
| 186 | `sec-appF-dependency-chart` | yes | yes | witnessed | source only |  |
| 187 | `sec-appF-one-page-theorem-summary` | yes | yes | witnessed | source only |  |
| 188 | `sec-appG-plotting-surfaces-and-contour-maps` | yes | yes | witnessed | source only |  |
| 189 | `sec-appG-visualizing-vector-fields` | yes | yes | witnessed | source only |  |
| 190 | `sec-appG-numerical-differentiation-and-the-jacobian` | yes | yes | witnessed | source only |  |
| 191 | `sec-appG-numerical-double-and-triple-integration` | yes | yes | witnessed | source only |  |
| 192 | `sec-appG-symbolic-line-and-surface-integrals` | yes | yes | witnessed | source only |  |
| 193 | `sec-appG-simulating-flows-and-conservation-laws` | yes | yes | witnessed | source only |  |
| 194 | `sec-appG-one-page-computational-summary` | yes | yes | witnessed | source only |  |

## Nonsection files

| File | Semantic read |
|---|---|
| `source/main.ptx` | yes |
| `source/docinfo.ptx` | yes |
| `source/frontmatter.ptx` | yes |
| `source/chapters/ch01-points-vectors-space/ch01-points-vectors-space.ptx` | yes |
| `source/chapters/ch02-vector-products/ch02-vector-products.ptx` | yes |
| `source/chapters/ch03-linear-functions-matrices/ch03-linear-functions-matrices.ptx` | yes |
| `source/chapters/ch04-curves-coordinates-surfaces/ch04-curves-coordinates-surfaces.ptx` | yes |
| `source/chapters/ch05-vector-valued-functions/ch05-vector-valued-functions.ptx` | yes |
| `source/chapters/ch06-functions-limits-continuity/ch06-functions-limits-continuity.ptx` | yes |
| `source/chapters/ch07-partial-derivatives-jacobian/ch07-partial-derivatives-jacobian.ptx` | yes |
| `source/chapters/ch08-chain-rule-coordinate-changes/ch08-chain-rule-coordinate-changes.ptx` | yes |
| `source/chapters/ch09-gradient-optimization/ch09-gradient-optimization.ptx` | yes |
| `source/chapters/ch10-double-integrals/ch10-double-integrals.ptx` | yes |
| `source/chapters/ch11-triple-higher-integrals/ch11-triple-higher-integrals.ptx` | yes |
| `source/chapters/ch12-change-of-variables/ch12-change-of-variables.ptx` | yes |
| `source/chapters/ch13-vector-fields-line-integrals/ch13-vector-fields-line-integrals.ptx` | yes |
| `source/chapters/ch14-greens-theorem/ch14-greens-theorem.ptx` | yes |
| `source/chapters/ch15-surfaces-flux-curl-divergence/ch15-surfaces-flux-curl-divergence.ptx` | yes |
| `source/chapters/ch16-differential-forms-wedge/ch16-differential-forms-wedge.ptx` | yes |
| `source/chapters/ch17-exterior-derivatives/ch17-exterior-derivatives.ptx` | yes |
| `source/chapters/ch18-generalized-stokes/ch18-generalized-stokes.ptx` | yes |
| `source/chapters/ch19-conservation-laws/ch19-conservation-laws.ptx` | yes |
| `source/chapters/ch20-capstone-projects/ch20-capstone-projects.ptx` | yes |
| `source/backmatter.ptx` | yes |
| `source/appendices/appA-single-variable-review/appA-single-variable-review.ptx` | yes |
| `source/appendices/appB-algebra-trig-complex/appB-algebra-trig-complex.ptx` | yes |
| `source/appendices/appC-matrix-algebra/appC-matrix-algebra.ptx` | yes |
| `source/appendices/appD-coordinate-systems/appD-coordinate-systems.ptx` | yes |
| `source/appendices/appE-differential-forms-quickref/appE-differential-forms-quickref.ptx` | yes |
| `source/appendices/appF-proof-sketches/appF-proof-sketches.ptx` | yes |
| `source/appendices/appG-computational-labs/appG-computational-labs.ptx` | yes |

## Remaining work boundary

No missing active files or unreviewed source sections remain. The identified logical corrections are proposed, not implemented. Known support limitations remain open in the textbook. Complete per-figure rendered layout, print compilation, arbitrary user-selected empirical project datasets and a formal theorem certification are outside the completed evidence. Strict schema validation fails on the existing backlog; see validation.md.