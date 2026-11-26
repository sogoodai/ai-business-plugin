# Sources and decision-changing counterexamples

Reviewed 16 November 2026. Original instructions and code; no third-party skill code or substantial prose copied. Platform behavior can change; recheck the relevant documentation when diagnosing that platform.

| Source | Mechanism used here | Limit or counterexample |
|---|---|---|
| [Google Analytics funnel exploration](https://support.google.com/analytics/answer/9327974?hl=en) | Entry rules, sequence and user-once counting change step membership. Reconcile them before dividing. | Open-funnel step totals can include entrants who never reached an earlier step. They are not a closed cohort's retention rate. |
| [Shopify checkout_started](https://shopify.dev/docs/api/web-pixels-api/standard-events/checkout_started) | Checkout Extensibility can emit a start on every checkout entry. Use declared identity and deduplication. | Multiple starts can be real re-entries rather than multiple people or broken transport. |
| [Shopify checkout_completed](https://shopify.dev/docs/api/web-pixels-api/standard-events/checkout_completed) | Completion usually emits on thank-you, but upsell placement and page-load failure affect emission. Reconcile records. | A completed order can lack this client event. A generic imitation thank-you page is not a Shopify order. |
| [Shopify accelerated checkout](https://help.shopify.com/en/manual/payments/accelerated-checkouts) | Wallets offer alternate checkout paths that can bypass cart steps. Inspect path eligibility. | Missing standard-cart events are not sufficient evidence of lost express purchases. |
| [Playwright assertions](https://playwright.dev/docs/test-assertions), [actionability](https://playwright.dev/docs/actionability) | Retry settled UI assertions and interact through actionable controls. | Passing HTTP or finding an element does not verify a saved order; force-clicking can hide customer-facing overlays. |
| [web.dev Web Vitals](https://web.dev/articles/vitals) | Use field distributions segmented by device when performance is a plausible mechanism. | One lab run or a bad score is not causal conversion evidence. Diagnose the observed stall or layout shift first. |

Public skill study: [Corey Haines' CRO skill](https://github.com/coreyhaines31/marketingskills/blob/main/skills/cro/SKILL.md), with its [MIT license](https://github.com/coreyhaines31/marketingskills/blob/main/LICENSE) checked directly. Its page/context assessment is useful for general page CRO. This skill adds an independently written narrower artifact: replay evidence, persisted outcome reconciliation, strict cohort comparability and an executable auditor. Studying a public skill does not establish that either skill improves model performance.

Practitioner examples were selected from an existing research cache, then checked against the linked original threads. They are failure-mode leads, not controlled results or promises:

- [Shopify abandoned-cart email report](https://www.reddit.com/r/shopify/comments/mjudd5/email_marketing_getting_854_for_every_1_you_spend/): one reported order rate uses email openers; another uses recipients. A higher percentage cannot rank those flows without a shared denominator. Reported revenue periods also do not reconcile from the post alone. No tactic or revenue claim is imported as an expected lift.
- [Webdev launch with failed signup](https://www.reddit.com/r/webdev/comments/mebyvc/my_biggest_solo_project_a_platform_where_you_can/): a visitor reported repeated validation failures; the creator suggested password strength while also noting other signups. The aggregate success count does not disprove one environment's failure. The creator's explanation remains a hypothesis until a replay isolates it.

These are mechanisms to test, not a reason to redesign every form. No benchmark is used by the auditor and none is needed to establish a reproduced broken transition.
