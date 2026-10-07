#!/bin/bash
# Seeds the pricing a pricing-strategy run already decided, so the case can
# check whether the landing page copy quotes those prices or invents new ones.
set -euo pipefail
case_dir="$(cd "$(dirname "$0")" && pwd)"
repo_root="$(cd "$case_dir/../.." && pwd)"
src="$repo_root/examples/restaurant-inventory/founder"
mkdir -p founder
cp "$src/pricing-strategy.md" "$src/facts.md" founder/
today="$(date +%Y-%m-%d)"
for f in founder/*.md; do
  LC_ALL=C sed -i '' "s/2026-09-21/$today/g" "$f" 2>/dev/null || LC_ALL=C sed -i "s/2026-09-21/$today/g" "$f"
done
