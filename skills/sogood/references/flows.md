# Worked flows

Inputs shown are the `input` object. Add `business_id` when the connection covers more than one business. Run `describe_action` once before the first write of any action: it is the source of truth for field names, and it says which tool runs the action.

## 1. Start or shape a business

**No SoGood business yet.**

1. Find the matching playbook skill in this plugin (for example `home-services`, `ecommerce-brand`, `digital-products`, `boring-businesses`) and run its first-session questions with the founder.
2. Write down, in their words: what they sell, to whom, price, how it is delivered, the first channel, and what they will not do.
3. Send them to [sogood.ai](https://sogood.ai/?utm_source=agent-plugin&utm_medium=skill&utm_campaign=ai-business-plugin) to describe the idea. Paste in the summary from step 2. The CEO agent turns it into a plan and starts the brand, site and first tasks.
4. Once the business exists, connect the MCP and continue below.

**Business already on SoGood.**

```text
read_action  getBusinessFacts                      -> positioning, products, pricing, audience
call_action  saveBusinessFacts  { ...only fields the founder stated... }
read_action  listTasks                             -> what the team is already doing
call_action  createTask  { "title": "Write 5 launch posts for Instagram", "description": "...", "idempotency_key": "launch-posts-1" }
```

`saveBusinessFacts` takes only facts the founder said; unknown fields are rejected. Use an `idempotency_key` on tasks so a retry does not create a duplicate.

## 2. Check sales

```text
read_action  getOrdersSummary     { "from": "2026-11-01", "to": "2026-11-30" }
read_action  listOrders           -> detail, newest first
read_action  getAnalyticsSummary  { "from": "2026-11-01", "to": "2026-11-30" }
read_action  getChannelMoney      -> marketplace settlements, fees and payouts (if a channel is connected)
read_action  listSubscriptions    -> recurring customers (stores can sell subscriptions)
```

- `getOrdersSummary` returns status counts, sales by currency and by channel, balance, open disputes, and how many orders lack fee data. A bare `to` date includes that whole day (UTC).
- `getAnalyticsSummary` needs both dates, at most 366 days apart. It returns visitors, pageviews, sessions, bounce rate, top pages, top referrers and tracked events (add to cart, checkout, lead), or `connected: false`.
- Report one short block: date range, revenue, orders, average order value (revenue / orders), visitors, conversion (orders / visitors), top referrer, open disputes. Say which numbers are missing instead of guessing.

## 3. Draft an ad

```text
read_action  listAdPlatforms        -> which platforms are enabled for drafts
read_action  getBusinessFacts       -> offer, audience, price
call_action  createTextAdDraft {
  "targetPlatform": "google",
  "headline": "Same-Day Gutter Cleaning",          // max 30 chars
  "additionalHeadlines": ["Free Quote in 2 Minutes", "Insured Local Crew"],
  "body": "Clean gutters, photos before and after, no mess left behind.",   // max 90 chars
  "additionalDescriptions": ["Book online today. Fixed prices, no surprises."],
  "keywords": ["gutter cleaning near me", "gutter cleaning cost"],
  "linkUrl": "https://example.com/gutters",
  "audience": { "countries": ["US"] },
  "idempotencyKey": "gutter-search-v1"
}
```

- Google needs at least 3 headlines, 2 descriptions and 1 keyword.
- Image ads (Facebook, Instagram, X, ChatGPT): `createImageAdDraft` with exactly one of `image` (an image the business already has), `generate` (makes a new image; this buys an image, so it is sensitive) or `fromLive`. `searchAdInspiration` finds live Meta ads to borrow layouts from.
- A draft is free and waits for the founder. Publishing, resuming or funding an ad is a sensitive, paid step: describe the budget and duration and get a yes. Use the `paid-ads` skill to pick the platform and budget first.

## 4. Get the business case

```text
read_action           getDeck        -> status (building or ready), link, page titles, builtAt
call_sensitive_action rebuildDeck    -> after the founder says yes; returns {queued: true}
```

Before the first deck exists, `rebuildDeck` answers `noDeckYet` and does nothing. Read the deck link and summarize the pages for the founder rather than pasting it raw.

## 5. Change the website

Copy (fast, no deploy):

```text
read_action           getSiteCopyCatalog                          -> editable keys and length caps
read_action           getSiteCopy
call_sensitive_action setSiteCopy  { "key": "hero.title", "value": "Fresh bread, delivered by 8am" }
```

Live in about a minute. Fields have length caps (for example `hero.eyebrow` is 40 characters).

Code:

```text
read_action           listCodeFiles / readCodeFile
call_action           commitCodeChanges   -> a commit on the site's own repository
read_action           checkSiteChanges    -> build and checks
call_sensitive_action deployCodeChanges   -> after a yes; live in about 75 seconds
```

Read the head again before the next commit: a deploy can add a build commit and an old head is refused as stale.

## Close the session

```text
call_action handBackToTeam { "summary": "Changed hero copy, drafted 1 Google ad, added 2 tasks." }
```

Handback runs checks. If they fail, fix the cause and hand back again. `force: true` turns failures into fix tasks for the team; use it only when the founder agrees.
