# Behavioral evaluation

These **89 optional maintenance cases** provide task prompts and observable acceptance checks. Their original prompts, checks, identifiers, and follow-up inputs are retained.

## What a behavioral case is

A case is a task prompt plus observable acceptance checks. For example, a prompt may ask for colors for a signed-error heatmap, and the checks ask whether the answer uses a meaningful diverging center, distinguishes missing data, and preserves supplied values. A maintainer can run the task after changing a skill or model and compare the actual output with those checks.

Each evaluation examines how the assistant uses a skill to complete the task.

## Use in maintenance

Maintainers choose and run cases when evaluating a change. Daily skill use follows `SKILL.md` and its local references; these cases remain repository-level maintenance materials. The copy tool leaves `evals/` in the source repository for single-skill, category, and all-skill selections.

If the published set of cases changes, update the case counts and documentation links. A case may check a requirement from a skill; the corresponding `SKILL.md` or reference remains the source of that requirement.

## Evaluation status

As of 2026-09-27, the 89 cases have been checked for valid definitions. Their execution status remains `not_run`.

| Evaluation | Status |
|---|---|
| Behavioral model runs and host routing | Not run |
| GPU training, robot execution, and weight downloads | Not performed |
| Package copying and independent use of bundled tools | Tested in temporary folders |

Completed release checks are recorded in the [changelog](../CHANGELOG.md). Record future model and runtime results separately with the source revision, host/model, inputs, environment, observed outputs, and conditions needed to interpret them.

## Included optional cases

- `cases.jsonl`: 16 original ideation cases.
- `technical-cases.jsonl`: 61 cases: one task for each of the 43 technical/writing additions and 18 cross-skill/edge cases, including large-cluster planning without a fixed card-count ceiling.
- `color-cases.jsonl`: 12 color-semantics, mapping, conference-template, evidence, and workflow-boundary cases.

## Definition format

Each non-empty JSONL line contains one object using this repository's schema version 1:

| Field | Type and meaning |
|---|---|
| `schema_version` | Integer `1`, identifying this repository's definition format |
| `id` | Non-empty identifier unique across all case files |
| `skills` | Array of expected skill names; empty for a negative-routing case |
| `available_skills` | Optional candidate skills to expose; required when `skills` is empty |
| `prompt` | The task given to the model |
| `checks` | Non-empty array of observable acceptance criteria |
| `execution_status` | `not_run` in definitions; actual runs are recorded separately |
| `tools` | Optional text describing tool availability |
| `follow_up` | Optional subsequent user message for a multi-turn case |

The schema uses `skills` arrays throughout. The two negative-routing cases have empty target arrays and expose the two ideation skills as candidates; their expected outcome is that neither skill is invoked. The original task content and criteria are preserved.

```sh
python scripts/validate_evals.py
```

This command checks all 89 definitions for valid fields, duplicate IDs, and available target skills. CI runs the same format check. Model execution and its results are recorded separately through the evaluation process below.

## Run a case

Use the target host/model with the required skill directory, realistic minimal raw inputs, and a disposable workspace. For standalone evaluation, omit all sibling skills. For routing evaluation, expose the relevant overlapping skill metadata and an existing project context.

Run the actual task. Record the model, date, tool access, input artifacts, selected skill(s), observed response or output files, side effects, and a pass/fail/partial judgement for each semantic check. Do not supply a desired answer as user context. Keep live accounts, unrelated files, costly training, and hardware actuation outside a test unless specifically authorized.

A case may require a small fixture or mocked tool interface. Assess planning from the proposed plan and execution from observed runtime results. Instantiate broad technical cases with the chosen project's concrete data and software environment.

## What to inspect

Evaluate scope preservation, backend/owner selection, source and evidence fidelity, standalone completeness, resource accounting, and the requested artifact. For code, run meaningful small checks when feasible. For real GPU execution, separately record hardware, software revision, dataset, observed memory, and quality metrics.

The boundary cases cover duplicate trainers, aggregate GPU budgets, incompatible environments, scientific text/plot ownership, retrieval layers, unsafe benchmark execution, unavailable teacher logits, agent-level versus weight-level improvement, VLA normalization, and other concrete failure modes.

Store actual evaluation results separately from case definitions, with a judgement supported by the observed output for each check.
