# FAISS: decisions and validation

## Decision points

- Cosine similarity via inner product requires consistent normalization of both stored vectors and queries.

- Approximate-index parameters trade recall for time/memory; choose from measured task needs rather than a generic billion-vector claim.

- CPU and GPU packages/index features differ. Verify the supported distribution and serialize through an appropriate CPU representation when required.

## Verify the requested change

- Search IDs map back to the intended records after filtering or deletion.

- A small query set matches exact distances/rankings where expected.

- Reloaded indexes reproduce results with the same embeddings and search parameters.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [facebookresearch/faiss wiki](https://github.com/facebookresearch/faiss/wiki)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/15-rag/faiss/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
