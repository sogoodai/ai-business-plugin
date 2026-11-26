# Economics and pricing

Every formula the agent needs, with worked examples. Metal prices move weekly: recompute with the current LBMA fix before quoting any number to the owner. All metal values below use the LBMA PM fix of 9 November 2026 (gold $4,125.36/oz, silver $58.66/oz, StoneX). Pricing psychology, tiers and increase notices in general live in the `offers-pricing` skill; this file keeps what is specific to metal, stones, labor and jewelry channels.

## 1. Metal value per gram

```
pure price per gram   = spot per troy oz / 31.1035
alloy value per gram  = pure price per gram x fineness
fineness: 24k 0.999 | 18k 0.750 | 14k 0.585 | 10k 0.417 | sterling 0.925 | platinum 950 0.950
```

At the 9 November 2026 fix:

| Alloy | Contained value per gram |
|---|---|
| Pure gold | $132.63 |
| 18k | $99.48 |
| 14k | $77.59 |
| 10k | $55.31 |
| Pure silver | $1.89 |
| Sterling | $1.74 |

These are contained-metal values, not supplier prices. Casting grain, sheet, wire and chain carry a fabrication premium, and casting and finishing lose metal. Always use the owner's own supplier invoice per gram, plus a loss allowance the owner confirms (ask; do not invent one).

**Trick:** silver is about 1% of a sterling piece's price at normal handmade markups. A £75 sterling ring holds about £2.60 of silver (r/streetwearstartup, 1,523-pt thread, 59-pt reply). Never justify a silver price with "silver is expensive". Justify it with design, time and equipment. In gold the opposite holds: a 5 g 14k piece holds about $388 of gold before any work (derived from the LBMA fix), so the metal line drives the price and must be repriced as gold moves.

## 2. Unit cost build-up (handmade and small-batch)

```
metal cost      = grams x supplier price per gram x (1 + loss allowance)
unit cost       = metal cost + stones + findings and chain + packaging
                  + labor hours x hourly rate + overhead per piece
overhead/piece  = monthly fixed costs (tools, studio, software, insurance, hallmarking) / pieces per month
```

Labor hours come from a time journal, not memory. A jeweler with decades of experience and thousands of pieces found his estimates were "substantially wrong" once he logged each step (stone sorting, fabrication, engraving, setting, polishing); the featured ring took 16 hours (r/jewelrymaking, 971 pts). Make the owner log five pieces of each design before the agent sets prices.

## 3. From unit cost to wholesale and retail

The retail channel sets the structure. Boutiques and galleries expect keystone: wholesale is about 50% of MSRP (Faire wholesale guidance, 2026). So:

```
wholesale price  = unit cost / (1 - brand margin on wholesale)
MSRP             = wholesale x 2                 (keystone)
DTC price        = MSRP                          (never undercut your stockists)
wholesale-eligible = (wholesale - unit cost - wholesale selling costs) >= owner's floor
```

Decide wholesale before the design is final. A piece priced for healthy DTC margin is often structurally unable to wholesale unless the construction is simplified, the run is larger, or MSRP goes up.

### Worked example A: sterling stacking ring

Assumptions the owner supplies (example values): 3 g sterling at a supplier price of $3.00/g with 10% loss; findings and a small stone $4; packaging $2; 45 minutes labor at $30/hour; overhead $3 per piece.

```
metal       = 3 x 3.00 x 1.10                = $9.90
unit cost   = 9.90 + 4 + 2 + 22.50 + 3       = $41.40
wholesale   = 41.40 / (1 - 0.33)             = $61.79 -> $62
MSRP        = 62 x 2                         = $124 -> $125 (round to the price ladder)
```

DTC on Etsy at $125 with $5 of free shipping absorbed:

```
transaction fee 6.5% of 125            = $8.13
payment processing (about 3% + $0.25 US; verify for the shop's country) = $4.00
listing fee                            = $0.20
contribution, no Offsite Ads           = 125 - 41.40 - 5 - 12.33 = $66.27
Offsite Ads order (15% under $10k/yr)  = -$18.75  -> $47.52
```

The owner's labor is already paid inside unit cost, so these contributions are profit before fixed marketing. Price every Etsy SKU so the Offsite Ads case still clears the owner's floor (Etsy fees page, 2026: 15% under $10,000 in the last 365 days, 12% above and then mandatory, capped at $100 per order).

Wholesale on Faire for the same ring (outside North America; in North America the opening order pays 15% plus a $10 fee instead): $62 wholesale less 25% on a marketplace-originated first order = $46.50, less 15% on reorders = $52.70, 0% for boutiques the brand brings itself (Faire brand terms, 2026). The first Faire order nets $5.10 over unit cost: send every boutique the brand's own Faire link.

### Worked example B: 14k gold pendant with a sapphire

Assumptions: 5 g 14k cast at contained value plus 8% casting loss; natural sapphire $120; chain and findings $45; 3 hours labor at $60; packaging $8; overhead $20.

```
metal       = 5 x 77.59 x 1.08              = $419
unit cost   = 419 + 120 + 45 + 180 + 8 + 20 = $792
DTC price at 55% gross margin = 792 / 0.45  = $1,760
```

**Replacement-cost check.** If gold rises 10%, the metal line becomes $461 and unit cost $834: the same $1,760 now earns 52.6%. Set a reprice trigger, for example "reprice when replacement-cost margin falls 3 points below target", and store both historical cost and replacement cost per SKU.

**Metal surcharge method** (for catalogs too large to retag): publish a base price at a reference gold price and add a metal adjustment.

```
price = base price + grams x fineness x (current pure price per gram - reference pure price per gram) x metal multiplier
```

The owner chooses the multiplier (often the same multiplier used on materials). Show the formula on custom quotes so customers see that the price follows the market, not the maker's mood.

## 4. Repricing discipline when metal moves

- **Reprice in steps, not in one catch-up jump.** A store skipped adjustments at gold reference levels of $2,200, $2,400 and $2,800, then had to jump from a $2,400 basis to $4,400 at once (r/jewelers, 121-pt thread; a 7-pt reply reports the same pattern elsewhere).
- **Website prices go stale first.** One jeweler needs about 3 full days to retag web prices by hand; when online gold sales suddenly accelerated, the likely cause was underpriced listings (r/jewelers, 97-pt thread). Agent rule: if gold moved more than the trigger since the last web price update, freeze paid promotion of gold SKUs until they are repriced.
- **Split the range instead of pricing everyone out.** A jeweler since 2000 replaced low-four-figure midrange pieces with two tiers: sub-$500 sterling production pieces with rhodolite, amethyst or peridot (some redesigned with less metal to reach about $350), and low-to-mid five-figure custom gold work. It carried the business through 2008 and the 2011 metal spike (r/jewelers, 83 pts, 17-pt agreement). One studio reports 80% of its work is now silver because customers prefer the price point (r/jewelers, 11 pts; 44-pt supporting reply).
- **Add repairs and trade-in credit when metal is high.** Repair demand rises when replacement gets expensive (r/jewelers, 19 pts). Offer credit for customers' unwanted gold against custom work: one customer was bringing 7 g of 18k earrings to avoid buying that gold again (r/jewelers, 7 pts; customer's account).

## 5. Channel contribution and break-even ROAS

```
contribution / order = net revenue - unit cost - pick, pack and shipping paid - payment fees
                       - marketplace fees - affiliate or creator commission - return reserve
return reserve       = return rate x (refund + return shipping - resale value of returned item)
break-even ROAS      = order value / contribution per order
allowable CAC        = contribution per order - owner's target profit per order
target ROAS          = order value / allowable CAC
```

### Worked example C: demi-fine necklace on Meta

$68 AOV, landed COGS $14, pick, pack and shipping $6, payment fees $2, 8% return rate with a $50 net loss per return (outbound shipping, return label, re-plating) = $4 reserve.

```
contribution     = 68 - 14 - 6 - 2 - 4 = $42
break-even ROAS  = 68 / 42             = 1.62
target profit $10 -> allowable CAC $32 -> target ROAS 2.13
```

Compare: apparel and accessories Meta median CPA $36.98 (Triple Whale, Aug 2025 to Jul 2026). At that CPA this necklace loses money on the first order. The fixes, in order: raise AOV (matching earrings, a second chain, gift box), cut return loss with scale photos, then buy traffic.

## 6. Wholesale, consignment and Faire compared

$120 MSRP sterling piece, unit cost $40:

| Route | Brand receives | When | Risk |
|---|---|---|---|
| Wholesale, brand's own account | $60 | Prepaid or on agreed terms | Low |
| Faire, retailer brought by brand | $60 | Faire terms | Low |
| Faire, marketplace first order | $45 | Faire terms | Low; $5 over cost |
| Faire, reorder | $51 | Faire terms | Low |
| Consignment 60/40 | $72 | Monthly, after it sells | Stock tied up, tarnish, damage, shop not displaying it |
| Consignment 50/50 | $60 | After it sells | Wholesale money with consignment risk: refuse |

Rule from a long-time jewelry consignor: 60/40 (artist/shop) is the most common split, 80/20 is rare, and at 50/50 the shop should buy at wholesale instead (Jewelry Making Journal, undated, possibly outdated). Galleries commonly cite 25% to 50% commission and 60 to 90 day display periods (Jewelers Mutual, pre-2024, possibly outdated). Treat these as negotiating anchors, not 2026 benchmarks.

## 7. Permanent jewelry per-hour economics

```
event gross       = booked appointments x show rate x average ticket + walk-ins x average ticket
                    + charm attach rate x charms sold x charm price
event costs       = chain inches x cost per inch + charm materials + card fees + host share or flat fee
                    + travel + argon and consumables
contribution/hour = (event gross - event costs) / (event hours + setup + teardown + travel hours)
```

### Worked example D: 4-hour boutique pop-up, new artist

Throughput 2 to 3 per hour for a new artist (The Maker's Chest, 2026, vendor blog): plan 10 appointments at $75, charm attach 30% at $30.

```
gross        = 10 x 75 + 3 x 30                         = $840
chain        = 10 x 7.5 in x $0.20 (gold-filled)        = $15
charms       = 3 x $4                                   = $12
card fees    = 2.9% x 840                               = $24
host share   = 15% x 840                                = $126
travel       = $30
contribution = 840 - 207                                = $633
per hour     = 633 / 6 hours (incl. 1 h setup, 1 h teardown and travel) = $105
```

Gold-filled chain wholesale runs about $0.15 to $0.25 per inch and solid 14k $1.50 to $4.00+ per inch (vendor blogs, 2026). Material is small; throughput and host terms decide profit. A private bachelorette of 8 at $72.50 = $580 for about 2.5 hours with no host share beats most public pop-ups. Compare every event with the owner's floor per hour before accepting. Sunstone's "up to $300/hour gross at busy events" is equipment-vendor promotion, not a benchmark.

Welders from major brands start at $999; Sunstone estimates payback after 50 to 70 bracelets (Sunstone blog, March 2024).

## 8. Custom and commission math

```
custom quote = metal (current price, surcharge method) + stones + CAD or design hours x design rate
               + bench hours x bench rate + casting and setting outsourced + overhead + insurance and shipping
deposit      >= metal + stones + design hours already spent            (non-refundable once work starts)
```

- **Set a custom minimum.** One jeweler stopped taking customs under $250 after repeated loss-making discounted jobs; their customs now run $1,500 to $3,000 and clients have voluntarily paid more, including $1,000 to $1,400 for an 80-hour piece (r/jewelers, 4 pts on a 13-pt thread).
- **Quote friends the full price and itemize materials.** A $200 quote for a 40-inch hand-knotted necklace with $60 of beads and 7 hours of labor collapsed when the friend arrived with $60 expecting free labor (r/jewelers, 44 pts; replies with 24 and 10 pts said $200 was already too low).
- **Insurance and signature are part of the price** on any piece above the platform's seller protection. Build it in; never let the buyer opt out (section on shipping risk in [custom-and-bridal.md](custom-and-bridal.md)).

## 9. Price ladders and tier moves

- **Ladder up while it sells.** An eBay jewelry seller launched at $5.99 and raised to $6.99, $7.49, $7.79 and $7.99 after each 10 sales to earn Best Match position first (r/Entrepreneur, 1,108 pts). A knife maker kept raising until he reached several hundred dollars and buyers still bought (r/Entrepreneur, 1,462 pts).
- **Add a fine tier above a $20 to $60 range.** One owner says $20 to $60 transactions did not build the business fast enough and recommends genuinely valuable pieces at a few hundred dollars (r/smallbusiness, 5 pts on a 242-pt thread). A secondhand report: a fine brand's pieces under $3,000 sat while $10,000 to $30,000 pieces sold (r/jewelers, 6 pts). Check the owner's own sell-through by price band before moving.
- **Separate quality tiers clearly.** Sterling findings and Swarovski crystals in an intricate higher tier, simpler pieces in a lower tier, so one listing does not carry two expectations (r/EtsySellers, 566-pt thread).
- **Low-ticket labor kills.** An origami rose at $12 took almost an hour to make and pack with seller-paid shipping; after 93 orders and about $1,000 the maker concluded it did not pay (r/EtsySellers, 661 pts). Time every SKU and drop the ones that cannot pay the owner (r/EtsySellers, 311 pts).
