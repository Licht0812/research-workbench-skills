# CrewAI: decisions and validation

## Decision points

- Use a flow for deterministic state/event control and a crew where role-based collaboration is materially useful.

- Avoid assigning multiple roles ownership of the same canonical file; name the writer and readers per artifact.

- LLM-based judgement by another role is not independent scientific verification; check against source evidence or executable criteria.

## Verify the requested change

- Every task receives the required predecessor output with a valid schema.

- The workflow can terminate on both success and failure.

- Tool retries and role delegation remain within the configured task and cost limits.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [CrewAI documentation](https://docs.crewai.com/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/14-agents/crewai/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
