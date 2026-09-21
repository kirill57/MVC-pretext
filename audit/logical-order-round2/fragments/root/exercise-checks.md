# Chapter10–13 task witnesses

Each row cites the original source task and exact source support. Worked examples and duplicate instructions remain classified separately from assessments.

## checkpoint-10-1-why-refining-converges
Source: `source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:61–78`; supported.
Boundary error lies in the shrinking strip around finitely many smooth arcs; its area tends to zero. This asks for the supplied geometric explanation, not a proof for arbitrary boundaries.
Support: `c10s1-subsec-area-as-limit-of-sums` (`source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:13–98`)

## checkpoint-10-1-why-columns-give-exact-volume
Source: `source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:239–256`; supported_at_stated_informal_level.
Bound the total discrepancy by base area times maximum cell height oscillation; continuous height on the closed bounded base makes that oscillation small. Uniformity is a proof-sketch ceiling also present in 10.2, not a claimed analysis proof.
Support: `c10s1-subsec-volume-under-a-surface` (`source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:100–180`)

## checkpoint-10-1-what-does-f-stand-for
Source: `source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:301–318`; supported.
Interpret f as amount per area, so f times cell area is an amount; sum gives area, mass or charge according to units.
Support: `c10s1-subsec-riemann-sums-over-rectangles` (`source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:182–291`)

## source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:65:1
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:65–76`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Choose a sample point (x_{ij}^*,y_{ij}^*)\in R_{ij} for each subrectangle. The corresponding Riemann sum is \boxed{ S= \sum_{i=1}^{m}\sum_{j=1}^{n} f(x_{ij}^*,y_{ij}^*)\,\Delta x_i\,\Delta y_j. }
Support: `c10s2-subsec-partitions-sample-points` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:14–130`)

## checkpoint-10-2-sample-points-stop-mattering
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:111–129`; supported_at_stated_informal_level.
Absolute difference of the sums is bounded by sum of cell oscillations times cell areas. The later supplied continuous-integrability theorem formalizes the geometric continuity explanation; no formal uniformity proof is demanded.
Support: `c10s2-subsec-partitions-sample-points` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:14–130`)

## checkpoint-10-2-what-breaks-integrability
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:145–163`; supported.
Persistent positive weighted oscillation prevents upper and lower sums meeting; a function taking 0 and 1 densely in every cell is a sufficient example, not a necessary description of every nonintegrable function.
Support: `c10s2-subsec-integrable-functions-informally` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:132–295`)

## checkpoint-10-2-why-divide-by-area
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:308–326`; supported.
A constant 7 gives 7A; divide by positive A to recover 7. A constant equivalent height h satisfies hA=integral.
Support: `c10s1-def-double-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:258–270`)

## checkpoint-10-3-roof-two-ways
Source: `source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:91–108`; supported.
Both group the same nonnegative small columns and both explicitly give 120; geometric explanation requires no general Fubini proof.
Support: `c10s3-subsec-roof-sliced-two-ways` (`source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:27–141`)

## checkpoint-10-3-inner-integral-meaning
Source: `source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:257–274`; supported.
Each inner integral adds a signed slice; Fubini for continuous functions identifies both totals.
Support: `c10s3-thm-fubini-rectangles` (`source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:217–250`)

## checkpoint-10-3-when-order-fails
Source: `source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:403–420`; supported.
The origin singularity is unbounded, so continuous-on-rectangle Fubini does not apply; the displayed antiderivatives give opposite pi/4 values.
Support: `c10s3-subsec-why-hypotheses-matter` (`source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:350–427`)

## checkpoint-10-4-inner-limits-functions
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:136–153`; supported.
For each fixed x the y endpoints track the lower and upper boundary curves; fixed endpoints would describe a rectangle rather than slanted edges.
Support: `c10s4-def-type-i-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:110–124`)

## source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:330:1
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:330–330`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Write the outer limits from the shadow of the region on the outer axis.
Support: `c10s4-subsec-drawing-the-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:316–341`)

## source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:331:1
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:331–331`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Write the inner limits from the slice.
Support: `c10s4-subsec-drawing-the-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:316–341`)

## checkpoint-10-4-redraw-when-reversing
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:418–434`; supported.
For 0<=y<=x<=1, reversed slices have x in [0,1] and y in [0,x]; simply swapping constants and functions loses the region.
Support: `c10s4-subsec-reversing-the-order` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:343–435`)

## checkpoint-10-4-why-split
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:452–467`; supported.
A disconnected slice needs separate intervals; a single lower-upper pair would fill its gap. The hint supplies the diagnostic before the worked islands calculation.
Support: `c10s4-subsec-region-must-be-split` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:437–489`)

## checkpoint-10-5-extra-r-factor
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:172–189`; supported.
Arc length is r times angular width and radial thickness is Delta r; multiply to obtain r Delta r Delta theta.
Support: `c10s5-subsec-why-area-element` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:74–190`)

## checkpoint-10-5-cell-size-varies
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:220–238`; supported.
For fixed radial/angular spans the rays separate in proportion to radius; exact sector difference also increases with r.
Support: `c10s5-subsec-why-area-element` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:74–190`)

## checkpoint-10-5-why-symmetry-helps
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:376–393`; supported.
F(r)r is independent of theta, whose full-circle integral multiplies by 2pi.
Support: `c10s5-subsec-radial-symmetry` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:349–416`)

## source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:580:1
Source: `source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:580–580`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Check that the polar description covers the region once.
Support: `c10s5-subsec-main-lesson` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:553–596`)

## checkpoint-10-6-com-weighted-average
Source: `source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:101–118`; supported.
Sum position times small mass, then divide by total mass. Equal geometric weights would ignore the heavier side; the displayed prompt already gives the relevant numerator.
Support: `c10s6-subsec-center-of-mass` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:82–227`)

## checkpoint-10-6-inertia-r-squared
Source: `source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:242–260`; supported.
The supplied r-squared weighting quadruples when r doubles. The optional hint supplies speed r omega and squared-speed kinetic energy as physical explanation, so prior mechanics is not required for the numerical answer.
Support: `c10s6-subsec-moment-of-inertia` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:229–319`)

## checkpoint-10-6-same-integral-many-meanings
Source: `source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:478–496`; supported.
Each f Delta A is a local amount; addition is identical while units and normalization determine interpretation.
Support: `c10s6-def-mass-lamina` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:48–61`), `c10s6-def-probability-density` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:376–389`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## checkpoint-10-7-meaning-of-convergence
Source: `source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:62–79`; supported.
First integrate on radius-A disks, then let A tend to infinity; convergence means finite limiting totals.
Support: `c10s7-subsec-unbounded-regions` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:20–195`)

## checkpoint-10-7-why-comparison-works
Source: `source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:312–329`; supported_at_stated_informal_level.
For integrable truncations the running totals are increasing and bounded by 3pi, hence have a finite limit. The following supplied comparison theorem states the needed truncation-integrability condition.
Support: `c10s7-subsec-convergence-comparison` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:286–424`)

## checkpoint-10-7-why-polar-cracks-gaussian
Source: `source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:480–497`; supported.
The polar factor r makes u=r squared have du=2r dr; finite square/disk squeeze has already justified the double-integral route.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`)

## c10s8-worked-review-example-drawing-the-region
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:141–182`; worked example; supported.
x ranges0..2; y ranges x^2..2x; integral of y is32/15.
Support: `c10s4-subsec-drawing-the-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:316–341`)

## c10s8-worked-review-example-sprinkler
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:184–217`; worked example; supported.
Integral 2pi integral0..2 (10-r)r dr=104pi/3; divide by4pi gives26/3.
Support: `c10s5-thm-double-integrals-polar` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:283–300`)

## c10s8-ex-cc-01
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:222–230`; supported.
Positive area element, represented in sums by small cell area.
Support: `c10s1-def-double-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:258–270`)

## c10s8-ex-cc-02
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:232–240`; supported.
Each cell contributes 1 times its area; summing gives area.
Support: `c10s1-subsec-area-as-limit-of-sums` (`source/chapters/ch10-double-integrals/sections/sec-10-from-area-to-volume-by-slicing.xml:13–98`)

## c10s8-ex-cc-03
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:242–246`; supported.
Signed cross-sectional integral at a frozen outer coordinate.
Support: `c10s3-def-iterated-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:164–183`)

## c10s8-ex-cc-04
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:248–252`; supported.
The new slices have different endpoints; describe the same set before writing limits.
Support: `c10s4-subsec-reversing-the-order` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:343–435`)

## c10s8-ex-cc-05
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:254–258`; supported.
State x interval with y between two x-dependent graphs versus y interval with x between two y-dependent graphs.
Support: `c10s4-def-type-i-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:110–124`), `c10s4-def-type-ii-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:246–260`)

## c10s8-ex-cc-06
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:260–269`; supported.
Radial thickness times arc length r Delta theta.
Support: `c10s5-subsec-why-area-element` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:74–190`)

## c10s8-ex-cc-07
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:271–275`; supported.
Circular boundaries or radial integrands simplify under x=r cos theta,y=r sin theta.
Support: `c10s5-subsec-radial-symmetry` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:349–416`), `c10s5-subsec-shifted-circle` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:418–498`)

## c10s8-ex-cc-08
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:277–281`; supported.
M=integral rho dA.
Support: `c10s6-def-mass-lamina` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:48–61`)

## c10s8-ex-cc-09
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:283–291`; supported.
Distance to y-axis is measured by x and distance to x-axis by y, with signed moments.
Support: `c10s6-def-moments-center-mass` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:198–213`)

## c10s8-ex-cc-10
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:293–297`; supported.
The constant value producing the same total over the same positive area.
Support: `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c10s8-ex-cc-11
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:299–306`; supported.
1/r on the unit disk has integral 2pi; shrinking ring area offsets its growth.
Support: `c10s7-subsec-unbounded-functions` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:197–284`)

## c10s8-ex-cc-12
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:308–312`; supported.
1/(1+r squared) tends to zero but ring-weighted radial integral grows logarithmically.
Support: `c10s7-ex-decay-too-slow` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:167–187`)

## c10s8-ex-cc-13
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:314–318`; supported.
Nonnegativity, ordered bounds, integrability on bounded nonsingular truncations, and convergence/divergence of the comparison function.
Support: `c10s7-thm-comparison-test` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:331–372`)

## c10s8-ex-sk-01
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:324–331`; supported.
Integrate y first: 2x+4; then x from 0 to3 gives 21.
Support: `c10s3-thm-fubini-rectangles` (`source/chapters/ch10-double-integrals/sections/sec-10-iterated-integrals-and-fubini-s-theorem.xml:217–250`)

## c10s8-ex-sk-02
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:333–340`; supported.
Inner result x cubed+x squared/2; integrate 0 to1 to get 5/12.
Support: `c10s4-thm-type-i` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:190–218`)

## c10s8-ex-sk-03
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:342–352`; supported.
x:0..4,y:0..x/2 or y:0..2,x:2y..4.
Support: `c10s4-def-type-i-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:110–124`), `c10s4-def-type-ii-region` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:246–260`)

## c10s8-ex-sk-04
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:354–363`; supported.
x:-2..2,y:x squared..4; integral x squared(4-x squared) dx=128/15.
Support: `c10s4-thm-type-i` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:190–218`)

## c10s8-ex-sk-05
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:365–372`; supported.
x:0..1, y:0..x.
Support: `c10s4-subsec-reversing-the-order` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:343–435`)

## c10s8-ex-sk-06
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:374–381`; supported.
x:0..2, y:0..x squared.
Support: `c10s4-subsec-reversing-the-order` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:343–435`)

## c10s8-ex-sk-07
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:383–393`; supported.
Integrate r over r:0..3,theta:0..pi gives9pi/2.
Support: `c10s5-thm-double-integrals-polar` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:283–300`)

## c10s8-ex-sk-08
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:395–404`; supported.
Integrate r cubed over r:0..2 and full angle gives8pi.
Support: `c10s5-thm-double-integrals-polar` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:283–300`)

## c10s8-ex-sk-09
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:406–415`; supported.
2pi integral r/(1+r squared) dr from1 to3=pi log5.
Support: `c10s5-thm-double-integrals-polar` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:283–300`)

## c10s8-ex-sk-10
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:417–427`; supported.
3 integral(1+x) dx from0 to2=12.
Support: `c10s6-def-mass-lamina` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:48–61`)

## c10s8-ex-sk-11
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:429–437`; supported.
Mx=18, My=14, mass12, center(7/6,3/2).
Support: `c10s6-def-moments-center-mass` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:198–213`)

## c10s8-ex-sk-12
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:439–450`; supported.
Square integral x+y=1 gives C=1; integrate x+y on x:0..1,y:0..1-x to get1/3.
Support: `c10s6-def-probability-density` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:376–389`), `c10s4-thm-type-i` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-general-regions.xml:190–218`)

## c10s8-ex-sk-13
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:452–461`; supported.
Triangle integral(x+y)=1/3; divide by area1/2 to get2/3.
Support: `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c10s8-ex-sk-14
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:463–470`; supported.
Direct polar integral2pi integral_0^infinity r/(1+r squared)^2 dr=pi.
Support: `c10s7-thm-comparison-test` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:331–372`), `c10s7-def-improper-unbounded-region` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:81–95`)

## c10s8-ex-sk-15
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:472–479`; supported.
Polar truncation is pi log(1+A squared), which diverges.
Support: `c10s7-ex-decay-too-slow` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:167–187`)

## c10s8-ex-sk-16
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:481–488`; supported.
Exponent p=3/2<2;2pi integral_0^1 r^(-1/2)dr=4pi.
Support: `c10s7-subsec-convergence-comparison` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:286–424`)

## c10s8-ex-sk-17
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:490–497`; supported.
2pi integral_epsilon^1 dr/r diverges.
Support: `c10s7-subsec-unbounded-functions` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:197–284`)

## c10s8-ex-sk-18
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:499–506`; supported.
Substitute u=2x to get sqrt(pi)/2.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`)

## c10s8-project-estimating-rainfall
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:509–613`; supported.
Six deliverables: draw4x3cells; sum39.7 times4=158.8 cm km squared; convert by10000 to1588000m cubed; divide by48 to3.30833cm; indicate maximum near(5,3); discuss unsampled peaks. Worked parts supply the arithmetic, and contour interpretation was taught10.2.
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:580:1
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:580–580`; covered instruction.
Duplicate/local instruction within c10s8-project-estimating-rainfall. Six deliverables: draw4x3cells; sum39.7 times4=158.8 cm km squared; convert by10000 to1588000m cubed; divide by48 to3.30833cm; indicate maximum near(5,3); discuss unsampled peaks. Worked parts supply the arithmetic, and contour interpretation was taught10.2.
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## checkpoint-11-1-one-versus-density
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:98–115`; supported.
Each term1 Delta V is a cell volume; density Delta V is the cell amount.
Support: `c11s1-subsec-volume-as-triple-integral` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:14–148`)

## checkpoint-11-1-three-ordinary-integrals
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:279–295`; supported_at_stated_informal_level.
Group the same small box contributions along one direction, then the next two. It is a geometric discovery explanation; continuous-box Fubini is supplied immediately below.
Support: `c11s1-subsec-integrals-over-boxes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:150–264`)

## checkpoint-11-1-six-orders-same-answer
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:455–471`; supported.
There are3!=6 orders, and continuous-box Fubini states their agreement.
Support: `c11s1-thm-fubini-boxes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:325–341`)

## checkpoint-11-2-inequalities-to-limits
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:83–102`; supported.
Choose outer x then y then z; the innermost integral traverses exactly the allowed z interval for the already fixed x,y.
Support: `c11s2-subsec-describing-by-inequalities` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:15–104`)

## checkpoint-11-2-slice-drops-a-dimension
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:172–190`; supported.
After z integration, the result depends only on x,y and is integrated over the planar shadow.
Support: `c11s2-thm-triple-integral-z-simple` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:143–170`)

## checkpoint-11-2-reorder-needs-redescribe
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:332–352`; supported.
Solve x+ y+z<=6 for the new inner variable x; its yz shadow is0<=y<=6,0<=z<=6-y. The prompt itself supplies the new inequalities, so no future solution is needed.
Support: `c11s2-subsec-describing-by-inequalities` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:15–104`), `c11s2-def-z-simple-solid` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:118–127`)

## source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:460:1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:460–460`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Describe that shadow using the two-dimensional methods from .
Support: `c11s2-subsec-compact-guide` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:451–496`)

## source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:461:1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:461–461`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Write the integral from inside to outside.
Support: `c11s2-subsec-compact-guide` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:451–496`)

## checkpoint-11-3-why-factor-r
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:55–72`; supported.
The angular edge has length r Delta theta, so the same angular increment spans more distance farther from the axis. This asks for local geometry, not the missing integration bridge ROOT-02.
Support: `c11s3-subsec-volume-element` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:28–149`)

## checkpoint-11-3-why-round-shapes-fit
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:196–212`; supported.
Rotational symmetry removes theta from boundary equations, unlike a rectangular box.
Support: `c11s3-subsec-cylinders-cones-symmetry` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:151–252`)

## source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:278:1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:278–278`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Describe the shadow in the xy-plane by bounds on r and \theta.
Support: `c11s3-subsec-choosing-bounds` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:254–336`)

## source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:281:1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:281–281`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Describe the vertical bounds for z.
Support: `c11s3-subsec-choosing-bounds` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:254–336`)

## checkpoint-11-3-tubes-and-revolution
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:388–406`; supported.
A full angular sweep gives circumference2pi r; multiply by radial thickness and vertical extent. The r in the integral records circumference per angle.
Support: `c11s3-subsec-solids-revolution-tubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:338–416`)

## checkpoint-11-4-volume-element-factor
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:93–112`; supported.
Radial edge d rho, meridian arc rho d phi, latitude arc rho sin phi d theta; multiply. Exact integration still needs ROOT-02 repair, but this geometric checkpoint is prepared.
Support: `c11s4-subsec-volume-element` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:19–159`)

## checkpoint-11-4-shells-are-easy
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:170–186`; supported.
Concentric balls/shells have constant radial bounds and full constant angular bounds.
Support: `c11s4-subsec-balls-shells-cones` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:161–249`)

## checkpoint-11-4-angular-factors-out
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:388–406`; supported.
For radial density, integrate sin phi to2 and theta to2pi. A general density mixing rho,phi cannot factor its radial part from phi; a separable special case still can.
Support: `c11s4-subsec-radial-densities` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:369–453`)

## checkpoint-11-5-axis-distance
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:241–260`; supported.
A point on the axis has circular radius and speed0 even if far from the origin; distance to the axis governs rotational weight.
Support: `c11s5-moment-of-inertia` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:231–357`)

## checkpoint-11-5-same-integral-many-meanings
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:428–447`; supported.
Multiply density by cell volume and add; units identify mass, charge or energy.
Support: `c11s5-total-charge-and-total-energy` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:359–466`)

## checkpoint-11-5-why-integrate-to-one
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:529–547`; supported_with_announced_hint.
The point must lie somewhere in its sample region; the hint explicitly identifies certainty with probability1.
Support: `c11s5-probability-in-three-dimensions` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:468–579`)

## checkpoint-11-6-what-stays-and-what-changes
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:94–111`; optional_supported.
Box products and weighted sums generalize; visualization does not. Optional section explicitly supplies n-dimensional Fubini below.
Support: `c11s6-def-higher-dimensional-integral` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:76–87`)

## checkpoint-11-6-volume-near-the-surface
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:239–256`; optional_supported.
Volume ratio is(1/2)^n, tending to0. This proves exclusion of the inner half-size cube, not an unspecified shrinking-width concentration theorem.
Support: `c11s6-subsec-what-changes-in-rn` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:21–112`)

## checkpoint-11-6-ball-volume-decreases
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:364–382`; optional_supported.
Vn=(2pi/n)V(n-2); after n>=13 the factor is less than1/2, so both parity subsequences tend to0. The preceding recurrence supplies what the weaker hint alone would not prove.
Support: `c11s6-unit-ball-volume-recurrence` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:351–362`)

## c11s7-example-wedge
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:157–201`; worked example; supported.
Integrate1+z from0..4-x-y, then x0..2,y0..1, obtaining35/3.
Support: `c11s2-thm-triple-integral-z-simple` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:143–170`)

## c11s7-example-round-tank
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:203–243`; worked example; supported.
Integrate(1+r)r over z0..3+r/2,r0..2,theta0..2pi:104pi/3.
Support: `c11s3-subsec-choosing-bounds` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:254–336`)

## c11s7-example-spherical-cone
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:245–291`; worked example; supported.
Angular factor pi and radial integral integral0..2 rho^3 d rho=4 give C=1/(4pi); probability rho<=1 is1/16.
Support: `c11s4-subsec-volume-element` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:19–159`)

## c11s7-cc-1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:296–300`; supported.
Positive volume element represented by cell volume.
Support: `c11s1-def-triple-integral-first-meaning` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:117–129`)

## c11s7-cc-2
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:302–306`; supported.
Sum cell volumes with weight1.
Support: `c11s1-subsec-volume-as-triple-integral` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:14–148`)

## c11s7-cc-3
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:308–312`; supported.
Unsigned volume versus alternating oriented coordinate volume form; no general three-covector expansion is needed.
Support: `c11s1-subsec-volume-as-triple-integral` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:14–148`)

## c11s7-cc-4
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:314–318`; supported.
Every vertical slice is one interval between two graphs over the xy shadow.
Support: `c11s2-def-z-simple-solid` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:118–127`)

## c11s7-cc-5
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:320–324`; supported.
Fix the two outer coordinates; their allowed set is the projection perpendicular to the inner axis.
Support: `c11s2-subsec-compact-guide` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:451–496`)

## c11s7-cc-6
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:326–330`; supported.
Angular arc length grows in proportion to r.
Support: `c11s3-subsec-volume-element` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:28–149`)

## c11s7-cc-7
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:332–339`; supported.
Two angular edges contribute rho and rho sin phi.
Support: `c11s4-subsec-volume-element` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:19–159`)

## c11s7-cc-8
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:341–348`; supported.
Angle down from the positive z-axis.
Support: `c11s4-tab-spherical-coordinates` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:28–48`)

## c11s7-cc-9
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:350–357`; supported.
A circular cylinder has constant radial/vertical bounds.
Support: `c11s3-subsec-cylinders-cones-symmetry` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:151–252`)

## c11s7-cc-10
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:359–366`; supported.
A centered ball has one constant radial upper bound.
Support: `c11s4-subsec-balls-shells-cones` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:161–249`)

## c11s7-cc-11
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:368–372`; supported.
Different choices of inner slicing direction yield different nested inequalities for the same solid.
Support: `c11s1-thm-fubini-boxes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:325–341`), `c11s2-subsec-changing-order` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:324–449`)

## c11s7-cc-12
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:374–378`; supported.
The weighted averages divide by finite positive total mass; zero mass makes the quotient undefined.
Support: `c11s5-ex-positive-total-mass` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:213–228`)

## c11s7-cc-13
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:380–384`; supported.
Squared distance x squared+y squared=r squared.
Support: `c11s5-def-moment-of-inertia` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:270–280`)

## c11s7-cc-14
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:386–390`; supported.
Nonnegative and total integral1.
Support: `c11s5-probability-in-three-dimensions` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:468–579`)

## c11s7-cc-15
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:392–400`; optional_supported.
Each of n side lengths is multiplied by positive a, giving a^n. Optional review route is marked.
Support: `c11s6-subsec-what-changes-in-rn` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:21–112`)

## c11s7-sk-1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:406–410`; supported.
Unit-volume means give6(1+1/2+3/2)=18, or integrate sequentially.
Support: `c11s1-thm-fubini-boxes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:325–341`)

## c11s7-sk-2
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:412–419`; supported.
Integrate x+y over0<=y<=x,0<=x<=2: integral(3x squared/2)dx=4.
Support: `c11s2-thm-triple-integral-z-simple` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:143–170`)

## c11s7-sk-3
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:421–432`; supported.
x:0..6,y:0..(6-x)/2,z:0..(6-x-2y)/3.
Support: `c11s2-subsec-describing-by-inequalities` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:15–104`)

## c11s7-sk-4
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:434–438`; supported.
Use prior problem bounds with f=1; intercepts6,3,2 give nested integral6.
Support: `c11s2-thm-triple-integral-z-simple` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:143–170`)

## c11s7-sk-5
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:440–448`; supported.
Above first-quadrant quarter disk x squared+y squared<=16, between z=0 and z=x+y.
Support: `c11s2-def-z-simple-solid` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:118–127`)

## c11s7-sk-6
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:450–458`; supported.
y:0..1,z:0..1-y,x:0..1-y-z.
Support: `c11s2-subsec-changing-order` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-general-solid-regions.xml:324–449`)

## c11s7-sk-7
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:460–470`; supported.
2 integral_0^3(2+x)dx=21.
Support: `c11s5-def-mass-from-density` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:50–60`)

## c11s7-sk-8
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:472–480`; supported.
Nx=2 integral_0^3 x(2+x)dx=36, xbar=12/7; ybar=1,zbar=1/2 by reflection symmetry.
Support: `c11s5-def-center-of-mass` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:193–205`)

## c11s7-sk-9
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:482–491`; supported_formula_with_proof_gap.
Iz=delta0 h 2pi integral_0^a r cubed dr=delta0 h pi a^4/2; M=delta0 h pi a squared. Uses supplied cylindrical formula whose justification is ROOT-02.
Support: `c11s5-def-moment-of-inertia` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:270–280`), `c11s3-subsec-choosing-bounds` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:254–336`)

## c11s7-sk-10
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:493–503`; supported_formula_with_proof_gap.
4*2pi integral_0^3 r dr=36pi.
Support: `c11s3-subsec-volume-element` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:28–149`)

## c11s7-sk-11
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:505–514`; supported_formula_with_proof_gap.
2pi integral_0^5 (5-r)r dr=125pi/3.
Support: `c11s3-subsec-cylinders-cones-symmetry` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:151–252`)

## c11s7-sk-12
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:516–525`; supported_formula_with_proof_gap.
4*2pi integral_1^3 (1/r)r dr=16pi.
Support: `c11s3-ex-radially-denser-pipe` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:226–251`)

## c11s7-sk-13
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:527–537`; supported_formula_with_proof_gap.
Full theta and0<=r<=2; z:0..5+r cos theta gives20pi since cosine average0.
Support: `c11s3-ex-cylinder-slanted-roof` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:295–326`)

## c11s7-sk-14
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:539–548`; supported_formula_with_proof_gap.
phi:0..pi/4,rho:0..3,theta full;18pi(1-sqrt2/2).
Support: `c11s4-ex-ball-cut-by-cone` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:221–243`)

## c11s7-sk-15
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:550–557`; supported_formula_with_proof_gap.
Angles both0..pi/2,rho0..5;125pi/6.
Support: `c11s4-ex-first-octant-of-a-ball` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:294–314`)

## c11s7-sk-16
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:559–569`; supported_formula_with_proof_gap.
2pi integral_(2pi/3)^pi integral_0^4 rho squared sin phi d rho d phi=64pi/3.
Support: `c11s4-subsec-angular-bounds` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:251–367`)

## c11s7-sk-17
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:571–579`; supported_formula_with_proof_gap.
4pi integral_0^2(3+rho)rho squared d rho=48pi.
Support: `c11s4-subsec-radial-densities` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:369–453`)

## c11s7-sk-18
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:581–591`; supported_formula_with_proof_gap.
4pi integral_2^5 12 d rho=144pi.
Support: `c11s4-subsec-radial-densities` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:369–453`)

## c11s7-sk-19
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:593–602`; supported.
Cube integral(x+y+z)=3/2 so C=2/3; lower half integral=5/8 giving probability5/12.
Support: `c11s5-probability-in-three-dimensions` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:468–579`)

## c11s7-sk-20
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:604–613`; supported_formula_with_proof_gap.
C=3/(4pi); radius-half volume ratio1/8.
Support: `c11s5-probability-in-three-dimensions` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-applications-of-triple-integrals.xml:468–579`), `c11s4-ex-volume-of-a-ball` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-spherical-coordinates-in-integrals.xml:129–148`)

## c11s7-sk-21
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:615–623`; supported.
Cylindrical, r<=2 and0<=z<=7.
Support: `c11s7-coordinate-systems` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:23–155`)

## c11s7-sk-22
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:625–633`; supported.
Spherical, rho<=3 and0<=phi<=pi/2.
Support: `c11s7-coordinate-systems` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:23–155`)

## c11s7-sk-23
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:635–643`; supported.
Rectangular, x,y already have constant bounds and z one affine upper bound.
Support: `c11s7-coordinate-systems` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:23–155`)

## c11s7-sk-24
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:645–654`; optional_supported.
Mass5*2*1*3*4=120; marked optional.
Support: `c11s6-subsec-what-changes-in-rn` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:21–112`)

## c11s7-sk-25
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:656–664`; optional_supported.
Prompt supplies formula; substitute R=3 to get81pi squared/2.
Support: `c11s6-subsec-volumes-balls-and-boxes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:230–325`)

## c11s7-sk-26
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:666–675`; optional_supported.
Uniform-volume ratio1^6/2^6=1/64.
Support: `c11s6-ex-four-dimensional-quality-control-box` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-higher-dimensional-integrals.xml:48–74`)

## c11s7-sk-27
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:677–685`; supported.
Angles differing by2pi yield the same point; angular interval4pi sweeps two full turns and doubles the volume integral.
Support: `c11s3-subsec-choosing-bounds` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-cylindrical-coordinates-in-integrals.xml:254–336`)

## c11s7-sk-28
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:687–694`; supported.
Coordinate form dx wedge dy wedge dz versus unsigned dV=dx dy dz; use the explicitly defined coordinate three-form, not an arbitrary product rule.
Support: `c11s1-subsec-volume-as-triple-integral` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-triple-integrals.xml:14–148`)

## c11s7-project-volume-formulas
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:697–821`; supported_formula_with_proof_gap.
Five deliverables: describe cube centers versus meridian versus shells; evaluate the three explicit finite sums at four N; compare absolute errors to4pi/3; report observed error decay only; explain coordinate fit. All sum and sample formulas are supplied locally, so programming syntax is optional rather than a hidden mathematical premise.
Support: `c11s7-project-method-cubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:713–728`), `c11s7-project-method-cylindrical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:730–745`), `c11s7-project-method-spherical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:747–760`)

## source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:790:1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:790–790`; covered instruction.
Duplicate/local instruction within c11s7-project-volume-formulas. Five deliverables: describe cube centers versus meridian versus shells; evaluate the three explicit finite sums at four N; compare absolute errors to4pi/3; report observed error decay only; explain coordinate fit. All sum and sample formulas are supplied locally, so programming syntax is optional rather than a hidden mathematical premise.
Support: `c11s7-project-method-cubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:713–728`), `c11s7-project-method-cylindrical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:730–745`), `c11s7-project-method-spherical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:747–760`)

## checkpoint-12-1-why-a-stretch-factor
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:63–78`; supported.
Equal du steps under x=u squared give different dx; derivative2u measures oriented local length scaling.
Support: `c12s1-subsec-single-variable-substitution` (`source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:18–93`)

## checkpoint-12-1-why-tiny-matters
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:200–217`; supported.
Differentiability gives remainder divided by increment norm tending to0; a fixed derivative approximates only small tiles. Earlier vector differential supports this beyond a picture.
Support: `c12s1-subsec-local-linearization` (`source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:177–289`)

## checkpoint-12-1-why-a-determinant
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:310–326`; supported.
Nearly parallel nonzero edges have positive length product but arbitrarily small enclosed area; determinant includes angle and orientation.
Support: `c12s1-subsec-why-determinants-appear` (`source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:291–372`)

## checkpoint-12-2-why-columns-are-images
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:63–78`; supported.
Multiply A by each coordinate unit vector: it selects that column, the image edge direction.
Support: `c12s2-subsec-parallelograms-from-squares` (`source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:15–128`)

## checkpoint-12-2-meaning-of-det-zero
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:236–253`; supported.
Dependent columns collapse area and make the map noninvertible; it cannot serve as reversible planar coordinates.
Support: `c12s2-subsec-area-scaling-det` (`source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:130–254`)

## checkpoint-12-2-why-keep-the-sign
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:292–307`; supported.
Sign distinguishes preservation from reversal of ordered directions; magnitude alone measures unsigned area.
Support: `c12s2-subsec-orientation-sign` (`source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:256–338`)

## checkpoint-12-3-varying-determinant
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:114–131`; supported.
For shear(u,v+u squared), DT=[[1,0],[2u,1]] has determinant1 everywhere though nonlinear. Variation is possible, not inevitable.
Support: `c12s1-def-jacobian-determinant-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:264–274`)

## checkpoint-12-3-right-locally-wrong-globally
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:285–301`; supported.
(u squared,v) maps both u signs to same interior image; integrating abs2u over[-1,1] counts twice.
Support: `c12s3-subsec-one-to-one-splitting` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:257–351`)

## source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:366:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:366–381`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Compute: x_r=\cos\theta, \qquad x_\theta=-r\sin\theta, and y_r=\sin\theta, \qquad y_\theta=r\cos\theta. Therefore \frac{\partial(x,y)}{\partial(r,\theta)} \amp= \det \begin{pmatrix} \cos\theta \amp -r\sin\theta\\ \sin\theta \amp r\cos\theta \end{pmatrix} \amp= r\cos^2\theta+r\sin^2\theta \amp= r. So \boxed{ dA=r\,dr\,d\theta. } This is the old pola
Support: `c12s3-subsec-polar-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:353–455`)

## checkpoint-12-3-polar-r-meaning
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:383–399`; supported.
Derivative vectors are perpendicular with lengths1 and r, so determinant equals the same radial-thickness times angular-arc scale.
Support: `c12s3-subsec-polar-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:353–455`), `c10s5-subsec-why-area-element` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-in-polar-coordinates.xml:74–190`)

## source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:35:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:35–44`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Compute the volume directly: \operatorname{Vol}(E) \amp= \int_1^2\int_1^3\int_0^{xy}1\,dz\,dy\,dx \amp= \int_1^2\int_1^3 xy\,dy\,dx \amp= \left[\int_1^2 x\,dx\right]\left[\int_1^3 y\,dy\right] \amp= \frac32\cdot4 \amp= 6.
Support: `c12s4-subsec-volume-scaling-jacobian` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:18–244`)

## checkpoint-12-4-why-determinant-is-volume
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:84–100`; supported.
Scalar triple product/determinant measures parallelepiped volume, including relative directions that lengths alone omit.
Support: `c12s4-subsec-volume-scaling-jacobian` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:18–244`)

## checkpoint-12-4-vanishing-spherical-factor
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:316–332`; supported.
At rho0 all angles identify one point; at poles the azimuth direction collapses, so derivative loses a volume direction.
Support: `c12s4-subsec-cylindrical-spherical-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:246–365`)

## checkpoint-12-4-read-region-not-integrand
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:418–433`; supported.
Ellipsoid axes suggest rescaling to a ball; simplifying bounds can be decisive even when integrand1 needs no simplification.
Support: `c12s4-subsec-general-transformations-r3` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:367–434`)

## checkpoint-12-5-signed-area-meaning
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:142–157`; supported.
The negative value records orientation reversal under T; positive area discards ordered-direction information.
Support: `c12s5-subsec-what-happens-to-dxdy` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:22–158`)

## checkpoint-12-5-why-repeats-vanish
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:302–318`; supported.
Determinant definition is alternating in rows; repeated covectors give zero. The six permutations of distinct coordinates survive with permutation signs, exactly the3x3 determinant expansion.
Support: `c12s5-subsec-pulling-back-volume-elements` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:273–370`)

## checkpoint-12-5-absolute-value-vs-sign
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:377–393`; supported.
Unsigned size is nonnegative; absolute value removes whether parameter orientation agrees with target orientation.
Support: `c12s5-subsec-what-happens-to-dxdy` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:22–158`)

## checkpoint-12-6-multiplicity
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:94–110`; supported.
Interior injectivity fails because theta and theta+2pi coincide; local Jacobian cannot distinguish repeated images.
Support: `c12s6-not-one-to-one` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:18–118`)

## checkpoint-12-6-zero-jacobian-meaning
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:175–191`; supported.
Neither polar coordinates at the origin nor complex squaring there is a regular invertible chart. Polar boundary degeneracy does not overcount positive area; the full complex disk has interior double coverage. Zero determinant obstructs a differentiable inverse, not automatically integrability.
Support: `c12s6-zero-jacobian` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:120–213`)

## checkpoint-12-6-orientation-flip
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:294–311`; supported.
Image of positive parameter boundary is clockwise; absJ would erase the sign needed to distinguish the two oriented integrals.
Support: `c12s6-oriented-integrals-remember-sign` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:264–372`)

## c12s7-subsec-slanted-window
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:181–229`; worked example; supported.
Inverse x=(u+v)/2,y=(u-v)/2 has absolute determinant1/2; integrate u on[1,3]x[0,2] to obtain4.
Support: `c12s3-thm-change-of-variables-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:152–196`)

## c12s7-subsec-curved-plate
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:231–301`; worked example; supported.
u=xy,v=y/x gives inverse determinant1/(2v); mass integral1..4 u du times integral1..3 dv/(2v)=15log(3)/4.
Support: `c12s3-thm-change-of-variables-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:152–196`)

## source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:266:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:266–295`; covered instruction.
Duplicate/local instruction within c12s7-subsec-curved-plate. u=xy,v=y/x gives inverse determinant1/(2v); mass integral1..4 u du times integral1..3 dv/(2v)=15log(3)/4.
Support: `c12s3-thm-change-of-variables-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:152–196`)

## c12s7-subsec-stretched-ball
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:303–356`; worked example; supported.
Scale x=2u,y=3v,z=w, determinant6, then spherical integral6*4pi integral0..1(1+rho^2)rho^2 d rho=64pi/5.
Support: `c12s4-thm-change-of-variables-space` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:169–221`)

## c12s7-ex-cc-jacobian-plane
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:361–368`; supported.
Signed local area multiplier of derivative.
Support: `c12s1-def-jacobian-determinant-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:264–274`)

## c12s7-ex-cc-jacobian-space
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:370–377`; supported.
Signed local volume multiplier of derivative.
Support: `c12s4-def-jacobian-determinant-space` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:142–167`)

## c12s7-ex-cc-absolute-value
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:379–387`; supported.
Unsigned size remains positive after orientation reversal.
Support: `c12s6-why-absolute-value` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:215–262`)

## c12s7-ex-cc-wedge-vs-dA
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:389–398`; supported.
Ordered planar orientation.
Support: `c12s5-tab-orientation-vs-absolute-value` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:395–424`)

## c12s7-ex-cc-wedge-vs-dV
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:400–409`; supported.
Ordered spatial orientation.
Support: `c12s5-tab-orientation-vs-absolute-value` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:395–424`)

## c12s7-ex-cc-signed-pullback
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:411–419`; supported.
Alternating bilinear expansion produces xu yv-xv yu, with its sign.
Support: `c12s5-subsec-determinant-as-coefficient` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:160–271`)

## c12s7-ex-cc-one-to-one-interior
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:421–427`; supported.
Avoid counting positive-area image points repeatedly under the supplied simple formula.
Support: `c12s3-subsec-one-to-one-splitting` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:257–351`)

## c12s7-ex-cc-boundary-overlaps
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:429–433`; supported_at_stated_informal_level.
For the stated piecewise smooth boundaries the repeated sets contribute no area/volume; whole-region overlap would matter.
Support: `c12s3-subsec-polar-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:353–455`)

## c12s7-ex-cc-polar-origin
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:435–442`; supported.
r0 is a parameter boundary collapsing to one image point, not repeated interior area.
Support: `c12s3-subsec-polar-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:353–455`)

## c12s7-ex-cc-jacobian-zero-patch
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:444–451`; supported.
The nonzero-J condition of the taught theorem fails; derivative collapses full-dimensional local measure, illustrated by(u,0) or(u,v,0).
Support: `c12s3-subsec-one-to-one-splitting` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:257–351`), `c12s4-subsec-volume-scaling-jacobian` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:18–244`)

## c12s7-ex-cc-crease-split
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:453–460`; supported.
No single derivative across crease; restrictions match smooth extensions on either side, allowing piecewise use.
Support: `c12s3-subsec-one-to-one-splitting` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:257–351`)

## c12s7-ex-cc-multiplicity-two
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:462–470`; supported.
Generic disk point has two angular preimages and is counted twice.
Support: `c12s6-not-one-to-one` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:18–118`)

## c12s7-ex-cc-boundary-suggests-vars
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:472–478`; supported.
Choose combinations constant on boundary curves so limits become constants.
Support: `c12s7-subsec-skills-choosing` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:27–179`)

## c12s7-ex-cc-integrand-vs-element
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:480–487`; supported.
Composition changes field values; absJ changes weights assigned to parameter cells.
Support: `c12s3-subsec-jacobian-determinant` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:205–255`)

## c12s7-ex-cc-local-vs-global
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:489–496`; supported.
DT inspects one point; injectivity compares pairs of distinct parameter points across the domain.
Support: `c12s6-not-one-to-one` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:18–118`)

## c12s7-ex-sk-jacobian-linear
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:502–511`; supported.
3*2-(-1)*1=7.
Support: `c12s1-def-jacobian-determinant-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-the-geometry-of-substitution.xml:264–274`)

## c12s7-ex-sk-area-unit-square
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:513–523`; supported.
abs7 times unit area=7.
Support: `c12s2-thm-area-scaling-linear` (`source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:172–208`)

## c12s7-ex-sk-integral-image-square
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:525–534`; supported.
J=7,x-y=u-3v;7 integral_unit(u-3v)=-7.
Support: `c12s2-thm-area-scaling-linear` (`source/chapters/ch12-change-of-variables/sections/sec-12-linear-changes-of-variables.xml:172–208`)

## c12s7-ex-sk-solve-uv
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:536–545`; supported.
x=(u+v)/2,y=(u-v)/2,J=-1/2.
Support: `c12s7-subsec-slanted-window` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:181–229`)

## c12s7-ex-sk-area-uv-region
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:547–557`; supported.
Parameter rectangle[0,2]x[1,3] has area4;absJ1/2 gives2.
Support: `c12s7-subsec-slanted-window` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:181–229`)

## c12s7-ex-sk-disk-area
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:559–566`; supported.
2pi integral_0^a r dr=pi a squared for radius a>=0.
Support: `c12s3-thm-change-of-variables-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:152–196`)

## c12s7-ex-sk-annulus-integral
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:568–577`; supported.
2pi integral_1^2 r cubed dr=15pi/2.
Support: `c12s3-thm-change-of-variables-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:152–196`)

## c12s7-ex-sk-circular-plate-mass
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:579–587`; supported.
2pi integral_0^3(10-r squared)r dr=99pi/2.
Support: `c12s3-ex-dye-circular-spill` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:401–431`)

## c12s7-ex-sk-hyperbola-region-area
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:589–601`; supported.
Inverse x=sqrt(u/v),y=sqrt(uv),J=1/(2v);u2..6,v1..4 gives2log4=4log2.
Support: `c12s7-subsec-curved-plate` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:231–301`)

## c12s7-ex-sk-hyperbola-region-integral
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:603–610`; supported.
Integrate u/(2v) over[2,6]x[1,4] gives8log4=16log2.
Support: `c12s7-subsec-curved-plate` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:231–301`)

## c12s7-ex-sk-pullback-uvuv
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:612–622`; supported.
4(u squared+v squared)du wedge dv; vanishes only at origin.
Support: `c12s5-def-pullback-area-form` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:201–213`)

## c12s7-ex-sk-double-cover
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:624–632`; supported.
Polar form sends(s,alpha) to(s squared,2alpha); opposite domain points coincide except origin.
Support: `c12s6-zero-jacobian` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:120–213`)

## c12s7-ex-sk-reflection-pullback
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:634–644`; supported.
-du wedge dv; reverses orientation.
Support: `c12s6-oriented-integrals-remember-sign` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:264–372`)

## c12s7-ex-sk-volume-scale-diagonal
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:646–654`; supported.
abs(2*3*4)=24.
Support: `c12s4-def-jacobian-determinant-space` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:142–167`)

## c12s7-ex-sk-ellipsoid-volume
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:656–665`; supported.
24 times unit ball volume4pi/3=32pi.
Support: `c12s4-thm-change-of-variables-space` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:169–221`)

## c12s7-ex-sk-cylinder-volume
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:667–674`; supported.
5*2pi integral_0^3 r dr=45pi.
Support: `c12s4-thm-change-of-variables-space` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:169–221`)

## c12s7-ex-sk-ball-volume
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:676–683`; supported.
Full angles give4pi integral_0^a rho squared d rho=4pi a cubed/3.
Support: `c12s4-subsec-cylindrical-spherical-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:246–365`)

## c12s7-ex-sk-ball-mass
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:685–693`; supported.
4pi integral_0^2(4-rho)rho squared d rho=80pi/3.
Support: `c12s4-ex-radially-denser-ball` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:339–364`)

## c12s7-ex-sk-jacobian-uvw
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:695–703`; supported.
Triangular derivative matrix with diagonal1,1,uv has determinant uv.
Support: `c12s4-subsec-volume-scaling-jacobian` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:18–244`)

## c12s7-ex-sk-variable-ceiling-volume
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:705–714`; supported.
Parameter bounds u1..2,v0..1,w0..1;J=u(1+v), integral9/4.
Support: `c12s4-ex-solid-variable-ceiling` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:484–516`)

## c12s7-ex-sk-polar-wedge-plane
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:716–726`; supported.
r dr wedge d theta.
Support: `c12s5-def-pullback-area-form` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:201–213`)

## c12s7-ex-sk-cylindrical-wedge
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:728–738`; supported.
Use taught triple-wedge determinant to get r dr wedge d theta wedge dz.
Support: `c12s5-subsec-pulling-back-volume-elements` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:273–370`)

## c12s7-ex-sk-spherical-element
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:740–748`; supported.
rho squared sin phi d rho d phi d theta (unsigned stated range).
Support: `c12s4-subsec-cylindrical-spherical-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:246–365`)

## c12s7-ex-sk-cover-once
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:750–759`; supported.
Once in the interior, with theta seam and r0 boundary overlap.
Support: `c12s3-subsec-polar-revisited` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:353–455`)

## c12s7-ex-sk-cover-twice
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:761–770`; supported.
Two full turns give multiplicity2 except exceptional boundary points.
Support: `c12s6-not-one-to-one` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:18–118`)

## c12s7-ex-sk-choose-vars-wedge
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:772–780`; supported.
Polar:r1..3,theta arctan2..arctan5; maps first-quadrant ray boundaries to constants.
Support: `c12s7-tab-natural-substitutions` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:54–92`)

## c12s7-ex-sk-choose-vars-parallelogram
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:782–790`; supported.
Set u=x+y,v=x-2y; then u1..4,v0..3 and invert nonzero linear determinant.
Support: `c12s7-subsec-skills-choosing` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:27–179`)

## c12s7-ex-sk-rules-plane
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:792–798`; supported.
Compose coefficient; multiply by absJ for unsigned integral or J for pulled-back form and induced orientation, under stated injectivity/regularity assumptions.
Support: `c12s5-def-pullback-area-form` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:201–213`), `c12s3-thm-change-of-variables-plane` (`source/chapters/ch12-change-of-variables/sections/sec-12-nonlinear-changes-of-variables-in-the-plane.xml:152–196`)

## c12s7-ex-sk-rules-space
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:800–806`; supported.
Same rule in3D, keeping the exact signed versus unsigned conventions and theorem hypotheses.
Support: `c12s5-subsec-pulling-back-volume-elements` (`source/chapters/ch12-change-of-variables/sections/sec-12-pullbacks-of-area-and-volume-elements.xml:273–370`), `c12s4-thm-change-of-variables-space` (`source/chapters/ch12-change-of-variables/sections/sec-12-changes-of-variables-in-space.xml:169–221`)

## c12s7-ex-sk-example-double-cover
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:808–815`; supported.
Polar map on0<=r<=1,0<=theta<=4pi yields2pi while image area pi.
Support: `c12s6-not-one-to-one` (`source/chapters/ch12-change-of-variables/sections/sec-12-warning-examples.xml:18–118`)

## c12s7-subsec-project-gaussian
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:818–980`; supported.
Six deliverables: definite integral needs no elementary primitive; finite square/disk squeeze justifies squaring; polar u=r squared gives I squared=pi; scaled Gaussian sqrt(pi/a); normalized C=1/(sigma sqrt(2pi)); radial symmetry explains polar choice. All local worked parts support hand-in; no unproved improper Fubini.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:836:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:836–847`; covered instruction.
Use the earlier bounded-square Fubini/disk comparison to justify squaring the Gaussian integral; later scaling/normalization parts are not needed for this instruction.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`)

## source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:941:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:941–941`; covered instruction.
Duplicate/local instruction within c12s7-subsec-project-gaussian. Six deliverables: definite integral needs no elementary primitive; finite square/disk squeeze justifies squaring; polar u=r squared gives I squared=pi; scaled Gaussian sqrt(pi/a); normalized C=1/(sigma sqrt(2pi)); radial symmetry explains polar choice. All local worked parts support hand-in; no unproved improper Fubini.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:944:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:944–944`; covered instruction.
Duplicate/local instruction within c12s7-subsec-project-gaussian. Six deliverables: definite integral needs no elementary primitive; finite square/disk squeeze justifies squaring; polar u=r squared gives I squared=pi; scaled Gaussian sqrt(pi/a); normalized C=1/(sigma sqrt(2pi)); radial symmetry explains polar choice. All local worked parts support hand-in; no unproved improper Fubini.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:947:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:947–947`; covered instruction.
Duplicate/local instruction within c12s7-subsec-project-gaussian. Six deliverables: definite integral needs no elementary primitive; finite square/disk squeeze justifies squaring; polar u=r squared gives I squared=pi; scaled Gaussian sqrt(pi/a); normalized C=1/(sigma sqrt(2pi)); radial symmetry explains polar choice. All local worked parts support hand-in; no unproved improper Fubini.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:953:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:953–957`; covered instruction.
Duplicate/local instruction within c12s7-subsec-project-gaussian. Six deliverables: definite integral needs no elementary primitive; finite square/disk squeeze justifies squaring; polar u=r squared gives I squared=pi; scaled Gaussian sqrt(pi/a); normalized C=1/(sigma sqrt(2pi)); radial symmetry explains polar choice. All local worked parts support hand-in; no unproved improper Fubini.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:966:1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:966–969`; covered instruction.
Duplicate/local instruction within c12s7-subsec-project-gaussian. Six deliverables: definite integral needs no elementary primitive; finite square/disk squeeze justifies squaring; polar u=r squared gives I squared=pi; scaled Gaussian sqrt(pi/a); normalized C=1/(sigma sqrt(2pi)); radial symmetry explains polar choice. All local worked parts support hand-in; no unproved improper Fubini.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## checkpoint-13-1-instruction-book
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-vector-fields.xml:81–98`; supported.
A field assigns a velocity at every domain point regardless of whether a chosen particle visits it; a trajectory is a parameterized curve following those assignments.
Support: `c13s1-subsec-vector-at-every-point` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-vector-fields.xml:19–131`)

## checkpoint-13-1-gradient-knows-the-hill
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-vector-fields.xml:180–198`; supported.
At regular points gradient is perpendicular to level curves and points toward greatest increase; zero gradient is a stationary exception, and generic fields need not arise from a scalar potential.
Support: `c13s1-subsec-velocity-force-gradient` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-vector-fields.xml:133–217`)

## checkpoint-13-1-flow-line-meaning
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-vector-fields.xml:343–361`; supported.
Differentiate r and compare with the field evaluated at r(t); equality matches the local arrow, whereas a fixed evaluation would prescribe one constant vector.
Support: `c13s1-def-flow-line` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-vector-fields.xml:323–334`)

## checkpoint-13-2-speed-factor-meaning
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-line-integrals-of-scalar-functions.xml:155–171`; supported.
Speed converts parameter time to length; dropping it makes the result depend on arbitrary tracing speed.
Support: `c13s2-def-line-integral-scalar-function` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-line-integrals-of-scalar-functions.xml:128–139`)

## checkpoint-13-2-parameter-not-arc-length
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-line-integrals-of-scalar-functions.xml:232–247`; supported.
Unit speed norm(rprime)=1 makes arc-length increment equal parameter increment (up to an origin choice).
Support: `c13s2-subsec-arc-length-element` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-line-integrals-of-scalar-functions.xml:97–172`)

## checkpoint-13-2-orientation-irrelevant
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-line-integrals-of-scalar-functions.xml:319–335`; supported.
Norm introduces abs(phi prime); reversal changes traversal order but not positive length weights.
Support: `c13s2-thm-scalar-line-integral-reparametrization` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-line-integrals-of-scalar-functions.xml:282–297`)

## checkpoint-13-3-perpendicular-no-work
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:127–144`; supported.
Every dot product with the tangent displacement is0; total work0.
Support: `c13s3-subsec-force-dotted-displacement` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:21–145`)

## checkpoint-13-3-direction-survives
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:244–260`; supported.
Velocity reverses direction whereas speed stays unchanged; linear pairing records the reversal as a sign.
Support: `c13s3-subsec-parametrization-orientation` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:233–404`)

## checkpoint-13-3-swirl-vs-radial
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:507–523`; supported.
Swirl is tangent in the direction of travel, giving positive dot product; radial is perpendicular and gives0.
Support: `c13s3-ex-swirling-field-positive-circulation` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:428–444`), `c13s3-ex-radial-field-zero-circulation` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:472–498`)

## checkpoint-13-4-form-as-machine
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:103–121`; supported.
The point fixes coefficients but the displacement supplies vector components to be measured; both are needed for the scalar evaluation.
Support: `c13s4-subsec-work-written-pdx` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:27–122`)

## checkpoint-13-4-no-length-element
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:180–197`; supported.
A1-form pairs directly with directed displacement. Its pullback already includes rprime; adding another speed would double-count the parameter change.
Support: `c13s4-subsec-why-1-form-integrates` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:124–198`)

## checkpoint-13-4-arrow-vs-rule
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:431–451`; supported.
Polar coordinate displacement has angular term r e_theta dtheta; the metric identifies vectors with work forms, so e_theta corresponds to r dtheta, not dtheta. Both descriptions are valid with the metric conversion, and the form itself integrates without a metric.
Support: `c13s4-subsec-vector-fields-and-1-forms` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:332–475`), `c13s4-ex-angular-unit-vector` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:375–414`)

## checkpoint-13-5-potential-needs-domain
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml:266–286`; supported.
A global single-valued potential would have zero change on a closed loop; angle increases2pi, so only local angle branches are potentials.
Support: `thm-c13s5-ftli` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml:205–240`), `c13s4-ex-image-counted-twice` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:298–322`)

## checkpoint-13-5-converse-meaning
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml:330–348`; supported.
The prompt supplies candidate phi(X)=integral_A^X omega; path independence makes that definition unambiguous. The later theorem proves its differentiability, so this is a conceptual discovery question rather than an instruction to assume a proof.
Support: `thm-c13s5-exact-path-independent` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml:310–323`)

## checkpoint-13-5-closed-loop-zero
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml:469–487`; supported.
Endpoint difference phi(A)-phi(A)=0; a nonzero loop integral disproves a global potential.
Support: `thm-c13s5-ftli` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-conservative-vector-fields-and-exact-1-forms.xml:205–240`)

## checkpoint-13-6-direction-of-the-arrow
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:104–122`; supported.
Necessary exact-implies-closed does not imply its converse; extra domain hypotheses are needed for the supplied sufficient theorem.
Support: `c13s6-test-py-qx-plane` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:16–255`)

## checkpoint-13-6-what-the-hole-feels-like
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:406–423`; supported.
A loop around a missing point cannot contract within the domain; angle-form example has zero local curl yet nonzero loop integral.
Support: `c13s6-simply-connected-regions` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:347–461`), `c13s4-ex-image-counted-twice` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:298–322`)

## checkpoint-13-6-why-gluing-fails
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:548–567`; supported.
Following local angle branches around a full loop adds2pi, so they cannot agree as one single-valued continuous potential.
Support: `c13s6-local-versus-global-potentials` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:463–581`)

## source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-warning-examples.xml:32:1
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-warning-examples.xml:32–50`; not a separate assessment; local exposition.
Expository algorithm or immediately worked calculation, not a separate assessment. Read with its displayed definition/bounds/calculation: Write \alpha=P\,dx+Q\,dy, where P(x,y)=\frac{-y}{x^2+y^2}, \qquad Q(x,y)=\frac{x}{x^2+y^2}. Compute: P_y \amp= \frac{-(x^2+y^2)+2y^2}{(x^2+y^2)^2} \amp= \frac{y^2-x^2}{(x^2+y^2)^2}, and Q_x \amp= \frac{(x^2+y^2)-2x^2}{(x^2+y^2)^2} \amp= \frac{y^2-x^2}{(x^2+y^2)^2}. Thus P_y=Q_x everywhere on D.
Support: `c13s7-subsec-curl-zero-no-global-potential` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-warning-examples.xml:21–133`)

## checkpoint-13-7-local-test-misses-hole
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-warning-examples.xml:54–71`; supported.
Derivatives detect local compatibility; they do not encode whether a loop surrounds a missing point. The given angle form supplies the exact counterexample.
Support: `c13s6-local-versus-global-potentials` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:463–581`)

## checkpoint-13-7-shrinking-loop-keeps-circulation
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-warning-examples.xml:285–302`; supported.
Origin is excluded, so radial shrinking cannot finish there. Direct calculation gives tangential field1/R times length2piR=2pi for every positive R; no claim of unproved limit exchange is needed.
Support: `c13s7-subsec-singularity-hidden-at-origin` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-warning-examples.xml:233–311`)

## checkpoint-13-7-half-plane-vs-punctured-plane
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-warning-examples.xml:318–336`; supported.
On x>0 arctan(y/x) is a single branch; on punctured plane continuation around origin changes angle by2pi, contradicting a global potential.
Support: `c13s6-local-versus-global-potentials` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-curl-tests-in-the-plane-and-in.xml:463–581`)

## c13s8-project
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-chapter-review-and-applications.xml:203–379`; supported.
Rectangle sides give0,ab,ab,0; circle pullback R squared dt gives2pi R squared; polygon edge i gives xi*y(i+1)-x(i+1)*yi by cancellation of t terms. Sum gives boundary integral. Shoelace AREA identity is explicitly deferred to14.7, not assumed for the boundary calculation; retain that proof ceiling.
Support: `c13s3-def-work-integral` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:167–178`), `c13s4-def-pullback-1-form` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:218–233`), `c13s8-project-rectangle` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-chapter-review-and-applications.xml:219–322`), `c13s8-project-circle` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-chapter-review-and-applications.xml:324–344`), `c13s8-project-polygon` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-chapter-review-and-applications.xml:346–378`)

## source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-chapter-review-and-applications.xml:229:1
Source: `source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-chapter-review-and-applications.xml:229–232`; covered instruction.
Parametrize the four rectangle edges in positive orientation and pair -y dx+x dy with their velocities; contributions0,ab,ab,0 sum2ab. Circle/polygon project parts are not prerequisites.
Support: `c13s3-def-work-integral` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-work-integrals-of-vector-fields.xml:167–178`), `c13s4-def-pullback-1-form` (`source/chapters/ch13-vector-fields-line-integrals/sections/sec-13-differential-1-forms.xml:218–233`)

## c10s8-project-part-4-deliverable-1
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:583–585`; supported by announced project scaffold.
Draw4x3 equal cells over[0,8]x[0,6].
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c10s8-project-part-4-deliverable-2
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:586–591`; supported by announced project scaffold.
Sum12 readings39.7, multiply by cell area4:158.8.
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c10s8-project-part-4-deliverable-3
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:592–598`; supported by announced project scaffold.
1cm*1km^2=10000m^3, so1588000m^3.
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c10s8-project-part-4-deliverable-4
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:599–601`; supported by announced project scaffold.
Mean158.8/48=3.30833cm.
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c10s8-project-part-4-deliverable-5
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:602–604`; supported by announced project scaffold.
Connect comparable readings in a contour sketch, with maximum near(5,3).
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c10s8-project-part-4-deliverable-6
Source: `source/chapters/ch10-double-integrals/sections/sec-10-chapter-review-and-applications.xml:605–610`; supported by announced project scaffold.
A peak between sensors can be missed; midpoint data do not bound that error without further information.
Support: `c10s2-ex-midpoint-estimate` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:78–104`), `c10s2-subsec-numerical-estimates` (`source/chapters/ch10-double-integrals/sections/sec-10-double-integrals-over-rectangles.xml:387–585`), `c10s6-def-average-value` (`source/chapters/ch10-double-integrals/sections/sec-10-applications-of-double-integrals.xml:419–428`)

## c11s7-project-what-to-hand-in-deliverable-1
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:793–795`; supported by announced project scaffold.
Describe Cartesian inside-center counting, meridional cylindrical sums and spherical shell sums.
Support: `c11s7-project-method-cubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:713–728`), `c11s7-project-method-cylindrical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:730–745`), `c11s7-project-method-spherical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:747–760`)

## c11s7-project-what-to-hand-in-deliverable-2
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:796–798`; supported by announced project scaffold.
Use supplied midpoint finite sums at N=4,8,16,32; formulas need only finite loops/arithmetic.
Support: `c11s7-project-method-cubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:713–728`), `c11s7-project-method-cylindrical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:730–745`), `c11s7-project-method-spherical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:747–760`)

## c11s7-project-what-to-hand-in-deliverable-3
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:799–804`; supported by announced project scaffold.
Subtract4pi/3 from each estimate and take absolute value.
Support: `c11s7-project-method-cubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:713–728`), `c11s7-project-method-cylindrical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:730–745`), `c11s7-project-method-spherical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:747–760`)

## c11s7-project-what-to-hand-in-deliverable-4
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:805–807`; supported by announced project scaffold.
Compare measured errors for these N; spherical has the smallest errors in displayed table. No universal asymptotic theorem is required.
Support: `c11s7-project-method-cubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:713–728`), `c11s7-project-method-cylindrical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:730–745`), `c11s7-project-method-spherical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:747–760`)

## c11s7-project-what-to-hand-in-deliverable-5
Source: `source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:808–813`; supported by announced project scaffold.
Curved coordinate cells match the boundary and reduce partial-cell mismatch.
Support: `c11s7-project-method-cubes` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:713–728`), `c11s7-project-method-cylindrical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:730–745`), `c11s7-project-method-spherical` (`source/chapters/ch11-triple-higher-integrals/sections/sec-11-chapter-review-and-applications.xml:747–760`)

## c12s7-subsubsec-project-handin-deliverable-1
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:943–945`; supported by announced project scaffold.
The definite integral can be evaluated by symmetry and a limit without finding an elementary antiderivative.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## c12s7-subsubsec-project-handin-deliverable-2
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:946–948`; supported by announced project scaffold.
Square bounded integrals and use bounded-square Fubini; squeeze with inscribed/circumscribed disks before taking limits.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## c12s7-subsubsec-project-handin-deliverable-3
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:949–951`; supported by announced project scaffold.
Polar integral over disk radiusR is pi(1-exp(-R^2)); limit pi, positive square root sqrt(pi).
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## c12s7-subsubsec-project-handin-deliverable-4
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:952–958`; supported by announced project scaffold.
u=sqrt(a)x gives sqrt(pi/a), a>0.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## c12s7-subsubsec-project-handin-deliverable-5
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:959–964`; supported by announced project scaffold.
Take a=1/(2sigma^2), sigma>0; normalizing constant1/(sigma sqrt(2pi)).
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)

## c12s7-subsubsec-project-handin-deliverable-6
Source: `source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:965–970`; supported by announced project scaffold.
Squaring makes the integrand exp(-(x^2+y^2)), radial, so polar separates the angle and a one-variable substitution.
Support: `c10s7-subsec-gaussian-integral` (`source/chapters/ch10-double-integrals/sections/sec-10-improper-double-integrals.xml:426–505`), `c12s7-subsubsec-project-part1` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:834–848`), `c12s7-subsubsec-project-part2` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:850–876`), `c12s7-subsubsec-project-part4` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:898–915`), `c12s7-subsubsec-project-part5` (`source/chapters/ch12-change-of-variables/sections/sec-12-chapter-review-and-applications.xml:917–937`)
