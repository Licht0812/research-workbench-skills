# Creative operators

Use selected operators to change a specific bottleneck. These are ideation heuristics, not evidence that a resulting hypothesis is novel or correct. The names retain the upstream conceptual lineage; the procedures below are practical adaptations.

| Blockage | Useful operators | Desired change |
|---|---|---|
| Repeating the same architecture tweak | Reformulation; constraint manipulation | Change the problem representation or the adjustable variable |
| All candidates sound alike | Bisociation; structure mapping | Import a different causal mechanism |
| A tradeoff seems unavoidable | Inversion; dialectical synthesis | Expose the assumption or regime creating the opposition |
| A result has no explanation | Abstraction laddering | Identify the broader relation and its boundary |
| A good idea was previously infeasible | Adjacent possible | Verify which prerequisite has actually changed |

## 1. Bisociation: combine mechanisms

Identify a target bottleneck and a small number of mechanisms from another field. Pair mechanisms with target operations, rather than taking the Cartesian product of domain buzzwords. Ask what state, signal, or decision would change in the target system.

**Produce:** a candidate intervention and the interaction that makes the combination useful.

**Reject:** a renamed existing component, an analogy without implementation consequences, or a combination whose benefit is merely assumed.

## 2. Reformulation: change the problem statement

Vary one representation at a time: objective, unit of prediction, granularity, formalism, timescale, or decision-maker. For example, changing from selecting individual passages to selecting a set introduces redundancy and coverage as explicit relationships.

**Produce:** old formulation, new formulation, what becomes easier to express, and what information the new formulation loses.

**Check:** the new objective still addresses the user's original need; changing the metric alone can conceal failure.

## 3. Structure mapping: transfer relationships

Describe the source mechanism accurately before borrowing it. Map entities, relations, feedback, and assumptions into the target. Choose the most informative match, regardless of how far apart the field names sound.

| Mapping element | Question |
|---|---|
| Entities | Which target objects correspond to the source objects? |
| Relationship | Which dependency, conservation property, or feedback rule transfers? |
| Intervention | What concrete operation changes in the target? |
| Prediction | What differs from a plausible baseline if the mapping is useful? |
| Break point | Which source assumption is absent in the target? |

**Produce:** a prediction that follows from the mapping and a condition under which it fails.

## 4. Constraint manipulation: expose conventions

Classify restrictions as hard, user-imposed, or conventional/hidden. Tighten, relax, or replace a conventional restriction and examine the resulting mechanism. A budget imposed by the user remains binding for recommendations.

**Produce:** the original constraint, its status, the alternative, and the cost of changing it.

**Check:** removing a resource limit in a thought experiment is not a feasible solution under that limit.

## 5. Negation and inversion: test the opposite premise

Write the assumption precisely, negate it, and construct the most coherent system allowed by that negation. Possibilities include delaying a decision, moving computation offline, reversing the direction of inference, or treating errors as observable signals.

**Produce:** an alternative mechanism plus a regime where it could help and a regime where it should hurt.

**Check:** a familiar opposite is not automatically new; verify prior work before novelty claims.

## 6. Abstraction laddering: change the level

Generalize a concrete effect into a relationship, then specialize it into a tractable case. Keep the assumptions needed at each level explicit. Use a counterexample to prevent an attractive generalization from becoming an unsupported universal claim.

**Produce:** concrete observation → proposed principle → boundary condition → probe.

**Check:** a conceptual unification needs explanatory or predictive value beyond new terminology.

## 7. Adjacent possible: revisit a changed prerequisite

Identify the original obstacle and the proposed enabling change. Verify the change, its date, accessibility, and resource requirements when presenting it as current fact. Ask which part of the old argument stops applying.

**Produce:** previous limitation, verified or explicitly assumed enabler, newly feasible experiment, and remaining dependency.

**Check:** vendor announcements do not establish access, reliability, cost, or scientific benefit. Avoid fixed year-based lists of supposedly current capabilities.

## 8. Dialectical synthesis: locate the tradeoff

State the two goals and the assumptions under which they conflict. Explore separation across regimes, timescales, components, or information conditions. A useful result may be a clearer impossibility boundary rather than achieving both goals.

**Produce:** the tension, the changed assumption, a conditional mechanism, and a joint measurement of both goals.

**Check:** do not claim to bypass mathematical lower bounds, the CAP theorem, or information-theoretic limits. A changed loss criterion or operating regime must be explicit.
