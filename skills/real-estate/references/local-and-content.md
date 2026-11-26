# Google profile, local content, social and AI answers

Depth on Google Business Profile, review math, citations and AI visibility lives in `local-seo`; content systems in `organic-social`; ad accounts in `paid-ads`. This file keeps only the real estate angles.

## Google Business Profile for agents, teams, PMs and LOs

- **Local ranking is relevance, distance and prominence; reviews feed prominence** ([Google](https://support.google.com/business/answer/7091)). Portals own broad "homes for sale" search; the map pack for "realtor [city]", "property management [city]" and "mortgage lender near me" is winnable.
- **Individual agent profiles:** Google allows practitioner profiles; check your broker's policy and keep the name exactly as licensed. No keyword stuffing.
- **Neighborhood language in reviews is the real estate edge.** For "[neighborhood] realtor" queries, an agent whose reviews name the neighborhood can outrank one with more generic reviews; measure the share of reviews naming a neighborhood vs the top 3 competitors (UnifAPI agent-reputation-benchmark, MIT, a heuristic, not a measured ranking factor). Ask clients to mention the specific thing you did and where.
- **Velocity beats lifetime total.** A stale count loses to a competitor collecting reviews every month (same skill; `local-seo` has the review-gap math).
- **Ask after visible value events:** offer accepted, closing, a hard problem solved. One buyer couple posted a review right after offer acceptance without being asked (r/realtors 1748, 2025).
- **Schema:** RealEstateAgent for agents and brokerages (there is no RealEstateBrokerage type), Person for the agent, RealEstateListing for listings, Event for open houses (claude-seo, MIT).
- **Property managers:** owner leads come overwhelmingly from Google search and maps (88.4% in one agency's 31-company dataset, 2026, selection bias). The PM profile, service pages and reviews from owners (not just tenants) are the core asset.

## Neighborhood and relocation pages

- **Score before writing:** opportunity = intent x demand x winnability, each 1.0, 0.5 or 0.2. "Moving to [neighborhood]" and "[neighborhood] vs [neighborhood]" are high intent and thin on portals; skip queries Zillow already answers well; up-rank prompts where AI answers cite no local source (UnifAPI neighborhood-guide-opportunity, MIT).
- **Write only where you have unique local evidence:** sold-price patterns, commute times, new development, HOA quirks, flood or insurance facts, photos you took. Google warns that mass-produced low-value AI pages can violate its scaled content abuse policy; do not spin out "[city] realtor" pages by swapping place names ([Google](https://developers.google.com/search/docs/fundamentals/using-gen-ai-content)).
- **Fair housing guard:** describe places and amenities (parks, transit, commute, named schools and their boundary maps), never who lives there or who it suits. Avoid "safe", "family-friendly neighborhood", demographic descriptions. See [compliance.md](compliance.md).
- **Negative-angle relocation articles travel.** "10 things you should know before moving to Seattle" drew hundreds of comments and years of referral leads from agents elsewhere; the suggested paid version is "10 reasons not to move to [city]" with how locals handle each (r/marketing 604, 2024).
- **Answer the questions prospects search after hearing your name:** "Why did this listing reduce?", "What does $X buy in these three neighborhoods?", "What inspection issue killed the last deal?", "What are sellers conceding right now?" (research synthesis, 2026).

## AI answers

- Google: generative features run on core Search ranking; `llms.txt`, special AI files, artificial chunking and manufactured mentions are not needed ([Google](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)). FAQ rich results stopped showing on 7 May 2026 ([Google updates](https://developers.google.com/search/updates)).
- Third-party mentions matter for ChatGPT. An agency client said 2 of her last 5 clients found her through ChatGPT; in about 15 test prompts she appeared through mentions on local blogs, forums and Zillow discussions, while the agency's owned-channel work barely registered (r/DigitalMarketing 94, 2026; causation not established). Earn mentions in local press, community forums, school and nonprofit pages, and portal reviews.
- Run the prompts a mover would ask ("best realtor for first-time buyers in [city]", "how to choose a property manager in [city]") monthly and log who is cited (`local-seo` has the method).

## Short video that agents actually sustain

- **Format:** say the client's question in the first two seconds with no intro or name, answer in one sentence, spend 15 to 25 seconds on the reason or caveat, end abruptly without "follow for more" (the poster's looping claim is unverified) (r/realtors 174, 2026).
- **Topics:** the last 20 questions clients asked you, for example "Do I need to fix the bathroom before listing", "What does earnest money actually do", "Why did this house sit for 90 days" (same thread).
- **Batching:** 8 to 10 videos in about 90 minutes; same shirt, phone on books at eye level, window in front of you; read the script once, then say it in your own words. Budget about 40 minutes per finished video including editing: 12 videos a month is about 8 hours (same thread).
- **Edit checklist:** burned-in subtitles, cut every pause, a cut or angle change about every 3 seconds, on-screen text hook for the first 2 seconds matching the spoken hook (same thread).
- **Per platform:** hook in the first caption line for Reels, a search-style title for Shorts, on-screen text that carries the whole point on TikTok (same thread).
- **Paid reach:** boosting real estate videos at about $5 a day built local awareness when lead-gen campaigns failed (r/realtors 1200, 2021). Run under the housing special ad category.
- **Social is credibility, not the first source.** 41% of prospective buyers say social presence makes them more likely to hire, but social is the first source for only 4 to 5% (Zillow 2025, 2026). KPI: profile visits, branded search, direct inquiries, assisted appointments, not followers.
- **Branding first is a trap for new agents.** One agent spent six months on team name, website and business cards and earned nothing (r/realtors 184, 2022).

## Community groups and events

- A local Facebook group plus real events, for newcomers with no local friends: 35 sales in 2025 (r/realtors 230, 2025). Mechanics in [lead-sources.md](lead-sources.md#sphere-and-past-clients).
- Local newsletters sell their best ad slots to real estate, healthcare and financial services because the lifetime value is high and decisions are local (Naptown Scoop, $300,000 a year from ads at 21,000 subscribers; r/Newsletters 36, 2024). Sponsoring a trusted local newsletter can beat your own.

## Billboards and signs

- Copy is two or three words a driver reads in about 3 seconds: a provable claim such as "500 homes sold" (r/marketing 604, 2024). Test the idea on Meta at about $5 a day first (same thread). Any "#1" claim needs a defined metric, area and period.
- Commercial leasing: flying V signs at centers and signs in vacant windows generate "a ton of calls", 75% going nowhere; screen fast (r/CommercialRealEstate 133, 2026).
