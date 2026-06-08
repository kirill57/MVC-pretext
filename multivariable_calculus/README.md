# Multivariable Calculus: From Vectors to Differential Forms

LaTeX source for the textbook *Multivariable Calculus: From Vectors to Differential Forms*.

This is a **stub** — directory layout, preamble, theorem environments, and per-chapter section/subsection scaffolding only. No content yet.

## Quick start (Overleaf)

1. Zip the entire project folder.
2. In Overleaf: **New Project → Upload Project**, select the zip.
3. Set the main document to `main.tex` (Overleaf usually detects this automatically).
4. Compile with **pdfLaTeX**.

## Quick start (local)

```bash
pdflatex main
pdflatex main      # second pass for ToC and refs
```

## Directory layout

```
multivariable-calculus/
├── main.tex                root file: \part headers, \include directives
├── preamble.tex            packages, theorem environments, hyperref/cleveref
├── macros.tex              math shorthands (\R, \pd, \norm, \dform, ...)
├── frontmatter/
│   ├── preface.tex
│   └── howto.tex           tag legend + suggested course paths
├── chapters/               20 chapter stub files, ch01-...-ch20-...
├── appendices/             7 appendix stub files, appA-...-appG-...
├── backmatter/
│   └── unifying-themes.tex
├── figures/                drop graphics here; \graphicspath is already set
├── references.bib          empty BibTeX file (uncomment \bibliography in main.tex)
├── .gitignore
└── README.md
```

## How section tags are recorded

Every section in the TOC carries one or more tags (Core, Bridge, Forms, Optional, Counterexample, Project). These appear as a comment line directly above the corresponding `\section{...}`:

```latex
%% --- 7.6  [Counterexample] ---
\section{Sufficient conditions and warning examples}
\label{sec:7.6}
```

This keeps the tags visible to anyone editing the source without changing how anything renders. If you later want them to show in the margin or in the ToC, define a `\sectiontag{...}` macro in `macros.tex` and grep-replace the comment lines.

## Theorem environments available

Numbered together within each chapter (so cross-references read 7.2.1, 7.2.2, ...):

- `theorem`, `proposition`, `lemma`, `corollary`
- `definition`, `example`, `counterexample`
- `remark`, `warning`

Unnumbered narrative environments (used by this book's pedagogy):

- `recall` — explicit callback to earlier material at the start of a section
- `hook` (renders as **Looking ahead**) — end-of-section forward pointer

Customize the styling in `preamble.tex`.

## Adding a new chapter

1. Create `chapters/chNN-slug.tex` following the pattern of any existing chapter.
2. Add an `\input{chapters/chNN-slug}` line to `main.tex` under the appropriate `\part{}`.

## Adding a figure

Drop the file in `figures/` and reference it as `\includegraphics{filename}` — no path needed; `\graphicspath` is set in `preamble.tex`.

## Regenerating from the TOC

`build_stubs.py` (one level up from this directory in the build environment) parses the source TOC and overwrites `chapters/` and `appendices/`. **Do not run it after you've started writing content** — it will overwrite the files. Keep it only as a record of how the stubs were generated.
