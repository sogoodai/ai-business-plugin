# Economics: formulas and worked examples

Wedding numbers lie in two ways: the booking lag (a 2026 inquiry may be a 2027 wedding) and the gap between booked and collected money. Always state the cohort (inquiry month), the denominator and whether a figure is booked or collected. Reject any metric without both.

## The funnel, defined per vendor type

Never blend vendor types into one "conversion rate" (research pass, 2026). Use the stage that matches the sale:

| Vendor | Stages |
|---|---|
| Venue | inquiry -> two-way reply -> tour -> hold or proposal -> signed + deposit |
| Photographer, videographer, DJ, band | inquiry -> two-way reply -> call or showcase -> proposal -> signed + retainer |
| Florist, planner, decor | qualified inquiry -> design consult -> proposal -> signed + deposit |
| Caterer | inquiry -> tasting -> proposal -> signed + deposit |
| Rentals | qualified request -> quote -> paid reservation |
| Corporate (any) | RFP -> proposal within 1 to 4 days -> provisional hold -> contract |

```
two-way rate         = inquiries with at least one reply from the couple / all inquiries
stage rate           = reached stage n+1 / reached stage n (same inquiry-month cohort)
cohort booking rate  = signed with retainer / qualified inquiries
qualified inquiry    = date open + inside service area + budget band at or above the minimum
```

Worked example (photographer, 12 months): 180 inquiries, 120 qualified, 70 two-way, 34 calls, 24 proposals, 16 signed. Booking rate on qualified = 13%. Two-way is 58%: half the qualified couples never answered the first reply. That is the first fix (reply speed, SMS, price in the first message), not more traffic.

## Contribution per booking

```
contribution = contract value
             - second shooter or associate pay
             - outsourced editing, album and print cost
             - wholesale flowers, hard goods, labor (florist)
             - food cost and event staff (caterer)
             - delivery, setup, strike labor and damage allowance (rentals)
             - travel, parking, hotel
             - card or payment fees (about 3%)
```

Owner time is not in contribution but belongs in the hourly check:

```
effective hourly = contribution / (consult + planning + event + travel + editing or production + revisions hours)
```

Editing load (operators report): about 4 editing hours per shooting hour for photography (r/WeddingPhotography 114); a 4-hour, two-location video booking took 28+ hours of editing (r/weddingvideography 19); solo videographers report about 35 hours per wedding all in, teams 25 to 50. One photographer with 25 years in reports editing a wedding in 2 to 3 hours by controlling light and shooting deliberately, earning about $300 an hour all in (r/WeddingPhotography 203). Editing hours are the biggest hidden cost in photo and video pricing.

## Required average booking

```
required avg booking = (owner income target + business overhead + taxes) / realistic bookings per year
```

Example (operator, r/WeddingPhotography 50): $80,000 need / 25 weddings = $3,200, at 60 to 80 hours per wedding. Check the realism of the denominator: 25 weddings with 76% of demand in six months means about 4 a month in season, which is often the physical cap for a solo shooter who edits.

A $5,000 package is not $5,000 of income. One photographer computed $25 to $30 an hour after second shooter, overhead and taxes on a $5,000 middle package (r/WeddingPhotography 35-upvote comment; another commenter noted tax applies to profit, not revenue, so recompute with real numbers).

## Date value and displacement

The scarce asset is the date, not the hour.

```
date value          = contribution of the booking that date normally attracts
displacement cost   = date value - contribution of the booking that actually took it
peak share          = bookings on the top 20 dates / all bookings
```

Example: a photographer's peak June Saturday normally books the 8-hour $4,800 package (contribution $3,900). A 4-hour $2,200 package (contribution $1,700) takes it 14 months out. Displacement cost = $2,200. That is why operators remove the smallest package from peak dates (r/WeddingPhotography 46) and why a portfolio-rate booking taken more than a year ahead hurts twice: the price was set before the raise (r/weddingvideography 18).

Rule: on the top 20 dates, accept only packages at or above 80% of that date's normal contribution, unless the owner chooses otherwise. Off-peak dates have a date value near zero, so a small package there is pure gain.

## Channel economics

```
source CAC     = (subscription or listing + ad spend + show costs + agency + labor answering that source) / signed bookings from that source
booking ROAS   = contracted revenue / media spend
cash ROAS      = collected revenue attributable / media spend
CMER           = contribution from source / total marketing cost of source
payback test   = keep a source only if CMER beats the owner's target (start at 3) after the booking lag
```

Scale on CMER and open dates, never on CPL.

### Marketplace example (The Knot, WeddingWire)

The Tahoe venue (IVGID, July 2023 to June 2024, possibly outdated): $5,880 on The Knot -> 206 leads at $29; $5,880 on WeddingWire -> 282 leads at $21; Google $13,215 -> 97 leads at $136. No booking data was reported, which is exactly the problem. Apply Mikla's 2026 tour rates to show why CPL misleads:

| Source | Leads | CPL | Tour rate (Mikla) | Tours | Cost per tour |
|---|---|---|---|---|---|
| The Knot | 206 | $29 | 10.0% | 21 | $280 |
| WeddingWire | 282 | $21 | 7.4% | 21 | $280 |
| Google (website form) | 97 | $136 | 18.1% | 18 | $734 |

Here marketplaces still win per tour, because their CPL was very low. The decision changes with your own CPL, tour-to-booking rate, average booking value and staff time per lead (marketplace leads ghost 58 to 66% of the time, so labor per tour is higher). Compute with the owner's numbers before keeping or cutting. Illustration only: the tour rates come from another dataset.

### Bridal show math

```
fully loaded show cost = booth + decor and samples + travel + staff hours x rate + print + follow-up hours
show CMER              = contribution from bookings traced to the show, after 6 to 12 months / fully loaded cost
```

Studio4Motion's practitioner guide (2026, low confidence): 75 to 150 leads, 10 to 20% to consult, 30 to 50% of consults book. At the midpoint, 110 leads -> 16 consults -> 6 bookings. With a $1,800 fully loaded cost and $1,600 contribution per booking, CMER = 5.3. With the operator's real January result (0 bookings), CMER = 0. Judge each show on its own and on at least two editions; the first run of anything underperforms (marketingskills `events`, MIT).

### Google Ads math

```
max CPL = contribution per booking x target booking rate / target CMER
```

Example: contribution $2,800, inquiry-to-booking 12%, target CMER 3 -> max CPL = $2,800 x 0.12 / 3 = $112. The Arch Wedding Studio case ran $98 to $117 CPL on destination work with higher ticket, which fits. A $1,800 DJ with $1,200 contribution and 15% booking rate has a $60 ceiling; Google at $100+ CPL loses money there.

## Speed and follow-up exposure

```
speed exposure per month = qualified inquiries x (30% - 23%) x contribution
```

Reunion's gap is a correlation, so present it as money at risk, not a promised gain. Example: 25 qualified inquiries a month x 0.07 x $2,500 = $4,375 a month of contribution exposed by next-day replies. 42% of inquiries arrive after hours (Reunion 2026), so the evening gap is usually the biggest part.

## Price increase check

```
break-even booking drop = raise % / (contribution margin % + raise %)
```

A 10% raise at 60% contribution margin survives a 14% drop in bookings: 0.10 / 0.70. A videographer who needs 20 weddings instead of 30 to 35 after raising (r/weddingvideography 25) shows the other side: fewer, better-paid dates free editing time. When inquiries keep coming but bookings stop after a raise (one videographer: 2 to 3 inquiries a week, 1 booking after going from $1,000 to $1,650; r/weddingvideography 32), test the presentation (price page, first reply) before rolling the price back.

## Referral partner value

A planner or venue is worth the downstream bookings they influence, not one job.

```
partner value per year = referrals sent to you x your booking rate on their referrals x contribution
```

Track every referral by partner name in both directions. A venue that sends 6 qualified couples a year at a 50% booking rate and $2,000 contribution is worth $6,000 a year: more than most marketplace subscriptions, for the cost of excellent service, fast image delivery and reciprocity.

Commission deals: one videographer paid venues 500 per wedding to be bundled into quotes as sole supplier and reportedly went from 10 to 15 weddings a year to 80 to 100 (secondhand, r/weddingvideography 16). Check: is the commission below your CAC from other sources and below the contribution of the extra bookings? Disclose commissions where local law or the venue's clients expect it.

## Cash protection

```
unearned cash = payments received for events not yet delivered
safe to spend = retainers on cancellable terms counted as earned only per contract + payments for delivered events
```

Keep unearned cash in a separate account. One videographer took $3,000 paid in full a year early; the couple cancelled and asked for a refund minus the deposit (r/weddingvideography 33). Another practitioner tracks upcoming vs completed contract money in Wave and treats only completed-event money and deposits as spendable.

## Off-season product test

```
weekday product margin = (price - direct cost) / owner hours
```

If a 3-hour courthouse package earns the same or better effective hourly rate as a full Saturday (operators report 2 to 3 hour events with strong hourly earnings and little editing, r/WeddingPhotography 203), it is a product line, not a filler. If not, it is a filler: cap how many you take and never on peak dates.
