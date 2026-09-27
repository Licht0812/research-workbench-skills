#!/usr/bin/env python3
"""Offline CCF palette selection and sRGB contrast/grayscale diagnostics.

Adapted from easyplot's MIT palette module (Rimagination, 2026).
Diagnostics are context-dependent screens, not CCF/WCAG/CVD certification.
"""
import argparse
from itertools import combinations
import json
import math
import re

from easyplot_palettes import easyplot_palette, easyplot_palette_info, easyplot_palettes


def parse_hex(value, background=(1.0, 1.0, 1.0)):
    """Accept #RGB, #RRGGBB, #RRGGBBAA; composite alpha onto opaque sRGB."""
    if not isinstance(value, str) or not re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})", value):
        raise ValueError("Use #RGB, #RRGGBB, or #RRGGBBAA: " + str(value))
    token = value[1:]
    if len(token) == 3:
        token = "".join(c * 2 for c in token)
    rgb = tuple(int(token[i:i+2], 16) / 255 for i in (0, 2, 4))
    if len(token) == 8:
        alpha = int(token[6:], 16) / 255
        rgb = tuple(c * alpha + b * (1-alpha) for c, b in zip(rgb, background))
    return rgb


def relative_luminance(rgb):
    linear = [c / 12.92 if c <= 0.04045 else ((c+0.055)/1.055)**2.4 for c in rgb]
    return sum(c*w for c, w in zip(linear, (0.2126, 0.7152, 0.0722)))


def contrast_ratio(first, second):
    a, b = relative_luminance(first), relative_luminance(second)
    return (max(a, b)+0.05)/(min(a, b)+0.05)


def lstar(rgb):
    y = relative_luminance(rgb)
    return 116 * y**(1/3) - 16 if y > 216/24389 else (24389/27)*y


def grayscale_hex(value, background="#FFFFFF"):
    y = relative_luminance(parse_hex(value, parse_hex(background)))
    s = 12.92*y if y <= 0.0031308 else 1.055*y**(1/2.4)-0.055
    b = max(0, min(255, round(255*s)))
    return f"#{b:02X}{b:02X}{b:02X}"


def cvd_for_selection(record, n):
    info = dict(record["cvd"])
    if "by_n" in info:
        info["status_for_requested_n"] = info["by_n"].get(str(n), "not_assessed")
    else:
        info["status_for_requested_n"] = info["status"]
    info["requested_n"] = n
    info["simulation_run"] = False
    return info


def audit_colors(colors, labels=None, background="#FFFFFF", role="marks", order="none", min_gray_delta=10.0):
    if not colors:
        raise ValueError("At least one color is required")
    if role not in {"text", "marks"} or order not in {"none", "increasing", "decreasing"}:
        raise ValueError("Unknown role or lightness order")
    if not math.isfinite(min_gray_delta) or min_gray_delta < 0:
        raise ValueError("The grayscale threshold must be finite and nonnegative")
    if not re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", background):
        raise ValueError("Background must be an opaque #RGB or #RRGGBB color")
    labels = list(labels) if labels is not None else [str(i+1) for i in range(len(colors))]
    if len(labels) != len(colors) or len(set(labels)) != len(labels) or any(not isinstance(x, str) or not x.strip() for x in labels):
        raise ValueError("Supply one unique nonempty label for each color")
    bg = parse_hex(background)
    rgbs = [parse_hex(color, bg) for color in colors]
    lightness = [lstar(rgb) for rgb in rgbs]
    threshold = 4.5 if role == "text" else 3.0
    ratios = [contrast_ratio(rgb, bg) for rgb in rgbs]
    entries = [{"label": name, "hex": color, "grayscale": grayscale_hex(color, background),
                "contrast_vs_background": round(ratio, 4), "cie_lstar": round(light, 4),
                "below_contrast_screen": ratio < threshold}
               for name, color, ratio, light in zip(labels, colors, ratios, lightness)]
    # Continuous maps need adjacent-lightness checks, not an O(n^2) category audit.
    pairs = combinations(range(len(colors)), 2) if order == "none" else zip(range(len(colors)-1), range(1,len(colors)))
    low_pairs = []
    count = 0
    min_delta = None
    for i, j in pairs:
        delta = abs(lightness[i]-lightness[j])
        min_delta = delta if min_delta is None else min(delta, min_delta)
        if delta < min_gray_delta:
            count += 1
            if len(low_pairs) < 20:
                low_pairs.append({"first": labels[i], "second": labels[j], "delta_lstar": round(delta, 4)})
    violations = []
    if order != "none":
        for i in range(len(lightness)-1):
            change = lightness[i+1]-lightness[i]
            if (order == "increasing" and change < -1e-9) or (order == "decreasing" and change > 1e-9):
                violations.append(i)
    warnings = []
    if any(x < threshold for x in ratios):
        warnings.append("Some samples are below the background contrast screen; inspect their actual strokes, fills, labels, and boundaries.")
    if count and order == "none":
        warnings.append("Some colors have similar grayscale lightness; inspect labels and non-color cues where identities must be distinguished.")
    if violations:
        warnings.append("Selected samples reverse the requested lightness direction; review the quantitative encoding without sorting the palette.")
    return {"background": background, "role": role, "contrast_screen": threshold,
            "colors": entries, "gray_delta_heuristic": min_gray_delta,
            "gray_pairs_compared": "all" if order == "none" else "adjacent",
            "gray_pairs_below_heuristic": count, "gray_pairs_preview": low_pairs,
            "minimum_gray_delta": None if min_delta is None else round(min_delta, 4),
            "lightness_order": order, "lightness_reversal_indices": violations,
            "warnings": warnings,
            "limitations": ["No final figure was rendered or inspected by this command.",
                            "No CVD simulation or certification is performed.",
                            "Contrast applicability depends on geometry; a heatmap is not required to make every sample contrast 3:1 with white.",
                            "Grayscale uses equal-luminance sRGB, not a printer profile; L* separation is a heuristic."]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    listing = commands.add_parser("list", help="List palette metadata")
    for flag in ("family", "kind", "cvd"):
        listing.add_argument("--"+flag)
    show = commands.add_parser("show", help="Return selected HEX colors and source metadata")
    audit = commands.add_parser("audit", help="Diagnose a named palette or custom colors")
    show.add_argument("palette")
    audit.add_argument("palette", nargs="?")
    for sub in (show, audit):
        sub.add_argument("--n", type=int)
        sub.add_argument("--reverse", action="store_true")
    audit.add_argument("--colors", nargs="+")
    audit.add_argument("--labels", nargs="+")
    audit.add_argument("--background", default="#FFFFFF")
    audit.add_argument("--role", choices=("text", "marks"), default="marks")
    audit.add_argument("--order", choices=("none", "increasing", "decreasing"), default="none")
    audit.add_argument("--min-gray-delta", type=float, default=10.0)
    args = parser.parse_args()
    try:
        if args.command == "list":
            result = easyplot_palettes(args.family, args.kind, args.cvd)
        else:
            if args.command == "audit" and bool(args.colors) == bool(args.palette):
                raise ValueError("Choose exactly one palette ID or --colors")
            if args.command == "audit" and args.colors and (args.n is not None or args.reverse):
                raise ValueError("--n and --reverse require a named palette")
            record = easyplot_palette_info(args.palette) if args.palette else None
            colors = easyplot_palette(args.palette, args.n, args.reverse) if record else args.colors
            cvd = cvd_for_selection(record, len(colors)) if record else {"status_for_requested_n": "not_assessed", "simulation_run": False}
            if args.command == "show":
                result = {"id": args.palette, "kind": record["kind"], "colors": colors,
                          "source": record["source"], "cvd": cvd}
            else:
                if len(colors) > 512:
                    raise ValueError("Audit at most 512 samples per run; select --n or use increasing/decreasing samples representative of the figure")
                result = audit_colors(colors, args.labels, args.background, args.role, args.order, args.min_gray_delta)
                result.update({"palette_id": args.palette, "cvd": cvd})
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except ValueError as error:
        parser.error(str(error))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
