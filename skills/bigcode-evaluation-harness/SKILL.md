---
name: bigcode-evaluation-harness
description: "Run BigCode Evaluation Harness generation and isolated code scoring. Use for HumanEval、MBPP、pass@k; interactive-agent evaluation is separate."
license: "MIT"
---

# BigCode Evaluation Harness

Own the benchmark protocol and generated-code scoring, separating generation from isolated execution.

## Workflow

1. Pin the harness/task revision, model/tokenizer/chat format, data split, prompt construction, stopping rules, and decoding settings.
2. Generate a small set first; inspect prompt removal, stop tokens, indentation, language, and task ID mapping.
3. Execute generated programs only in a restricted environment with time/resource limits and no unrelated credentials, files, or network access.
4. Aggregate correctness and pass@k with valid sample counts; report failures, exclusions, seeds, and uncertainty.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget inference workers and isolated execution separately; account for decoding memory, sandbox CPU limits, and concurrent samples.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Protocol/config, generated samples, isolated execution results, and correctly computed metrics.
