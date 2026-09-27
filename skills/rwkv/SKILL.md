---
name: rwkv
description: "Implement or evaluate RWKV recurrent-state models and streaming inference. Use for RWKV 架构、状态管理与流式序列 using the matching model generation."
license: "MIT"
---

# RWKV

Own RWKV-specific model and state semantics; preserve the requested RWKV generation and checkpoint.

## Workflow

1. Match checkpoint generation, tokenizer, state format, precision, kernels, and runtime before proposing code.
2. Create a small batched or streaming baseline, with explicit state initialization, update, reset, and serialization.
3. For training, define sequence boundaries, state carry policy, truncated backpropagation if applicable, and validation splits.
4. Compare chunked and unchunked processing under matching settings; evaluate memory use and long-range information retention separately.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Version-matched model/state implementation, state lifecycle description, and task-specific efficiency and quality comparisons.
