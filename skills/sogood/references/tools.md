# SoGood MCP reference

Source: SoGood MCP server code and live checks, November 2026. The live catalog wins: run `search_actions` and `describe_action`.

## Endpoints

| URL | For | Tools |
|---|---|---|
| `https://mcp.sogood.ai/mcp` | Any MCP client; used by this plugin | 5 generic tools over the full action catalog |
| `https://mcp.sogood.ai/mcp/claude` | Claude directory connector | Area tools (`commerce_read`, `website_write`, `ads_sensitive`...) |
| `https://mcp.sogood.ai/mcp/openai` | ChatGPT apps | Area tools, without money-moving actions |

All three use the same OAuth sign-in at sogood.ai. Streamable HTTP, stateless, JSON responses (no SSE). Up to 10 messages per batch, 512 KB per request. Long results are cut at about 40,000 characters with a `truncated` note and a smaller page size to retry with.

## Catalog by area

The catalog is an allowlist of SoGood's own API actions (about 290). Main areas, with the actions you will use most:

| Area | Read | Write | Sensitive (ask first) |
|---|---|---|---|
| Business facts and knowledge | `getBusinessFacts`, `listKnowledgeDocuments`, `getKnowledgeDocument` | `saveBusinessFacts` | |
| Team and tasks | `listTasks`, `getTask`, `listThreads`, `listThreadMessages`, `getCurrentSprint` | `createTask`, `updateTask`, `postThreadMessage`, `answerTask` | `deleteTask` |
| Store | `listProducts`, `getProduct`, `listVariants`, `listOrders`, `getOrdersSummary`, `listCustomers`, `listSubscriptions`, `listDisputes` | `createProduct`, `updateProduct`, `updateVariant`, `updateOrder` | `createRefund`, `cancelSubscription`, `fulfillOrderShipment`, deletes |
| Website | `getSiteCopy`, `getSiteCopyCatalog`, `listCodeFiles`, `readCodeFile`, `getAnalyticsSummary`, `listWebsiteErrors` | `commitCodeChanges`, `createBlogPost` (draft), `updateBlogPost` | `setSiteCopy`, `deployCodeChanges`, publishing a post |
| Ads | `listAdPlatforms`, `listAdDrafts`, `listAds`, `getAdMetrics`, `searchAdInspiration` | `createTextAdDraft`, `createImageAdDraft` (with an existing image), `updateAdDraft`, `pauseAd` | `publishAd`, `resumeAd`, `topUpAd` |
| Social | `listSocialAccounts`, `listSocialPosts`, `getSocialPostMetrics` | `createSocialPostDraft` | `createSocialPost`, `approveSocialPost`, `unpublishSocialPost` |
| Inbox | `listEmailThreads`, `listMessagingConversations` | `createEmailReplyDraft` | `sendEmail`, `replyEmail`, `sendEmailReplyDraft` |
| CRM | `listContacts`, `listDeals`, `listCompanies` | `createContact`, `createDeal`, `updateDeal` | deletes |
| Business case | `getDeck` | | `rebuildDeck` |
| Account | `listCredits`, `creditsHistory`, `getPlanFeatures` | | |

Not in the catalog: buying credits, changing the plan, wallet credits, pausing or deleting the business, Stripe account changes.

## How sensitive actions work

- An action is sensitive when it sends, publishes, deletes or spends. `call_action` refuses it with `wrong_tool` and names `call_sensitive_action`; nothing runs.
- Some actions are sensitive only in some cases (publishing a blog post, removing a variant, deleting files in a code commit, approving a task). `call_action` answers `428 founder_confirmation_required`; ask the founder, then repeat on `call_sensitive_action`.
- There is no second server-side approval. The founder's yes in chat, plus your client's approval prompt, is the gate. Keep that prompt on.
- Every write is logged before it runs. If logging fails, the write does not run (`audit_unavailable`).
- Records you create are tagged "Made by MCP" in the dashboard.

## Errors

| Error | Meaning | Do |
|---|---|---|
| `wrong_tool` | Read on a write tool, or sensitive on `call_action` | Use the tool it names |
| `wrong_business` | That business is not on this connection | Use one listed in the server instructions |
| `business_required` | Several businesses, no `business_id` | Pass `business_id` |
| `business_removed` | The founder removed it from the connection | Stop; ask the founder |
| 401 "disconnected in SoGood" | Connection revoked | Reconnect |
| 428 | Needs the founder's confirmation | Ask, then `call_sensitive_action` |
| 402 `mcp_daily_cap` / `insufficient_credits` | Daily limit or credits reached | Tell the founder; do not retry in a loop |
| 409 on a task or code write | Stale read | Read again, then retry once |
| 503 | A safety check is down | Nothing ran; retry later |

Field names vary between actions (`id`, `contact_id`, `draftId`; `idempotencyKey` on ads, `idempotency_key` on tasks). `describe_action` settles it.
