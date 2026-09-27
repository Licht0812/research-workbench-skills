---
name: ccf-conference-colors
description: "Select and audit scientific figure colors for CCF-listed venues. Use for 论文配色、跨图颜色一致性、对比度与灰度检查; preserve existing data and plotting source."
license: "See LICENSE and assets/palette-licenses/NOTICES.md"
---

# CCF Conference Colors

Make scientific comparisons readable in the actual conference template. CCF identifies venues, not a universal official palette. Use the specified venue, year, track, and final figure size; if they are unknown, deliver a provisional color specification and identify the remaining layout check.

## Workflow

1. Read the existing figure source, data semantics, and any established method-to-color mapping. Identify nominal categories, ordered magnitudes, signed deviations, or cyclic quantities. Preserve values, scales, uncertainty definitions, and group identities.
2. Choose the smallest suitable palette using [the selection guide](references/palette-guide.md). Reuse an existing adequate mapping. Prefer a restrained categorical set for methods, a perceptually ordered map for magnitudes, a justified neutral center for signed differences, and a cyclic map only for periodic data. Do not recolor factual images or scientific pseudocolor layers without understanding their meaning.
3. Freeze explicit labels, HEX values, non-color cues, background, missing-data treatment, and normalization in one project color contract. Keep each method's identity across panels and papers' main/supplementary figures. The [contract example](assets/color-contract.example.json) is illustrative, not a required global palette. Never remap colors according to result rank.
4. Apply the contract in the current authoring source. Pair color with useful line styles, sparse markers, direct labels, or region boundaries when comparison needs them. Use neutral text and restrained highlighting; visual emphasis must not exaggerate the evidence. Color-only requests need no new plotting stack.
5. Run the bundled contrast/grayscale diagnostics where useful, then inspect the rendered figure at its destination size, including grayscale. Treat reported CVD metadata as source evidence; actual CVD simulation is a separate check. Use [the conference checklist](references/conference-checks.md) for venue-specific verification and honest pass/fail reporting.

## Local tools

All paths below are relative to this skill folder. Python 3.9+ is sufficient for palette selection, auditing, and the offline gallery; no network, GPU, sibling skill, or full easyplot installation is needed.

```sh
python3 scripts/ccf_palette.py list --kind qualitative
python3 scripts/ccf_palette.py show tol.bright --n 3
python3 scripts/ccf_palette.py audit tol.bright --n 3 --role marks
```

Import `scripts/easyplot_palettes.py` for exact palette selection; optional `easyplot_cmap` requires the project's installed Matplotlib. See [usage examples](references/usage.md). Runtime dependency installation is not part of ordinary palette selection.

## Deliverable and boundaries

Return the selected palette and rationale, explicit label-to-color mapping, necessary non-color cues, updated source or requested exports, and what was actually checked. A suggestion-only task can end with a concise specification; an applied figure task needs rendered inspection. Do not claim CCF certification, universal color-vision accessibility, completed simulation, or checked PDF output without evidence.

Own colors within the existing visual workflow. Academic Plotting or another chosen renderer may own chart construction; this skill remains usable alone and does not invoke another skill automatically. It does not create research results, choose statistical tests, rewrite manuscripts, execute training, or generate images with a generative model.

The bundled 205-palette subset retains source-specific licenses and provenance. See [NOTICE](NOTICE.md) and [palette notices](assets/palette-licenses/NOTICES.md) before redistribution.
