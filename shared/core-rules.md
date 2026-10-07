Rules for every run, inlined into each skill by `shared/sync-core-rules.py`. The long form, with the reasoning, is in `${CLAUDE_PLUGIN_ROOT}/shared/conventions.md`.

1. Read the files on the Reads line before you ask the founder anything, and say what you found there. Asking for something already saved in `founder/` is the mistake that folder exists to prevent.
2. If the input is empty and nothing in `founder/` answers the Needs line, ask for those items in one message and stop. If only some are missing, go ahead and list each guess as "Assumption:".
3. If the input contradicts a saved file, the input wins. Say which saved fact it replaces.
4. Save your output to the file on the Saves to line, replacing any earlier version. Its first line is a comment: `<!-- /founder:<skill-name> · YYYY-MM-DD · input: <the founder's input on one line> -->`.
5. Append facts the founder stated in this run to `founder/facts.md`, one per line with the date and this skill's name. Only what the founder gave you, never your estimates.
6. Competitor names, prices, funding, market sizes and benchmarks need a source link next to the claim. No source means writing "Estimate:" with the arithmetic shown, or "Not found". Never present a guess as a fact.
7. Never invent the founder's metrics, customers, quotes, testimonials, logos or team. Write a bracketed placeholder saying what goes there, such as `[Quote from a beta user about hours saved per week]`.
8. Plain words, and a number beats an adjective. Sentence case headings. No em dashes or en dashes: use a period, a comma or a colon. Do not end with a summary of what you already said. Stay under the skill's word limit.
9. End your reply with the path you saved to and, at most, two other skills that would use this output next.
