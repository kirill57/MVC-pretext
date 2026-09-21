# Independent challenge of GF-05

Root independently reread `c18s10-ex-pr-any-surface`, lines519–528 of `source/chapters/ch18-generalized-stokes/sections/sec-18-chapter-review-and-capstone-problems.xml`, the Chapter18 wrapper,15.2's scalar surface-integral definition and the compact Stokes statements in15.5/18.2/18.5.

Attempted refutation: “surface” could carry a standing compact-admissible convention. The actual15.2 definition instead allows a once-covered regular parameter domain whenever the integral exists, with compact continuous patches only as a sufficient example. Neither the Chapter18 wrapper nor this review's task supplies an all-surfaces-compact convention. The immediately neighboring hemisphere task has a compact surface by its explicit equation, but this one newly quantifies “any smooth upward-oriented surface.”

Take the exterior planar surface `S={(x,y,0):x²+y²>=1}`, oriented upward. It is smooth with the stated unit-circle boundary; its induced orientation is clockwise. The truncated annulus of outer radius R has integral `3pi(R²-1)`, tending to infinity. Thus the literal hypotheses do not determine the intended finite3pi answer.

Retain H/I,P2, high confidence in the literal counterexample and moderate contextual severity. Supply “compact” and explicitly compatible counterclockwise boundary orientation. Then Stokes applied to `(3/2)(x dy-y dx)` gives3pi. This is a local review-scope omission, not a defect in the correctly stated compact theorem, and does not justify weakening its compactness hypothesis.
