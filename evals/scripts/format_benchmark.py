#!/usr/bin/env python3
"""Turn one `claude plugin eval --json` result into the rows of evals/benchmark.md.

Usage:
    python3 evals/scripts/format_benchmark.py results.json [--label weekly]

Writes evals/benchmark.md: the latest run in full, then one history row per run.
Reads only fields the documented schema guarantees, and says "n/a" for anything
a run left out, so a schema addition never breaks the page.
"""
import json
import pathlib
import sys
from datetime import date

PAGE = pathlib.Path("evals/benchmark.md")
HISTORY_START = "<!-- history:start -->"
HISTORY_END = "<!-- history:end -->"


def num(v, places=2, dash="n/a"):
    return f"{v:.{places}f}" if isinstance(v, (int, float)) else dash


def delta(v):
    if not isinstance(v, (int, float)):
        return "n/a"
    return f"{v:+.2f}" if v else "0.00"


def main() -> int:
    args = sys.argv[1:]
    if not args:
        print("usage: format_benchmark.py results.json [--label weekly]")
        return 1
    label = "weekly"
    if "--label" in args:
        i = args.index("--label")
        label = args[i + 1]
        args = args[:i] + args[i + 2:]
    d = json.loads(pathlib.Path(args[0]).read_text(encoding="utf-8"))

    cases = d.get("cases", [])
    agg = d.get("aggregates", {})
    model = (d.get("config", {}) or {}).get("model") or d.get("model") or "n/a"
    judge = (d.get("config", {}) or {}).get("judgeModel") or "n/a"
    when = date.today().isoformat()
    partial = " (partial run: %s)" % d.get("partialReason") if d.get("partial") else ""

    rows = ["| Case | With plugin | Without | Delta |", "|---|---|---|---|"]
    for c in sorted(cases, key=lambda c: c.get("name", "")):
        ca = c.get("aggregates", {})
        rows.append(
            f"| `{c.get('name','?')}` | {num(ca.get('score'))} | "
            f"{num(ca.get('score', 0) - ca['delta']) if isinstance(ca.get('delta'), (int, float)) and isinstance(ca.get('score'), (int, float)) else 'n/a'} | "
            f"{delta(ca.get('delta'))} |"
        )

    latest = f"""## Latest run

{when} · {label} · agent {model} · judge {judge} · Claude Code {d.get('claudeVersion','n/a')}{partial}

{chr(10).join(rows)}

Suite score {num(agg.get('overallScore'))}, mean delta {delta(agg.get('meanDelta'))}, \
{agg.get('casesPassed','n/a')} of {agg.get('casesTotal','n/a')} cases at threshold, \
{num(d.get('costUsd'))} USD, {int(d.get('durationSeconds') or 0)}s.
"""

    history_row = (
        f"| {when} | {label} | {model} | {num(agg.get('overallScore'))} | "
        f"{delta(agg.get('meanDelta'))} | {agg.get('casesPassed','n/a')}/{agg.get('casesTotal','n/a')} | "
        f"{num(d.get('costUsd'))} |"
    )

    header = """# Benchmark

What the plugin scores against plain Claude, re-measured on a schedule rather than quoted once. \
A case's score is the share of its graders that passed, averaged over its runs. Delta is the \
with-plugin score minus the same cases run with no plugin loaded, so a delta of zero means \
Claude did as well without us.

Losses stay on this page. See [README](./README.md) for what each case checks and how the \
suite is run.
"""

    if PAGE.exists():
        old = PAGE.read_text(encoding="utf-8")
        before, rest = old.split(HISTORY_START, 1)
        _, after = rest.split(HISTORY_END, 1)
        history_body = rest.split(HISTORY_END, 1)[0].strip().split("\n")
        existing = [ln for ln in history_body if ln.startswith("| 2")]
    else:
        after = ""
        existing = []

    history = [
        "| Date | Run | Agent model | Suite score | Mean delta | Cases at threshold | Cost |",
        "|---|---|---|---|---|---|---|",
        history_row,
    ] + existing

    PAGE.write_text(
        f"{header}\n{latest}\n## History\n\n{HISTORY_START}\n"
        + "\n".join(history)
        + f"\n{HISTORY_END}\n{after.lstrip()}",
        encoding="utf-8",
    )
    print(f"wrote {PAGE} for {when} {label}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
