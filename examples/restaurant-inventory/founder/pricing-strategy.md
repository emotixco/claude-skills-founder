<!-- /founder:pricing-strategy · 2026-09-21 · input: B2B SaaS for restaurant inventory, targeting independent restaurants with 1-3 locations -->

# Pricing strategy: restaurant inventory SaaS for 1-3 location independents

Assumption: US market, per location per month, USD. All costs are estimates, none vendor-quoted. Competitor prices reused from `founder/competitor-matrix.md`, checked 2026-09-21.
Assumption: the product leads with the invoice-based recovery report, counting behind it. If you are building count-first, these prices are unreachable.

## 1. Pricing model analysis

| Model | Fit | Pros | Cons |
|---|---|---|---|
| Flat subscription | 5 | How the segment already buys. Forecastable, no bill shock in a heavy ordering month. | Caps upside on a 3-location customer getting 3x the value. |
| Usage-based (per invoice, % of spend) | 3 | Scales with the value driver. | An operator who hides invoices to cut the bill destroys the dataset the product runs on. |
| Per-seat | 1 | None. | The buyer is the owner. 1 to 2 users. Friction for a rounding error. |
| Freemium | 4 | The free 90-day audit is already your outreach hook and doubles as top of funnel. | ~$31 per audit. Uncapped, it is a marketing budget disguised as a product. |
| Credits | 1 | None. | An owner-operator will not manage a balance for a back-office chore. |
| One-time purchase | 1 | None. | The value is continuous monitoring. A one-time sale removes your reason to keep watching. |

**Recommendation: flat subscription per location, free one-time audit as the entry point.** Because the segment has an established flat anchor at $249 to $500 and no room for a meter. Spend your advantage on being visibly cheaper than MarketMan, not on a model the buyer works out on a napkin.

**The rev-share model in `founder/validate-idea.md` is right as a proof mechanic, wrong as the billing model.** Taking 20-30% of recovered money fails on collection, not on appeal: you cannot invoice against a credit until the distributor issues it, and you control neither that decision nor its timing. Keep the promise, bill it as a guarantee on a flat fee.

## 2. Tier design

### Audit. Free, one time.

Upload 90 days of invoices, get one report naming the dollars of price creep, duplicate charges and off-contract pricing found.

- Up to 150 invoices, one location, one report
- Line-item extraction on every invoice
- Vendor price history across the 90 days uploaded
- Pre-drafted credit request emails, one per vendor
- Top 20 items ranked by spend
- No POS connection, no card

**Upgrade trigger:** price creep is continuous, so the report has a shelf life of about three weeks. When they want the next one, they are on Watchdog.

Gate it behind a business email and one POS or accounting connection. At $31 a run, an ungated audit is free labor for consultants and competitors.

### Watchdog. $79/mo, or $790/yr ($65.83/mo, 17% off).

- Weekly recovery report, Friday, one number at the top
- 150 invoices/month, then $0.35 each
- Price-change alerts within 24 hours of an invoice landing
- Pre-drafted credit requests, tracked to resolution
- Sales sync: Square, Clover, Toast
- QuickBooks Online and Xero sync
- Unlimited users, no setup fee, no sales call
- No counting required anywhere in this tier

**Upgrade trigger:** they ask what a plate costs, or why cost of goods moved when purchasing did not. Both need recipes.

### Control. $189/mo, or $1,890/yr ($157.50/mo, 17% off). Self-serve.

Everything above, plus:

- Recipe and menu costing, unlimited, repriced on every invoice
- Menu margin ranking, weekly
- Par-based ordering with one-click POs
- Count app, optional
- Theoretical vs actual variance, once counts exist
- Unlimited invoices
- Locations 2 and 3 at $149/mo each (21% off), with cross-location vendor price comparison

**Upgrade trigger:** a fourth location or multi-entity accounting. Both out of segment. Refer to Restaurant365 for a fee: a 4-location group with a bookkeeper cannot be served at $189 self-serve.

Keep Control self-serve. "No sales call" is the gap named in the matrix, and the only structural advantage $189 has over $350 with a sales team.

## 3. Competitive pricing context

All checked 2026-09-21.

| Competitor | Price and inclusions | You sit |
|---|---|---|
| [Kosto](https://kosto.app/) | $29 / $59. Invoice audit and price alerts only. | **Above.** $79 adds POS sync, accounting sync, tracked recovery. Never undercut $59. |
| [MarketMan](https://www.marketman.com/pricing-for-restaurant-inventory-management-system) | $249 / $299 / $449+, full platform. Starter caps scans at 50/mo. | **Below at both tiers.** $189 is 24% under Starter with unlimited invoices. Lead with the cap, not the price: 50/month is under what one location receives. |
| [MarginEdge](https://www.marginedge.com/pricing/) | $350, 10% off annual, no setup fee. Invoices keyed by their team, daily P&L, AP and bill pay. | **Below, deliberately.** Your anchor (section 5). Do not chase AP and bill pay: their moat, and a money-transmission problem. |
| [WISK.ai](https://www.wisk.ai/price) | $249 single venue, $399 bundle, plus $750 setup. Beverage-first. | **Below and adjacent.** Put "no setup fee" in the same type size as your price. |
| [Restaurant365](https://www.capterra.com/p/139768/Restaurant365/pricing/) | ~$469-499 / ~$689-749, quarterly, unpublished. Accounting and payroll. | **Far below, different buyer.** Your ceiling in the comparison table, and your referral exit. |

$79 prices against Kosto, $189 against MarketMan Starter, nothing against MarginEdge. The $59-to-$249 hole is the only unoccupied ground here.

## 4. Unit economics check

All estimates. Re-run at 20 live locations. Volume: 80 invoices/location/month at Watchdog, 120 at Control, 2 pages each (from 3-4 deliveries/week across 5-8 vendors).

**Watchdog, $79/mo.** Extraction 80 × 2pp × $0.06 = $9.60. Review of low-confidence lines 15% × 80 = 12 × 3 min × $12/hr = $7.20. Hosting $1.50. Stripe 2.9% × $79 + $0.30 = $2.59. Support 0.2 tickets × 15 min × $25/hr = $1.25. **COGS $22.14. Margin (79 − 22.14) / 79 = 72%.**

**Control, $189/mo.** Extraction 120 × 2 × $0.06 = $14.40. Review 18 × 3 min × $12/hr = $10.80. Hosting $2.50. Stripe 2.9% × $189 + $0.30 = $5.78. Support 0.5 tickets × 20 min × $25/hr = $4.17. **COGS $37.65. Margin 80%.**

**Free audit.** 150 × 2 × $0.06 = $18.00, plus 22 × 3 min × $12/hr = $13.20. **$31.20 per audit.** That is CAC, not COGS. At 25% audit-to-paid it is $125 per customer, well inside the $800-$1,500 blended CAC assumed in `founder/validate-idea.md`, and the strongest argument for the free tier.

**Break-even.** Fixed monthly: $400 infrastructure, $300 tooling, $2,500 part-time ops contractor for invoice review and onboarding = **$3,200/mo**, founder salary excluded.

- Watchdog only: $3,200 / $56.86 = **57 locations**
- Control only: $3,200 / $151.35 = **22 locations**
- 60/40 mix, blended contribution $94.66 = **34 locations**

**Target blended ARPU: $123/location/month** ($79 × 0.6 + $189 × 0.4) = $1,476 ARR per location. So $1M ARR is 678 retained locations, not the 420 estimated in `founder/validate-idea.md` against a $200 assumption. Plan against 678.

## 5. Pricing psychology

**Anchoring: MarginEdge's $350 is the anchor, not one of your tiers.** Add a fourth column headed "Typical full platform" at $350, sourced and dated. Control at $189 anchors internally, to make $79 trivial. A buyer comparing $79 to nothing evaluates price. One comparing $79 to $189 to $350 evaluates position.

**Decoy: the counting add-on.** Show "Watchdog + count app, $139/mo". Deliberately bad value: $60 for one feature, when $50 more buys recipes, ordering, variance and unlimited invoices. It pushes buyers into the 80% margin tier. Expect almost nobody to buy it. That is the design.

**Annual framing: "two months free," never "17% off."** $790 is $79 × 10, so say that: this operator prices a discount in units of time. Offer it at the second renewal month, not at signup. Asking a segment where 42% were unprofitable in 2025 ([NRN](https://www.nrn.com/independent-restaurants/the-independent-restaurant-sector-shrunk-by-2-3-in-2025)) for $790 on day one converts worse than it retains.

## 6. Launch pricing vs. scale pricing

**First 90 days: keep $79 and $189. Do not discount. Sell the guarantee.** "If we do not find at least 3x your monthly fee in recoverable and avoidable cost in your first 60 days, the first six months are free."

Because the objection here is belief, not budget. Discounting to $39 answers a question nobody asked and teaches the market your price is soft. The guarantee costs $22.14/mo where you are wrong, on customers you want identified fast. Track claim rate as the primary launch metric: above 20%, the product thesis is wrong and no pricing fixes it.

One exception: **the first 25 locations get $59 and $149, locked 24 months, capped at 25 and stated publicly as capped.** Design partners give you invoice volume and vendor catalog coverage, the real moat named in `founder/validate-idea.md`. Not lifetime, which is a liability you carry into your own diligence.

**Grandfathering.** Price held 12 months from signup. At renewal, move to current list with 60 days notice and one email showing the dollars recovered that year next to the increase. Never raise mid-term, or on a customer with an open ticket from the prior 30 days.

**Raise price when all three hold for two consecutive months:**

1. 90-day logo retention above 85%. Below that, a rise on a leaky bucket accelerates the leak.
2. Median recovered dollars per location per month above $800, 10x the Watchdog fee. That ratio makes the increase defensible in one sentence.
3. Free-audit-to-paid conversion above 30%. Below that, demand cannot absorb a move.

Then take new-customer list to $99 and $229, leave existing customers on their anniversary schedule, once a year at most.

**The one trigger to move faster:** MarketMan launching a sub-$100 invoice-only tier inside Square. The correct response is up, not down. Move Watchdog to $129 with vendor catalog benchmarking they cannot match without your data, and stop competing at the bottom, where Square's distribution beats you.
