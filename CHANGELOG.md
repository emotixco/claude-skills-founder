# Changelog

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
