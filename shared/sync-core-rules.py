#!/usr/bin/env python3
"""Copy shared/core-rules.md into every skill, between the markers.

Each SKILL.md carries the rules inline because a skill that only points at
shared/conventions.md is a skill whose rules a smaller model never reads.
See evals/reads-the-shared-rules for the measurement behind that.

Run from the repo root after editing shared/core-rules.md:

    python3 shared/sync-core-rules.py          # writes
    python3 shared/sync-core-rules.py --check   # fails if any skill is stale
"""
import pathlib
import sys

START = "<!-- core-rules:start -->"
END = "<!-- core-rules:end -->"
ROOT = pathlib.Path(__file__).resolve().parent.parent


def block() -> str:
    body = (ROOT / "shared" / "core-rules.md").read_text(encoding="utf-8").strip()
    return f"{START}\n\n{body}\n\n{END}"


def main() -> int:
    check = "--check" in sys.argv
    wanted = block()
    stale, written = [], []
    for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
        text = skill.read_text(encoding="utf-8")
        if START not in text or END not in text:
            print(f"no markers: {skill.relative_to(ROOT)}")
            return 1
        head, rest = text.split(START, 1)
        _, tail = rest.split(END, 1)
        new = head + wanted + tail
        if new == text:
            continue
        if check:
            stale.append(skill.relative_to(ROOT))
        else:
            skill.write_text(new, encoding="utf-8")
            written.append(skill.relative_to(ROOT))
    if check and stale:
        print("stale, run python3 shared/sync-core-rules.py:")
        for p in stale:
            print(f"  {p}")
        return 1
    print(f"{len(written)} skill(s) updated" if not check else "all skills current")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
