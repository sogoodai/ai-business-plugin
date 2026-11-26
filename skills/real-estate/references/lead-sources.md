# Lead source economics

The industry's most common analytical error is using cost per lead as if it were cost per client. Public data is good on clicks and leads and weak on closings: no independent 2025 to 2026 dataset gives cost per closing for sphere, Zillow, Realtor.com, Redfin, Google, Meta, open houses, expireds, FSBOs and farming side by side (research synthesis, 2026). So the agent's job is to compute the owner's own numbers and use public data only as sanity checks.

## The math

```
GCI per closing = price x commission rate
net per closing = GCI - portal referral fee - brokerage split - team split - transaction fees
   (order matters: a fee "off the top" and a split "off the remainder" are different; read the contracts)
cost per closing (source) = (spend + referral fees + data/dialer cost) / closings (12-month cohort)
allowable cost per lead = net per closing x lead-to-close rate (12+ months, same source)
allowable cost per connection = net per closing x connection-to-close rate          (Zillow PA)
referral-fee equivalent = fee% x GCI   (compare with upfront cost per closing)
payback months = cost per closing / (net per closing / months from lead to close)
```

Worked example, Zillow at Zillow's own 10% Flex target: $223 per connection x 10 = $2,230 of connection cost per closing in a major metro, $1,390 elsewhere, before splits and labor (derived, not Zillow's published CPA). On a $400,000 sale at 2.5% (GCI $10,000), a 40% Flex fee costs $4,000 per closing. If the agent then splits 50% with a team and pays a $250 admin fee, take-home is $2,750 before the brokerage split. One agent reported a 40% Zillow fee, 50% team split and $250 admin fee left "5%"; the order was not stated and the figure does not reconcile, so compute it yourself before accepting team leads (r/realtors 288, 2024).

Long-cycle rule: never judge a source before the nurture window closes. Operators report the first-month closing rate roughly doubling or tripling after 6 months of drip (1 per 30 leads in month one, plus 1 or 2 more by month six; r/realtors 1200, 2021).

## Source table

| Source | Cost basis | Conversion data available | Typical cost per closing | Notes |
|---|---|---|---|---|
| Sphere and past clients | time, gifts, events, mail | share of first contacts (Zillow 2026) | lowest when systematized; no public figure | 81% of seller-buyers reuse the agent (Zillow 2026) |
| Agent-to-agent referrals | 25 to 35% referral fee | none public | fee x GCI | 25% reported on two out-of-province purchases (r/realtors 337, 2024) |
| Zillow Premier Agent | $139 to $223 per connection (2026) | Zillow target 10% connection to close | $1,390 to $2,230 at target, derived | 6-month minimum suggested by Zillow; share of voice by ZIP |
| Zillow Flex | 40% seller side; buyer side varies | none public | 40% of GCI | Zillow can change the fee on 15 days' notice |
| Realtor.com ReadyConnect | pay at close | 2019 claim only | contract | screens timeframe and live-transfers |
| Opcity (Realtor.com referral model) | 33 to 38% at close (2024 third party); 35% reported | | 33 to 38% of GCI | heavy app reporting and hard exit reported (r/realtors 1200, 2021) |
| Redfin Partner | referral fee at close | Redfin ranks partners on local close rate | fee schedule (30% reported, r/realtors 1200, 2021) | fee changes on 30 days' notice |
| Google Search | CPC | 1.29% click to lead, $157.59 CPL (LocaliQ 2026) | unknown; no closings from Google in 2 years for one agent (r/realtors 1200, 2021) | seller and PM intent best |
| Meta lead forms | CPL | $13.74 CPL (WordStream 2026) | $4,000 spend for a $2,000 commission (BoldLeads, r/realtors 1200, 2021) vs 1 to 2 deals a month (r/realtors 1025, 2020) | qualify, chatbot, long nurture |
| Open houses | time, signs | 6% of buyers met agent there (Zillow 2026) | time only | listing agent's or a teammate's listing |
| Expireds and FSBOs | data list, dialer | population stats only (REDX 2026) | 1 to 2 listings a month reported (WA) | DNC rules apply, see compliance |
| Farm and EDDM | $0.26 a piece + print | mail 1 to 2% first contact (Zillow 2026) | 6 to 8 listings a year from one farm reported | 18 months minimum |

## Portals: what actually moves the economics

- **Portals reward operational behavior.** Redfin requires 5-minute average connection, 55% acceptance, 80% customer list compliance and at-or-above local close rates, or it pauses or removes you (Redfin 2025). Zillow tells Flex teams not to overload agents. A team that buys fewer leads with deterministic routing beats one that buys more.
- **Shop ZIPs yourself.** Sales reps push expensive areas. One agent found rural Washington ZIPs at $1 to $10 a month for most of the share, and California ZIPs at about $100 a lead where most were $250. Add small ZIPs Realtor.com does not sell to your profile for free leads (r/realtors 1200, 2021). Many of those buyers purchase elsewhere, so track where they buy.
- **Check program favoritism before renewing.** One office saw Premier leads worsen after Flex launched and cancelled Premier after a Flex team lead said Flex teams got better leads; unverified claim (r/realtors 351, 2024). Compare connection-to-appointment by program, not by gut.
- **Use referral-fee leads to keep leverage busy.** A team routed 30% split Redfin leads to its showing agent between better leads, in a market with about $10,000 average commission (r/realtors 1200, 2021).
- **Answer with the right channel.** Zillow and Opcity call you live (often at bad moments); Realtor.com used to text the consumer first so the agent replied at once (r/realtors 1200, 2021). Make the system send the first text and route the callback.
- **Ask "Are you already working with an agent?" on the first call.** One agent drove halfway through an hour-long Sunday trip before learning the Zillow lead was represented (r/realtors 305, 2024).
- **Portal power is shifting.** NWMLS's settlement with Compass forces portals showing its data to display the listing agent's name and contact prominently; a sample of 400 Zillow listings across 80+ MLSs found this in only four MLSs (NWMLS, CRMLS, MARIS, PrimeMLS) (r/realtors 121, 2026, citing Mike DelPrete). Listing agents in those MLSs get more direct buyer calls from their own listings: answer them like paid leads.

## Expireds

- **The channel is crowded.** One cancelled listing triggered 30 to 50 calls a day for a week (r/realtors 230, 2026); another seller got eight agents calling before noon and one calling her 72-year-old father (r/RealEstate 1003, 2024). Cold dialing the same list as everyone else is the weakest version.
- **DNC applies.** The FCC declined to exempt expired listings; you may not call a registered number to solicit a listing without an exemption ([NAR](https://www.nar.realtor/telemarketing-cold-calling)). The previous listing broker's firm has an established business relationship for up to 18 months (state association summary; verify).
- **Differentiate with a diagnosis.** Before any contact, pull the listing history: list price vs closed comps, days on market vs area average, photo count and quality, floor plan present, number of reductions, showing count if visible, MLS and portal errors. Deliver it as a one-page "why it didn't sell" by mail or at the door. Common culprits: priced over a search ceiling (a $420,069 list price drops out of $420,000 filters, r/RealEstate 3022, 2023), listed in the wrong MLS for weeks (r/RealEstate 915, 2025), showing requests going to the seller's spam folder (12 missed, r/RealEstate 799, 2025), missing garage photos (r/RealEstate 894, 2021), missing condo budget and HOA documents (r/RealEstate 1389, 2025).
- **Expireds in a slow market are also rental prospects.** Accidental landlords who cannot sell often rent instead; refer them to a property manager or pitch management yourself (r/PropertyManagement 59, 2026).
- **Score, do not forecast.** `probability the property needs an agent x contactability x your differentiation x observed contact-to-appointment` (research synthesis). The 44.4% relist rate is what happened to the population, not your conversion.

## FSBOs

- **Small and mostly pre-sold.** FSBO was 5% of 2026 sales and 62% of FSBO sellers knew the buyer (NAR 2026). Most FSBOs do not need a listing; some need a contract and a closing.
- **Offer what they lack.** A limited-service or contract-only package where state law and the broker allow it (one agent charges $750 for the contract only and rebates excess compensation, secondhand report, r/RealEstate 2386, 2024). Fraud screening is a real value: a Missouri couple used fake bank statements and fake wire confirmations to get keys to a FSBO home (r/realtors 296, 2024).
- **Calls:** a buyer's agent with a real buyer may call a FSBO about that buyer; soliciting the listing needs a DNC check ([NAR](https://www.nar.realtor/telemarketing-cold-calling)).
- **Cadence:** most FSBO wins took a drip plus weekly follow-up; one listed on the first call (r/realtors 1200, 2021). Expect other agents to undercut on fee or overpromise on price: one agent never had a FSBO pan out for that reason (same thread).

## Geographic farming and mail

- **Pick the farm by turnover and fit:** homes sold last 12 months / homes in the farm. With median tenure 12 years, about 8% a year is normal; under 4% rarely pays.
- **Same 300 to 1,000 doors, 10 pieces a year, for 18+ months.** Rotate: "I have a buyer", just listed, just sold, a seller testimonial, something kept (a tide calendar in a beach farm got mentioned at listing appointments), quarterly market update with your listings, then pop-bys introducing yourself as "the person from the mailers" and hand-delivered open house invitations (r/realtors 1200, 2021, 6 to 8 listings a year).
- **The counter-case:** an agent who mailed thousands of pieces across two states got zero calls; one-and-done just-sold mailers are the usual failure (same thread).
- **Measure what mail can be measured on:** unique phone, URL or QR per piece type; cost per identifiable homeowner conversation, then per listing appointment, then per signed listing; keep an adjacent area as a holdout where feasible (research synthesis).
- **Hand-built lists beat bought lists for niches.** Investors gave a Fiverr worker a map and the assessor website to build owner name, property and mailing address, then mail-merged letters; one deal per 100-letter round (r/realestateinvesting 631, 2022). A letter with a Street View photo of the owner's building, hand-signed, with a handwritten figure on top, drew 15 to 20% response (r/realestateinvesting 614, 2018). Investor offers, not listing pitches, but the personalization mechanism transfers.
- **Door hangers:** 3 to 5% to call on weekend knocks, with a clear call to action (r/realtors 415, 2025).

## Open houses

- **Treat them as database events.** Funnel KPI: identified movers, substantive conversations, buyer consultations or seller appointments booked, signed clients (research synthesis).
- **Schedule two back to back:** 12 to 2 pm and 2:15 to 4:15 pm, Saturday and Sunday, for four prospecting slots a weekend (r/realtors 279, 2024).
- **One question sorts every visitor:** "Are you mainly comparing this home, this neighborhood, or trying to work out what your own place would sell for?" (research template). The third answer is a listing lead.
- **Know the home cold:** HOA budget, assessments, permits, utility costs, school boundary maps (not opinions about schools), what sold nearby and why.
- **Invite the neighbors in person beforehand.** Many are future sellers and know someone who wants to move near them (r/realtors 1200, 2021).
- **Agreements:** visitors at an open house hosted for the listing broker need no written buyer agreement; the moment you start working with one (finding homes, arranging tours), you need one before touring ([NAR consumer guide](https://www.nar.realtor/the-facts/consumer-guide-to-open-houses-and-written-agreements)).

## Sphere and past clients

- **Size the opportunity:** owners in database / 12 = expected sales a year among them (inference from NAR's 12-year tenure). Your capture rate is closings from them / that number. Under 25% means they are using someone else.
- **Event triggers beat calendar touches:** purchase anniversary, equity milestone, a sale on their street, school-year moves, lease end, rate move (refinance), new baby or job (ask, do not infer), estate events. Fields to keep: relationship type, last transaction, likely next event, property owned, referral given, review status, landlord status, next reason to contact (research synthesis).
- **Local Facebook groups plus events** produced 35 sales in 2025 for one agent in a fast-growing area: sign-up sheets at events, a newsletter twice a month (99% opted in when asked), a personal message to every new group member, testimonials posted in the group, self-promotion about 10% of posts (r/realtors 230, 2025).
- **Visible community roles.** A one-hour classroom lesson for a child's class led to a parent buying a $1.2M to $1.4M home days later (not intended as marketing; r/realtors 1748, 2025). A top agent started by getting a haircut twice a month and selling stylists' homes, then their clients' (r/realtors 290, 2020). Some daycares give parents free ad space (r/realtors 1748, 2025).
- **Referral friction:** a friend with a license wanted referral fees for mutual friends the agent already served; brokerages require a real referral, not a claim on the sphere (r/realtors 282, 2025).

## Specialties that create their own lead flow

- **Pick a niche that does not depend on discretionary buyers.** Life events (marriage, divorce, death, birth, job transfer) move people regardless of rates (r/realtors 437, 2025). One agent went from 1 sale to 50 in year three by specializing in short sales after 2009 (same thread).
- **Relocation content.** A "10 things you should know before moving to Seattle" article generated hundreds of comments and years of referral leads from agents elsewhere (r/marketing 604, 2024).
- **Analytical positioning.** An agent who published market analyses and charts for a year moved from residential into commercial and development and closed over $15M (r/realtors 290, 2020).
- **Commercial:** specialization (hotels) took one broker to about $500k a year by year three (r/CommercialRealEstate 76, 2021); off-market lists from public distress data (NYC energy use plus liens and matured mortgages) beat random cold outreach (r/CommercialRealEstate 466, 2026); in stalled markets, 1031 exchange buyers were the ones still active (r/CommercialRealEstate 71, 2025).
