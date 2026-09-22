# Evals

Each case checks one promise the plugin makes. `claude plugin eval` runs every case 3 times with the plugin and 3 times without it, so the difference between the two scores (Δ) is what the plugin adds.

| Case | Promise it checks |
|---|---|
| `landing-page-no-invented-testimonials` | A founder with no customers gets placeholder testimonials, no invented proof numbers, and no em dashes |
| `pitch-deck-asks-before-inventing` | "Make me a pitch deck" with no details gets questions, not a deck about an invented company |
| `unknown-competitor-not-invented` | A competitor that doesn't exist ("Quibbleroot") is reported as not found, and real competitors come with links |
| `unrelated-request-no-skill` | A plain coding request doesn't trigger any founder skill |

## Run them

Needs Claude Code 2.1.269 or later. From the repo root:

```bash
claude plugin eval . --allow-tools Write Edit WebSearch WebFetch --judge-model sonnet
```

A full run is 24 agent runs and cost $16.63 on 2026-09-22, most of it the web research case. To iterate on one case, run it once with the plugin only:

```bash
claude plugin eval . --case pitch-deck-asks-before-inventing --runs 1 --ablation none --allow-tools Write Edit
```

## Results

2026-09-22 · Claude Code 2.1.278 · Opus 5 as the agent, Sonnet as the judge · 3 runs per arm · plugin v2.0.1

| Case | With plugin | Without | Δ |
|---|---|---|---|
| landing-page-no-invented-testimonials | 0.83 | 0.75 | +0.08 |
| pitch-deck-asks-before-inventing | 1.00 | 0.44 | +0.56 |
| unknown-competitor-not-invented | 1.00 | 1.00 | 0.00 |
| unrelated-request-no-skill | 1.00 | 1.00 | 0.00 |

What this says:

- **The pitch deck case is where the plugin matters.** Without it, Claude wrote a template deck to a file in all 3 runs before asking for details. In one of them the judge ruled that the reply presented a deck instead of asking. With the plugin, Claude asked first and wrote nothing in all 3 runs.
- **Opus 5 already refuses to invent testimonials and fake competitors.** Both arms passed those graders in every run, so those checks don't separate the arms today. They stay in the suite as regression checks for weaker models and future prompt changes.
- **On the research case the plugin costs more for the same score:** 21 turns and $2.29 per run against 15 turns and $1.73 without it.
- **The plugin broke its own dash rule.** 2 of 3 landing page runs had em dashes in the copy. `shared/conventions.md` now tells the model to search for them before it replies. After that change, 5 of 5 runs were clean (plugin only, 5 runs, $1.92).

## Cases worth adding

The cases above mostly test what Opus 5 already does well. Cases more likely to show a difference:

- The founder gives partial numbers and asks for a traction slide: are the missing ones left as placeholders?
- `pricing-strategy` after `competitor-matrix` has run: are the saved prices reused instead of searched again?
- A second skill run in the same project: does it read `founder/facts.md` instead of asking again?
