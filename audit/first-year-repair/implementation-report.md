# First-year repair implementation

The user authorized implementation of the revised ordered plan and requested folded optional material. All LO-01 through LO-14 repairs are implemented locally. The baseline commit remains 9a9d110af839b539fe598de66ecc4320a4126af4; these are uncommitted working-tree changes. The original LaTeX/archive sources were not edited.

## Result

| Finding | Implemented behavior |
|---|---|
|LO-01|13.5 supplies the path-subdivision theorem before using it; 13.6 states the parameter-integral rule and its uniform-control background, with a two-route polynomial illustration. 17.5 retains the radial-potential/contraction/cancellation proof in a folded optional panel. 19.2 states the fixed-region rule for area and volume. Appendix F contains four optional guided analysis exercises with complete solutions and an explicitly supplied completeness fact.|
|LO-02|The folded Chapter 11 oriented-volume connections define a triple wedge by three covectors on the same vector space, evaluated pointwise. A folded extension derives the local rules. The sign change between (r,z,theta) and (r,theta,z) is explicit. Chapter 12 repeats the definitions for its core route.|
|LO-03|General cylindrical and spherical integration theorems are supplied with continuity, domain and once-coverage conditions. Guided derivations prove the formulas for arbitrary continuous integrands on a specified cylinder and ball. Their scope is not inflated to all regions.|
|LO-04|The mixed-partial difference remains 2, but the example no longer calls that number a value of d(dg). The needed regularity facts are stated, with the first-derivative estimates in a folded optional panel.|
|LO-05|A core guided exercise proves circle and then disk constancy. Global propagation is supplied; the complete relative-open/relative-closed argument is folded and marked optional.|
|LO-06|Gradient normals require C1 and a nonzero defining gradient. The plane defined by z versus z-squared illustrates the distinction. The multiplier checkpoint allows a zero objective gradient and explains the squared-circle failure.|
|LO-07|The endpoint checkpoint distinguishes a tangent line from two-sided feasible motion.|
|LO-08|The review continuity criterion is restricted to accumulation points and explicitly handles isolated points.|
|LO-09|The forms version of Green's theorem inherits the closed bounded region, boundary orientation and open-neighborhood C1 hypotheses.|
|LO-10|The Hessian preview explains its future notation and starts folded, with an optional title.|
|LO-11|The basis-images checkpoint explicitly assumes linearity; the existing nonlinear counterexample remains.|
|LO-12|Triangle equality includes zero vectors and coincident stops.|
|LO-13|The Monte Carlo project links directly to the sampling recipe and explains independent uniform coordinate draws, the mask, total-N denominator and fluctuating error.|
|LO-14|The spanning-surface exercise specifies compactness, induced counterclockwise boundary and regularity. Its checked primitive 3x dy yields 3pi.|

Two existing problems were strengthened instead of adding duplicates: the repeated-cylinder-coverage exercise now compares 4pi with 8pi, and the line-integral checkpoint compares scalar length and work under reversal. The preexisting optional higher-dimensional section and its review exercises now fold as well.

## Folding and content locations

The stylesheet xsl/optional-folds.xsl, selected by the web target in project.ptx, uses PreTeXt's native details/summary renderer for optional exercises and small titled divisions. Native asides already start folded. Optional headings begin with **Optional:**. The feature does not depend on custom browser JavaScript.

All 3,505 original semantic IDs remain. The new source has 3,527 IDs.

| Original content | Current location / wrapper |
|---|---|
|13.5 unnamed compactness step inside the path-independence proof|Uses c13s5-thm-path-subdivision; the fuller justification is appF-ex-path-grid-subdivision.|
|13.6 finite-cover paragraph inside c13s6-lem-parameter-integral|Replaced by an explicit supplied uniform-continuity fact and its MVT estimate; fuller argument in appF-ex-uniform-continuity.|
|17.5 unnamed proof inside c17s5-thm-simply-connected-potential|c17s5-optional-potential-proof, a following optional aside. The theorem ID and statement remain.|
|11.3 and 11.4 form-language paragraphs|c11s3-optional-oriented-volume and c11s4-optional-oriented-volume, within the original volume-element subsections.|
|3.6 Hessian-preview content|Still in c3s6-subsec-hessian-preview, inside c3s6-optional-hessian-content. The table ID remains.|
|11.6 four subsections|The four c11s6-subsec-* IDs and their content remain in place; wrappers are now foldable paragraphs divisions. The introductory material is in c11s6-optional-introduction.|
|19.5 unnamed maximum-principle proof idea|Local mechanism in c19s5-ex-averaging-forces-local-constancy; global proof in c19s5-optional-global-propagation. The theorem ID remains.|

The ordered plan's previously proposed compulsory compactness exercises were never textbook content. The new Appendix F investigation therefore does not remove any existing source IDs.

## Learning and mathematical checks

[task-checks.json](task-checks.json) records routes for all 209 exercises in the affected section files: 197 core and 12 optional. Nineteen new or changed exercises received current explicit mathematical route checks; unchanged prompts retain their previously audited routes, checked against the changed prerequisites. This is a same-agent integration review, not a claim of independent review.

The skip check removes optional passages from the dependency analysis:

- Chapter 11 core applications use the supplied scalar integral theorems. Its core review questions about the fixed Cartesian volume form use the existing Chapter 2 definition; they require no arbitrary triple-wedge calculation. The numerical project uses scalar formulas only.
- The cylindrical derivation uses planar polar integration on the continuous sliced function. The spherical derivation starts from the supplied cylindrical theorem, then uses planar polar integration and an angle substitution. Neither uses the later general substitution theorem to prove itself.
- Chapter 12 supplies its own determinant definition and rules after the optional previews are skipped.
- Potentials, parameter integrals and conservation laws have visible supplied statements. The 14.5 moving-endpoint calculation still uses the fixed-interval lemma plus FTC and the chain rule. Maxwell's surface/solid calculations use the fixed-region theorem on fixed parameter domains, whereas its local vector-potential calculation correctly uses the one-dimensional parameter lemma. The circle-mean derivative also uses that lemma.
- The maximum-principle checkpoint separates the local averaging mechanism from the supplied global result. Its optional proof is not required.

All seven references crossing from the retained route into optional content are explicitly optional-proof/navigation references; their contexts are in [skip-test-links.json](skip-test-links.json). None is the sole source of a core operation.

The optional analysis proof dependencies are acyclic: nested-box completeness is supplied; subsequence extraction uses it; uniform continuity, cover control and subdivision use subsequences. The potential proof uses the parameter lemma and subdivision, not an assumed embedded spanning surface. The optional propagation proof uses local averaging and the stated definition of connectedness. Links from the Appendix F solutions back to applications identify those applications, rather than using their conclusions as premises.

The new solutions check zero cases, one-sided endpoints, parameter orientation and operator regularity. The ball-volume check is explicitly distinguished from the arbitrary-integrand derivation. The squared-plane and squared-circle diagnostics distinguish a poor defining function from a singular geometric set.

## Validation

The installed executable was verified as PreTeXt **2.53.0**, matching requirements.txt.

| Check | Result |
|---|---|
|PreTeXt web build with --no-generate|**Pass, exit 0** after all source edits; [build log](build-final.log). Existing graphics were reused.|
|XML, active XIncludes, IDs, references and graphics nesting|**Pass:** 226 active files, 195 sections, 3,527 IDs, 304 references, zero structural errors. Two preexisting inactive XML/PTX files remain.|
|Audit scanner/annotation fixtures|**12 pass.** These test the audit tooling, not mathematical truth.|
|Optional HTML rendering|**21 titled optional blocks** are native closed details elements with visible Optional labels. [Machine receipt](verification.json).|
|Original IDs and protected content|No original IDs lost; Sections 4.5 and 5.2 and all image source elements are unchanged.|
|Git whitespace|Pass with the cr-at-eol setting, respecting the repository's existing tracked CRLF files.|
|Strict schema/semantic validation|**Still fails, exit 1: 1,319 inherited messages**, comprising 1,073 schema messages plus the same 246 additional messages. Four inherited 11.6 subsection-structure errors were repaired; **zero new diagnostics**.|

[Diagnostic comparison](diagnostic-comparison.json) matches rule/message, source file and semantic object, allowing line changes. Jing's reported XPath incorrectly points into a preceding paragraph for several Chapter 17 subsection errors. Their assembled start tags and the complete ordered set of direct-subsection diagnostics identify the affected IDs; this normalization is recorded explicitly. It does not rely on totals alone.

The HTML build retains ten preexisting deprecated exercise-list warnings and a Windows temporary-directory cleanup warning. These are distinct from a successful HTML conversion and from the strict-validation failures.

Browser checks used the local preview to verify initial collapsed state and expansion in the cylindrical/spherical connections, Hessian preview, higher-dimensional section, potential proof, regularity panel, maximum-principle proof and new Appendix F investigation. The inspected pages rendered mathematics without reported MathJax errors. The spherical panel and Appendix F exercise were also visually inspected. HTML checks cover all 21 optional blocks; browser checks are representative, not a claim that every page received a screenshot review.

No graphics were changed, so no fresh Asymptote compilation was needed or claimed. A print/PDF build was not run. No commit, push or publication was performed.

Reproduce the focused checks from the repository root:

    ./.cache/grid-velocities-venv/Scripts/pretext.exe build web --no-generate
    ./.cache/grid-velocities-venv/Scripts/pretext.exe validate web --method local --report-form terse
    ./.cache/grid-velocities-venv/Scripts/python.exe tools/check_prerequisites.py
    ./.cache/grid-velocities-venv/Scripts/python.exe audit/logical-order-round2/tools/test_fixtures.py
    ./.cache/grid-velocities-venv/Scripts/python.exe audit/first-year-repair/verify_repair.py
    git -c core.whitespace=cr-at-eol diff --check
