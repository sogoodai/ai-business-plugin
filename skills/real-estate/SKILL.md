---
name: real-estate
description: Grow a real estate agent, team, property manager or mortgage loan officer business. Lead source economics (sphere, Zillow, Realtor.com, Redfin, Google, Meta, open houses, expireds, FSBOs, farming), speed to lead and long nurture, listing presentations, buyer consultations after the NAR settlement, owner acquisition and retention for property management, agent referral partners for loan officers, scripts, and fair housing, RESPA and TCPA rules.
---

# Real estate: win the first conversation, then compound the database

For buyer and listing agents, small teams (up to about 20 people), residential property managers and mortgage loan officers, mostly US, with UK, EU, Canada and Australia notes. Built from 90 practitioner threads selected out of 1,875 scraped (r/realtors, r/RealEstate, r/realestateinvesting, r/CommercialRealEstate, r/Mortgages, r/PropertyManagement), 2025 to 2026 data (NAR, Zillow Consumer Housing Trends, Pied Piper, LocaliQ, WordStream, Redfin, Buildium, AppFolio, MBA, NBER, CFPB, HUD, FCC, Google, Rightmove, ASA, ACCC) and the public real estate skills worth keeping (UnifAPI, MIT). "Operators report" marks a Reddit anecdote with its upvotes and year; everything else carries its source and year. Full list: [references/sources.md](references/sources.md). The owner's and their broker's decisions win over this guide, and nothing here is legal advice.

## How these businesses actually grow

- **Production is thin, so a few deals change everything.** The median REALTOR did about 9 transaction sides and $59,200 gross income in 2025; teams did 31 to 32 sides and $17.5M median volume (NAR 2026 Member Profile). Two extra closings a year is a 20% raise for the median agent.
- **Relationships and online split the first contact.** Buyers found the agent they used through websites and apps 28%, friend or family referral 19%, a past agent 11%, open houses 6%, search 5%, social 4%, direct mail 1%. Sellers: online 35%, referrals 30%, past agent 14%, search 7%, social 5%, open house 3%, mail 2% (Zillow CHTR 2026). Database work and online capture are the two engines; everything else is a feeder.
- **The first agent who shows up usually wins.** 54% of buyers hired the first agent they contacted (50% in 2025) and 67% of sellers contacted only one agent (Zillow 2026).
- **The industry does not answer.** In a 2,198-inquiry mystery shop of 21 US brokerage brands, 68% of website inquiries got no response within 24 hours, 10% reached an agent within an hour, and phone calls reached an agent live 33% of the time (Pied Piper, Oct 2026). Answering is the cheapest edge available.
- **One client is often two sides.** 81% of agent-assisted sellers who also bought used the same agent for both (Zillow 2026). Every seller conversation is also a buyer conversation.
- **Owners move about once every 12 years.** Median tenure before selling hit 12 years (NAR 2026 profile). Rough inference: about 1 in 12 owner households in a sphere sells in any year, so a 300-owner sphere produces about 25 sales a year. The question is capture rate, not "does my sphere move".
- **Property managers and loan officers grow through someone else's trust.** 62% of mortgage buyers used an agent referral while shopping and 20% first found their lender that way (Zillow 2026). 79% of agents send over 40% of their clients to just four loan officers (NBER working paper, 91,988 agents, 2026). Only 23% of rental owners rate their manager's value excellent (Buildium 2026, vendor survey).

## Route by sub-model first

| Sub-model | Main growth engine | First metric to fix | Go deep in |
|---|---|---|---|
| Buyer agent | Online and portal capture, buyer consultation, open houses as database events | Inquiry to two-way contact, then consult to signed agreement | [buyers-and-nar-settlement.md](references/buyers-and-nar-settlement.md), [speed-to-lead-and-nurture.md](references/speed-to-lead-and-nurture.md) |
| Listing agent | Sphere and past clients, farm, expireds, listing presentation | Listing appointments per month and list-to-sold ratio | [listings-and-sellers.md](references/listings-and-sellers.md), [lead-sources.md](references/lead-sources.md) |
| Team lead | Paid or portal leads routed to agents, ISA and leverage | Cost per closing and agent take-home by source | [team-lead.md](references/team-lead.md) |
| Property manager | Google Search and Maps for owners, agent referrals, accidental landlords | Owner churn and cost per signed door | [property-management.md](references/property-management.md) |
| Loan officer | Agent referral partners, past-client and preapproval database | Funded loans per active partner | [loan-officers.md](references/loan-officers.md) |

## First session: ask, then compute

Ask the owner:

1. Sub-model, license type, broker or company, country and state or province, markets served, average price point.
2. CRM and whether you can export 12 months of leads with source, stage, appointment, agreement, close date and gross commission or loan revenue.
3. Every lead source with monthly spend and contract terms: Zillow (Premier Agent or Flex), Realtor.com, Redfin, Opcity, Homes.com, Google, Meta, mail, data lists, referral networks.
4. Who answers new inquiries, in what time, on which days; what happens after hours and on weekends.
5. Split and fees: brokerage split, team split, referral fees, caps, admin fees. Agent or LO net per closing.
6. Database: total contacts, past clients, sphere, how many have phone and email, what consent exists for texting.
7. Reviews: Google rating and count, Zillow and Realtor.com reviews, testimonials.
8. Listings taken last 12 months, list-to-sold ratio, average days on market vs the local MLS.
9. Property managers: doors, owners, fee schedule, owner churn last 12 months, reasons. Loan officers: units funded, partners who sent anything, pull-through.
10. What they will not do (cold calls, door knocking, video), and who approves ads and compliance.

Then compute ([references/lead-sources.md](references/lead-sources.md)):

```
net per closing = sale price x commission rate - referral fee - brokerage split - team split - fees
cost per closing (by source) = (spend + referral fees paid) / closings from that source (12-month cohort)
allowable cost per lead = net per closing x observed lead-to-close rate (same source, 12+ months)
allowable cost per connection = net per closing x connection-to-close rate   (Zillow)
two-way contact rate = leads with any real reply / leads             (first diagnostic)
sphere capture = closings from past clients and sphere / estimated sphere moves (owners / 12)
PM door value per year = rent x fee% x 12 + leasing fee x turnover rate + renewal fees
LO partner yield = funded loans from partner / buyers partner closed (ask partner)
```

Report the three biggest leaks in money. The usual first finding: unworked leads and a silent database are worth more than any new source.

## Lead source economics in one screen

| Source | How you pay | What the data shows | Rule |
|---|---|---|---|
| Sphere and past clients | Time, events, mail | 19 to 30% of first contacts are referrals, 11 to 14% past agent (Zillow 2026) | Fix first; event triggers, not "checking in" |
| Zillow Premier Agent | Per connection | $223 major metro, $139 elsewhere; Zillow asks Flex partners for 10% connection to close, so about $2,230 / $1,390 per closing before splits (Zillow 2026, vendor target) | Commit 6 months only with 5-minute answering |
| Zillow Flex | Referral fee at close | 40% on seller connections, variable on buyers (Zillow pricing page 2025) | Model net after fee and team split before accepting |
| Realtor.com ReadyConnect | Pay at close | Live transfer, contact attempted in about 4 seconds; 3 to 5x conversion claim is 2019 data | Treat as a live conversation, owner plus backup |
| Redfin Partner | Referral fee at close | 5-minute connection, 55% acceptance, 80% customer list compliance required (Redfin 2025) | Fee schedule changes on 30 days' notice; read yours |
| Google Search | Per click | Residential agents 1.29% click to lead, $157.59 CPL; property management 10.24%, $76.71 CPL (LocaliQ 2026) | Best for PM owners and sellers; import offline conversions |
| Meta lead forms | Per lead | $13.74 CPL, 9.95% click to lead (WordStream 2026) | Cheap lead, not cheap closing; qualify in the form |
| Open houses | Time | 6% of buyers, 3% of sellers met their agent there (Zillow 2026) | Database event; count consultations, not visitors |
| Expireds and FSBOs | Data plus calls | 44.4% of expireds relisted, 31.8% of FSBOs listed with an agent (REDX 2026, vendor, population not your conversion); FSBO is 5% of sales and 62% knew the buyer (NAR 2026) | DNC scrub first; differentiate or skip |
| Farming and mail | Postage, $0.26 EDDM | Mail is 1 to 2% of first contacts (Zillow 2026); operators report 6 to 8 listings a year from 10 mailers plus pop-bys (r/realtors 1200, 2021) | 18+ months in one area or not at all |

Operators report about 1 closing per 30 Zillow or Realtor.com leads in the first month, plus 1 or 2 more after about 6 months of drip: roughly $1,500 per closing from Zillow at about $150 a lead vs $300 to $450 from Realtor.com at $30 to $45 (r/realtors 1200, 2021, pre-Flex prices; the poster's own numbers do not fully reconcile). No independent 2025 to 2026 dataset gives cost per closing by source. Say so; compute the owner's own.

## Decision rules, in order

1. **Answer before you buy.** Every inquiry gets an automatic reply in under a minute and a human in 5 minutes during staffed hours, with a named backup. If leads arrive faster than agents answer, cut spend. Redfin removes partners who miss its standards; Zillow tells Flex teams not to give agents more connections than they can handle.
2. **Mine the database before new sources.** Segment past clients, sphere, old buyers, old sellers, renters who might buy, landlords. Request missing reviews. Trigger outreach on events (purchase anniversary, equity milestone, a listing near them, rate move, lease end). Track conversations and appointments per 100 reachable contacts.
3. **Sell the consultation, not the tour.** US buyer agents need a written agreement before an in-person or live virtual tour, with compensation that is objectively ascertainable (NAR practice changes, 17 August 2024). Package the 20-minute strategy session as the product.
4. **Win listings with pricing evidence.** 42% of sellers name pricing and market knowledge as the most valuable agent service, 67% put it in their top two (Zillow 2026). Floor plans (33%) and photos (26%) matter to buyers far more than video (4%) (Zillow 2025).
5. **Add one paid source at a time.** Google Search first for sellers, owners and refinance intent; Meta for awareness and long-nurture lists; portals only with answering in place. Kill or keep on cost per signed client after a full nurture window, never on CPL.
6. **Property managers: sell maintenance control and communication.** Owners pick on tenant management 57%, maintenance coordination 43%, customer service 34%, responsiveness 31%; poor communication is the top switching reason at 57% (Buildium 2026).
7. **Loan officers: become one of an agent's four.** Offer an observable service level (preapproval turnaround, a call to the listing agent on every offer, file updates), never a referral-linked benefit.
8. **Compliance gates everything.** Fair housing copy and targeting, RESPA on every partner deal, DNC scrub before every call list, written consent before automated texts. See [references/compliance.md](references/compliance.md).

## Speed to lead and nurture in one screen

- **Minute 0 to 5:** call; if no answer, text naming the property or request and asking one question; call again at minute 5. Realtor.com's automatic first text was simply "Hey this is Bryan! When is a good time to talk!" (r/realtors 1200, 2021).
- **Day 1 to 10:** one touch a day, alternating call and text, each referencing something specific. Then days 14, 21, 30.
- **Long nurture:** by timeline bucket (0 to 3, 3 to 6, 6 to 12, 12+ months) with saved-search listing alerts as the engine and a personal touch monthly tied to an event. Operators report the 6-month drip adds 1 or 2 closings per 30 leads on top of the first month's one (r/realtors 1200, 2021).
- **Lifecycle states, never a silent lead:** NEW, ATTEMPTED, TWO-WAY, QUALIFIED, APPOINTMENT, AGREEMENT, ACTIVE, UNDER CONTRACT, CLOSED, NURTURE, LOST or DO NOT CONTACT. Each has an owner, a next action and a due time (research synthesis, 2026).
- **The first diagnostic is lead to two-way contact,** before lead to appointment. It separates a traffic problem from a follow-up problem.

Full cadences, CRM fields, ISA and VA setup: [references/speed-to-lead-and-nurture.md](references/speed-to-lead-and-nurture.md).

## What changed in 2024 to 2026

- **NAR practice changes (17 August 2024):** written buyer agreement before touring; no compensation offers on the MLS; buyer agent pay must be specific and negotiable. Average buyer agent commission was 2.43% in Q2 2025, back to pre-settlement levels (Redfin). Open house visitors do not need an agreement with the listing agent hosting.
- **Private listings:** NAR's Multiple Listing Options for Sellers (2025) allows delayed marketing with a signed seller disclosure; Zillow's Listing Access Standards (enforced from June 2025) ban a listing for life if it is publicly marketed but not on the MLS within 24 hours, three strikes per agent.
- **Fair housing guidance:** HUD withdrew its 2024 digital advertising guidance and other FHEO guidance in September 2025. The Fair Housing Act's advertising ban (42 U.S.C. 3604(c), 24 CFR 100.75), state agencies and private suits are unchanged. Keep the conservative rules.
- **TCPA:** AI-generated voices count as artificial voice and need prior consent (FCC, Feb 2024). Consent can be revoked by any reasonable means (FCC order, compliance dates 2025 to 2026). The one-to-one lead-generator consent rule was vacated (11th Cir., Jan 2025): collect your own consent anyway.
- **Search:** Google says llms.txt and AEO or GEO hacks are not needed and it stopped showing FAQ rich results on 7 May 2026. Templated "[city] realtor" pages risk scaled content abuse.

## When practitioners and the data disagree

| Topic | Practitioners say | Data says | Rule |
|---|---|---|---|
| Cold calling and door knocking | Brutal, "masochistic" (r/realtors 1200); one agent knocks 25,000 doors a year and wins (r/realtors 1025) | No independent conversion data; DNC fines up to $53,088 per violation (FTC 2025) | Only if the owner likes it, scrubbed, scripted, and measured per conversation |
| Facebook leads | "Hot garbage" vs 1 to 2 deals a month from under $7 a day | $13.74 CPL, intent unequal to search | Qualify in the form, nurture 6 to 12 months, judge on closings |
| Mailers | Thousands spent, zero calls vs 6 to 8 listings a year | Mail is 1 to 2% of first contacts | One farm, 10 pieces a year, pop-bys, 18+ months |
| Open houses | 8 to 12 a month, no deals in 8 months (r/realtors 82, 2026) | 6% of buyers met their agent there | Two back-to-back opens per day; KPI is booked consultations |
| Expireds | Avalanche of 30 to 50 calls a day per seller (r/realtors 230, 2026) | No exemption from the DNC registry | Mail and door with a written diagnosis; call only scrubbed numbers |
| Speed to lead | "Answer every call, even at dinner" built a $25M team (r/realtors 184, 2022) | The "21x in 5 minutes" stat is pre-2024 and not real estate | Five minutes as an operating standard; measure your own win rate by response time |

## Never

- Never write copy or targeting that says or implies who should live somewhere: "perfect for young couples", "family neighborhood", "safe area", "no kids". Describe the property and amenities.
- Never offer or accept anything of value for a settlement service referral (RESPA Section 8), including "I'll pay for your event if you send me three buyers".
- Never call a number on the National Do Not Call Registry to solicit a listing, including expireds and FSBOs, without an exemption.
- Never send automated marketing texts or AI voice calls without prior express written consent.
- Never forecast a vendor's population statistic (REDX relist rates, Realtor.com's 2019 multiple) as your conversion rate.
- Never publicly market a listing off-MLS in an MLS that follows Clear Cooperation, or claim "#1 agent" without a defined, provable metric (ASA in the UK; state rules in the US).
- Never invent a review, testimonial, sold price or market statistic; never change a client's file, price or terms as a marketing action.

## Before you write any message

Use [references/scripts.md](references/scripts.md): portal first text, sphere touches, referral ask, review request, expired and FSBO calls, open house sign-in and follow-up, buyer consultation, listing presentation close, price reduction, property management owner pitch and monthly update, loan officer agent pitch.

## References

- [benchmarks.md](references/benchmarks.md): metric, typical, top quartile, source, year; production, sourcing, response, ads, PM, LO, international.
- [lead-sources.md](references/lead-sources.md): cost per closing by source, portal mechanics, expireds, FSBOs, farming, open houses, sphere math.
- [speed-to-lead-and-nurture.md](references/speed-to-lead-and-nurture.md): first 5 minutes, 30-day and 24-month cadences, CRM fields, ISA and VA.
- [listings-and-sellers.md](references/listings-and-sellers.md): listing presentation, pricing evidence, launch assets, price reductions, private listings, UK and Australia.
- [buyers-and-nar-settlement.md](references/buyers-and-nar-settlement.md): buyer consultation, agreements, compensation, qualifying, buyer fee models.
- [local-and-content.md](references/local-and-content.md): Google profile for agents, neighborhood pages, video system, Facebook groups, AI answers.
- [property-management.md](references/property-management.md): owner acquisition, offers and fees, accidental landlords, retention, value events.
- [loan-officers.md](references/loan-officers.md): agent partner program, scoring, refinance and past-client triggers, product angles, ad rules.
- [team-lead.md](references/team-lead.md): split math, lead routing, ISA, showing agents, recruiting offers.
- [compliance.md](references/compliance.md): fair housing, RESPA, NAR rules, TCPA and DNC, Reg Z, UK, EU, Canada, Australia.
- [scripts.md](references/scripts.md): exact wording for every recurring conversation.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [plan-90-days.md](references/plan-90-days.md): 90-day plans for agents, team leads, property managers and loan officers.
- Sibling skills: `local-seo` for Google Business Profile, reviews and AI visibility depth; `paid-ads` for account structure, bidding and special ad categories; `email-sms-loyalty` for flows, deliverability and consent records; `organic-social` for content systems; `b2b-outbound` for cold outreach mechanics (loan officer to agent, PM to investor); `home-services` for missed-call text back and quote follow-up patterns.
