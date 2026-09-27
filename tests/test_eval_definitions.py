import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("case_validate", ROOT / "scripts/validate_evals.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class EvaluationDefinitionTests(unittest.TestCase):
    def check_cases(self, cases):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "cases.jsonl"
            path.write_text("\n".join(json.dumps(x) for x in cases) + "\n")
            return validator.validate_cases([path], {"example-skill"})

    def case(self, **updates):
        return dict(schema_version=1, id="case-one", skills=["example-skill"], prompt="Compare supplied options.",
                    checks=["Uses the supplied evidence."], execution_status="not_run", **updates)

    def test_optional_context_and_follow_up_are_retained(self):
        count, errors = self.check_cases([self.case(tools="browsing unavailable", follow_up="Use only the supplied paper.")])
        self.assertEqual(count, 1)
        self.assertEqual(errors, [])

    def test_duplicate_ids_across_definitions_are_rejected(self):
        _, errors = self.check_cases([self.case(), self.case()])
        self.assertTrue(any("duplicate id" in e for e in errors))

    def test_unknown_skill_empty_checks_and_embedded_results_are_rejected(self):
        for key, value in [("skills", ["missing-skill"]), ("checks", []), ("execution_status", "passed")]:
            with self.subTest(field=key):
                case = self.case();case[key] = value
                self.assertTrue(self.check_cases([case])[1])

    def test_repository_definitions_have_valid_targets_and_unique_ids(self):
        names = {r["name"] for r in json.loads((ROOT / "catalog.json").read_text())["skills"]}
        count, errors = validator.validate_cases(sorted((ROOT / "evals").glob("*.jsonl")), names)
        self.assertGreater(count, 0)
        self.assertEqual(errors, [])

    def test_negative_routing_requires_an_explicit_candidate_set(self):
        case = self.case();case["skills"] = []
        self.assertTrue(self.check_cases([case])[1])
        case["available_skills"] = ["example-skill"]
        self.assertEqual(self.check_cases([case]), (1, []))


if __name__ == "__main__":
    unittest.main()
