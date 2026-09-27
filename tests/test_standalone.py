import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("skill_validate", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class StandaloneTests(unittest.TestCase):
    def test_each_package_validates_without_the_repository_or_other_skill(self):
        for name in validator.SKILLS:
            with self.subTest(skill=name), tempfile.TemporaryDirectory() as temp:
                folder = Path(temp) / name
                shutil.copytree(ROOT / "skills" / name, folder)
                self.assertEqual(validator.validate_skill(folder), [])

    def test_external_reference_dependency_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            name = validator.SKILLS[0]
            folder = root / name
            shutil.copytree(ROOT / "skills" / name, folder)
            (root / "outside.md").write_text("not part of package", encoding="utf-8")
            with (folder / "SKILL.md").open("a", encoding="utf-8") as f:
                f.write("\n[dependency](../outside.md)\n")
            self.assertTrue(any("escapes package" in e for e in validator.validate_skill(folder)))

    def test_missing_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as temp:
            folder = Path(temp) / validator.SKILLS[0]
            shutil.copytree(ROOT / "skills" / folder.name, folder)
            reference = next((folder / "references").glob("*.md"))
            reference.unlink()
            self.assertTrue(any("missing reference" in e for e in validator.validate_skill(folder)))


if __name__ == "__main__":
    unittest.main()
