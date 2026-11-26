# Operations and agency-level tricks

How good operators run small accounts week to week, and the tricks owners rarely know.

## Weekly cadence

| Day | Do |
|---|---|
| Monday | Read change history for the last 7 days (look for "Google Ads Team", automated rules, recommendations); confirm auto-apply is still off; pacing; kill decisions on rolling 14-day data; fatigue check |
| Wednesday | Launch new tests; day-7 checks on last week's launches; search-terms pass on one account (rotating) |
| Friday | Scale or roll back; disapprovals; Friday readout to the owner |
| Monthly | Creative retro, target CPA and allowable CAC review, placement report, negative list refresh, LSA lead reconciliation, audit score |

Source: coreyhaines31 weekly cadence (MIT) and operators (r/googleads 15). Small Search accounts ($1k to 5k/month): about an hour of search-term cleanup at start, then 15 to 30 minutes a week; struggling accounts weekly, stable ones every 2 to 3 weeks (r/PPC 33, 24 accounts run solo).

Classify every change as "creative test", "economics change", "targeting expansion" or "measurement fix", with date, reason and expected effect. Never ship two changes of different types to the same campaign on the same day; you will not know which worked.

## Automation that pays for itself

- Overnight sweep across accounts: pacing, disapprovals, conversion drops, spend spikes, zero-conversion days; delivered as a morning brief (a manager of 118 accounts, r/PPC 70). Script alerts for spend spikes, zero conversions and disapprovals plus a 30-minute Monday MCC sweep (r/PPC 33).
- A daily change-history diff that flags changes your team did not make.
- LLM search-term mining against a written ideal-customer profile; group by intent, flag negatives, draft recommendations; a human approves. Public repo used by practitioners: fourteenwm/ppc-ai-skills.
- Copy QA chain: one model writes, a second checks ad policy, a third checks the claim exists on the landing page.
- Concept generation with forced variety: split past ads into hook, visual, headline, offer, angle and hero subject; score each; generate new combinations; keep a file of past ideas so the model does not repeat itself.

## Budget-entry safety

- Set account-level budgets on invoiced Google accounts and reset them on the 1st. An agency forgot to reset raised daily budgets on 1 May and overspent $104,000; Google gave a $10,000 courtesy credit, the maximum the rep could give (r/PPC 123). Typing a monthly amount into a daily field, and comma vs decimal point confusion (EUR 50,000 in a weekend), are the other classics.
- Check spend within hours of any launch: a $300/month plan spent about $150 on day one, and a "spend $300, get $300" credit was still not applied after $550 (r/googleads 27).
- Max Conversions can spend 2x the daily budget on a given day (balanced monthly).
- Pay ad bills with a cash-back card where allowed: 2% of $3M a year is $60k (r/PPC 339). On Meta, prefer prepaid top-ups for fraud safety.

## Handling Google reps

Reps work recommendation quotas; one asked for tCPA on a zero-data campaign as a "big favour" (r/PPC 151). Their changes cost real money: spend +300% and sales +0% at $1,150/day, then a recommendation of $2,950/day that was just desired sales x current CPA (r/PPC 323); CPC from $50 to $425 and $10,000 in 30 hours (r/googleads); cost per conversion 3.99 to 48.99 after a rep's broad match switch.

- Opt out of contact explicitly; outsourced rep opt-outs lapse about every 3 months.
- Phone script, said to work 70% of the time: "Hi Google Ads, unfortunately, I don't take unplanned meetings and won't be able to have a discussion with you. If you have any recommendations about my account, feel free to email them to me. Do not contact me by phone again."
- Ask for recommendations in a Google Sheet with supporting data and projections. Ask for a server-side tracking walkthrough before any budget discussion; reps then leave you alone for a quarter (41 upvotes).
- What reps are good for at higher spend: closed betas (the "3P Inventory Control" and channel priority betas), internal industry and audience reports for YouTube planning, competitor insight reports.
- Agency heads-up to clients: "Hey just a heads up, you'll likely get some calls or emails from a sales rep at Google who wants you to cede control and adopt settings that will ultimately cost you astronomically more money with little to no increase in performance. Feel free to forward those to us and we'll field them and apply anything relevant." Do not insult the rep in a forward that copies the client.
- Escalate reps who contact clients behind the agency's back to their supervisor; one report brought account credit and an apology.
- "Your ads don't show 90% of the time" from a rep means 10% impression share: explain it to the owner before they panic.
- If performance drops around a platform update and a rep's change at the same time, compare dates in change history; if causes cannot be separated, revert the rep's change.
- Never replace a working account wholesale: an agency imported a 3-keyword template over a working setup, CPC tripled and an auto glass shop went from booked 2 weeks out to empty days (r/googleads 17).

## Competitor research

- **Meta Ad Library:** ads running 60+ days are evidence of profit; sort EU-visible ads by reach through the Ad Library API to rank competitors' concepts by sustained budget (r/FacebookAds 154, vendor claim). Save only ads running more than 2 weeks to the swipe file.
- **Log competitor ads in a sheet:** first 3 lines, CTA, format, start date, landing URL, offer. Read their UTMs in landing URLs (`utm_campaign=search-competitor` tells you the strategy).
- **Click competitors' ads and opt in** to receive their retargeting and email sequences.
- **YouTube:** VidTao shows competitor ad spend over time.
- **Google competitor spend estimate** (r/PPC 39): their impressions = your impressions / your impression share x their impression share (Auction Insights); their CTR = your CTR x 1.25, 1.0 or 0.75 depending on whether their position-above rate is over 60%, 30 to 60% or under 30%; their CPC = your CPC x (your Quality Score / their estimated QS); spend = clicks x CPC. Rough, but useful for sizing.
- **Amazon and TikTok:** see which products brands push heavily in GMV Max; affiliates read that as demand.
- **Seasonal arbitrage:** a product trending on TikTok while Amazon and local retailers were out of stock did GBP 2k in 3 days on Google Shopping (r/dropship 218).
- **Smaller language markets** (Nordics, Benelux, Portugal) often have little bidding competition in a category.

## Agency qualification and pricing (if the user runs an agency)

- Run BuiltWith before taking a client: no email tool, GA or pixel means too early (r/PPC 538).
- Budget floors from operators: personal injury Search $10 to 15k a month; supplements $10k+ a month with a real differentiator; refuse SaaS at $40/day with $25+ CPCs (fewer than 2 clicks a day). Check fulfillment capacity: one installation business dropped its agency because it could not install what was sold.
- Turn a "free trial" request into a paid 7-day audit with no changes made, pitched on waste found.
- Fee models: minimum monthly fee plus 10 to 15% of ad-driven revenue; percentage of spend with lower rates above thresholds; an optional 10% annual increase written into the contract; $1,500 to 2,000/month plus a per-lead fee.
- Offboarding: a 1 to 2 page handover (strategy, recent tests and why they won or lost), keep internal SOPs; a 30-minute wrap-up call brought back about 10% of clients who moved in-house (r/PPC 163).
- Ask every happy client for introductions to 2 business owners; one agency credits this for about $60k/month (r/FacebookAds 152).

## Client-ego tricks (use with care)

- Clients searching their own ads and not seeing them call the agency. Some agencies spend about 10% of budget on a tight exact-match campaign around the client's own location so they see their ads; others call it waste (r/PPC 45). Better: teach the owner to use the Ad Preview tool, which does not cost clicks or skew data.
- Annotate account changes neutrally ("strategy pivot to display ads") so an owner can reverse a bad decision without losing face (r/PPC 41).

## Reporting language

- Positive: "Conversions are up and we're hitting our CPA target. Our recommendation is to increase budget by 10%."
- Negative: "CPA is too high. We're continuing to add negative keywords to filter our traffic. We recommend you add [XYZ] to your landing page to improve conversion rates."
- Never pad a quiet week: "nothing material changed" protects credibility. Never report platform revenue as business revenue.
