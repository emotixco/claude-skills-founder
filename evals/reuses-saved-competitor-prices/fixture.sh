#!/bin/bash
# Seeds the workspace with a competitor matrix an earlier skill run saved,
# so the case can check whether the next skill reuses it instead of searching again.
set -euo pipefail
case_dir="$(cd "$(dirname "$0")" && pwd)"
repo_root="$(cd "$case_dir/../.." && pwd)"
src="$repo_root/examples/restaurant-inventory/founder"
mkdir -p founder
cp "$src/competitor-matrix.md" "$src/validate-idea.md" "$src/facts.md" founder/
# Keep the saved prices inside the 30 day window the pricing skill re-checks after.
today="$(date +%Y-%m-%d)"
for f in founder/*.md; do
  LC_ALL=C sed -i '' "s/2026-09-21/$today/g" "$f" 2>/dev/null || LC_ALL=C sed -i "s/2026-09-21/$today/g" "$f"
done
