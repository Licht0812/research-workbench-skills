# Conference adaptation and final-size review

Reviewed 2026-09-27. The CCF recommended-venue list is not a figure-color specification. A target such as “CCF A” is insufficient to determine column width, typography, anonymization, accessibility text, or export rules. Read the actual venue/year/track instructions and the supplied manuscript template; its rules take precedence over this skill's defaults.

## Apply the actual template

1. Record venue, year, track, review/camera-ready stage, and the current official author-instructions URL. For an unspecified venue, make the palette usable now and leave exact layout checks explicitly provisional.
2. Read the destination `\columnwidth` or `\linewidth` for a single-column figure and `\textwidth` for a spanning figure. Use the actual measured width, not one purported universal “CCF width.” Match the surrounding type and verify text after scaling into the manuscript.
3. Preserve a single project color contract. For multi-panel comparisons, hold shared series, normalization, and colorbar limits fixed unless a justified exception is labeled.
4. Inspect a rendered export at actual size: colored strokes on their background, labels on fills, touching areas, confidence bands, legend keys, dense crossings, and clipping. Check grayscale; add useful non-color cues where necessary. A checked swatch sheet alone does not establish that the final paper figure is readable.
5. Export a vector PDF/SVG when supported by the destination and appropriate to the content; preserve editable source. For raster content, verify the venue's current resolution requirements. Check embedded fonts and the compiled manuscript when those tools are available. Do not silently turn a requested vector result into a bitmap.
6. Provide an informative caption and figure description where the venue requires it. Describe the scientific relationship and labels rather than relying on “the red curve.” Document any unperformed check.

## Primary guidance and its limits

| Source | What it supports here |
|---|---|
| [CCF category list](https://www.ccf.org.cn/Academic_Evaluation/By_category/) | Identifying a venue/category; not certifying any palette. |
| [ICML 2026 author instructions](https://icml.cc/Conferences/2026/AuthorInstructions) | Use the year's style file; vector experimental plots and accessibility review are encouraged in its camera-ready instructions. Verify later years afresh. |
| [CVPR 2026 author guidelines](https://cvpr.thecvf.com/Conferences/2026/AuthorGuidelines) | Its own official template controls paper formatting, including figures and tables. No generic CCF format is substituted. |
| [ACM DIS 2023 accessible figures guide](https://dis.acm.org/2023/creating-accessible-figures-and-tables/) | Practical guidance on accessible figures and descriptions; this historical guide is not a claim about every current ACM venue's submission rules. |
| [W3C text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) and [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) | 4.5:1 ordinary text and 3:1 relevant graphical contrast are useful screening references. Applicability depends on geometry and context; these are web-accessibility criteria, not a CCF paper acceptance test. |

## Reporting a result

State the selected palette ID and any chosen subset; label-to-HEX mapping; method-specific line/marker cues; background and missing-data color; scale limits, transform and center; actual venue/size if known; rendered exports inspected; diagnostic findings and their treatment. Mark CVD simulation, grayscale viewing, PDF/font review, and manuscript compilation separately as completed, unavailable, or not requested. Do not collapse them into an unsupported “all accessibility checks passed.”
