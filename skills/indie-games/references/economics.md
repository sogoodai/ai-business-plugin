# Economics: what a wishlist is worth and what to pay for one

Run these before recommending any spend, publisher deal or price. Use the developer's own Steamworks numbers wherever they exist; external numbers are priors.

## 1. Revenue waterfall (gross to take-home)

A real case, $560,000 Steam gross over five years, two games (r/gamedev 3,460, 2026):

| Step | Amount | Running total |
|---|---|---|
| Gross | | $560,000 |
| Refunds (22%; 60%+ of sales from China) | -$134,000 | $425,000 (approx.) |
| Steam 30% | -$127,000 | $297,000 |
| US withholding (30% with no treaty, 5% after moving to Thailand) | -$9,700 | $287,700 |
| Regional publisher (China, Korea, Japan only) | -$115,000 | $172,000 |
| Local digital income tax 15% | -$26,000 | $146,000 |
| Co-founder split 50/50 | | **$73,000 each, about $15,000 a year** |

Second case: Mortal Glory, $128,884 revenue, Steam sent $76,592 (about 59%), about $55,063 after personal income tax (43%) (r/gamedev 1,941).

Rules:
- Plan on Steam paying out about 55 to 60% of the dashboard gross with normal refunds and no publisher. Steamworks gross includes VAT and sales tax where collected.
- File the W-8BEN with treaty country; no treaty means 30% US withholding on US sales.
- Valve's cut drops to 25% after $10M and 20% after $50M per title; irrelevant for almost every indie, do not model it.
- Segment refunds by country before blaming the game. A commenter with 325 upvotes made the point: "22% in China and 2% elsewhere" needs a different fix from "22% everywhere".

## 2. Wishlist forecast

```
week-one units = launch wishlists x k
k: weak 0.05, central 0.15, strong 0.30
first-year units: no public benchmark; Mortal Glory sold 5,000 in week one and 17,525 in year one (3.5x)
```

- Central k is GameDiscoverCo's 2024 to 2025 median for games over 25k (0.15x). The spread between games is 10 to 20x, so always show three scenarios.
- Lower k when: many wishlists came from a free prologue or F2P hub (WarriOrb: a third of 16k wishlists from 80,000 free-prologue claims, 1.1% of wishlisters bought by day 3), from giveaways, from cheap Asian ad traffic, or are over a year old.
- Raise k when: a recent demo converts above 20%, wishlists are recent and creator-driven, the price is under $10, and the seven-day review score will be above 90% (high converters averaged 91% vs 67%).
- An operator forecast 20% with 10% as "worst case" and landed near 5% (r/gamedev 3,385). Treat published "poor" benchmarks as the middle, not the floor.

## 3. Value per wishlist and the ad ceiling

```
net per sale = price x (1 - launch discount) x 0.70 x (1 - refund rate) x (1 - VAT/sales tax share)
value per wishlist = net per sale x first-year conversion
max cost per wishlist (CPW) = value per wishlist x 0.5
```

Worked example: $15 game, 10% launch discount, 11% refunds, 10% blended tax share, first-year conversion 0.15.
- Net per sale = 15 x 0.9 x 0.7 x 0.89 x 0.9 = $7.57
- Value per wishlist = 7.57 x 0.15 = $1.14
- Max CPW = about $0.57

A commenter's rule of thumb gives the same order: "$1 per wishlist is expensive unless the game sells for around $20" (r/gamemarketing). The 0.5 factor leaves room for overestimated conversion; an ad can still earn more through the Discovery Queue lift from launch sales, but do not bank on it.

Operator CPW data to compare against: Reddit ads $0.75, $1.26, $1.48; VK $0.65; paid creators $1.88 and $3.72; outsourced marketer $3.29; paid community posts $3.40; TikTok agency over $10. Vendor creator cases claim $0.15 to $0.24.

Kill rule: review CPW weekly per channel and stop any channel above the ceiling for two consecutive weeks. The visual novel developer knowingly paid $1.48 against a $1.00 target to chase 7,000 wishlists and called it a mistake (r/gamedev 924).

## 4. Event lift (do not count the baseline)

```
baseline = median daily net wishlists over the last 28 days with no event
lift = wishlists in the event window - baseline x days
cost per incremental wishlist = spend / lift
```

"Sir, We Have an Orc Problem" got about 18,000 wishlists in Next Fest week, but only a few thousand above a normal week (r/gamedev 2,332). Trapster's case subtracted a 1,400 a day baseline before claiming 6,600 incremental. Use the same method for creators, festivals and ads.

## 5. Publisher hurdle

```
required sales lift to break even = 1 / developer share - 1
```

| Developer share | Publisher must lift net sales by |
|---|---|
| 67.9% (Voyer no-advance average) | 47% |
| 57.9% (Voyer with-advance average) | 73% |
| 50% | 100% |
| 45% (a "standard deal" offered to a 1,500-wishlist student team) | 122% |
| 24% (average first tranche in stepped deals) | 317% until recoup |

Then subtract recoupable marketing, porting and localization if the contract lets the publisher deduct them before the split. A regional-only deal changes the math: the same student team negotiated 50/50 on China, Japan and Korea only, 100% elsewhere, publisher paying its own marketing (r/IndieDev 5,171). A regional publisher that took about $115k was estimated to have doubled sales and owned access to the biggest market (r/gamedev 3,460); top comments (993 upvotes) warned against dropping it to save the cut.

## 6. Localization payback

```
localization payback = (country wishlist share x expected units x net per sale) / translation cost
```

Check the Steamworks wishlist report by country first. A visual novel spent $2,800 on EN/CN/JP and dropped Japanese after seeing few Japanese wishlists; AI translation plus native proofreading was "good enough" for the rest (r/gamedev 924). In the other direction, small-market localizations (Indonesian, Romanian) produced 78 and 45 wishlists in a 38-hour demo window (r/gamemarketing 72) and a Portuguese TikTok found a Portuguese streamer. Valve uses supported languages in recommendation relevance, so cheap languages can pay through discovery as well.

## 7. Mobile unit economics

```
cohort LTV(day N) = sum of revenue per install by day N, per country x OS x source x creative
payback = CPI / (LTV per day after store fees)
scale only if LTV(D90 or D180) / CPI > 1.3 with a cash buffer
```

Store fees: 15% for small developers in the Apple and Google small business programs (under $1M a year), 30% above. Use your own cohort curves; never mix Adjust and GameAnalytics medians.

## 8. Time value of a small game

Short projects with a clear hook have the best ratios in the data: Bunny Park, 6 weeks, $5, about $30k in a year (r/gamedev 2,282); Marble's Marbles, under 2 months, $30k+ in month one (r/gamedev 936); "Sir, We Have an Orc Problem", 4 months, $361,657 gross in 24 hours (r/gamedev 2,332); Paddle Paddle Paddle, 4 months solo, 183,000 sold (r/Unity3D 1,211). Compare with a 1.5-year game at about $7k per developer per year (same 2,332 thread). Recommend prototype-and-test cycles of two weeks (Outbound studio cap) before committing years.
