"""Original packages must have real notices without bypassing imported provenance."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("provenance_validate", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        self.folder = self.root / "skills/swablab-log"
        self.folder.mkdir(parents=True)
        self.notice = "Copyright (c) 2026 Research Workbench Skills contributors"
        (self.folder / "SKILL.md").write_text(
            "---\nname: swablab-log\ndescription: Record training runs.\nlicense: MIT\n---\n\nRecord the run.\n",
            encoding="utf-8")
        (self.folder / "LICENSE").write_text("MIT License\n\n" + self.notice + "\n", encoding="utf-8")
        self.original = {"name": "swablab-log", "source_id": "original"}
        self.imported = {
            "name": "imported-skill", "source_id": "orchestra",
            "upstream_path": "upstream/SKILL.md", "git_blob_sha": "b" * 40,
        }
        imported_folder = self.root / "skills/imported-skill"
        imported_folder.mkdir()
        (imported_folder / "LICENSE").write_text("Copyright (c) Upstream contributors\n", encoding="utf-8")
        self.sources = {
            "upstream": {
                "id": "orchestra", "commit": "a" * 40,
                "copyright_notice": "Copyright (c) Upstream contributors",
                "files": [{"path": "upstream/SKILL.md", "git_blob_sha": "b" * 40}],
            },
            "original_skills": {
                "swablab-log": {
                    "created_on": "2026-10-07", "license": "MIT",
                    "copyright_notice": self.notice,
                    "description": "Newly authored SWABLAB training recorder.",
                    "technical_references": [],
                },
            },
        }

    def check(self, rows=None, sources=None):
        return validator.validate_provenance(
            self.root, [self.original] if rows is None else rows,
            self.sources if sources is None else sources)

    def test_original_requires_no_fabricated_upstream_hash(self):
        self.assertEqual(self.check(), [])

    def test_original_record_is_required(self):
        for originals in ({}, [], {"swablab-log": "not a source record"}):
            with self.subTest(originals=originals):
                sources = copy.deepcopy(self.sources)
                sources["original_skills"] = originals
                self.assertIn("swablab-log: missing original provenance", self.check(sources=sources))

    def test_imported_fields_cannot_be_relabelled_original(self):
        for field in ("upstream_path", "upstream_name", "git_blob_sha", "source_url"):
            with self.subTest(field=field):
                row = {**self.original, field: "existing upstream value"}
                self.assertTrue(any("must not include upstream provenance fields" in error
                                    for error in self.check(rows=[row])))

    def test_original_license_must_match_entry_and_package(self):
        entry = self.folder / "SKILL.md"
        entry.write_text(entry.read_text().replace("license: MIT", "license: Apache-2.0"))
        self.assertIn("swablab-log: original license differs from SKILL.md", self.check())
        entry.write_text(entry.read_text().replace("license: Apache-2.0", "license: MIT"))
        (self.folder / "LICENSE").write_text("Apache License\n\n" + self.notice + "\n")
        self.assertIn("swablab-log: original license differs from LICENSE", self.check())

    def test_original_contributions_keep_repository_license(self):
        self.sources["original_skills"]["swablab-log"]["license"] = "Apache-2.0"
        self.assertTrue(any("must use the repository MIT license" in error for error in self.check()))

    def test_original_copyright_must_appear_in_package(self):
        for notice in (None, "", "Copyright (c) Different author"):
            with self.subTest(notice=notice):
                self.sources["original_skills"]["swablab-log"]["copyright_notice"] = notice
                self.assertIn("swablab-log: missing its original copyright", self.check())

    def test_original_does_not_skip_imported_commit_or_blob_checks(self):
        rows = [self.original, self.imported]
        self.assertEqual(self.check(rows=rows), [])
        sources = copy.deepcopy(self.sources)
        sources["upstream"]["commit"] = "short-sha"
        self.assertIn("orchestra: provenance needs a full upstream commit.", self.check(rows=rows, sources=sources))
        row = {**self.imported, "git_blob_sha": "c" * 40}
        self.assertIn("imported-skill: missing upstream provenance", self.check(rows=[self.original, row]))

    def test_imported_copyright_remains_required(self):
        (self.root / "skills/imported-skill/LICENSE").write_text("Different notice\n")
        self.assertIn("imported-skill: missing its upstream copyright", self.check(rows=[self.imported]))


if __name__ == "__main__":
    unittest.main()
