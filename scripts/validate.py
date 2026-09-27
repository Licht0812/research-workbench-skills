#!/usr/bin/env python3
"""Check skill format separately from this repository's distribution conventions."""

import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
SKILLS = tuple(row["name"] for row in CATALOG["skills"])
LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")


class UniqueKeyLoader(yaml.SafeLoader):
    """Reject ambiguous duplicate YAML fields rather than silently replacing them."""


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        try:
            if key in result:
                raise yaml.YAMLError("Duplicate YAML key: " + str(key))
            result[key] = loader.construct_object(value_node, deep=deep)
        except TypeError as error:
            raise yaml.YAMLError("YAML mapping keys must be scalar") from error
    return result


UniqueKeyLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def relative_links(path, boundary):
    errors = []
    for value in LINK.findall(path.read_text(encoding="utf-8")):
        parsed = urlsplit(value.strip("<>"))
        if parsed.scheme or not parsed.path:
            continue
        target = (path.parent / unquote(parsed.path)).resolve()
        if target != boundary and boundary not in target.parents:
            errors.append(str(path) + ": reference escapes package: " + value)
        elif not target.exists():
            errors.append(str(path) + ": missing reference: " + value)
    return errors


def validate_skill_format(folder):
    """Check Agent Skills metadata and present OpenAI UI metadata; extras are optional."""
    folder = Path(folder).resolve()
    errors = []
    entry = folder / "SKILL.md"
    if not entry.is_file():
        return [folder.name + ": SKILL.md must be a regular file"]
    try:
        source = entry.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return [folder.name + ": unreadable UTF-8 entry: " + str(error)]
    match = re.match(r"\A---\n(.*?)\n---\n(.+)\Z", source, re.S)
    if not match or not match.group(2).strip():
        return [folder.name + ": missing frontmatter or empty instructions"]
    try:
        meta = yaml.load(match.group(1), Loader=UniqueKeyLoader)
    except yaml.YAMLError as error:
        return [folder.name + ": invalid YAML: " + str(error)]
    if not isinstance(meta, dict):
        return [folder.name + ": frontmatter must be a mapping"]
    allowed = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
    if set(meta) - allowed:
        errors.append(folder.name + ": unsupported frontmatter field")
    if not isinstance(meta.get("name"), str) or meta["name"] != folder.name:
        errors.append(folder.name + ": metadata name does not match directory")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", folder.name) or len(folder.name) > 64:
        errors.append(folder.name + ": invalid skill name")
    description = meta.get("description", "")
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append(folder.name + ": invalid description")
    for field in ("license", "compatibility", "allowed-tools"):
        if field in meta and (not isinstance(meta[field], str) or not meta[field].strip()):
            errors.append(folder.name + ": " + field + " must be a non-empty string")
    if isinstance(meta.get("compatibility"), str) and len(meta["compatibility"]) > 500:
        errors.append(folder.name + ": compatibility exceeds 500 characters")
    if "metadata" in meta and (not isinstance(meta["metadata"], dict) or
                              any(not isinstance(k, str) or not isinstance(v, str)
                                  for k, v in meta["metadata"].items())):
        errors.append(folder.name + ": metadata must map strings to strings")
    agent = folder / "agents/openai.yaml"
    if agent.exists():
        try:
            config = yaml.load(agent.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
        except (OSError, UnicodeError, yaml.YAMLError) as error:
            errors.append(folder.name + ": invalid agents/openai.yaml: " + str(error))
            config = None
        if not isinstance(config, dict) or not isinstance(config.get("interface"), dict):
            errors.append(folder.name + ": interface must be a mapping")
        else:
            ui = config["interface"]
            for field in ("display_name", "short_description"):
                if not isinstance(ui.get(field), str) or not ui[field].strip():
                    errors.append(folder.name + ": invalid interface." + field)
            for field in ("default_prompt", "brand_color", "icon_small", "icon_large"):
                if field in ui and (not isinstance(ui[field], str) or not ui[field].strip()):
                    errors.append(folder.name + ": invalid interface." + field)
            if "policy" in config:
                policy = config["policy"]
                if not isinstance(policy, dict):
                    errors.append(folder.name + ": policy must be a mapping")
                elif "allow_implicit_invocation" in policy and type(policy["allow_implicit_invocation"]) is not bool:
                    errors.append(folder.name + ": allow_implicit_invocation must be boolean")
    return errors


def validate_skill(folder):
    """Apply this collection's release policy in addition to the public format."""
    folder = Path(folder).resolve()
    errors = validate_skill_format(folder)
    for required in ("LICENSE", "NOTICE.md", "agents/openai.yaml"):
        if not (folder / required).is_file():
            errors.append(folder.name + ": repository convention requires " + required)
    for path in folder.rglob("*"):
        if path.is_symlink():
            errors.append(folder.name + ": distribution convention forbids symlinks")
        elif path.suffix == ".md":
            errors.extend(relative_links(path, folder))
    license_file = folder / "LICENSE"
    if license_file.is_file():
        license_text = license_file.read_text(encoding="utf-8")
        if "Copyright (c)" not in license_text or "Permission is hereby granted" not in license_text:
            errors.append(folder.name + ": missing complete instruction/code license")
    if errors:
        return errors
    ui = yaml.load((folder / "agents/openai.yaml").read_text(encoding="utf-8"), Loader=UniqueKeyLoader)["interface"]
    if not 25 <= len(ui["short_description"]) <= 64:
        errors.append(folder.name + ": creator UI convention requires 25–64 characters")
    if "$" + folder.name not in ui.get("default_prompt", ""):
        errors.append(folder.name + ": repository default_prompt must mention this skill")
    return errors


def main():
    errors = []
    actual = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if len(set(SKILLS)) != len(SKILLS) or actual != set(SKILLS):
        errors.append("Catalogue must list every skill exactly once.")
    for name in SKILLS:
        errors.extend(validate_skill(ROOT / "skills" / name))
    for path in ROOT.rglob("*.md"):
        if any(part in {".venv", ".git", "__pycache__"} for part in path.parts):
            continue
        errors.extend(relative_links(path, ROOT))
    for path in (ROOT / ".github").rglob("*.yml"):
        yaml.safe_load(path.read_text(encoding="utf-8"))
    sources = json.loads((ROOT / "docs/sources.json").read_text(encoding="utf-8"))
    upstreams = {sources["upstream"].get("id", "orchestra"): sources["upstream"],
                 **sources.get("additional_upstreams", {})}
    for source_id, upstream in upstreams.items():
        if not re.fullmatch(r"[a-f0-9]{40}", upstream["commit"]):
            errors.append(source_id + ": provenance needs a full upstream commit.")
    for row in CATALOG["skills"]:
        upstream = upstreams.get(row.get("source_id", "orchestra"))
        entries = {entry["path"]: entry for entry in upstream["files"]} if upstream else {}
        entry = entries.get(row["upstream_path"])
        if not entry or row["git_blob_sha"] != entry["git_blob_sha"]:
            errors.append(row["name"] + ": missing upstream provenance")
        if upstream and upstream["copyright_notice"] not in (ROOT / "skills" / row["name"] / "LICENSE").read_text(encoding="utf-8"):
            errors.append(row["name"] + ": missing its upstream copyright")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Validated " + str(len(SKILLS)) + " self-contained skills, YAML metadata, local links, licenses, and provenance.")
    print("This is structural validation; it does not run model behavioral evaluations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
