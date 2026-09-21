# Reference partition findings

Snapshot `9a9d110af839b539fe598de66ecc4320a4126af4`, branch `main`. Audit only: Chapter 9, Appendices A–E, their wrappers and the main/front/backmatter route. Primary source reading was completed before consulting old dispositions. These are two root causes with three primary assessment occurrences. No P1 prerequisite blocker was established in this partition. Independent challenge remains pending.

## REF-01 — Two checkpoints omit the nonzero defining-gradient condition

- **Category / priority:** H, with a local B aspect; P2. This is an underqualified assessment, not an absence of the underlying theory.
- **Status / confidence:** confirmed local observation; high confidence in the counterexamples, medium-high in classifying the brief checkpoint omissions as defects rather than inferred contextual hypotheses.
- **Occurrences:** `source/chapters/ch09-gradient-optimization/sections/sec-9-the-gradient-and-level-sets.xml:255–273`, `checkpoint-9-1-gradient-normal-tangent-plane`; and `source/chapters/ch09-gradient-optimization/sections/sec-9-constrained-optimization-and-lagrange-multipliers.xml:168–184`, `checkpoint-9-5-gradients-parallel`.
- **Faithful excerpts:** “Why does that force … to be a normal vector to the whole surface”; “on a smooth curve, why must … be parallel”. Neither checkpoint states that the defining gradient is nonzero.
- **Required capability:** distinguish a smooth geometric level set from a regular defining function, and distinguish an orthogonal zero vector from a usable normal direction.
- **What is available:** Chapter 8 gives the regular implicit-function statements (`c8s6-thm-ift-plane-curve:382–411`, `c8s6-thm-ift-surface:413–433`) and explicitly warns at `c8s6-why-the-hypotheses-matter:536–541` that `(y-x)^3=0` is a smooth line despite a zero gradient. The chain rule (`c8s1-thm-chain-rule-curve:199–247`) proves annihilation of tangent directions. In Chapter 9 the corresponding surface theorem at `304–325` and the multiplier paragraph/theorem at `186–241` restore the missing nonzero conditions, after the affected checkpoints.
- **Search and support disposition:** all Chapter 9 text, hints, examples, tables, graphics source and review tasks were read; the cited Chapter 8 sources were also read. Thus this is not a negative keyword-search claim. Earlier support actually teaches why smoothness of the set alone is insufficient.
- **Witness / counterexample:** take `F(x,y,z)=z^2` and level `F=0`. Its set is the smooth plane `z=0`, but `grad F=0` on it. Being perpendicular to every tangent direction cannot select a normal vector or determine the tangent plane through `grad F dot displacement=0` (which becomes `0=0`). For the multiplier checkpoint, set `g(x,y)=(x^2+y^2-1)^2`, `f(x,y)=x`. The constraint `g=0` is the smooth unit circle and `(1,0)` is its maximum for `f`; `grad g(1,0)=0` and `grad f(1,0)=(1,0)`, so no scalar multiplier exists.
- **Minimal repair:** add “Assume the defining function is C1 near p and its gradient at p is nonzero” before each checkpoint’s question (and make the adjoining general explanatory sentences share that scope). The first hint should say the tangent directions span a plane for a regular smooth level surface. Retain both later theorem statements and the counterexamples already taught.
- **Downstream impact:** reread the two hints, `c9s7-cc-gradient-normal`, `c9s7-cc-tangent-plane`, `c9s7-cc-constrained-condition`, the existing singular-representation exercise `c9s7-sk-parabola-constraint`, and decision-tree figure `fig-c9s7-decision-path`. The figure already says “Regular constraint”; retain it. No new lesson or relocation is needed.
- **Verification:** both squared-defining-function counterexamples must now fall outside the checkpoint hypotheses. The ordinary ellipsoid and circle examples must remain usable. Keep the distinction between singular representation and singular geometric set.
- **Prior relation:** residual scope omission following M04/M05 and the old Chapter 9 “no new defect” coverage dispositions. The kernel proof and the repaired parabola task are correct; this finding does not reopen them.

## REF-02 — The endpoint hint attributes failure to a missing tangent

- **Category / priority:** G/H; P2.
- **Status / confidence:** confirmed local observation; high confidence about the mathematical distinction, medium-high that the suggestive hint needs correction.
- **Source:** `source/chapters/ch09-gradient-optimization/sections/sec-9-warning-examples.xml:170–186`, `checkpoint-9-6-multiplier-misses-boundary`, especially hint `179–184`.
- **Excerpt:** “it needs a well-defined tangent direction … Ask yourself whether such a direction exists where the allowed set simply stops.”
- **Required capability:** apply the interior-extremum premise of one-variable Fermat along the feasible curve, distinguishing two-sided and one-sided feasible motion.
- **Available support:** the immediately preceding example (`c9s6-multiplier-misses-endpoint:134–168`) has `f=x` on a horizontal line segment. `c9s2-thm-fermat:229–262` and the source’s boundary examples already identify the interior-point condition. No new manifold or tangent-cone theory is needed.
- **Witness:** the segment `r(t)=(t,0)`, `-1<=t<=1`, has the same well-defined tangent line at both endpoints as in its interior. Its smooth extension has derivative `(1,0)` there. Yet `f(r(t))=t` attains an endpoint maximum at `t=1` while its derivative is `1`. The missing hypothesis is an interior point of the feasible parameter interval, where motion is possible in both tangent directions. Corners may add a separate nonunique-tangent issue.
- **Minimal repair:** replace the hint with: “The zero-derivative argument uses an interior point of the feasible curve, so motion in both tangent directions is allowed. At an endpoint only one side is feasible. Why can a one-sided maximum have a nonzero derivative? At a corner, examine the boundary pieces separately.”
- **Downstream impact:** align `c9s7-cc-endpoints-corners` and `c9s7-sk-segment` with this explanation. Keep the already correct worked segment example and endpoint checking in the optimization checklist.
- **Verification:** a student’s answer must explain the horizontal segment example without claiming its tangent disappears at the endpoint. The multiplier theorem’s C1/nonzero-gradient hypotheses alone do not remove a separately imposed segment endpoint restriction.
- **Prior relation:** newly identified within a section previously marked protected/no defect. This does not contradict the old valid conclusions about the multiplier equation or endpoint values.

## Editorial observations outside the defect count

`source/frontmatter.ptx:20–24` still contains a visible placeholder preface. The actual reader contract at `29–43` is present and was used. The placeholder is not evidence of an unspecified mathematical prerequisite.

The restated EVT in `c9s5-thm-extreme-value` omits “nonempty”, present in the earlier supplied theorem `c6s4-thm-extreme-value-theorem`. Restoring that word is a small scope cleanup; no assessed task in Chapter 9 uses the empty set. Appendix C’s local density formula is not, by itself, a claim of global substitution over a multiply covered region, so it is not reported as a new integration-theorem gap.
