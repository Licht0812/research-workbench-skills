# Research options and first investigation

Use the amount of structure needed for the user's decision. All experimental examples below are proposals, not measured results.

## Several directions

Start with the research objective and binding constraints. A comparison can use:

| Direction | Problem and mechanism | Distinguishing prediction | Feasibility | Main uncertainty |
|---|---|---|---|---|

Then explain a conditional preference in prose. Develop the preferred option with:

- A two-sentence problem/insight statement.
- The nearest approaches that need comparison, with verified citations only when inspected.
- The smallest probe: data/setup, comparator, controlled variables, and observation.
- A confound and a result that would weaken the hypothesis.
- A next decision: proceed, revise, or stop under specified observations.

## One existing idea

Keep the user's mechanism fixed unless they invite alternatives. Improve the causal account, identify the simplest rival, narrow the scope, and propose a discriminating initial investigation. Do not convert development into an unsolicited accept/reject review.

## Worked example — hypothetical opportunity map

**Context:** The user reports that a document QA system becomes less reliable as redundant retrieved passages accumulate. They have an existing model endpoint, a fixed evaluation set, and one week. They want conceptual options, without browsing or model training.

| Direction | Mechanism | Prediction | Main risk |
|---|---|---|---|
| Evidence diversity | Select complementary passages under a fixed token budget | Support coverage improves especially for questions requiring multiple facts | A simple deduplication baseline may explain the gain |
| Conflict detection | Detect incompatible claims before answer generation | Improvements concentrate on conflicting-evidence examples | Detection errors may discard useful evidence |
| Evidence ordering | Place relevant support where the answer model can use it consistently | Reordering the same content changes outcomes | Effects may be specific to the selected model |

**Conditional preference:** Start with evidence diversity if redundancy is the dominant observed failure. Start with conflict detection if errors cluster around inconsistent sources. This recommendation depends on the user's reported error distribution.

**First probe:** Use a fixed subset, identical answer model, and matched context budgets. Compare ordinary retrieval, simple deduplication, and diversity-aware selection. Separate support coverage from answer correctness, and inspect changed answers for confounds. If simple deduplication matches the more complex method, revise the proposed contribution.

**Evidence status:** All three are hypotheses; the supplied failure observation is not independently verified. Literature novelty is unverified because this example is intentionally offline. No experiment has been run and no gain is claimed.
