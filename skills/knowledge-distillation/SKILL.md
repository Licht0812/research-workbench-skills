---
name: knowledge-distillation
description: "Design teacher-student distillation from accessible responses, logits, or representations. Use for 知识蒸馏、小模型能力迁移 and controlled teacher comparisons."
license: "MIT"
---

# Knowledge Distillation

Own the distillation objective, teacher/student alignment, and compression-quality comparison.

## Workflow

1. Identify teacher access, student architecture, tokenizer/output space, target task, data rights, and resource budget.
2. Choose response, logit, or representation distillation according to available teacher outputs; specify temperature, masking, and any supervised loss.
3. Check the objective on a small batch, freeze the teacher unless explicitly training it, and separate synthetic-data generation from student updates when useful.
4. Evaluate held-out task quality, calibration or validity where relevant, and actual student inference cost against the starting student and teacher.

Check version-sensitive APIs against the installed project or its pinned official source. Report validation actually performed and any unresolved runtime checks.

Budget teacher inference, student training, cached outputs, and evaluation together; make teacher/student concurrency explicit.

Read [the workflow reference](references/workflow.md) when implementation decisions or validation details are needed.

## Deliverable

Teacher/student contract, loss implementation, data provenance, and quality/efficiency comparison.
