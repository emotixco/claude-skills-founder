<!-- /founder:metrics-dashboard · 2026-11-01 · input: A cozy mobile puzzle game with a playground meta layer, built by one developer, with no paid user acquisition budget. -->

# Metrics dashboard: cozy mobile puzzle game with a playground meta layer

Assumption: you are building the MVP in `founder/mvp-scope.md` (about 3 weeks), then running a TestFlight and Play closed test. No live numbers exist yet.
Assumption: no revenue for 90 days. In-app purchases are out of scope until D7 passes 10% across 500 players.
Assumption: no raise is planned. Section 6 is written for a publisher pitch, which is the more likely money for a solo game.

## 1. Stage

**Pre-launch, moving into post-launch (0 to 100 players) within about 30 days.** The one question to answer: does the playground pull players back into the puzzle, and can free channels bring players at all? Every metric below serves one of those two. Revenue, LTV, and CAC are meaningless until then.

With 50 players, one person moves a rate by 2 points. Read 2-week trends.

## 2. The five metrics

**1. Organic new players per week**
- Definition: count of `first_open` events in the week, from testers who came through your posts, clips, or communities.
- Current: 0. Firebase console, Analytics, `first_open` count.
- Targets: 30 days: 25 per week. 60 days: 50. 90 days: 100.
- Why: with $0 budget, this is your entire growth engine. It decides whether mobile is viable or whether to take the PC and Steam route from `founder/validate-idea.md`.
- If below target: post 1 ten-second puzzle clip per day for 14 days on TikTok and Shorts, each ending with the test link. If still under 25 per week by day 60, put up the $100 Steam page and compare.

**2. Activation rate**
- Definition: % of new players who fire `first_item_placed` in their first session.
- Current: not measured. `first_item_placed` users ÷ `first_open` users, same cohort.
- Targets: 30 days: 70%. 60 days: 80%. 90 days: 85%.
- Why: the MVP promise is "first item in under 3 minutes." Players who never see the playground never test it.
- If below target: check which level has the highest `level_fail` or `level_quit` count before the first unlock. Make that level easier or lower the star cost of item 1.

**3. D1 retention**
- Definition: % of players who open the game again on the calendar day after `first_open`.
- Current: not measured. Firebase console, Analytics, Retention.
- Targets: 30 days: 25% (first closed test cohort). 60 days: 30%. 90 days: 35%.
- Why: it is the first signal the game is worth more content. 22% is the median and 40% is the top 10% for mobile games ([GameAnalytics 2025 benchmarks](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks)). Puzzle sits above the median in that report.
- If below target: interview 5 players who did not return, by message, with one question: "What were you doing the moment you closed it?" Fix the top answer before adding levels. Once 500 players exist, track D7 here instead, target 10%.

**4. Return-to-puzzle rate**
- Definition: % of players who start another level (`level_start`) within 5 minutes after placing their first item, in the same session.
- Current: not measured. Build as a funnel in Firebase: `first_item_placed` then `level_start`.
- Targets: 30 days: 50%. 60 days: 60%. 90 days: 70%.
- Why: this is the playground hypothesis in one number. Low means the meta is a dead end, not a pull.
- If below target: show the next locked item and its star cost on the playground screen with a "Play to unlock" button. If it stays under 50% after that change, test cutting the playground down to a reward screen.

**5. Share rate**
- Definition: % of players who open the playground and fire `share_completed` at least once.
- Current: not measured. `share_completed` users ÷ `playground_open` users.
- Targets: 30 days: 5%. 60 days: 10%. 90 days: 20%.
- Why: 20% is the trigger in `founder/mvp-scope.md` for building friend visits. It is your only built-in loop.
- If below target: prompt Share once, right after the 5th item is placed, with the image prefilled. Add the game name and test link to the image itself.

## 3. Metrics to ignore

| Metric | Why it feels important | Why it misleads | Track instead |
|--------|------------------------|-----------------|---------------|
| Total downloads or TestFlight invites | Big, always goes up | Says nothing about whether anyone plays twice | D1 retention |
| Clip views and follower counts | Fast feedback, dopamine | 100,000 views with 3 installs is a failed channel | Organic new players per week |
| Waitlist or Discord size | Feels like an audience | Signups who never open the build are not players | `first_open` from that source |
| Average session length | Long sessions sound like love | One stuck player on level 7 for 20 minutes raises it | `level_fail` per level, activation rate |

## 4. Tracking setup

| Need | Tool | Cost | Setup time |
|------|------|------|------------|
| Product analytics and crashes | Firebase Analytics and Crashlytics | Free. Both listed as no-cost products on the [Firebase pricing page](https://firebase.google.com/pricing), usable in production on the Spark plan ([plans doc](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans)) | 1 day (already in MVP scope) |
| Revenue tracking | None yet. App Store Connect and Play Console reports when ads or IAP arrive | Included with developer accounts | 0 |
| User feedback | Tally form linked from a "Feedback" button and from the tester invite | Free plan with no submission limit, fair use ([Tally pricing](https://tally.so/pricing)). Pro is $29/month ([source](https://www.jetadmin.io/blog/tally-pricing/amp/)) | 30 minutes |
| Dashboard | One Google Sheet, filled by hand each Monday from Firebase | Free | 30 minutes |

Add one question to the Tally signup: "Where did you find this game?" It is the only acquisition attribution you need at this size.

**Events to track**

| Event | Fires when | Tells you |
|-------|-----------|-----------|
| `first_open` | Automatic, first launch | New players (metric 1) |
| `session_start` | Automatic | D1 and D7 return |
| `level_start` (level_id) | Level loads | Progress depth, metric 4 |
| `level_complete` (level_id, stars, seconds, moves) | Level solved | Difficulty curve |
| `level_fail` (level_id) | Out of moves or time | Where players hit a wall |
| `level_quit` (level_id) | Player leaves mid-level | Frustration points |
| `stars_earned` (total) | Stars added | Economy pacing |
| `playground_open` | Playground screen shown | Meta reach |
| `first_item_placed` (seconds_since_install) | First item ever placed | Activation (metric 2) and the 3-minute promise |
| `item_placed` (item_id) | Any item placed | Which items motivate |
| `item_locked_tap` (item_id) | Player taps a locked item | Desire for the next reward |
| `share_tapped` | Share button pressed | Share intent |
| `share_completed` | Share sheet returns success | Metric 5 |
| `feedback_opened` | Feedback button pressed | Who bothers to talk to you |
| `level_30_complete` | Final level solved | Content runway (30% triggers building more levels) |

## 5. Weekly review template

Every Monday, 15 minutes: 10 to pull numbers into the sheet, 5 to write.

```
Week of: ___
Organic new players: ___ (last week: ___, target: 25 / 50 / 100)
Activation rate: ___% (target: 70% / 80% / 85%)
D1 retention: ___% (target: 25% / 30% / 35%)
Return-to-puzzle rate: ___% (target: 50% / 60% / 70%)
Share rate: ___% (target: 5% / 10% / 20%)
Crash-free users (Crashlytics): ___%
Hardest level this week (most level_fail): ___

Top source from Tally: ___
What worked: ___
What didn't: ___
One thing to try this week: ___
```

## 6. Investor and publisher metrics

If you pitch a publisher, Apple Arcade, or an investor in the next 6 months, they will ask for:

| Metric | What good looks like | Source |
|--------|---------------------|--------|
| D1 retention | 22% is median, 40% is top 10% | [GameAnalytics 2025](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks) |
| D7 retention | 4% is median, 12% is top 10% | [GameAnalytics 2025](https://gamedevreports.substack.com/p/gameanalytics-mobile-gaming-benchmarks) |
| Organic installs per week and trend | Not found as a benchmark. Show week over week growth | |
| Cost per install you avoided | Puzzle CPI is $3 to $5 | [Game Growth Advisor 2026](https://gamegrowthadvisor.com/blog/2026-03-17-user-acquisition-cpi-benchmarks-2026/) |

**How to show numbers that aren't good yet:**
- Always give the sample size: "D1 31%, n = 48 testers." Publishers distrust rates with no n.
- Show the trend across builds, not one snapshot: "D1 went from 19% to 31% across 3 builds after we fixed level 4." Iteration speed is what they are buying from a solo developer.
- Say what the number decided: "Return-to-puzzle was 38%, so we added the next-item preview, and it rose to 55%."
- Label friends and family and exclude them.

---

Saved to `founder/metrics-dashboard.md`. Next: `/founder:go-to-market` to plan where the organic players in metric 1 come from, and `/founder:pitch-deck` once you have 4 weeks of numbers.
