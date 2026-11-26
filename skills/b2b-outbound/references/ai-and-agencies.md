# AI SDRs, automation, and buying outbound from agencies

Two buy-or-build questions small companies get wrong: letting an AI write and send everything, and paying a lead-gen agency for "meetings". Sources: [sources.md](sources.md).

## What the evidence on AI SDRs actually supports

There is no independent, normalized, cross-vendor study showing that autonomous AI SDRs raise meetings by a known percentage. The evidence is vendor case studies plus counter-evidence on AI-written messages.

For:
- Salesforce, Perk: prospecting agent produced 3x call volume, 2x email reply rate, 60% of North American pipeline (first-party customer story).
- Common Room, Superhuman: AI-recommended contacts booked meetings at 2.5x cold contacts, replies +50%, lead-to-opportunity time -35%, closed-won pipeline 2.4x.
- UserGems, NetSPI (Jan 2026): 71 meetings, 32 SQOs, $610K pipeline, $44K closed-won in 4 to 5 months from a signal-led workflow.
- These mix better signals, faster workflow and automation. They prove AI helps decide who to contact; they do not prove AI-written outreach caused the gains.

Against:
- Hunter 2026 survey: 69% of US decision-makers are bothered when they believe AI wrote the email.
- Expandi 2026, within the same accounts: AI-hyperpersonalized LinkedIn messages had 12% lower acceptance and no reply gain vs those accounts' human templates.
- Hunter 2025 sends: manually edited emails 5.2% vs fully automated 4.4%.
- Operators: fully AI-booked meetings showed 52% vs 71% for human-booked (r/b2bmarketing 24, unsourced). "AI is not good enough to write a compelling offer" (r/agency 37).

Practitioner uses that held up:
- LLM first lines from recent posts or company news stored in a CRM field, escalated to a stronger model when quality is low; reported about 3x previous replies (r/SaaS 364, possibly a tool plug).
- AI agents find businesses with a fixable visible problem, the LLM drafts around that problem, a human rewrites the opening line (r/EntrepreneurRideAlong 210).
- Claude Code scripts that audit a prospect's site (PageSpeed, schema, title tags, last blog date) to produce a verified one-line opener (r/LeadGeneration 52).
- AI scores prospects 0 to 10 with reasons; the seller picks who gets contacted (r/LeadGeneration 79, unnamed tool).
- AI triages replies (OOO, referral, objection, hard no, ready to schedule); humans answer the warm ones; saves about 1 hour per SDR per day (r/b2bmarketing 22).
- Post-call follow-up drafted from the transcript plus an SOP within 10 minutes (r/agency 26).

## The division of labor

| AI owns | Human owns or approves |
|---|---|
| Enrichment, dedupe, verification, suppression | Claims and proof used in messages |
| Signal detection, trigger classification, ICP scoring | Tier 1 messages (every one) and a sample of Tier 2 |
| Research briefs with a source URL per fact | Positive replies, objections, referrals |
| Drafts, variants, segment copy | Anything sensitive (health, money, layoffs, breaches) |
| Scheduling, cross-channel stop rules, CRM hygiene | Legal exceptions and new countries |
| Meeting prep, call summaries, experiment reports | Pricing, negotiation, discovery |

Rule for an agent drafting: facts first, then the angle, in two separate steps. Every fact gets a source URL and date. "No hook found" is an allowed output. Before any autonomous send: each claim matches an approved source, no phrase from the banned list, a daily cap applies, and a human samples a share weekly.

Rule for an agent sending: only after 100+ drafts of a reply type were approved without edits, and only for low-risk types (out of office, unsubscribe, bounce, not now). Positive replies stay human until then.

## Automation lines not to cross

- No LinkedIn automation or scraping on the owner's account (terms violation, permanent bans, vendors removed by LinkedIn).
- No dozens of auto-created domains or fake warmup conversations "because the vendor calls it warming".
- No AI voice calls to US mobiles without consent (TCPA).
- No sending to scraped personal addresses.
- No bait: "I've got 5-10 people interested in your gym" style openers that are admitted bait-and-switch.

## Buying outbound from an agency or setter

The market is full of "guaranteed leads". What operators report losing:
- About $10K for a "20 qualified leads a month" pilot: the vendor counted positive replies, including people asking for a case study, as leads. Zero meetings (r/agency 30).
- GBP 574 upfront for "5 clients in 2 months" with a signed refund promise: zero leads, no refund (r/LeadGeneration 22).
- $25-per-lead "content syndication" that was raw tool database exports; the vendor claimed Dubai and operated from elsewhere (r/LeadGeneration 21).
- GBP 8K a month for about 4 qualified meetings a quarter; one in-house SDR did better by month 2 (r/b2bmarketing 128).
- A 500 to 1,500 a day operation booked no-shows, people who ghosted after call 2 and buyers without budget; the client fired them around month 6 (r/b2bmarketing 40).
- About $100K in a year on a directory sponsorship (Clutch) with no pipeline (r/b2bmarketing 39).

Agency-side economics, so the owner knows what is realistic (r/b2bmarketing 61 and 19; r/LeadGeneration 15 and 23):
- Retainers run $1,500 to $6,000 a month; one account manager carries 25 to 30 clients, so 2 to 3 hours per client a week.
- Typical client lifespan 5 to 7 months. Month 1 is data gathering.
- Pay-per-meeting creates disputes ("that lead would have closed anyway"); agencies move to flat retainers or 90-day paid trials.
- Commission math: a $5K deal at 20% commission and a 20% close rate is worth $200 per appointment to the provider, below market.
- About half of prospective clients are a fit; slow client follow-up (48 hours) gets the agency blamed.

**Questions to ask before signing:**
1. Show 12 months of results, not the best month (one agency's best was 47 meetings against an average of 12).
2. Report total replies, positive replies, meetings booked, meetings held and opportunities separately. 200 "replies" can mean 35 to 40 positive.
3. Define a lead as a held meeting with a title and company size we approved, in writing.
4. Whose domains and inboxes? Never let them send from our primary domain. Who owns the domains and data at the end?
5. Which countries, and how do you handle GDPR, PECR, CASL and opt-outs?
6. What is "pipeline"? Often meetings x deal size; real pipeline is maybe 20 to 30% of that.
7. A prospect asking "how fast can we scale to 10K a day from one domain" is a red flag, from either side.

**Rule:** run outbound in-house (founder or one SDR plus the agent) until conversion rates are known, then outsource volume with those numbers in the contract (r/LeadGeneration 41).

## Tool map (no endorsement, check current terms)

| Job | Common options |
|---|---|
| Contact data | Apollo, ZoomInfo, Lusha, Prospeo, Hunter, Findymail, Anymail Finder; Clay or FullEnrich for waterfalls |
| Signals | TheirStack, PredictLeads (hiring); UserGems, Clay (job changes); Common Room, Trigify (engagement); Crunchbase (funding); BuiltWith, Wappalyzer (stack); RB2B, Warmly, Koala (site visitors) |
| AI list builders | Exa Websets, Parallel FindAll: precise, incomplete (one 2026 evaluation: the best found about a fifth of possible matches) |
| Sending | Instantly, Smartlead, lemlist, Woodpecker, EmailBison |
| Inboxes | Google Workspace, Microsoft 365 direct; managed providers |
| Verification | NeverBounce, ZeroBounce, MillionVerifier, Bouncer, Reoon; BounceBan for catch-alls |
| Placement and reputation | GlockApps, MailReach, Google Postmaster Tools, Microsoft SNDS |
| Calling | Power dialers (Orum, Nooks, Aircall), parallel dialers for large lists |
| Video | Loom, Tella, Sendspark, Vidyard |
| Booking | Calendly, SavvyCal |
| CRM | HubSpot, Attio, Close, Pipedrive |

Webhooks for "reply received", "bounced" and "unsubscribed" from the sending tool are the simplest way for an agent to enforce the cross-channel stop.

## Tricks most owners miss

- AI's proven value is deciding who deserves a human-quality message now, not writing more email.
- A fully autonomous agent multiplies a bad offer. Prove the offer by hand on 50 to 250 accounts first.
- The legal burden does not move to the vendor because an agent sourced, sent or classified the message.
- One reusable, genuinely useful asset (a guide, a teardown template, a benchmark) beats hundreds of AI-personalized first lines.
