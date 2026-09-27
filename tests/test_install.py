import importlib.util
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("skill_install", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / "source"
        shutil.copytree(ROOT / "skills", self.source)
        self.dest = self.root / "installed"

    def test_all_packages_are_byte_identical(self):
        installer.install(self.source, self.dest, installer.SKILLS)
        for name in installer.SKILLS:
            source_files = {p.relative_to(self.source / name): p.read_bytes()
                            for p in (self.source / name).rglob("*") if p.is_file()}
            dest_files = {p.relative_to(self.dest / name): p.read_bytes()
                          for p in (self.dest / name).rglob("*") if p.is_file()}
            self.assertEqual(source_files, dest_files)

    def test_single_skill_does_not_require_sibling(self):
        name = installer.SKILLS[0]
        for sibling in installer.SKILLS[1:]:
            shutil.rmtree(self.source / sibling)
        installer.install(self.source, self.dest, (name,))
        self.assertTrue((self.dest / name / "SKILL.md").is_file())
        self.assertEqual([p.name for p in self.dest.iterdir()], [name])

    def test_dry_run_makes_no_destination(self):
        targets = installer.install(self.source, self.dest, installer.SKILLS, dry_run=True)
        self.assertEqual(len(targets), len(installer.SKILLS))
        self.assertFalse(self.dest.exists())

    def test_collision_is_detected_before_any_skill_is_installed(self):
        first, second = installer.SKILLS[:2]
        existing = self.dest / second
        existing.mkdir(parents=True)
        (existing / "user-notes.txt").write_text("keep me", encoding="utf-8")
        with self.assertRaises(FileExistsError):
            installer.install(self.source, self.dest, installer.SKILLS)
        self.assertFalse((self.dest / first).exists())
        self.assertEqual((existing / "user-notes.txt").read_text(), "keep me")

    def test_missing_license_prevents_partial_install(self):
        (self.source / installer.SKILLS[1] / "LICENSE").unlink()
        with self.assertRaises(ValueError):
            installer.install(self.source, self.dest, installer.SKILLS)
        self.assertFalse(self.dest.exists())

    def test_destination_cannot_be_inside_source(self):
        with self.assertRaises(ValueError):
            installer.install(self.source, self.source / "nested", installer.SKILLS)
        self.assertFalse((self.source / "nested").exists())

    def test_source_symlink_is_rejected(self):
        (self.source / installer.SKILLS[0] / "external").symlink_to(self.root)
        with self.assertRaises(ValueError):
            installer.install(self.source, self.dest, installer.SKILLS)
        self.assertFalse(self.dest.exists())

    def test_dangling_destination_symlink_is_preserved(self):
        self.dest.mkdir()
        target = self.dest / installer.SKILLS[0]
        target.symlink_to(self.root / "missing")
        with self.assertRaises(FileExistsError):
            installer.install(self.source, self.dest, installer.SKILLS)
        self.assertTrue(target.is_symlink())

    def test_copy_failure_publishes_no_skill(self):
        with patch.object(installer.shutil, "copytree", side_effect=OSError("simulated copy failure")):
            with self.assertRaises(OSError):
                installer.install(self.source, self.dest, installer.SKILLS)
        self.assertEqual(list(self.dest.iterdir()), [])

    def test_second_package_failure_rolls_back_only_new_folders(self):
        self.dest.mkdir()
        sentinel = self.dest / "unrelated.txt"
        sentinel.write_text("preserve", encoding="utf-8")
        rename = Path.rename
        second = installer.SKILLS[1]

        def fail_second(path, target):
            if Path(target).parent == self.dest / second:
                raise OSError("simulated publish failure")
            return rename(path, target)

        with patch.object(Path, "rename", fail_second):
            with self.assertRaises(OSError):
                installer.install(self.source, self.dest, installer.SKILLS)
        self.assertEqual(list(self.dest.iterdir()), [sentinel])
        self.assertEqual(sentinel.read_text(), "preserve")

    def test_default_uses_documented_user_scope_without_legacy_codex_home(self):
        custom = self.root / "custom-codex"
        with patch.dict(os.environ, {"CODEX_HOME": str(custom)}), patch.object(Path, "home", return_value=self.root):
            self.assertEqual(installer.default_destination(), self.root / ".agents" / "skills")
            self.assertFalse(custom.exists())

    def test_cli_can_select_multiple_packages_without_writing_in_dry_run(self):
        names = installer.SKILLS[:2]
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--skill", names[0], "--skill", names[1],
                                 "--dest", str(self.dest), "--dry-run"],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.count("Would copy:"), 2)
        self.assertFalse(self.dest.exists())

    def test_cli_rejects_all_mixed_with_individual_selection(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--skill", "all", "--skill", installer.SKILLS[0],
                                 "--dest", str(self.dest)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse(self.dest.exists())

    def test_cli_list_returns_the_catalogue_without_installing(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--list", "--dest", str(self.dest)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(result.stdout.splitlines(), list(installer.SKILLS))
        self.assertFalse(self.dest.exists())

    def test_cli_without_a_selection_never_copies_all(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--dest", str(self.dest)], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Choose --skill, --category, or --all", result.stderr)
        self.assertFalse(self.dest.exists())

    def test_each_category_copies_only_its_independent_packages(self):
        for category in installer.CATEGORIES:
            with self.subTest(category=category):
                destination = self.root / ("category-" + category)
                result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                         "--category", category, "--dest", str(destination)],
                                        capture_output=True, text=True)
                self.assertEqual(result.returncode, 0, result.stderr)
                expected = {row["name"] for row in installer.CATALOG
                            if row["category"].split()[0] == category}
                self.assertEqual({p.name for p in destination.iterdir()}, expected)
                for name in expected:
                    source_files = {p.relative_to(ROOT / "skills" / name): p.read_bytes()
                                    for p in (ROOT / "skills" / name).rglob("*") if p.is_file()}
                    copied_files = {p.relative_to(destination / name): p.read_bytes()
                                    for p in (destination / name).rglob("*") if p.is_file()}
                    self.assertEqual(source_files, copied_files)

    def test_categories_and_skills_form_a_union_without_duplicates(self):
        selected = installer.select_skills(("accelerate", "ccf-conference-colors"), ("08", "08", "21"))
        expected = {"accelerate", "deepspeed", "pytorch-fsdp2", "pytorch-lightning", "ray-train",
                    "brainstorming-research-ideas", "creative-thinking-for-research", "ccf-conference-colors"}
        self.assertEqual(set(selected), expected)
        self.assertEqual(len(selected), len(expected))

    def test_cli_filtered_listing_does_not_copy(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--category", "21", "--list", "--dest", str(self.dest)],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(set(result.stdout.splitlines()), {"brainstorming-research-ideas", "creative-thinking-for-research"})
        self.assertFalse(self.dest.exists())

    def test_cli_lists_categories_with_counts_without_copying(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--list-categories", "--dest", str(self.dest)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("08 分布式训练\t5 skills", result.stdout)
        self.assertEqual(len(result.stdout.splitlines()), len(installer.CATEGORIES))
        self.assertFalse(self.dest.exists())

    def test_cli_explicit_all_copies_the_full_catalogue(self):
        result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                 "--all", "--dest", str(self.dest)], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual({p.name for p in self.dest.iterdir()}, set(installer.SKILLS))

    def test_invalid_or_mixed_all_selection_never_writes(self):
        for selection in (("--all", "--category", "08"), ("--all", "--skill", "academic-plotting"), ("--category", "99")):
            with self.subTest(selection=selection):
                result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"),
                                         *selection, "--dest", str(self.dest)], capture_output=True, text=True)
                self.assertNotEqual(result.returncode, 0)
                self.assertFalse(self.dest.exists())


if __name__ == "__main__":
    unittest.main()
