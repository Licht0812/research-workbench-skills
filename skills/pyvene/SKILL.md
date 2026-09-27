---
name: pyvene
description: "Build causal tracing, activation replacement, or learned interchange interventions with pyvene. Use for pyvene 因果干预、表示交换与干预训练."
license: "MIT"
---

# pyvene

Own declarative pyvene interventions and their source/base alignment; use the selected model's existing implementation where supported.

## Workflow

1. Specify the causal hypothesis, target component, layer, unit or position, source/base pairing, and target metric.
2. Construct an intervention configuration using the installed pyvene API and verify component naming on the actual model.
3. For fixed interventions, compare identity, zero/random, and relevant source interventions as appropriate; for learned interventions, separate fitting and evaluation data.
4. Validate hook lifetime, tensor shape, position alignment, and output effects before a broader sweep.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget intervention activations, retained graphs, and any trainable intervention parameters; restrict caches to the locations needed by the hypothesis.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Intervention specification, controls, paired data rules, and measured causal-test results or executable experiment code.
