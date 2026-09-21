# MVC-pretext — independent full logical-order and prerequisite audit

## 0. Assignment, scope, and authority

Perform an independent, source-based audit of the active textbook in `kirill57/MVC-pretext`. Determine whether a student following the declared reading order can understand every required statement, calculation, proof, example, checkpoint, and exercise using material already explained, explicitly declared entry prerequisites, or a sufficient local introduction.

This assignment is **audit first**, followed by an implementable repair plan. Do not rewrite the textbook merely because a scanner finds an unfamiliar word. Unless the author separately authorizes implementation, write audit artifacts and proposed changes only. Do not commit, push, open a pull request, merge, deploy, or modify the remote repository. Preserve unrelated local work.

The target is an undergraduate multivariable-calculus textbook. Do not import the prerequisites, proof standards, or chapter structure of an unrelated graduate/Almost Mathieu book. Preserve the textbook's intended progression from geometry to calculus to differential forms.

### Snapshot and existing work

- Repository: `kirill57/MVC-pretext`.
- Snapshot examined for this second-pass brief: `9a9d110af839b539fe598de66ecc4320a4126af4`.
- Snapshot date: September 20, 2026.
- Active entry point: `source/main.ptx`.
- Previous, now historical baseline: `328f9b437edd3eb80e6d6aa8f85cd1704fcec7f8`.
- Current reports include `PREREQUISITE_AUDIT.md`, `PREREQUISITE_COVERAGE.md`, and the associated rewrite report. The coverage report records 194 active sections: 145 chapter sections and 49 appendix sections. Recompute these counts; do not hard-code them.
- The earlier instruction file, `MVC-pretext-Codex-prerequisite-rewrite-plan.md`, documents the first correction campaign. Its proposed introduction schedule has been refined subsequently.

**Preserve the later author-directed decision about Section 5.2.** It now introduces ordinary derivatives of frozen-parameter surface curves, regular parameter points, and a cross-product normal, after vector differentiation. It avoids surface-partial shorthand and explicitly points to the later full tangent-plane justification. Section 7.5 supplies the partial-derivative/Jacobian language; Chapter 15 develops the systematic surface theory. Do not restore the obsolete plan that forbade every surface-tangent discussion until Chapter 15. Keep Section 4.5 geometric.

Before beginning, record the actual HEAD, branch, working-tree status, and relevant uncommitted changes. If HEAD has advanced, compare the passages named in this brief with the actual checkout. Do not reproduce an old defect by overwriting a newer correction.

Read applicable repository instructions, including `CONVERSION-PLAN.md`, `CONVERSION-AGENT.md`, any applicable `AGENTS.md`, the frontmatter, and the existing audit artifacts. Treat prior findings as leads and prior dispositions as claims to verify, not as proof of correctness. After identifying operational constraints, make fresh judgments from the source before consulting the old disposition for each candidate where practical.

Keep `multivariable_calculus/` and its archive read-only. They are historical source material, not the currently taught reading path. A definition in the old LaTeX source does not establish that the active PreTeXt reader has received it.

## 1. The student contract

The current `source/frontmatter.ptx` explicitly assumes algebra, trigonometry, and single-variable calculus, including limits, continuity, differentiation rules, the Mean Value Theorem, definite integrals, the Fundamental Theorem of Calculus, and basic substitution. It explicitly does not assume prior multivariable calculus, differential geometry, or exterior algebra. Appendices are references, not silently assumed prior reading.

Use that contract, rather than an imagined mathematically mature reader, to evaluate dependencies. Do not solve a prerequisite problem by quietly adding real analysis, topology, differential equations, linear algebra, or exterior algebra to the entry requirements. Any proposed change to the reader contract must be explicit and submitted as an editorial decision.

At the same time, do not demand explanations of every elementary algebraic manipulation already covered by the contract. The standard is sufficient preparation for the task, not definition-first formalism or maximal expansion.

A worked example can introduce an idea before a formal definition. A discovery exercise can introduce a rule by giving all the data needed to derive it. Neither is a defect merely because the named theorem comes later.

## 2. The central test: availability of a capability

Do not track only the first appearance of a word or symbol. Track the first sufficient explanation of the **specific capability** needed at a particular point.

For each required use U, establish at least one of:

1. The capability is explicitly included in the entry contract.
2. An earlier, accessible passage sufficiently defines or explains it and provides the rule needed at U.
3. The current passage supplies that explanation before the student must use it.
4. A precisely stated theorem has been supplied for use under explicit hypotheses, with honest proof status and no disguised circular proof.

A hyperlink to a later definition does not, by itself, satisfy a present computational prerequisite. A later proof can legitimately support a theorem whose complete statement and hypotheses have already been supplied for use. Distinguish these situations.

For each concept or operation, separately record:

- first mention;
- first concrete explanation;
- first formal definition, where present;
- first demonstrated computation;
- first justified general rule;
- first required use;
- later generalizations and changes of scope.

Not every concept needs seven different locations. Multiple roles can be filled by one passage. The point is to prevent an earlier mention from being mistaken for an earlier lesson.

### Examples of capabilities that must remain distinct

| Earlier material | What it does not automatically authorize |
|---|---|
| The coordinate volume form evaluated on three vectors | Arbitrary three-covector wedge expansion or grouping a 2-form with a 1-form |
| Wedge of two covectors | Vector bivectors, general exterior powers, or arbitrary-degree products |
| A determinant of a derivative matrix | The change-of-variables theorem for integrals |
| Two coordinate-curve derivatives at one point | A differentiable surface patch and its full tangent-plane approximation |
| Existence of partial derivatives | Total differentiability or a valid linear differential |
| Pointwise continuity | A uniform estimate over an entire compact parameter set without its supporting argument |
| A correct calculation for a polynomial | A theorem for all functions with the stated regularity |
| A statement that a domain is one piece | The relative-open/relative-closed characterization of connectedness |
| The formula for d on C1 forms | Applying that operator to a form outside its stated domain |
| A supplied special-case theorem | A proof of every higher-dimensional or lower-regularity generalization |

## 3. Classification and severity

Classify before recommending a change. Allow more than one classification when justified, but identify the root cause.

**A — Required prerequisite gap.** The reader must perform an operation or use a notion without sufficient earlier or local preparation.

**B — Local ordering problem.** The support exists in the same section, but a checkpoint, proof, example, or visible label requires it too early.

**C — Optional preview.** A genuinely dispensable, clearly identified forward-looking passage. This may deserve simplification, but it is not automatically a logical dependency defect.

**D — Legitimate early special case.** A sufficient local introduction precedes a later general treatment. Preserve it unless a separate problem is found.

**E — Supplied theorem or postponed proof.** The theorem may be used under its stated hypotheses, but its proof status and destination must be accurate. Distinguish a supplied standard theorem from a theorem promised to be proved later.

**F — Circular or incomplete claimed justification.** A proof uses its own conclusion, a downstream consequence, or an unestablished extension. Identify the actual dependency chain; do not call a true theorem false.

**G — Type, domain, or notation mismatch.** Examples include vector versus covector, Jacobian matrix versus determinant, a scalar value versus a differential, unsigned measure versus an oriented form, and applying an operator outside its declared regularity class.

**H — Hypothesis or quantifier gap.** Examples include promoting a directional estimate to a uniform one, ignoring multiplicity, changing a sufficient condition into a necessary one, or using a pointwise assertion over a whole region.

**I — Navigation or assessment dependency leak.** An optional section, appendix, hidden solution, outdated caption, or stale review item supplies an unannounced prerequisite to a required task.

Priority levels:

- **P1:** blocks a required argument/task, creates circular reasoning, or materially misrepresents a mathematical operation or theorem.
- **P2:** a real local/background gap or scope ambiguity with a modest repair.
- **P3:** preview clarity, navigation, or exposition improvement without an established blocking dependency.

State the evidence status separately: confirmed local observation; supporting source not yet found; disputed classification; resolved; protected/nonissue. Severity is not confidence.

## 4. Reconstruct the real reading order

Follow the actual `xi:include` chain from `source/main.ptx`. Do not sort filenames or infer order from a legacy ID. The inserted quaternion and torsion lessons already demonstrate why this matters.

Include chapter wrappers, introductions, frontmatter, backmatter, appendices, and all referenced source fragments. Record repeated inclusion occurrences if a fragment is included in more than one place. Distinguish active material from orphaned or archived files.

An inventory record should contain:

- snapshot SHA and source hash;
- source path, original line range, and XML ID;
- inclusion ancestry and inclusion occurrence;
- actual chapter/section position and title;
- position within the section;
- element role;
- whether the material is required, optional, a hint, a solution, or a preview;
- relevant visible mathematical text;
- cross-reference targets.

Preserve source locations while expanding includes. A convenient XML parser may be used, but do not lose the origin of an included node. Report unsupported XInclude features or parsing failures rather than silently dropping content.

### What is student-facing?

Read prose, definitions, theorem statements, proofs and proof sketches, examples, exercises, projects, chapter reviews, hints, solutions, tables, figure captions, image descriptions, and visible labels inside graphics. A formula embedded in a figure can create exactly the same prerequisite gap as a displayed equation.

Macro definitions in `docinfo.ptx` do not teach their mathematical meaning. Code comments that are not rendered are not student-facing explanations. Conversely, a label inside an Asymptote or TikZ figure may be visible even when a text-only scan overlooks it.

Do not require every unchanged figure to be redrawn. Inspect rendered output where the meaning or visibility of a label matters; record whether inspection was source-only or rendered. Never report rendered review when only source code was read.

## 5. Build two dependency graphs, not one

### 5.1 Learning-availability graph

An edge records that passage U needs capability C, and points to the earlier/local passage that makes C available. Include assessment and optional-material status. This graph answers: could a student reach U with the needed tools?

### 5.2 Mathematical-proof graph

An edge records that a proof of result R depends on a stated result S, an entry assumption, or a separately proved supporting lemma. A forward proof reference is allowed here, but it must not close a cycle.

A supplied theorem may be an explicitly declared root of the book's proof graph. That is honest only when it is identified as supplied, not simultaneously advertised elsewhere as fully proved within the book. Do not require a full proof of general Stokes or the inverse function theorem merely because the book teaches their use.

For every theorem with a deferred proof:

1. Find the exact promised destination.
2. Compare dimensions, regularity, domain assumptions, boundary assumptions, multiplicity, and conclusion.
3. Verify that the destination contains the promised proof rather than a restatement or another forward pointer.
4. Trace its supporting results for circularity.
5. Record any intentionally supplied general theorem whose in-book proof covers only a special case.

Do not manufacture a mathematical cycle from harmless motivational references. State the exact implications needed by the purported proof.

## 6. Concept ledger and type checks

Use capability-level entries. A useful machine-readable form is:

```json
{
  "concept_id": "wedge.three_covectors",
  "name": "Wedge of three linear scalar measurements",
  "type": "V* x V* x V* -> alternating trilinear forms on V",
  "scope": "real finite-dimensional coordinate spaces",
  "first_mention": null,
  "first_sufficient_explanation": null,
  "first_required_use": null,
  "rules_available": [],
  "prerequisite_concepts": [],
  "source_evidence": [],
  "confidence": "pending"
}
```

Fill source records with the actual path, XML ID, line range, and snapshot. Do not leave an important capability's support as a vague chapter number.

Audit families should include:

- set, domain, image, level set, boundary, open/closed set, relative openness/closedness, connected/path-connected/simply connected;
- finite covers, subsequences, compactness, uniform continuity and uniform estimates;
- scalar/vector functions, linear maps, independence, bases, transpose, determinant, inverse, rank, quadratic forms;
- curve parameter, traversal, orientation, regularity, velocity, arc length, curvature, torsion and frames;
- partial/directional/total derivative, differentials, Jacobian matrix and determinant, gradient, Hessian;
- chain rule, inverse/implicit functions, optimization hypotheses and constrained critical points;
- Riemann sums, mesh, integrability, general-region integrals, Fubini, changes of variables and improper integrals;
- scalar line/surface measures versus work and flux, parameter coverage, multiplicity, orientation;
- covectors, coordinate forms, two-covector and three-covector wedge rules, general-degree forms, pullbacks, exterior derivatives, closed/exact forms;
- boundary orientation, Green/Stokes/divergence, differentiating parameter integrals, conservation laws and PDE operations;
- any probability, entropy, ODE, numerical, or computational notions actually required in applications and appendices.

This is a search map, not a claim that each family contains a defect or a mandate to introduce every topic early.

## 7. Full audit passes

### Pass 1 — Fresh sequential student reading

Read each section in actual order while maintaining the available-capability ledger. Stop at every new symbol, rule, or inference that would make the student ask “what operation is that?” or “why is that allowed?” Resolve the question from preceding/local source, not from your own mathematical knowledge.

Use general knowledge to diagnose what support would be needed, but label any proposed new lemma or explanation as a repair, not as existing book content.

### Pass 2 — Required exercise and checkpoint reconstruction

For every required task, write a dependency witness: a solution outline sufficient to identify the needed methods and the exact earlier/local support for each. Compute explicitly where the solution or prerequisite status is uncertain. Fully solve the high-risk, moved, or ambiguous tasks.

A difficult problem is not a prerequisite defect when it can genuinely be solved from taught tools. A discovery problem can be legitimate before the theorem it is intended to reveal. Conversely, an expected solution that silently invokes a future theorem is a defect even when the answer is simple.

A hint can provide an announced scaffold. A hidden solution that introduces the missing theory after the attempt does not retroactively prepare the student. Record scaffolded and unscaffolded availability separately.

Check optional lessons and required chapter reviews together. An item is not genuinely optional if later required work depends on it without another explanation.

### Pass 3 — Theorem and proof audit

Check the exact inference at every “therefore,” “by continuity,” “by compactness,” “clearly,” “as before,” “recall,” “the same argument,” and “in general” in a proof. Do not object to these phrases mechanically. Determine what mathematical fact the phrase is actually using.

In particular, inspect:

- finite-to-infinite and pointwise-to-uniform transitions;
- differentiating or taking limits under an integral;
- changing variables based only on a derivative calculation;
- claiming a tangent plane from two coordinate directions alone;
- local-to-global potential arguments;
- support of arbitrary-dimension statements by only 2D/3D calculations;
- general forms versus decomposable wedges;
- smoothness and open-neighborhood hypotheses;
- repeated coverage, seams, axes, poles, boundary parameters and singular charts.

Do not expand a deliberately identified proof sketch into an entire analysis course. Record its ceiling and check that subsequent text does not promote the sketch to a full proof.

### Pass 4 — Global notation and type consistency

Follow each overloaded symbol through the book. Explicitly inspect:

- `r` as radius versus a vector parametrization;
- subscripts indexing a family versus denoting derivatives;
- `J` as matrix versus scalar determinant;
- `dx` as coordinate covector, its value on a vector, a pulled-back differential, and notation in an ordinary integral;
- `d` as differential, exterior derivative, or ordinary derivative notation;
- boundary `partial` versus partial differentiation;
- scalar area/volume factors versus oriented forms;
- vectors versus covectors and the role of the Euclidean dot product;
- physical time versus a geometric parameter;
- polar/spherical angle order and signed versus absolute Jacobians.

Do not replace every wedge by a cross product or every differential by a finite increment. Those changes would erase mathematical distinctions the book intends to teach.

### Pass 5 — Cross-reference and appendix audit

Verify that each reference supplies the actual prerequisite, not merely a related subject. A reference can resolve syntactically and still be semantically wrong.

An appendix is a valid support when the reader is directed to a sufficiently precise passage at the point of need. It is not silently prior material simply because it exists somewhere in the book. Treat appendix sections according to their intended independent/reference reading routes.

### Pass 6 — Counterexample and boundary-case review

Test questionable general assertions using examples tailored to the claimed implication. Use exact calculations where practical. Do not claim that numerical sampling proves a theorem.

A compact test collection:

1. A continuous two-parameter map whose image is a curve or point.
2. A smooth plane with a degenerate parametrization versus a genuinely singular cone.
3. A sphere with a collapsed polar coordinate edge.
4. A function with existing partial derivatives but no total derivative.
5. A C1 function whose mixed second partials at one point exist but disagree; respect the stated domain of exterior differentiation.
6. A field with a potential on a domain that has a hole: simple connectivity is sufficient, not necessary for a particular field.
7. An orientation-reversing coordinate change versus reversing an ordinary iterated integration order.
8. A double covering in a parametrized integral.
9. A nonlinear map with constant Jacobian determinant.
10. A pointwise-convergent family without the uniform control needed to exchange limit and integral. For an optional exact test on [0,1], `f_n(t)=n^2 t(1-t)^n` tends pointwise to zero, while its integral tends to one.

Verify examples before using them. The tests diagnose implications; they are not a requirement to insert all ten examples into the book.

### Pass 7 — Independent challenge and consolidation

A second reviewer/pass should try to refute both the proposed defects and the “supported” judgments. Ask whether an earlier special case was missed, whether a task is a legitimate discovery problem, and whether the proposed repair introduces a new prerequisite.

When multiple agents are available, partition reading work but maintain a shared versioned concept ledger. Chapter-local approval cannot establish a cross-chapter dependency. Have a separate integration review check the global graph and all relocated material.

Do not claim an independent review occurred unless a genuinely separate review was performed. A second pass by the same agent is useful but should be described accurately.

## 8. Seed findings from the second targeted pass

The findings below come from source windows in thirteen current chapter sections, together with repository searches, wrappers, frontmatter, and existing reports. They are not a second line-by-line certification of all 194 sections. Reconfirm every finding against the actual checkout, and distinguish observed use from an exhaustively established absence of earlier support.

### U01 — Three-factor wedge operations precede their sufficient rule

**Priority/class:** P1 or P2 depending on whether the passage is required; A/G.

**Uses:**

- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml`, `c11s3-subsec-volume-element`.
- `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml`, `c11s4-subsec-volume-element`.

The cylindrical calculation derives `dx wedge dy = r dr wedge dtheta` and then appends `wedge dz`; the spherical lesson gives a transformed triple wedge. The source now explains where the differentials live, which is a genuine repair. That explanation does not itself define multiplying a two-form by a one-form or evaluating an arbitrary triple of covectors.

**Earlier special case:** Section 2.7, `c2s7-def-volume-form-dx-dy-dz`, defines the coordinate volume form by its value on three vectors. Do not misreport the basic triple symbol as entirely absent earlier.

**Later sufficient rule:** Section 12.5, `c12s5-subsec-pulling-back-volume-elements`, explicitly defines the determinant evaluation of `alpha wedge beta wedge gamma` for three linear scalar measurements and explains grouped expressions, distribution, and repeated factors.

**Preferred repair:** If the Chapter 11 forms comparisons are optional, move their unsupported triple-product manipulation to 12.5 and retain the ordinary integration lesson. If the audit establishes an intentional, required earlier use, move the compact three-covector determinant rule to the earliest appropriate algebraic location and reference it thereafter. Do not add general exterior algebra merely to support one identity.

### U02 — The volume element needs an explicit integration bridge

**Priority/class:** P1/P2; A/E/F, according to the final proof-status decision.

**Uses:** The same `c11s3-subsec-volume-element` and `c11s4-subsec-volume-element`.

The lessons proceed from approximate tiny-box geometry, and then determinant/form identities, to exact integral computations. The scale factors are correct. The remaining issue is the unannounced step from local scaling to a rule for integrating over a region. A derivative determinant is not, by itself, the substitution theorem.

**Recommended independent route, requiring no chapter reorder:**

1. Derive cylindrical integration by Fubini and the already taught planar polar rule, applied to horizontal slices.
2. For spherical integration, fix the azimuth `theta` and work in the meridional half-plane `(r,z)`.
3. Use the planar polar substitution `r=rho sin(phi)`, `z=rho cos(phi)`. In unsigned area, its scale factor is `rho`.
4. The existing cylindrical weight `r` then becomes `rho sin(phi)`, so the total weight is `rho^2 sin(phi)`.
5. State continuous-integrand, region, once-covering, angular-range, and degeneracy conventions at the level actually justified. Start with suitable bounded coordinate regions; handle seams/axes/poles explicitly rather than assuming global injectivity.

For clarity, planar polar coordinates here can be written with angle `psi=pi/2-phi`. The meridional signed determinant is negative in `(rho,phi)` order, but the ordinary area factor is positive `rho`. Do not create an orientation-sign error while supplying the unsigned integration argument.

An alternative is to state the spherical special-case substitution theorem precisely for use, identify the tiny-box discussion as motivation, and give an honest later justification. The author should not be forced into a full general change-of-variables proof just to repair this lesson.

### U03 — Finite-cover compactness is an unannounced supporting principle

**Priority/class:** P2; A/F (supporting analysis).

**Location:** Section 13.6, `c13s6-lem-parameter-integral`.

The added parameter-integral proof selects finitely many neighborhoods covering a closed interval and takes the minimum of their allowed increment sizes. This is the right strategy, but it invokes the finite-subcover property. The proof calls this the usual finite-cover argument without first supplying that principle there.

The current entry contract does not explicitly assume real-analysis compactness. The targeted search did not locate an earlier finite-subcover theorem. The full audit must confirm its first sufficient support rather than treating the absence as established solely by a keyword search.

**Repair:** Supply a short closed-interval finite-cover lemma, or explicitly direct the student to an appropriate supporting proof before this use. Then show how it produces one increment bound valid for all integration parameters. Keep the parameter-integral lemma; do not replace it by an unexplained “differentiate under the integral sign.”

### U04 — The new homotopy proof invokes a subsequence theorem

**Priority/class:** P2; A/F (same supporting-analysis family as U03).

**Location:** Section 17.5, `c17s5-thm-simply-connected-potential`.

The square-subdivision argument invokes the bounded-sequence subsequence theorem coordinate by coordinate. The theorem name and the selected subsequence are doing mathematical work. The targeted repository search found this invocation, not an earlier statement/proof of the supporting theorem.

**Repair:** Provide the needed bounded-sequence/nested-interval lemma with an explicit reference, or derive the uniform local-control statement using the already supplied finite-cover toolkit. Do not replace a continuous contraction by a smooth contraction, and do not assume every loop bounds an embedded smooth surface. Preserve those strengths of the current proof.

Count U03/U04 as separate occurrences with a shared potential root repair, not automatically as two unrelated theory insertions.

### U05 — Relative openness/closedness enters the maximum-principle argument

**Priority/class:** P2; A/G in a proof sketch, not a false theorem.

**Location:** Section 19.5, `c19s5-thm-no-interior-maximum`.

The proof idea says that the maximum-attaining set is open in R and closed in R, hence equals connected R. The relative meanings and the connectedness criterion are not explained in that local argument. Determine whether a genuinely sufficient earlier lesson exists; informal references to a domain being one piece are not automatically enough for this proof step.

**Repair:** State the elementary relative-open/relative-closed criterion, or replace the final step by a carefully explained propagation argument along a path. Keep the source's proof-sketch status honest. Do not announce that the theorem is wrong or demand a full abstract-topology chapter.

### U06 — A formal mixed-partial calculation is written as an exterior derivative outside its stated domain

**Priority/class:** P2; G/H, scope clarification.

**Definition:** Section 17.2, `c17s2-def-exterior-derivative-plane-1-form`, defines d on 1-forms with C1 coefficients.

**Use:** Section 17.4, `c17s4-ex-c2-hypothesis`, computes for

`g(x,y)=xy(x^2-y^2)/(x^2+y^2)` off the origin, with g(0,0)=0,

that `g_xy(0,0)=-1` and `g_yx(0,0)=1`, and writes a displayed `d(dg)=2 dx wedge dy` there. The paragraph already says it is trying to run the formula outside the hypotheses. Nevertheless the display uses the same operator notation as the defined C1 theory.

**Repair:** Retain the diagnostic calculation, but display the formal coefficient `g_yx(0,0)-g_xy(0,0)=2` and explicitly state that dg is not a C1 form near the origin. Therefore the book's classical exterior derivative of dg is not defined there. Do not call this a counterexample to d squared equals zero in the previously defined calculus. Do not introduce distributional forms as an incidental repair.

This is a type/domain issue, not a claim that the underlying mixed-partial calculation is incorrect.

### U07 — The Hessian preview still contains unexplained derivative subscripts

**Priority/class:** P3; C, not a demonstrated required dependency.

**Location:** Section 3.6, `c3s6-subsec-hessian-preview`.

The explicitly labeled preview displays a matrix containing `f_xx`, `f_xy`, `f_yx`, and `f_yy`, before their later calculus development. Because it is expressly a preview, do not count it as a hard prerequisite defect unless a required downstream task relies on it.

**Suggested refinement:** Keep the quadratic-form geometry and a generic symmetric matrix H; say in words that later second derivatives produce this matrix. Put the derivative-entry formula in Chapter 9. This preserves the motivation without requiring students to decode four new symbols in Chapter 3.

## 9. Protected current material and false positives

Explicitly record important nonissues in the audit:

- Section 5.2's frozen-parameter curve derivatives have an available one-variable vector-derivative foundation. Its broader tangent-plane justification is explicitly deferred. Do not remove the author-directed lesson because it precedes Chapter 7.
- The current Section 3.4 has an independent determinant-product argument using alternating multilinearity and a permutation definition. Re-audit it, but do not repeat the old circularity finding without checking this new proof.
- Section 2.7's two-covector wedge definition is a legitimate algebraic early introduction. It does not need to wait until Chapter 16.
- A gradient can be introduced before a chapter titled “Gradient and Optimization”; inspect the actual earlier definition and proof.
- The Hodge-star mention in the Maxwell gateway explicitly says it is not needed there. That is an appropriate optional future topic unless a hidden assessment depends on it.
- A supplied classical theorem can be used before its full proof. The audit should enforce accurate hypotheses and proof status, not automatically require full proofs of every standard theorem.

For every rejected candidate, give the exact earlier/local support or the precise reason it is a harmless preview. “Probably standard” is not a disposition.

## 10. Repair planning principles

Choose the least disruptive correct repair that preserves the learning objective:

1. Move a checkpoint after its actual support.
2. Replace unsupported notation with an already taught description.
3. Add a short local definition or rule when the idea is genuinely needed now.
4. Insert a reusable elementary lemma when several proofs need the same missing principle.
5. Move optional advanced material to its natural later treatment and merge duplicates.
6. Supply a precise theorem for current use with an honest proof status when proving it now would distort the course.
7. Rewrite the exercise so it uses available tools, preserving depth and interest.
8. Correct a hypothesis, type, or quantifier and inspect downstream uses.

Do not solve an audit by moving all definitions to the beginning. Do not remove interesting examples merely to reduce the count of unfamiliar words. Do not mark required material optional while leaving later required dependencies on it.

Every proposed change must include its downstream impact: reviews, hints, solutions, captions, visible graphics, references, chapter introductions, and old audit dispositions. Preserve stable XML IDs when their semantic object is retained; when material moves, track its new location. Do not leave a valid ID attached to an unrelated replacement merely to avoid a broken-link warning.

For U01/U02, prefer connecting existing ideas over expanding the curriculum: an integration argument should rest on Fubini/polar substitution, and an optional triple-wedge comparison should not force a new theory before it is needed.

## 11. Automation: triage, not certification

A scanner may help produce candidates. It must not declare that the book is logically ordered.

Useful checks include:

- active inclusion order and section counts;
- duplicate and unresolved XML IDs;
- references to later targets;
- occurrences of derivative notation, wedge/pullback/exterior-derivative notation, and unfamiliar operator names;
- uses of “uniformly,” “compact,” “subsequence,” “connected,” “same argument,” and “as shown”;
- exercise positions relative to local definitions;
- optional-to-required reference edges;
- suspicious jumps from 2D to nD or from smooth to merely differentiable;
- old IDs in relocated material and remaining source-graphic labels.

Do not label all forward references as errors. Do not use absence of literal keywords to prove absence of an equivalent earlier explanation. Do not mistake comments or macro definitions for student instruction.

If writing a scanner, test it on at least these fixtures:

1. A defined-before-use concept: no defect.
2. An example that sufficiently introduces a concept before the named definition: no automatic defect.
3. A required exercise before its rule: candidate defect.
4. A clearly optional preview unused later: protected.
5. An optional preview used by required homework: candidate leak.
6. A supplied theorem with a genuine later independent proof: no automatic defect.
7. A proof cycle among deferred results: report the cycle.
8. A coordinate 3-form followed by an arbitrary three-covector manipulation: distinguish the capabilities.
9. A symbol defined only in a hidden solution or macro: not earlier support.
10. A prerequisite visible only in a graphic label: include it.
11. A file whose lexical name disagrees with XInclude order: use the inclusion order.
12. A missing source fragment: report incomplete coverage rather than silently passing it.

## 12. Audit deliverables

Write the new campaign's artifacts in a separate audit directory, for example `audit/logical-order-round2/`, without overwriting the previous reports as though their review history had not happened.

### A. `scope-and-coverage.md` with `coverage.json`

Record actual snapshot, entry contract, active inclusion count, included/excluded resources, tool limitations, and per-section review states. Distinguish:

- inventoried;
- mechanically scanned;
- semantically read;
- prerequisite support verified;
- required-task dependency witnesses completed;
- independent challenge completed;
- source-graphic versus rendered-graphic review;
- unresolved or blocked.

A file being read does not mean every supporting dependency was verified. A parse/build pass is not a logical pass.

### B. `concept-ledger.json` and `dependency-graphs.json`

Record the capability-level availability evidence and the separate learning/proof graphs. Keep references machine-resolvable to the snapshot and XML IDs. Record supplied theorem roots and unresolved supports explicitly.

### C. `findings.md`

Each finding needs:

- unique ID, category, priority, confidence/evidence status;
- exact source location and a short faithful excerpt;
- the capability/inference required;
- what the student has actually been taught at that point;
- the earlier support found, or the later support and search needed to establish the gap;
- an explanation distinguishing missing preparation from mathematical falsity;
- a solution/dependency witness for affected tasks;
- minimal proposed repair and downstream impact;
- verification criteria;
- relation to earlier findings: new, residual, recurrence, introduced by a prior repair, or already resolved.

Group occurrences by root cause. Do not inflate the defect count by counting every occurrence of one missing supporting lemma as an independent conceptual failure.

### D. `exercise-checks.md`

Record required-task dependency witnesses and fully checked high-risk solutions. Mark unresolved tasks honestly. Separate lack of prerequisite support from legitimate difficulty.

### E. `proof-status-and-nonissues.md`

Track supplied theorems, promised proof destinations, limited proof sketches, and rejected false positives. This protects the book against overcorrection.

### F. `repair-plan.md`

Order repairs by dependency and instructional impact. Give file/ID-level instructions, not “clarify prerequisites throughout.” Specify content to retain, move, replace, or introduce; provide small model passages when needed. Make author-level structural decisions explicit.

### G. `validation.md`

Record the commands actually run, results, warnings, rendered pages inspected, and remaining limitations. In audit-only mode, distinguish baseline structural validation from a post-repair validation that has not been performed.

## 13. Validation and completion conditions

Use the repository's actual toolchain and configuration rather than assuming a CLI version or target name. Read `project.ptx`, requirements, and repository instructions before choosing build commands. Appropriate checks typically include XML/XInclude parsing, reference/ID validation, and the configured PreTeXt web build. Regenerate and inspect affected graphics only when implementation is authorized.

Do not edit generated HTML, generated LaTeX, or output assets by hand to hide a source problem. Report unrelated baseline warnings separately from new warnings.

A **full audit** can be reported complete only when:

1. Every active section and wrapper is accounted for at the recorded snapshot.
2. All required student-facing content has received semantic reading, not only token scanning.
3. Every required task has a dependency witness or is explicitly recorded as unresolved.
4. Every claimed-supported dependency has a sufficient earlier/local/declared source.
5. Deferred proof references and supplied-theorem boundaries have been checked.
6. Root-cause findings and proposed repairs include downstream consequences.
7. Both defects and important nonissues have been challenged.
8. Missing files, unavailable graphics, unresolved supports, and unreviewed items remain visible.
9. The summary distinguishes an audit of learning order from a full mathematical correctness certification.

If any condition is unmet, deliver the actual completed work and a precise remaining-coverage ledger. Do not relabel a targeted pass “194/194 verified” because an older report used that count.

## 14. Final report to the author

Lead with the actual outcome: what new required-use gaps were established, what old problems are now resolved, and what remains uncertain. Give counts of root causes and affected occurrences separately. Distinguish high-priority corrections from optional preview improvements.

Include the inspected commit, coverage status, the most consequential examples, the recommended repair order, and a clear statement of what was not changed or verified. Estimate uncertainty subjectively and label it as such; do not present numerical confidence as a mathematical certification.

Do not end with a vague claim that everything is now logically consistent. Support the conclusion with the coverage and dependency evidence.

## 15. Source map for the seed findings

All following paths are pinned to `9a9d110af839b539fe598de66ecc4320a4126af4` for this brief. Stable XML IDs above identify the passages more reliably than rendered subsection numbers.

Use the permalink prefix:

`https://github.com/kirill57/MVC-pretext/blob/9a9d110af839b539fe598de66ecc4320a4126af4/`

| Source | Path | Role |
|---|---|---|
| S01 | `source/frontmatter.ptx` | Actual entry prerequisites and treatment of previews/deferred proofs |
| S02 | `PREREQUISITE_COVERAGE.md` | Previous review's 194-section scope and its own limitations |
| S03 | `source/chapters/ch05-vector-valued-functions/sections/sec-5-derivatives-and-integrals-of-vector-valued-functions.xml` | Author-directed current Section 5.2 surface-grid lesson |
| S04 | `source/chapters/ch02-vector-products/sections/sec-2-alternating-products-a-first-glimpse-of-forms.xml` | Earlier coordinate volume form and two-covector algebra |
| S05 | `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml` | Early triple-wedge manipulation and cylindrical integration transition |
| S06 | `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml` | Spherical volume factor, forms comparison, and exact integral uses |
| S07 | `source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml` | Later general three-covector determinant evaluation |
| S08 | `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml` | Finite-cover step in parameter-integral lemma |
| S09 | `source/chapters/ch17-exterior-derivatives/sections/sec-17-closed-and-exact-forms.xml` | Subsequence theorem used in the homotopy-grid proof |
| S10 | `source/chapters/ch19-conservation-laws/sections/sec-19-potential-theory-and-harmonic-functions.xml` | Relative-open/closed step in maximum-principle proof idea |
| S11 | `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-exterior-derivative-of-a-1-form.xml` | C1 domain of the defined exterior derivative |
| S12 | `source/chapters/ch17-exterior-derivatives/sections/sec-17-the-rule-d-squared-equals-zero.xml` | Formal mixed-partial calculation outside that domain |
| S13 | `source/chapters/ch03-linear-functions-matrices/sections/sec-3-quadratic-forms-and-symmetric-matrices.xml` | Explicitly optional Hessian-symbol preview |
| S14 | `source/chapters/ch03-linear-functions-matrices/sections/sec-3-determinants-of-linear-transformations.xml` | Current independent determinant-product proof; protected against stale findings |
| S15 | `source/chapters/ch19-conservation-laws/sections/sec-19-maxwell-s-equations-as-a-forms-gateway.xml` | Explicitly optional Hodge-star mention |

This brief does not establish that no additional earlier explanation exists under different terminology. U03–U05 especially require the full audit's negative-search and source-reading checks before definitive book-wide absence claims are made.
