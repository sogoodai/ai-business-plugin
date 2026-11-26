# Segmentation and measurement

The hidden asset is not the list. It is the event chain consent, message, click or reply, booking or order, margin, next visit. Without it, personalization is fluent guessing and loyalty ROI is attribution theater (research 2026).

## Segments worth building on a small list

Create a segment only if it changes timing, content or offer, or carries a planned test. "VIP women 35 to 44 who opened twice" is useless if it gets the same campaign. Mailchimp's BFCM 2025 data showed segmented or personalized campaigns at $166 vs $150 AOV (+11%), observational.

The seven fields that cover most small businesses: recency, frequency, monetary value, category or service bought, predicted next date, first-time vs repeat, location or staff member.

| Segment | Rule (pick one definition per business and reuse it everywhere) | What changes |
|---|---|---|
| New subscriber, no purchase | 0 orders or visits | Welcome flow, first-order offer |
| First-timer | exactly 1 order or visit | Second-visit push at the format's return window; this is where most customers are lost |
| Repeat / active | 2+ and one within the normal gap | Normal cadence, cross-sell, referral ask |
| VIP | top 10% by spend, or 5 to 6+ orders or $500+ (finsilabs, MIT); restaurants and salons: 4+ visits | Recognition, early access, no discounts, owner note |
| Quiet | current gap > 2x own normal gap | Win-back ladder |
| Gone | > 3x | One last-chance message, then low-cadence list |
| Discount-only buyers | only ever bought with a code | Keep out of full-price launches; switch to value messaging |
| Unengaged | no click, order, booking or reply in 180 days | Exclude from campaigns; sunset |

Send rules (finsilabs, MIT): VIP at most 2 emails a week and never in discount sends; never test on a segment under 200 contacts; Klaviyo-style smart sending 16 hours between messages.

Predictive CLV and churn in Klaviyo need roughly 500+ purchasers and 180+ days of orders (harvest reviewer note). Most stores under $1M use the rule-based windows here.

## Lapse math

```
gaps = days between consecutive orders or visits for one customer
normal_gap = median(gaps)                    # needs 3+ visits; else use business or service median, flag "estimate"
quiet if days_since_last > 2 x normal_gap    # anthropics small-business, Apache-2.0
gone  if days_since_last > 3 x normal_gap
at_risk (softer) if > 1.5 x normal_gap       # finsilabs lifecycle, MIT
priority = lifetime spend, then frequency, then last order size   # not length of silence
```

Sanity-check dates first: duplicate orders, refunds and gift purchases distort gaps. One-time buyers are not "at risk" before about 45 days in ecommerce (finsilabs, MIT).

Flagged first: a customer who left a negative review and then stopped buying (call, no offer). Behavior signals that precede bad reviews: fulfillment time drifting up, 3+ refunds on one SKU, rising split shipments, rising share of first-order customers who never return (anthropics, Apache-2.0).

## Targets to track (finsilabs lifecycle, MIT, uncited)

- Subscriber to first purchase over 10% within 30 days.
- First-time buyer to repeat over 30% within 90 days (compare with category repeat rates in [benchmarks.md](benchmarks.md): coffee 31.7%, jewelry 16.9% over 365 days).
- Loyal customers over 40% of revenue.
- Restaurants: first-to-second visit conversion at 30, 60 and 90 days; loyalty 90-day active rate (66 to 72% in Paytronix's best segments).
- Educators: month-N retention = cohort customers with paid activity in month N / cohort start; code cancellations (achieved goal, schedule, affordability, mismatch, service issue, season ended, moved to AI or self-study, competitor, unknown). Only 6% of music-school cancellations cited cost (Opus1 2026).

## Proving it works

- **Holdouts:** 10 to 15% untreated group on each flow and campaign where the list allows (Paytronix 2026). Compare visits or orders and margin over the same window.
- **Attribution windows:** state them. Vendor dashboards count opens or 24-hour view-throughs; incremental revenue is usually lower.
- **Primary metric order:** incremental revenue or bookings, then conversion, then click or reply, then unsubscribe and complaint. Opens only as a deliverability alarm.
- **Two-way channels:** measure qualified reply rate and booked-from-reply rate. Route any reply containing a date, a service name, "price", "availability", "book" or a question mark to a person or the booking tool at once (research 2026).
- **Tiny lists:** run the same A/B across several sends and pool results; do not declare a winner on one underpowered campaign.
- **Revenue check against cost:** one operator's $20-a-month email tool returned $881 attributed (160-pt thread); fine, but compute contribution, not revenue.

## AI-written messages: what the evidence says

- **Wine Access, three randomized trials (Dube and Xu, 2025):** AI and hybrid email copy roughly matched professional writers on gross profit, so the win was lower cost; a prompt-based GPT cell later beat human copy by 8 to 9%.
- **Causal alignment field experiment (Angelopoulos, Lee and Misra):** across 36 campaigns and 283M impressions, a model aligned to past A/B outcomes raised subject-line CTR 32% vs unassisted humans; a larger general-purpose LLM did not improve outcomes.
- **Mailchimp, Oct to Dec 2025:** emails using its AI feature showed 50% higher order rate and 33% higher conversion; adopters differ from non-adopters, so not causal.
- **Attentive, 25B+ SMS, 2026:** content components moved conversion from +19% to -24%; superlatives -11.4% and jargon -7.8% in non-offer sends.

Agent workflow: retrieve the last 20 comparable messages and their results; generate variants that differ on one meaningful dimension (timing, offer, CTA, proof, framing); enforce brand and legal rules; hold out 10 to 20% where volume permits; pick winners on conversion or gross profit, not opens; write the result back to the creative history. "Generate and send" without that memory is the wrong architecture.

## Copy rules with evidence

- Concrete benefit, exact offer, deadline, one CTA. No "game-changing", "best ever" or insider terms (Attentive 2026).
- Plain text in the owner's voice for small senders (115-pt and 61-pt threads); build a voice profile from 15 to 30 emails the owner actually sent (anthropics small-business, Apache-2.0).
- Email length: 50 to 125 words transactional, 150 to 300 educational; one primary CTA; first-name fallback "there" (coreyhaines31 emails, MIT).
- Banned openers: "I hope this email finds you well", "I wanted to reach out", "Just checking in", "Quick question for you" (anthropics slop test, Apache-2.0).
