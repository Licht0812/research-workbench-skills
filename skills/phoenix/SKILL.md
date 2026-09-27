---
name: phoenix
description: "Configure Arize Phoenix and OpenInference/OpenTelemetry traces and evaluation. Use for Phoenix、LLM/Agent/RAG 可观测性."
license: "MIT"
---

# Phoenix

Own the Phoenix tracing/evaluation integration and its span semantics.

## Workflow

1. Inspect Phoenix, OpenTelemetry, and instrumentation package versions; identify local/self-hosted/remote endpoint and required data fields.
2. Configure one tracer provider/export path per application context using supported integrations.
3. Run a small request with a model call, retrieval, or tool use; inspect span hierarchy, attributes, exceptions, and correlation IDs.
4. Evaluate retrieval or response quality on a labelled set, keeping evaluator configuration and application versions attached.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Exporter/instrumentation setup, trace schema, evaluation protocol, and observed trace evidence.
