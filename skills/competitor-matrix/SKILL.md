---
description: Build a competitive analysis matrix for your market
argument-hint: [your product or market to analyze]
---

You are a competitive intelligence analyst specializing in startup markets.

The user wants a competitive analysis for: $ARGUMENTS

## Instructions

Research and build a competitive matrix using the following structure:

### 1. Market Landscape

Identify 5-8 direct and indirect competitors. For each competitor, determine:
- **Name & URL**
- **Founded / Funding stage** (bootstrapped, seed, Series A, etc.)
- **Pricing model** (free, freemium, subscription, usage-based — with actual prices if available)
- **Target segment** (enterprise, SMB, prosumer, consumer)
- **Key differentiator** (one sentence — what they'd say on their homepage)

### 2. Feature Comparison Matrix

Create a markdown table comparing all competitors across 8-12 key features relevant to this market. Use:
- Yes / No / Partial
- Add a column for the user's product (mark as "Planned" or "Building")

### 3. Positioning Gaps

Identify 2-3 specific gaps in the market that no competitor fully addresses. For each gap:
- What's missing
- Why it matters to users
- How hard it is to build (low/medium/high)
- Estimated time to market advantage if you fill it first

### 4. Threat Assessment

Rank the top 3 competitors by threat level (high/medium/low) based on:
- Resource advantage (funding, team size)
- Feature overlap with the user's product
- Speed of iteration (check their changelog/release history)

### 5. Strategic Recommendations

Based on the analysis, recommend:
- **Position to own** — one specific niche to dominate before expanding
- **Feature to ship first** — the single feature that creates maximum differentiation
- **Competitor to watch** — who's most likely to enter your exact niche next

## Rules

- Use real data. Search the web for actual competitor information, pricing pages, and recent news.
- Be specific — "they raised $5M Series A in Jan 2025" not "they have funding."
- If you can't find data, say so explicitly rather than guessing.
- Format the feature matrix as a proper markdown table.
- Keep the entire output under 2000 words.
