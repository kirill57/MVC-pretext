# LaTeX → PreTeXt Conversion Plan
**Book:** *Multi-Variable Calculus: From Vectors to Differential Forms* (Cyrill Oseledets)

This document is the master plan. The companion file **`CONVERSION-AGENT.md`** is the
per-section operating checklist the code agent follows. Read both before starting.

---

## 1. Scope

| Item | Count |
|---|---|
| Parts | 6 |
| Chapters | 20 |
| Appendices | 7 (A–G) |
| Sections (chapters + appendices) | 192 |
| Subsections | ~770 |
| LaTeX source lines | ~85,000 |
| `tikzpicture` figures | 177 |
| `pgfplots` (`axis`) figures | 20 |
| Raster images (`.png`) | 1 (`Spherical_Volume.png`) |

LaTeX source of record: `multivariable_calculus/` (do **not** edit it; it is the input).
PreTeXt output: `source/` (this is what we build and ship).

---

## 2. What is already done (do not redo)

1. **Full empty skeleton** generated and committed under `source/`:
   - `source/main.ptx` — `<book>` with 6 `<part>`s, all 20 chapters, frontmatter/backmatter.
   - `source/docinfo.ptx` — all math macros translated from `macros.tex`; `latex-image-preamble` mirroring the LaTeX preamble (tikz, tikz-3dplot, pgfplots + libraries).
   - `source/frontmatter.ptx`, `source/backmatter.ptx` (backmatter `xi:include`s the 7 appendices).
   - `source/chapters/<chXX-slug>/<chXX-slug>.ptx` — 20 chapter wrappers, each `xi:include`-ing its sections.
   - `source/chapters/<chXX-slug>/sections/sec-<n>-<slug>.xml` — 192 section **stubs** (correct titles, placeholder body, `TODO` marker).
   - `source/appendices/<appX-slug>/...` — same structure for appendices.
   - `publication/publication.ptx` — parts decorative, numbering to level 2, `default-modern` theme, asset dirs.
2. **Proof-of-concept section fully converted** and build-verified:
   `source/chapters/ch01-points-vectors-space/sections/sec-1-why-multivariable-calculus-begins-with-geometry.xml`
   Use it as the **reference template** for prose, display math, examples, tables, and a `latex-image` figure.
3. **Toolchain proven** in this environment: `pretext build web` + `pretext generate latex-image`
   produce HTML and render the TikZ figure to SVG correctly.

Every other section file is a stub whose body still says *"Placeholder. Content not yet converted."*

---

## 3. Toolchain (local install — chosen approach)

Install once on the Windows machine (PowerShell):

```powershell
python -m pip install --upgrade pretext      # PreTeXt CLI (2.41+)
```

You also need a **LaTeX** distribution (MiKTeX or TeX Live) and **dvisvgm** (ships with both)
for `latex-image` → SVG. For 3D Asymptote figures you need **Asymptote** (`asy`), which is
included with TeX Live or installable standalone. Verify:

```powershell
pretext --version
pdflatex --version
dvisvgm --version
asy --version
```

Core commands (run from the project root, where `project.ptx` lives):

```powershell
pretext build web            # build HTML  -> output/web/
pretext generate latex-image # render TikZ/pgfplots figures -> generated-assets/
pretext generate asy         # render Asymptote figures
pretext view web             # serve + open in browser (PreTeXt-View)
```

Notes learned during setup:
- The **devcontainer** (`pretextbook/pretext-full`) also works and bundles everything, but local
  install gives faster iteration. Either is fine; pick one and stay consistent.
- `output/`, `generated-assets/`, and `.cache/` are git-ignored build artifacts.
- If a regenerate "succeeds" but produces **no** image, the asset cache may be stale: the hash is
  stored in `.cache/.web_assets.json`. Delete `.cache/` (or that file) and regenerate.

---

## 4. Figure policy — **hybrid** (the most error-prone part; read carefully)

Decision tree for every `\begin{figure}` in the source:

1. **2-D `tikzpicture`** (no `tikz-3dplot`, no `\begin{axis}`):
   → keep the TikZ code, place it in a PreTeXt `latex-image`. Minimal edits.
2. **3-D scenes** (`tikz-3dplot`, `\tdplot...`, 3D coordinates) **or** complex `pgfplots` surfaces:
   → **rewrite in Asymptote** (`<asymptote>`), which produces far better 3-D HTML/SVG.
   Use the `asymptote-drawing` skill to generate/clean the Asymptote code.
3. **2-D `pgfplots`** (function/area plots): either keep as `latex-image` (fast) or port to
   Asymptote if the result is poor. Prefer `latex-image` unless it renders badly.
4. **Raster image** (`Spherical_Volume.png`): copy the file to `assets/images/` and reference it
   with `<image source="images/Spherical_Volume.png" width="..."/>`. No redraw.

### Mandatory figure structure (this bit caused a real bug — get it right)

A figure is **`figure` → `image` → (`latex-image` | `asymptote`)**. `latex-image` must **not**
be a direct child of `figure`. The HTML build will *silently* accept the wrong nesting but the
image will **never generate**.

```xml
<figure xml:id="fig-...">
  <caption>...</caption>
  <image width="60%">
    <latex-image>
      \begin{tikzpicture}[...]
        ...
      \end{tikzpicture}
    </latex-image>
  </image>
</figure>
```

Inside `latex-image`/`asymptote`, raw `<`, `>`, `&` are XML-illegal: write `&lt; &gt; &amp;`.
In TikZ this matters for arrow tips (`->` becomes `-&gt;`) and options like `>=stealth`
(`&gt;=stealth`). See the POC figure for a worked example.

### Figure verification is not optional
Every converted figure must be **looked at**: run `pretext build web` + `pretext view web`,
open the page, and compare the rendered SVG against the original LaTeX PDF. The generated SVG
lives at `generated-assets/latex-image/<fig-id>-N.svg`. Diagrams that compile but look wrong
(missing labels, clipped, wrong arrows) are the #1 conversion defect.

---

## 5. Element / environment mapping (LaTeX → PreTeXt)

| LaTeX | PreTeXt | Notes |
|---|---|---|
| `\section{...}` | `<section>` (one file each) | already stubbed |
| `\subsection{...}` | `<subsection>` | |
| paragraph text | `<p>...</p>` | every block of prose |
| `\(...\)` inline | `<m>...</m>` | |
| `\[...\]` display | `<md>...</md>` | **`<me>`/`<men>` are DEPRECATED** in PreTeXt ≥2026-05; use `<md>`/`<mdn>` (single line: `<md>`; numbered: `<md number="yes">`). |
| `align`/`aligned` multi-line | `<md>` with `<mrow>...</mrow>` per line, `\amp` for `&` | numbered: `<mdn>` or per-`mrow` `number="yes"` |
| `equation`+`\label` | `<md number="yes" xml:id="eq-...">` | |
| `\begin{theorem}` | `<theorem><statement>...</statement></theorem>` | proofs go in sibling `<proof>` |
| `proposition`/`lemma`/`corollary` | `<proposition>`/`<lemma>`/`<corollary>` | |
| `\begin{definition}` | `<definition><statement>...</statement></definition>` | wrap defined word in `<term>` |
| `\begin{example}` | `<example><title>..</title><statement>..</statement></example>` | title from the optional `[...]` arg |
| `\begin{counterexample}` | `<example>` with `<title>Counterexample: ...</title>` | PreTeXt has no native counterexample |
| `\begin{remark}` | `<remark>` | |
| `\begin{warning}` | `<warning>` | |
| `recall` (custom) | `<remark><title>Recall</title>...` | unnumbered narrative env |
| `hook` / "Looking ahead" (custom) | `<aside><title>Looking ahead</title>...` | end-of-section forward pointer |
| `\begin{proof}` | `<proof>` | |
| `enumerate` / `itemize` | `<ol>` / `<ul>` with `<li>` | |
| `array`/`tabular` of words+math | `<table><title/><tabular>` with `<row>`/`<cell>` | header row `header="yes" bottom="medium"`; see POC tables |
| `\emph{...}` | `<em>...</em>` (emphasis) or `<term>...</term>` (defining a term) | judge by intent |
| `\textbf{...}` | `<alert>` or `<term>` | |
| `\label{...}` | `xml:id="..."` on the element | |
| `\ref{}` / `\cref{}` / `\eqref{}` | `<xref ref="..."/>` | PreTeXt auto-generates "Theorem 7.2", etc. |
| `\footnote{...}` | `<fn>...</fn>` | |
| figure (see §4) | `<figure><caption/><image>...` | |

### Macros
All custom macros from `macros.tex` are already defined in `source/docinfo.ptx`
(`\R \Z \N \Q \Cplx \vect \zerovec \pd \pdmix \norm \abs \dform \grad \divg \curl \Hess
\Image \Kernel \spn \sgn \inner \Arg`). Use them verbatim inside `<m>/<md>`.
`\DeclareMathOperator`/`\DeclarePairedDelimiter` were re-expressed as `\newcommand`
(the only form allowed in `<macros>`).

---

## 6. Phased execution

**Phase 0 — done:** skeleton, POC section, toolchain, this plan.

**Phase 1 — front/back matter & one full chapter:** convert `preface.tex`, `howto.tex`, then
**all of Chapter 1** end-to-end (it is the smallest "real" chapter and exercises every pattern).
Build + view after each section. This shakes out remaining pattern questions cheaply.

**Phase 2 — bulk conversion, chapter by chapter (Ch 2–20, then appendices):**
For each chapter, convert section by section in order. After each section: build, validate, and
**view every figure**. Do not advance to the next chapter with a red build.

**Phase 3 — figures pass:** revisit all 3-D/pgfplots figures flagged for Asymptote; redraw and
visually verify. (Many can be batched once the prose is done.)

**Phase 4 — global polish:** cross-references (`<xref>`), index entries (`<idx>`), exercises,
numbering audit, full-book `pretext build web` + `pretext build pdf`, link check.

Suggested order favors getting a continuously-building book early: prose first (fast, high value),
hard 3-D figures batched later.

---

## 7. Definition of done (per section) — enforced by `CONVERSION-AGENT.md`

A section is "done" only when **all** hold:
1. No `TODO ... NOT STARTED` marker remains; body fully converted.
2. `xmllint --noout --xinclude source/main.ptx` is clean (well-formed + valid xincludes).
3. `pretext build web` completes with **no errors and no deprecation warnings**.
4. Every figure in the section renders to SVG and has been **visually compared** to the source PDF.
5. All `\label` → `xml:id` and all `\ref/\cref` → `<xref>` resolved (no broken references).

---

## 8. Known pitfalls (seen during setup)

- **Figure nesting** (`figure>image>latex-image`) — silent failure if wrong. See §4.
- **`<me>` is deprecated** — use `<md>`. A book-wide `me→md` is safe (inline `<m>` is unaffected).
- **XML-escaping inside `latex-image`/`asymptote`** — `< > &` → `&lt; &gt; &amp;`.
- **Stale asset cache** — delete `.cache/` if a figure won't regenerate.
- **`xml:id` uniqueness** — must be unique across the whole book and cannot start with a digit
  (section ids use the `sec-<chapnum>-<slug>` scheme already in the stubs).
- **Pandoc** (`pandoc -f latex -t ...`) can bootstrap a section's prose, but its output is rough:
  it mangles theorem environments, custom macros, and all figures. Always hand-correct; never
  trust Pandoc output for math, environments, or figures.
