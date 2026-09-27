# BigCode Evaluation Harness: decisions and validation

## Decision points

- For n samples and c correct solutions, estimate pass@k as 1 - C(n-c,k)/C(n,k) when n >= k; do not report unsupported k values.

- A harness flag acknowledging code execution is not a sandbox. Keep the execution environment separate from the research workspace.

- Benchmark success does not establish an agent's ability to navigate repositories or validate molecular/material claims; those require separate tasks.

## Verify the requested change

- A known small set of correct, incorrect, and non-terminating programs produces the expected outcomes.

- No task or prompt is silently skipped, duplicated, or contaminated by generated solutions.

- Generation and evaluation artifacts preserve model, task, and run identity.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [bigcode-project/bigcode-evaluation-harness](https://github.com/bigcode-project/bigcode-evaluation-harness)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/11-evaluation/bigcode-evaluation-harness/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
