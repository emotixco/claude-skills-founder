# Evals

Each case checks one promise the plugin makes. `claude plugin eval` runs every case 3 times with the plugin and 3 times without it, so the difference between the two scores (Δ) is what the plugin adds.

| Case | Promise it checks |
|---|---|
| `landing-page-no-invented-testimonials` | A founder with no customers gets placeholder testimonials, no invented proof numbers, and no em dashes |
| `pitch-deck-asks-before-inventing` | "Make me a pitch deck" with no details gets questions, not a deck about an invented company |
| `partial-numbers-stay-placeholders` | The numbers the founder has are used; the revenue they don't have stays a placeholder |
| `unknown-competitor-not-invented` | A competitor that doesn't exist ("Quibbleroot") is reported as not found, and real competitors come with links |
| `reuses-saved-competitor-prices` | With a competitor matrix already in `founder/`, pricing reuses those prices instead of searching again |
| `uses-saved-facts-without-reasking` | Facts already in `founder/facts.md` are used, not asked for a second time |
| `input-overrides-saved-fact` | The founder states an MRR that contradicts `founder/facts.md`. The new number wins, the reply says which saved fact it replaces, and the ledger is updated |
| `landing-page-matches-saved-prices` | Pricing already decided $79 and $189 tiers. The landing page copy quotes those, and doesn't invent its own |
| `reads-the-shared-rules` | A skill opens `${CLAUDE_PLUGIN_ROOT}/shared/conventions.md` and follows two rules that live only there: the saved file's header format, and no em dashes |
| `unrelated-request-no-skill` | A plain coding request doesn't trigger any founder skill |

The last five cases seed the workspace first, from `fixture.sh` in the case directory, so they need `--scaffold`. Two of them copy the real output in `examples/restaurant-inventory/` and rewrite its dates to today, so the saved prices stay inside the 30 day window the pricing skill re-checks after.

## Run them

Needs Claude Code 2.1.269 or later. From the repo root:

```bash
claude plugin eval . --scaffold --allow-tools Write Edit WebSearch WebFetch --judge-model sonnet
```

A full run is 42 agent runs and cost $11.61 on 2026-10-07. To iterate on one case, run it once with the plugin only:

```bash
claude plugin eval . --case pitch-deck-asks-before-inventing --runs 1 --ablation none --allow-tools Write Edit
```

`--case` takes one glob and does not repeat: a second `--case` replaces the first.

## Results

2026-10-07 · Claude Code 2.1.292 · Sonnet as the judge · 3 runs per arm · plugin v2.1.0

### Opus 5 as the agent

| Case | With plugin | Without | Δ |
|---|---|---|---|
| landing-page-no-invented-testimonials | 1.00 | 1.00 | 0.00 |
| partial-numbers-stay-placeholders | 1.00 | 1.00 | 0.00 |
| pitch-deck-asks-before-inventing | 1.00 | 1.00 | 0.00 |
| reuses-saved-competitor-prices | 1.00 | 1.00 | 0.00 |
| unknown-competitor-not-invented | 1.00 | 1.00 | 0.00 |
| unrelated-request-no-skill | 1.00 | 1.00 | 0.00 |
| uses-saved-facts-without-reasking | 1.00 | 1.00 | 0.00 |
| input-overrides-saved-fact | 1.00 | 0.83 | +0.17 |
| landing-page-matches-saved-prices | 1.00 | 1.00 | 0.00 |
| reads-the-shared-rules | 1.00 | 0.11 | +0.89 |

**One case separates the arms on Opus 5: `input-overrides-saved-fact`, at Δ +0.17.** When the founder states an MRR that contradicts the saved one, both arms use the new number and both mention the old one. The difference is the ledger: with the plugin, all 3 runs wrote the new figure into `founder/facts.md`, and without it, none of the 3 did. The next session that reads that file gets the stale number.

`reads-the-shared-rules` is the largest Δ in the suite, and part of it is tautological: saving to `founder/persona-gen.md` with a particular header is a rule only the plugin states, so plain Claude cannot pass that grader. The part that is not tautological is the dash rule, which lives in the same file: 2 of 3 runs without the plugin put em dashes in the personas, and 0 of 3 with it did.

**On the other eight cases the plugin changes nothing these cases can measure.** Plain Claude keeps the placeholders, says a fake competitor is fake, reads the files sitting in `founder/`, and asks before inventing a company. What the plugin still does is make that the default every time, in the same structure, saved to the same place. That is worth something, and it is not what these graders measure.

It also costs more. Per run, with the plugin against without:

| Case | Turns | Cost |
|---|---|---|
| uses-saved-facts-without-reasking | 10 vs 4 | $0.54 vs $0.09 |
| unknown-competitor-not-invented | 17 vs 6 | $1.20 vs $0.64 |
| reuses-saved-competitor-prices | 9 vs 6 | $0.36 vs $0.17 |
| landing-page-no-invented-testimonials | 8 vs 1 | $0.24 vs $0.12 |

### Haiku 4.5 as the agent

Same suite, same day, `--model haiku`, $2.89 for all 42 runs.

| Case | With plugin | Without | Δ |
|---|---|---|---|
| landing-page-no-invented-testimonials | 0.75 | 0.50 | +0.25 |
| reuses-saved-competitor-prices | 0.60 | 0.40 | +0.20 |
| uses-saved-facts-without-reasking | 0.17 | 0.00 | +0.17 |
| input-overrides-saved-fact | 0.33 | 0.33 | 0.00 |
| landing-page-matches-saved-prices | 0.04 | 0.00 | +0.04 |
| reads-the-shared-rules | 0.00 | 0.00 | 0.00 |
| partial-numbers-stay-placeholders | 1.00 | 1.00 | 0.00 |
| pitch-deck-asks-before-inventing | 1.00 | 1.00 | 0.00 |
| unknown-competitor-not-invented | 1.00 | 1.00 | 0.00 |
| unrelated-request-no-skill | 0.83 | 0.83 | 0.00 |

Mean Δ +0.09. On the weaker model the rules do carry weight: every Haiku run without the plugin put invented proof numbers in the landing page copy, and 3 of 3 failed to read the saved competitor matrix at all. With the plugin it read the file in all 3 runs.

**On Haiku the skills often don't fire at all.** In all 3 runs of `input-overrides-saved-fact`, Haiku answered in a single turn without invoking any skill, so the plugin never got to apply its rules. One of those runs then used the stale $2,100 as "average customer value per fleet", which is the exact mistake the ledger rule exists to prevent.

Invoked by name, the rule does land on Haiku. Running `/founder:pitch-deck` with the same prompt, Haiku replied: "your product brief from earlier shows $2,100 MRR, but you just crossed $6,400 last week with three bigger fleets signing. I'm using $6,400 as the current number." It then asked whether the deck is live or sent ahead and stopped there, so it never reached the slide or the ledger. If you run these skills on Haiku, call them by name rather than describing the task.

**`landing-page-matches-saved-prices` fails in both arms on Haiku, and its runs disagree with each other.** Asked for a pricing section with the decided prices sitting in `founder/pricing-strategy.md`, Haiku asked the founder what the tiers should be instead of opening the file, in 5 of 6 runs. One early without-plugin run did read it and scored 1.00, which pulled that arm to 0.33 before a re-run put both arms near zero. With 3 runs per arm, a single case score on Haiku is not worth quoting on its own.

One of those runs invoked the skill and then said "the skill path points to a different directory than your current project", which suggests the `${CLAUDE_PLUGIN_ROOT}` reference in every skill reads as an obstacle to a smaller model rather than a file to open.

**On Haiku the shared rules never load at all.** `reads-the-shared-rules` scores 0.00 in both arms, and the reason is in its indicator grader: with the plugin loaded, Haiku opened `${CLAUDE_PLUGIN_ROOT}/shared/conventions.md` in 0 of 3 runs. The skill itself fired in 2 of those 3, so the instruction to read the file was in front of it and went unused. Nothing in `shared/conventions.md` applied: no `founder/` file was written in any run, and every run used em dashes.

That reading was wrong, and measuring the fix is what showed it. In 2.1.4 the nine core rules were inlined into every `SKILL.md`, so Haiku no longer has to open anything to have them. It scored 0.00 again: no `founder/` file in any run, em dashes in every run, with the rules sitting in its context. Haiku does not skip the rules because they are one Read away. It skips them because they are rules.

The inlining stayed anyway, for a different reason that did measure: on Opus 5 it removes a Read from every skill run. `uses-saved-facts-without-reasking` went from 10 turns and $0.54 a run to 6 turns and $0.26, and the eight other cases held their scores.

The plugin doesn't rescue Haiku, though. `uses-saved-facts-without-reasking` scores 0.17 with the plugin, because Haiku reads `founder/facts.md` and still asks for facts that are in it.

### What changed since 2026-09-22

The first run of this suite, on Claude Code 2.1.278, showed `pitch-deck-asks-before-inventing` at Δ +0.56: plain Claude wrote a template deck to a file before asking. On 2.1.292 that no longer happens, and the case is Δ 0. The number wasn't wrong then and isn't wrong now. A plugin's measured value moves when the model and the harness underneath it move, which is the reason to keep the suite and re-run it rather than quote a number once.

## Writing graders that don't lie to you

Four of the five failures this suite has produced were grader bugs, not plugin bugs. The pattern each time:

- **The dash check read the whole session** and matched Claude Code's own tool messages ("file state is current in your context"). Grade the final reply unless you mean the transcript.
- **The plugin saves to `founder/` and replies with a summary**, while plain Claude puts everything in the reply. Grading only the reply punished the plugin for following its own rules, so the prompts now ask for the full output in the reply, which is what a user would say anyway.
- **A rubric asked for more than the skill promises.** "Leaves revenue as a placeholder and asks for it" failed a reply that correctly left the placeholder. Grade the promise, nothing extra.
- **A judge called the copy's own voice a testimonial.** The landing page skill writes pain points in the customer's words on purpose, so the rubric now says those are not testimonials.
- **A judge read "setup takes minutes" as an invented proof number.** The rubric was about numbers, so it now says that qualitative product claims are outside it. The run before and the three after all passed on copy of the same shape, which is what a borderline rubric looks like.
- **An allowlist of permitted prices failed three times in a row.** The pricing rubric listed the prices the saved strategy allows, and the copy kept using others the same file prescribes: the $350 competitor anchor, the $59 founding offer, then the count-app add-on written as "+$60" where the file says "$139 total". Define what counts as a contradiction instead of enumerating what is allowed, and let regex carry the hard check.

## Cases worth adding

- The same suite on Sonnet, to see where between Haiku and Opus the plugin stops changing the outcome.
