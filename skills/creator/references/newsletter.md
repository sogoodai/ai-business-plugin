# Newsletters: Substack, beehiiv, Kit, Ghost

Playbook for a writer whose business is an email publication: free list, paid tier, sponsorships, products. Flow design, deliverability law and consent rules in depth: sibling `email-sms-loyalty`. This file is the newsletter-as-business view.

## The economics in one screen

```
paid subscribers        = free list x free-to-paid conversion
paid MRR                = paid subs x (monthly price x monthly share + annual price / 12 x annual share)
paid subscriber LTV     = price x 1 / monthly churn      (beehiiv method: median price x estimated months)
sponsor revenue / issue = sponsored issues x price, where price = list size / 1,000 x CPM  (or median clicks x CPC)
max CPA per free sub    = (paid conversion x paid LTV x gross margin + sponsor revenue per sub per year) x payback share
source quality          = paid conversions per 1,000 free subs from that source, at 90 days
```

Benchmarks to calibrate (vendor data, say so when quoting):

| Metric | Typical | Better | Source, year |
|---|---|---|---|
| Free to paid conversion | 0.62% median | about 2 to 5% top quartile; top 10%: Finance 20%, Investing 18.7%, Economy 30.8% | beehiiv, thousands of paid publications, Jun 2026 |
| Free to paid by vertical (median) | Travel 0.30%, Finance 0.78%, Investing 0.84%, Sports 1.93% | | beehiiv, Jun 2026 |
| Monthly paid churn | Food & Drink 5.06%, News 5.47%, Sports 7.76%, Investing 11.72%, AI 13.33%, Money 16.67% | | beehiiv, Jun 2026 |
| Paid price | $10 a month, $100 a year median | Investing $27 / $292 median, $600 a year top quartile | beehiiv, Jun 2026 |
| Paid subscriber LTV (median) | $83 (Community) | $230 (Investing) | beehiiv, Jun 2026 |
| Median paid launch | 45 days after starting | | beehiiv, Jun 2026 |
| Substack's own free to paid guide | 5 to 10% "typical", 10% target | | Substack going-paid guide (older, pre-2024) |
| Open rate | 41%+ platform-wide | | beehiiv, 28B emails, 2025 data |
| Click rate | 4.59% regular sends | 13.48% automations | beehiiv, 15.68B emails, 2024 data |
| Network share of new Substack subs | over 50% of free, 30%+ of paid | | Substack, 2026 |
| SparkLoop paid acquisition | $1 to $5 per confirmed subscriber | | SparkLoop Help, 2026 (vendor) |
| Cancel flow recovery | 10 to 20% of cancel attempts | | beehiiv, 2026 (vendor estimate, not measured) |
| Dunning recovery | 20 to 40% of failed payments | | beehiiv, 2026 (vendor estimate) |

Conflict: beehiiv's 0.62% platform median and Substack's 5 to 10% guide differ by 10x. Different populations and maturity. Rule: plan on 1% of an engaged free list, celebrate 3%, and never quote 10% as normal.

Annual overtook monthly as the larger share of beehiiv subscription revenue in mid-2025 (beehiiv, Jun 2026). Default the checkout to annual and show the monthly equivalent.

## Growth channels, ranked by what operators report

1. **Network surfaces inside the platform.** Substack Notes and recommendations, beehiiv Recommendations. beehiiv says Recommendation Network users grow 2.75x faster and recommenders are 32x more likely to be recommended back (Jun 2025, vendor association). Turn recommendations on in week one and recommend 3 to 5 adjacent letters.
2. **Rank sources by paid conversions, not free signups.** One writer (22,000 free, 400 paid): recommendations brought about 15,000 free but only 77 paid; Notes brought 121 paid, the top paid source. Two 350,000-view TikToks produced fewer paid members than Notes (r/Substack, 205 pts). Substack itself cut low-quality recommendation signups in Dec 2025 because they caused spam reports and churn.
3. **Notes copy that works** (3,640 Notes over 15 months, one writer, r/Substack, 74 pts): statement openers beat questions (median 27 vs 19); first-person position or admission scored 40 vs 10 for leading with a number; news alone 9, news with an opinion in line one at the overall median; 73 to 100 words best; no links; 6 to 8 a day spread out; early morning and mid-afternoon best, 9pm worst. Milestone Notes ("Any writers under 1000 subscribers, connect with me!", 3.4K likes) get likes and no subscribers.
4. **30-minute daily engagement quota for 3 months:** 5 comments on writers you read, 10 likes, reply to every notification, 3 comments on new profiles. 1,600+ subscribers in 6 months after a flat year (r/Substack, 219 pts).
5. **Recommendation partners by growth rate, not size.** A slow-growing 15,000 list sent almost nothing (r/Substack, 84 pts). Balance swaps by subscribers delivered: if they sent 100 and you sent 50, give extra sends; offer 3 mentions for 1 to a list 3x your size (200k-subscriber operator, r/Newsletters, 55 pts).
6. **Meta lead-form ads with an audience callout** are the cheapest paid source operators report: €0.57 per subscriber over 21 days with a lead magnet, welcome open about 40% (r/Newsletters, 18 pts); local letters at about $0.31 with a 4-second "CITY NAME, PARENTS" callout and 50% opens, testing 4 ads with one variable each (r/Newsletters, 24 and 37 pts). One operator spends about $40 a day for 120 to 150 subs a day with a $0.50 ceiling (r/Substack, 39 pts). Pair with hygiene: 3,200 subscribers bought through Boosts and affiliates opened at about 20% (r/Newsletters, 15 pts).
7. **SparkLoop and paid recommendations.** Publishers set a CPA (example $4.50) and monthly cap; referred subscribers must stay subscribed and engaged through a 10 to 14 day screening period or are rejected (SparkLoop Help, Jul 2026). As a buyer, require source-level 90-day paid conversion before scaling. As a seller, it is filler income.
8. **Referral program with a cheap first milestone.** Classic ladder: 3 referrals a sticker, 10 a mug, 20 a t-shirt (The Pour Over, 20k to 100k+ in under 12 months, vendor case, 2021). The first reward must be reachable and cost almost nothing (a PDF, an archive post).
9. **LinkedIn for professional letters; X threads for analysis letters.** 6 LinkedIn posts a week grew 12,000 free subscribers (r/Substack, 109 pts); one big X thread per weekly article grew 0 to 2,362 at 45% opens, CTA "hit the link in bio" because links in posts throttle reach (r/Substack, 88 pts).
10. **Google for investing and reference content:** 32 of 45 paid subscribers (71%) of one stock letter came from Google, none from the Substack network (r/Substack, 55 pts). Publish on a domain you control.
11. **Reddit:** posting about your newsletter in r/Substack fails; posting a shortened article as value in reader-interest subreddits works (350,000 views, about 2,000 clicks, r/Substack 64 pts).

## Signup page and welcome

- **Paid-traffic signup page:** no scroll; headline, subhead, email field, button above the fold on mobile; remove archive and login links (r/Newsletters, 55 pts).
- **Concrete benefit:** "We interview NBA athletes to show you their mental preparation before games", not "Your go-to place for NBA interviews." Identity button: "Yes, I hate instant coffee." Promise an instant bundle so the welcome email gets opened (r/Newsletters, 18 pts).
- **Welcome system** (built from beehiiv's 13.48% automation click rate vs 4.59% regular): email 0 delivers the promised asset and sets cadence; email 1 sends the single best evergreen piece; email 2 asks one segmentation question; email 3 makes the first paid, product or affiliate offer; then the normal cadence. Flow templates: `email-sms-loyalty`.
- **First four sends by source:** watch opens, clicks and unsubscribes per acquisition source; network and ad subscribers decay differently.

## Converting free to paid

- **Every jump needs a dated event:** a price increase on a fixed date, a discount ending at midnight, a cohort close. "Other approaches did not come close" (r/Substack, 205 pts).
- **Grandfather and announce.** Keep existing paid at the old price and email the increase to free readers: zero churn, and the announcement converted more than any sequence (r/Substack, 109 pts).
- **Conversion emails sell what is coming,** "here's what you're about to miss", never "here's what we covered" (same thread).
- **Fixed paid day.** Half of upgrades happened on the weekly paid-post day versus 2% the day before (r/Substack, 205 pts).
- **Paywall mid-story,** at the unresolved moment. Worst converter: free intro, then the useful section locked.
- **More posts is not more paid.** A third weekly edition for 6 months: 25 editions, about 400,000 emails, 7 paying members (r/Substack, 205 pts). Keep one free and one paid a week until data says otherwise.
- **Keep the paid archive paid:** archive access is part of the renewal value.
- **What sells:** concrete data the reader acts on (holdings, comp data, screeners, deal lists, templates). In a technical letter, career content was about 70% of revenue and 4x revenue per post (r/Substack, 109 pts).
- **Substack Boost** sends an automated upsell to about 0.1% of the list per day with a default 20% first-year discount, plus pre-cancel offers (Substack, 2026). Turn it on only if the discount fits the pricing plan.
- **Churn and dunning are growth:** cancel flow (survey, pause, offer) and failed-payment retries recover what acquisition cannot (beehiiv 10 to 20% and 20 to 40%, vendor estimates).

## Sponsorships

- **Reality under 25k:** sponsors were detected in 5% of 1K to 5K lists, 5% of 5K to 25K, 14% at 25K to 100K, 29% at 100K to 500K (32,667 newsletters, r/Newsletters, 15 pts). Under 25K, put paid tier, products and affiliates first, and sell direct small sponsors early.
- **Early direct deals happen:** $100 slot at 200 subscribers; under $300 at about 1,000; a local sponsor at $250 a week on 4,000 (r/Newsletters 15, 19, 37 pts).
- **Networks underpay:** offers usually below $3 CPC or $6 CPM (beehiiv Ad Network, Paved, WellPut); at 4,000 subscribers one month paid $8.32 in Boosts and $29.94 in beehiiv Ads against $250 from one direct sponsor (r/Newsletters, 32 and 37 pts). Use networks only to fill unsold slots.
- **Pricing:** a newsletter primary sponsor runs $30 to $80 CPM on engaged lists (RevenueLab, 400+ disclosed deals 2024 to 2026, directional). Public skills list vertical bands (consumer $15 to 25, business $25 to 50, developer $30 to 60, finance $40 to 80, executive $50 to 100 CPM), uncited. Smart buyers divide price by median clicks per placement and compare with their best CPC, so quote both CPM and median clicks.
- **Local letters sell categories, not reach:** a 21,000-subscriber local letter makes about $300,000 a year from ads; real estate, healthcare and financial services held the top slots and 5 of 210 advertisers held over 50% of them (r/Newsletters, 36 pts). Pick advertiser categories before content.
- **Selling:** cold calling converted best; cold email from a separate domain got 10 to 25% opens and 2 to 4% replies; Meta video ads to a sponsor form cost $4 to $10 per sponsor lead (r/Newsletters, 15 pts). Outbound mechanics: sibling `b2b-outbound`.
- **Media kit for newsletters:** audience role and industry (survey or enrichment), country split, median unique clicks per sponsor placement, sponsor renewal count, sample placement with result. See [brand-deals.md](brand-deals.md).

## Platform choice

| Situation | Pick | Why |
|---|---|---|
| Personal essays, culture, politics, writer wants network discovery | Substack | Network drives over half of new free subs; 10% fee on paid |
| Media business, sponsors, multiple publications, referral tools | beehiiv | Recommendation Network, ad network, referral program, flat plans |
| Creator selling products and courses, automations | Kit | Commerce and automation depth |
| SEO-led publication on own domain | Ghost or beehiiv with custom domain | Archive ranks on your domain |

Operators report moving paid subscribers off Substack through Stripe without subscriber action and dropping the 10% fee (r/Substack, 45 pts). Risks: beehiiv terminated one publication for alleged non-genuine ad engagement and kept a $1,000+ wallet balance; withdraw ad earnings monthly (r/Newsletters, 46 pts). Substack: forwarded emails' upgrade button once let a recipient upgrade on the sender's card; tell readers to share links, not forward (r/Substack, 163 pts).

## Deliverability in one paragraph

After a year in spam, one operator recovered by warming a new sending domain from 50 emails a day over 6 weeks, removing 6-month non-openers, switching to double opt-in (signups about -30%, complaints down), fixed send days and fewer images (r/Newsletters, 21 pts). Opens are inflated by Apple auto-opens and clicks by corporate link scanners; replies and paid conversions are the honest metrics. Full setup (SPF, DKIM, DMARC, sunset rules): `email-sms-loyalty`.

## Tricks most writers miss

- The highest-engagement topic is often the lowest-converting one; an adjacent topic with half the reach brought paid subscribers (r/Substack, 205 pts). Track paid conversions per topic one week after each post.
- A recurring section readers look for ("The LinkedIn post of the week", a poll, a riddle) is among the most-clicked items and gives sponsors a stable placement (r/Newsletters, 55 pts; r/Substack, 89 pts).
- Under-$5 product right after signup to recover ad cost per subscriber (planned by an operator, untested). Test it only with paid traffic.
- For a local letter, print and legal notices can be revenue: one automated city letter claims $95k a year in legal notices (secondhand, r/Newsletters, 28 pts).
