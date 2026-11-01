# Gallery

Five ideas, run through the skills end to end, with every file the run produced. Nothing is edited, including the parts that are wrong or hedged.

Most skill repositories show you the prompt. This shows you what came back, what it cost, and what we could not verify.

| Example | Chain | Verdict | Cost |
|---|---|---|---|
| [Physiotherapy scheduling, UK](./physio-scheduling/) | validate, competitors, pricing | Pivot to a waitlist filler on top of Cliniko | $3.73 |
| [Office coffee, Baku](./office-coffee/) | validate, personas, go to market | Pivot to the service company first | $3.23 |
| [Cozy puzzle game, solo dev](./cozy-puzzle/) | validate, MVP scope, metrics | Pivot the channel to PC and Switch | $3.05 |
| [A social network for dogs](./pet-social/) | validate | Kill it | $1.05 |
| [Restaurant inventory, US](./restaurant-inventory/) | validate, competitors, pricing | Pivot to selling recovered money | $7.67 |

## How these were produced

The four newer examples ran on 2026-11-01 with Claude Code 2.1.316, Opus 5 as the agent, in an empty directory with the plugin loaded and nothing else. The restaurant example ran on 2026-09-21 on an earlier version, which is why its cost per run is higher.

Each run is a plain command, the way a user would type it:

```
/founder:validate-idea <the idea, in one or two sentences>
```

## What the gallery is evidence for

**The `founder/` folder is the point.** In the physiotherapy example the pricing skill writes: "All prices from `founder/competitor-matrix.md`, checked 2026-11-01. None are older than 30 days, so none were re-checked." The second skill reused the first skill's research instead of paying to search again. The eval suite measures the same behaviour; here you can read it.

**Sources or nothing.** Competitor prices, funding and market numbers carry a link and a date. Where a number could not be confirmed, the text says "Not found" or marks the figure an estimate and shows the arithmetic.

**It says no.** One example is here because the skills killed the idea rather than scoping it.

**It does not score what it does not know.** Three of the four scorecards leave founder fit unscored and ask for it, because the input said nothing about the founder.

## Link checking

All 90 links cited across the four newer examples were requested on 2026-11-01. 72 returned 200. 13 returned 403, which is bot blocking by sites such as Dealroom, Nintendo Life and Daily Coffee News rather than a broken citation. One returned 410 and one timed out, both in the physiotherapy example and both backing minor claims the text already hedges. The rest were rate limits or server errors on the day.

A cited page is a snapshot. Check anything you are about to put in front of an investor.
