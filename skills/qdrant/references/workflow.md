# Qdrant: decisions and validation

## Decision points

- Changing dimensions, metrics, or embedding models requires an explicit collection migration or fresh collection, not silent vector mixing.

- Payload filters should represent the intended data restrictions; test missing/null fields and combined filter logic.

- When LlamaIndex or LangChain supplies an integration, choose one owner for collection creation, writes, and deletes.

## Verify the requested change

- Known points are retrieved or excluded according to vector and filter semantics.

- Updates/deletions do not leave stale records in the application's lookup path.

- Restored state preserves vectors, payloads, IDs, and collection configuration.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [Qdrant documentation](https://qdrant.tech/documentation/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/15-rag/qdrant/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
