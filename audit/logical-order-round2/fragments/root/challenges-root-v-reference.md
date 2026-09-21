# Independent challenge of Chapter9 and AppendixA–E review

Reviewer: root, separate from the reference worker. Snapshot `9a9d110af839b539fe598de66ecc4320a4126af4`. This is a challenge of selected findings and protected judgments, not a second full reading of all40 sections.

## REF-01: attempted contextual defense; retained P2

I reread Section9.1's preceding regular-level-curve discussion and its new surface subsection (lines231–325), and Section9.5's complete normal-line discussion and subsequent theorem (lines135–241). The strongest defense is that earlier passages and the later theorem already say the gradient must be nonzero. This prepares an attentive reader to repair the checkpoint, so P1 would overstate the defect.

It does not make the checkpoint's unrestricted claim true. `F=z^2` defines the perfectly smooth plane `z=0` with zero gradient everywhere on it. The zero vector determines no normal direction or plane equation. In9.5 let `g=(x^2+y^2-1)^2`, constrain `g=0`, and maximize `f=x`. The circle is smooth; at `(1,0)`, `grad f=(1,0)` while `grad g=0`, so no multiplier satisfies `grad f=lambda grad g`. The prose immediately before the checkpoint also infers parallelism of two vectors perpendicular to a tangent without excluding the zero constraint gradient. Retain the two occurrences under one omitted-regularity root; repair the nearby prose as well as the task.

## REF-02: attempted endpoint defense; retained P2

Section9.6's segment example (lines134–168) is correct. Its hint (lines179–184) nevertheless suggests that stopping at an endpoint destroys a well-defined tangent. `r(t)=(t,0)` for `-1<=t<=1` has a well-defined one-sided tangent at both ends and a smooth extension. What fails is two-sided feasible motion in the domain; `f(t,0)=t` has nonzero derivative at its endpoint maximum. Replace the hint with a question about which signs of a small parameter change remain feasible. No new tangent theory or constraint theorem is necessary.

## Supported judgment: second derivative test

Attempted objection: a positive definite quadratic form merely has a positive value in each direction; this is not yet a uniform lower bound. The worker's reconstruction explicitly applies the already supplied EVT to the unit circle and then uses the earlier uniform Taylor remainder. If `q>=m>0` there, homogeneity gives `q(h)>=m||h||^2`; the remainder becomes smaller than a fixed fraction of that expression. This is sufficient, and it differs from the finite-cover/subsequence facts missing later. Protected decision retained.

## Supported judgment: multiplier proof and singular constraint task

Attempted objection: zero objective gradient invalidates an equality-of-kernels argument. The current source uses only kernel inclusion and explicitly decomposes `v=(v-dg(v)w)+dg(v)w` with `dg(w)=1`. This proves `df=lambda dg` even when `df=0`. For the review parabola task, `g=y-x^2` has nonzero gradient, while `h=(y-x^2)^2` has zero gradient on the same image. Substitution reduces the distance function to `x^2+x^4`, with global minimum0. This independently supports the task without a regularity theorem for the singular encoding. Protected decision retained.

## Supported judgment: reference appendix scope

Attempted objection: AppendixC's local Jacobian area factor might silently supply the earlier global integral substitution theorem. It cannot: appendices are not preceding reading, and local determinant scaling does not contain integral hypotheses. The worker explicitly keeps those scopes separate. AppendixD/E summaries are checked against their wrapper regularity/orientation conventions, not treated as independent first lessons. No additional confirmed reference finding follows from that objection.

## Rendered spot-check outside this partition

Root opened the rebuilt Section5.2 page and inspected the visible double-cone figure and caption at `c5s2-fig-double-cone-grid-velocities`. The labels use ordinary grid velocities `v,w` and normal `N`, with a collapsed vertex and the caption's scaling qualification. The nearby definition visibly links the complete tangent-plane justification to Theorem15.1.10 and keeps map regularity distinct from image singularity. This current-run check is limited to that figure/subsection; it does not certify all graphics or regenerated assets.
