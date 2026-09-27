---
name: long-context
description: "Design and evaluate context extension with supported positional methods such as RoPE scaling or YaRN. Use for 长上下文扩展; kernel speedups alone are insufficient."
license: "MIT"
---

# Long Context

Own position/context changes, continued-training choices, and length-dependent evaluation.

## Workflow

1. Inspect the model's actual positional scheme, original context, config schema, tokenizer, attention implementation, and checkpoint compatibility.
2. Select a method compatible with that architecture; specify which weights/configuration change and whether continued training is needed.
3. Use a staged length curriculum or controlled comparison appropriate to the task, budgeting activations and KV cache as well as parameters.
4. Evaluate both short-context regression and long-range tasks at multiple lengths and evidence positions.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Size model states, batches, parallelism, and concurrent workloads from the project's actual memory, interconnect, and compute allocation; verify a representative configuration before scaling.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Position/config change, training rationale, length/position evaluation matrix, and measured resource costs.
