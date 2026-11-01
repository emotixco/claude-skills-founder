<!-- /founder:competitor-matrix · 2026-11-01 · input: A scheduling app for independent physiotherapy clinics in the UK with 1 to 3 therapists. It fills cancelled slots by texting patients on a waitlist. -->

# Competitor matrix: waitlist-fill scheduling for small UK physio clinics

Assumption: the product is still the idea in the input. Nothing has been built and there are no customers yet. `founder/validate-idea.md` recommended building an add-on for existing systems rather than a full scheduling app. This matrix covers both, and section 5 explains why the add-on is the better bet.

All pages were checked on 2026-11-01.

## 1. Market landscape

**1. Jane** ([jane.app](https://jane.app))
- Founded and funding: founded in 2014. Mostly self-funded, with under $10M raised externally. JMI Equity bought more than $100M in shares in a 2021 secondary round. A $500M secondary round led by TCV at a $1.8B valuation was reported in May 2025, and ARR passed $100M in October 2024 ([BetaKit](https://betakit.com/jane-software-to-be-reportedly-valued-at-1-8-billion-in-upcoming-secondary-financing/)).
- Pricing: per month, in Canadian dollars. Balance is CA$59, Practice is CA$79 and Thrive is CA$99, each for one practitioner. Extra practitioner prices aren't listed ([pricing](https://jane.app/pricing)). The UK site redirects to this page, and I found no GBP prices.
- Segment: SMB, 1 to 50+ practitioners.
- Differentiator: an all-in-one practice system. Automatic wait list notifications come only with the top Thrive plan ([guide](https://jane.app/guide/using-automatic-wait-list-notifications)).

**2. Cliniko** ([cliniko.com](https://www.cliniko.com))
- Founded and funding: founded in Melbourne in 2011, according to [Cliniko's own story](https://www.cliniko.com/story/). It was funded with a home renovation loan and is described as bootstrapped by [GetLatka](https://getlatka.com/companies/cliniko.com).
- Pricing: per month, in US dollars. $45 for 1 practitioner and $95 for 2 to 5. SMS costs 10¢ a message ([pricing](https://www.cliniko.com/pricing/)).
- Segment: SMB.
- Differentiator: simple practice management at one flat price. Its wait list is manual: staff pick a patient from the list when they book ([help](https://help.cliniko.com/en/articles/1402450-using-the-wait-list)).

**3. WriteUpp** ([writeupp.com](https://www.writeupp.com))
- Founded and funding: founded in the UK, in 2013 according to a third-party profile ([FitGap](https://us.fitgap.com/products/writeupp)). Its CEO is based in Toronto ([about](https://www.writeupp.com/about-us)). Funding: Not found.
- Pricing: Flex from £19.95 per user, Solo from £27.95 and Group from £45.95. Solo includes 100 SMS a month, and Group includes 100 SMS per clinician ([pricing](https://www.writeupp.com/pricing)).
- Segment: SMB and solo practitioners in the UK and Ireland.
- Differentiator: built for UK and Ireland clinics. It keeps a waiting list ([help](https://help.writeupp.com/en/article/can-i-keep-a-waiting-list-in-writeupp-akittd/)), but I found no sign that it sends offers automatically.

**4. Pabau** ([pabau.com](https://pabau.com))
- Founded and funding: based in London. Its own [about page](https://pabau.com/about/) says it has never taken external funding. The founding year is 2009 or 2012, depending on the source.
- Pricing: not public. Pricing depends on location and user count. There is a "Team" plan for 2 to 3 users ([pricing](https://pabau.com/pricing/)).
- Segment: SMB, mostly aesthetics and medical clinics.
- Differentiator: an all-in-one clinic CRM. When a slot opens, it flags matching waitlist clients, and staff send an SMS or email with a booking link ([waitlist](https://pabau.com/features/waitlist/)).

**5. Zanda, formerly Power Diary** ([zandahealth.com](https://zandahealth.com/uk/pricing/))
- Founded and funding: Not found.
- Pricing: Starter is £15 a month for 1 practitioner. Growth is £25 a month plus £15 for each extra practitioner. SMS costs £0.09 per message and replies are free ([UK pricing](https://zandahealth.com/uk/pricing/)).
- Segment: SMB.
- Differentiator: low base price. Staff can bulk-text the waitlist from a filtered list ([comparison](https://zandahealth.com/uk/comparisons/eclinic-alternative/)).

**6. Penciled** ([penciled.com](https://www.penciled.com))
- Founded and funding: YC W24. Sources disagree on funding. "Over $2.6M" from YC, Initialized Capital and angels is the most-cited figure ([YC](https://www.ycombinator.com/companies/penciled)). CB Insights lists $500K ([CB Insights](https://www.cbinsights.com/company/somn)).
- Pricing: a flat annual price per therapist seat, plus a one-time $1,200 onboarding fee per location. Tier prices: Not found ([site](https://www.penciled.com/)).
- Segment: SMB to mid-market US physical therapy clinics on WebPT.
- Differentiator: an AI front-office agent. It texts and calls eligible waitlist patients in parallel and books the first reply straight into WebPT.

**7. WaitOnce** ([waitonce.com.au](https://www.waitonce.com.au/))
- Founded and funding: built in Australia by an allied health professional. It received a 2024 Innovation Connect grant and has a 2025 provisional patent ([site](https://www.waitonce.com.au/)). Equity funding: Not found.
- Pricing: Not found. There is a 30-day free trial ([Cliniko listing](https://www.cliniko.com/connected-apps/waitonce)).
- Segment: small allied health practices.
- Differentiator: a waitlist add-on for Cliniko, Halaxy, Nookal and Splose that "sends automated offers when cancellations occur".

## 2. Feature comparison matrix

| Feature | Jane | Cliniko | WriteUpp | Pabau | Zanda | Penciled | WaitOnce | Your product |
|---|---|---|---|---|---|---|---|---|
| Full diary, notes and invoicing | Yes | Yes | Yes | Yes | Yes | No | No | Planned (input) |
| Waitlist record | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Planned |
| Offer sent automatically on cancellation | Yes (Thrive only) | No | Unknown | Partial (flags match, staff send) | Partial (staff send) | Yes | Yes | Planned |
| Offer by SMS | Unknown | No | Unknown | Yes | Yes | Yes | Unknown | Planned |
| Patient books from the message without staff | Yes (link) | No | Unknown | Yes (link) | Unknown | Yes | Yes (portal) | Planned |
| Book by replying "YES" (no link or login) | Unknown | No | Unknown | No | Unknown | Yes | Unknown | Planned |
| Contacts patients in parallel, first reply wins | Partial (exclusive window) | No | Unknown | Unknown | Unknown | Yes | Unknown | Planned |
| Works on top of the clinic's existing system | No | No | No | No | No | Yes (WebPT only) | Yes (Cliniko and 3 others) | Planned |
| Public GBP pricing | No | No | Yes | No | Yes | No | No | Planned |
| Reports revenue recovered from filled slots | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Unknown | Planned |
| AI voice calls to the waitlist | No | No | No | No | No | Yes | No | No |

## 3. Positioning gaps

**Gap 1: hands-off SMS fill for UK clinics on Cliniko or WriteUpp**
- What's missing: Penciled does the full workflow, but only for WebPT in the US. WaitOnce sends automatic offers in Cliniko, but it is Australian, has no public pricing, and doesn't say whether it uses SMS. Cliniko and WriteUpp leave UK users with a manual list.
- Why it matters: in a 1 to 3 therapist clinic the physio is also the receptionist. A slot cancelled at 8am is lost if nobody texts the list until lunch.
- Difficulty: medium. You need cancellation webhooks or polling, safe write-back, and double-booking protection.
- Head start: Estimate: 3 to 9 months. WaitOnce already has the Cliniko integration, and Cliniko's API is the same worldwide, so its barrier to entering the UK is marketing and GBP billing rather than code. Cliniko has run a manual wait list for years, so a native version is possible but not signalled.

**Gap 2: reply "YES" to book, with no link, app or login**
- What's missing: Jane and Pabau send a booking link, and WaitOnce uses a portal. Only Penciled confirms bookings directly over SMS, and only in the US.
- Why it matters: physio patients skew older. Every extra tap loses some replies, and when the slot is in 2 hours, speed decides whether it gets filled.
- Difficulty: low. Twilio inbound SMS plus a first-reply lock.
- Head start: Estimate: 1 to 3 months. It is easy to copy once someone sees it.

**Gap 3: proof of money recovered**
- What's missing: I found no competitor page showing a monthly "£ recovered" report for filled cancellations.
- Why it matters: owners will pay £30 a month if they can see it returned £300. This turns the product from a cost into a visible return.
- Difficulty: low.
- Head start: about zero on its own. It mainly helps sales and retention when combined with Gaps 1 and 2.

## 4. Threat assessment

| Rank | Competitor | Threat | Resources | Feature overlap | Iteration speed |
|---|---|---|---|---|---|
| 1 | WaitOnce | High | Small: grant-funded, equity Not found | Highest: automatic Cliniko waitlist offers, the same buyer | Active: patent filed in 2025, Pitch Fest 2026 win, 4 integrations ([site](https://www.waitonce.com.au/)). No public changelog found |
| 2 | Jane | Medium | Very large: $100M+ ARR | High, but only for clinics already on Jane Thrive | Ships steadily, but I found no dated changelog. Clinics must migrate their whole practice to get the feature |
| 3 | Penciled | Medium | About $2.6M, YC-backed | Highest on features: parallel SMS, first reply wins, AI calls | Fast, as is typical for YC, but US and WebPT only. The UK needs new integrations, GBP billing and UK GDPR work |

## 5. Strategic recommendations

- **Position to own:** UK physio clinics with 1 to 3 therapists that already use Cliniko. Sell an add-on that installs in 10 minutes, not a scheduling app. Five of the seven competitors already sell a full diary, so a new one would have to win a migration battle against Jane (CA$59 to CA$99 a month) and Zanda (from £15). An add-on only has to beat a manual list. Expand to WriteUpp next, since it is the main UK-built system, and then to osteopaths and chiropractors.
- **Feature to ship first:** cancellation in Cliniko, then an SMS to matching waitlist patients in parallel. The first "YES" gets booked straight back into Cliniko, and everyone else gets a "slot taken" text. This covers Gaps 1 and 2 at once, and in the UK only Penciled's US-only product does the same.
- **Competitor to watch:** WaitOnce. It already has the exact Cliniko workflow and allied health credibility. Entering the UK costs it little more than a GBP price and some marketing. Check its site and Cliniko's connected apps page each month for UK pricing, SMS support or UK testimonials.
