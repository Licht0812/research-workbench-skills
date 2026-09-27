#!/usr/bin/env python3
"""Copy explicitly selected independent skills to a chosen folder or host skill directory."""

import argparse
import json
import os
from pathlib import Path
import shutil
import tempfile


REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((REPO_ROOT / "catalog.json").read_text(encoding="utf-8"))["skills"]
SKILLS = tuple(row["name"] for row in CATALOG)
CATEGORIES = {row["category"].split()[0]: row["category"] for row in CATALOG}


def select_skills(names=(), categories=(), all_skills=False):
    """Select a union in catalogue order; categories do not add dependencies."""
    names, categories = tuple(names), tuple(categories)
    if all_skills:
        if names or categories:
            raise ValueError("Use --all alone, or combine --skill and --category.")
        return SKILLS
    if not names and not categories:
        raise ValueError("Choose --skill, --category, or --all; use --list to inspect without copying.")
    if any(name not in SKILLS for name in names):
        raise ValueError("Unknown skill name.")
    if any(category not in CATEGORIES for category in categories):
        raise ValueError("Unknown category ID; use --list-categories for available categories.")
    return tuple(row["name"] for row in CATALOG
                 if row["name"] in names or row["category"].split()[0] in categories)


def default_destination():
    """Use the current documented Codex user-scope discovery directory."""
    return Path.home() / ".agents" / "skills"


def install(source_root, destination, names, dry_run=False):
    """Preflight all packages, stage copies, and roll back only newly added folders."""
    source_root = Path(source_root).resolve()
    destination = Path(destination).expanduser().resolve()
    names = tuple(names)
    if not names or len(set(names)) != len(names) or any(n not in SKILLS for n in names):
        raise ValueError("Select supported skill names without duplicates.")
    if destination == source_root or source_root in destination.parents:
        raise ValueError("The installation destination must be outside the source skills directory.")
    if destination.exists() and not destination.is_dir():
        raise ValueError("The destination must be a directory.")

    plan = []
    for name in names:
        source = source_root / name
        if source.is_symlink() or not source.is_dir():
            raise ValueError("Missing or symlinked source skill: " + name)
        if any(p.is_symlink() for p in source.rglob("*")):
            raise ValueError("Source packages must not contain symlinks: " + name)
        for required in ("SKILL.md", "LICENSE", "NOTICE.md"):
            if not (source / required).is_file():
                raise ValueError("Incomplete skill package: " + name + "/" + required)
        target = destination / name
        if os.path.lexists(target):
            raise FileExistsError("Refusing to overwrite existing destination: " + str(target))
        plan.append((source, target))

    if dry_run:
        return [target for _, target in plan]

    destination.mkdir(parents=True, exist_ok=True)
    created = []
    with tempfile.TemporaryDirectory(prefix=".research-skills-stage-", dir=destination) as staging:
        staged_root = Path(staging)
        for source, target in plan:
            shutil.copytree(source, staged_root / target.name)
        try:
            for _, target in plan:
                # Reserve the exact destination; mkdir never replaces a concurrently added folder.
                target.mkdir()
                created.append(target)
                for child in (staged_root / target.name).iterdir():
                    child.rename(target / child.name)
        except BaseException:
            for target in reversed(created):
                shutil.rmtree(target)
            raise
    return [target for _, target in plan]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", choices=("all",) + SKILLS, action="append",
                        help="Select one skill; repeat or combine with --category")
    parser.add_argument("--category", choices=tuple(CATEGORIES), action="append",
                        help="Select a category ID; repeat or combine with --skill")
    parser.add_argument("--all", action="store_true", help="Explicitly select every skill")
    parser.add_argument("--list", action="store_true", help="List available names without installing")
    parser.add_argument("--list-categories", action="store_true", help="List category IDs and counts without copying")
    parser.add_argument("--dest", type=Path, default=default_destination(),
                        help="Parent skill directory; default: ~/.agents/skills (use --dest for other hosts)")
    parser.add_argument("--dry-run", action="store_true", help="Show targets without writing files")
    args = parser.parse_args()
    if args.list and args.list_categories:
        parser.error("Choose --list or --list-categories, not both.")
    if args.list_categories:
        if args.skill or args.category or args.all:
            parser.error("--list-categories only lists the available categories.")
        for key, label in CATEGORIES.items():
            count = sum(row["category"] == label for row in CATALOG)
            print(f"{label}\t{count} skills")
        return 0
    if args.list and not (args.skill or args.category or args.all):
        print("\n".join(SKILLS))
        return 0
    choices = args.skill or []
    legacy_all = "all" in choices
    if legacy_all and (choices != ["all"] or args.category or args.all):
        parser.error("Use --skill all alone; --all is the preferred spelling.")
    try:
        names = select_skills(() if legacy_all else choices, args.category or (), args.all or legacy_all)
        if args.list:
            print("\n".join(names))
            return 0
        targets = install(REPO_ROOT / "skills", args.dest, names, args.dry_run)
    except (OSError, ValueError) as error:
        parser.exit(1, "Installation stopped: " + str(error) + "\n")
    for target in targets:
        print(("Would copy: " if args.dry_run else "Copied: ") + str(target))
    if not args.dry_run:
        print("Independent folders copied. To use them in a host, place only the selected folders in its supported skill directory.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
