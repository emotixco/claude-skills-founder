#!/usr/bin/env python3
"""Check every SKILL.md the way something other than Claude Code would read it.

`claude plugin validate` is lenient about frontmatter: it passed a skill whose
description held an unquoted colon, which strict YAML rejects outright. The
directories that index these files are not lenient, so this runs the checks
that catch that class of mistake before it ships.

    python3 .github/scripts/check_skills.py

Exits 1 and lists every problem it found.
"""
from __future__ import annotations

import pathlib
import re
import sys

DASHES = {chr(0x2014): "em dash", chr(0x2013): "en dash"}  # written as code points so this file passes its own rule
TEXT_SUFFIXES = {".md", ".json", ".yml", ".yaml", ".py", ".sh"}


def frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 3)
    return text[4:end] if end != -1 else None


def check_skills(root: pathlib.Path, problems: list[str]) -> int:
    try:
        import yaml
    except ImportError:
        problems.append("pyyaml is not installed, so frontmatter was not parsed")
        return 0
    paths = sorted(root.glob("skills/*/SKILL.md"))
    if not paths:
        problems.append("no skills found under skills/*/SKILL.md")
    for p in paths:
        rel = p.relative_to(root)
        folder = p.parent.name
        fm = frontmatter(p.read_text(encoding="utf-8"))
        if fm is None:
            problems.append(f"{rel}: no frontmatter block")
            continue
        try:
            data = yaml.safe_load(fm)
        except yaml.YAMLError as e:
            first = str(e).splitlines()[0]
            problems.append(
                f"{rel}: frontmatter is not valid YAML ({first}). "
                "A value holding a colon, a hash or a quote needs quoting"
            )
            continue
        if not isinstance(data, dict):
            problems.append(f"{rel}: frontmatter is not a mapping")
            continue
        name = data.get("name")
        if name != folder:
            problems.append(f"{rel}: name is {name!r} but the folder is {folder!r}")
        desc = data.get("description")
        if not isinstance(desc, str) or not desc.strip():
            problems.append(f"{rel}: description is missing or not text")
        elif len(desc) > 1024:
            problems.append(f"{rel}: description is {len(desc)} characters, keep it under 1024")
    return len(paths)


def check_dashes(root: pathlib.Path, problems: list[str]) -> None:
    import subprocess

    out = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
        cwd=root,
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split()
    for rel in out:
        p = root / rel
        if p.suffix.lower() not in TEXT_SUFFIXES or not p.is_file():
            continue
        if rel.startswith("examples/"):
            continue  # unedited skill output, published as it came back
        text = p.read_text(encoding="utf-8", errors="replace")
        for ch, label in DASHES.items():
            if ch in text:
                line = text[: text.index(ch)].count("\n") + 1
                problems.append(f"{rel}:{line}: {label}, which this repo does not use")


def main() -> int:
    root = pathlib.Path(__file__).resolve().parents[2]
    problems: list[str] = []
    count = check_skills(root, problems)
    check_dashes(root, problems)
    if problems:
        print(f"{len(problems)} problem(s):\n")
        for p in problems:
            print(f"  {p}")
        return 1
    print(f"{count} skills checked, frontmatter parses, no stray dashes.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
