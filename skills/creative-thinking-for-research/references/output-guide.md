# Hypothesis cards and example

Adapt these fields to the requested format. They are a completeness aid, not mandatory headings for every response.

## Compact card

- **Research question:** the specific unknown.
- **Reframing:** the assumption changed and why it matters.
- **Mechanism:** the proposed intervention and expected causal link.
- **Prediction:** an observable difference from a rival account.
- **Probe / disconfirmation:** the smallest comparison and what would weaken the idea.
- **Evidence status:** supplied observation, verified source, or hypothesis; state unverified literature status once when it applies to all cards.
- **Feasibility:** fit with the user's actual resources.

For an analogy, add a short source-to-target mapping and its break point. For several candidates, compare mechanisms and decisive uncertainties rather than assigning unsupported decimal scores.

## Worked example — hypothetical, not a research result

**User context:** An existing document QA system retrieves many near-duplicate passages. The user has one workstation and wants a fresh direction without training a foundation model. Assume the duplication observation is supplied by the user; no literature search has been performed.

**Reframing:** Move from ranking passages individually to allocating a fixed evidence budget across distinct claims.

**Mapping:** Portfolio diversification concerns correlated contributions to a whole. Here, passages are candidate evidence items and overlapping claims are a possible proxy for redundant contributions. The analogy breaks if textual overlap poorly represents evidential dependence.

**Hypothesis:** A selection rule that penalizes redundant claim coverage may preserve more complementary evidence at a fixed context length.

**Rival explanation:** Any gain could come from shorter passages or ordinary deduplication, rather than the proposed claim representation.

**Probe:** On a small, fixed QA subset with support annotations, compare ordinary retrieval, simple deduplication, and the proposed selection rule at the same token budget and with the same answer model. Inspect coverage and answer correctness separately.

**Disconfirmation:** If simple deduplication performs comparably, or claim extraction errors dominate, the extra representation has little demonstrated value.

**Status:** Conceptual candidate; novelty and effectiveness unverified. A focused search should examine set-based retrieval, diversity-aware retrieval, and evidence selection before treating this as a contribution.

## Single-idea and offline requests

For “develop this one idea,” provide alternative formulations of that mechanism only as needed; do not replace it with a catalogue of unrelated projects. For “do not browse,” work from the supplied material and label novelty unverified. A proposed experiment remains a proposal until execution is requested.
