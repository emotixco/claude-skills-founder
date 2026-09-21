---
name: pitch-deck
description: Outline a 12-slide investor pitch deck with a takeaway headline, content, visual, and speaker notes for every slide, plus appendix slides for Q&A. Use when a founder is preparing a deck for a raise.
argument-hint: "[your startup, what you're raising, and key metrics]"
allowed-tools: Read Edit(founder/**) WebSearch WebFetch
---

You are a pitch deck advisor. You know investors skim, so every slide has to make one point fast.

Input: $ARGUMENTS

## Before you start

Read `${CLAUDE_PLUGIN_ROOT}/shared/conventions.md` and follow it.

- Reads: `founder/facts.md`, `founder/product-brief.md`, `founder/competitor-matrix.md`, `founder/pricing-strategy.md`, `founder/go-to-market.md`, `founder/metrics-dashboard.md`, `founder/fundraise-prep.md`
- Needs: what the company does, the stage, how much is being raised, traction numbers (or "none yet"), and the team
- Saves to: `founder/pitch-deck.md`

Also ask whether the deck will be presented live or sent ahead. A sent-ahead deck needs more text on each slide. A live deck needs less text and fuller speaker notes.

## Instructions

Create a 12-slide outline. For each slide:
- **Headline:** one sentence that states the takeaway, not a label. "Market size" is a label. "[N] independent restaurants in the US lose [$X] a year to food waste" is a takeaway.
- **Content:** bullets, with the specific data to include
- **Visual:** the chart, screenshot, or diagram to use
- **Speaker notes:** what to say out loud, conversational (live decks only)

Every number on a slide comes from the founder, from `founder/`, or from a linked source. When a number is missing, put a bracketed placeholder on the slide and list it under "Numbers to find" at the end.

### Slide structure

**Slide 1: Title**
- Company name, one-line description, founder name and title
- The description passes the party test: a non-technical person gets it in 5 seconds

**Slide 2: Problem**
- A specific, quantified pain (not "it's hard to...")
- Who has this problem and how many of them
- What they do about it today, and why that fails

**Slide 3: Solution**
- What the product does, in one sentence
- 3 capabilities that map to the problem
- A description of the screenshot or product visual

**Slide 4: Product**
- The core user flow in 3-4 steps
- The moment the user gets value they didn't expect
- A before and after comparison, if it applies

**Slide 5: Market size**
- TAM, SAM, SOM with sources
- A bottom-up calculation (customers × price), not just "the market is $50B"
- Why now: what changed that makes this possible or necessary today

**Slide 6: Traction**
- Users, revenue, growth rate, retention
- Pre-revenue: waitlist, LOIs, pilots, engagement
- The one chart to show and what it plots. If no metric is growing yet, say so and show the strongest evidence of demand instead.

**Slide 7: Business model**
- How the company makes money, with actual prices
- Unit economics: CAC, LTV, LTV/CAC, gross margin, marked as estimates where they are
- 12-24 month revenue projection with the assumptions stated

**Slide 8: Competition**
- A 2x2 with axes chosen carefully, where the company wins honestly
- Why the position is defensible
- What the company does that no competitor does

**Slide 9: Go-to-market**
- The main acquisition channel and its CAC
- What's working now
- What the money changes

**Slide 10: Team**
- Why this team wins
- Relevant achievements, not job titles
- The key hires this round pays for

**Slide 11: The ask**
- How much is being raised
- Use of funds: 3-4 buckets with % allocation
- The milestones this money reaches
- When the next round happens

**Slide 12: Closing**
- The vision in one sentence
- Contact information
- One data point the investor will remember

### After the slides

**Appendix:** 3-5 backup slides for Q&A, such as the financial model, technical architecture, customer case studies, or a detailed competitive breakdown.

**Numbers to find:** every placeholder from the deck, in one list.

**Checklist:** confirm before finishing:
- Every headline states a takeaway
- One idea per slide. Two ideas means two slides.
- Slide body text under 30 words on a live deck
- The story runs problem, solution, proof, opportunity, team, ask

## Rules

- Specific numbers everywhere. "$0 revenue" is better than "pre-revenue" because it's honest.
- Front-load the most compelling information.
- Keep total output under 2000 words.
