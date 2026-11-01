<!-- /founder:validate-idea · 2026-11-01 · input: A scheduling app for independent physiotherapy clinics in the UK with 1 to 3 therapists. It fills cancelled slots by texting patients on a waitlist. -->

# Idea validation: waitlist-fill scheduling app for small UK physio clinics

Assumption: the founder has no physio background, no existing clinic relationships, and no code yet. Nothing in `founder/` says otherwise.

## 1. The 30-second assessment

The pain is real: a late cancellation in a 1 to 3 therapist clinic is lost income the owner feels directly. But "a scheduling app" is the wrong product. These clinics already run their diary, notes and invoicing in a practice management system (Cliniko, Jane, Pabau, WriteUpp), and nobody migrates their whole clinic for one feature. Waitlist texting is a feature, and two of those incumbents already ship it.

## 2. The five fatal questions

**Q1: Who is the customer, and would they pay today?**

The buyer is the owner-physio of a 1 to 3 therapist private clinic who treats patients all day and does admin at night. Estimate: at about £55 a session, refilling 2 extra slots a month is worth £110. They would pay £20 to £40 a month for an add-on that proves it fills slots. They would not pay to replace their practice management system, because that means moving patient notes, online booking and invoicing. So: yes for an add-on, no for a scheduling app.

**Q2: Why hasn't someone built this already?**

They have.
- [Jane](https://jane.app/guide/using-automatic-wait-list-notifications) sends automatic wait list notifications when a slot is cancelled, on its top Thrive plan ([Jane AU guide](https://janeapp.com.au/guide/setting-up-your-wait-list-notifications)), about $71 a month per [Toolradar](https://toolradar.com/tools/jane-app/pricing). Jane has a UK site ([janeapp.co.uk](https://janeapp.co.uk/guide/using-the-wait-list)).
- [Pabau](https://pabau.com/features/waitlist/) matches waitlisted clients to open slots and lets staff text or email them.
- [Penciled](https://www.ycombinator.com/companies/penciled/jobs) (YC) uses an AI agent to text and call waitlist patients for physical therapy clinics, mainly in the US.
- [Cliniko](https://help.cliniko.com/en/articles/1402450-using-the-wait-list) has a wait list, but I found no evidence it sends automatic offers. That is the gap.

What's different now: very little. SMS is cheap and old. The only new angle is the gap in Cliniko and similar tools that keep a manual list.

**Q3: What's the distribution advantage?**

None built in. Patients receive texts, but they don't buy clinic software, so there is no loop. Reachable channels:
- [Physio First](https://www.physiofirst.org.uk/about.html), the association for self-employed physios, with about 2,000 to 3,000 members ([CSP guide](https://acptr.csp.org.uk/system/files/publication_files/The%20essential%20guide.pdf)).
- Practice management integration directories, if you build as an add-on.
- UK physio business Facebook groups and direct outreach to clinics on Google Maps.

The first 100 will come from manual outreach. That's fine for 100. It doesn't scale cheaply.

**Q4: Can this be a big business, or is it a feature?**

It is a feature. Jane and Pabau prove the incumbents will build it, and Cliniko can add it whenever it chooses.

Ceiling, UK physio only. Estimate: about 4,500 physios work in private practice ([Insights10](https://www.insights10.com/blogs/uk-physiotherapy-market-analysis), source unverified). At about 1.8 physios per small clinic, that's about 2,500 target clinics. 2,500 × £30 × 12 = £900k ARR at 100% market share. Realistic share of 10% gives £90k ARR.

To reach $1M ARR you need about 2,800 clinics at £30 a month. That requires leaving "UK physio, 1 to 3 therapists" behind: all allied health (osteo, chiro, podiatry, sports massage) across the UK, Australia and New Zealand, sold as an add-on to the systems they already use.

**Q5: Can the founder actually build this?**

The technical work is modest: read cancellations from a practice management API, text matching waitlist patients in order, take the first "YES", and book it back. The hard parts are operational:
- Race conditions and double bookings when two patients reply at once, or the receptionist books the slot by hand.
- UK GDPR: you process health data (appointment type, physio name), so you need a DPA, ICO registration and consent wording for texts.
- Integration permission: if Cliniko's API or terms limit write access, the product breaks.

No first hire is needed. It helps a lot to have a physio co-founder or adviser for credibility with owners.

## 3. Idea scorecard

| Dimension | Score | Notes |
|-----------|-------|-------|
| Problem severity | 3 | Late cancellations cost real money, but busy clinics often refill by phone already |
| Market size | 2 | About 2,500 UK clinics (estimate). Ceiling under £1M ARR |
| Willingness to pay | 2 | £20 to £40 a month as an add-on. Near zero as a system replacement |
| Competition gap | 2 | Jane and Pabau ship it. The gap is only in tools like Cliniko |
| Distribution | 3 | Physio First and integration directories are reachable. No growth loop |
| Timing | 2 | Nothing changed recently that makes this newly possible |
| Founder fit | ? | Unknown. Do you have a physio network, clinic experience, or integration skills? |
| **Total** | **14/30 + ?** | |

Even a 5 on founder fit gives 19/35: significant concerns. The idea needs a different angle.

## 4. Validation experiments

**Experiment 1: Is the pain big enough?**
- Test: small clinics lose at least 4 unfilled late cancellations per therapist per month.
- How: message 30 UK clinic owners (Physio First directory, Google Maps). Ask 10 of them to export the last 90 days of cancellations from their system and tell you which slots were refilled. Count unfilled cancellations made under 24 hours ahead.
- Success: median at least 4 unfilled late cancellations per therapist per month across 10 clinics. Under 2 means kill.
- Time and cost: 1 week, £0.

**Experiment 2: Does texting a waitlist actually fill slots?**
- Test: a texted waitlist fills at least 40% of offered slots.
- How: run it by hand (concierge) for 3 clinics for 2 weeks. The clinic messages you each cancellation. You text their waitlist from a Twilio number or a dedicated phone, and the clinic books whoever says yes first.
- Success: at least 40% of offered slots filled, and 2 of 3 clinics agree to pay £30 a month to keep it.
- Time and cost: 2 weeks, about £50 for SMS and a number.

**Experiment 3: Which system do they use, and will they pre-pay?**
- Test: enough clinics run a system without automatic waitlist offers, and they'll pay.
- How: one-page site, "Auto-fill cancellations in Cliniko. £29 a month." Add a form that asks for their practice management system, and a £29 pre-order through Stripe. Post it in 3 UK physio business Facebook groups and the Physio First member forum.
- Success: 20 sign-ups that name their system, with at least 60% on a system without automatic waitlist offers, and 5 paid pre-orders.
- Time and cost: 10 days, under £100.

## 5. The honest verdict

**Pivot it.** Don't build a scheduling app. Build a waitlist auto-filler that plugs into the systems clinics already use, starting with Cliniko, whose wait list appears to be manual. Then widen the market to every small allied health clinic in the UK, Australia and New Zealand. That turns a feature nobody will migrate for into an add-on that installs in 10 minutes and pays for itself with one filled slot.

The most important thing this week: check that the [Cliniko API](https://docs.api.cliniko.com/) can read cancellations, read the wait list and create appointments, and that its terms allow it. Then start Experiment 1 with 10 clinic owners. If either fails, stop.

Also tell me about yourself: do you have physio or clinic experience, or a network in UK private practice? That decides the founder fit score.
