# Pricing, minimum stays, fees and rate tactics

Score every pricing change on RevPAR, net payout and pickup pace, not occupancy. Formulas in [economics.md](economics.md). General price psychology lives in `offers-pricing`. Sources in [sources.md](sources.md).

## Step 1: fix the base

1. Reprice Airbnb for the 15.5% host-only fee: old payout / 0.845. Apply it to cleaning and extra-guest fees too.
2. Build the comp set: 10 to 20 listings with the same sleeps, bedrooms, key amenity and location band. Remove non-comparables from Vrbo's comp set before trusting its metrics.
3. Price five date patterns against comps on guest total: midweek near-term, weekend near-term, weekend 30 to 60 days out, an event date, peak season.
4. Load the next 12 months of seasonal rates and holiday minimums before those dates enter the booking window. Vrbo reopened dates at a $99 winter rate for a June oceanfront request; an Airbnb villa sold at £48.52 a night against an intended £220 (r/AirBnB 458).

## Step 2: dynamic pricing with rules

Evidence: Wheelhouse's A/B test of 1,000+ live listings (2026) gave +7.49% RevPAR with ADR nearly flat, so the gain came from capturing demand. Beyond's switching data (2026) shows about a third of accounts flat or down. Treat the tool as an engine you configure, not an answer.

Configure:

- **Base and minimum price** from your own costs and history, never the tool's default. In a soft market the tool may go very low: Beyond would have priced a South Florida 4-bed under $200 (r/airbnb_hosts 640). Set the floor at the price where a stay still beats an empty night after cleaning and wear.
- **Weekday and weekend spread, events, last-minute floor.**
- **Far-out minimum stays** on peak weekends and event windows, loosened as arrival approaches; **gap minimums** equal to the gap; check-in and check-out day rules; adjacent-day rules to stop one-night remainders (PriceLabs 2026). Short stays booked far ahead create orphans that cannot be repaired later.
- **Audit the output.** After connecting, check 10 random dates for minimum stay, price and availability on every channel. A rogue sync set 90 to 135-night minimums for two years and bookings stopped (r/airbnb_hosts 1,416).
- **Check stacked discounts.** Smart Pricing gap cuts plus a 10% non-refundable discount produced a booking "barely worth hosting" (r/airbnb_hosts 1,005). Know which discounts are on in each channel; Vrbo auto-enabled some in 2025 (r/vrbo 643).
- **Measure against a control:** the same months last year adjusted for market pace, or a sister listing left on manual. Keep the tool only if RevPAR beats the control after 8 to 12 weeks.

## Minimum stays and gaps

| Window | Rule |
|---|---|
| 60+ days out, peak and events | Longer minimums (PriceLabs' London case used longer minimums 60+ days out and Thursday to Sunday constraints) |
| 14 to 60 days | Loosen if pickup trails the market |
| Under 14 days | Minimum drops to fit remaining gaps |
| Orphan gap | Minimum equals gap length; price only those nights |

Screen gap requests. A host who opened one-night gaps after a call from a self-described Airbnb manager got a local "sister and three children" booking that became a 30+ person party: $598 emergency cleaning, $750 sofa bed (r/airbnb_hosts 1,690). Operator rules: no same-day local one-nighters, 2-day advance notice (an ex-OTA worker said most incidents were same-day bookings), read the guest's written reviews, not just the rating (a 4.5+ guest's reviews described destroyed property, r/airbnb_hosts 1,060).

Business-model choice (both work, the cost structure decides):

- Short-stay model: 3-night maximum, about 95% occupancy, per-stay fee, host cleans (r/airbnb_hosts 434).
- Mid-term model: 25-night minimum across Airbnb and two mid-term platforms, fully booked, fewer turnover costs (r/airbnb_hosts 288, 2026).
- Spread fixed fees: a 3-night minimum because cleaning costs the same for 1 night as for 5 (19 upvotes).

## Events and peak dates

- Block the month around an unannounced festival until dates are public, then price and open (68 upvotes; a Comic-Con host was booked within minutes at normal rates three years running).
- A host who set a peak weekend at about $500 instead of $1,050 asked the guest to accept $750 two days later; the guest refused and the host honored it (r/AirBnB 357). Price first, open second.
- Honor mistakes. A host who cancelled an underpriced Super Bowl stay drew a 1-star review, and Airbnb rehoused the guest at the original rate (r/vrbo 897 thread). Hosts who forgot to update rates and honored them were upvoted (36 and 23).

## Cleaning fees and fee stack

- Compute fee load for the most common stay ([economics.md](economics.md)). Airbnb ranks total price.
- Options: fold into the rate (short-stay markets), low fixed fee per booking (long stays; one host charges $10 from 1 night to 3 months), or drop it.
- Operator case: $200+ fee dropped, nothing else changed at first, from about one weekend a month to every weekend for six weeks and bookings into the slow summer (r/AirBnB 218, 2024). Another host with no cleaning fee reports a 5.0 rating and being booked out (r/AirBnB 492, 2026). Uncontrolled, but consistent with guest complaints.
- A fee is a promise: "You paid a cleaning fee" justifies a no-chores checkout. A big fee plus a chore list is the most-cited reason guests say they now book hotels.

## Guest count, groups, parties

- Big home in a thin market: rate for 2 to 3 guests plus extra-guest fee, visible in the search quote (r/airbnb_hosts 589).
- Advertise sleeps and included occupancy that match the quote. Raising a quote from $3,300 to $3,800 for a short stay, then asking $450 more when the group grew to the advertised 12, ended in a credit-card dispute threat (r/vrbo 412).
- Parties as a product: whole house only, about 10% premium, the next day blocked for cleaning. Close the loophole of booking every unit separately (r/airbnb_hosts 473).
- Hotels: a larger, higher-occupancy room sat among the least used; about half of guests who needed it balked at a $20 premium (r/hotels, 7 upvotes). Validate demand before building premium room types.

## Long stays, work and production

- Do not auto-discount work and production stays. A film company paid full price (257 upvotes); a six-week booking paid $20,000.
- Ask production inquiries whether they need lodging, a filming location or a production office. Locations belong on Peerspace-type platforms at commercial rates (22-upvote advice on clarifying occupants, cleaning and use).
- Mid-term demand (corporate, insurance, relocation) is in [partnerships.md](partnerships.md).

## Discounts and offers

- Launch or slow-month discounts belong on specific dates, not the whole calendar.
- Weekly guest checks: a hotel offers unadvertised weekly rates to callers who reach the manager in the daytime; weekly guests need less housekeeping (r/hotels, 22 upvotes).
- Evacuation or crisis discounts go in the listing with reasonable proof required, not in a community subreddit (a host was banned from r/pasadena for it, r/vrbo 277).
- Badges do not create price ceilings. A Dubai host with 2 Gold Guest Favorite units at 95% occupancy found any increase stopped bookings after 20,000 new listings arrived in a year (r/airbnb_hosts 291, 2026). Raise in small steps and watch pace for 2 weeks per step.

## Hotel and B&B rate tactics

- **Rate match at the desk.** A caller ready to book direct asked to match a third-party rate $30 lower and was refused; they booked the OTA and stopped asking hotels (r/hotels 2,299). Give staff a rule: match a verified, bookable OTA rate for the same room and terms when inventory is open.
- **Make the direct rate visible and true.** Guests report hotel sites priced above the OTA and above Google's displayed direct rate (147 and 12 upvotes). Show the member or direct rate on the home page, not in an offers tab (a guest would have booked all nights direct had the promo been on the home page, r/hotels 55).
- **Watch refundable rebookers.** A guest booked at $350, saw $270 two weeks out, rebooked and cancelled (r/hotels 1,567 thread). Late price cuts leak revenue from refundable reservations; prefer targeted offers to public cuts close in.
- **Make cancellation fees unambiguous:** say whether the fee applies before the cutoff as well as after (a work-trip team argued over it).
- **Pre-arrival paid upgrade emails:** a luxury property offered a suite at $150 extra a night against a normal gap near $1,000 (r/hotels 309). Price upgrades as a fraction of the rack gap; sell them before arrival.
- **Oversold nights:** a former worker sold a suite's parlor separately at a discount, disclosing the pull-out bed (9 upvotes); guests who get a downgraded room are contacted proactively, moved the next day, and comped dinner, breakfast or valet (52 upvotes).
- **Corporate clients on OTAs.** A receptionist spotted a returning company booking through Booking.com at 50% above its corporate rate and called them; it saved the client about 10k and the hotel the commission. A 29-upvote reply warned OTAs may audit and still charge commission. Do it only where the contract allows.
- **EEA:** parity clauses are gone at Booking.com (July 2024). Elsewhere, read each OTA contract before pricing direct below OTA.

Tricks most owners miss: tighten far-out minimums before discounting peak dates; the cheapest fix for a weak month is often removing a fee or a stale minimum, not cutting the rate; and refundable discounts that raise cancellations can lower Booking.com rank because it ranks on net bookings.
