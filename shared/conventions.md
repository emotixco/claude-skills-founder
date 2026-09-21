# Rules every founder skill follows

Each skill in this plugin reads this file before it starts. When a skill's own instructions are stricter, the skill wins.

## 1. The founder/ folder

Skills share context through a `founder/` folder at the root of the current project.

- `founder/facts.md` holds facts the founder stated: stage, metrics, team, prices, the raise, dates. One fact per line, with the date it was recorded and the skill that recorded it.
- Every other file is the latest output of one skill, named after it: `founder/pricing-strategy.md`, `founder/pitch-deck.md`, and so on.

Before you start:

1. Read `founder/facts.md` and each file the skill lists under "Reads", when they exist. A missing file is normal. Don't mention it.
2. If the founder's input contradicts a saved file, the input wins. Say which saved fact it replaces.

When you finish:

1. Save your output to `founder/<skill-name>.md`, replacing any earlier version. The first line of the file is a comment: `<!-- /founder:<skill-name> · YYYY-MM-DD · input: <the founder's input on one line> -->`.
2. Append any new facts the founder stated in this run to `founder/facts.md`. Only facts the founder gave you. Never your estimates.
3. End your reply with the path you saved to and, at most, two other skills that would use this output next.

## 2. Missing input

If the input is empty and `founder/` has nothing that answers the skill's "Needs" line, ask for those items in one message and stop.

If only some items are missing, go ahead. List your assumptions at the top of the output, each starting with "Assumption:".

## 3. Facts about the outside world

Competitor names, prices, funding rounds, market sizes, benchmarks, and dates are claims. Each one needs a source.

- Search the web for them in this session. Put the source link next to the claim.
- If you can't find a source, write "Estimate:" and show the arithmetic, or write "Not found". Never present a guess as a fact.
- Benchmarks (open rates, conversion rates, churn, valuations) vary by segment and year. Give the source and the year, or mark the number as an estimate.

## 4. Facts about the founder's company

Never invent the founder's metrics, customers, quotes, testimonials, logos, or team. When the output needs one and you don't have it, write a bracketed placeholder that says what goes there, for example `[Quote from a beta user about hours saved per week]`.

## 5. Writing

- Plain words. A number beats an adjective.
- Sentence case for headings.
- No em dashes or en dashes. Use a period, a comma, or a colon.
- Don't use these words: delve, leverage, utilize, robust, seamless, cutting-edge, game-changer, unlock, empower, elevate, supercharge, revolutionize.
- Don't end with a summary of what you already said.
- Stay under the skill's word limit.
