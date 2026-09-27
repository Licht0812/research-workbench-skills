import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "skills/ccf-conference-colors"
SCRIPTS = PACKAGE / "scripts"
sys.path.insert(0, str(SCRIPTS))
import easyplot_palettes as palettes
import ccf_palette as audit
import build_gallery


class ColorTests(unittest.TestCase):
    def test_registry_matches_the_frozen_selection_hashes(self):
        data = json.loads((PACKAGE / "assets/palettes.json").read_text())
        manifest = json.loads((PACKAGE / "assets/provenance.json").read_text())
        actual = {p["id"]: hashlib.sha256(json.dumps(p, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest() for p in data["palettes"]}
        self.assertEqual(len(actual), 205)
        self.assertEqual(actual, manifest["records"])
        self.assertEqual(sum(manifest["counts_by_family"].values()), 205)
        self.assertNotIn("tol.pale", actual)
        self.assertNotIn("tol.dark", actual)

    def test_python_reader_retains_the_upstream_git_blob_contents(self):
        manifest = json.loads((PACKAGE / "assets/provenance.json").read_text())
        blobs = {row["path"]: row["git_blob_sha"] for row in manifest["source_files"]}
        for rel in ("scripts/easyplot_palettes.py",):
            data = (PACKAGE / rel).read_bytes()
            value = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
            self.assertEqual(value, blobs[rel])

    def test_categorical_order_and_defensive_copies(self):
        self.assertEqual(palettes.easyplot_palette("tol.bright", 3), ["#4477AA", "#EE6677", "#228833"])
        record = palettes.easyplot_palette_info("tol.bright")
        record["colours"][0] = "#000000"
        self.assertEqual(palettes.easyplot_palette("tol.bright", 1), ["#4477AA"])

    def test_native_scheme_uses_the_requested_class_count(self):
        self.assertEqual(palettes.easyplot_palette("brewer.BrBG", 5), ["#A6611A", "#DFC27D", "#F5F5F5", "#80CDC1", "#018571"])
        with self.assertRaises(ValueError):
            palettes.easyplot_palette("scico.acton_discrete", 7)

    def test_lut_endpoints_midpoint_and_selected_reverse(self):
        stored = palettes.easyplot_palette("viridis.viridis")
        self.assertEqual(palettes.easyplot_palette("viridis.viridis", 2), [stored[0], stored[-1]])
        self.assertEqual(palettes.easyplot_palette("viridis.viridis", 1), [stored[128]])
        self.assertEqual(palettes.easyplot_palette("tol.bright", 3, True), ["#228833", "#EE6677", "#4477AA"])

    def test_bad_palette_requests_never_silently_recycle(self):
        for n in (0, -1, True, 3.0, 8):
            with self.subTest(n=n), self.assertRaises(ValueError):
                palettes.easyplot_palette("tol.bright", n)
        with self.assertRaises(ValueError):
            palettes.easyplot_palette("Tol.Bright", 3)

    def test_known_contrast_and_grayscale_anchors(self):
        black, white = audit.parse_hex("#000"), audit.parse_hex("#FFFFFF")
        self.assertAlmostEqual(audit.contrast_ratio(black, white), 21)
        self.assertAlmostEqual(audit.contrast_ratio(white, white), 1)
        self.assertAlmostEqual(audit.lstar(black), 0)
        self.assertAlmostEqual(audit.lstar(white), 100)
        self.assertEqual(audit.grayscale_hex("#000"), "#000000")
        self.assertEqual(audit.grayscale_hex("#FFF"), "#FFFFFF")

    def test_transparency_is_composited_on_the_actual_background(self):
        self.assertEqual(audit.parse_hex("#00000000"), (1, 1, 1))
        self.assertEqual(audit.parse_hex("#FFFFFF00", (0, 0, 0)), (0, 0, 0))
        self.assertAlmostEqual(audit.parse_hex("#00000080")[0], 127/255)
        self.assertEqual(audit.grayscale_hex("#00000000"), "#FFFFFF")

    def test_invalid_colors_labels_and_background_are_rejected(self):
        for colors, kwargs in [(["red"], {}), (["##FFFFFF"], {}), (["#000", "#FFF"], {"labels": ["x", "x"]}), (["#FFF"], {"background": "#00000080"}), (["#FFF"], {"min_gray_delta": float("nan")})]:
            with self.subTest(colors=colors, kwargs=kwargs), self.assertRaises(ValueError):
                audit.audit_colors(colors, **kwargs)

    def test_diagnostics_report_lightness_reversal_without_changing_values(self):
        colors = ["#FFFFFF", "#000000", "#AAAAAA"]
        result = audit.audit_colors(colors, order="increasing", role="text")
        self.assertEqual(result["lightness_reversal_indices"], [0])
        self.assertEqual([x["hex"] for x in result["colors"]], colors)
        self.assertEqual(result["contrast_screen"], 4.5)
        self.assertTrue(result["warnings"])

    def test_class_count_cvd_evidence_is_not_extended_to_unlisted_counts(self):
        record = palettes.easyplot_palette_info("brewer.BrBG")
        self.assertEqual(audit.cvd_for_selection(record, 1)["status_for_requested_n"], "not_assessed")
        self.assertEqual(audit.cvd_for_selection(record, 5)["status_for_requested_n"], "reported")
        self.assertFalse(audit.cvd_for_selection(record, 5)["simulation_run"])

    def test_offline_cli_works_when_the_skill_is_copied_alone(self):
        with tempfile.TemporaryDirectory() as temp:
            isolated = Path(temp) / PACKAGE.name
            shutil.copytree(PACKAGE, isolated)
            env = dict(os.environ)
            env.pop("PYTHONPATH", None)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            result = subprocess.run([sys.executable, str(isolated / "scripts/ccf_palette.py"), "audit", "tol.bright", "--n", "3"], cwd=temp, env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual(len(data["colors"]), 3)
            self.assertFalse(data["cvd"]["simulation_run"])

    def test_cli_reports_ambiguous_and_invalid_requests(self):
        for arguments in (["audit"], ["audit", "tol.bright", "--colors", "#FFFFFF"], ["audit", "--colors", "#FFFFFF", "--n", "2"], ["show", "unknown"], ["show", "tol.bright", "--n", "8"]):
            with self.subTest(arguments=arguments):
                result = subprocess.run([sys.executable, str(SCRIPTS / "ccf_palette.py"), *arguments], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertIn("error:", result.stderr)

    def test_gallery_and_svg_are_reproducible_from_the_registry(self):
        self.assertEqual(build_gallery.gallery(), (PACKAGE / "assets/palette-gallery.html").read_text())
        self.assertEqual(build_gallery.preview(), (PACKAGE / "assets/palette-preview.svg").read_text())

    def test_contract_example_uses_stable_named_palette_values(self):
        contract = json.loads((PACKAGE / "assets/color-contract.example.json").read_text())
        self.assertTrue(contract["example_only"])
        self.assertEqual([s["color"] for s in contract["series"]], palettes.easyplot_palette(contract["palette_id"], 3))
        self.assertFalse(any(contract["checks"].values()))


if __name__ == "__main__":
    unittest.main()
