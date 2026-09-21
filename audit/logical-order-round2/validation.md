# Validation receipt

Audit-only snapshot: `9a9d110af839b539fe598de66ecc4320a4126af4`, branch `main`. Work directory: `D:/work/sabbatical/2025/Books/MVC-pretext`. The nominal OneDrive task directory was not used as the source checkout.

## Baseline and toolchain

The controlling audit brief, applicable conversion instructions, `project.ptx`, requirements, frontmatter and prior audit artifacts were read. The matching local executable is `.cache/grid-velocities-venv/Scripts/pretext.exe`, PreTeXt2.53.0. Its Python is3.13 with lxml6.0.2. Existing ignored local Asymptote/Jing configuration was retained. This audit did not reinstall the toolchain or regenerate assets.

Commands actually run in the checkout:

```powershell
git rev-parse HEAD
git branch --show-current
git status --short
./.cache/grid-velocities-venv/Scripts/pretext.exe --version
./.cache/grid-velocities-venv/Scripts/pretext.exe build web --no-generate
./.cache/grid-velocities-venv/Scripts/pretext.exe validate web --method local --report-form terse
./.cache/grid-velocities-venv/Scripts/python.exe audit/logical-order-round2/tools/inventory.py
./.cache/grid-velocities-venv/Scripts/python.exe audit/logical-order-round2/tools/test_fixtures.py
./.cache/grid-velocities-venv/Scripts/python.exe audit/logical-order-round2/tools/consolidate.py
./.cache/grid-velocities-venv/Scripts/python.exe audit/logical-order-round2/tools/compose_reports.py
./.cache/grid-velocities-venv/Scripts/python.exe audit/logical-order-round2/tools/validate_artifacts.py
git diff --check
```

The inventory command ran before semantic review; later fixture invocations use isolated temporary fixture roots and do not overwrite that snapshot. Partition scripts also generated their own witness/coverage evidence. Early integration checks caught audit-metadata shape and duplicated-support issues; these were repaired in the audit artifacts, not in the textbook.

| Check | Actual result |
|---|---|
|Active XML/XInclude inventory|225 active files;194 sections;3505 IDs;285 cross-reference records; zero parsing, missing-fragment, duplicate-ID or unresolved-reference issues.|
|Configured HTML build|**Pass, exit0.** Assets were reused with `--no-generate`; this is not a fresh Asymptote compilation result.|
|Strict schema/semantic validation|**Fail, exit1:1323 messages**, exactly1077 schema plus246 additional validation messages.|
|Active-source preservation|All225 file hashes still match the inventory; HEAD unchanged; no tracked diff.|
|Task reconciliation|All910 formal task elements witnessed; all1122 mechanical candidates witnessed or explicitly classified. No missing candidate disposition.|
|Artifact checks|JSON/source locations and hashes validated; exact counts in `evidence/artifact-validation.json`. Zero errors and zero cycles in the recorded proof graph.|
|Forward-support triage|Ten edges are local project scaffolds inside a containing project and precede the separately witnessed hand-in steps; one is the explicitly reported Monte Carlo navigation gap. None is silently accepted as a later prerequisite. Zero support edges point only into a hidden solution.|
|Scanner/annotation fixtures|12 pass. Ten test reviewer-supplied capability/proof annotations; two execute the real inventory for nonlexical XInclude order and a missing fragment. These tests do not certify semantic sufficiency.|
|Git whitespace|`git diff --check` succeeds; tracked source has no changes. Audit Markdown/JSON is additionally parsed/checked by the audit tools.|

Receipts: [HTML build log](evidence/baseline-build-web.log), [strict-validation command log](evidence/baseline-validate.log), [complete strict-validation report](evidence/baseline-validation-report.txt), [category counts](evidence/validation-counts.json), [fixture results](evidence/fixtures.json), [integration summary](evidence/integration-summary.json), and [artifact validation](evidence/artifact-validation.json).

The246 additional messages comprise185 missing image descriptions,24 Unicode em dashes,17 Unicode en dashes,18 Unicode double quotes and2 Unicode single quotes. The1077 schema errors include the existing book-wide section-structure problems. The build also reports10 deprecated lists directly inside exercise statements and a Windows temporary-directory cleanup warning (`WinError5`, external/images). The successful HTML build does not erase these failures. These are baseline results: no post-repair validation can be claimed because no repair was implemented.

## Rendered and computational checks

The rebuilt local Section5.2 page was reloaded at `http://localhost:8137/output/web/sec-5-derivatives-and-integrals-of-vector-valued-functions.html`. Browser inspection verified the grid-velocity definition, its link to Theorem15.1.10, and the visible cone figure/caption at `c5s2-fig-double-cone-grid-velocities`. The figure labels use ordinary v,w,N, show the collapsed vertex, and the caption qualifies the arrow scaling. The existing preview tab was retained for the author.

This is a current-run spot-check of that subsection, not an inherited claim of whole-book rendering. All other graphic labels were inspected in source. No figure was regenerated, no full layout/accessibility review was performed, and the print target was not built.

Exact manual calculations cover the counterexample probes, Gaussian bounds, sign/multiplicity cases and high-risk task solutions. Independent review also recomputed the12 entries of the Chapter11 three-method volume table. The general-forms worker ran focused SymPy checks and extracted the actual AppendixG midpoint/Monte Carlo function bodies for constant-value, empty-mask and two seeded sampling checks; its exact versions, calls and outputs are in the [runtime receipt](fragments/general-forms/proof-status-and-nonissues.md#runtime-validation-receipt). Those finite experiments do not prove convergence or general runtime compatibility.

## What remains unverified or unchanged

No textbook source, historical archive, prior audit report, remote repository or Git history was changed. No commit, push, PR, merge or deployment occurred. The logical repair plan is proposed only. The existing schema backlog and the listed logical support/scope findings remain open in the textbook. Most rendering, print compilation, arbitrary empirical project choices and a formal certification of every mathematical argument remain outside the evidence. Full source reading and successful record checks are not described as a clean logical or schema pass.
