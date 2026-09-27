# Offline palette tools

Run these examples from the skill folder. No tool installs software, changes host settings, or contacts a service.

## Python and command line

```sh
python3 scripts/ccf_palette.py list --family tol
python3 scripts/ccf_palette.py show brewer.BrBG --n 5
python3 scripts/ccf_palette.py audit tol.bright --n 3 --role marks
python3 scripts/ccf_palette.py audit --colors '#4477AA' '#EE6677' '#228833' --labels Baseline Method Ablation
python3 scripts/ccf_palette.py audit viridis.viridis --n 16 --order increasing
```

Audit output is JSON on stdout. Exit status zero means diagnostics ran successfully; it does not mean a figure passed accessibility review. Invalid input gives a nonzero exit. Inspect the `warnings`, actual role/background, CVD evidence, and `limitations` fields. `--role text` screens 4.5:1; `marks` screens 3:1. `--order` checks the selected samples' lightness direction, not perceived uniformity. Full-range diagnostics can be obtained by omitting `--n`.

```python
import sys
sys.path.insert(0, "scripts")  # use this skill's scripts directory
from easyplot_palettes import easyplot_palette, easyplot_palette_info

labels = ["Baseline", "Method", "Ablation"]  # stable project order
colors = dict(zip(labels, easyplot_palette("tol.bright", len(labels))))
metadata = easyplot_palette_info("tol.bright")
```

The getters use the standard library. In an existing Matplotlib environment:

```python
from easyplot_palettes import easyplot_cmap
from matplotlib.colors import TwoSlopeNorm

cmap = easyplot_cmap("scico.vik")
norm = TwoSlopeNorm(vmin=-2, vcenter=0, vmax=2)  # illustrative limits only
# ax.imshow(actual_signed_values, cmap=cmap, norm=norm)
```

Use real limits and actual data in a real plot. Qualitative palettes are refused by `easyplot_cmap`. Missing data default to `#E2E2E2`; expose their meaning in the legend/description. For a heatmap this may need a boundary or hatching to avoid confusion with low values.

## Selection rules and provenance

- IDs and filters are exact and case-sensitive. Find IDs with `list`; no name guessing or silent fallback.
- `prefix` takes the first requested colors, refuses excess categories, and never recycles.
- `native` uses an exact stored class-count scheme; sizes 1/2 use the first colors of the smallest scheme. Missing larger native sizes fail.
- `lut` selects stored indices with endpoint-preserving half-up rounding. It does not invent higher precision; requesting more colors than the table contains repeats entries.
- `reverse` reverses the selected result. Qualitative identity still requires a stable mapping.

The [registry](../assets/palettes.json) holds 205 tables; [provenance](../assets/provenance.json) records the exact upstream commit, original Git blobs, selection rule, and canonical record hashes. A hash is an integrity check, not a perceptual guarantee.

## Preview and regeneration

Open [the offline gallery](../assets/palette-gallery.html) in a browser to search all 205 palettes, filter by family/type, switch to grayscale, and copy IDs. It loads no external assets. Regenerate it and the compact [preview](../assets/palette-preview.svg) with:

```sh
python3 scripts/build_gallery.py
```

The gallery shows sampled swatches; full HEX/native-size values remain in the registry. Gallery CVD badges report the full palette record, so confirm `cvd.by_n` for the specific chosen class count before applying a discrete scheme. The grayscale display is not a CVD simulation. Preview drawings are color references, not experimental results.
