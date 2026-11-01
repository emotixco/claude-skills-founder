<!-- /founder:pricing-strategy · 2026-11-01 · input: A scheduling app for independent physiotherapy clinics in the UK with 1 to 3 therapists. It fills cancelled slots by texting patients on a waitlist. -->

# Pricing strategy: waitlist auto-fill for small UK physio clinics

Assumption: the founder has not stated a price. Nothing in `founder/facts.md` gives one.
Assumption: this prices the Cliniko add-on recommended in `founder/validate-idea.md`, not a full scheduling app. A full app would be priced against Zanda (£15 a month) and Cliniko ($45 a month), which already have the diary, notes and invoicing. You lose that fight on price.
Assumption: a typical therapist has 8 late cancellations a month, and each one triggers 10 outbound texts (5 offers, 1 confirmation, 4 "slot taken"). Estimate, to be replaced by Experiment 1 data.

## 1. Pricing model analysis

| Model | Fit score | Pros | Cons |
|-------|-----------|------|------|
| Flat subscription | 5 | Owners budget monthly. Easy to compare with "one filled slot" | SMS cost grows with clinic size, so it needs bands |
| Usage-based (per filled slot) | 3 | Pays only when it works | Bills swing with cancellations. Owners dislike paying more in a bad month |
| Per-seat | 3 | Therapist count tracks cancellation volume | Receptionist logins shouldn't cost money. A 1 to 3 seat market gives little expansion |
| Freemium | 1 | Low friction | Every free clinic costs SMS money, in a market of about 2,500 clinics |
| Credits | 2 | Covers SMS cost exactly | Owners have to manage top-ups. Running out mid-cancellation means a lost slot |
| One-time purchase | 1 | Simple | SMS and hosting cost every month |

**Recommendation: flat monthly subscription, banded by therapist count, SMS included up to a cap.** Because the buyer thinks "is this cheaper than one filled appointment?", and a fixed number answers that. Bands keep SMS cost in line with revenue.

## 2. Tier design

Prices exclude VAT. All plans: 30-day free trial, 50 SMS, no card needed.

### Solo: £24 a month, or £240 a year (17% off)
- 1 therapist
- 150 SMS a month, then 6p per SMS
- Cliniko sync: cancellations in, bookings back
- Parallel offers, first "YES" reply books the slot
- Up to 100 waitlist patients
- Monthly email: slots filled and £ recovered
- **Upgrade trigger:** a second therapist joins, or the clinic hits the SMS cap 2 months in a row.

### Clinic: £49 a month, or £490 a year (17% off). Target tier
- Up to 3 therapists
- 400 SMS a month, then 5p per SMS
- Everything in Solo
- Unlimited waitlist patients
- Matching rules: preferred therapist, time of day, appointment type
- Weekly £ recovered report per therapist
- 2 staff logins
- **Upgrade trigger:** a fourth therapist or a second site.

### Group: £99 a month, or £990 a year (17% off)
- Up to 8 therapists, 2 locations
- 1,200 SMS a month, then 4p per SMS
- Everything in Clinic
- Custom sender name ("CityPhysio")
- Unlimited staff logins
- 30-minute onboarding call and signed DPA
- **Self-serve**, with an optional call. Because the deal size (£1,188 a year) can't pay for a sales process.

The gated feature on Clinic is matching rules, because only multi-therapist clinics need "offer this slot only to Sarah's patients".

## 3. Competitive pricing context

All prices from `founder/competitor-matrix.md`, checked 2026-11-01. None are older than 30 days, so none were re-checked.

| Competitor | Price | What's included | Where you sit |
|---|---|---|---|
| [Jane](https://jane.app/pricing) | CA$59 / 79 / 99 per practitioner a month | Full system. Auto waitlist only on Thrive (CA$99) | Below. Jane charges CA$20 more per practitioner to step from Practice to Thrive. Your Solo plan costs about the same as that step, without a migration |
| [Cliniko](https://www.cliniko.com/pricing/) | $45 (1 practitioner), $95 (2 to 5) | Full system, manual waitlist, SMS 10¢ each | Add-on on top. Clinic at £49 is roughly half of Cliniko's 2 to 5 plan. Justify it with £ recovered, not features |
| [WriteUpp](https://www.writeupp.com/pricing) | £19.95 to £45.95 per user | Full UK system, 100 SMS, waitlist with no auto offers | Between. Next integration target, same price bands work |
| [Zanda](https://zandahealth.com/uk/pricing/) | £15, or £25 + £15 per extra practitioner. SMS 9p | Full system, staff bulk-text the waitlist | Above. Zanda is a cheap system, you are a revenue tool. Don't target Zanda users first |
| [WaitOnce](https://www.waitonce.com.au/) | Not found. 30-day trial | Same Cliniko workflow, Australia | Publish GBP prices before it does. Public pricing is a gap in this market (5 of 7 hide it) |

## 4. Unit economics check

Inputs:
- Twilio UK outbound SMS: $0.056, inbound $0.0075, UK mobile number $2.50 a month ([Twilio](https://www.twilio.com/en-us/sms/pricing/gb), checked 2026-11-01).
- Estimate: $1 = £0.79, so outbound SMS = £0.044 and number = £1.98.
- Estimate: hosting £1 per clinic, £2 for Group.
- Estimate: ongoing support £3 (Solo), £4 (Clinic), £8 (Group) a month, at £20 an hour.
- Stripe UK cards: 1.5% + 20p (estimate, check your Stripe account).

| | Solo | Clinic (3 therapists) | Group (8 therapists) |
|---|---|---|---|
| SMS | 8 × 10 = 80 × £0.044 = £3.52 | 240 × £0.044 = £10.56 | 640 × £0.044 = £28.16 |
| Numbers | £1.98 | £1.98 | 2 × £1.98 = £3.96 |
| Hosting | £1.00 | £1.00 | £2.00 |
| Support | £3.00 | £4.00 | £8.00 |
| Stripe | £0.36 + £0.20 = £0.56 | £0.74 + £0.20 = £0.94 | £1.49 + £0.20 = £1.69 |
| **Cost** | **£10.06** | **£18.48** | **£43.81** |
| **Gross margin** | (24 − 10.06) / 24 = **58%** | (49 − 18.48) / 49 = **62%** | (99 − 43.81) / 99 = **56%** |
| Contribution | £13.94 | £30.52 | £55.19 |

Clinic is costed at its worst case (3 therapists). At 2 therapists its margin is 71%.

Break-even, estimate: £300 a month fixed costs (ICO fee, insurance, tools, domain), no founder salary.
- Solo only: 300 / 13.94 = **22 clinics**
- Clinic only: 300 / 30.52 = **10 clinics**
- Group only: 300 / 55.19 = **6 clinics**

To also pay you £3,000 a month: 3,300 / 30.52 = **109 Clinic-tier clinics**.

**Target blended ARPU: £44 a month.** Estimate mix: 50% Solo, 40% Clinic, 10% Group = £12.00 + £19.60 + £9.90 = £41.50. Push it to £44 by steering 2-therapist clinics to Clinic, not by raising Solo.

To lift margins, skip "slot taken" texts to patients who never replied.

## 5. Pricing psychology

1. **Anchoring: Group (£99) is the anchor.** Show it on the right of the page, so £49 looks moderate. Because almost nobody in a 1 to 3 therapist market buys it, its job is to frame Clinic.
2. **Decoy: Solo is the decoy for any clinic with 2 or more therapists.** It is capped at 1 therapist and has no matching rules, so a 2-therapist clinic can't use it. £49 for 3 therapists is £16.33 each, which reads as a deal next to £24 for one.
3. **Annual framing: "2 months free", not "17% off".** Then frame the price as appointments: "£49 a month. Less than one filled appointment." Estimate: a private physio session is about £55, from `founder/validate-idea.md`. Show the £ recovered number on the billing page at renewal.

VAT note: physio treatment is usually VAT-exempt, so most clinics can't reclaim VAT. Once you pass the £90,000 VAT threshold, your £49 becomes £58.80 to them. Plan the scale price with that in mind.

## 6. Launch pricing vs. scale pricing

**Launch price (first 90 days): Founding member, £19 Solo and £35 Clinic, for the first 20 clinics.** Because you have no case studies, no £ recovered data, and WaitOnce could enter the UK. In return, ask each founding clinic for a 15-minute case study call and permission to publish its numbers. Add a guarantee: if it fills no slot in the first 30 days, the next month is free.

**Grandfathering:** founding members keep their price for 12 months from signup. After that they move to the standard price with 60 days' notice, or they can lock their founding price for one more year by paying annually. Because it rewards the clinics that took the risk without capping your revenue forever.

**Price increases.** Raise prices for new customers by 20% to 25% when any of these hold for 60 days:
- Trial-to-paid conversion is above 50%.
- Median £ recovered per clinic is at least 8 times its plan price (for example £390 a month on Clinic).
- Fewer than 1 in 5 prospects mention price as a reason not to buy.

Raise existing customers at most once a year, by no more than 15%, with 60 days' notice and the £ recovered figure in the same email.
