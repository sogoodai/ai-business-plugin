# Wholesale, consignment, galleries, markets and trade shows

The reorder engine (Faire reorder timing, account lists from Google Maps, big-retail terms, MAP) is in `ecommerce-brand` (wholesale.md). Craft fair operations in general are in `art-handmade`; a physical shop's own events in `local-retail`. This file keeps the jewelry decisions: which SKUs can wholesale, consignment terms, galleries, trunk shows, jewelry markets and trade shows.

## Decide wholesale at SKU level

Create a `wholesale_eligible` flag per SKU. A SKU is eligible only when:

```
wholesale price (= MSRP / 2) - unit cost - samples, freight and commissions per unit >= owner's floor
```

Most handmade lines need a separate wholesale edit: simpler construction, lighter metal, larger runs, or a higher MSRP. Do not offer the whole DTC catalog to boutiques. Gold SKUs need a metal clause (price valid for 30 days or tied to a reference gold price) or they will be underwater by the reorder.

## The buyer edit and line sheet

Buyers want six strong sellers, not the archive. The line sheet holds, per SKU: photo, SKU code, wholesale, MSRP, metal and fineness, stone and origin, lengths and sizes, lead time, opening minimum, reorder minimum, case pack if any, ship-from location, defect and repair terms. One page for first contact; full catalog only on request.

Add a shelf kit with the first order: a display card with the materials and care line, a one-line staff pitch, three on-body photos for the shop's social posts.

## Terms that protect a small maker

- **Prepaid first order from new accounts.** A candle maker declined a boutique chain order that would have tripled revenue because it came with custom labels, net 60 and 30-day returns of unsold stock; she offered a smaller prepaid trial instead (r/smallbusiness, 934 pts). Jewelry has the same exposure, plus tarnish on returned stock.
- **Faire:** outside North America 25% on a marketplace-originated first order, 15% after; in North America 15% plus a $10 new-customer fee on opening orders; 0% on retailers you bring (Faire brand terms 2026). Send boutiques you recruit your own Faire link. Keep MSRP consistent across Faire and your site (Faire pricing policy).
- **Deposits fund big orders.** Take a deposit that covers metal and findings before you buy them.
- **Pitch around the retailer's problem.** A jewelry-care seller opened with "If I had a way for you to give out less discounts would you be interested in hearing me out?", demonstrated the cleaner, walked through a $3,000 sale negotiation, then quoted $5 a kit with a 50-kit minimum (r/Entrepreneur, 1,237 pts). The kit cost about $2.50 (30 ml cleaner, microfiber cloth, bag, label); the manager countered at $3. Lead with the store's margin or sell-through, never with your story.

## Consignment

Use it to enter a shop that will not buy yet, then convert to wholesale.

- **Split:** 60/40 artist/shop is the most common; 80/20 is rare; refuse 50/50 and ask the shop to buy at wholesale instead, because consignment adds risk, paperwork and slow monthly payment (Jewelry Making Journal, undated, possibly outdated). One long-time consignor holds a 60/40 floor and has one shop at 70/30.
- **Galleries:** commonly 25% to 50% commission with 60 to 90 day display periods (Jewelers Mutual, pre-2024, possibly outdated). Treat as negotiating anchors.
- **Never consign on a handshake.** The agreement covers title (stays with the maker until paid), theft, loss and damage while on premises, insurance, markdown authority (none without written consent), payout timing and statements, monthly inventory reconciliation, display requirements, return shipping and condition on return, and termination notice. Template in [scripts.md](scripts.md).
- **Check that the stock is on the floor.** A maker's shop reported zero sales after a month; a friend had bought one there, and the maker found the products had never been put out. The recovered stock sold out at a grocery-store table later (r/Entrepreneur, 1,115 pts).
- **Inventory count in photos** at drop-off and at each reconciliation. Tarnished or damaged returns may be unsellable.
- **Cafes and apparel shops count.** A maker celebrated consignment placement in a local cafe and an apparel shop (r/jewelrymaking, 1,034 pts). Non-jewelry shops have no competing jewelry case.

## Galleries and museum shops

- Pitch a coherent collection with a story and price range, not single pieces.
- Gallery wholesale variant: one Etsy maker sold to galleries for years at 30% off retail with a $500 minimum (r/EtsySellers, cited in `ecommerce-brand`).
- Ask for the commission in writing, how long pieces stay, who pays shipping both ways, and whether the gallery insures work on its premises.

## Trunk shows and in-store events

- Typical shop commission on a jewelry trunk show: 20% to 25% of sales; some shop owners prefer a piece or a donation to their cause (Jewelry Making Journal forum, undated).
- Ask the host for promotion commitments in writing: email to their list, two social posts, in-store signage two weeks ahead.
- Capture every visitor's contact with consent (custom order waitlist, birthstone reminder).
- Permanent jewelry pop-ups: [permanent-jewelry.md](permanent-jewelry.md).

## Markets, fairs and cons

- **Expect 3x to 5x the booth fee in sales; 10x is a strong show.** Bring 2x to 3x the stock you expect to sell (fair guides and forums, anecdotal).
- **Choose spending crowds and price points:** Comic Cons and fairs where attendees arrive to spend suit a $60 range (r/smallbusiness, 5 pts).
- **Check sightlines before paying.** One maker's third allocation was a narrow lane behind two vendors, facing a pillar, beside an aggressive perfume sampler that made shoppers reroute (r/jewelrymaking, 486 pts).
- **Crystal and gemstone booths:** keep a stone-meaning guide that shoppers can leaf through themselves, and phrase beliefs as history: "some people believe that this stone is good for..." or "it's been said that in the past this stone was used for..." (r/jewelrymaking, 516 pts; 238 pts for the self-serve guide).
- **Turn browsers into buyers in the booth:** a mirror, ring sizers, and a "try it on" invitation; payment by card; a QR to the custom-order form.
- **Test a table where people already buy handmade:** a sugar scrub maker sold almost everything at a specialty grocery's sampling table by greeting every shopper, then booked every Saturday (r/Entrepreneur, 1,115 pts).

## Trade shows

- Judge a show on 12-month account contribution, not orders written at the booth. Track pre-booked appointments, qualified buyers scanned, opening orders, 90-day reorders and 12-month gross contribution.
- Build the target-account list before buying space, and book meetings beforehand: pre-booked buyer meetings are a better KPI than badge scans.
- Emerging-designer programs reduce the cost of entry (NY NOW's emerging fine jewelry incubator, now CURATED at Luxury Lifestyle, required fewer than 5 years in business in 2025). Booth prices are not published (Shoppe Object discloses pricing only after jury acceptance). No defensible 2026 trade-show ROI benchmark exists: do not invent one.

## Other B2B routes

- **Marketplace supplier programs:** a US sterling jewelry maker found a Wish recruiter hiring US dropship suppliers on LinkedIn, had a call two hours later, and reports about $30,000 a month for a year (r/ecommerce, 90 pts; dated). Look for marketplace or retailer recruiters whose mandate matches your fulfillment.
- **B2B dropship from stranded stock:** an accessories brand with $1M of inventory offered competitors dropshipping at 50% off retail through a quick landing page and became the category's main dropship supplier (r/Entrepreneur, 1,532 pts).
- **Corporate and group orders:** engraved pieces for teams, sororities and clubs use the same tiered package idea trophy makers use (four preset tiers, r/smallbusiness, 926-pt thread).
- **Repeat Etsy resellers:** when someone keeps clearing out the shop to resell, make a custom wholesale listing for them and raise public prices.
