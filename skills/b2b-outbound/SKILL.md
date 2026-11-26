---
name: b2b-outbound
description: Run B2B outbound for a small company. Cold email setup (domains, inboxes, warmup, Google and Microsoft rules), lists, signals and triggers, personalization, templates, follow-ups, LinkedIn outreach, cold calling and missed-call sequences, appointment setting, discovery, reply benchmarks, CAN-SPAM, GDPR, PECR and CASL, AI SDRs and lead-gen agencies. Use for "nobody replies", "set up cold email", "write a sequence", "should I buy an agency".
---

# B2B outbound: the right people, the right week, one honest reason

Built from 616 practitioner tactics extracted from 246 threads (r/b2bmarketing, r/LeadGeneration, r/salestechniques, r/sales, r/Emailmarketing) plus outbound threads from r/agency, r/freelance, r/SaaS, r/microsaas, r/startups and r/Entrepreneur; 2025 to 2026 data (Hunter, Smartlead, Instantly, Woodpecker, Belkins, Lemlist, Expandi, Gong, Orum, Smarter Outbound); primary rules (Google, Microsoft, LinkedIn, FTC, ICO, EDPB, CRTC, ACMA, FCC); and the best public skills (coreyhaines31 cold-email, prospecting and sales-enablement, MIT). "(r/sub, score)" marks a practitioner report; everything else carries its source and year. Sources: [references/sources.md](references/sources.md). The owner's decisions win over this guide.

## How outbound works for small companies in 2026

- **It is a targeting and infrastructure problem before a copy problem.** Sequences of 21 to 50 recipients replied at 6.2% vs 2.4% at 500+ (Hunter, 31M emails sent in 2025). Fixing warmup, DNS and per-inbox volume with identical copy roughly doubled one agency's replies (r/b2bmarketing, 61).
- **Timing beats cleverness.** A dated trigger (job change, new leader, hiring, funding, stack change, competitor engagement) gives the "why now". Job-change plays report 17%+ replies (Common Room 2025, vendor's own play).
- **Short, plain, human.** Under 80 words, plain text, no link in email 1, tracking off (7.4% vs 4.4% replies, Hunter 2026), an interest question instead of a meeting ask.
- **Three touches per channel, then stop.** 3 emails 6.8% vs 1 email 3.3% (Hunter); email 7 earns a quarter of email 1 (Smartlead 2026). LinkedIn: 3 messages 9.8% vs 5+ 5.0% (Expandi 2026).
- **Offer something smaller than a meeting.** A free deliverable instead of "hop on a quick call" took one client from 0.9% to 3.4% replies in 2 weeks (r/b2bmarketing, 170).
- **Channels have jobs.** Email carries the reason, LinkedIn adds recognition, the phone gets the conversation. A reply on any channel stops all of them.
- **AI decides who deserves a human-quality message.** 69% of US buyers are bothered by AI-written email (Hunter 2026); AI LinkedIn notes cut acceptance 12% (Expandi 2026). AI researches, scores and drafts; humans approve Tier 1 and answer positive replies.
- **Law depends on the recipient's country and entity type.** US CAN-SPAM allows cold B2B email with rules; Germany, Canada and Australia effectively need consent; UK sole traders need consent while UK companies do not.

## First session: ask, then compute

Ask the owner:

1. What you sell, price, and first-year gross margin per customer. Current close rate from a held meeting.
2. Last 12 months of closed-won and closed-lost deals (industry, size, title, cycle).
3. Target countries, and whether buyers are companies or sole traders.
4. Current domains and inboxes; anything ever sent cold from the main domain; sending tool; CRM.
5. Data and signal tools already paid for (Apollo, Sales Navigator, Clay, dialer).
6. Who sends, who approves claims and offers, whether you will call, whether LinkedIn is the founder's personal asset.
7. Proof you can name (results, logos, case numbers) and offers you will make (audit, sample, pilot, free tier).
8. What you will never do (calls, free work, guarantees, certain countries).

Then compute ([references/plan-90-days.md](references/plan-90-days.md)):

```
positive reply rate      = positive replies / contacts sequenced            (not opens, not sends)
meeting rate per contact = meetings held / contacts sequenced
contacts needed / month  = target held meetings / meeting rate per contact
inboxes needed           = (new contacts per day x emails per contact) / 15 to 25
domains needed           = inboxes / 2 to 3, plus 10 to 20% spares
cost per held meeting    = (tools + data + inboxes + hours x rate) / meetings held
max cost per meeting     = first-year margin x close rate from held meeting / 3   (3:1 rule of thumb)
connect rate             = conversations / dials        (below 5%: fix phone data first)
LinkedIn yield           = meetings / invitations sent
```

## Benchmarks to check first

Vendors use different denominators. Pick one, keep it, never average them ([references/benchmarks.md](references/benchmarks.md)).

| Metric | Typical | Strong | Source |
|---|---|---|---|
| Cold email reply, sender percentile | 0.74% median | 1.43% p75 | Smartlead, 850M emails, H1 2026 |
| Cold email reply, campaigns | 3.43% average | 5.5%+ top quartile | Instantly, 2025 data |
| Positive reply per prospect | 0.79% median | 1.36% top quartile | Smarter Outbound 2026 |
| Bounce | 1.54% median | under 1%; pause at 2% | Smartlead H1 2026 |
| LinkedIn acceptance | 27 to 29% | 53.9%+ top 10% | Lemlist and Expandi, 2025 to 2026 |
| LinkedIn message reply | 6.6 to 10.4% | 19.9%+ top 10% | Lemlist, Expandi |
| Cold call connect | 5.4% | 13.3% top quartile | Gong, 300M calls, pub. 2024 |
| Sends per meeting | 344 average | | Gong, 28M emails, 2025 |

## Decision rules, in order

1. **No authentication, primary-domain sending or tracking on:** fix infrastructure before anything else ([references/infrastructure.md](references/infrastructure.md)). Gmail's 5,000-a-day bulk threshold counts the whole primary domain, subdomains included, and bulk status is permanent.
2. **List over 600 or ICP over 10,000 companies:** split by trigger and persona until each campaign shares one problem ([references/lists-and-signals.md](references/lists-and-signals.md)). 1 to 2 contacts per company.
3. **Every prospect needs a dated signal or a verified gap.** Roughly half of a list has no signal: those go to Tier 3 or out.
4. **Replies far below your benchmark:** deliverability first (seed test, bounces, Postmaster), then list, then offer, then copy. Never add steps or volume to fix a low rate.
5. **Replies fine, positives low:** the offer or the ICP is wrong. Read 20 replies and group the no-reasons.
6. **Positives fine, few meetings:** reply speed and booking. Answer in minutes with two times.
7. **Meetings fine, no deals:** discovery, authority and single-threaded champions ([references/discovery-and-booking.md](references/discovery-and-booking.md)).
8. **Scale only a proven segment,** by adding inboxes and segments, never by raising per-inbox volume above about 25.
9. **Before any send, check country and entity type** ([references/legal.md](references/legal.md)).

## Cold email setup in one screen

- 2 to 5 secondary domains, 2 to 3 real-person inboxes each, SPF + DKIM (2048) + DMARC p=none aligned to From, Postmaster and SNDS.
- Licensed Workspace or Microsoft 365 tenants; match the sender provider to the prospect's MX; SMTP replied at half of Workspace in one 3-month test (r/b2bmarketing, 46).
- Warm 14 to 21 days, start at 5 to 10 cold a day per inbox, ramp to 15 to 25. Median sender: 13.9 a day (Smartlead 2026).
- Plain text, no link in email 1, tracking off, opt-out line and postal address.
- Verify within a week of sending; bounce under 2%; catch-alls on separate inboxes.
- Stop-loss: bounce over 2%, placement under 70%, complaints near 0.1%, reply under about 1% after 300 delivered.

## Copy and cadence in one screen

- Trigger, consequence, one proof point, one soft ask. Remove the personalized line: if the email still works, it was decoration.
- Two meaningful custom facts lift replies (5.6% vs 3.6%, Hunter 2026). Manually edited beats fully automated (5.2% vs 4.4%).
- Subject 2 to 4 lowercase words that look internal. Interest CTAs: "Is this a relevant topic for you?" (r/sales, 901).
- Day 0, 3, 8. Each follow-up adds information; never "just checking in". 88.5% of replies land within 24 hours of a send (Smartlead), so a human watches the inbox.
- Permission offers beat links: "I wrote out a google doc going over how you can... Can I send it over?" (r/b2bmarketing, 25).

Templates, frameworks, offers and reply handling: [references/copy-and-cadence.md](references/copy-and-cadence.md).

## LinkedIn in one screen

- No official weekly invite cap; restrictions follow ignored invites and automation. Automation and scraping break the User Agreement: manual or assisted only on the founder's profile.
- No note maximizes acceptance (36% vs 29%, r/b2bmarketing, 42); a note maximizes replies (8.2% vs 5.3%, Belkins 2026). Free accounts get about 3 notes a month.
- Engage, request, ask about their process, value in message 2 (the strongest step), light ask or voice note, stop.
- Short DMs win: under 20 words 28% replies vs 80+ words 4% (r/LeadGeneration, 28).

Depth: [references/linkedin.md](references/linkedin.md).

## Calling in one screen

- Permission opener: "This is a cold call, can I take 30 seconds to tell you why I called, then you tell me if it's worth continuing?" (Gong: 11.18% vs 2.15% for "bad time?").
- Missed call: LinkedIn note referencing the call within 5 minutes, email next day: 14.1% responses vs 2.3% voicemail callbacks (r/Entrepreneur, 480).
- Callbacks are 4x more likely to book; 75% arrive within 1.75 hours (Orum). They interrupt everything.
- Tuesday to Thursday 10:00 to 11:30 connected at 19% vs 5% Friday afternoon for one caller (r/Entrepreneur, 480).
- No AI voice or ringless voicemail to US mobiles without consent; scrub DNC.

Depth, scripts and gatekeepers: [references/cold-calling.md](references/cold-calling.md).

## When practitioners and the data disagree

| Topic | Practitioners say | Data says | Rule |
|---|---|---|---|
| Volume | 200 to 3,700 a day needed | Small sequences reply 2.6x better; one sender fell from 2.1% to 0.7% past 150K emails | Prove by hand on 50 to 250, then scale by segments |
| Sequence length | 8+ touches (r/sales, 901) | 3 emails beat 1; returns fall steeply after 3 | 3 per channel, add channels for more touches |
| Connection note | Leave it blank | Notes cut acceptance but raise replies | Blank for Tier 3 and networking, note for Tier 1 and 2 |
| Cold call opener | "Bad time?" as pattern interrupt | 2.15% vs 11.18% permission | Permission opener by default, test your own |
| Personalization | Video or deep research per prospect | 2 meaningful facts lift; AI decoration hurts | Segment copy plus one real trigger; video for Tier 1 |
| Open tracking | Use opens to time calls or gifts | Tracking on: 4.4% vs 7.4% replies | Off; time follow-ups on replies and site signals |
| Performance pricing | "Pay only for meetings" | Disputes; guarantees on inboxing ended in $52K refunds | Define a lead as a held, approved meeting; short paid trials |

## Never

- Never send cold from the primary domain, or buy reseller inboxes on borrowed tenants.
- Never automate or scrape LinkedIn on the owner's account.
- Never fake "Re:" or "Fwd:", invent a shared connection, or claim a result the owner cannot prove.
- Never mention tracked website visits or opens to a prospect.
- Never email Germany, Canadian or Australian contacts, or UK sole traders, without a recorded consent basis.
- Never AI-voice, ringless-voicemail or cold-text US mobiles without consent.
- Never send anything the owner has not approved: messages, offers, prices. Drafts are free.
- Never let an agent answer positive replies, objections or pricing questions alone until its drafts were approved unchanged 100+ times.

## References

- [infrastructure.md](references/infrastructure.md): provider rules, setup checklist, volume, warmup, verification, monitoring, stop-loss, costs.
- [lists-and-signals.md](references/lists-and-signals.md): ICP from wins, signal ranking and freshness, signal recipes, gap plays, tiers, data sources, suppression.
- [copy-and-cadence.md](references/copy-and-cadence.md): what moves replies, verbatim templates with results, frameworks, subjects, CTAs, offers, follow-ups, multichannel, reply handling.
- [linkedin.md](references/linkedin.md): official limits, benchmarks, note decision, sequence, DMs with results, automation decision.
- [cold-calling.md](references/cold-calling.md): benchmarks, openers, pushback, gatekeepers, missed-call sequences, timing, dialers, call law.
- [discovery-and-booking.md](references/discovery-and-booking.md): speed, booking, show rates, discovery questions, qualification schema, objections, post-call follow-up, handoff.
- [benchmarks.md](references/benchmarks.md): reply rates by source and year with denominators, LinkedIn, calling, AI cases, operator numbers, diagnosis table.
- [legal.md](references/legal.md): CAN-SPAM, PECR, GDPR legitimate interest and EDPB 2026, Germany, CASL, Spam Act, phone rules, record and audit checklist.
- [ai-and-agencies.md](references/ai-and-agencies.md): AI SDR evidence, division of labor, buying an agency or setter, tool map.
- [by-seller.md](references/by-seller.md): agencies, SaaS, selling to local SMBs, industrial, enterprise, buyer roles.
- [mistakes.md](references/mistakes.md): mistake, what it cost, do instead.
- [plan-90-days.md](references/plan-90-days.md): week-by-week plan with exit checks, weekly rhythm and formulas.
- Sibling skills: `offers-pricing` (offer design, guarantees, price psychology), `launch-first-customers` (first 10 customers from a standing start), `agency-freelance` and `saas-apps` (segment-specific outbound), `email-sms-loyalty` (opt-in marketing email deliverability and flows), `paid-ads` (account-warming and retargeting ads), `organic-social` (founder content on LinkedIn), `website-conversion` (the page a reply clicks to).
