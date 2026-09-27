# LangSmith: decisions and validation

## Decision points

- Avoid double auto-instrumentation through framework integrations and manual wrappers; it can duplicate spans and distort latency.

- Model-based evaluators need sampled human/source checks; a single judge score does not establish scientific validity.

- Use the existing authorized endpoint and trace mode; do not silently upload raw research data or credentials.

## Verify the requested change

- A known tool failure appears in the correct trace and is not converted into an apparent success.

- Dataset example IDs, reference outputs, and evaluated versions remain aligned.

- Traces and evaluator results have distinct meanings and reproducible links.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [LangSmith documentation](https://docs.langchain.com/langsmith)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/17-observability/langsmith/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
