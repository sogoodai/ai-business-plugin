# Outbound for agencies and freelancers

General cold outreach infrastructure (domains, warmup, sequencers, list tools) belongs to `b2b-outbound`. This file holds what works when the product is a service. Rule from the research: fix the offer and the list before the copy, and judge on positive replies per prospect, never opens or sends.

## Benchmarks to judge a campaign

| Metric | Median | Top quartile | Source |
|---|---|---|---|
| Cold email reply rate | 3.43% | 5.5%+ (top 10%: 10.7%+) | Instantly, 2025 data, pub. Jan 2026 |
| Reply per prospect, services sellers | 4.9% | 7.1% | Smarter Outbound, 2026 |
| Positive reply per prospect | 0.79% | 1.36% | Smarter Outbound, 2026 |
| Replies that come from follow-ups | 42% | | Instantly, 2026 |
| LinkedIn acceptance | 28.5% | | Expandi, 2026 |
| LinkedIn reply to outbound message | 10.4% | | Expandi, 2026 |
| LinkedIn meetings per invite | 0.54% | | Reachium, 2026 (concentrated sample) |

Vendor datasets with different definitions: compare against one, never an average. Operator numbers for calibration: one service per campaign 1 to 2% positive vs 0.3 to 0.5% for multi-service pitches (40 pts); construction SMBs 1 positive per 260 emails vs ad agencies 1 per 120, and newer companies replied about 2x more (32 pts); 5,000+ businesses, 6 replies, 1 client (225 pts); about 1 decent client per 1,000 personalized LinkedIn messages (60 pts).

Diagnosis order (research decision rules):
1. Replies below benchmark: deliverability and targeting first, then the offer. Do not add sequence steps.
2. Replies fine, positives low: the offer or the ICP is wrong.
3. LinkedIn acceptance low: targeting and the founder's profile. Acceptance fine, no conversations: the first message after acceptance.

## The offer that gets replies: show, don't pitch

The email contains a trigger proving you chose them, one narrow proof point, one specific observation about their asset, and a low-friction next step. Best performers in the threads:

- **The audit is the whole email.** Check: website exists, ranks for "service + neighborhood", appears in ChatGPT or Siri for "service + city", complete Google Business Profile, basic schema. Send only when real gaps exist; include the actual searches where competitors show instead. No services, no credentials. Close: "thought you'd want to see this, happy to walk through what I'd fix first if you're curious." Reply rate went from 2% to 18% on the same business types and cities (r/digital_marketing, 78 pts). Scripting the searches cut each audit from 15 to 20 minutes to 30 seconds.
- **Speculative redesign, built only after a yes.** 120 manual emails in a month: about 25 replies, 10 wanted the mockup, 5 calls, 3 clients (r/agency, 84 pts). Subject: "We redesigned one of your pages. Want to see it?" Body: "We mocked up a redesigned version of one of your [product/service] pages, purely speculative, but we believe it could increase both conversions and search performance by ~30%. Should we send it over?" The bulk version (about 1,000 emails in a week) got 2 small clients: manual beat volume (32 pts).
- **Three sentences, no intro:** "your booking page errors out on mobile" / "anyone coming from Instagram can't book" / "want me to send a 2-minute video showing the fix? Free either way." (61 pts)
- **Two free fixes, then a call ask** (Reddit DMs, 200 sent, 10 replies, 5%): "I can rank you #1 on __ & ___. 2 optimizations you can do right now: 1. ---- 2. ---- Wanna do a 15-mins call?" (r/EntrepreneurRideAlong, 524 pts)
- **Narrow outcome with a deadline:** "Can I revive your dead list in the next 14 days?" instead of "email marketing services" (r/copywriting, 359 pts).
- **Real errors in their listings:** a local SEO agency emailed multi-location networks about actual Google Maps errors; good click-through, but it burns the database fast (60 pts).
- **Short can match researched for local:** subject "question about {Company}", two-line body, industry lists within driving distance; reply rate almost equal to deep research (194 pts).

Research template:
> Subject: [company] + [specific problem]
> Hi [Name], noticed [specific trigger]. For [similar client type], we [measurable result] by [mechanism]. I spotted [specific gap] in [their site, ad funnel, workflow, content]. I can send a 90-second teardown showing the two changes I'd test first. Want it?

Higher-performing Instantly campaigns used under 80 words (observational). Skip the greeting and the introduction (77 pts).

## Follow-up

- Follow-ups add information, never "bumping". Instantly: 42% of replies come after step one.
- Cadences that worked: day 0, day 3 "floating this back up", day 7 close-out (61 pts); days 1, 2, 5, 10, with interest arriving on day 5 (53 pts); multichannel with a tailored video on day 3, just over 2x lead-to-opportunity vs email or DM alone over 1.5 years (39 pts).
- Of one agency's last 20 clients, 6 came from cold email: 2 signed within days, 1 within two weeks, 2 after about two months of follow-ups (108 pts). Keep a 10 to 12 month follow-up rhythm for "not now" (72 pts).
- Outbound ramp to plan around (for an outbound agency's own sales): 2 to 7 meetings in month 1, 10 to 15 in month 2, full speed in month 3 (88 pts).

## Lists

- 100 to 250 accounts with an observable trigger per pilot, one hypothesis per segment, a volume low enough to inspect every record (research plan).
- Pretend you can email only 50 people: define title, industry, size and "the trigger that makes them need it now" (40 pts).
- 4 small segments of 300 to 600 (US, SEO or PPC agencies, 1 to 10 and 11 to 20 staff, owners only), each with its own copy (56 pts).
- Data quality: "verified" Apollo data gave 30% bounces and burned domains every 20 days; moving to waterfall verification and ESP matching took one agency from 0.8% to 5.1% reply on 130,000 emails over 4 months (129 pts). Clean exports before sending (659 pts).
- Use AI for the first line and research only; operators say it cannot write the offer (37 pts).
- Infrastructure cost for a founder doing it in-house: 5 to 10 domains at $12 a year, 15 to 30 inboxes at $3.50 a month, a sending tool at $100 to $200 a month, so $200 to $400 a month plus 5 to 10 founder hours a week (88 pts).

## Deliverability and law (2024 to 2026 changes)

- Gmail since February 2024: SPF or DKIM for all senders, valid DNS and PTR, TLS, spam complaints under 0.3%. Bulk senders (about 5,000+ Gmail messages a day) need SPF, DKIM, DMARC and one-click unsubscribe. Enforcement tightened in November 2025.
- A cold email agency with full money-back guarantees refunded 20 clients at $2,600 each ($52,000) when Google filtering changed (r/startups, 270 pts). Never guarantee what a platform controls.
- US CAN-SPAM covers B2B: truthful headers and subjects, a postal address, an opt-out honored within 10 business days.
- UK PECR: corporate subscribers can generally be emailed without consent, but sole traders and some partnerships are protected like consumers; UK GDPR still applies. ICO guidance is under review after the Data (Use and Access) Act.
- Canada CASL: express or defined implied consent; unsubscribes honored within 10 business days.
- Australia: express or inferred consent; unsubscribes within 5 working days.
- EU: national ePrivacy rules differ and can protect professional addresses; never use "B2B = legitimate interest" as a blanket rule (EDPB 2024).
- A channel that only works by breaking a platform's terms or outreach law is not a channel.

## LinkedIn

- LinkedIn prohibits bots, extensions and software that scrape or automate activity; ignored invitations and suspected automation trigger restrictions; there is no published safe daily quota. The agent researches and drafts; the founder sends by hand.
- Free accounts can add a personalized note to only 3 invitations a month, 200 characters max; Premium removes the note cap. Save notes for the highest-value prospects.
- Connection note: "Saw your point about [specific topic]. It maps closely to work we're doing with [ICP] around [problem]. No pitch, I'd like to compare notes."
- After acceptance, diagnose, don't pitch: "Thanks, [Name]. The thing I'm curious about from your [post, change, hiring signal]: are you already solving [problem] internally, or is it still on the backlog?"
- Operators: direct CEO and owner connects with no hard sell: about half accept within 8 hours (131 pts). 10 researched messages a day beat 1,000 generic in one niche: 3 design clients (188 pts). Warm for a few weeks by engaging with posts before messaging (3 threads). Trigger DMs from post likes, profile views or lead-magnet downloads (76 pts). 1,352 contacts gave 199 replies but only 2 real conversations (76 pts): count conversations.
- Writers: use the People tab to find the editors who assign work, not the top title: "I came across [company] on LinkedIn and was wondering if you were looking for any additional freelance writers. I've written for publications like [x, x and x]... Here are a few samples of my recent work: [link]." (113 pts)
- Casual DM: "Hey, I saw what you're working on, looks cool. If you ever need help with X, let me know." (50 pts)

## Video (Loom) in outreach

- Evidence is vendor case studies: Vidyard Superside 1.5% replies without video vs 6% with; Loom Intercom +19% replies. Enough to test on top accounts, not to record for every prospect.
- Permission first: "I spotted two things on [asset] that may be costing [specific outcome]. I recorded a 70-second walkthrough. Want me to send it?" Structure: 10 s on their actual asset, 25 s isolating the issue, 20 s on the fix or a comparison, 10 to 15 s on one next step (research playbook design, not a measured optimum).
- Operator script (90 to 120 s, value in the first 5 s, their homepage or LinkedIn on screen): "Hey [NAME], typically when I speak to [PROSPECT TYPE] they really struggle to [ACTIVITY]. Spending countless hours [PAIN], and pouring their budget down the drain in the process. I've worked with [COMPETITORS] so know first hand that this is a real bottleneck to [OUTCOME]. So if this sounds familiar I'd love to share how we can help you turn things around. Simply reply to this message and we'll line up a chat." (39 pts)
- Conflict: unsolicited Loom audits cost more production time than they earned for one agency, and a 27-pt commenter says critiques fail without credibility (36 pts). Rule: video for warm or high-fit accounts after a reply or an opt-in, or as day 3 of a sequence; never as the first cold touch to a cold list.

## Cold calling (local and SMB buyers)

- 50 new calls a day in a protected 4-hour block (150 to 200 a week actual) took a solo web developer to about $120,000 a year; first sale on about the 17th call, 2.5 months later; cycles later 2 weeks to 1 month (r/Entrepreneur, 1,843 pts). About 70% pickup, 2.5% sales on all dials.
- Best windows: 9 to 11:30 a.m., peak 10 to 11. A month of data: 19% connect Tuesday to Thursday 10 to 11:30 vs 9% Monday mornings and 5% Friday afternoons (480 pts).
- Opener test over 820 dials a month: "Hey this is a cold call, you can hang up but give me 18 seconds first" kept 30% past 30 seconds, vs 22% for "Did I catch you at a bad time" and 14% for an immediate pitch (480 pts).
- No voicemail: a LinkedIn request referencing the call within 5 minutes, then email the next day. LinkedIn got 14.1% responses vs 2.3% voicemail callbacks; reps who adopted it raised meetings 37% in a month (480 pts).
- The first call only qualifies and books call two; 5 of one agency's last 20 clients came from calls, signing 1 week to 6 months later (108 pts).
- Secondhand benchmark (podcast): 1 appointment per 8 local calls, half of appointments close (46 pts).

## Time-box outbound while delivering

Four threads agree on fixed blocks with a tiny quota: 2 to 3 hours at the same time weekly even if the output is "5 outreach messages or 3 follow-ups" (64 pts); Tuesday and Thursday 8:00 to 9:30 a.m., research batched in 45 minutes on Monday evening for 20 businesses; if an emergency kills a block, skip to the next one instead of squeezing it in (61 pts). Losing all clients in one month after neglecting the pipeline while busy is the classic outcome (212 pts).

## Tricks most owners miss

- Separate list quality from copy quality: test a new ICP or trigger before rewriting subject lines (research).
- A cold email stack bought before the offer works wastes money: about $2,000 in tools for 2 clients, while a manual campaign closed 3 (84 pts).
- Define a "lead" as a booked meeting when buying outbound from anyone (30 pts).
- Inbound speed: an AI step that researches the company and drafts the intro within 5 minutes of a form fill (37 pts); a follow-up drafted from the call transcript within 10 minutes (26 pts).
