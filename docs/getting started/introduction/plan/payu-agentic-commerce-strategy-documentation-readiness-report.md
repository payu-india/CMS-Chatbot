---
title: '# PayU Agentic Commerce: Strategy & Documentation Readiness Report'
deprecated: false
hidden: true
metadata:
  robots: index
---
# PayU Agentic Commerce: Strategy & Documentation Readiness Report

**Prepared:** 2026-09-28
**Status:** Strategy / Research — No repository changes made
**Purpose:** To assess whether and how PayU Developer Docs should support Agentic Commerce, and to propose a phased implementation path

***

## 1. Executive Summary

PayU is further along the path to Agentic Commerce than it appears. The capabilities exist. What is missing is the documentation, structure, and framing that would allow an AI agent — or the developer building one — to discover and use those capabilities reliably.

**The critical finding:** A minimum viable agentic commerce journey exists today using PayU's Payment Links API and existing OAuth 2.0 authentication. An AI agent can authenticate programmatically, create a payment request, share it with a customer, receive a webhook on completion, and verify the transaction. This is a complete, RBI-compliant agentic payment loop. It is not documented as such anywhere in the repository.

**The strategic gap is narrative and architecture, not capability.**

India's regulatory environment (mandatory 2FA for customer payments) actually clarifies PayU's agentic path rather than blocking it. The human-in-the-loop redirect model — where the agent creates the payment request and the customer completes it on a hosted, 2FA-enabled page — is both RBI-compliant and the dominant global pattern adopted by Stripe, Shopify, and others. PayU's existing flow fits this model precisely.

The competitive context is urgent. Stripe has a live MCP server and Agent Toolkit. Visa and Mastercard have announced agent credential frameworks. Google has published the A2A protocol. `llms.txt` is becoming a baseline expectation for any developer-facing platform that wants AI coding assistants to generate correct integration code. Developers building agentic commerce flows will reach for Stripe first, not because Stripe's payments are better, but because Stripe's documentation tells the agent story and PayU's does not.

**Recommended first action:** Do not wait for new API capabilities. Write the agent integration story using what exists, restructure the IA to surface it, add `llms.txt`, and expand the Remote MCP server with two additional tools (payment status verification and transaction check). These four actions require no Engineering dependencies and directly unlock the MVP journey.

***

## 2. What Agentic Commerce Means for PayU

Agentic Commerce is not a single new product. It is a new class of caller for PayU's existing payment infrastructure — one that is programmatic, non-human, and designed to operate within a broader AI-driven workflow.

### From Each Stakeholder's Perspective

**The Merchant**
Today, a merchant integrates PayU by building a checkout form, handling redirects, and writing webhook handlers. In an agentic world, the merchant registers their payment capability once — via an MCP server, an OpenAPI spec, or a simple Payment Link configuration — and AI systems (their own chatbot, a third-party shopping agent, a voice assistant) can invoke that capability on their behalf without the merchant writing new integration code for every channel. The merchant's question shifts from "how do I integrate PayU into my checkout?" to "how do I make my PayU integration accessible to AI agents?"

**The Developer**
For the developer building an AI agent or AI-powered merchant application, PayU's APIs need to behave predictably under programmatic, non-human invocation: idempotent requests, machine-readable errors, clear state transitions, async-safe status checking, and OAuth-based machine-to-machine authentication. The developer is not reading docs at a terminal — they are prompting an AI coding assistant that reads the docs on their behalf, or building an LLM workflow that calls PayU directly at runtime. Documentation must be structured for both audiences.

**The AI Agent**
An AI agent interacts with PayU as a set of callable tools with defined inputs, outputs, states, and error conditions. The agent does not understand product marketing or narrative explanations. It needs to know: what operation am I authorized to perform? What are the required parameters? What constitutes success? What states can a payment be in? What should I do if this call fails? If the documentation does not answer these questions in a structured, queryable form, the agent will either fail, hallucinate, or call the wrong endpoint.

**PayU**
Agentic Commerce represents a new distribution channel. When a developer builds an AI assistant that can initiate PayU payments, every user of that assistant becomes a potential PayU transaction. PayU's acquisition model has historically been direct developer integration. Agentic Commerce adds a layer above: developers who build payment-capable AI agents are integrators even if they never write a traditional checkout form. This changes the developer experience goal from "first transaction in \< N days" to "first agent-initiated transaction in \< N minutes" — a much tighter loop enabled by MCP tooling and structured documentation.

**The End Customer**
The customer interacts with an AI assistant — a chatbot, a voice agent, or a co-pilot within a merchant's app. They express an intent: "I want to buy this," "Book me a slot," "Renew my subscription." The agent handles the order context. A payment link (or a checkout URL) arrives in the conversation. The customer completes payment on a familiar, hosted page with the payment method of their choice and the 2FA step they expect. They do not experience "AI-initiated payment" as anything different from clicking a link — which is precisely what makes this model safe and viable in India today.

### Realistic End-to-End Scenario

A customer is using a merchant's WhatsApp-based ordering bot powered by an LLM:

> Customer → "I want to reorder my usual protein powder, 2 kg"

The flow that follows:

```
Customer
  → tells WhatsApp bot (LLM agent) their intent

AI Agent
  → retrieves product SKU and price from merchant catalog
  → checks customer's previous order history (udf fields from prior PayU transaction)
  → calls POST /payment-links (PayU API) with:
       amount = ₹1,499
       description = "Protein Powder 2kg – Reorder"
       customer.phone = +91-XXXXXXXXXX
       invoiceNumber = "ORD-{merchant_ref}"
       udf1 = "whatsapp_bot_session_id"
  → receives Payment Link URL in response

Merchant
  → their server holds the OAuth client credentials
  → their webhook handler is registered at notify_url

PayU
  → creates Payment Link
  → returns URL to agent
  → when customer pays: fires webhook to notify_url with payment status
  → payment page handles UPI/card + 2FA (RBI-compliant)

Payment Method
  → customer taps UPI in the payment link
  → completes ₹1,499 payment with UPI PIN (2FA satisfied)

Payment Confirmation
  → PayU fires notify_url webhook (form-urlencoded POST)
  → merchant server verifies hash, updates order status
  → agent calls GET /payment-links/{invoiceNumber}/transactions
  → confirms status = "success"

Post-payment
  → agent sends WhatsApp confirmation: "Your order is placed. Delivery in 2-3 days."
  → merchant triggers fulfillment
```

### What PayU Supports Today, What Requires What

| Step                                                | Status              | Notes                                                                                 |
| --------------------------------------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| OAuth 2.0 client_credentials for Payment Links      | **Supported today** | Documented in `api-auth-token.md`                                                     |
| POST /payment-links (programmatic creation)         | **Supported today** | Documented in `api-create-share.md`                                                   |
| GET /payment-links/{id}/transactions (status check) | **Supported today** | Documented in `api-cancel-status.md` + `api-transactions.md`                          |
| Webhook on payment completion (notify_url)          | **Supported today** | Documented in `callbacks-webhook-reference.md`                                        |
| Customer-facing payment page with 2FA               | **Supported today** | PayU hosted checkout                                                                  |
| udf1-5 for order/session context                    | **Supported today** | Part of standard Payment Links parameters                                             |
| Documented as a unified agent flow                  | **Not documented**  | No end-to-end agent guide exists                                                      |
| Async coordination pattern (webhook + poll)         | **Not documented**  | No agent-specific retry or polling guide                                              |
| invoiceNumber idempotency guarantee                 | **Unconfirmed**     | Behaviour exists but not documented as a contract — requires Engineering confirmation |
| JSON webhook payloads                               | **Not supported**   | Webhooks are `application/x-www-form-urlencoded`                                      |
| Idempotency keys (`X-Idempotency-Key`)              | **Not supported**   | Not documented for any PayU API                                                       |
| Agent identity tagging on transactions              | **Not supported**   | No `agent_id` or `delegation_id` field                                                |
| Spending controls / budget limits for agents        | **Not supported**   | Requires new product capability                                                       |
| Redirect-free payment capture                       | **Not supported**   | Regulatory constraint: RBI 2FA requirement                                            |

***

## 3. Current Industry/Competitor Landscape

### What Is Already in Production (CURRENT / ADOPTED)

**Stripe** is the most technically mature payment platform for agentic use cases. Their `@stripe/agent-toolkit` NPM package exposes Stripe operations as LLM tool definitions compatible with OpenAI, Anthropic, LangChain, and Vercel AI SDK. Their official `@stripe/mcp` server exposes 18+ operations (payment intents, customers, refunds, invoices, subscriptions) via MCP and is actively maintained. Stripe also adopted `llms.txt` early, meaning AI coding assistants consistently generate correct Stripe code. Stripe's primary agent pattern — create a Payment Intent or Payment Link and return the URL to the user — is structurally identical to what PayU's Payment Links API already supports.

**Shopify's Storefront API** (GraphQL) is agent-compatible by design: public tokens allow unauthenticated product browsing, and the cart → checkout flow is fully programmable. Shopify was an OpenAI Operator launch partner (January 2025), optimised for browser-automation checkout completion. Shopify Sidekick is merchant-facing (admin agent), not customer-facing.

**OpenAI Operator** (January 2025) uses browser automation — it fills checkout forms the way a human would. This means it works with _any_ checkout, including PayU's hosted checkout, without PayU needing to do anything. The limitation is fragility: screen scraping breaks when UI changes.

**MCP for commerce** has a growing ecosystem. Stripe's official server is the reference implementation. Community servers exist for Shopify, PayPal, and Square. The pattern is consistent: MCP server holds API credentials, exposes operations as named tools, returns structured JSON.

### What Is Announced but Not Fully Deployed (EMERGING / ANNOUNCED)

**Visa Intelligent Commerce** (announced March 2025) introduces "agent credentials" — tokenised payment instruments scoped to an AI agent with spending limits, merchant category restrictions, and expiry windows. Transactions carry agent-originator metadata. API in limited partner preview.

**Mastercard Agent Pay** (announced 2025) follows an identical model: agentic tokens, cardholder-set spending controls, cross-platform agent identity. Joint announced deployment with Microsoft Copilot for B2B procurement.

**Google A2A (Agent-to-Agent) Protocol** (announced May 2025) is an open standard for agents to communicate with each other and discover each other's capabilities. Agent capability is described at `/.well-known/agent.json`. Commerce is an explicit use case in the spec. Not yet widely deployed outside the Google ecosystem.

`llms.txt` is an informal but rapidly adopted standard: a structured Markdown file at the site root that gives LLMs an optimised summary of what a platform offers and how to use it. Stripe, Shopify, Anthropic, Cloudflare, and many developer tool platforms have adopted it. No formal standards body governs it, but it is becoming a baseline expectation.

### India-Specific Context (Critical)

**UPI Circle** (launched by NPCI, September 2024) is the most strategically relevant development for PayU. UPI Circle allows a primary UPI user to delegate limited payment authority to a secondary user with defined limits (amount, frequency, validity period). The conceptual model maps directly to agent delegation: the customer authorises the agent to make payments on their behalf within defined constraints. This is the India-native infrastructure blueprint for autonomous agent payments.

**India's 2FA regulatory requirement** is the most important constraint in this entire strategy. RBI mandates second-factor authentication for every customer-initiated digital payment. This means an AI agent cannot complete a payment on a customer's behalf without some form of customer authentication. This is not a PayU limitation — it is a regulatory boundary. It defines the outer edge of what is possible for consumer-facing agentic payments in India today.

The practical implication: the human-in-the-loop redirect model (agent creates payment request, customer completes it themselves) is not a workaround. It _is_ the compliant agentic commerce pattern for India. PayU's existing flow is built for exactly this.

**ONDC (Open Network for Digital Commerce)** is India's decentralised commerce protocol. It is JSON-based (Beckn Protocol), highly machine-readable, and explicitly designed for programmatic access. An AI agent acting as a "Buyer App" on ONDC could discover products and initiate a PayU payment — this is a credible near-term integration path.

**Account Aggregator (AA)** enables consented, read-only financial data sharing. An agent could query a customer's AA to confirm available balance before initiating a payment request — a relevant pre-transaction decision step.

### Key Technical Patterns (Cross-Platform)

These patterns are consistent across every serious implementation:

1. **Human-in-the-loop redirect** — Agent creates payment request, returns URL, customer completes payment on hosted page. Universally adopted, RBI-compliant.
2. **Pre-authorised mandate drawdown** — Customer sets up a standing instruction upfront; agent draws down within the authorised limits. The India equivalent is UPI AutoPay / eNACH. This is the viable path to autonomous payments today.
3. **OAuth 2.0 machine-to-machine** — `client_credentials` flow for agent authentication. Stripe, PayPal, and PayU (for Payment Links) all use this. It is the correct auth pattern for programmatic callers.
4. **Structured async confirmation** — Payment initiation is synchronous; confirmation is async (webhook + polling fallback). Every mature implementation documents this pattern explicitly for agent callers.
5. **MCP as the agent interface layer** — MCP wraps REST APIs in a structured tool format. Stripe's official MCP server is the reference; PayU already has a Remote MCP server (Payment Links tools), establishing precedent.

***

## 4. PayU Current-State Capability Assessment

The following assessment is based directly on repository inspection. File citations are provided.

### What Exists and Is Ready

**OAuth 2.0 client_credentials (Payment Links)** — Fully documented in `docs/Collect Payments/no-code/payment-links/api-auth-token.md` and `reference/payment links/get-token-api-for-payment-links.md`. Scoped access (`create_payment_links`, `read_payment_links`, `update_payment_links`), token caching guidance, test and production base URLs — this is a machine-to-machine auth pattern correctly implemented for agent use.

**Payment Links API** — 8 fully documented API operations backed by `reference/payment-links-oas-v2.yaml` (well-formed OpenAPI 3.0). Programmatic creation, fetching, sharing, updating, cancelling, and transaction status. 10 link types supported. `invoiceNumber` functions as a merchant-controlled reference key.

**Remote MCP Server** — Documented in `docs/MCP & CLI/payu-remote-mcp-server-integration.md`. 13 tools including 4 Payment Links tools (`payLinks_paymentLink_create`, `payLinks_paymentLink_sendPaymentLink`, `payLinks_paymentLink_getByInvoiceNumber`, `payLinks_paymentLink_updatePaymentLink`). OAuth 2.1 PKCE authentication. This means an agent running in an MCP-compatible host (Claude, Cursor, Windsurf) can today create and manage Payment Links via PayU without writing any code.

**Payment status verification** — `verify_payment` API is documented in `reference/General/check-transaction-apis/verify_payment_api.md`. The `GET /payment-links/{invoiceNumber}/transactions` endpoint provides transaction status for Payment Links specifically.

**Webhooks** — Payment events (Successful, Failed, Refund, Dispute) documented in `docs/Developer Tools/webhooks-consolidated/` and `docs/Quick Start/callbacks-webhook-reference.md`. Webhook verification via reverse SHA-512 hash documented with code examples in multiple languages.

**Error codes** — `payment-error-codes.json` at the repository root: \~hundreds of error codes with description, category, and type. Not structured as named objects, but machine-parseable.

**Existing agentic commerce documentation** — `docs/MCP & CLI/agentic-commerce/index.md` (merchant-facing guide covering 4 merchant options and payment methods for agents) and `docs/MCP & CLI/agentic-commerce/build-your-own-chatgpt-merchant-app.md` (technical guide for MCP server backed by Payment Links). These show clear intent and some prior thinking — they are starting points, not finished agent documentation.

**Order context fields** — `udf1-5` on all payment APIs + `invoiceNumber` + `description` + `source` on Payment Links provide adequate order/session metadata transport.

**UPI AutoPay / eNACH / SI (Standing Instructions)** — Documented as recurring payment capabilities. These are today's closest analog to pre-authorised agent payments and are fully operational. See `docs/Offerings/` and `reference/Pre-debit and Recurring Payments/`.

### What Exists Partially or Is Undocumented

**Async coordination pattern** — The `verify_payment` API and webhook infrastructure exist. The pattern "create payment → set webhook → wait for event OR poll status → confirm" is never documented as a single guide for programmatic/agent callers.

`invoiceNumber`**&#x20;as idempotency key** — The repository does not document the behaviour when a `POST /payment-links` call is made twice with the same `invoiceNumber`. Whether it returns the existing link (idempotent) or rejects the duplicate is undocumented. _This requires Engineering confirmation before it can be relied upon by agents._

**OpenAPI quality consistency** — `payment-links-oas-v2.yaml` and the `pl-*.yaml` files are well-formed OpenAPI 3.0. Many other specs in `reference/` are Postman collection JSON exports — machine-parseable but not OAS-compliant. There is no unified OpenAPI catalog listing all available PayU APIs.

**Integration ASK AI Docs** — 13 AI-synthesised integration guides in `docs/Integration ASK AI Docs/` covering affordability, recurring payments, refunds, and others. These are good for retrieval-augmented generation but are written as narrative guides, not structured capability descriptors.

### What Does Not Exist

- `llms.txt` — No file found at any level of the repository or implied documentation site.
- `Idempotency keys` (`X-Idempotency-Key` or equivalent) — Not documented for any PayU API.
- JSON webhook payloads — Payment webhooks use `application/x-www-form-urlencoded`. No JSON Schema for any webhook payload.
- Agent-specific error recovery guide — No documentation on what an agent should do when `verify_payment` returns `pending`, when a webhook is not received, or when a payment link expires.
- Unified capability manifest / agent.json — No structured file describing what PayU APIs are available for programmatic access.
- Agent identity fields on transactions — No `agent_id` or `session_id` field on any PayU API.
- Transactional MCP tools (verify, refund, transaction check) — The Remote MCP covers Payment Links creation and management. It does not expose `verify_payment`, `cancel_refund_transaction`, or general transaction status tools.

***

## 5. Gaps

The following table maps agentic commerce requirements to PayU's current state.

| Agentic Commerce Capability       | PayU Capability Today                                             | Documentation Support                    | Gap                                                                           | Required Action                                                        |
| --------------------------------- | ----------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Product discovery                 | None (not a PayU responsibility; merchant catalog)                | None                                     | PayU does not own this layer                                                  | None required — note in docs                                           |
| Merchant/product information      | `udf1-5`, `description`, `productinfo` fields available           | Partial                                  | Not framed for agent consumption                                              | Documentation reframe                                                  |
| Payment initiation (programmatic) | Payment Links API: `POST /payment-links`                          | Good                                     | Not documented as agent flow                                                  | Write agent guide                                                      |
| Checkout (customer-facing)        | PayU-hosted payment page via link URL                             | Good                                     | Not framed as agent-safe redirect                                             | Clarify in agent docs                                                  |
| Payment methods                   | 15+ methods supported (UPI, cards, netbanking, wallets, EMI)      | Moderate                                 | Not surfaced in agent context                                                 | Add to agent guide                                                     |
| Customer authentication (2FA)     | PayU hosted page handles it                                       | Implicit                                 | 2FA compliance not explained in agent context                                 | Explicit compliance note                                               |
| Payment authorization             | OAuth 2.0 `client_credentials` for Payment Links                  | Good                                     | Only for Payment Links; not for payment API directly                          | Clarify scope in docs                                                  |
| Payment status                    | `GET /payment-links/{id}/transactions`, `verify_payment`          | Partial                                  | Not documented as agent polling pattern                                       | Write async status guide                                               |
| Webhooks                          | Payment events documented, hash verification documented           | Moderate                                 | Form-urlencoded (not JSON), no JSON Schema, sample payloads hidden            | Unhide samples; add JSON Schema                                        |
| Refunds                           | Refund APIs documented                                            | Moderate                                 | Not in Remote MCP, no agent refund guide                                      | Add to MCP + write guide                                               |
| Transaction verification          | `verify_payment` command API                                      | Moderate                                 | Not in Remote MCP, not framed for agent use                                   | Add to MCP; write guide                                                |
| Idempotency                       | None documented                                                   | None                                     | Critical gap for safe agent retries                                           | Confirm `invoiceNumber` behavior; document; pursue `X-Idempotency-Key` |
| Error handling                    | `payment-error-codes.json` exists                                 | Poor                                     | Unlabeled array format; no per-endpoint error schema; no agent recovery guide | Restructure JSON + write error recovery guide                          |
| Security                          | Hash-based auth, OAuth, HMAC                                      | Good                                     | Not framed for agent trust model                                              | Add agent security section                                             |
| Credentials                       | OAuth `client_credentials` (Payment Links), SHA-512 (payment API) | Moderate                                 | Two auth systems not reconciled for agent callers                             | Unified auth guide for agents                                          |
| Consent                           | Implicit (customer accepts on payment page)                       | None                                     | No explicit agent consent model documented                                    | India 2FA compliance section                                           |
| Agent identity                    | None                                                              | None                                     | No `agent_id` field on any API                                                | Future: product capability                                             |
| Customer identity                 | Phone, email, name on Payment Links                               | Good                                     | Not documented for agent-populated PII rules                                  | Reference existing `build-your-own-chatgpt-merchant-app.md`            |
| Order context                     | `udf1-5`, `invoiceNumber`, `description`, `source`                | Moderate                                 | Not framed as agent session/order metadata                                    | Document as agent context fields                                       |
| Merchant context                  | `key` field (merchant identifier)                                 | Implicit                                 | Obvious but not framed for agents                                             | Minor addition                                                         |
| Structured API schemas            | `payment-links-oas-v2.yaml`, per-operation YAMLs                  | Good (Payment Links); mixed (other APIs) | No unified catalog; many specs are Postman JSON not OAS                       | OpenAPI consolidation                                                  |
| Machine-readable documentation    | No `llms.txt`, no capability manifest                             | None                                     | Significant gap for AI coding assistant discoverability                       | Add `llms.txt` immediately                                             |
| AI-readable content               | Integration ASK AI Docs (13 pages)                                | Partial                                  | Good for RAG, not structured as capability metadata                           | Improve frontmatter; add capability tags                               |
| Agent-facing APIs/interfaces      | Remote MCP (4 Payment Links tools)                                | Partial                                  | Missing: verify, refund, transaction check tools                              | Expand MCP server                                                      |

***

## 6. Payment Links Assessment

The recently restructured Payment Links documentation (`docs/Collect Payments/no-code/payment-links/`) positions Payment Links as the strongest existing vehicle for agentic commerce at PayU. Here is a direct assessment of each capability question.

**Can an AI agent discover a Payment Link?**
Yes, with limitations. `GET /payment-links` with date/status filters allows programmatic listing. `GET /payment-links/{invoiceNumber}` retrieves a specific link by merchant reference. The `payLinks_paymentLink_getByInvoiceNumber` MCP tool wraps this. What does not exist: a semantic search or catalog of links by product/category. Discovery is by reference number, not by intent.

**Can an agent initiate or share a Payment Link?**
Yes, today. `POST /payment-links` is fully programmatic, OAuth-protected, and well-documented. The `payLinks_paymentLink_create` MCP tool wraps it. The `POST /payment-links/{id}/share` API sends the link via SMS/email to the customer — `payLinks_paymentLink_sendPaymentLink` wraps this. An agent can create _and_ deliver a payment link without any human API call.

**Can an agent determine amount/context?**
Yes. The Payment Links API supports dynamic amount setting, `description`, `source`, `udf1-5`, `invoiceNumber`, and `productinfo`-equivalent fields. Open Amount links (`isAmountFilledByCustomer: true`) allow the customer to set their own amount — useful for donation or tip scenarios. The agent can populate full order context in the link parameters.

**Can an agent understand Payment Link status?**
Yes. `GET /payment-links/{invoiceNumber}` returns link status (active/inactive/paid/expired). However, the link between "link status" and "payment completion" is not cleanly documented — a link can be "paid" or the transaction can appear in the transactions endpoint. This needs clarification in agent-facing documentation.

**Can an agent verify payment completion?**
Yes. `GET /payment-links/{invoiceNumber}/transactions` returns all transactions against a link including status. `verify_payment` API (general) also works by `txnid`. The gap: neither is surfaced in the Remote MCP tools, and neither is documented as the definitive "agent confirmation check" pattern.

**Can an agent respond to payment failure?**
Partially. The webhook fires for failed payments. The agent can poll status. But the documentation for "agent should do X when payment fails" — cancel the link, create a new one, retry with a different method — does not exist. Error recovery for agents is entirely undocumented.

**Can Payment Links support an agentic purchase journey?**
Yes, for the human-in-the-loop redirect model. The journey is: agent creates link → sends to customer → customer pays (2FA on PayU page) → webhook fires → agent confirms. This is a complete, RBI-compliant agentic commerce journey. It works today. It is not documented as such.

**What additional APIs/metadata would be required?**

For the journey to be agent-ready without product changes:

1. Documented idempotency behaviour for `invoiceNumber` (Engineering confirmation)
2. A documented async status pattern (when to poll, when to rely on webhook, retry intervals)
3. Webhook for Payment Link payment specifically documented and unhidden
4. JSON Schema for webhook payload (nice-to-have for typed agent handling)

For a fully autonomous/redirect-free journey (requires product changes):

1. A payment collect API that triggers UPI Collect directly to the customer's VPA without a browser redirect — subject to RBI 2FA compliance assessment
2. Spending mandate drawdown against a pre-approved UPI AutoPay or eNACH mandate
3. UPI Circle integration — delegate limited payment authority to the agent

**The bottom line on Payment Links:** It is the right foundation for P0 agentic commerce at PayU. The restructured documentation provides a solid base. The gap is framing, async patterns, and a small number of specific agent-oriented additions — not new product capability.

***

## 7. AI-Ready Documentation vs Agent-Ready Documentation

This distinction is fundamental and frequently conflated. PayU's existing documentation strategy has focused on AI-readability — structured Markdown, clean frontmatter, code examples, the Integration ASK AI Docs collection. That is necessary but not sufficient.

### AI-Ready Documentation

AI-readable documentation is optimised to help a human developer, aided by an AI coding assistant, understand and implement an integration. The user is ultimately human.

A developer asks their coding assistant: "How do I create a Payment Link with PayU?"

The AI coding assistant reads the documentation and produces: a code snippet, the API endpoint, the required parameters, and a brief explanation. The developer reviews it, adjusts it, runs it.

Good AI-readable documentation is: clear Markdown structure, complete parameter tables with types and descriptions, working code examples in multiple languages, consistent frontmatter metadata, cross-linked related pages.

PayU's recently restructured Payment Links documentation (`overview.md`, `api-create-share.md`, etc.) is good AI-readable documentation.

### Agent-Ready Documentation

Agent-ready documentation is optimised to be queried and acted upon by an AI agent operating autonomously within a workflow. The caller is not human. The agent cannot ask a follow-up question. It must be able to determine, from the documentation, every decision in the flow.

An AI agent reasoning through a payment task needs to answer, without human intervention:

1. **Discovery:** What can PayU do? What operations are available? How do I authenticate?
2. **Pre-conditions:** What inputs are required? What are the validation rules? What can go wrong before I start?
3. **Execution:** What is the exact API call? What are the required vs optional fields? What does a successful response look like?
4. **State:** What state is the system in after my call? What states can a payment be in? How do I know when the state changes?
5. **Confirmation:** What constitutes definitive completion? When is polling appropriate? When is a webhook sufficient?
6. **Failure handling:** What error codes mean what? Which are retryable? With what delay? Which require a different strategy entirely?
7. **Safety:** Is this call idempotent? What happens if I call it twice? Can I safely retry?

### The Documentation Patterns Required for Agent-Ready

| Pattern                         | Description                                                                     | Example in PayU context                                                                                                                                       |
| ------------------------------- | ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Capability manifest**         | Machine-readable listing of what operations the platform supports               | `llms.txt` at docs root, or `/.well-known/agent.json`                                                                                                         |
| **Precondition schemas**        | Exactly what must be true before an agent can call an endpoint                  | Auth scopes required, required fields, field validation rules — in OpenAPI or structured prose                                                                |
| **State machine documentation** | All possible states a resource can be in and what transitions are possible      | Payment link states: `active` → `paid` / `expired` / `cancelled`; transaction states: `success` / `failure` / `pending`                                       |
| **Async coordination pattern**  | Explicit guidance on how an agent should track completion                       | "After creating a payment link: register notify_url, wait up to X minutes, poll GET /transactions if no webhook received, consider it failed after Y minutes" |
| **Error recovery playbook**     | Machine-readable or highly structured guidance: error code → recommended action | "E001: retry after 5s. E002: do not retry, surface to human. E003: create new link with different amount."                                                    |
| **Idempotency contracts**       | Explicit statement of which operations are safe to retry and how                | "POST /payment-links with the same invoiceNumber returns the existing link — safe to retry"                                                                   |
| **Scope documentation**         | What each auth credential is authorized to do                                   | OAuth scope `create_payment_links` enables POST; scope `read_payment_links` enables GET — agent must request both                                             |
| **Agent-context fields**        | Which fields should agents use to carry session/workflow context                | udf1 = agent_session_id, udf2 = workflow_id, invoiceNumber = merchant_order_ref                                                                               |

These patterns are not about adding more content. They are about structuring existing content differently — adding machine-readable schemas, explicit state diagrams, and recovery tables alongside the existing human-readable prose.

***

## 8. Proposed PayU Agent-Ready Documentation Model

### A. Human Developer Documentation — What Stays

The core product documentation for human developers remains unchanged in substance. PayU Hosted Checkout guides, SDK documentation, plugin integration guides, and platform-specific guides serve human developers who are building traditional payment flows. These should be cleaned up (the Collect Payments / Payment Gateway duplication resolved, the MCP / MCP & CLI duplication resolved) but their content is not the problem. The IA restructuring is the priority, not content rewrites.

### B. AI-Readable Documentation — What Should Improve

These improvements serve developers using AI coding assistants. They require no Engineering changes.

**Frontmatter enrichment.** Every documentation file should add a `metadata.capability` tag indicating the operation type (`payment-initiation`, `status-check`, `refund`, `authentication`, etc.). This improves semantic retrieval from RAG-based tools like the Developer MCP.

`llms.txt`**&#x20;for the docs site.** A structured Markdown file at the root of the documentation site summarising PayU's capabilities, linking to key integration guides, and noting authentication requirements. This is the single highest-impact, lowest-effort action. Stripe, Shopify, Cloudflare, and Anthropic have all adopted it. AI coding assistants referencing the docs site will use it to produce correct initial code. The file should be maintained as a living document.

**OpenAPI consolidation.** A single `payu-openapi-catalog.yaml` file listing all available APIs with links to individual spec files. This allows an agent (or developer's AI assistant) to discover the full API surface without navigating the directory structure. The individual high-quality spec files (`payment-links-oas-v2.yaml`, `pl-*.yaml`, `pdn-rp-api.yaml`, etc.) remain as-is.

**Structured&#x20;**`payment-error-codes.json`**.** The current format — an array of unlabeled 4-element arrays — is machine-parseable only if you already know the schema. Restructure as named objects: `{"code": "E1620", "description": "...", "category": "WRONG_PAYMENT_METHOD_SELECTED", "type": "...", "retryable": false, "recommended_action": "..."}`. Adding `retryable` and `recommended_action` fields transforms it from a reference table into an agent-consumable decision resource. This is a documentation change, not a product change.

**Integration ASK AI Docs expansion.** The 13 existing synthesis pages are useful for RAG retrieval. Add structured frontmatter (capability tags, API list, auth method) to each. Add a 14th page: "Agentic Commerce Integration" covering the Payment Links agent flow end-to-end.

### C. Agent-Facing Documentation — What Is Different

This is a new layer, not a rewrite of existing documentation. It lives in a dedicated section (see Section 9 for the proposed IA) and is structured around tasks, not products.

The key principle: agent-facing documentation is organised around what the agent needs to _do_, not around what PayU has _built_. An agent does not care whether a feature lives in "Collect Payments" or "Offerings" — it cares about "initiate payment" → "confirm payment" → "handle failure."

Specific pages required:

**"PayU for AI Agents" overview.** What PayU supports for programmatic/agent callers, what is explicitly not supported (redirect-free autonomous payment), and why (RBI 2FA). This page sets expectations and prevents agents from attempting flows that will fail.

**Agent authentication guide.** OAuth 2.0 `client_credentials` for Payment Links, SHA-512 hash for general payment APIs — unified in a single page with explicit scopes, token lifecycle, and credential storage guidance.

**Payment request creation guide (agent-optimised).** The POST /payment-links call with annotated field usage for agents: which fields carry order context, which carry session identity, how to use `invoiceNumber` as a reference key.

**Async payment confirmation guide.** The critical missing document: after creating a payment link, how does an agent confirm completion? Define the recommended pattern: register `notify_url`, wait for webhook, fall back to polling `GET /payment-links/{id}/transactions` at 30-second intervals, consider the transaction terminal after N minutes without confirmation, always call `verify_payment` before taking fulfillment action.

**Error recovery playbook.** Structured guide mapping error categories to agent recovery strategies. Not a reference table — a decision tree. "If you receive error category X, do Y. If the payment link expires before payment, create a new link and re-share. If verify_payment returns `pending`, wait and poll again."

**India compliance context for agents.** Why 2FA applies, what it means for the agent flow, why the hosted-page redirect model is the correct approach, and what UPI AutoPay enables for pre-authorised scenarios. This page protects developers from building non-compliant flows.

### D. Machine-Readable Interfaces — What PayU Should Expose

Each recommendation is tied to a specific agentic use case.

`llms.txt` — Use case: A developer building an LLM agent asks their AI coding assistant "help me integrate PayU payment links." The assistant reads `llms.txt` and generates correct code for OAuth + POST /payment-links + webhook handling on the first attempt, instead of producing outdated or incorrect code based on web scraping. Effort: one file, maintained by the documentation team. No Engineering required.

**Consolidated OpenAPI catalog** — Use case: An agent building a payment flow needs to discover which PayU endpoint to call for "cancel a pending payment link." A unified catalog file with all endpoints and their descriptions enables semantic matching. Also enables automatic SDK generation and Postman collection import. Effort: documentation team + review by Engineering to confirm completeness. No product changes.

**JSON Schema for webhook payloads** — Use case: An agent's webhook handler needs to parse the payment completion event. JSON Schema allows typed parsing, IDE autocompletion, and validation. The current `application/x-www-form-urlencoded` format requires the developer to write a custom parser with no schema safety. Adding JSON Schema as documentation alongside the existing payload format is a documentation change. Switching the actual webhook payload to JSON requires Engineering. The documentation change (schema document) should happen first; the API change follows in P1.

**Structured&#x20;**`payment-error-codes.json` — Use case: An agent receives error code `E1620` and needs to decide whether to retry, surface the error to the customer, or try a different payment method. A structured JSON with `retryable` and `recommended_action` fields enables the agent to make this decision without consulting documentation at runtime. Effort: documentation-only restructuring.

**Remote MCP expansion** — Use case: A developer building an agent using Claude Desktop or Cursor needs to verify a payment status as part of their workflow. Today's Remote MCP has no `verify_payment` tool. Adding it means the developer can prototype the full "create → wait → verify" loop entirely within their AI coding environment. Effort: Engineering (MCP server update) + Documentation. This is P1, not P0.

`/.well-known/agent.json` (future, P2) — Use case: An orchestrating agent (e.g., a shopping AI) is deciding which payment processor to use. It queries `/.well-known/agent.json` at `api.payu.in` and discovers PayU's payment capabilities, supported methods, and authentication requirements in a structured format. This aligns with the emerging Google A2A standard. No implementation precedent within PayU yet — P2 consideration.

***

## 9. Proposed Information Architecture

### Position: Cross-Product, Top-Level Section

Agentic Commerce should sit as a **top-level section at the same level as Payment Gateway and Collect Payments** — not within them, and not as a subsection of MCP & CLI. The reasoning:

Agentic Commerce is not a payment _product_. It is a consumption _pattern_ that cuts across Payment Links, Recurring Payments, Webhooks, and Authentication. Placing it within any one product section suggests it is that product's responsibility, creates the expectation that other products are "not for agents," and limits discoverability.

The existing `docs/MCP & CLI/agentic-commerce/` content is a starting point. It should be migrated to a top-level section and expanded. The MCP & CLI section remains for the technical MCP server documentation (Remote MCP, Developer MCP, CLI tool) — these are infrastructure, not the commerce use case.

There is also a second reason: the `agentic-commerce/index.md` is currently written as a merchant business guide, and `build-your-own-chatgpt-merchant-app.md` is a technical guide for one specific scenario (ChatGPT App + MCP). Neither is a comprehensive developer guide for building agent-initiated payments. The proposed IA accommodates both by giving the section proper depth and scope.

### Proposed Structure

```
Agentic Commerce
├── Overview
│   ├── What is Agentic Commerce?
│   ├── How PayU Fits into Agent Flows
│   └── What is Supported Today (and What is Not)
│
├── Before You Start
│   ├── Prerequisites
│   ├── India Compliance & RBI 2FA
│   └── Choosing the Right Integration Pattern
│
├── Quickstart
│   ├── Step 1: Authenticate as an Agent (OAuth 2.0)
│   ├── Step 2: Create a Payment Request
│   ├── Step 3: Present the Link to Your Customer
│   ├── Step 4: Confirm Payment Completion
│   └── Complete Code Example
│
├── Integration Patterns
│   ├── Human-in-the-Loop (Recommended for India)
│   │   └── Payment Links Flow
│   ├── Recurring / Pre-Authorised
│   │   └── UPI AutoPay & eNACH
│   └── Delegated Payments (UPI Circle)  [Future / P2]
│
├── Using the PayU MCP Server
│   ├── Remote MCP: Available Tools
│   ├── Developer MCP: Documentation Search
│   └── MCP Examples (Claude, GPT, Gemini)
│
├── Payment Lifecycle for Agents
│   ├── Payment States & Transitions
│   ├── Async Confirmation Pattern
│   │   ├── Webhooks
│   │   └── Polling Fallback
│   └── Error Recovery Playbook
│
├── Authentication & Credentials
│   ├── OAuth 2.0 for Payment Links (Machine-to-Machine)
│   ├── SHA-512 Hash for Payment APIs
│   └── Scopes Reference
│
├── Agent Context Fields
│   └── Using udf, invoiceNumber, and source
│
├── Security
│   ├── PII Handling (Agent Rules)
│   ├── Webhook Signature Verification
│   └── Credential Storage
│
├── Testing
│   ├── Test Credentials for Agents
│   └── Simulating Webhooks Locally
│
└── API Reference
    ├── Payment Links API → [links to reference/payment-links-oas-v2.yaml]
    ├── Verify Payment API → [links to reference/verify_payment.json]
    └── Webhook Payloads → [links to structured payload docs]
```

### IA Cleanup Required (Prerequisite)

Before the Agentic Commerce section can be properly surfaced, two duplication problems in the current IA must be resolved:

1. **Collect Payments vs. Payment Gateway** — These are near-identical directory trees. One should be canonical; the other archived or removed. This affects the `_order.yaml` navigation and the ability to clearly link from the Agentic Commerce section to the right product documentation.

2. **MCP vs. MCP & CLI** — Two separate directories for overlapping MCP content. These should be merged into a single canonical location before the Agentic Commerce section references them.

These cleanups are not optional prerequisites — they are necessary for the Agentic Commerce section to link to authoritative sources rather than duplicates.

***

## 10. Minimum Viable Agentic Commerce Journey

### The Journey

The following is the smallest complete agentic commerce loop that PayU can support today, without any product or Engineering changes:

```
Step 1: AUTHENTICATE
Agent calls POST /oauth/token
  with client_credentials grant
  → receives Bearer token (scoped: create_payment_links + read_payment_links)

Step 2: CREATE PAYMENT REQUEST
Agent calls POST /payment-links
  with: amount, description, customer.phone, invoiceNumber (merchant ref), udf1 (session context)
  → receives paymentLink URL

Step 3: DELIVER TO CUSTOMER
Agent sends paymentLink URL to customer
  via: in-conversation message, SMS (POST /payment-links/{id}/share), WhatsApp, or email

Step 4: CUSTOMER COMPLETES PAYMENT
Customer opens URL → PayU-hosted page
  → selects payment method (UPI, card, netbanking)
  → completes 2FA (UPI PIN, OTP) [RBI-compliant]
  → payment processed

Step 5: RECEIVE WEBHOOK
PayU fires POST to notify_url
  with: mihpayid, status, txnid, amount, hash
  → merchant server verifies hash → confirms status = "success"

Step 6: VERIFY COMPLETION
Agent calls GET /payment-links/{invoiceNumber}/transactions
  → confirms transaction present with status = "success"
  → OR calls verify_payment with txnid for independent confirmation

Step 7: CONFIRM TO CUSTOMER + TRIGGER FULFILLMENT
Agent sends: "Payment of ₹X received. Your order is confirmed. Ref: {invoiceNumber}"
Merchant fulfillment process triggered
```

### Is This Feasible Today?

**Yes.** Every API in this journey exists and is documented. The Remote MCP server handles Steps 1, 2, and 6 via tools (`payLinks_paymentLink_create`, `payLinks_paymentLink_getByInvoiceNumber`). The webhook infrastructure is live. The verify_payment API is documented.

### What Is Missing for This to Be Properly Documented

| Missing Element                                     | Where the Gap Is                                                              | What Is Needed                                                                                                 |
| --------------------------------------------------- | ----------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| This 7-step journey as a single, canonical document | Nowhere in the repo                                                           | Write it — documentation change only                                                                           |
| Idempotency contract for `invoiceNumber`            | Step 2 — safe retry                                                           | Engineering confirmation; document the behaviour                                                               |
| Specific webhook for Payment Link payment           | Step 5 — which webhook event fires                                            | Clarify in webhook docs + test (may already work via `notify_url` but not explicitly stated for Payment Links) |
| Async wait / polling guidance                       | Steps 5–6 — how long to wait, when to poll                                    | Write the async coordination pattern doc                                                                       |
| Error recovery at each step                         | All steps — what if POST /payment-links fails? What if webhook never arrives? | Write the error recovery playbook                                                                              |
| Step 6 tool in Remote MCP                           | Step 6 — verify_payment is not exposed                                        | Add verify_payment tool to Remote MCP (P1, Engineering)                                                        |
| A complete working code example                     | The Quickstart page                                                           | Write with OAuth + Payment Links + webhook handler                                                             |

***

## 11. P0/P1/P2 Roadmap

### P0 — Documentation Foundation (0–4 Weeks, No Engineering Dependencies)

These actions can begin immediately. They require no product changes, no API changes, and no Engineering involvement beyond factual confirmation of specific behaviours.

**P0.1 — Write the Agent Integration Guide**
A single, end-to-end guide covering the 7-step MVP journey. Includes complete code examples (Node.js/Python). Lives in the new Agentic Commerce section. Becomes the canonical reference for developer-facing agentic commerce documentation.
_Why:_ The capability exists. The documentation does not. This is the highest-impact, lowest-effort action.
_Dependency:_ Engineering to confirm `invoiceNumber` idempotency behaviour and webhook behaviour for Payment Link payments.
_DevEx impact:_ High — reduces time-to-first-agent-transaction from "unknown/impossible" to "hours."
_Complexity:_ Low.

**P0.2 — Add&#x20;**`llms.txt`**&#x20;to the Documentation Site**
A structured Markdown file summarising PayU's API capabilities, authentication methods, key documentation pages, and known limitations. Maintained as documentation changes.
_Why:_ This is the single most impactful action for improving AI coding assistant output quality. Every developer using GitHub Copilot, Claude, Cursor, or ChatGPT to write PayU integration code benefits immediately.
_Dependency:_ Access to the documentation site deployment (to place file at root). Content is documentation-team owned.
_DevEx impact:_ High, indirect — AI coding assistants generate better initial code, reducing back-and-forth.
_Complexity:_ Very low.

**P0.3 — Restructure&#x20;**`payment-error-codes.json`
Add field names, `retryable` boolean, and `recommended_action` string to each error code entry. Convert from unlabeled array to named object format.
_Why:_ Current format requires prior knowledge of the schema to parse. Agent-friendly format enables runtime decision-making without documentation lookup.
_Dependency:_ None. Pure documentation/data change.
_DevEx impact:_ Medium — enables typed error handling in agent code.
_Complexity:_ Low (scripted transformation).

**P0.4 — Write the Async Status Confirmation Pattern**
A dedicated documentation page covering: register notify_url, receive webhook, verify via GET /transactions, poll interval, timeout handling, and call verify_payment for independent confirmation.
_Why:_ This is the most common failure point in agentic integrations — agents need explicit guidance on async coordination.
_Dependency:_ None beyond Engineering confirmation of exact timing guarantees.
_DevEx impact:_ High — prevents the most common agent integration error.
_Complexity:_ Low.

**P0.5 — Restructure the IA (Remove Duplication)**
Resolve Collect Payments / Payment Gateway and MCP / MCP & CLI duplication. Create the top-level Agentic Commerce section. Update `_order.yaml` files.
_Why:_ Without resolving duplication, the Agentic Commerce section will link to ambiguous or outdated content. This is a blocker for everything else in the IA.
_Dependency:_ Internal decision on canonical product doc structure. No Engineering.
_DevEx impact:_ Medium — reduces navigation confusion for all developers, not just agent builders.
_Complexity:_ Medium (content audit and redirect management).

**P0.6 — Add JSON Schema for Payment Webhook Payloads (Documentation Only)**
Publish a JSON Schema document describing the payment webhook payload structure, even though the actual payload is form-urlencoded. This is documentation ahead of the API change.
_Why:_ Typed webhook handling is a prerequisite for robust agent code. Even before the API changes to JSON, having a schema enables developers to write deserialisation code with type safety.
_Dependency:_ None.
_DevEx impact:_ Medium.
_Complexity:_ Low.

**P0.7 — Write India Compliance Context for Agents**
A clear, honest page explaining RBI 2FA requirements, what this means for agentic payment flows, and why the hosted-page redirect model is the compliant pattern. Include a brief note on UPI AutoPay as the path toward pre-authorised scenarios.
_Why:_ Without this, developers will attempt to build autonomous payment flows that are non-compliant. This page prevents wasted integration effort and potential compliance risk.
_Dependency:_ Legal/Compliance review recommended.
_DevEx impact:_ Medium — prevents misdirected efforts.
_Complexity:_ Very low.

***

### P1 — Developer and Agent Capabilities (1–3 Months, Light Engineering)

These require Engineering involvement but are incremental additions to existing systems.

**P1.1 — Expand Remote MCP Server**
Add tools: `verify_payment`, `get_transaction_status`, `cancel_payment_link`, and optionally `initiate_refund`.
_Why:_ The Remote MCP today covers only Payment Links creation and management. The agent flow requires status verification. Without this, a developer using the MCP must drop out to raw API calls for Step 6 of the MVP journey.
_Dependency:_ Engineering (MCP server update) — estimated low complexity (wrapping existing APIs).
_DevEx impact:_ High — completes the agent flow within the MCP toolchain.
_Complexity:_ Medium for Engineering.

**P1.2 — Document Idempotency Behaviour Formally**
Confirm and document the idempotency behaviour of `POST /payment-links` with the same `invoiceNumber`. If it is not currently idempotent, implement idempotency and document it.
_Why:_ Agent retry safety is non-negotiable. Network failures happen. An agent that retries a failed payment creation must not generate duplicate charges.
_Dependency:_ Engineering confirmation/implementation.
_DevEx impact:_ High — a foundational trust guarantee.
_Complexity:_ Low to medium depending on current behaviour.

**P1.3 — Publish Consolidated OpenAPI Catalog**
A single `payu-openapi-catalog.yaml` or equivalent listing all available APIs, grouping them by capability, with links to individual spec files.
_Why:_ Enables AI coding assistants and agent frameworks to discover the full PayU API surface through a single query. Also enables automatic SDK generation and Postman collection import.
_Dependency:_ Documentation team + Engineering review for completeness.
_DevEx impact:_ Medium-high.
_Complexity:_ Medium (content auditing, cross-referencing the mixed-quality reference directory).

**P1.4 — Agent SDK Examples for Major Frameworks**
Code examples for the MVP journey in: LangChain (Python), OpenAI Agents SDK (Python/Node), Anthropic tool use (Python). These become the foundation of the Quickstart and the Agentic Commerce section's reference examples.
_Why:_ Developers building agents use these frameworks. A native example in their framework of choice reduces adoption friction from days to hours.
_Dependency:_ Documentation team. No Engineering.
_DevEx impact:_ Very high — the strongest developer acquisition lever for agent-builder audience.
_Complexity:_ Medium (writing and testing examples).

**P1.5 — Switch Payment Webhooks to JSON (or Add JSON Option)**
Offer `application/json` webhook payloads as an opt-in alongside the existing form-urlencoded format.
_Why:_ Form-urlencoded webhook payloads require manual parsing, are not typed, and have no standard schema. JSON payloads with a documented schema enable type-safe, auto-generated webhook handlers.
_Dependency:_ Engineering (webhook delivery system change).
_DevEx impact:_ Medium — improves developer experience for all webhook consumers, not just agent builders.
_Complexity:_ Medium for Engineering.

***

### P2 — Advanced Agentic Commerce (3–12 Months, Product and Regulatory Involvement)

These require either new product capabilities, regulatory assessment, or both.

**P2.1 — UPI Circle Integration Guide and API Support**
Document UPI Circle as the primary agent delegation mechanism for India. If PayU's UPI implementation supports UPI Circle, expose it via API and document the delegation flow. If not, prioritise it as a product roadmap item.
_Why:_ UPI Circle is the India-native regulatory-compliant path to pre-authorised agent payments. It is the equivalent of what Visa Intelligent Commerce is building for card networks — but it exists today in India's UPI infrastructure.
_Dependency:_ Product/Engineering + NPCI/banking partner support.
_DevEx impact:_ Very high — unlocks the first genuine autonomous payment flow in India.
_Complexity:_ High.

**P2.2 — Agent Identity Fields on Transactions**
Add optional fields to the payment API: `agent_id`, `workflow_id`, `delegation_ref`. These carry through to the transaction record and webhook payload.
_Why:_ Merchants, regulators, and payment networks are moving toward requiring agent-origin tagging on transactions. Getting ahead of this creates a differentiated audit trail feature.
_Dependency:_ Product/Engineering.
_DevEx impact:_ Medium — enables enterprise merchant compliance requirements.
_Complexity:_ Medium.

**P2.3 —&#x20;**`/.well-known/agent.json`**&#x20;Capability Manifest**
Publish a machine-readable capability manifest at a well-known URL describing PayU's agent-accessible APIs, supported operations, authentication methods, and India-specific constraints.
_Why:_ Aligns with Google's A2A protocol. Enables orchestrating agents to discover PayU's capabilities without human documentation review.
_Dependency:_ Engineering (static file serving + content definition).
_DevEx impact:_ Medium-low initially; grows as A2A protocol adoption increases.
_Complexity:_ Low (static file).

**P2.4 — ONDC + PayU Integration Guide**
A developer guide for building an AI agent that discovers products on ONDC and completes payment via PayU.
_Why:_ ONDC is the machine-readable commerce layer for India. The combination of ONDC product discovery + PayU payment completion is the most realistic near-term Indian agentic commerce scenario.
_Dependency:_ Requires ONDC protocol knowledge and potentially a PayU ONDC integration. Partially documentation-only if the integration already exists.
_DevEx impact:_ High for Indian merchant/developer ecosystem.
_Complexity:_ High.

***

## 12. DevEx Goal Alignment

### Goal 1: Reduce Integration TAT

**Direct impact.** The time a developer spends from "I want to accept PayU payments in my AI agent" to "my first test transaction is complete" is currently undefined — not because the APIs do not work, but because no documentation tells them how to use those APIs in an agentic context.

`llms.txt` directly reduces TAT for the growing population of developers who use AI coding assistants as their primary documentation interface. When Cursor or Claude reads `llms.txt` and generates a correct OAuth + Payment Links + webhook handler on the first attempt, the developer does not need to debug incorrect code, hunt through multiple documentation pages, or raise a support ticket.

The consolidated OpenAPI catalog and agent SDK examples reduce TAT by eliminating the current "figure it out yourself" phase for developers working in LangChain, OpenAI Agents, or Anthropic's SDK.

The async confirmation pattern guide reduces TAT by preventing the most common agent integration failure: a developer who creates a payment link but cannot figure out how to reliably confirm completion.

**Estimated impact:** For the agent-builder developer persona specifically, these documentation changes could reduce integration TAT from "days to weeks (if possible at all)" to "hours."

### Goal 2: Settlement Active → Transaction Active

**Indirect but meaningful impact.**

The hypothesis is that merchants who complete KYC and become Settlement Active do not proceed to Transaction Active because the integration barrier is too high. For a segment of these merchants — particularly SMB merchants and solo operators who are not technical developers — the barrier is not the API itself but the requirement to build a checkout integration.

Agentic Commerce and the documentation changes associated with it address this in two ways:

First, the Remote MCP server's Payment Links tools already enable a merchant (or their AI assistant) to create payment links programmatically without writing code. If a merchant can instruct their AI assistant "create a payment link for ₹500 for \[customer name]" and have it work through the MCP server, the checkout barrier is effectively zero. The documentation for this flow — the MCP Quickstart, the agent guide — is what makes it discoverable.

Second, better `llms.txt` and structured OpenAPI documentation means that when a technical developer at a merchant business tries to integrate PayU with assistance from an AI coding tool, the quality of code they produce is higher, they encounter fewer errors, and they are less likely to abandon the integration mid-way. Reduced abandonment = more merchants reaching Transaction Active.

This is not a primary DevEx goal for Agentic Commerce — it is a collateral benefit. The primary value for this goal is the MCP server's zero-code path for SMB merchants. That story should be told explicitly in the Agentic Commerce documentation.

***

## 13. Risks and Dependencies

### Regulatory Risk (High)

India's 2FA requirement is a hard regulatory boundary. Any agentic commerce documentation that implies an agent can complete a customer payment without the customer authenticating is non-compliant. The India Compliance Context document (P0.7) is not optional — it is a legal protection as much as a developer guide. Every integration pattern in the Agentic Commerce section must be reviewed against RBI guidelines before publication.

_Mitigation:_ Explicit compliance sections in all agent flow documentation. Legal/Compliance review of P0.7 before publication. UPI AutoPay as the documented "pre-authorised" path — it is already regulated and understood.

### False Capability Claims Risk (High)

The repository currently contains one page (`build-your-own-chatgpt-merchant-app.md`) that references capabilities (tool schemas, MCP transport patterns) that are specific to a ChatGPT App SDK integration. As the Agentic Commerce section is expanded, there is a risk of documenting aspirational capabilities (spending controls, agent credentials, redirect-free payments) that PayU does not yet support. Every capability stated in agent-facing documentation must be confirmed against live API behaviour.

_Mitigation:_ All documentation should clearly label "available today," "requires Product/Engineering confirmation," and "planned for future release." The capability table in this document (Section 5) provides the current baseline.

### Engineering Confirmation Dependency (Medium)

P0.1 (agent integration guide) is blocked on Engineering confirming:

1. The behaviour of `POST /payment-links` with a duplicate `invoiceNumber`
2. Whether the `notify_url` webhook fires for Payment Link payments specifically
3. Any undocumented limitations on the `verify_payment` API

These are factual confirmations, not new feature requests. They should be quick to resolve.

### Content Duplication Risk (Medium)

Adding an Agentic Commerce section without resolving the Collect Payments / Payment Gateway duplication and MCP / MCP & CLI duplication creates a third overlapping content tree. The IA cleanup (P0.5) must precede or accompany the new section's launch.

### MCP Protocol Drift Risk (Low-Medium)

MCP is an evolving specification. PayU's Remote MCP server and documentation were built against a specific MCP version. As the specification evolves (the March 2025 update added OAuth 2.0 support; further updates are expected), the MCP documentation will need updates. This is a maintenance cost, not a blocker.

### Competitive Timing Risk (Low)

Stripe's Agent Toolkit is live. `llms.txt` adoption is growing. Developers building agentic payment flows are making toolchain choices now. Each month of delay in publishing agent-facing documentation is a month where developers default to Stripe for their agent-commerce payment needs — not because Stripe's payment product is better for India, but because Stripe's documentation tells the story and PayU's does not.

***

## 14. Recommended Strategy

**If PayU wanted to start becoming Agentic-Commerce-ready today, this is what to do first:**

The core insight is this: PayU does not need to build anything new to have a compelling agentic commerce story. The Payment Links API, OAuth 2.0 authentication, Remote MCP server, and webhook infrastructure are already a complete agent-ready payment system. What is missing is the documentation that assembles these pieces into a coherent story for the agent-builder developer persona.

### 1. Documentation Changes

Write four documents that do not exist and should:

- The 7-step agent integration guide (MVP journey, end-to-end, with working code)
- The async payment confirmation pattern (webhook + polling + verify_payment)
- The error recovery playbook for agent callers
- The India compliance context for agent payments

These four documents transform PayU's agent story from "technically possible, figure it out yourself" to "here is exactly how to do it."

### 2. API/Interface Changes

Two changes require Engineering and should be prioritised:

- Confirm and document `invoiceNumber` idempotency behaviour — this is a confirmation exercise, possibly a one-line documentation change, possibly a small engineering task
- Add `verify_payment` and `get_transaction_status` tools to the Remote MCP server — these are wrappers around existing APIs

### 3. IA Changes

Create a top-level Agentic Commerce section. Migrate and expand the existing `docs/MCP & CLI/agentic-commerce/` content into it. Simultaneously resolve the Collect Payments / Payment Gateway duplication so that the Agentic Commerce section's cross-links are unambiguous.

### 4. Machine-Readable Assets

Publish `llms.txt` at the docs site root. This is the single highest-impact, lowest-effort action in the entire roadmap. Restructure `payment-error-codes.json` with named fields and `retryable` / `recommended_action` properties.

### 5. Developer Experience Changes

Write one complete, tested code example for the MVP journey in each of: Python (LangChain / Anthropic SDK) and Node.js (OpenAI Agents SDK). Make these the centrepiece of the Agentic Commerce Quickstart. A developer who can copy, run, and adapt a working example is a developer who does not abandon the integration.

### 6. Product/Engineering Dependencies

P0 actions require only two confirmations from Engineering. P1 requires MCP server expansion and idempotency implementation. The recommendation is to get Engineering confirmation for P0 in the same sprint that documentation writing begins, so that the published guide is accurate from day one.

### 7. Measurement/KPIs

| Metric                                                   | Baseline                     | Target                                       | Measurement                                                              |
| -------------------------------------------------------- | ---------------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| First agent-initiated test transaction (new integrators) | Undefined/unknown            | \< 2 hours from Quickstart                   | Developer onboarding survey + time-to-first-transaction logs             |
| AI coding assistant code quality                         | Not measured                 | First-attempt code runs without modification | Developer feedback; test with Cursor/Claude against published `llms.txt` |
| Remote MCP tool usage                                    | Payment Links creation only  | verify_payment tool usage appears in logs    | MCP server access logs                                                   |
| Agentic Commerce docs page views                         | Zero (section doesn't exist) | \> 500 unique/month within 60 days           | Documentation analytics                                                  |
| Integration support tickets for agent flows              | Unknown                      | Decrease YoY as documentation matures        | Support ticket tagging                                                   |

***

## 15. What We Should Do Next

The following are the concrete actions, in priority order, with owner suggestions and dependencies.

**Action 1 (Week 1): Engineering Confirmation**
Contact PayU Engineering to confirm: (a) `invoiceNumber` idempotency behaviour on duplicate POST /payment-links calls, (b) whether `notify_url` fires for Payment Link payments, (c) any known limitations on `verify_payment` that differ from the documented spec. These confirmations unlock all P0 documentation work.

**Action 2 (Weeks 1–2): Write&#x20;**`llms.txt`
Draft the `llms.txt` file. It should summarise: PayU's core payment APIs, the OAuth 2.0 authentication model for Payment Links, the SHA-512 hash model for general APIs, the key integration patterns (hosted checkout, server-to-server, Payment Links), and links to the most important documentation pages. Get documentation team review. Coordinate with the team responsible for the docs site deployment to publish it at the root.

**Action 3 (Weeks 2–4): Write the Agent Integration Guide**
Write the 7-step MVP journey document. Include complete, tested code examples (Node.js and Python). Cover: authenticate, create link, confirm payment, handle webhook, verify completion. This becomes the Quickstart page in the Agentic Commerce section.

**Action 4 (Weeks 2–4): Write Supporting Pages**

- Async Payment Confirmation Pattern
- Error Recovery Playbook
- India Compliance Context for Agents

**Action 5 (Weeks 3–4): IA Restructuring**
Propose and execute the IA changes: create Agentic Commerce section, migrate existing agentic-commerce content, resolve Collect Payments / Payment Gateway duplication. Update `_order.yaml` files.

**Action 6 (Weeks 4–6): Restructure&#x20;**`payment-error-codes.json`
Write the restructuring script and output the new named-object format. Review with Engineering/Product for the `retryable` and `recommended_action` fields.

**Action 7 (P1 Sprint): Remote MCP Expansion**
Raise an Engineering request to add `verify_payment`, `get_transaction_status`, and `cancel_payment_link` to the Remote MCP server. Document the new tools in the MCP section of the Agentic Commerce docs.

**Action 8 (P1 Sprint): Agent SDK Examples**
Write and test integration examples for LangChain (Python) and OpenAI Agents SDK. Publish as the reference code in the Agentic Commerce Quickstart and as standalone recipes in `recipes/`.

**Action 9 (P1 Sprint): Consolidated OpenAPI Catalog**
Audit the `reference/` directory, identify the well-formed OAS specs, and produce a single catalog YAML linking them. Publish as a machine-readable asset.

**Action 10 (P2, Product Roadmap): UPI Circle Integration**
Brief the Product team on UPI Circle's relevance to agentic commerce. Initiate an assessment of whether PayU's UPI integration supports UPI Circle delegation, and if not, what would be required to support it. This is the key to unlocking the next level of agentic commerce for India.

***

_Document status: Research and strategy complete. No repository changes made. Ready for review and prioritisation._
