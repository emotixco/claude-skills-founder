#!/bin/bash
# Seeds founder/facts.md the way an earlier skill run would have left it.
set -euo pipefail
today="$(date +%Y-%m-%d)"
mkdir -p founder
cat > founder/facts.md <<EOF
# Facts the founder stated

One fact per line, with the date recorded and the skill that recorded it.

- $today · product-brief · Lanemark sells route planning software to independent trucking fleets with 5 to 30 trucks.
- $today · product-brief · 212 fleets are in the private beta.
- $today · product-brief · Monthly recurring revenue is \$2,100.
- $today · product-brief · Week 4 retention is 61 percent.
- $today · product-brief · Two co-founders, both full time, one was a dispatcher for 9 years.
- $today · product-brief · Raising \$500K as a pre-seed round on a SAFE.
EOF
