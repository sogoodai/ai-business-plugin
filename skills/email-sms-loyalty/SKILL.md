---
name: email-sms-loyalty
description: Build and fix email, SMS, WhatsApp, loyalty, membership and referral programs for any small business (salons, restaurants, home services, tutors and coaches, ecommerce). Use for welcome, cart, rebook, win-back and review flows, popups, QR and Wi-Fi list capture, open and click benchmarks, Gmail and Yahoo deliverability, DMARC, TCPA, 10DLC, GDPR and PECR consent, WhatsApp template costs, punch cards, points, paid memberships, referral rewards and segmentation.
---

# Email, SMS, WhatsApp and loyalty: harvest the demand you already paid for

Built from 2025 to 2026 platform data (Klaviyo, Omnisend, Mailchimp, Postscript, Attentive, Toast, Bloom, Paytronix, Chatarmin, Meta, Google, Yahoo, FCC, ICO), 439 practitioner tactics from Reddit across beauty, local services, restaurants, education and ecommerce, two field experiments on AI-written email, and the best public skills (coreyhaines31 marketingskills, finsilabs, anthropics small-business, AgriciDaniel claude-email, aaron-he-zhu, ai-restaurant-claude). "Operators report" marks a practitioner anecdote with its thread score; everything else carries a source and year. Full list: [references/sources.md](references/sources.md). The owner's decisions and local law win over this guide. This is not legal advice.

## How owned channels actually make money

- **Triggers beat broadcasts by an order of magnitude.** Klaviyo 2026: flows were 5.3% of email sends and about 41% of email revenue; flow revenue per recipient about 18x campaigns. Omnisend 2025 data: automated email $3.41 per email vs $0.155 for campaigns (benchmark report) or $2.87 vs $0.18 (2026 ecommerce report). Bloom restaurants 2025 to 2026: one-off blasts brought back 0.27% of recipients, welcome 7.2%, at-risk win-back 6.5%. All vendor-attributed and intent-selected, but a 16x to 27x gap does not close.
- **The money is the second visit or order.** Toast Q1 2026: 7% of guests drive up to 50% of order volume; 86% of email-originated and 83% of SMS-originated orders came from repeat guests. Zenoti: the 42% of beauty clients who come back more than once a year make 80% of revenue.
- **SMS is an interruption budget, not cheap email.** Postscript 2026 p75: abandoned-cart SMS $10.95 per message and back-in-stock $13.34, campaign SMS $0.55. Spend texts on intent and time-sensitive inventory.
- **Opens are dead as a KPI.** Apple Mail Privacy Protection preloads pixels. Rank by incremental revenue or bookings, then conversion, then click, then unsubscribe and complaints. Opens are a deliverability diagnostic only.
- **Loyalty works when the reward arrives before the habit breaks.** Toast 2026: loyalty guests returned near 30% vs 7% baseline; more than half of diners quit programs because rewards were too hard to earn. Paytronix 2026: behavior shifts at visit four. All self-selected; use a holdout.
- **Referrals are asked for, timed and routed.** Jobber 2026: 59% of home-service owners name referrals a top source. App-based "refer a friend, get 15%" got almost nothing for a subscription box; a personal founder email at the one-year anniversary produced a "massive flow" (operators report, 154-pt thread).

## First session: ask, then compute

Ask the owner:

1. Business type, country and the countries of the people on the list (law follows the recipient).
2. Tools: ESP or CRM, SMS provider, booking/POS/store platform, WhatsApp Business app or API. Can you export 12 months of orders or visits with customer IDs?
3. List size per channel, and how each contact got there (form, checkout box, booking, imported, bought). Is the consent wording and timestamp stored?
4. Which automations run today, with their last 90 days of sends, clicks, orders or bookings.
5. Sending domain, whether SPF, DKIM and DMARC exist, and who else sends from that domain (booking tool, invoicing, Google Workspace).
6. Offers they will and will not run; margin per order or visit; whether discounts are allowed in win-back.
7. Spare capacity: which days, providers or SKUs need demand. Referral and gap-fill messages route there.
8. Loyalty or membership in place, its rules, redemption rate and liability.

Then compute ([references/segmentation-and-measurement.md](references/segmentation-and-measurement.md)):

```
flow share = automated revenue / total email+SMS revenue           (under 30% = flows missing)
revenue per recipient (RPR) = attributed revenue / delivered recipients   (same vendor, same AOV band only)
normal gap = median days between a customer's own orders or visits (3+ needed; else business median, label "estimate")
quiet = current gap > 2 x normal gap;  gone = > 3 x normal gap
replenishment trigger day = median reorder interval - shipping days - buffer
complaint rate = spam complaints / delivered   (keep < 0.1%, never reach 0.3%)
max referral reward (both sides) = target CAC - other acquisition cost per customer
loyalty net value = (member visits - holdout visits) x contribution per visit - reward cost
popup value per 1,000 visitors = incremental first orders x contribution - discount cost on orders that would have happened anyway
```

Report the three biggest leaks in money: missing flows, list decay or deliverability, and discount leakage.

## Build order (do not skip ahead)

1. **Instrument and authenticate.** Consent fields per channel, SPF, DKIM, DMARC `p=none`, one-click unsubscribe, STOP handling, 10DLC if US SMS. See [references/deliverability.md](references/deliverability.md) and [references/compliance.md](references/compliance.md).
2. **Four triggers before any newsletter**, each with an exit on purchase or booking:
   - Ecommerce: welcome, checkout/cart abandonment, post-purchase, back-in-stock or replenishment, then win-back.
   - Local services and beauty: new-client welcome, missed-call and quote follow-up, post-visit review plus rebook, due-soon then lapse.
   - Restaurants: signup welcome, first-visit to second-visit nudge, lapse by rhythm, visit-four milestone.
   - Educators: lead magnet nurture, trial or assessment follow-up, progress report before package end, renewal.
3. **Capture at moments of intent** (checkout, booking, Wi-Fi, receipt QR with a job), then popups. [references/capture.md](references/capture.md).
4. **SMS and WhatsApp only into high-intent triggers** first. [references/whatsapp.md](references/whatsapp.md).
5. **Loyalty or membership** designed around one repeat behavior. [references/loyalty-and-referrals.md](references/loyalty-and-referrals.md).
6. **Campaign calendar and testing loop** last.

Revenue-stage shortcut (NX ecommerce builder, MIT): pre-launch = welcome only; under $10k a month = welcome + cart + post-purchase; $10k to $50k = add browse, review, cross-sell; $50k+ = add win-back, VIP, replenishment, sunset.

## Benchmarks to check first

Open rates are inflated and not comparable across vendors. Full tables: [references/benchmarks.md](references/benchmarks.md).

| Metric | Typical | Upper | Source, year |
|---|---|---|---|
| Email campaign, ecommerce | 31.0% open, 1.69% click | 45.1% / 3.38% (top 10%) | Klaviyo 2026 |
| Email flows, ecommerce | 32.2% open, 5.58% click | 45.8% / 10.48% (top 10%) | Klaviyo 2026 |
| Campaign RPR, under $1M brand, $44 to $83 AOV | $0.11 median | $0.29 p75 | Klaviyo Help, Oct 2026 |
| Abandoned-cart email RPR | $6.77 | $13.70 (top 10%) | Klaviyo, 110k+ accounts, 2026 |
| Beauty campaign email | 44% open, 1.7% click, 4.2% click-to-book | n/a | Phorest, 530+ businesses, 2025 data |
| Restaurant email | 21.7% mean open, 2.1% click | n/a | Toast support benchmark 2026 |
| Education email | 35.64% open, 3.02% click, 0.18% unsub | n/a | Mailchimp, accessed Nov 2026 |
| SMS campaign | 12.39% CTR, 0.12% conversion, $0.15 per SMS | p75 $0.55 EPM (Postscript) | Omnisend 2025 data; Postscript 2026 |
| WhatsApp campaign | 72% median open, 12.0% click, 0.34% opt-out | n/a | Chatarmin, 382 brands, 2026 |
| Popup submit rate | 1.30% median (Poptin); 2.3% median (Klaviyo) | 2.67% p75; 3%+ target | Poptin 2026; Klaviyo 2026 |
| List growth | 1 to 3% a month "healthy" | n/a | Klaviyo Academy citing AgencyAnalytics (weak) |

No sourced email benchmark exists for home services, and no causal benchmark exists for paid memberships in small service businesses. Say so instead of inventing one.

## Decision rules the agent applies

- **No send without provable channel permission.** A phone number from a booking is a reminder channel, not marketing consent. Email consent does not cover SMS or WhatsApp. Fail closed when provenance is missing.
- **Transactional and marketing are separate systems.** Reminders, receipts and confirmations run regardless; marketing needs consent and quiet hours.
- **No lifecycle message after its goal happened.** Every flow exits on purchase, booking or reply. A "forgot something?" after checkout is the most common self-inflicted unsubscribe.
- **No discount before a no-discount version has been tested.** Cart message 1, win-back message 1 and replenishment never carry a discount. If over 30% of recovered carts used a code, the discount comes too early (finsilabs, MIT).
- **Lapse is per customer.** Never a flat 90 days. A six-week color client and a monthly massage client are on different clocks.
- **Segment only if it changes timing, content or offer.** Never send to a segment under 200 contacts as a test of anything (finsilabs, MIT).
- **Measure incrementally.** 10 to 15% holdout where the list allows (Paytronix 2026). On tiny lists, repeat tests over time.
- **Pause broad sends early.** At 10,000 delivered, 30 complaints is already 0.3%. Stop at 0.1%.

## Channel choice in one screen

| Need | Channel | Why |
|---|---|---|
| Education, news, long proof, receipts | Email | Cheapest per send; tolerates 24-hour delay |
| Cart, back-in-stock, same-week openings, expiry, payment failure | SMS (US, UK, AU) or WhatsApp (EU south, LatAm, India) | Intent decays in hours |
| Booking by reply, questions, service | Two-way SMS or WhatsApp | Measure booked-from-reply, not clicks |
| Reminders and confirmations | Transactional SMS, email, WhatsApp utility | No marketing consent needed; no promotions inside |
| High-value lapsed, unhappy customer | Phone call or personal email from the owner | "The apology is the offer" (anthropics, Apache-2.0) |

WhatsApp marketing costs $0.0118 per message in India, $0.0397 in Mexico, $0.0625 in Brazil and $0.1365 in Germany (Meta rate card, 1 October 2026); utility messages inside the 24-hour window became chargeable on that date. Fetch the live card before budgeting: [references/whatsapp.md](references/whatsapp.md).

## Loyalty and referrals in one screen

- **Punch card** for frequent, similar tickets with weak identification; pre-stamp 2 of 10 (34% vs 19% completion, Nunes and Dreze 2006). **Points or cashback** when tickets vary and the POS knows the customer. **Item rewards** for premium positioning (fine dining 20% vs 13% for cashback, Toast 2026). **Paid membership** only with a natural interval and spare capacity.
- First reward inside one or two normal visit cycles; redeem the usual order; recognize visit four.
- Referral reward budget = target CAC minus other acquisition cost; pay on the referred customer's paid, non-refunded purchase; push referrals only to providers or days with room (salon: +10% new clients from certificates given only to stylists under 70% productivity, Salon Today 2025).
- Judge every program on visits or orders and margin against a holdout. Depth: [references/loyalty-and-referrals.md](references/loyalty-and-referrals.md).

## When practitioners and the data disagree

| Topic | Practitioners say | Data says | Rule |
|---|---|---|---|
| Popup timing | Instant popup converts about 10% (operators); delay to time-on-page minus 5 to 10 s; trigger on 2nd page view | Delays of 20 to 50 s lifted capture 20 to 43% in Wisepops tests | Default engagement trigger; if an ad promised the offer, show it at once; test |
| Popup rate | 8% target, 18% "for seven-figure brands", 9% spin wheel | 1.30% median, 2.67% p75 (Poptin); 2.3% median (Klaviyo) | Reddit numbers are discount popups on ad traffic. Judge against your own baseline and dedupe repeat signups (about 25%) |
| Cart timing | 20 min, 4 h, 24 h | First email 2 to 4 h, second 20 to 48 h (Klaviyo) | Email at 1 to 4 h, SMS at 30 to 60 min only with SMS consent and carts over $30 to $50 |
| Cart recovery | "60% recovery" | 5 to 15% email recovery (public skills, uncited); voice + SMS 18 to 25% (operator, 1,000 carts) | Treat anything over 25% as a measurement error |
| WhatsApp opens | 98% | 79.6% weighted, 72% median (Chatarmin 2026) | Never quote 98% |
| Win-back count | One message, then stop | Three touches over 4 weeks (anthropics, Apache-2.0) | Max 3 touches across 2 channels, any reply stops it |
| Automation vs personal | Plain-text founder emails convert 4x | Flows earn 16x to 22x campaigns | Automate the trigger, write it plainly in the owner's voice; at under about 10 carts a day, write them by hand |

## Never

- Never buy, rent or scrape a list, or import contacts without their consent record.
- Never text marketing outside 9 am to 8 pm recipient local time (safe default; federal US is 8 am to 9 pm and several states are stricter).
- Never disguise marketing as a WhatsApp utility template to pay the lower rate.
- Never condition a reward on a positive review, or send review asks only to happy customers.
- Never use guilt in reactivation ("You made Duolingo sad" lost a 10-year user, 32-pt comment).
- Never broadcast one client's problem to the whole list (a graphic hygiene newsletter drew "I'd stop coming" replies).
- Never let a flat-dollar coupon outlive the catalog it was built for ($5 off a $6 item, operators report).
- Never invent a benchmark, an offer or a client quote; never send a message the owner has not approved.

## Before writing any message

Use the verbatim templates in [references/templates.md](references/templates.md) and the timing in [references/flows.md](references/flows.md). Plain text, one CTA, the owner's real name, a concrete slot or product, opt-out line where required. Run the slop test: would the owner say it out loud; could it go to another business with two words changed; does it open with a compliment; any phrase the owner never uses (anthropics small-business, Apache-2.0).

## References

- [benchmarks.md](references/benchmarks.md): email, SMS, WhatsApp, popup, loyalty and repeat-rate tables by vertical with source and year.
- [flows.md](references/flows.md): every automation with trigger, timing, exit, discount rule and copy arc, by business type.
- [templates.md](references/templates.md): verbatim email, SMS and WhatsApp copy for each flow.
- [capture.md](references/capture.md): popups, QR, Wi-Fi, checkout and booking opt-in, rates and tricks.
- [compliance.md](references/compliance.md): checklist for TCPA, 10DLC, quiet hours, GDPR and ePrivacy, UK PECR, CASL, Australia.
- [whatsapp.md](references/whatsapp.md): costs by country (Oct 2026), templates, windows, EU, LatAm and India playbooks.
- [deliverability.md](references/deliverability.md): Gmail, Yahoo and Microsoft rules, SPF, DKIM and DMARC setup, warming, list hygiene.
- [loyalty-and-referrals.md](references/loyalty-and-referrals.md): punch cards vs points vs paid memberships, measured lift, referral design and data.
- [segmentation-and-measurement.md](references/segmentation-and-measurement.md): segments worth building on a small list, lapse math, holdouts, AI copy testing.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [plan-90-days.md](references/plan-90-days.md): week-by-week plan with exit checks.
- [by-niche.md](references/by-niche.md): what changes for beauty, restaurants, home services, education and ecommerce.
- Sibling skills hold segment angles: `beauty-business` (rebooking, deposits, memberships), `restaurant` (regulars, visit-four, direct ordering), `ecommerce-brand` (store CRO, BFCM), `education-coaching` (launches, parents), `local-seo` (review requests and GBP).
