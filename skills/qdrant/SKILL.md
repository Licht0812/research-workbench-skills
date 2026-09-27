---
name: qdrant
description: "Configure Qdrant vector collections, payload indexes, filters, updates, and retrieval evaluation. Use for Qdrant 向量服务与持久化."
license: "MIT"
---

# Qdrant

Own Qdrant's collection schema and persistence/search contract; leave embeddings and agent orchestration to their existing components.

## Workflow

1. Identify deployment mode, client/server versions, embedding dimension/metric, named-vector schema, IDs, and payload fields.
2. Create a small collection and validate upsert, filtered queries, update, deletion, and source metadata.
3. Add payload indexes or hybrid retrieval only for actual query patterns; benchmark recall and latency against a suitable reference.
4. Document persistence, snapshot/restore or migration behavior, and how embedding/schema changes are versioned.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Collection/index configuration, CRUD/query code, retrieval tests, and persistence/migration notes.
