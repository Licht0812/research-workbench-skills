---
name: nemo-curator
description: "Build or audit NeMo Curator text, image, video, or audio curation pipelines. Use for NeMo 数据清洗、去重与质量筛选."
license: "MIT"
---

# NeMo Curator

Own data selection and curation decisions, preserving a reversible mapping from source records to outputs.

## Workflow

1. Inspect data schema, source identity, modality, intended task, and existing split/group boundaries.
2. Select compatible quality filters and exact, fuzzy, or semantic deduplication methods; calibrate them on representative samples.
3. Run a small audit recording retained/rejected counts and rejection reasons, including rare but scientifically important strata.
4. Scale the verified stages within the allocation and export curated data plus source IDs, filter versions, and split-preserving provenance.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget concurrent readers, decoding workers, GPU filters, intermediate storage, and output shards for the actual dataset.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Curation pipeline, filter settings, representative audit, and traceable output dataset.
