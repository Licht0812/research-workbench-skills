# Ten ideation lenses

Select the lenses that reveal different aspects of the user's problem. These are practical heuristics inherited and adapted from the upstream skill, not a guarantee of high-impact research.

| Starting point | Useful lenses |
|---|---|
| Broad topic, no research question | Problem orientation; tensions; stakeholder rotation |
| Strong system, unexplained failure | Boundary probing; decomposition; simplicity |
| New tool looking for a use | Problem orientation; changed assumptions |
| Results without a general explanation | Abstraction ladder; clarity test |
| A promising idea that feels incremental | Structural transfer; tensions; composition |

## 1. Problem-first and capability-first

For a problem, identify who or what is affected, the failure condition, and its consequence. For a new capability, identify a real bottleneck it could change and why a simpler tool cannot already do so. A useful contribution may improve understanding rather than serve a product user.

**Artifact:** problem → consequence → candidate mechanism → unresolved assumption.

## 2. Abstraction ladder

Move from a concrete case to a general relation, then back to a testable instance. Explore an adjacent domain only if the relation survives the move.

**Artifact:** specific failure, proposed principle, scope boundary, and concrete probe. Do not generalize from a single observation without marking the generalization as a hypothesis.

## 3. Tensions and tradeoffs

Identify two desired properties and the assumptions making them conflict. Ask whether the tradeoff is empirical, a consequence of current implementation, or a formal limitation. A better characterization of the boundary may itself be useful.

**Artifact:** joint objective, source of tension, changed condition, and a way to measure both properties fairly.

## 4. Structural cross-pollination

Describe the target problem without domain-specific labels. Find a source mechanism with matching relationships. Map entities, dependencies, and interventions, then name the assumption that fails to transfer.

**Artifact:** source mechanism → target intervention → discriminating prediction. “X is like Y” without operational consequences is insufficient.

## 5. What changed?

Revisit an old limitation only after identifying the prerequisite that may have changed: accessible data, hardware, theory, deployment conditions, or tooling. Verify current facts before relying on them.

**Artifact:** earlier obstacle, dated enabler or explicit assumption, remaining obstacle, and newly feasible question. A new model name alone does not establish a research opportunity.

## 6. Failure and boundary probing

Select one implicit assumption about distribution, scale, composition, time, or operating conditions. Vary it in a controlled way and propose competing explanations for failure.

**Artifact:** assumed regime, boundary violation, failure mechanism, and a comparison that could distinguish causes. Avoid presenting a known limitation as an undiscovered gap.

## 7. Simplicity test

Construct the smallest credible explanation or baseline. Compare under matched resources, preprocessing, and tuning opportunity. Additional components need an identifiable role; removing them is an intervention, not merely a styling choice.

**Artifact:** simplest alternative, reason complexity might matter, and the observation that separates the accounts.

## 8. Stakeholder rotation

View the problem through relevant users, operators, developers, scientists, or other affected groups. Select perspectives that change the question; do not perform every role as a ritual.

**Artifact:** overlooked failure, affected group or scientific objective, and an observable consequence. Confirm whether the claimed need is supplied, sourced, or hypothesized.

## 9. Composition and decomposition

For a combination, identify a necessary interaction between components and what capability it should enable. For a decomposition, isolate which component or information source is causing the observed behavior.

**Artifact:** interaction hypothesis or bottleneck hypothesis, comparator, and a removal/replacement intervention. “A + B” without an interaction account is only a recipe.

## 10. Two-sentence clarity test

State the problem and consequence in one sentence. State the proposed mechanism and expected reason it addresses the problem in another, using conditional wording for untested effects.

**Artifact:** a clear pitch plus the uncertainty that remains. Clarity is a communication check, not proof of significance, novelty, or likely acceptance.
