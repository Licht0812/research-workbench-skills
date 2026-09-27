---
name: moe-training
description: "Implement or study MoE routing, expert capacity, load balancing, and supported expert parallelism. Use for MoE 专家训练与路由实验 within the selected backend."
license: "MIT"
---

# MoE Training

Own the MoE mechanism and its dense-baseline comparison while using one compatible existing training backend.

## Workflow

1. Specify expert count/size, top-k routing, shared experts if any, capacity/drop policy, and the selected implementation.
2. Compute total and active parameter counts separately; budget expert weights, optimizer state, routing buffers, and communication.
3. Validate a small dense-versus-MoE experiment, logging expert utilization, dropped tokens, router entropy, auxiliary losses, and task loss.
4. Introduce expert parallelism only when supported and useful; verify checkpointing and actual throughput at matched comparison conditions.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

MoE/routing implementation, resource and comparison contract, utilization diagnostics, and checkpoint/evaluation evidence.
