<!-- /founder:mvp-scope · 2026-11-01 · input: A cozy mobile puzzle game with a playground meta layer, built by one developer, with no paid user acquisition budget. -->

# MVP scope: cozy mobile puzzle game with a playground meta layer

Assumption: you listed no features, so the list below is inferred from the genre and from `founder/validate-idea.md`.
Assumption: "playground meta layer" means a space the player fills with items earned from puzzles.
Assumption: art comes from a bought asset pack or your own hand. Build times exclude original art.
Note: `founder/validate-idea.md` recommended pivoting to premium PC and Switch. Your input says mobile, so this scope is for mobile. Everything below is built in Unity, so a PC build later costs days, not weeks.

## 1. Feature triage

| Feature | Category | Reasoning |
|---------|----------|-----------|
| Core puzzle mechanic with feel (animation, sound, haptics) | Must have | It is the game, and the only thing a 10-second clip can sell. |
| 30 handcrafted levels | Must have | Enough for about 1 hour of play, which is enough to measure day 1 return. |
| One playground with 15 items unlocked by stars | Must have | It is the hypothesis being tested. Without it, you are testing a different game. |
| Share playground as an image | Must have | With $0 budget, a player's post is the only distribution you get. |
| Local save | Must have | Losing progress on app close kills day 1 retention, the number you need. |
| Analytics and crash reports | Must have | Without them, the test produces opinions, not numbers. |
| Tutorial as the first 3 levels | Should have | Level design can teach the mechanic. Build a separate tutorial only if players get stuck. |
| More levels (to 100) | Should have | Only worth it once day 1 retention says people come back. |
| Daily reward | Should have | Cheap retention lever, but it inflates the numbers you are trying to read. |
| Rewarded ads | Should have | First revenue test, after retention is proven. |
| Free item placement (drag anywhere) | Should have | Fixed slots deliver 80% of the feeling for 20% of the work. |
| In-app purchases and store | Won't have | No one buys before they care. |
| Visit a friend's playground | Won't have | Needs accounts, a server, and moderation. |
| Accounts and cloud save | Won't have | No server means no hosting cost and no outages. |
| Multiple playground themes | Won't have | One playground answers the question. |
| Live events and seasons | Won't have | Live ops is a team job. |
| Push notifications | Won't have | A 30-level game has nothing to remind people about. |
| Leaderboards | Won't have | Competitive features fight the cozy promise. |
| Level editor tool | Won't have | Write levels as JSON by hand for 30 levels. |
| NPCs or story | Won't have | Content cost with no test value. |

## 2. MVP definition

**A player can solve a puzzle and see a new item appear in their playground in under 3 minutes.**

Features:
1. Core puzzle mechanic with feel
2. 30 levels loaded from JSON
3. One playground, 15 fixed item slots, unlocked by stars
4. Local save
5. Share playground image through the native share sheet
6. Analytics and crash reports

## 3. User flow

```
Step 1: Player opens the app from a TestFlight or Play test link. Level 1 loads with no menu.
Step 2: Player solves level 1 (about 45 seconds) and earns stars.
Step 3: Player taps "Go to playground" and places the first item in a glowing slot.
Step 4: Player taps "Share" and posts the playground image, or returns to level 2.
```

Each step is under 60 seconds. The first item lands inside 2 minutes.

## 4. Technical scope

**Build vs. buy**

| Need | Decision |
|------|----------|
| Engine | Buy (free): [Unity Personal, free under $200K revenue or funding](https://unity.com/pricing-updates). Godot also works, but Firebase support in Unity is official. |
| Analytics and crashes | Buy (free): Firebase Analytics and Crashlytics, both listed as no-cost on the [Firebase pricing page](https://firebase.google.com/pricing). |
| Sharing | Buy (free): native share sheet through a Unity plugin. |
| Art and sound | Buy: one cozy asset pack. Do not draw before the test. |
| Puzzle, levels, playground, save | Build. |
| Auth, payments, email | None. Not needed. |

**Stack:** Unity, C#, levels as JSON files, save as one local JSON file, Firebase. No backend.

**Build time (one developer)**

| Feature | Days |
|---------|------|
| Core mechanic with feel | 5 |
| Level loader and 30 levels | 4 |
| Playground with 15 slots | 3 |
| Local save | 0.5 |
| Share image | 1 |
| Analytics and crash reports | 1 |
| Store builds and test setup | 1.5 |
| **Total** | **16 working days (about 3 weeks)** |

**Hosting:** none. The game runs on the phone. Distribution is free inside your developer accounts:
- iOS: TestFlight allows [up to 10,000 external testers per app](https://developer.apple.com/help/app-store-connect/test-a-beta-version/invite-external-testers). The first external build needs Apple's beta review, so allow 1 to 2 days.
- Android: a new personal Play account must run a [closed test with at least 12 testers for 14 days](https://support.google.com/googleplay/android-developer/answer/14151465) before production. Start that clock in week 2, not after launch.

## 5. What you're not building, and why

| Feature | Why it feels important | Why it doesn't matter yet | Revisit when |
|---------|------------------------|---------------------------|--------------|
| Visiting friends' playgrounds | It is the growth loop the validation called for | A shared image tests the same urge for 1 day of work instead of 3 weeks | 20% of players who reach the playground tap Share |
| In-app purchases | Free-to-play needs revenue | No revenue model survives bad retention | Day 7 retention passes 10% across 500 players |
| 100+ levels | Puzzle players burn content fast | If players quit at level 8, level 80 is waste | 30% of players finish level 30 |
| Cloud save and accounts | Players lose progress on new phones | Testers keep their phone for the 2 weeks the test runs | Public launch on the stores |
| Live events | Every top puzzle game runs them | Events retain an audience you don't have yet | 1,000 daily players |

## 6. Launch criteria

**Must work:**
- [ ] Levels 1 to 30 are all solvable, checked by you on a phone
- [ ] Stars unlock items, and each of the 15 items can be placed
- [ ] Progress survives closing and reopening the app
- [ ] Share produces an image of the playground on iOS and Android
- [ ] Analytics logs `level_start`, `level_complete`, `item_placed`, `share_tapped`, and app opens by day
- [ ] No crash in 30 minutes of play on one older Android phone
- [ ] First item lands in under 3 minutes for a new player

**Can be broken or ugly:**
- Menus and settings screen (one mute button is enough)
- Placeholder sounds on non-core actions
- Tablet layout

**The one thing to test with the first 10 users:** after placing the first item, do they go back to the puzzle on their own? Watch without speaking. If they stop at the playground and close the app, the meta is not pulling. If they rush past it to the next level, the puzzle carries the game and the playground is decoration.
