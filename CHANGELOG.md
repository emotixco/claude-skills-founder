# Changelog

## 2.4.1 · 2026-11-03

- Fixes the frontmatter of `/founder:status`, whose description held an unquoted colon and so was not valid YAML. Thanks to @samkelleher for catching it in #21. Claude Code reads it anyway, but anything stricter, including the directories that index these files, would have read the description as broken.
- Adds `.github/scripts/check_skills.py` and a Check workflow that runs it on every push and pull request. It parses each skill's frontmatter the way a strict reader would, confirms the name matches its folder and that a description exists, and fails on an em or en dash in a tracked text file outside `examples/`. No model calls, so nothing is billed.

## 2.4.0 · 2026-11-01

- Adds `/founder:status`. It reads the `founder/` folder and answers "where are we" in one screen: what each skill decided and how old that is, the facts on record, the open questions and placeholders, what has gone stale, and which skill to run next. It writes no file, because a saved copy would be wrong as soon as the next skill runs, and it states nothing the folder does not say.
- Adds the eval case `status-reports-the-folder`, which seeds a folder holding one file written today and one written 60 days ago, then checks that the report flags the stale prices, names a next step, keeps every number matching the files, and leaves no file behind.
- The suite is now 11 cases and the plugin 14 skills.

## 2.3.0 · 2026-11-01

- Adds a scheduled benchmark. `.github/workflows/benchmark.yml` re-runs the eval suite and publishes the result to `evals/benchmark.md`, with a history row per run and the losses left in. Weekly it runs the four chaining cases; monthly it runs the whole suite including the expensive web-research case. The agent is pinned to Sonnet and the judge to Haiku so a model rollout is not mistaken for a plugin regression.
- The workflow does nothing until an `ANTHROPIC_API_KEY` secret exists, because every run is billed to that key rather than to a Claude plan. It can also be started by hand with a model, a case glob and a cost ceiling.
- `evals/scripts/format_benchmark.py` turns one `--json` result into the page, and marks a run partial when a cost ceiling cut it short.

## 2.2.0 · 2026-11-01

- Adds a gallery: four new worked examples under `examples/`, each one a real chain of skills run in an empty directory with every file it produced, unedited. A UK physiotherapy SaaS, an office coffee subscription in Baku, a solo developer's cozy puzzle game, and one idea the skills told us to kill.
- Each example lists its cost, turns and time per skill, what to look at, and what could not be verified. All 90 cited links were requested on the day: 72 returned 200, 13 were bot blocks, one was dead and one timed out, and the gallery says which.
- The physiotherapy example is the readable proof of the `founder/` folder: the pricing skill states that it reused the competitor prices the earlier skill saved, rather than searching again.
- `evals/README.md` gained a section on running the suite without burning plan usage, with the measured split between models.

## 2.1.7 · 2026-10-17

- Adds the Skills Directory security badge to the README. Their scanner graded the skills A, 100 of 100, and the badge re-reads that grade on every scan rather than freezing today's result.

## 2.1.5 · 2026-10-17

- Adds a plugin icon, a 1024px square built from the same terminal mark and brand gradient as the README banner. The Claude plugin directory reads the icon once, at first submission, so it has to exist before the plugin is submitted. The vector source sits beside the banner in the assets folder.

## 2.1.4 · 2026-10-07

- Records a change that was tried and not shipped: inlining the nine core rules into all 13 skills, so a small model would not have to open `shared/conventions.md`. Haiku 4.5 scored 0.00 on `reads-the-shared-rules` either way, writing no `founder/` file and using em dashes in every run with the rules in its context, and Opus 5 held at 1.00. Fewer turns were seen afterwards, but a conventions change landed in the same window, so that cannot be credited to inlining. `evals/README.md` says where to look next instead.
- The `no-invented-proof-numbers` rubric now says it judges numbers, not qualitative claims like "setup takes minutes", after a judge failed a correct run on one. Three re-runs pass.

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
