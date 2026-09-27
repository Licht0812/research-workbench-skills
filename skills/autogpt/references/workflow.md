# AutoGPT: decisions and validation

## Decision points

- Platform and Classic are different implementations; verify the matching setup and component model.

- Persistent agents need an explicit trigger, resource budget, stop/cancel path, and treatment of duplicate events.

- A workflow that sends messages or changes external systems needs task authorization for those actions; creating a graph is not that authorization.

## Verify the requested change

- Retries do not duplicate non-idempotent tool effects.

- Secrets are configured outside graph exports and logs.

- The workflow reaches success or a visible failure state within its configured limits.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Significant-Gravitas/AutoGPT](https://github.com/Significant-Gravitas/AutoGPT)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/14-agents/autogpt/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
