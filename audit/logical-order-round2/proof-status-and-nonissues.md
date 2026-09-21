# Proof status, deferred destinations and protected material

Snapshot `9a9d110af839b539fe598de66ecc4320a4126af4`. Every active source section and wrapper was read. This record distinguishes a theorem available for use from a complete in-book proof. The [two graphs](dependency-graphs.json) encode task/capability availability separately from critical mathematical proof dependencies. They are not an exhaustive formal derivation of every theorem or algebraic step.

## Deferred proofs and supplied roots

| Earlier passage | Exact destination/support | Scope and result of audit |
|---|---|---|
|1.5 `thm-triangle-inequality`|2.4 `c2s4-cor-triangle-inequality`, preceded by independent `c2s4-thm-cauchy-schwarz`|All real finite dimensions, including zero vectors. The algebraic proof is independent of triangle inequality; no cycle. The residual checkpoint wording is LO-12.|
|5.2 `c5s2-def-regular-grid-point`|15.1 `c15s1-thm-tangent-plane-to-a-parametrized-surface` and preceding regular-patch/local-graph argument|Nearby continuous grid velocities become C1 partials; the proof uses the full first-order vector remainder for all increments and a rank2 local graph. The promised stronger tangent-sheet justification exists. Preserve5.2.|
|10.2 linear midpoint example|10.3 `c10s3-thm-fubini-rectangles` plus entry polynomial integration|The later iterated-integral method verifies that affine functions have exact midpoint sums on rectangles. This explanatory forward expectation is not a new named theorem or an improper-integral argument.|
|13.6 `c13s6-thm-curl-test-simply-connected`|17.5 `c17s5-thm-simply-connected-potential`|Plane scope is included in the later n=2/3 theorem: open, path-connected, simply-connected domain and C1 closed1-form. Local primitives and continuous homotopy-grid cancellation are correct; LO-01 leaves the compactness supporting premise unsupplied. The statement is available, but the promised proof is not fully supported under the entry contract.|
|13.8 `c13s8-project-polygon`|14.7 `c14s7-ex-shoelace`|Finite edge formula is already calculated; Green's theorem then proves its area interpretation for a simple positively oriented polygon. No circular use of the shoelace area identity is needed.|
|6.4 EVT|`c6s4-thm-extreme-value-theorem`|Explicitly supplied on a nonempty closed bounded set; no full in-book proof promised. It does not automatically teach finite subcovers or subsequences.|
|8.5 inverse theorem;8.6 implicit results|`c8s5-thm-inverse-function`, `c8s6-thm-ift-plane-curve`, `c8s6-thm-ift-surface`|Inverse existence/C1 regularity is supplied; differentiating the inverse identity proves only its derivative formula. The scalar implicit graph results use augmented maps and the supplied inverse theorem.|
|General change of variables|12.3 `c12s3-thm-change-of-variables-plane`;12.4 `c12s4-thm-change-of-variables-space`|Precise C1, coverage, Jacobian and region conditions are supplied. The limiting discussion is a proof idea, not a full general measure-theoretic proof. Earlier determinant algebra remains independent.|
|Green, classical Stokes, divergence|14.2/14.3;15.5/15.6;18.4–18.7|Exact rectangle/box and finite regular-chart arguments are distinguished from general patching/limiting sketches. General statements are supplied for use. LO-09 is a weaker restatement, not a defect in the precise earlier Green theorem.|
|Generalized Stokes|18.2 `c18s2-thm-generalized-stokes`;18.7 proof ideas; AppendixF wrapper|Supplied for compact oriented piecewise smooth objects in the book's dimensions1–3. The book does not promise a complete arbitrary-dimensional manifold proof. Surface naturality is independently expanded with chain/product rules and C2 mixed-derivative cancellation, avoiding a Stokes/naturality cycle.|
|Curvature/torsion uniqueness and optional Hodge notation|5.5 closing preview;19.4 optional future connection|No required task depends on proving curve uniqueness or computing an unintroduced Hodge star. These remain previews, not missing entry prerequisites.|

The exact source locations/hashes are machine-resolvable in the ledger and graph. Supplied roots are not converted into “proved here” claims by this audit.

## Significant protected decisions

- Section4.5 stays geometric. Section5.2 introduces ordinary derivatives of frozen-parameter curves, parameter regularity and cross-product normals at the proper point in the progression. Section7.5 supplies the partial/Jacobian language;15.1 supplies full tangent-plane theory. The plane/cone/sphere probes distinguish chart defects from genuine image singularities.
- Section2.7 legitimately introduces arbitrary two-covector wedge and the fixed coordinate three-form. LO-02 concerns only the later arbitrary triple/grouping operation. Do not remove the early forms lesson.
- Section3.4 proves determinant scaling/product independently by coordinate/permutation expansion. Section7.2 proves its gradient rule without assuming the later chain rule. The matrix chain-rule remainder is controlled by an explicit matrix bound.
- Existing partials, all directional derivatives, total differentiability and continuous partials are different capabilities. The current early warning examples preserve those distinctions. The17.4 display problem is specifically application of the exterior derivative outside its stated coefficient class.
- The Gaussian integral uses bounded-square Fubini and disk comparison before taking limits. Required exercises can reconstruct it without improper Fubini. The polar theorem is supplied earlier with sector-area motivation; the Chapter11 repair can build on it without a general3D substitution cycle.
- Scalar length/area densities use nonnegative speed/norm factors. Work/flux/forms retain traversal or orientation signs. Reversing scalar integration order is not reversing orientation. Double coverage and boundary coordinate collapse are treated separately.
- The nonlinear shear `(u,v)->(u,v+u²)` has determinant1; the text already rejects the false rule that every nonlinear map must have a varying Jacobian.
- The punctured-plane angular form is closed but not exact; the radial logarithmic form on the same punctured domain is exact. A hole permits an obstruction but does not force every closed form to be nonexact.
- The Maxwell local magnetic primitive is actually constructed. Spacetime d4 is defined before use with the relevant signs and C2 scope. Fixed-domain conservation assumptions are explicit; no moving-domain transport theorem is silently supplied.
- The entropy, least-squares, cone-truncation and surface-integration project witnesses use taught or locally supplied tools. AppendixG code limits and sampling variability remain visible rather than being mistaken for general numerical convergence proofs.

## Complete partition evidence and independent challenge

The detailed source-first proof status is retained in five partitions:

- [Chapters1–8](fragments/foundations/proof-status-and-nonissues.md)
- [Chapter9 and AppendicesA–E](fragments/reference/proof-status-and-nonissues.md)
- [Chapters10–13](fragments/root/proof-status-and-nonissues.md)
- [Chapters14–15](fragments/greens-surfaces/proof-status-and-nonissues.md)
- [Chapters16–20 and AppendicesF/G](fragments/general-forms/proof-status-and-nonissues.md)

Each partition's primary judgments were checked against the earlier report only after fresh source analysis where practical. Challenges used different readers and attempted contextual defenses as well as counterexamples. The linked challenge records in findings.md distinguish retained literal defects from lower-confidence editorial severity. [Exact diagnostic probes](evidence/counterexample-probes.md) include all examples required by the audit brief.

No new circular proof was established. The mechanical cycle check likewise found none in the recorded critical dependency graph. Neither observation proves that every possible dependency in the book has been formally encoded or certified. Known unsupported premises remain explicit under LO-01 and LO-05; intended proof sketches keep their stated limits.
