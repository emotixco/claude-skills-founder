# Changelog

## 2.1.3 · 2026-10-07

- New eval case `reads-the-shared-rules`: does a skill actually open `${CLAUDE_PLUGIN_ROOT}/shared/conventions.md` and follow two rules that live only there, the saved file header and the no-dash rule.
- The case found that on Haiku 4.5 the shared rules never load: with the plugin, Haiku opened the file in 0 of 3 runs, wrote no `founder/` file, and used em dashes in every run. On Opus 5 the same case is 1.00 against 0.11 without the plugin. `evals/README.md` has the detail and the fix worth measuring next.

## 2.1.2 · 2026-10-07

- New eval case `landing-page-matches-saved-prices`: with the tiers already decided in `founder/pricing-strategy.md`, the landing page copy has to quote $79 and $189 rather than invent its own. Opus 5 passes with and without the plugin, 3 runs each.
- `shared/conventions.md` now says to read the skill's "Reads" files before asking the founder anything, and to say what was found there. The evals caught Haiku asking what the tiers should be while the decided prices sat unopened in `founder/`.
- `evals/README.md` records that this case fails in both arms on Haiku 4.5, that its per-arm scores moved from 0.33 to 0.00 between runs, and that a single Haiku case score at 3 runs is not worth quoting alone.

## 2.1.1 · 2026-10-07

- New eval case `input-overrides-saved-fact`: the founder states an MRR that contradicts `founder/facts.md`, so the new number has to win, the reply has to say what it replaces, and the ledger has to be updated. On Opus 5 this is the one case where the plugin beats plain Claude, Δ +0.17, because without it the stale number stays in `founder/facts.md` in every run.
- `evals/README.md` records that on Haiku 4.5 the skills frequently do not fire from a described task, and that calling them by name works.

## 2.1.0 · 2026-10-07

- Three new eval cases, two of which seed `founder/` first to test whether skills reuse saved work: `reuses-saved-competitor-prices`, `uses-saved-facts-without-reasking`, and `partial-numbers-stay-placeholders`. They need `--scaffold`.
- `/founder:pitch-deck` now also triggers when you ask for one slide, such as the traction slide. The evals caught it staying silent on "write the traction slide for my pitch deck", and Claude invented a revenue figure without it.
- Issue templates for a broken install and for a new skill idea, and a line in the README asking people to report both.
- `evals/README.md` carries the full results for Opus 5 and Haiku 4.5, the per-run cost of running with the plugin, and the four grader bugs this suite has produced so far. On Opus 5 the plugin no longer changes any case outcome; on Haiku 4.5 it raises 3 of 7.

## 2.0.2 · 2026-09-22

- Added `evals/`: 4 cases that compare the plugin with plain Claude using `claude plugin eval`. Results and what they show are in `evals/README.md`.
- `shared/conventions.md` now tells the model to search its text for em and en dashes before replying. The evals caught the dash rule failing in 2 of 3 landing page runs. After the change, 5 of 5 were clean.

## 2.0.1 · 2026-09-22

- Links to the old `commands/<name>.md` files work again. v2.0.0 moved the skills to `skills/`, so those links returned 404, including `commands/pricing-strategy.md`, which had 1,671 views in the previous 14 days. Each old path now holds a short file that points to the new location and the install steps.
- `plugin.json` sets `"commands": []`, so the plugin doesn't load those files. Without it, every skill showed up twice.
- If you still have v1 linked into `.claude/commands/`, running an old command now shows how to install v2 instead of "Unknown command".

## 2.0.0 · 2026-09-21

Breaking: the skills moved from `commands/*.md` to `skills/<name>/SKILL.md`, and the repo is now a Claude Code plugin. v1 copies in `.claude/commands/founder/` no longer update. See "Upgrading from v1" in the README.

- Install with `/plugin marketplace add emotixco/claude-skills-founder` and `/plugin install founder@emotix`, or clone into `~/.claude/skills/founder`. The v1 install commands failed on machines where `.claude/commands` didn't exist yet.
- Skills save their output to `founder/` in your project and read each other's files. Facts you state once are kept in `founder/facts.md`.
- Competitor prices, funding rounds, market sizes, and benchmarks need a source link, or they're marked as estimates. Nine skills pre-approve web search to find them.
- Your own metrics, quotes, and testimonials are never invented. Missing ones become bracketed placeholders.
- A skill run with no input asks for what it needs.
- `/founder:pitch-deck` asks whether the deck is presented live or sent ahead, writes a takeaway headline and speaker notes for every slide, and ends with a list of numbers to find. Based on #1 by @Haoyang0708.
- Removed invented track records from the skill prompts, such as "45% open rates" and "80+ decks".
- Rules shared by every skill live in `shared/conventions.md`.
- README: skill count corrected from 12 to 13, and a new `examples/` folder with unedited output.

## 1.0.0 · 2026-03-10

- First release: 13 commands for startup founders. The README said 12.
