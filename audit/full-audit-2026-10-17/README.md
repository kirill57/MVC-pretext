# MVC book full audit and corrections

The active PreTeXt edition was reviewed across all 20 chapters, seven appendices, 195 sections, and 919 exercise prompts. The three source-review ledgers record 105 corrected findings; the integration pass also repaired inherited PreTeXt markup, accessibility descriptions, the placeholder preface, and remaining visual layout defects. The original LaTeX archive was preserved.

The review retains the first-year route, the ordinary frozen-parameter surface velocities in Section 5.2, intuitive advanced connections, and clearly marked folded optional material. Exercise review checked the supplied prerequisites, statements, hints, solutions, and feasible solution routes. Targeted exact and numerical calculations independently challenged worked results and delicate proof claims; open-ended projects were checked for feasibility rather than a unique answer.

## Important mathematical corrections

- Corrected the repeated hill value to `H(2,1)=167/2` and its tangent-plane intercept to `163/2`.
- Supplied quaternion algebra assumptions before regrouping products and corrected a misleading square-relation checkpoint.
- Repaired missing hypotheses for determinant formulas, continuity, inverse derivatives, extrema, integral averages, theorem applications, and appendix formulas.
- Compared differentiability remainders with input displacement length, avoiding division by a possibly vanishing linear term.
- Corrected the Riemann nonintegrability checkpoint, separation-of-variables hint, coordinate sign conventions, and radial-shell interpretation.
- Distinguished formal mixed-partial cancellation from the classical exterior derivative when regularity is insufficient; supplied differentiability for the counterexample potential.
- Tightened orientation, regularity, coverage, boundary-seam cancellation, and neighborhood assumptions in forms and Stokes arguments.
- Corrected modeling and computational examples, variable descriptions, code prerequisites, and misleading exercise or checkpoint ordering.

## Visual and organizational corrections

Live HTML inspection covered all 232 active pages, all 204 figures through 313 figure/table captures, all 122 table captures, and page-heading contact sheets. Suspected missing portions of two figures were traced to a sticky-navigation screenshot artifact and independently checked against their complete native SVGs.

Confirmed label collisions were corrected in the lap/displacement, spherical-shell, local-continuity, capacitor, and annulus figures. All four late-chapter figures passed a second independent local render check. Green's theorem review arrays became semantic tables; the substitution checklist became an ordered list. Optional derivations retain native accessible folds and expand into the full reading column. The linear-map animation was activated in the actual browser and advanced from `t=0` through an intermediate frame to `t=1`, ending with the Replay control.

## Validation and reproducibility

The final HTML source passes `pretext validate web --report-form terse` with no schema errors or validation-plus messages. The existing native animation is reported as one experimental construct, which is informational. `pretext build web` succeeds without source or deprecation warnings. Windows denies cleanup of one temporary output directory after a successful build; this does not affect the generated book.

All 3542 original explicit identifiers are retained. The source check finds 3547 identifiers, 311 references, 195 sections, and no structural/reference failures. The local output link audit checked 410643 local links, fragments, knowls, and asset references across 265 generated HTML files with zero failures. The additional generated HTML files include interactive figure wrappers.

The live baseline and local browser sweeps use Chromium at 1280 px and 390 px widths, load MathJax, open all native details, inspect assets and math errors, and record screenshots. Mathematical rendering, asset loading, overflow, and fold checks pass across all 232 local pages. The sweep found one intermittent Asymptote WebGL stack overflow in Section 4.1: a folded example initialized its frame at zero viewport size, producing an invalid subdivision tolerance. The stylesheet now defers Asymptote frames until visible. The [runtime investigation](browser-error-review.json) records the failure, diagnosis, ten successful diagnostic trials and three successful tests of the rebuilt production HTML, including opening the example and resizing it. The renderer itself remains unmodified. A final sweep of all 35 Asymptote-containing pages, covering all 58 diagrams, passed with no runtime, formula, asset, or layout errors. Eleven side-by-side child figures required capturing their image boxes because their outer elements use `display:contents`; a focused three-page recheck closed those screenshot-only gaps. Long formulas may scroll within their display on narrow phones. Desktop optional derivations now fit the reading column. This audit concerns the HTML edition; it does not assert a page-by-page PDF layout review or a formal proof that no further error can exist.

Reproduce the checks from the repository root with the pinned PreTeXt environment and its configured graphics tools. The browser audit additionally uses Playwright with Chromium, Pillow, and lxml:

```powershell
pretext validate web --report-form terse
pretext build web
python tools/check_prerequisites.py
python tools/check_html_links.py output/web
pretext view web --no-launch --port 8137
python tools/audit_html.py --base http://127.0.0.1:8137/output/web/ --output logs/full-audit-2026-10-17/local --screenshots --mobile
```

## Evidence and complete finding lists

Screenshots and detailed build/browser logs remain in the ignored `logs/full-audit-2026-10-17` directory. The committed compact verification receipt records the final results and the separate runtime recheck. Source ledgers contain section coverage, exercise routes, corrected findings, computational checks, and material qualifications.

- [Chapters 1 to 6 and Appendices A to B](ch01-06.json)
- [Chapters 7 to 13 and Appendices C to D](ch07-13.json)
- [Chapters 14 to 20 and Appendices E to G](ch14-20.json)
- [Independent mathematical and visual challenge](independent-review.json)
- [Final local figure verification](final-figures.json)
- [Table review](tables-review.json)
- [Later page-header review](pages-review.json)
- [Structural migration receipt](markup-migration.json)
- [Original identifier preservation](source-preservation.json)
- [Integration corrections](root-findings.json)
- [Final validation receipt](verification.json)
- [Asymptote runtime investigation and production verification](browser-error-review.json)

## Chapters 1 to 6 and Appendices A to B

- **C2-01** The checkpoint claimed i^2=-1 alone forces an ordinary Euclidean quarter turn. Replaced by the actual coordinate rotation and norm check; square relation now confirms two turns.
- **C2-02** Explicitly supplied distributivity, central real scalars, and associativity before algebraic regrouping; corrected ij deduction to use k^2=-1 with associativity.
- **C2-03** Replaced an invalid implication from passing through zero to reversing sign by term pairing in the explicit determinant formulas.
- **C3-01** Added the nonzero coefficient-vector hypothesis to the level-hyperplane checkpoint.
- **C3-02** Added nonzero determinant before the three-dimensional Cramer quotient formulas.
- **C4-01** Declared standard spherical ranges and axis/origin angle exceptions; made x!=0 explicit for tangent conversion.
- **C4-02** Declared positive semiaxis parameters in the ellipsoid model and quadric gallery.
- **C5-01** Placed the already optional swept-area 1-form connection in a titled paragraphs block marked Optional so publication folding can hide it.
- **C5-02** Identified -g k as gravitational acceleration rather than force; Newton equation and derived formulas retained.
- **C6-01** Handled isolated domains in componentwise continuity proof and replaced the punctured-limit substitution proof of composition by direct epsilon/delta continuity control, including repeated intermediate values.
- **C6-02** Qualified directional steepness comparison to equal distances from the summit along the axes; adjusted matching review exercise to remove a location-dependent ambiguity.
- **A-01** Specified two-sided neighborhood, endpoint, relative-domain, and isolated-point conventions.
- **A-02** Critical points must be defined interior domain points; explicitly extended oscillatory example at zero.
- **A-03** Stated a sufficient C^(n+1) interval hypothesis for Taylor Lagrange remainder at the actual evaluation point.
- **A-04** Added piecewise C1 length hypotheses, x!=0 conversion condition, and single-coverage nonnegative-radius polar-area conditions; synchronized summary.
- **A-05** Supplied C1/continuity sufficient hypotheses, explained signed substitution does not need monotonicity, and specified du/dv notation; average-value formula elsewhere now requires a<b.
- **B-01** Restricted arbitrary real exponent laws to positive bases and separated integer exponent/root cases; circle parameter R explicitly positive.
- **B-02** Specified integer exponents for de Moivre and Euler power formulas, with nonzero base for negative powers.
- **B-03** Declared positive integer n and nonzero target; recorded zero-target and n=1,2 polygon exceptions; synchronized summary and root index range.
- **B-04** Specified nonnegative swept angle for unsigned arc length, inverse trig derivative domains and inverse-function notation, and x!=0 for tan conversion.

## Chapters 7 to 13 and Appendices C to D

- **M071** Repeated numerical hill-height error: H(2,1)=167/2=83.5, not169/2=84.5; corrected all Chapter7 occurrences and tangent-plane intercept163/2.
- **M072** Quadratic remainder is small compared with input step length; comparison with the linear term fails when that term cancels. Corrected.
- **M081** Physical lengths must stay nonnegative on reversed coordinate steps; added absolute values.
- **M082** Inverse-derivative derivation now assumes differentiability of map and local inverse, separating this conditional formula from the later existence theorem.
- **M083** Remainder argument now uses bounded displacement/time ratio and explicitly handles zero displacement; avoids claiming proportional nonzero motion.
- **P081** Moved checkpoint after the variables, diagram and formulas it asks students to read.
- **M091** Second-order term need not be first visible nonzero behavior. Intro now allows zero/flat quadratic term and higher-order classification; differential zero written as0, not vector0.
- **M092** Extreme-value theorem now explicitly nonempty; practical candidate table includes failure of derivatives.
- **M101** Corrected false hint that every integrand is a quantity per unit area; height times area is volume, density times area mass,1 times area area.
- **M102** Failure of Riemann integrability need not cause oscillation in every cell. Replaced by area-weighted oscillation-sum criterion and distinguished small bad sets.
- **M103** Average-value definition now requires an integrable function and finite positive area.
- **M104** Explained that the two closed L-shape rectangles differ from the setminus description on zero-area boundary segments only.
- **M105** Concentration comparison example now assumes continuity/local integrability rather than deducing Riemann integrability from an integrable upper bound.
- **M106** Restored nonnegative/absolute-convergence restrictions in improper-integral summary; replaced hardcoded Problem10 with semantic xref.
- **M111** Replaced falsely necessary factorization claim by sufficient rule for separated factors on independent limits. Explained partially angle-dependent separated densities and supplied checked solution.
- **M112** Replaced unquantified near-surface conclusion from one half-size cube by explicit fixed-distance-to-face fraction(1-epsilon)^n and checked optional solution.
- **M113** Corrected volume grows like rho² to thin-shell volume per unit radial thickness grows like rho².
- **P111** Specified centimeter coordinates and mass72 grams in gel-block example.
- **P112** Qualified universal assertion that cylindrical coordinates solve every axis-organized problem.
- **M121** Clarified injectivity on the interior versus permitted boundary repetitions; crease splitting uses smooth branch extensions that satisfy theorem's open-neighborhood hypotheses.
- **M122** Clarified interior injectivity versus boundary repetition in spatial substitution theorem.
- **M131** Warning example formerly inferred availability of dPhi merely from existing partials. Added |Phi|<=|xy|<=r²/2 proving total differentiability and exactness at origin while coefficients lack C1.
- **M132** Average along curve now requires finite positive length and continuous integrand. Supplied harmonic-series lower-bound explanation for infinite-length oscillatory curve.
- **P131** Removed misleading distrust of dot product; checkpoint now asks why the metric factor makes dot product and form calculations agree.
- **P132** Fixed a the constant curve typo.
- **AC01** Defined pivots in echelon form, avoiding apparent identification of arbitrary leading entries with independent pivot columns.
- **AC02** Reference change-of-variables formula now cites its global hypotheses and uses explicit T* for oriented area rather than equating forms on distinct domains.
- **AC03** Restricted direction-language to real eigenvectors/eigenvalues; specified positive integer powers. Summary now states nonzero eigenvectors, full basis, symmetric positive-definite setting.
- **AD01** Distinct coordinate pairs represent the same point; replaced literal tuple equalities by defined equivalence relation. Added nonnegative radius and quadrant/axis-safe angle recovery; relabeled general integral as integral, not area.
- **AD02** Added nonnegative radius and sine/cosine angle recovery including x=0; tangent shorthand now correctly limited and quadrant-qualified.
- **AD03** Explained appendix variable order(rho,phi,theta) versus reversed angular order and sign. Added radius/inclination recovery, axis-safe azimuth and away-origin cone equation scope.

## Chapters 14 to 20 and Appendices E to G

- **14-01** Restricted reversal claim to 1-form integrals.
- **14-02** Replaced with two semantic 2-column tables; preserved Green formula and corrected C1 open-neighborhood checklist.
- **15-01** Defined compact surface without boundary.
- **15-02** Unpaired edges trace true boundary; paired seams cancel with opposite orientations.
- **15-03** Distinguished pointwise coefficient expressions from unavailable classical exterior derivative; repaired checkpoint and C2 gradient summary.
- **15-04** Explained volume expansion/compression; mass uses density-weighted flux.
- **16-01** Put 1 outside text command.
- **16-02** Supplied coefficient-distributive coordinate concatenation definition and sign rules.
- **16-03** Restricted to repeated 1-form; even-degree factor need not square to zero.
- **16-04** Added compact, continuous-coefficient, piecewise regular, one-cover integration contract.
- **16-05** Allowed coordinate seams/zero-volume exceptional sets under change-of-variables hypothesis.
- **16-06** Fixed integrand and reversed ordered orientation.
- **16-07** Independent degree-to-degree input/output rows.
- **17-01** Restored bounded closure and C1 open-neighborhood scope.
- **17-02** Specified k>=1 and C2 primitive in exact-implies-closed theorem.
- **17-03** Said no global beta exists with alpha=d beta.
- **17-04** Caption excises small ball, cavity label says removed ball, inner normal leader moved away.
- **17-05** Split g partial derivatives, radial-potential derivative calculation and contraction boundary conditions into shorter rows.
- **18-01** Closed and bounded in surrounding Euclidean space.
- **18-02** Specified dx wedge dy orientation.
- **18-03** Replaced with correctly mixed text/math two x-faces label.
- **18-04** Oriented boundary equals zero; second exterior derivative equals zero.
- **18-05** Corrected b2 <= r2 <= a2 and specified 0<b<a.
- **18-06** Moved checkpoint after H(y) and boundary integral calculation.
- **18-07** Stated compact piecewise smooth boundary and C1 field on open neighborhood of whole surface.
- **18-08** Matching induced boundaries and C1 form neighborhoods of each whole admissible surface suffice.
- **18-09** C2 regular oriented surface patch with paired seam cancellation; C2 orientation-compatible solid diffeomorphism, C1 form.
- **18-10** Added C1 primitive and open-neighborhood/admissible compact surface or bounded solid assumptions.
- **19-01** Scoped to solely bulk transport; law on every fixed control region.
- **19-02** Effective in-plane conductivity includes plate thickness; c>0 explicit.
- **19-03** Time-independent equilibrium ut=0, hence utt=0.
- **19-04** Stated established properties under supplied regularity and boundary hypotheses.
- **19-05** Regular level curves are streamlines; critical points are stationary velocities.
- **19-06** Marked usual ideal-capacitor approximation and separately supplied exact total-current equality.
- **19-07** Each compact admissible surface, shared induced boundary and C1 magnetic 1-form neighborhood; no swept volume needed.
- **19-08** Short in/out labels, density label below box, electric-field and plates labels separated with leader.
- **20-01** Parallel to yz-plane; tangent slice caption says vertical slices; gradients require regular level point.
- **20-02** Specified r,h,V positive; strict convexity and endpoint blow-up prove unique absolute minimum h=2r.
- **20-03** Convergence exactly 0<alpha<1; behavior discussion scoped to nonzero start.
- **20-04** Mass-weighted root-mean-square distance.
- **20-05** Area average vs heat capacity, areal density or depth, rainfall-depth integral as water volume.
- **20-06** Explained cancellation; compare grids or known exact solution.
- **20-07** Only angle-form winding may change; exact-form closed-loop integral stays zero.
- **20-08** Tracked quantity can have sources; source-free conserved quantity cannot.
- **20-09** Outer label anchored outside ring; inner label placed in cavity.
- **E-01** Corrected 1-,2-,k-form text/math boundaries.
- **F-01** C1 field on open neighborhood of closure.
- **F-02** Inserted f continuous on R.
- **G-01** Recipes are independent; supply functions/bounds/placeholders.
- **G-02** Sympify components and use simultaneous=True.
- **G-03** xfun/yfun/zfun names.
- **G-04** Created 7x7x7 meshgrid, explicit helical field (-Y,X,onesZ).
- **G-05** Divergence zero is incompressibility; source-free advective law then gives density constant along particles.
- **G-06** Zero extension g with independent uniform points; code already evaluates f only inside mask.
