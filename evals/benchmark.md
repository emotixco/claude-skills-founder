# Benchmark

What the plugin scores against plain Claude, re-measured on a schedule rather than quoted once. A case's score is the share of its graders that passed, averaged over its runs. Delta is the with-plugin score minus the same cases run with no plugin loaded, so a delta of zero means Claude did as well without us.

Losses stay on this page. See [README](./README.md) for what each case checks and how the suite is run.

## Latest run

No scheduled run has been published yet. The workflow is armed by adding an `ANTHROPIC_API_KEY` secret to the repository, and it can also be started by hand from the Actions tab.

Until then, the most recent manual numbers are in [README](./README.md): on 2026-10-07 the suite scored the same with and without the plugin on Opus 5 for 8 of 10 cases, and on Haiku 4.5 the plugin raised 3 of 10.

## History

<!-- history:start -->
| Date | Run | Agent model | Suite score | Mean delta | Cases at threshold | Cost |
|---|---|---|---|---|---|---|
<!-- history:end -->
