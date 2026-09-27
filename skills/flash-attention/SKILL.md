---
name: flash-attention
description: "Integrate and benchmark PyTorch SDPA or flash-attn kernels. Use for FlashAttention、注意力显存与吞吐优化 with numerical equivalence checks."
license: "MIT"
---

# FlashAttention

Own the attention-kernel change and its measured comparison, preserving the model's masking, position, and dropout behavior.

## Workflow

1. Identify attention layout, dtype, GPU, PyTorch/CUDA version, masking, dropout, grouped-query heads, and variable-length requirements.
2. Prefer an existing supported model/SDPA integration before adding a compiled extension; verify the backend actually selected.
3. Compare outputs and, for training, gradients against a suitable reference across representative shapes and masks.
4. Benchmark warm runs at matched batch/sequence length with synchronization, peak memory, and end-to-end context.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Benchmark representative sequence lengths, head dimensions, dtypes, and device architecture under the actual memory budget.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Minimal integration change, compatibility constraints, numerical checks, and a reproducible benchmark.
