#!/bin/bash
# Seeds a founder/ folder with one fresh file and one that has gone stale,
# so the case can check what the status skill reports and what it flags.
set -euo pipefail
mkdir -p founder
today="$(date +%Y-%m-%d)"
old="$(date -d '60 days ago' +%Y-%m-%d 2>/dev/null || date -v-60d +%Y-%m-%d)"

cat > founder/facts.md <<EOF
# Facts the founder stated

One fact per line, with the date recorded and the skill that recorded it.

- $today · product-brief · Lanemark sells route planning software to independent trucking fleets with 5 to 30 trucks.
- $today · product-brief · 212 fleets are in the private beta.
- $today · product-brief · Monthly recurring revenue is \$2,100.
- $old · competitor-matrix · The nearest competitor charges \$49 per truck per month.

## Open questions

- $today · product-brief · Whether the two co-founders are both full time. Not stated.
EOF

cat > founder/competitor-matrix.md <<EOF
<!-- /founder:competitor-matrix · $old · input: route planning for small trucking fleets -->

# Competitor matrix: route planning for small trucking fleets

Assumption: US market. All prices checked $old.

## 1. Market landscape

**Samsara** (samsara.com)
Pricing: \$49 per truck per month on the fleet plan, checked $old.

## 5. Strategic recommendations

**Position to own:** dispatch for fleets too small for enterprise telematics.
EOF

cat > founder/product-brief.md <<EOF
<!-- /founder:product-brief · $today · input: route planning for independent trucking fleets -->

# Product brief: Lanemark

**Value proposition:** Lanemark plans tomorrow's routes for a 20 truck fleet in ten minutes, unlike enterprise telematics priced for 500 truck fleets.

**Success metrics:** 50 paying fleets within 90 days. Price per truck is [price not decided].
EOF
