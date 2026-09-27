# Choosing colors for scientific comparisons

Choose by the variable's meaning before choosing by appearance. The local [gallery](../assets/palette-gallery.html) contains every bundled palette and searchable source/CVD metadata. Its grayscale switch is a luminance preview, not a simulation of a color-vision deficiency (CVD).

| Meaning | Useful starting points | Apply and inspect |
|---|---|---|
| Unordered methods / ablations | `tol.bright`, `tol.muted`, `tol.high_contrast` | Use stable explicit labels. Capacity is a storage limit, not a promise that every color is distinguishable in a small figure. Prefer a small set; use direct labels or facets for crowded comparisons. |
| Magnitude / density / probability | `viridis.viridis`, `viridis.cividis`, `scico.batlow`, `cmocean.thermal` | Declare scale limits and units; keep limits consistent for comparable panels. Choose direction deliberately. Label missing values separately. |
| Signed change around a meaningful reference | `scico.vik`, `cmocean.balance`, `brewer.BrBG` | State the center (often zero) and the normalization. Do not invent a zero center for strictly positive magnitudes. Explain asymmetric limits. |
| Phase / angle / periodic position | `cmocean.phase`, `scico.romao` | A cyclic palette is justified only when the endpoints are neighbors. Mark units and wrap point. |
| Ordered discrete bins | A native `brewer` or `scico.*_discrete` scheme | Use the exact supported class count and show boundaries. Do not interpolate an unrecorded native scheme silently. |
| A single highlighted method | One chosen accent plus visibly distinct neutral references | Preserve existing assignments. Use line width, markers or direct labels sparingly; never use dramatic contrast to imply unsupported superiority. |

These are starting points, not CCF-approved presets. `matplotlib.tab10/tab20` are useful legacy mappings but have no blanket CVD guarantee in this registry. `viridis.turbo` and other colorful maps are retained for source completeness within the selected families, not recommended as default scientific magnitude maps. Consult each record's kind and CVD annotations.

## Quantitative meaning

- Categories use qualitative colors; a sequential gradient can falsely imply ordering among unrelated methods.
- Keep a method's color fixed even when its rank changes, a panel omits it, or the plotting table is sorted. Preserve the label-to-color map rather than relying on a global plotting cycle.
- A signed diverging map needs an explicit center and a matching colorbar; do not use a single linear normalization with an off-center zero accidentally.
- Log transforms, clipping, saturation, and missing values affect interpretation. Record them with the scale. Do not encode unavailable measurements as the minimum observed value.
- Error bands inherit their method's color with documented transparency. Diagnose the displayed composite against its real background; transparency changes both contrast and grayscale separation.
- Plotting colors do not authorize altering microscopy, molecular surfaces, material phase maps, spectra, segmentation labels, or instrument-provided pseudocolor semantics. Preserve the relevant legend and physical meaning.

## What accessibility evidence means

`reported`, `conditional`, `not_assessed`, and `not_recommended` are upstream metadata categories. For ColorBrewer, `cvd.by_n` can depend on the exact number of classes; an unlisted count is unassessed even if the family is generally reported as accessible. These labels do not substitute for inspecting the actual figure at final size.

The Python audit checks sRGB contrast and CIE L* separation. Its L* distance threshold is a tunable screening heuristic, not a standard, and near-equal grayscale shades can still be distinguished by adequate labels, markers, or spatial separation. It does not compute CVD simulation or a perceptual color-difference guarantee. If a simulation tool is available in the project, state its model, deficiency type/severity, and which rendered export was checked; never report an unrun simulation as passed.

Do not automatically darken a selected palette until every continuous heatmap cell exceeds a generic contrast threshold. Contrast needs depend on the actual graphical boundary and task. Thin colored lines on white, text over fills, and touching colored regions each need their own review.
