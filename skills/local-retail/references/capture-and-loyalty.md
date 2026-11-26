# POS capture, regulars and loyalty

Flow build order, deliverability, consent law details and loyalty math live in `email-sms-loyalty`. This file covers what changes in a shop: the till is the capture point, purchases are irregular, and many categories are one-off.

## Why identity matters more than followers

- A regular (4+ purchase days a year) spends about 6x a transient buyer (Square, March 2026).
- Sellers that launched email marketing, text marketing or loyalty saw an average 5% increase in transactions in the next 3 months vs the prior 3 (Square 2026, before/after, not causal).
- A customer record links to purchases; a follower does not. Track identified rate and the move from visit 1 to 2, 3 and 4. Enrollment counts nothing.

## The capture prompt

**Rules**

- One prompt at payment, asked by the person at the till every time. Staff skip it when rushed; make it part of the receipt question.
- Name the value. "Want the receipt by email?" plus what they will get and how often.
- Minimum fields: email or mobile, then one preference. Never name, birthday, phone, email and ZIP at once (research synthesis 2026).
- Preference field options match how the shop buys and messages: women's, men's, kids, gifts, books (genre), records, furniture, flowers, a branch.
- Capture consent per channel. Email consent does not cover SMS.
- Log the source code (event, partner, counter, online) on the record.

Wording: [scripts.md](scripts.md#pos-capture).

**Other capture points**

- QR on receipts, bags, gift tags and the counter card, landing on a one-field form with the preference picker.
- Event signups with a reason (early access, next event tickets).
- Wishlist and waitlist slips: "Tell me when the next one comes in" with item, size, era, author.
- Guest Wi-Fi with an explicit opt-in box (cafe-shops and bookshops with seating).
- Tablet signup at checkout with "10 to 15% off your next visit" is common in templates (AgriciDaniel claude-email local-business asset, MIT, uncited). Prefer a non-discount value first; add a next-visit offer only if capture stays low.

## Consent by country (summary)

| Market | Rule for marketing email and SMS |
|---|---|
| US | Email: CAN-SPAM opt-out model. SMS: express written consent (TCPA), STOP handling, quiet hours. A phone number given for a receipt is not texting consent |
| UK | PECR: consent, or soft opt-in for your own customers buying similar goods if opt-out was offered at collection and in every message (ICO) |
| EU | ePrivacy national laws plus GDPR; soft opt-in varies by country |
| Canada | CASL: consent, sender identification, working unsubscribe (CRTC) |
| Australia | Spam Act: consent, identification, easy unsubscribe (ACMA) |

Do not roll out one US-style checkbox everywhere. Full checklist: `email-sms-loyalty` compliance reference.

## Flows for shops (priority order)

Klaviyo 2026: SMS flows order at 1.9% vs 0.27% for campaigns. Build triggers before newsletters.

| Flow | Trigger | Content | Shop notes |
|---|---|---|---|
| Welcome | Signup | Who we are, what is new, next event, review link after the first purchase | One email plus one text if SMS consent |
| Post-purchase | Purchase with ID | Care tips, matching items, review ask on day 3 to 5 | Florists: care card and "vase refill" reminder |
| Back-in-stock / waitlist | Item, size or author arrives | Item photo, hold for 48 hours | Highest-intent message a shop sends |
| New arrivals matching first purchase | New stock tagged with same category | 3 items, prices, "reply HOLD" | Antiques and vintage: this replaces replenishment |
| Category rhythm | Category reorder time passes | Next book in series, seasonal refresh, plant food | Set by category, not a flat 30 days |
| Birthday or occasion | Date captured later | Gift reminder for others ("Mum's birthday is in 2 weeks") | Florists and gift shops: occasion reminders sell more than birthday treats |
| Quiet customer | Gap over 2x their own median gap (3+ purchases) | New arrivals, invite, no discount first | Rhythm rule from anthropics small-business (Apache-2.0) |

Track flow orders and revenue per recipient against campaign sends. Do not judge a 400-person list against DTC brand benchmarks.

## VIPs and clienteling

- **VIP = top 10 to 20% by 12-month spend** or anyone with 4+ purchase days (Square's regular). For a small shop that may be 30 to 150 people.
- **Personal texts from the owner or a named staff member**, not campaigns: new arrival in their size, a hold before it hits the floor, an invite to a preview hour. Wording: [scripts.md](scripts.md#vip-texts).
- **Clienteling notes on the POS record:** sizes, authors, eras, colors, who they buy for and when.
- **Preview hour before a drop, sale or holiday season** for VIPs only. Costs nothing and creates the "first access" the capture prompt promised.
- Shopify's PAIGE case reports clienteling emails at 69% open and 24% higher AOV (vendor case, large brand, opens inflated by Apple Mail Privacy Protection).

## Loyalty formats for shops

| Format | Fits | Watch |
|---|---|---|
| Points or spend-based rewards in the POS | Gift shops, bookshops, boutiques with repeat categories | Reward reachable within 2 to 3 normal visits |
| Punch card | Frequent, similar tickets (books, coffee corner, flowers) | Failed to turn passing boba traffic into regulars (operators report, 107-upvote comment). Weak where buyers do not come back by habit |
| Paid membership or club | Bookshop subscription box or signed-edition club, florist monthly arrangements, vintage "first look" club | Needs fulfillment capacity and a clear monthly value |
| Prepaid return product | Refillable vase, book club pickup, alteration plan | Kennedy's Flowers: 11,000+ refills, $182,000+, 200 visits a week (SAF 2025) |
| Wishlist and early access | Antiques, vintage, art, one-off stock | No points needed; scarcity is the reward |

Design rules (reward timing, pre-stamped cards, holdouts, referral budgets) are in `email-sms-loyalty`.

## Referrals

- A handwritten note to customers who refer friends (about 10 minutes, stationery and a stamp) earned a gift back from the referrer (r/smallbusiness, 2,216 points).
- For shops: a gift for the referrer on the friend's first purchase (not a discount on unrelated items), or a joint "bring a friend" preview night.

## Tricks most owners miss

- **Event capture tag:** every record captured at an event carries the event code; compare 90-day value by event.
- **Gift buyers are two customers.** Capture the giver; offer to remind them of the recipient's date next year.
- **Post-holiday exchange message** is a second-purchase prompt: send it to gift-card and gift-receipt buyers in early January.
- **For one-off categories, the waitlist is the loyalty program.** A rural media reseller kept a list of buyers who asked to hear about the next lot (r/Flipping, 1,841 points).
- **Mailing address for a free upgrade today** (a restaurant pattern: "free upgrade if you join our birthday club", r/smallbusiness, 1,209 points) works at the till for printed lookbooks and holiday catalogs.
