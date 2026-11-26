# Delivery apps, reservations and direct ordering

Marketplaces are a paid discovery channel. Reservation and phone platforms can quietly become a tax on demand you created. Use them deliberately, measure contribution, and move repeat guests to channels you own. Fee table: [benchmarks.md](benchmarks.md). Math: [economics.md](economics.md).

## 1. Decide whether and how to list

- **List for discovery and weather, not for your regulars.** A college-town owner chose DoorDash's 25% tier (with DashPass, without the wider radius) to reach transient students and fill cold, wet days, pricing so proceeds after commission match the cash price (operators report). A ghost kitchen has no choice; a destination restaurant may not need apps at all.
- **Pick the tier by test, not by pitch.** A 30% plan must bring enough extra orders and visibility to beat a 15 to 20% plan. Run comparable weeks on each tier, or pause in-app promotion for a period, and compare incremental orders, net contribution and the effect on direct sales (research report 2026).
- **Negotiate the onboarding.** DoorDash offered one restaurant that was "highly searched" in the app a 3-month contract, cancel any time, its existing local delivery charge, and a $20,000 bonus after 3 months (reported offer, operators report). Ask before signing.
- **Pickup on apps is cheap** (6 to 7%) but carries price-parity conditions. Use it when the app sends pickup guests you would not otherwise see.
- **Outside the US** (Deliveroo, Just Eat, Uber Eats UK and EU) commissions are negotiated. Read the actual contract before modeling.

## 2. Price the app menu

- Compute the markup that keeps proceeds equal: in-store price / (1 - commission). 25% needs +33%. A 10% markup on a 25% plan dropped one owner's margin from 40% to 15%; another raised Uber Eats prices 15% and still did over $1M a year there at its largest store (operators report).
- **Bundle markup is easier to swallow than item markup.** A $100 in-store family meal listed at $150 with "call the store for a 50 dollar discount" in the description still sells (operators report).
- **Build a delivery menu, not the dine-in menu:** items that travel, fewer modifiers, photos on every item, packaging cost in the price.
- **Check the terms** before marking up or adding inserts; parity clauses differ by product and country.

## 3. Platform hygiene (monthly)

- **Payout audit:** look for "marketing fees" in transaction details, then Marketing > Campaigns. One owner found "$0 delivery fee" and "Sponsored Listing" campaigns they said they never approved (operators report).
- **Promo ROAS is not profit.** Recompute any in-app ad or promo after commission, fees, food and packaging. A "2.13 ROAS" left one operator owing Uber money.
- **Promo-only buyers:** check whether names that order during promos ever come back at full price or order direct. One operator saw the same names vanish when promos ended; another saw app guests become in-person regulars. Measure your own.
- **Unauthorized listings:** search Uber Eats, DoorDash and Grubhub for your name even if you never signed up. One restaurant found a listing with an abbreviated menu 20% below its prices, taking orders it could not receive; support removed it in two hours after a firm call (operators report).
- **Listing audit** (ai-restaurant-claude, MIT): per platform, hours match Google, menu completeness, photo coverage, markup %, star rating, reply rate to app reviews.
- **Fake copies of you:** check misspellings of your domain and local "foodie" accounts using your logo with invented specials. Operators found both and had them removed.

## 4. Move guests to direct ordering

Give the direct channel a legitimate reason to exist, then make it as easy as the app.

**Reasons that work:**

- **A concrete first-order incentive redeemable only direct:** "$10 off, no minimum" on the restaurant's app, followed by points toward free meals; the guest who reported it now orders only there. The parent advice, website-only coupons in carryout bags, got 467 upvotes (operators report).
- **Direct-only items or bundles,** loyalty earning, easier reorder, pickup speed, catering and gift cards.
- What failed: three months of QR flyers in every Uber Eats bag saying "skip the fees, order direct and save" with no concrete amount, almost zero switched (operators report).

**Friction that kills it:**

- Saved details and one-tap reorder. A guest spent 10 to 15 minutes on a pizza site because details were re-entered and timeouts emptied the basket; walking in took 10 seconds (a 185-upvote customer comment stressed saved details and easy reordering).
- Final total: guests found direct delivery more expensive than Uber Eats at three restaurants despite lower menu prices, once delivery and service fees were added. Compare checkout totals for the same basket before claiming savings.
- Coverage: a flyer promised cheaper direct delivery to a guest outside the direct delivery radius. Pickup-only direct ordering was another stated barrier (67 upvotes).
- Broken coupons: a printed $10 coupon failed at checkout. Test every code end to end before it goes in a bag.

**Google is the switch point:** set the direct link as the preferred ordering option on the Business Profile and check where each order button really leads. A 108-upvote customer said they always pick the direct site when it is marked preferred; others land on Uber Eats by mistake.

**Direct-order delivery options:** Uber Direct (from $7.99 a delivery) or DoorDash Drive fulfill your own orders without marketplace commission; restaurants also pass a $7 to $8 driver charge to the guest through Toast (operators report). Model who pays the delivery cost before advertising free delivery.

**Insert wording** (direct offer only, never tied to a review): see [scripts.md](scripts.md).

**Software choice:** compute the break-even volume for each option ($499 flat / (25% - 3%) = $2,268 a month) and check the guest-facing fees (Owner.com charges the guest 5%). Commission-free POS ordering (Toast, Square) is often enough for a single location.

## 5. Reservations and phone orders

- **OpenTable:** operators report a $1 fee per cover for bookings referred through Google, including Maps, on traffic they believed their own SEO and brand created. One agreement named Google referrals explicitly and reported Google as a source; another said only "the opentable network". Read your agreement and reports. Ask for a promotional reduction when it expires ("you're going to have to switch to Resy if you can't get your bill down") and ask again at expiry (operators report).
- **Alternatives:** Toast Tables cost one operator the same monthly price as OpenTable with no per-booking charges and POS integration; Tock let another sell private rooms and table-minimum options online and lifted direct event bookings (operators report).
- **Google reservation link:** pick the provider that charges least for Google-sourced covers as the preferred reservation link. In the UK, Google's AI Mode books through TheFork, SevenRooms, ResDiary, OpenTable and others (Google, April 2026); check which integrations exist in the owner's country.
- **AI phone services on revenue share:** audit missed calls before paying a percentage of every order. One pizza owner found 4 missed calls in a week, all while closed, against a pitch of "hundreds" and a 4.85% fee. Require integration with the POS's live prep times; a fixed pickup time on a Friday rush sends guests to wait for food not ready (operators report).
- **Cap online orders by slot when quality suffers:** two orders per 15-minute slot kept one takeaway's food right during rushes (operators report).
- **Call to confirm anomalous online orders** (four large pizzas all with only double pineapple). The one skipped during a rush cost four replacement pizzas.
