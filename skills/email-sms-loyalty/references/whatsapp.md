# WhatsApp Business

Where customers already live on WhatsApp (most of the EU outside the Nordics, Latin America, India, Indonesia, the Middle East, Africa), it replaces SMS for both service and marketing. In the US and Canada it rarely does. Use it as a consented, conversational channel, not "SMS with read receipts".

## App vs Platform

| | WhatsApp Business app | WhatsApp Business Platform (API, via a BSP or Cloud API) |
|---|---|---|
| Fits | Solo or small team, a few hundred contacts | Automation, multiple agents, CRM, templates at scale |
| Cost | Free app | Per delivered template message (below) plus BSP fees |
| Broadcast | Broadcast lists only reach people who saved your number | Approved templates to opted-in users |
| Use | Replies, catalog, quick replies, labels | Cart, reminders, replenishment, campaigns |

## Pricing mechanics (Meta, checked 13 November 2026)

- **Per delivered message since 1 July 2025**, by template category (marketing, utility, authentication) and the recipient's country code. User-to-business messages are free.
- **Customer service window:** 24 hours after the customer's last message, free-form replies are allowed. Outside it, only approved templates.
- **Changes effective 1 October 2026:** service messages are now charged after the first **1,000 free per month per phone number**; **utility templates inside an open service window are now charged** (free from July 2025 to September 2026). Eligible government and non-profit organizations keep free service messages through 31 December 2027.
- **Free entry point:** a conversation started from a Click-to-WhatsApp ad or Page button opens a window up to **7 days** in which marketing, utility, authentication and service messages are free. Convert inside it, and ask for marketing opt-in in chat.
- **Volume tiers** lower utility and authentication rates per market as monthly volume grows; marketing has no tiers.
- **Template quality** is rated green, yellow or red from blocks, reports and read rates. Yellow or red templates risk pausing; messaging limits start at 250 unique users per 24 hours and step up to 2,000, 10,000, 100,000 and unlimited with quality (coreyhaines31 whatsapp, MIT, citing Meta docs).
- **US numbers:** coreyhaines31's file (Oct 2026, citing Meta) reports marketing templates are not delivered to US numbers; North America is otherwise billed regional rates. Verify on the live docs before planning US WhatsApp marketing.

## Rates by country, USD per delivered message (rate card effective 1 October 2026)

| Market | Marketing | Utility | Authentication | Service over free tier |
|---|---|---|---|---|
| India | $0.0118 | $0.0014 | $0.0014 | $0.0014 |
| Brazil | $0.0625 | $0.0068 | $0.0068 | $0.0068 |
| Mexico | $0.0397 | $0.0085 | $0.0085 | $0.0085 |
| Rest of Latin America (countries without their own rate; Argentina, Chile, Colombia and Peru have their own rows on Meta's card) | $0.0740 | $0.0113 | $0.0113 | $0.0113 |
| Indonesia | $0.0411 | $0.0250 | $0.0250 | $0.0250 |
| UK | $0.0635 | $0.0220 | $0.0220 | $0.0220 |
| Germany | $0.1365 | $0.0550 | $0.0550 | $0.0550 |
| North America | $0.0250 | $0.0034 | $0.0034 | $0.0034 |

Source: WACRM transcription of Meta's 1 October 2026 USD rate card; Meta's page confirms the directions: Mexico marketing up 1 Oct 2026; Spain, Italy and UK marketing up 1 Jul 2026; France marketing down 1 Jan 2026; India marketing up 1 Jan 2026; Colombia utility up and Argentina utility down 1 Oct 2025; Brazil billed in BRL since 1 Jul 2026. Spain, France, Italy, Colombia and Argentina figures were not retrievable in this pass; one third-party table lists Argentina marketing at $0.07107 (SleekFlow, undated). **Fetch the live rate card at execution time; Meta changes rates quarterly.**

Budget math:

```
campaign cost = recipients x marketing rate (+ BSP fee)
break-even conversion = cost per message / (AOV x contribution margin)
  Germany: $0.1365 / ($60 x 40%) = 0.57% of recipients must buy
  India:   $0.0118 / ($15 x 40%) = 0.20%
  Mexico:  $0.0397 / ($30 x 40%) = 0.33%
```

Compare with Chatarmin's 2026 ecommerce cohort: 12.0% click and EUR 1.03 attributed revenue per campaign message (vendor attribution, 24-hour window). In Germany a marketing send must convert well above SMS-level rates to pay.

## Playbooks

**Order of build:** utility and service first (order confirmation, shipping, booking confirmation, reminders), conversational help, then one narrowly segmented marketing template. Sending useful order updates before an offer raised offer conversion from 0.17% to 0.37% and return on messaging spend from 1.36x to 2.5x in a 20,000-customer A/B test (Spur, Golden Tree, 2026). Do not disguise marketing as utility to get the cheaper rate: Brazil marketing costs about 9x utility, India about 8x, and Meta reclassifies or rejects mixed templates.

**Cart recovery** (coreyhaines31 whatsapp, MIT): marketing template 45 to 60 minutes after abandonment, only with WhatsApp marketing opt-in; buttons [Finish checkout] [I have a question] (the question button opens a service window); optional 24-hour second touch only if the first was unread or unclicked, discount held until then; stop on purchase, opt-out or 48 hours.

**Welcome from a Click-to-WhatsApp ad:** pre-filled first message ("Hi! I'd like my 15% welcome code"), then "Here's your code WELCOME15. What are you shopping for today?" with 2 to 3 category reply buttons; ask for marketing opt-in in chat; convert inside the free entry window (MIT source above).

**Replenishment and win-back:** "Your [product] usually runs out around now. Want us to set aside a refill?" [Yes, reorder] [Not now] [Stop promotions]; "Not now" suppresses 30 days; max 1 to 2 marketing sends a month.

**Services (salons, clinics, tutors, trades):** booking confirmation and reminder as utility templates, reschedule by reply, gap-fill offers as marketing to opted-in clients only. In LatAm and Spain a reply on WhatsApp is often the booking itself; route any message with a date, service or price question to a human or the booking tool at once.

**Format:** bubbles of 1 to 3 sentences under about 60 words; brand in the first line; up to 3 reply buttons (20 characters each) or a list of up to 10 rows; hand off to a person on the keyword "agent" or after two bot misses, and say when they will reply (MIT source above).

## By region

- **EU:** WhatsApp counts as electronic mail for ePrivacy purposes; marketing needs prior consent per channel. German rates are the highest in Europe; reserve marketing templates for high-AOV or high-intent segments and lean on free entry windows from ads.
- **Latin America:** WhatsApp is the default customer channel. Mexico is cheap enough for regular campaigns; "Rest of Latin America" marketing at $0.074 is pricier than Brazil. Teams often run service and sales entirely in chat; measure booked-from-reply rate, not opens.
- **India:** the cheapest marketing rate in the table and near-free utility. Volume is not the constraint; template quality and blocks are. Keep marketing to 1 to 2 a month per person, and use utility for genuine order and appointment events.
- **Education:** WhatsApp and Facebook groups by profession and country worked for ESL tutors (free 15-minute check, then 4 or 8-week packages, 34-pt comment); WeChat parent groups play the same role for mainland Chinese families (7-pt comment).

## Measure

Reply rate, booked-or-ordered-from-reply rate, click, opt-out and block rate, template quality, and gross margin per message. Never quote the folklore "98% open rate"; Chatarmin measured 79.6% weighted and 72% median in 2026.
