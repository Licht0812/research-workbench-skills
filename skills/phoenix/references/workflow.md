# Phoenix: decisions and validation

## Decision points

- A training run is not a trace span hierarchy; connect run IDs when useful but do not replace the selected training tracker.

- Multiple auto-instrumentors/exporters can duplicate spans. Decide ownership before adding another integration.

- Remote exports must match the user's selected data handling; omit credentials and unnecessary raw inputs from telemetry.

## Verify the requested change

- A representative trace is complete and correctly nested, including error paths.

- Exporter failure does not silently block or corrupt the application workflow.

- Evaluations can be linked to the exact input, retrieved evidence, and output version.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Arize Phoenix documentation](https://arize.com/docs/phoenix)
- [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/17-observability/phoenix/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
