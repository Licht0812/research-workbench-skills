---
name: langsmith
description: "Instrument and evaluate LLM/agent applications with LangSmith traces, datasets, and evaluators. Use for LangSmith 追踪与应用评测; training metrics are separate."
license: "MIT"
---

# LangSmith

Own application trace and evaluation schemas, linking them to a stable application/model version.

## Workflow

1. Identify the selected tracing backend, application framework, data handling mode, and fields needed for diagnosis.
2. Instrument a representative request with parent/child spans, tool inputs/outputs, timing, errors, and version tags, minimizing sensitive payloads.
3. Construct a labelled evaluation dataset with clear task-level metrics and evaluator calibration.
4. Compare changes on the same dataset; separate tracing observations from evaluator judgements and record cost/latency alongside quality.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Instrumentation/evaluation code, trace field policy, dataset/metric definitions, and observed example traces.
