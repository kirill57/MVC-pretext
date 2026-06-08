# Conversion Agent — Operating Instructions

You convert *Multi-Variable Calculus* from LaTeX to PreTeXt, **one section at a time**.
Read `CONVERSION-PLAN.md` first (scope, figure policy, element-mapping table). This file is
the loop you repeat for every section. Work in small, verified increments — never batch many
sections before building.

## Inputs and outputs
- **Source of truth (read-only):** `multivariable_calculus/chapters/<chXX>.tex` and
  `multivariable_calculus/appendices/<appX>.tex`. Never edit these.
- **Target (you edit):** `source/chapters/<chXX-slug>/sections/sec-<n>-<slug>.xml`
  (stub already exists with the correct `<title>` and `xml:id`).
- **Reference template:** `source/chapters/ch01-points-vectors-space/sections/sec-1-why-multivariable-calculus-begins-with-geometry.xml` (a fully converted section — imitate its style).

## Per-section loop

1. **Locate.** Find the section in the source `.tex` (the stub's comment names the source file).
   Read the whole section, including every `\subsection`, environment, and figure, before writing.

2. **Convert the prose & math.** Replace the stub body. Map elements per the table in
   `CONVERSION-PLAN.md §5`. Key rules:
   - Each prose paragraph → one `<p>`.
   - Inline math `\(..\)` → `<m>..</m>`; display `\[..\]` → `<md>..</md>` (NOT `<me>` — deprecated).
   - Multi-line `align`/`aligned` → `<md>` with one `<mrow>` per line, `&` → `\amp`.
   - Theorems/definitions/examples → their PreTeXt elements **with a `<statement>` wrapper**;
     proofs become a sibling `<proof>`. Example/counterexample titles come from the `[...]` arg.
   - Use the predefined macros (e.g. `\norm{v}`, `\pd{f}{x}`, `\grad`) verbatim inside math.
   - Word/number tables (`array`/`tabular`) → `<table><title/><tabular>` (see POC).
   - `\label` → `xml:id`; `\ref`/`\cref`/`\eqref` → `<xref ref="..."/>`.

3. **Convert each figure** following `CONVERSION-PLAN.md §4`:
   - Decide latex-image (2-D TikZ) vs Asymptote (3-D / complex pgfplots) vs raster (`<image source>`).
   - **Structure: `figure → image → latex-image|asymptote`.** Never put `latex-image` directly in `figure`.
   - Escape `< > &` as `&lt; &gt; &amp;` inside the graphics code (e.g. `->` → `-&gt;`).
   - Give the `<figure>` a stable `xml:id="fig-..."` and move the `\caption{}` into `<caption>`.
   - For Asymptote redraws, use the `asymptote-drawing` skill.

4. **Remove the TODO marker** and set the status comment to `CONVERTED`.

5. **Validate XML:**
   ```
   xmllint --noout --xinclude source/main.ptx
   ```
   Must be clean. Fix any well-formedness/xinclude error before building.

6. **Build:**
   ```
   pretext build web
   ```
   Must finish with **no errors and no deprecation warnings**. (Deprecation warnings usually
   mean a stray `<me>`/`<men>` — switch to `<md>`/`<mdn>`.)

7. **Generate & inspect figures** (only if the section has figures):
   ```
   pretext generate latex-image   # and/or: pretext generate asy
   pretext view web
   ```
   Open the section page. For **each** figure, compare the rendered SVG
   (`generated-assets/latex-image/<fig-id>-N.svg`) against the original LaTeX PDF.
   If a figure "succeeds" but no SVG appears, delete `.cache/` and regenerate.
   Fix labels/arrows/clipping until the figure matches.

8. **Mark done** only when the §7 "Definition of done" checklist in `CONVERSION-PLAN.md` is fully met.
   Commit with a message like `convert: chXX §N <slug>`.

## Hard rules
- One section per loop. Build green before moving on.
- Never edit `multivariable_calculus/`.
- Never trust Pandoc output for math, environments, or figures — hand-correct everything.
- If unsure how an environment maps, check the POC section and the table in `CONVERSION-PLAN.md`;
  if still unsure, flag it in the section as an XML comment `<!-- REVIEW: ... -->` rather than guessing.
- Keep `xml:id`s unique and non-numeric-initial.

## Quick reference — commands
```
xmllint --noout --xinclude source/main.ptx   # validate whole book
pretext build web                              # build HTML
pretext generate latex-image                   # render TikZ/pgfplots figures
pretext generate asy                           # render Asymptote figures
pretext view web                               # serve + open (PreTeXt-View)
pretext build pdf                              # (periodic) full LaTeX/PDF build
```
