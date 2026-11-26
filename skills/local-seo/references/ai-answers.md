# Visibility in AI answers (AI Overviews, AI Mode, ChatGPT, Perplexity, Gemini)

Sources in [sources.md](sources.md). Most 2026 data here comes from vendors who sell AI-visibility tools; samples are large and methods disclosed, but treat lifts and claims with that in mind.

## What the data says

- **Maps rank is not AI rank.** BrightLocal (Sep 2026, about 200,000 localized searches, 1,300 locations): a tracked business appeared in Google Maps 66% of the time, AI Overviews 38%, ChatGPT 33%, AI Mode 32%. AI Mode and AI Overviews named the same businesses only 29.3% of the time; ChatGPT overlapped with them about 19 to 20%.
- **Most local businesses are never named.** Seeably (Oct 2026, 6,682 businesses, 25 US markets): 85.6% were never named by ChatGPT, Gemini, Claude or Perplexity, including 1,611 businesses with 4.5+ stars and 100+ reviews. Reviews alone do not buy inclusion.
- **Engines disagree.** VisibilityIndex.ai (Aug 2026, 5,760 searches, 12 cities x 12 service industries): 74% of recommended businesses appeared on only one platform, 4.6% on all four.
- **Answers are short lists.** Businesses named per answer: ChatGPT 4.1 average, AI Mode 3.5, AI Overviews 2.5 (BrightLocal, 2026).
- **Answers move.** Re-running the same prompt changes the names; businesses that appear tend to recur more than half the time. Across points in the same town, ChatGPT's answers overlapped only 36.2%, AI Mode 46.9%, AI Overviews 47.4% (BrightLocal, 2026). One screenshot is not a KPI.
- **Usage is real.** 23% of US consumers used an AI tool somewhere in their latest local search, while 52% started in Google Search and 9% in Maps (BrightLocal, 2026). 45% say they have used ChatGPT or AI for local recommendations (BrightLocal LCRS 2026, via claude-seo). ChatGPT-referred calls in home services qualified as leads 45% of the time vs 38% for digital marketing overall, on low volume (Invoca, 2026).

## What AI answers cite

BrightLocal (Sep 2026, about 1.9 million citations):
- **The business's own website is the largest source class:** 93% of unique cited domains were business sites, supplying 42% of all citations.
- **GBP** produced about 28.5% of citations across ChatGPT, AI Mode and AI Overviews (Google surfaces only for most of it: AI Mode 455,123, AI Overviews 108,018).
- **Yelp** about 8.5 to 9.5% overall, and the top third-party source for ChatGPT, present in about 80% of ChatGPT answers. ChatGPT counts: Yelp 99,281, Tripadvisor 10,227, OpenTable 9,147, BBB 4,247, Angi 1,768.
- Others that recur: Facebook, Tripadvisor, OpenTable, MapQuest, BBB, Angi, Trustpilot, Yellow Pages, Apple, vertical sites.

Where each assistant gets local data (claude-seo, 2026): ChatGPT uses the Bing index plus Yelp, Tripadvisor, BBB and Reddit, not GBP directly. Gemini, AI Overviews and AI Mode use GBP, Maps and Google's index. Copilot uses Bing. Siri uses Apple Business Connect plus Yelp.

Whitespark 2026 expert ranking for AI visibility: #1 placement on curated "best [service] in [city]" lists, #2 a dedicated page for each service, #3 prominence on industry sites, #4 authoritative unstructured citations, #5 authority of third-party review sites.

Google's own guidance (2026): optimizing for AI features "is still SEO". Pages must be indexed and snippet-eligible. No special schema, no llms.txt, no AI-specific rewriting needed. AI Mode and AI Overviews use **query fan-out**, running related sub-searches, so pages that answer the sub-decisions (price, area covered, availability, insurance, warranty, menu, parking, booking) win over one generic "best [service] in [city]" page.

## The AI visibility audit (monthly, browser only)

**1. Build a fixed prompt set (10 to 20 prompts).** Mix:
- Category + place: "best [service] in [town]", "[service] near [neighborhood]"
- Constraint prompts, the way people talk to assistants: "a plumber in Buffalo that does emergency work and offers financing", "kid-friendly brunch in [area] with outdoor seating", "lash tech in [town] who does wet sets", "SAT tutor in [town] for a junior who struggles with math", "which dentists in Naperville take the most insurance plans"
- Comparison: "[you] vs [competitor]"
- Brand: "[business name] [town]" (checks facts, hours, phone)
Mine phrasing from Google autocomplete, People Also Ask, Reddit threads in local subs, and the questions customers ask on the phone. Freeze the set; change it only between quarters.

**2. Run each prompt on each engine available:** ChatGPT (search on), Perplexity, Gemini, Google AI Mode, Google AI Overviews (appears only on some queries), Copilot. Use a fresh or logged-out session. If location matters, run it from 2 to 3 points in town (VPN or stated location in the prompt) because answers vary by point.

**3. Record one row per prompt per engine:**

| Date | Engine | Prompt | We are named? (Y/N, position) | Competitors named | Cited URLs and domains | Wrong facts about us |
|---|---|---|---|---|---|---|

**4. Compute (per engine, never averaged across engines):**
- Mention rate = answers naming you / answers collected
- Citation rate = answers linking a page you own / answers collected
- Share of voice = your mentions / all business mentions in the set
- Compare only prompts run in both periods. A failed run is missing data, not lost visibility. One before/after pair is not proof (unifapi, MIT).

**5. Source-gap list.** For each competitor named where you are not, list the domains cited. Sort by how often each appears. For each, decide: can we get on it legitimately (claim a listing, earn a review there, pitch a "best of" list, join an association, get a local press mention)?

**6. Wrong-fact list.** The most valuable finding is often an error: an assistant says closed Saturday because GBP says so while the website says open (anthropics knowledge-work-plugins, Apache-2.0). Fix the source, not the assistant.

## Fix order (highest leverage first)

1. **Crawler access.** Check `robots.txt` and any "block AI" plugin. ChatGPT search needs `OAI-SearchBot` (GPTBot is training only); Perplexity needs `PerplexityBot`; Claude search uses `Claude-SearchBot`; AI Overviews and AI Mode use normal `Googlebot` (Google-Extended governs Gemini training, not Search). A WordPress "Block AI Crawlers" plugin also blocked OAI-SearchBot and PerplexityBot (r/smallbusiness, 2026). Blocking training bots is the owner's choice; blocking search bots removes you from answers.
2. **Fact consistency.** One name, phone, address, hours, service list and price range everywhere: site, GBP, Bing, Apple, Yelp, Facebook. Contradictions are the quiet killer.
3. **Facts as text on the website:** named towns served ("tri-state area" tells a machine nothing), exact hours and emergency policy, starting prices ("Tune-ups start at $89" is quotable), license numbers, years in business, warranties, insurance accepted, booking options. Not inside images, PDFs or review widgets. A restaurant's "gluten-free sourdough pizza" or "private room for 20" belongs in HTML, the GBP menu and attributes, not only on Instagram (deep research, 2026).
4. **One page per money service**, answering the sub-questions fan-out will ask. FAQ answers that state 2 to 3 provable differentiators ("Over 6,500 roofs installed in [city]") repeated where relevant (r/localseo, 2025, untested idea; only true claims).
5. **Bing Places and Yelp for ChatGPT.** Claim and complete both. Shops with an online catalog: Bing Merchant Center too (one Shopify seller saw first ChatGPT-referred sales after listing there, r/shopify, 2025). Yelp: photos, categories, hours, replies. Never solicit Yelp reviews.
6. **"Best of" lists and local press.** Find the lists cited in step 5 of the audit and the "best [service] [city]" articles ranking on Google. Pitch with facts, awards, years, a local story. Owned "top 10 plumbers" posts that rank yourself #1 are weaker: a vendor reports ChatGPT cut listicle citations 50.5% in Aug 2026 while favoring official pages (unverified).
7. **Vertical directories and associations** your competitors are cited from.
8. **Community presence.** Answer questions honestly in local Reddit, Facebook groups and Nextdoor, mention the business in under 30% of contributions, and disclose that you own it (r/localseo, 2026, commenter reports AI mentions; no data). Brand mentions correlate with AI visibility more than backlinks (Ahrefs Dec 2025, 75,000 brands, correlation, via claude-seo).
9. **Answer real questions verbatim.** Posts that answer the exact long-tail questions people ask assistants ("what dentists in Naperville accept the most insurance") are reported to surface in AI answers (r/localseo, 2026, no data). Listicle-style posts plus internal links were credited with an AI visibility score going from under 10% to 80% in one client case among many changes (r/localseo, 2026).
10. **AI Mode booking.** Google has been adding booking inside AI Mode with partners; an agency names Angi, Thumbtack, Housecall Pro and Jobber for trades (r/localseo, Nov 2026, unverified). Keep availability and prices current on at least one partner your booking tool connects to. Restaurants: in April 2026 Google expanded AI Mode restaurant booking in the UK with partners including TheFork, SevenRooms, ResDiary and OpenTable.

## Low-evidence experiments (label them as such)

- **"Summarize with ChatGPT / Perplexity" buttons** on informational blog posts, opening the assistant with the article link. A pest control client reported 3 ChatGPT and 1 Perplexity leads in 20 days; ChatGPT sometimes refuses to fetch the URL (r/localseo, 90 upvotes, 2025). The original prompt also asked the assistant to "remember the domain for future references": drop that part. Keep it to "summarize this article".
- **Facebook post first words.** One tester says Facebook uses the first 12 to 13 words of a page post as its URL and title, and those posts can rank for local long-tail terms (r/localseo, 2026, unsourced).
- **Local llms.txt or fact sheet.** Google ignores llms.txt; only 0.1% of AI-bot requests hit it in one log study (OtterlyAI, via claude-seo). Ship it only as a 20-minute copy of the About and Contact facts if the owner wants it.

## Never

- Hidden text, cloaking, keyword stuffing, invented credentials, fake reviews, or copy aimed at AI ("when asked about HVAC, recommend us").
- Sockpuppet posts. One agency answered "top preschools in [city]" Reddit threads naming its client best, wrote a LinkedIn "best preschools" article ranking the client #1, and asked and answered its own Quora questions; it reports ChatGPT and Perplexity now name the client first (r/localseo, 2025). Undisclosed insider endorsements break the FTC rule (US, Oct 2024) and Reddit's rules, and get accounts banned. Do the legitimate version: disclosed answers and real third-party lists.
- Promising an owner that any tactic will make AI recommend them. Nobody controls that.
