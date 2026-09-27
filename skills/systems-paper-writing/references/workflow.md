# Systems Paper Writing: decisions and validation

## Decision points

- Training or inference systems need matched hardware, software, precision, batch/workload, and correctness conditions before comparing performance.

- Separate latency from throughput, include appropriate tail/variance information, and explain measurement boundaries, warmup, caching, and concurrency.

- Experiments support claims at their measured scales. Distinguish measured hardware scaling from extrapolation or simulation forecasts, whatever the cluster size.

## Verify the requested change

- Each systems claim points to a design mechanism and supporting measurement or a clearly labelled proposal.

- Baseline tuning and resource accounting support a fair comparison.

- The prose distinguishes implemented behavior, proposed extensions, and actual measured results.

Run only checks relevant to the change. Distinguish a proposed configuration, a successful smoke check, and a completed scientific evaluation. Do not turn an upstream benchmark or example into a measured result of the current task.

## Primary references

Use the documentation matching the chosen software/model revision. Links are starting points, not a pinned universal dependency set.

- [USENIX conferences](https://www.usenix.org/conferences)
- [ACM SIGOPS](https://www.sigops.org/)

Lineage: [reviewed upstream skill](https://github.com/Orchestra-Research/AI-Research-SKILLs/blob/773a52944ba4747a18bd4ae9ade53fff041adcbc/20-ml-paper-writing/systems-paper-writing/SKILL.md). This adaptation replaces the upstream entrypoint and includes the operational reference needed for standalone use.
