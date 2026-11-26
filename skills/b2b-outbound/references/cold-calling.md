# Cold calling, voicemail and the missed-call sequence

Calling is the slowest channel to run and the fastest to a conversation. Its biggest multiplier is data quality (who you can actually reach), then the opener, then volume. Sources: [sources.md](sources.md).

## Benchmarks

| Metric | Value | Source |
|---|---|---|
| Connect rate | 5.4% average; 13.3% top quartile (about 19 dials per conversation vs 8) | Gong, 300M calls, published 2024 (still current guidance; watch for staleness) |
| Connect rate | 9.1% median, 13.8% average, top 10% 34.1%+ | Lemlist, Oct 2025 to Nov 2026 (different dialers and definitions) |
| Meetings per connect | Power dialing 6.4% vs parallel 3.8% | Orum, published 2025 |
| Meetings per hour | Parallel 0.88 vs power 0.62 (individual contributors); managers 0.69 vs 0.53 | Orum 2025 |
| Callbacks | 75% arrive within 1.75 hours, 91% within 24 hours; a callback is 4x more likely to book a meeting | Orum, 2024 data published 2025 (possibly outdated) |
| Talk share on sales calls | 60% seller average; won deals 57% seller vs lost 62% | Gong, 326K calls, March 2025 |

Operator numbers for calibration:
- Solo web developer: 50 new calls a day in a protected 4-hour block (150 to 200 a week actual) plus about 15 follow-ups; reached a person about 70% of the time (local businesses); 2.5% of all calls became sales; about $120K a year. First sale took 2.5 months, around call 17; later cycles 2 to 4 weeks (r/Entrepreneur 1838).
- New caller: 2 to 3 conversations per 100 dials at first, 5 to 8 per 100 by week 8 (r/salestechniques 20).
- 73% of one seller's calls were answered by AI call screening, and 2% of those called back. Track screened calls as their own outcome (r/sales 232).
- Plumbers, 133 dials: about 1 in 6 answered, none signed. Check reachability and fit before building a calling program (r/EntrepreneurRideAlong 67).
- Secondhand podcast figure for local calling: 1 appointment per 8 calls, half of appointments close (r/agency 46).

## Openers

Gong's 300M-call comparison (2024 data):

| Opener | Success rate |
|---|---|
| "Did I catch you at a bad time?" | 2.15% |
| "How's your day going?" | 7.6% |
| Permission-based ("This is a cold call, can I have 30 seconds?") | 11.18% |
| Peer or name recognition ("Have you heard our name tossed around?") | 11.24% |

An operator's own test over 820 dials a month (r/Entrepreneur 480): "Hey this is a cold call, you can hang up but give me 18 seconds first" kept 30% of people past 30 seconds, vs 22% for "Did I catch you at a bad time" and 14% for an immediate pitch.

Conflict: several sales threads still like the "bad time" opener as a pattern interrupt (r/sales 646, 489). Rule: use the permission opener by default; "bad time" only paired with an immediate honest reason, and test it against your own numbers.

**Structure: context, own the cold call, ask for a short window, then one question.**

Permission opener (research pattern):
> Hi Priya, it's Sam from Acme. This is a cold call, but I called you specifically because {{trigger}}. Can I take 30 seconds to explain the connection, then you can tell me if it's relevant?

Peer recognition (only if true):
> We work with a few {{peer companies}}. Have you heard {{Company}} mentioned before?
> If no: "Fair enough. The reason I called is that we help {{peer type}} solve {{specific problem}}, and {{trigger}} made me think it might be relevant there too."

A full call flow an operator credits with lifting a 2% pickup-to-meeting rate (r/salestechniques 289):
> "Hi [Name], it's [Your Name] from [Company]. Have I caught you at a bad time?"
> If they ask who it is: "No worries, I'm [Name] from [Company]. Would it completely ruin your day if I told you this was a good old-fashioned cold call?" (pause)
> "Can I take 30 seconds to explain why I called? After that, if you never want to hear from me again, I'll take you off my list."
> "So I'm [Name], I [do X]. But you know, this is where you tell me you already have [X] completely sorted, and it couldn't possibly be better than what you've got."
> "Do you mind if I ask a cheeky question - what's the one thing you'd like to improve with [their pain point]?"
> "I know I said one question, but do you mind if I ask another? And is this something that's top of mind for you right now?"
> "Would it be the worst idea you've heard today if we chatted about this a little more? 15 minutes is usually enough time."

Reason, then silence (r/sales 646): say "this is", not "my name is", first name only, then "The reason I'm calling is because we're helping the big law firms in Adelaide with their property valuation needs, and I thought you might be interested too." Stop talking.

Quantified hook (r/salestechniques 20): "I can save you $12345, and I have data I can share to prove it. Can I ask for just 3 minutes of your life to discuss now?"

Qualifying opener for commodity services (energy broker, from 0 appointments on 30 calls a day to a claimed 10% close, r/salestechniques 41):
> When you set up with your electricity supplier did you ask them for a locked price for your electricity or did they just put you into a variable-rate invoice like they do with everyone else?

Then offer a 15-minute review, close with a specific time ("how about tomorrow at 12?"). If they are covered, congratulate them and spend 5 seconds asking for a referral.

Background-noise openers (r/salestechniques 69): "It sounds like you're driving, are you on hands free?" / "It sounds like you're with someone, are you in a meeting?"

Elevator line once they say yes (r/salestechniques 28): "You know (problem) well what we do is (solution) in fact, (proof)." Pause after the problem, end on the proof, stop talking.

Delivery: rehearse slower than feels comfortable and replace "um" with silence (r/salestechniques 81). Reuse the email research as the call script: "I actually sent you a note yesterday about ___." Flag any turn of yours over 40 words; it shows up in nearly every bad call (r/salestechniques 30).

## Pushback in the first minute

| They say | Reply |
|---|---|
| "I'm busy" | "Totally understand. Is there a better time this week, or should I send a two-line email instead?" |
| "Just send me an email" | "Will do. So I send something useful, is [the problem] on your plate this quarter or not really?" |
| "We already use [competitor]" | "Oh nice! How are you finding it?" then "If you don't mind me asking, what do you appreciate the most in a software like this?" (r/salestechniques 60) |
| "Not interested" | "Fair enough. Is that because [the problem] isn't a priority, or you've got it covered?" Ask once, then let go |
| "How did you get my number?" | Name the actual source, offer to remove them, do it |
| "Send some info / leave a card" | Admit you are bad at waiting for callbacks and ask for 30 more seconds (r/salestechniques 30) |

Never argue past a second no. Log the reason; no-reasons tell you more about the offer than meetings do. (Table partly adapted from coreyhaines31 sales-enablement skill, MIT.)

## Gatekeepers and routing

- Ownership check, then a real referral (r/salestechniques 20): "Hi Joe, are you still in charge of (your CRM/insurance/maintenance) or does someone else on your team handle that?" Then to the named person: "Hi Mark, I was just talking to Joe and he said you handle (the CRM) for your team. Is now a bad time?"
- Assistants: name, company, who you want and one line of why, then ask their advice: "Is Priya the right person for this, or is that someone else?"
- Gatekeeper opener for small offices (r/DigitalMarketing 124): name, company, what you do in three words, then "I was calling to talk about (what you sell), who's the best person to talk to?"
- Industrial buyers: start with engineering or the function owner and let their recommendation reach procurement (r/salestechniques 76). Take the lower referral: a weak VP call produced a referral to a manager who championed a GBP 5.3M ACV deal (r/sales 602).
- Multithread from a no: "Hey, I spoke with [Name] earlier today. He mentioned you're focusing on [Project/Priority] right now..." (r/salestechniques 16).

## The missed-call sequence

No answer is the normal outcome. What happens in the next 5 minutes decides whether the dial was wasted.

**Option A, no voicemail (r/Entrepreneur 480):** call; if no answer, send a LinkedIn connection request with a note referencing the call within 5 minutes; email the next day. All three touches within 24 hours. LinkedIn notes got 22 of 156 responses (14.1%) vs 7 of 310 voicemail callbacks (2.3%). Reps who adopted it raised meetings 37% in a month.

Note wording (pattern): "Just tried you on the phone about {{trigger}}. Easier to connect here. {{one-line reason}}."

**Option B, voicemail plus recap email (coreyhaines31 sales-enablement, MIT):** 20 to 30 seconds, name, one specific reason, "I'll send you a note too", then send the email within minutes with the subject "my voicemail".
> Hi Priya, Sam from Acme. I'm calling because you're scaling the SDR team, and I had one idea on keeping new reps' lists clean before they start sending. I'll send a short email with it. Again, Sam from Acme.

**Option C, first live dial on day 8 (r/salestechniques 16, claims 14 to 18% callbacks on warm-ish leads):** day 1 LinkedIn request, no note; day 2 20-second voicemail; day 3 email "Left you a quick voicemail yesterday, wanted to follow up..."; day 5 LinkedIn message; day 8 dial; day 14 email "Happy to close the loop if the timing isn't right, just let me know." The original used ringless voicemail, which the FCC treats as a call under the TCPA: in the US use a normal voicemail on an attempted call instead.

**Persistence wins on high-value contacts:** found a VP's number, left a voicemail, called again the next day and reached him (r/sales 649). Plan 3 attempts per contact on different days and times.

**Callbacks interrupt everything.** Route them to whoever is free, at once. 75% come within 1.75 hours.

**A short SMS with the rep's name before the call** reportedly raised answer rate 23% (r/LeadGeneration 29, unclear metric). US texting to mobiles needs consent; do not use it cold in the US.

## Timing, volume and dialers

- Windows that operators measured: 19% connect Tuesday to Thursday 10:00 to 11:30 vs 9% Monday morning and 5% Friday afternoon (r/Entrepreneur 480); 9:00 to 11:30, best 10 to 11 (r/Entrepreneur 1838). Industrial ops buyers: avoid Monday 8 to 12 (r/salestechniques 19). Test your own buyers by hour.
- Fewer, better dials: one rep cut from 100 to 200 dials a day to 10 to 30 researched ones and reported 2x output on half the hours (r/sales 466). Another cut from 140 to 84 dials a day by removing people who would never buy: meeting conversion up about 23%, no-shows nearly disappeared (r/salestechniques 19). A rep spending 3 to 4 days a week on research for 20 cold and 20 warm calls reported 75%+ answer and 20%+ meetings (r/sales 232).
- Daily rhythm: 10 to 15 calls a day, each with a reason (leadership move, new legislation, obvious need) (r/sales 1042). A late block at 15:15 to 17:15 in this order: past clients, then pipeline, then new business (r/salestechniques 98).
- Power dialer for narrow, senior, high-value lists; parallel dialer only for large, legally clean lists where throughput dominates (Orum 2025). Mobile numbers connect far better than switchboards but are the most expensive field: buy them for Tier 1 only.
- Phone data first: fixing direct dials can double conversations before any script work (Gong's connect gap is 5.4% vs 13.3%).

## Compliance for calls (see [legal.md](legal.md))

- US: scrub against the National Do Not Call Registry and your internal DNC list. Enriched "mobile" numbers are often personal cells, which the rules protect.
- AI-generated voices count as artificial voices under the TCPA (FCC, February 2024): AI-voiced calls to cell phones need prior express consent, written for marketing. Damages run $500 to $1,500 per call. Use AI voice only for inbound and requested callbacks.
- Record calls only where every party's jurisdiction allows it; some US states and many countries need all-party consent.
- Germany: B2B cold calls need presumed consent (a concrete reason to believe they would welcome the call). UK: screen against the TPS and CTPS for marketing calls.

## Tricks most owners miss

- The first call only qualifies and books call two. 5 of one agency's last 20 clients came this way, signing 1 week to 6 months later (r/agency 108).
- A no-answer is a LinkedIn note, not a voicemail, when the buyer is active on LinkedIn.
- Track openers by how many prospects stay past 10 and 30 seconds, by industry.
- Events beat booths: a briefed rep walking the floor gets 20 to 40 conversations in 2 days and 5 to 10 meetings; warm accounts by email and LinkedIn before, call the engagers after (r/b2bmarketing 28).
- Physical mail breaks silence on big accounts: a printed, pen-signed one-page note to a CFO timed to a board meeting, listing 3 blockers in the buyer's words, got a call from the EA the next morning after 97 days of silence (r/sales 4270, viral and possibly embellished). The ask: "Give me a 10-minute 'no-slides' call this week and I'll walk you through how we de-risk all three without changing price. If I can't, I'll write the breakup email for you."
