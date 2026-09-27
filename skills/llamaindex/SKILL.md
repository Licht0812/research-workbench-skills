---
name: llamaindex
description: "Build LlamaIndex ingestion, indexes, retrievers, query engines, and grounded tools. Use for LlamaIndex 研究资料检索与问答."
license: "MIT"
---

# LlamaIndex

Own source-to-node ingestion and retrieval/synthesis contracts, preserving source identity and citation traceability.

## Workflow

1. Identify source formats, document IDs, updates/deletions, chunking, embedding model, and access/filter requirements.
2. Build a small ingestion/index pipeline and inspect nodes, metadata, embeddings, and citation anchors.
3. Evaluate retrieval separately from answer synthesis; use labelled queries and inspect missed or misleading evidence.
4. Expose the verified query/retrieval component to the selected application, with persistence, refresh, and deletion behavior.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

If this workflow launches local models, GPU tools, or concurrent trials, size and schedule the combined workloads against the project's actual hardware and resource budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Ingestion/query implementation, versioned index contract, source-preserving outputs, and retrieval/synthesis evaluation.
