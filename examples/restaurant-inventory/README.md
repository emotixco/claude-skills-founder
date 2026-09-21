# Example: restaurant inventory SaaS

Three skills run in sequence on one idea, in an empty project. The files in [`founder/`](./founder/) are exactly what the skills wrote. Nothing was edited.

```
/founder:validate-idea B2B SaaS for restaurant inventory, targeting independent restaurants with 1-3 locations
/founder:competitor-matrix B2B SaaS for restaurant inventory, targeting independent restaurants with 1-3 locations
/founder:pricing-strategy B2B SaaS for restaurant inventory, targeting independent restaurants with 1-3 locations
```

Run on 2026-09-21 with Claude Opus 5 in Claude Code 2.1.268. The three runs took 12 minutes and cost $7.67 in API usage.

## What to look at

- [`validate-idea.md`](./founder/validate-idea.md) scores the idea 15/35 and recommends a pivot: sell recovered money from invoice audits instead of inventory software.
- [`competitor-matrix.md`](./founder/competitor-matrix.md) covers 8 competitors. Prices come from their pricing pages, dated. Where a vendor doesn't publish a price, it says so.
- [`pricing-strategy.md`](./founder/pricing-strategy.md) reuses the matrix's prices instead of searching again. It also disagrees with `validate-idea`: it keeps the recovery idea as a guarantee but rejects revenue share as the billing model, and corrects the $1M ARR estimate from 420 to 678 locations.
- [`facts.md`](./founder/facts.md) holds only what was given in the input, plus the question the skills couldn't answer: the founder's background.

## What we checked, and what we found

- All 32 links were requested on 2026-09-21. 22 returned 200 and 9 returned 403 from sites that block automated requests (Capterra, PitchBook, Toast, Restaurant365, Dining Alliance). One timed out and was opened by hand.
- Three claims were checked against their sources and match: MarginEdge's $80M Series D (August 11, 2026, $162M total, 13,000+ restaurants), MarginEdge's $350 per location price, and MarketMan's launch inside Square (April 2, 2026).
- `validate-idea` quotes MarginEdge at "around $330/mo" from a third-party comparison. `competitor-matrix` took $350 from MarginEdge's own pricing page. The official page is right.
- `pricing-strategy` is 1,646 words against its 1,500-word limit.
- Unit economics in `pricing-strategy` are estimates and are labeled as estimates. Check them against your own costs before using them.
