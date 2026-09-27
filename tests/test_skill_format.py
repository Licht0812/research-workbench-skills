"""Regression tests for public format versus collection-specific packaging."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("format_validate", ROOT / "scripts/validate.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class SkillFormatTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.folder = Path(temp.name) / "example-skill"
        self.folder.mkdir()

    def entry(self, extra="", description='"Compare the supplied research options."', body="Compare the options."):
        (self.folder / "SKILL.md").write_text(
            "---\nname: example-skill\ndescription: " + description + "\n" + extra + "---\n\n" + body + "\n",
            encoding="utf-8")

    def test_minimal_public_skill_needs_no_repository_extras(self):
        self.entry()
        self.assertEqual(validator.validate_skill_format(self.folder), [])
        errors = validator.validate_skill(self.folder)
        self.assertTrue(any("repository convention requires LICENSE" in x for x in errors))
        self.assertTrue(any("repository convention requires agents/openai.yaml" in x for x in errors))

    def test_optional_standard_fields_are_accepted(self):
        self.entry('license: MIT\ncompatibility: Python 3.9+\nmetadata:\n  version: "1.0"\n')
        self.assertEqual(validator.validate_skill_format(self.folder), [])

    def test_duplicate_frontmatter_is_rejected(self):
        self.entry('name: another-skill\n')
        self.assertTrue(any("Duplicate YAML key" in x for x in validator.validate_skill_format(self.folder)))

    def test_empty_or_nonstring_description_and_body_are_rejected(self):
        for description, body in [('" "', "Compare."), ("42", "Compare."), ('"Compare."', " ")]:
            with self.subTest(description=description, body=body):
                self.entry(description=description, body=body)
                self.assertTrue(validator.validate_skill_format(self.folder))

    def test_metadata_values_must_be_strings(self):
        self.entry('metadata:\n  version: 1\n')
        self.assertTrue(any("map strings to strings" in x for x in validator.validate_skill_format(self.folder)))

    def test_optional_ui_rejects_numeric_name_and_string_boolean(self):
        self.entry()
        (self.folder / "agents").mkdir()
        (self.folder / "agents/openai.yaml").write_text(
            'interface:\n  display_name: 42\n  short_description: "Research options"\npolicy:\n  allow_implicit_invocation: "false"\n')
        errors = validator.validate_skill_format(self.folder)
        self.assertTrue(any("interface.display_name" in x for x in errors))
        self.assertTrue(any("must be boolean" in x for x in errors))


if __name__ == "__main__":
    unittest.main()
