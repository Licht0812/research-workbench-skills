# LlamaIndex: decisions and validation

## Decision points

- Embedding model or chunking changes can require a new index; version those choices instead of mixing incompatible vectors.

- A vector-store client such as Qdrant supplies persistence/search; LlamaIndex supplies ingestion/query logic. Choose one owner for each operation.

- Answers should distinguish retrieved support from unsupported inference; absent evidence is not evidence of absence.

## Verify the requested change

- A returned citation resolves to the actual supporting source span.

- Filtering, updates, and deletion affect retrieval as intended.

- Retrieval recall and grounded-answer quality are assessed separately.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [LlamaIndex documentation](https://docs.llamaindex.ai/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/14-agents/llamaindex/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
