# Loyalty, memberships and referrals

Every number here from loyalty vendors is self-selected: people who join were already more likely to come back. The only honest test is a holdout or a before/after with a matched group. Design around one repeat behavior and judge on visits or orders and margin after rewards, never on enrollments.

## Pick the mechanic

| Mechanic | Fits when | Avoid when | Evidence |
|---|---|---|---|
| **Punch card or stamp (paper or app)** | High frequency, similar tickets (coffee, bakery, car wash, lunch), weak customer identification | Tickets vary a lot; tourist or passer-by trade | Pre-stamped 10-stamp card (2 free) completed 34% vs 19% for a blank 8-stamp card, same 8 purchases (Nunes and Dreze, JCR 2006, car wash) |
| **Points or cashback** | Frequent visits, variable tickets, POS or store identifies the customer | First reward is months away | Casual dining cashback 24 to 26% 90-day retention (Toast 2026); more than half of diners quit programs with rewards too hard to earn (Toast 2026) |
| **Item or experience reward** | Fine dining, premium services, brand positioning matters | Commodity products | Fine dining item reward 20% vs cashback 13% retention (Toast 2026) |
| **Paid membership or maintenance plan** | Natural recurring interval and spare capacity to trade for commitment (massage, facials, lash fills, blowouts, HVAC, pest, cleaning, lawn, tutoring blocks) | Demand already exceeds capacity at full price; irregular need | Salons with memberships: sales +8% vs +2% (Zenoti 2025 data); med aesthetics members 90.4% vs 50.6% retention, an upper bound (CorralData 2026); no causal small-business benchmark exists |
| **VIP tier and recognition** | A small set drives most revenue (Toast: 7% of guests = up to 50% of orders) | Under about 50 repeat customers | Visit-four milestone shifts behavior (Paytronix 2026, survivorship-biased) |
| **Subscription (ecommerce)** | Consumable with a real usage cycle | Durable goods | Clearer subscription-benefit PDP raised opt-ins 29% and conversion 9% (Shopify, Magic Spoon case) |

No loyalty at all is the right answer when the trade has no plausible repeat: a boba shop living on passers-by tried stamps and points without building regulars (boba shop thread, 257 pts, via the `restaurant` skill). Invest in reviews and location instead.

## Design rules

- **Time to first reward under one normal visit cycle.** If guests come every 2 weeks, the first reward lands within a month or two, not after 20 visits.
- **Start them closer.** Pre-stamp 2 of 10 (endowed progress). A car-wash operator recounting the study reports the same effect (26-pt comment).
- **Target visit 2 and visit 4,** not "1,000 points". Visit 2 is where most customers are lost; visit 4 is where habits form in Paytronix's data.
- **Redeem the usual order.** A customer spending $25 to $30 four times a week was told at first redemption that the extra protein didn't count, and never came back (6-pt comment, 7-pt agreement).
- **Rewards with low variable cost and high perceived value:** a drink, dessert, add-on service, priority slot, early access. Early access to events and drops beats permanent discounts for regulars (research 2026).
- **Make the balance visible in every receipt and post-purchase email**; trigger "you have $5 waiting" when the redeem minimum is reached; expiry warning 30 days before points lapse, one of the highest-converting loyalty emails (finsilabs loyalty, MIT).
- **Points ecommerce defaults** (finsilabs, MIT; scale tiers to AOV): 1 point per $1 (0.5 on low-margin catalogs), 100 points = $1, 500 minimum to redeem; signup 100, review 50 (never conditioned on sentiment), referral 200 on purchase, birthday month 2x; reverse points on refunds; requalify tiers yearly with a 30-day downgrade warning. Targets: enrollment over 30% of customers; redemption over 20% (under 15% = threshold too high or invisible).
- **Double points instead of codes** for promotions keeps prices clean.
- **Change thank-you codes when strangers use them.** Coupon extensions such as Honey spread a repeat-customer code to first-time buyers (47-pt comment); use unique single-use codes.
- **Grandfather loyal subscribers through a price rise.** A box company kept $12 legacy subscribers at $12 with the upgraded box while new customers paid $29 (1,754-pt thread).
- **The "20% for a year" card:** a unique code good for 20% off, capped at 6 uses in 12 months, inserted into every email, all other coupons switched off; faster repeat orders reported, on roughly 10x product margin (181-pt thread). Only on high-margin catalogs.

## Paid memberships and maintenance plans

```
member contribution per month = fee - (expected redeemed services x variable cost per service) - card fees
break-even utilization = fee / (pay-per-visit price x contribution margin)
member net value vs holdout = (member visits - matched non-member visits) x contribution - discount given
```

- **Structure in three tiers** (research 2026, trades): Basic = scheduled preventive visit(s) plus reminder; Priority = Basic plus priority scheduling and a reduced or waived call-out fee; Protection = Priority plus selected consumables or inspection and a defined service credit. Price from expected service cost plus retention value, never a round monthly number.
- **HVAC example:** 200 to 400 contracts at $15 to $25 a month give $3,000 to $10,000 a month before service calls, built over 2 to 3 years; maintenance customers convert to equipment replacement at 3 to 4x cold leads (89-pt comment, trades consultant). Photograph wear at each visit and give a timeline: "your capacitor is at about 70%, it'll probably last another season but I'd plan on replacing it next spring" (same comment).
- **Offer rate before conversion rate.** Plan offered on 90%+ of eligible jobs; ServiceTitan's legacy targets are 30% service-call-to-agreement and 80% tune-up-to-agreement, labeled potentially outdated.
- **Gym and studio graduation path:** small-group training clients graduate into ongoing access memberships; about $1,800 client LTV (32-pt comment).
- **Service bundles that pay:** "book four a month and get half off the fourth", with base prices high enough to carry it (15-pt comment).
- **Watch liability and crowding.** Track entitlement use, freeze and cancel rate, unused balances (local accounting treatment) and whether members fill peak hours that full-price clients wanted (research 2026).
- **Annual prepay hides involuntary churn.** About 23% of a gym's annual members stopped paying within months on failed cards (1,353-pt thread). Run dunning from day one ([flows.md](flows.md)).
- Beauty-specific membership design (series to membership, wording that loses members) lives in the `beauty-business` skill.

## Referrals

What the data supports: referrals and repeat work are each a top lead source for 59% of home-service owners (Jobber 2026). Formal referral-rate benchmarks are weak (Housecall Pro's 2 to 10% referral rate is third-party and unsourced).

**Sizing:**

```
max total reward (both sides) = target CAC - other acquisition cost per customer      (coreyhaines31 referrals, MIT)
  example: target CAC $200, other costs $40 -> up to $160 combined, e.g. $80 each side
referral return = (net referred contribution - program cost) / program cost, same cohort and window; use a holdout or call it "attributed"
```

**Design rules:**

- **Pay on the paid outcome, not the lead.** Reward after the referred customer pays and passes the refund window (7 to 14 days ecommerce, finsilabs MIT; first paid package for tutors, research 2026).
- **Route referral incentives to spare capacity.** One salon gave $50 off $250+ certificates only to stylists under 70% productivity and grew new clients 10% (Salon Today 2025). A busy provider gets no referral push.
- **Ask at a moment and name the capacity:** "I have a couple of openings next week if you have any friends who need..." plus cards (operator). One stylist only tells favorite clients when she has room and keeps a full book (1,057-pt thread).
- **Personal beats programmatic for small brands.** An app "refer a friend and get 15% off" got little response; a founder email at the one-year subscription anniversary offering a free box to someone they "would LOVE" brought a "massive flow" and better churn (154-pt thread). Template in [templates.md](templates.md).
- **Small, fast, service-native rewards:** a free hour of service per referral (computer repair owner, 6-pt); a quick add-on such as scalp massage, brow wax or polish change (9-pt); 20% off for both neighbors on the next lawn job (9-pt); a handwritten thank-you card (OP got a carton of drinks back, 2,215-pt thread).
- **Route-density referrals for home services:** a bigger discount for the next-door neighbor, smaller for a walkable one, more for consecutive houses (17-pt comment). Fill the route, not just the calendar.
- **Double-sided for ecommerce** (finsilabs, MIT): referrer $10 store credit after the refund window; friend 15% off first order (15% beat 10% for first-order conversion); $30 minimum; cap 5 to 10 referrals a month; placements in order: post-purchase page, confirmation email ("Give $10, Get $10"), account page, packaging insert; one-tap WhatsApp or SMS share.
- **Under about $100, lead with dollars ("$10 off" a $25 item, not "40%"); over $100 test percent** (coreyhaines31, MIT).
- **Professional partners beat customer programs for coaches and trades.** A coach gets 95% of clients from referrals after years of unprofitable digital ads (22-pt comment); another prices referral-partner packages at about $115 per session vs $150 base because partners pre-vet clients (7-pt). In regulated trades, default to reciprocal introductions; paid referral fees can raise licensing or anti-kickback issues (research 2026).
- **Look for audience inside the customer list.** One founder Googled every customer, found prominent athletes and realtors, and asked personally (116-pt thread).

**Where referral programs failed:**

- A tutor offered free classes to three parents for converted referrals; one shared on WeChat Moments and nobody responded (25-pt thread). Incentives do not create advocacy that isn't there; ask the parents whose child visibly improved, with a progress report in hand.
- Discounting a difficult client "because she'll refer friends" brought referrals of the same kind of client expecting the same 25% off (361-pt thread, 300-pt comment).
- A referral that wants "to figure it out as we go" cost a consultant two months of unpaid revisions and then the referrer's own $1,000 to $1,200 a month account (828-pt thread). Screen referrals like any lead; if one goes badly, call the referrer first and ask for advice.
- Referral-driven growth past delivery capacity: an agency at $60,000 a month lost quality and fell to about $20,000 (43-pt reply).
