#!/usr/bin/env python3
"""Validate optional evaluation definitions without running or scoring a model."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]


def validate_cases(paths, skill_names):
    errors, seen = [], set()
    count = 0
    fields = {"schema_version", "id", "skills", "available_skills", "prompt", "checks", "execution_status", "follow_up", "tools"}
    required = fields - {"follow_up", "tools", "available_skills"}
    for path in paths:
        for number, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
            label = f"{Path(path).name}:{number}"
            try:
                case = json.loads(line)
            except json.JSONDecodeError as error:
                errors.append(label + ": invalid JSON: " + error.msg)
                continue
            count += 1
            if not isinstance(case, dict) or not required <= case.keys() or case.keys() - fields:
                errors.append(label + ": invalid case fields")
                continue
            if type(case["schema_version"]) is not int or case["schema_version"] != 1:
                errors.append(label + ": unsupported schema_version")
            case_id = case["id"]
            if not isinstance(case_id, str) or not case_id.strip():
                errors.append(label + ": id must be a non-empty string")
            elif case_id in seen:
                errors.append(label + ": duplicate id: " + case_id)
            else:
                seen.add(case_id)
            names = case["skills"]
            if (not isinstance(names, list) or
                    any(not isinstance(n, str) or n not in skill_names for n in names)):
                errors.append(label + ": skills must name available packages")
            elif len(set(names)) != len(names):
                errors.append(label + ": skills must not contain duplicates")
            candidates = case.get("available_skills", names)
            if (not isinstance(candidates, list) or not candidates or
                    any(not isinstance(n, str) or n not in skill_names for n in candidates)):
                errors.append(label + ": available_skills must identify the candidate set, including for negative routing")
            elif isinstance(names, list) and all(isinstance(n, str) for n in names):
                if len(set(candidates)) != len(candidates) or not set(names) <= set(candidates):
                    errors.append(label + ": expected skills must be within unique available_skills")
            for field in ("prompt", "tools", "follow_up"):
                if field in case and (not isinstance(case[field], str) or not case[field].strip()):
                    errors.append(label + ": " + field + " must be non-empty text")
            checks = case["checks"]
            if (not isinstance(checks, list) or not checks or
                    any(not isinstance(c, str) or not c.strip() for c in checks)):
                errors.append(label + ": checks must contain observable acceptance criteria")
            if case["execution_status"] != "not_run":
                errors.append(label + ": store observed evaluation results separately from definitions")
    return count, errors


def main():
    names = {r["name"] for r in json.loads((ROOT / "catalog.json").read_text())["skills"]}
    count, errors = validate_cases(sorted((ROOT / "evals").glob("*.jsonl")), names)
    if count == 0:
        errors.append("No evaluation definitions found.")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {count} optional case definitions. No model evaluation was run.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
