# Prerequisite relocation and ID map

All194 section root IDs and the recursive include order are preserved, including Chapter5's curvature, Frenet, special-coordinates and review sequence. Old mathematical objects keep their IDs when moved. Removed wrapper/table IDs are documented below; no empty anchors were created. The final structural checker reports no duplicate IDs or unresolved references. The final HTML build also checks unnumbered cross-reference text.

## Surface content

| Old ID/content | Old location | Final location | Semantic treatment |
|---|---|---|---|
| `c4s5-ex-tangent-directions-cylinder` | 4.5 | 15.1; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml:129` | Same example ID; replaces duplicate unnumbered cylinder tangent calculation. |
| `c4s5-fig-cylinder-tangent-directions` | 4.5 | 15.1; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml:200` | Same source figure/code ID, after cross-product calculation; new alt text and scaling caption; regenerated. |
| `checkpoint-4-5-two-tangents-and-cross-product` | 4.5 | 15.1; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml:286` | Same task ID, now after regularity definition; corrected hint to tangent plane. |
| `c4s5-def-regular-point` | 4.5 | 15.1; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml:272` | Substantive legacy paragraph within existing c15s1-def-smooth-regular-surface-patch; no competing definition. |
| `c4s5-ex-regularity-cone-tip` | 4.5 | 15.1; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-parametric-surfaces-and-tangent-planes.xml:471` | Same example ID; merges duplicate cone discussion, adds actual no-plane proof. |
| `c4s5-def-orientation-informal` | 4.5 | 15.3; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-oriented-surfaces-and-flux.xml:101` | Substantive paragraph within existing orientation definition, after normals are taught. |
| `checkpoint-4-5-choosing-an-orientation` | 4.5 | 15.3; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-oriented-surfaces-and-flux.xml:119` | Same ID, after orientation definition and Mobius discussion. |
| `c4s6-ex-d6` | 4.6 | 15.3; `source/chapters/ch15-surfaces-flux-curl-divergence/sections/sec-15-oriented-surfaces-and-flux.xml:396` | Same cross-product practice ID; Chapter4 replacement has new ID c4s6-ex-cylinder-seam-grid. |
| `c4s5-subsec-tangent-directions` |4.5|15.1 existing coordinate-curve/normal subsections|Retired wrapper ID with no inbound source references; substantive example, figure, definition and checkpoint IDs preserved. |
| `c4s5-subsec-orientation-preview` |4.5|15.3 orientation/flux;15.4 order-sign explanation|Retired wrapper ID with no inbound source references; substantive orientation ID and checkpoint preserved; faulty vector wedge/sign claim removed. |
| New geometry checkpoints |4.5|4.5|New IDs c4s5-ex-cylinder-point-domain, c4s5-ex-saddle-grid, c4s5-ex-sphere-check-seams, c4s5-ex-same-cylinder-different-repetitions; all have hints/solutions. |
| `c4s5-fig-cylinder-from-rectangle` |4.5|4.5|Original source/ID retained; geometry-only visible labels retained. |

## Early checkpoints and determinant notation

| Original ID/block | Final destination/treatment | Semantic status and inbound-reference check |
|---|---|---|
| checkpoint-2-7-alternating-forces-zero | Same early2.7 location, statement now B(v,v)=0 | Preserves alternating-forces-zero reasoning; removes wedge before its definition. |
| checkpoint-2-7-wedge-not-multiplication | Moved within2.7 after c2s7-def-wedge-linear-measurements and derived rules | Same substantive distinction between alternating covector wedge and multiplication. |
| checkpoint-2-7-why-alternating-for-integration | Same2.7 checkpoint ID; concrete ordered-pair area reversal | Retains substantive orientation/alternation question; no integration theory demanded. |
| c3s4-subsec-change-of-variables | Retained3.4 finite signed/ordinary rectangle scaling | Root section and subsection IDs stable; differential calculation merged into12.5 by middle agent. |
| c3s4-tab-ordinary-vs-oriented-area | Merged semantically into c12s5-tab-orientation-vs-absolute-value | Original table removed, no empty anchor. Repository search found no inbound references to old table;12.5 table already distinguishes same two objects. |
| c3s4-thm-volume-scaling-space / c3s4-thm-determinant-product | Retained3.4; proofs replaced/strengthened | Same theorems, preserved arbitrary-n multiplicativity scope; no anchor reassignment. |
| checkpoint-7-2-gradient-dot-product | Moved after c7s2-thm-gradient-formula proof | Same required gradient calculation, now hypotheses and definition available. |
| c7s5-parametrized-surface | Existing7.5 example retained and preceded by explicit surface-partial bridge | New bridge replaces dependency on removed4.5 calculus; systematic destination15 handled by root. |
| c3s7-fig-input-square-output-parallelogram | Same3.7 figure, source labels unit input directions / images under derivative | Same mathematical figure; prose scales actual tiny input edges by epsilon. Root regeneration and render check required. |
| c7s5-fig-rubber-sheet | Same7.5 figure, labels Delta x F_x(P), Delta y F_y(P) | Same figure; corrected arrows denote increments, not unscaled columns. Root regeneration and render check required. |
| ex-c2s8-polar-area-element | Same active2.9 review; finite annular-sector area difference | Retains substantive polar radial/angular area factor, uses new finite explanation rather than dA substitution. |
| c5s6-rev-15 | Same active5.7 review; single-variable swept-area circle integral | Retains substantive circle swept-area computation, removes unsupported integral-of-form notation. Existing c5s6 ID numbering preserved although active section is5.7. |

No section root ID or owned chapter include order changed. No old calculus ID was attached to an unrelated replacement. All newly supplied definitions/corollaries have unique IDs and no empty anchors. Root structural checker verifies global uniqueness/references after all workers finish.

## Integration destinations and local reorderings

No chapter reordering or external publication. No original LaTeX files changed.

| Finding | Source | Destination | Destination/source evidence | Disposition | ID/xref handling |
| --- | --- | --- | --- | --- | --- |
| A06 | 3.4 c3s4-subsec-change-of-variables derivative expansion | 12.5 c12s5-linear-differential-scaling | source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:190–199 | Merged linear specialization into existing general differential calculation; original3.4 subsection keeps finite geometry. | Backward reference uses text="title" because source subsection is unnumbered. |
| A06 table | c3s4-tab-ordinary-vs-oriented-area | c12s5-tab-orientation-vs-absolute-value | source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:395–424 | Semantics merged into existing table, avoiding duplicate expositions. | Early owner found zero inbound refs to removed table ID; destination ID preserved. |
| M11 | 11.2 checkpoint-11-2-slice-drops-a-dimension before definition | Same section, after c11s2-thm-triple-integral-z-simple | source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:172–190 | Generic formula question follows local theorem; parallel vertical-fiber language corrected. | Same ID retained; no external references changed. |
| M22a | 14.3 checkpoint-14-3-zero-div-meaning before definition | After c14s3-def-divergence-plane | source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-flux-form.xml:187–204 | Definition before generic checkpoint. | Same ID retained. |
| M22b | 14.3 checkpoint-14-3-same-theorem before theorem | After c14s3-thm-green-flux-form | source/chapters/ch14-greens-theorem/sections/sec-14-green-s-theorem-flux-form.xml:277–294 | Two theorem statements precede requested comparison. | Same ID retained. |
| A12 endpoint | 13.6 broad deferred proof | c17s5-thm-simply-connected-potential | source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:425–444 | Precise later theorem referenced; local parameter lemma introduced before rectangle proof. | Endpoint implemented and independently reviewed; no circular dependence on Green/Stokes. |
| M20 endpoint | 13.8 shoelace used as known | c14s7-ex-shoelace | source/chapters/ch14-greens-theorem/sections/sec-14-chapter-review-and-applications.xml:143–186 | 13.8 formula now declared preview;14.7 supplies actual Green-based proof. | All existing project and example IDs retained. |

## Later proof endpoints and stable anchors

No existing section or exercise was moved or renumbered in chapters16-20 or appendicesA-G. All existing section IDs and include order are retained. No original multivariable_calculus file was edited.

New local proof anchors:

- c17s5-thm-simply-connected-potential: full deferred13.6 potential theorem endpoint, inserted within existing17.5.
- c18s5-pullback-derivative-justification: independent C2 coordinate proof of pullback/exterior derivative compatibility, inserted within existing18.5; referenced with custom text to avoid an unnumbered-target xref error.
- c19s4-local-magnetic-potential: explicit local box vector-potential construction, inserted within existing19.4.

Former17 chapter conclusion title changed to ordinary emphasized paragraph, retaining its prose purpose. The cone project retains c18s10-ex-cap3-cone and is corrected by truncation rather than moved. The writing project retains its IDs and replaces unsupported vector-wedge equality by the already-defined covector-form evaluation. All appendix/reference formula corrections remain in their original sections.

