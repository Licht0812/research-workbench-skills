---
name: transformer-lens
description: "Inspect supported models with TransformerLens hooks, activation caches, and controlled patching. Use for TransformerLens 激活修补与回路分析."
license: "MIT"
---

# TransformerLens

Own HookedTransformer-based experiments; keep the original model's behavior and tokenizer alignment as the reference.

## Workflow

1. Confirm model support and any weight conversion, normalization folding, centering, or tokenizer changes introduced by loading.
2. Define clean/corrupted or source/base examples, aligned positions, a behavioral metric, and competing explanations.
3. Cache only needed activations; patch selected locations with controls and repeated examples instead of sweeping every tensor by default.
4. Evaluate intervention effects and robustness; report where the model, conversion, metric, or intervention limits interpretation.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget activation caches and patching batches explicitly; retain only the layers, positions, and examples needed by the experiment.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Hypothesis, aligned example construction, hook configuration, intervention controls, and measured effect with uncertainty.
