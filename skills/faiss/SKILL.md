---
name: faiss
description: "Build, benchmark, and persist FAISS vector indexes with matched metrics and IDs. Use for FAISS 近邻检索、召回率与延迟比较."
license: "MIT"
---

# FAISS

Own vector-search index construction and search-quality measurement, not embedding training or agent orchestration.

## Workflow

1. Fix embedding model/version, dimension, dtype, distance metric, normalization, record IDs, and query distribution.
2. Establish an exact Flat baseline on a representative subset before choosing IVF, PQ, HNSW, or a supported GPU index.
3. Train indexes that require fitting on representative training vectors, then add/search with stable external-ID mapping.
4. Measure recall against exact search, latency, index memory, and build cost; verify persistence and incremental-update behavior.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Index implementation/config, embedding/ID contract, exact-baseline comparison, and reload evidence.
