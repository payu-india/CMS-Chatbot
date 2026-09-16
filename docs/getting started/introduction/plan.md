---
title: Plan
deprecated: false
hidden: true
metadata:
  robots: index
---
# PayU Developer Docs — Full Restructuring Plan (v2)

**Prepared**: September 16, 2026 | **Tier Strategy**: Integration-complexity tiers (No-Code / Prebuilt UI / Developer Required) | **AI-Ready Architecture**

***

## How to Read This Document

This plan has five parts:

1. **Baseline Measurement** — how to use GSC and GA to establish where you are today before touching anything
2. **New Information Architecture** — the complete top-to-bottom structure: tier definitions, taxonomy, global nav, full left nav across all 107 products, and six page-level templates
3. **AI-Readiness Layer** — the metadata schema, semantic chunking rules, and MCP alignment
4. **Migration Map** — every current section and product mapped to its new home, with exact repo paths
5. **What You've Missed** — capabilities and content types absent from both the current docs and this plan's scope

Phases and timelines are at the end.

***

## The Three Tiers — Definitions

The tier strategy organizes products by how much developer involvement is required, not by use case. This is the central organizing principle for every navigation, page label, and audience callout in the new docs.

**Tier 1 — No-Code** (27 products)
Zero developer involvement. A merchant or ops person configures the product via the PayU dashboard, installs a plugin, or shares a link. No API calls, no code to write. Examples: Payment Links, WooCommerce Plugin, Subscriptions Dashboard, Payouts Dashboard, Refunds Dashboard.

**Tier 2 — Prebuilt UI** (19 products)
A developer does the integration work, but PayU owns and maintains the complete payment UI. The merchant never builds a payment form. Examples: PayU Hosted Checkout, Android CheckoutPro SDK, Checkout Plus, Affordability Widget.

**Tier 3 — Developer Required** (47 products)
Full custom integration. The merchant builds the payment form and/or flow, calls APIs directly, and owns the UI. Full PCI scope responsibility. Examples: Merchant Hosted Checkout, S2S flows, Subscriptions API, Payouts API, Partner Onboarding API.

**Multi-Tier** (14 products)
A single product where different channels or features sit in different tiers. Examples: Refunds (T1: dashboard, T3: API), Subscriptions (T1: dashboard & links, T3: API/AutoPay), Offers (T1: dashboard, T2: widget, T3: API). These need an "Overview" page that routes developers to the right tier.

***

## Part 1 — Baseline Measurement (GSC + GA)

Do this before moving a single file. Once restructuring begins, pre-migration data becomes your primary validation reference.

### Google Search Console

Pull 16 weeks of data — this covers a full Indian festive season cycle. Export every report as CSV; don't rely on the GSC UI for trend analysis.

**Queries Report** — Segment into four intent buckets. For each bucket record: total impressions, average position, average CTR, and the top 10 queries.

- **Navigation intent**: `payu docs`, `payu developer portal`, `docs.payu.in`, `payu api documentation` — how many developers actively look for your docs
- **Integration intent**: `payu payment integration`, `payu woocommerce plugin`, `payu android sdk`, `payu upi integration`, `payu checkout integration`, `payu recurring payments api`, `payu payouts api` — demand signal for which tiers and products matter most in search
- **Troubleshooting intent**: `payu hash mismatch`, `payu error 422`, `payu payment failed`, `payu webhook not received`, `payu invalid hash` — where developers get stuck
- **Comparison intent**: `payu vs razorpay developer docs`, `payu integration easy` — competitive positioning

**Pages Report** — Sort by impressions descending. The top 20 pages by impressions are your highest-value URLs. Protect these during migration or guarantee 301 redirects are live before launch.

Also examine the bottom: pages with zero impressions in 16 weeks are either `hidden: true` (your platform likely sets `noindex` from this field), too thin for Google to surface, or orphaned with no inbound links.

**Coverage Report** — Download the "Not indexed" list. Any navigable page not indexed is invisible to 100% of organic developer traffic.

**Core Web Vitals** — Record pass/fail rates by section. Developer docs with poor CWV subtly signal product quality.

**Tier-specific query segments to track separately**: Tier 1 searches skew toward `woocommerce payu plugin`, `payu payment link setup`, `payu shopify`; Tier 2 toward `payu checkout sdk`, `payu android sdk integration`; Tier 3 toward `payu s2s api`, `payu merchant hosted checkout`, `payu subscriptions api`. Knowing which tier drives the most organic demand should inform which sections you restructure first.

### Google Analytics 4

**Five reports that matter most:**

**1. Top Pages by Engagement** — Sort by Views, but cross-reference with Average Engagement Time. High views + low engagement = intent mismatch or content failure. High engagement + low views = underranked valuable content (SEO opportunity).

**2. Entry Pages (Organic only)** — Filter by `First user medium = organic`. These are your de-facto homepages for organic developer traffic. If developers are landing deep in docs with no context (no tier indicator, no "you might need to read this first" callout), that's a structural gap.

**3. Exit Pages** — High exits mid-guide = friction point. High exits on API endpoint pages = developer couldn't find the answer. These are your highest-priority content fixes.

**4. Tier 1 vs Tier 2 vs Tier 3 funnel** — Once the new structure is live, build a GA4 custom funnel: `[Tier selection page]` → `[Product overview page]` → `[Integration guide or dashboard guide]` → `[API reference or success state]`. Drop-off at each step tells you where the tier navigation breaks.

**5. Internal Search Queries** — Top 100 search queries from inside the docs. Every high-volume query without a great result page is a content gap.

**Events to set up before restructuring begins:**

- `code_copy` — fires when a developer copies any code block. Your best engagement signal.
- `tier_selection` — fires when a developer clicks a tier badge or tier navigation item. Tells you which tiers developers actually use.
- `outbound_to_dashboard` — fires when a developer navigates from docs to the PayU dashboard.
- `404_error` — critical during and after migration.
- `feedback_helpful` / `feedback_unhelpful` — on every page's feedback widget (add this to all pages as part of the restructure).
- `search_query` — captures internal search terms.

**Snapshot these numbers today before any changes:**

| Metric                                     | Snapshot | Target (post-restructure, 6 months)      |
| ------------------------------------------ | -------- | ---------------------------------------- |
| Organic sessions/month to docs             | —        | +40%                                     |
| Avg. engagement time on integration guides | —        | \>3 minutes                              |
| Avg. engagement time on API endpoint pages | —        | \>2 minutes                              |
| 404 error rate                             | —        | \<0.5%                                   |
| Top integration guide exit rate            | —        | \<35%                                    |
| Internal search usage rate                 | —        | Decreasing (better nav = less searching) |
| % of navigable pages indexed (GSC)         | —        | \>90%                                    |
| Tier 1 guide completion rate               | —        | \>60%                                    |

***

## Part 2 — New Information Architecture

### 2.1 Canonical Terminology

Lock these names before any file moves. Inconsistency is a trust signal — if "Merchant Hosted Checkout" and "Custom Checkout" appear interchangeably, developers (and AI agents) lose confidence.

| Current (inconsistent)                                   | Canonical Name                                                            |
| -------------------------------------------------------- | ------------------------------------------------------------------------- |
| PayU Hosted Checkout / Redirect Flow / Prebuilt Checkout | **PayU Hosted Checkout**                                                  |
| Merchant Hosted Checkout / Custom Checkout / MHC         | **Merchant Hosted Checkout**                                              |
| Checkout Express / CommercePro Checkout                  | **Checkout Express**                                                      |
| S2S / Server-to-Server / Direct API                      | **Server-to-Server (S2S)**                                                |
| General APIs / verify_payment / Management API           | **Management APIs**                                                       |
| Key & Salt / Merchant Key / API Key                      | **Merchant Key** (key) and **API Salt** (salt) — always paired            |
| Hash / Checksum / SHA512 hash                            | **Hash** — never "checksum"                                               |
| txnid / transaction_id / merchant_txn_id                 | **txnid** — the PayU canonical field name                                 |
| Recurring Payments / Subscriptions / Auto-debit          | **Subscriptions** (the product) / **Recurring Payments** (the capability) |
| Tier 1 / No-Code / Dashboard                             | **Tier 1 — No-Code**                                                      |
| Tier 2 / Prebuilt UI / SDK                               | **Tier 2 — Prebuilt UI**                                                  |
| Tier 3 / Developer / API / Custom                        | **Tier 3 — Developer Required**                                           |

**URL slug convention**: lowercase, hyphenated, structured as `/{section}/{product}/{page}`. Never include tier numbers in slugs — tiers can change, but slugs should be permanent. Examples:

- `/accept-payments/merchant-hosted-checkout/cards` not `/tier3/MHC/credit-debit-cards`
- `/manage-subscriptions/subscriptions-api/create-a-mandate` not `/Offerings/introduction-recurring-payments`
- `/send-payouts/smart-send/overview` not `/payouts/payouts-integration/smart-send-introduction`

**API endpoint page naming**: always `Verb + Noun`. Predictable for search and AI retrieval.

- Good: `Create a Payment`, `Register a Mandate`, `Initiate a Payout`, `Fetch Bill Details`
- Bad: `postservice`, `Payment APIs`, `Mandate Registration`, `Get Transaction`

***

### 2.2 Global Navigation

Five items maximum. No dropdowns. Clean.

```
[PayU Logo]    Docs    API Reference    SDKs    Changelog    Support
                                                        [🔍 Search]  [Dashboard →]
```

The **Dashboard →** CTA should be visually distinct and persistent. Developers switch between docs and dashboard constantly — never make them hunt for it.

***

### 2.3 Left Navigation — Complete Structure

This is the full left nav across all 107 products, organized by use-case section with tier labels. Items marked **(NEW)** do not exist in the current repo and must be written. Tier badges `[T1]` `[T2]` `[T3]` appear as visual labels on each nav item, not as section dividers — a developer scanning the nav instantly knows how much work each product requires.

```
──────────────────────────────
  OVERVIEW & GET STARTED
──────────────────────────────

• What is PayU                              [concept]
• Key Concepts                              [concept — hash, webhooks, environments]
(• Architecture Overview)                   [NEW — payment flow diagram]
• Choose Your Integration Path             [NEW — tier decision guide, CRITICAL]
• Create Your Account                       [guide]
• Your First Payment in 5 Minutes          [tutorial — PayU Hosted Checkout quickstart]
• Test Your Integration                     [guide — sandbox, test cards, test UPI IDs]
(• Go-Live Checklist)                       [NEW — per tier: T1 checklist / T2 checklist / T3 checklist]

──────────────────────────────
  ACCEPT PAYMENTS
──────────────────────────────

[T1] No-Code

  ▸ Payment Links
    • Overview
    • Create from Dashboard
    • Bulk Upload via CSV

  • Payment Buttons                         [T1]
  • Invoices                                [T1]

  ▸ eCommerce Plugins                       [T1]
    • Overview — Choose Your Platform
    • Shopify
    • WooCommerce
    • Magento / Adobe Commerce
    • BigCommerce
    • OpenCart
    • PrestaShop
    • Wix
    • Shopmatic
    • Fynd
    • Odoo
    • Bagisto
    • Zoho
    • CommercePro Checkout Plugin

  ▸ In-Person Payments                      [T1]
    • Static UPI QR
    • Integrated Dynamic Storefront QR

  ▸ WhatsApp                                [T1 in this section]
    • Enhanced Payment Links

[T2] Prebuilt UI

  ▸ Web Checkout
    • PayU Hosted Checkout — Overview
    • Integration Guide
    • Customise the Checkout
    • Handle the Payment Response
    • Checkout Express (CommercePro)        [T2]
    • Checkout Plus                         [T2]

  ▸ Mobile SDKs                             [T2]
    • Overview — Choose Your SDK
    • Android CheckoutPro SDK
    • iOS CheckoutPro SDK
    • React Native SDK
    • Flutter SDK
    • Cordova SDK
    • Capacitor / Ionic SDK
    • UPI Bolt SDK

  ▸ WhatsApp                                [T2 in this section]
    • Native Payments (P2M / UPI Intent)
    • Interakt Integration

  ▸ In-Person & QR                          [T2]
    • Dynamic UPI QR (API-generated)

  ▸ Payment Links API                       [T2]
    • Create Payment Links via API

[T3] Developer Required

  ▸ Merchant Hosted Checkout                [T3]
    • Overview
    • Integration Guide
    ▸ Payment Methods
      • Cards (Credit / Debit)
      • UPI Intent
      • UPI Collect
      • Net Banking
      • Net Banking TPV
      • Wallets
      • BNPL
      • EFTNet

  ▸ Server-to-Server (S2S)                  [T3]
    • Overview
    • Standard Flow
    • Classic Flow (OTP)
    • Decoupled Flow
    • Direct Authorization
    • Handle the Payment Response

  ▸ Specialized Payment Methods             [T3]
    • Apple Pay
    • Native OTP Flow
    • EFTNET / Bank Transfer (NEFT/RTGS/IMPS)
    • Banking Connect (IBMB / NBBL)
    • Mutual Fund Payments
    • Account Funding Transaction (AFT)
    • Virtual Cards
    • Merchant Wallet / Closed Loop Wallet
    • TPV — API Integration
    • Push Tokenization
    • LazyPay Pay-in-3
    • EMI NTB Flow
    • Redemption using Prepaid

  ▸ In-Person & POS                         [T3]
    • Android POS SDK
    • POS Terminal Integration

  • Payment Links Bulk Upload API           [T3]

Multi-Tier Products

  ▸ EMI                                     [T2 auto in Hosted Checkout | T3 API]
    • Overview — Choose Your Approach
    • EMI in Hosted Checkout                [T2]
    • EMI API Integration                   [T3]
    • Cardless EMI                          [T3]

  ▸ BNPL                                    [T2 auto in Hosted Checkout | T3 API]
    • Overview — Choose Your Approach
    • BNPL in Hosted Checkout               [T2]
    • BNPL API Integration (S2S)            [T3]

  ▸ UPI QR                                  [T1 static | T2 dynamic API]
    • Overview — Choose Your Approach
    • Static QR from Dashboard              [T1]
    • Dynamic QR via API                    [T2]

  ▸ Save Cards / Tokenization               [T2 auto | T3 Push Tokenization]
    • Overview — Choose Your Approach
    (• Compliance: RBI Tokenization Rules)  [NEW]
    • Auto-Tokenization (Hosted Checkout)   [T2]
    • Push Tokenization API                 [T3]

  ▸ WhatsApp Payments                       [T1 links | T2 native SDK]
    • Overview — Choose Your Approach
    • Enhanced Payment Links                [T1]
    • Native Payments (P2M / UPI Intent)    [T2]

──────────────────────────────
  INCREASE CONVERSION
──────────────────────────────

  ▸ Affordability Suite
    • Overview
    • Offers Dashboard                      [T1]
    • Affordability Widget                  [T2]
    ▸ Offers API Integration                [T3]
      • Create an Offer
      • SKU-Based Discounts
      • No-Cost EMI Offers

  ▸ Rewards & Loyalty                       [T3]
    • Loyalty Edge API
    • TWID Rewards Integration
    • Rewards Partner Integration
    • RewardX / Pay with Rewards
    • Flipkart Supercoins

  • Recommendation Engine                   [T2]
  • MobiKwik Link Pay                       [T3]

──────────────────────────────
  MANAGE SUBSCRIPTIONS
──────────────────────────────

  ▸ Subscriptions                           [Multi-Tier]
    • Overview — Choose Your Approach
    • Subscription Links & Dashboard        [T1]
    • Subscriptions API                     [T3]
    • UPI AutoPay Mandate API               [T3]
    • Zion Subscription Automation          [T3]
    • eNACH Integration                     [T3]
    (• Subscription Webhooks)               [fill stub — HIGH PRIORITY]
    (• Retry Logic & Recovery)              [NEW]

──────────────────────────────
  MANAGE INTERNATIONAL PAYMENTS
──────────────────────────────

  All products in this section are [T3 — Developer Required]

  • Overview
  (• Supported Currencies & Methods)        [NEW]
  • Cross-Border Payments / Import
  • Dynamic Currency Conversion (DCC)
  • LRS Integration

──────────────────────────────
  SEND PAYOUTS
──────────────────────────────

  ▸ Payouts                                 [Multi-Tier]
    • Overview — Choose Your Approach
    • Payouts Dashboard                     [T1]
    • Single Transfer API                   [T3]
    • Smart Send (Auto-Rail Selection)      [T3]
    • Beneficiary Registration              [T3]
    • Pay to Phone                          [T3]
    • EFTNet                                [T3]
    • Payout Webhooks & Status
    (• Rate Limits & Bulk Limits)           [NEW]

──────────────────────────────
  RECONCILE & MANAGE PAYMENTS
──────────────────────────────

  ▸ Refunds                                 [Multi-Tier]
    • Overview — T1 Dashboard vs T3 API
    • Issue Refund from Dashboard           [T1]
    • Refund API Integration                [T3]
    • Refund States & Timelines
    • Partial Refunds

  ▸ Chargebacks                             [Multi-Tier]
    • Overview — T1 Dashboard vs T3 Webhooks
    • Chargeback Dashboard                  [T1]
    • Webhook Integration & Alerts          [T3]
    • Submit Evidence via API               [T3]

  ▸ Reports & Settlements                   [Multi-Tier]
    • Overview
    • Download Reports from Dashboard       [T1]
    • Reports API                           [T3]
    (• TDS / GST Handling)                  [NEW]
    (• Settlement Cycle Explained)          [NEW]

──────────────────────────────
  PARTNER & MARKETPLACE
──────────────────────────────

  ▸ Partner Program                         [Multi-Tier]
    • Overview — Choose Your Approach
    • Referral Links                        [T1]
    • Co-Branded OAuth Onboarding           [T3]
    • Partner API (Merchant Onboarding)     [T3]

  ▸ Split Settlements                       [Multi-Tier]
    • Overview
    • Dashboard for Split Settlements       [T1]
    • Split Settlements API                 [T3]

──────────────────────────────
  BILL PAYMENTS (BBPS)
──────────────────────────────

  • Overview
  • BBPS Connect Agent API                  [T2]
  • BBPS Recharge API                       [T3]
  (• Webhook Events)                        [NEW]

──────────────────────────────
  DEVELOPER TOOLS
──────────────────────────────

  ▸ Server-Side SDKs                        [T3]
    • Overview
    • PHP SDK
    • Java SDK
    • Node.js SDK
    • Python SDK
    • Go SDK

  ▸ Webhooks
    • Overview
    • Create & Configure
    (• Event Types Catalog)                 [NEW — fill stub HIGH PRIORITY]
    (• Payment Webhook Payloads)            [fill stub HIGH PRIORITY]
    (• Subscription Webhook Payloads)       [fill stub HIGH PRIORITY]
    • Verify a Webhook Signature
    (• Retry & Failure Handling)            [NEW]

  ▸ Authentication & Security
    • API Authentication
    • Hash Generation                       [concept + code, all languages]
    (• Rate Limits Reference)               [NEW]
    (• Idempotency)                         [NEW]

  ▸ AI Integration (MCP & CLI)
    • Dev Guide MCP Server
    • Remote MCP Server
    • PayU CLI
    • Agentic Commerce Suite

  ▸ Testing & Sandbox
    (• Sandbox Reference)                   [NEW — centralized test cards, UPI IDs, bank codes]
    (• Simulate Payment Outcomes)           [NEW — how to trigger success/failure/pending]
    (• Sandbox Limitations)                 [NEW]

  • Monitoring & Alerts

──────────────────────────────
  RESOURCES
──────────────────────────────

  • Error Code Reference
  (• Glossary)                              [NEW — HIGH AI-READINESS IMPACT]
  • SDKs & Libraries
  (• Postman Collections)                   [NEW — surface existing JSON files]
  (• Changelog)                             [NEW]
  (• Status Page)                           [NEW — link to uptime monitor]
  (• Community & Support)                   [NEW]
```

***

### 2.4 The "Choose Your Integration Path" Page

This page is the single most important new page in the restructured docs. It sits at the top of the left nav and answers the question every new developer has before reading anything else: _"Where do I start?"_

The page should be a decision tree built around three questions:

**Question 1**: Are you a developer?

- No → Go to Tier 1. Your path: `Payment Links → eCommerce Plugins → Dashboard features`
- Yes → Continue to Q2

**Question 2**: Do you need to build your own payment form/UI?

- No → Tier 2 is your path. PayU renders the UI. Your path: `PayU Hosted Checkout → Checkout Express → Mobile SDKs`
- Yes → Tier 3 is your path. You build the form. Your path: `Merchant Hosted Checkout → S2S`

**Question 3** (Tier 3 developers): Which platform?

- Web → Merchant Hosted Checkout or S2S
- Mobile → Android/iOS/RN/Flutter SDKs (note: CheckoutPro is Tier 2 — they stay on Tier 3 only if they need a custom UI)
- In-Person → Android POS SDK or POS Terminal

At the bottom of this page: a matrix table showing all use-case sections (Subscriptions, Payouts, Refunds, etc.) and which tier applies within each, so developers know that even if they're a Tier 3 payment integration, they can still use the Tier 1 dashboard for refunds.

***

### 2.5 Page-Level Templates

Every page is one of six types. Type determines structure. These are not suggestions — define them as enforced layouts in your docs platform.

***

#### Template A — Product Overview Page

Used for: section landing pages and multi-tier product overview pages.

```
[H1] Product Name
[Tier badge(s)] — e.g., "Available at Tier 1 and Tier 3"

[Lede — 2 sentences] What this product does and who it's for.

[H2] Choose your approach          ← FOR MULTI-TIER PRODUCTS ONLY
Comparison table: | | Tier 1 — No-Code | Tier 3 — Developer |
Rows: Who it's for | Setup time | Code required | Capabilities | Limitations
→ [Go to Tier 1 guide] or [Go to Tier 3 guide]

[H2] When to use this
Prose explanation. Include when NOT to use it. Include a comparison
to the closest alternative if one exists.

[H2] How it works
One diagram showing the sequence. Keep to the essential flow.

[H2] Prerequisites
| Requirement | Details | Where to get it |

[H2] Capabilities and limits
Specific technical capabilities. And: what this product cannot do.
Developers need the limits before committing to a path.

[Quick links]
→ Integration Guide  →  API Reference  →  Sample Code
```

***

#### Template B — Integration Guide Page

Used for: step-by-step implementation guides at any tier.

```
[H1] Verb + Outcome — e.g., "Set Up PayU Hosted Checkout"
[Tier badge] [T2 — Prebuilt UI]

[Info callout] Prerequisites: [linked list] | Time: ~30 min

[H2] What you'll build
One paragraph. Concrete end state. "By the end of this guide, your
checkout page will redirect customers to PayU's payment screen, collect
payment, and return them to your site with a success/failure response."

[H2] Step 1 — [Step name]
Why this step (one sentence). What to do.
[Code block with copy button]
[Expected output or screenshot]
[⚠ Common mistake — one-liner]

[Repeat for each step]

[H2] Test your integration
Specific test case. Include test credential. What success looks like.

[H2] Troubleshooting
| Error | Likely Cause | Fix |
Max 5 rows.

[H2] Next steps
3 links in the natural progression.
```

***

#### Template C — API Endpoint Page

The most critical template for AI-readiness. Every endpoint page must follow this structure exactly. LLMs parse these pages to generate integration code — structural inconsistency produces hallucinations.

```
[H1] Create a Payment
[Tier badge] [T3 — Developer Required]

[Method badge] POST    https://info.payu.in/merchant/postservice

[One-line description]
Submit a payment request to initiate a transaction. Returns a
transaction ID; customer is redirected to authentication.

[H2] Authentication
What credentials. How they're passed. Link: Hash Generation.

[H2] Headers
| Header | Type | Required | Description |

[H2] Request Parameters
| Parameter | Type | Required | Max Length | Description | Example |
[ALL parameters documented — no "see dashboard" shortcuts]

[H2] Request Example
[Code block — default: form-encoded POST]
[Toggle: cURL / PHP / Python / Java / Node.js / Go]

[H2] Response Parameters
| Parameter | Type | Description |

[H2] Response Examples
[Tab: Success 200]   [Tab: Common failures]
Each tab labeled with the scenario that produces it.

[H2] Error Codes (this endpoint)
| Code | Message | Cause | Fix |
Link → full Error Code Reference

[H2] Code Examples
cURL first (no dependencies), then PHP, Python, Java, Node.js, Go.

[H2] Related Endpoints
3 links max.

[H2] Changelog
| Date | Change |
```

***

#### Template D — Concept Page

Used for: Hash Generation, Webhooks overview, Payment Flow, Test vs. Production, Tokenization.

```
[H1] How [Concept] Works

[H2] What it is — 2-3 plain-language sentences.

[H2] Why it exists — The specific problem it solves.

[H2] How it works — Diagram for complex flows. Prose + example for simpler ones.

[H2] Implementation — Code block. Multiple languages.

[H2] Common mistakes — Top 3, as a table.

[H2] Terms defined on this page — Glossary entries inline.
Critical for AI-readiness: LLMs retrieve these definitions to
ground code generation using platform-specific terms.
```

***

#### Template E — Troubleshooting / Error Page

```
[H1] Error [Code]: [Verbatim Error Message]

[H2] What this means — Plain language, not a restatement of the error.

[H2] Common causes — Numbered list, ranked by frequency.

[H2] How to fix it — Per cause, with code where applicable.

[H2] If you're still stuck
→ Check [relevant guide]
→ Contact developer support (include: transaction ID, error response, hash input)
```

***

#### Template F — Tutorial / Recipe Page

Used for: end-to-end code walkthroughs ("Accept a Payment in Python").

```
[H1] [Action] in [Language/Platform]
[Tier badge]

[Full source code block first — with copy-all button]
Prerequisites | Time estimate

[H2] Overview — What this tutorial builds, end-to-end.

[H2] Code walkthrough — Break into sections, explain each.

[H2] Run it — Install, set env vars, run. Expected output.

[H2] What to do next — 3 links to the natural next step.
```

***

## Part 3 — AI-Readiness Layer

AI-readiness is not a separate phase. It's a standard applied to every page from the start of the restructure.

### 3.1 Enhanced Frontmatter Schema

```yaml
---
title: "Create a Payment"
excerpt: "Submit a payment request to the PayU API and initiate a transaction."

# Tier & product classification
tier: "tier-3"                    # tier-1 | tier-2 | tier-3 | multi-tier
tier_label: "Developer Required"  # No-Code | Prebuilt UI | Developer Required
product: "merchant-hosted-checkout"
section: "accept-payments"        # accept-payments | increase-conversion |
                                  # manage-subscriptions | international-payments |
                                  # send-payouts | reconcile-manage | partner-marketplace |
                                  # bill-payments | developer-tools | resources

# Page type & audience
page_type: "api-reference"        # overview | guide | api-reference | concept |
                                  # tutorial | troubleshooting
audience: "developer"             # developer | non-developer | platform-builder

# Navigation & discoverability
prerequisites:
  - "api-authentication"
  - "hash-generation"
related:
  - "verify-a-payment"
  - "handle-payment-response"
  - "payment-webhooks"
search_keywords:
  - "payment request"
  - "initiate payment"
  - "postservice API"
  - "create transaction"

# API metadata (api-reference pages only)
api_method: "POST"
api_endpoint: "/payment/postservice"
api_version: "v2"

# Maintenance
last_reviewed: "2026-09-16"
deprecated: false
hidden: false
---
```

The fields with the highest AI-retrieval impact: `excerpt` (used as chunk context in RAG), `prerequisites` (lets an agent chain docs in the right order), `related` (cross-document traversal), `search_keywords` (improves embedding recall for synonyms and paraphrase queries), and `tier` + `section` (lets the MCP server filter by audience before retrieval).

### 3.2 Semantic Chunking Rules

The PayU MCP server's `search_payu_docs` tool retrieves document chunks. Chunk quality depends entirely on heading structure.

**Rule**: Every H2 section must be a self-contained thought answerable as a standalone unit.

Bad (hard to chunk):

```
H2: Overview
H2: Details
H2: More Information
```

Good (each H2 is a retrievable answer):

```
H2: How Hash Verification Works
H2: Required Parameters for Hash Generation
H2: Hash Generation Code Examples
H2: Common Hash Mismatch Causes
```

When an agent receives the question "Why is my hash mismatching?", it should retrieve exactly one chunk that answers it, not need to parse an entire "Overview" section.

### 3.3 Glossary as Anchor Document

The Glossary page is the single highest-ROI AI-readiness investment per hour of writing effort. LLMs hallucinate on PayU-specific and non-obvious terms. A well-structured Glossary acts as a canonical grounding reference for the MCP server.

Minimum glossary entries: `txnid`, `mihpayid`, `productinfo`, `salt`, `SALT2`, `SALT7`, `udf1–udf5`, `hash`, `surl`, `furl`, `postservice`, `verify_payment`, `mandate`, `si_details`, `emi_amount`, `pg`, `enforce_paymethod`, `bank_code`, `card_token`, `bnpl`, `DCC`, `LRS`, `AFT`, `VAN` (Virtual Account Number for EFTNet), `eNACH`, `AutoPay`, `Zion`, `CheckoutPro`, `Bolt SDK`, `mihpayid vs txnid` (developers confuse these constantly).

### 3.4 Multi-Tier Product AI Routing

For multi-tier products, the Overview page must explicitly state which tier applies to which use case in a format that is retrievable as a single chunk:

```markdown
## Which Tier Is Right for You

| If you want to... | Use this approach | Tier |
|---|---|---|
| Issue refunds without code | PayU Dashboard | Tier 1 — No-Code |
| Issue refunds programmatically | Refund API | Tier 3 — Developer Required |
| Automate refunds triggered by events | Refund API + Webhooks | Tier 3 — Developer Required |
```

This structure allows the MCP server to answer "how do I do refunds without code?" with a direct Tier 1 answer, and "how do I automate refunds via API?" with a direct Tier 3 answer — from the same product section.

### 3.5 MCP Server Alignment

Both MCP tools should be documented with the input/output schema and a complete worked example showing: prompt → tool call → response → what the agent does next. Rate limits must be on both (currently only on Dev Guide MCP). The Remote MCP Server's OAuth authentication flow needs a dedicated page — it doesn't exist.

***

## Part 4 — Migration Map

Every current section, its product count, exact repo paths (from the product tier spreadsheet), and destination in the new structure.

### Section-Level Disposition

| Current Section                  | Products                                        | Action                                                                                                              | New Section                                                                     |
| -------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `docs/Collect Payments/`         | \~60+ products across all tiers                 | Distribute by tier and use case                                                                                     | Accept Payments (T1/T2/T3 groups)                                               |
| `docs/Offerings/`                | \~40+ products                                  | Distribute across: Increase Conversion, Manage Subscriptions, International, Reconcile & Manage, Accept Payments T3 | Per use case                                                                    |
| `docs/getting started/`          | Onboarding + Dashboard                          | Consolidate                                                                                                         | Overview & Get Started                                                          |
| `docs/API basics/`               | Auth, hash, REST format                         | Distribute                                                                                                          | Hash → Developer Tools; Auth → Developer Tools; REST format → individual guides |
| `docs/partners/`                 | Partner referral, co-branded OAuth, Partner API | Rename                                                                                                              | Partner & Marketplace                                                           |
| `docs/payouts/`                  | Payouts dashboard + API                         | Rename + clean stubs                                                                                                | Send Payouts                                                                    |
| `docs/BBPS/`                     | BBPS Connect + Recharge                         | Rename                                                                                                              | Bill Payments                                                                   |
| `docs/MCP & CLI/` + `docs/MCP/`  | MCP servers, CLI, agentic                       | Merge                                                                                                               | Developer Tools › AI Integration                                                |
| `docs/Developer Tools/`          | Webhooks, TWID                                  | Add to nav, fill stubs                                                                                              | Developer Tools › Webhooks                                                      |
| `docs/Whatsapp integration/`     | Enhanced links + Native payments                | Distribute across T1 / T2                                                                                           | Accept Payments (multi-tier WhatsApp)                                           |
| `docs/payu rewardsx/`            | RewardX, Flipkart Supercoins                    | Add to nav                                                                                                          | Increase Conversion › Rewards                                                   |
| `docs/Payment Gateway/`          | 312 files, nav-orphaned                         | Canonical diff vs Collect Payments; redirect loser                                                                  | Merge into Accept Payments                                                      |
| `docs/Payment Methods/`          | 9 files, nav-orphaned                           | Distribute into MHC payment method sub-pages                                                                        | Accept Payments › MHC                                                           |
| `docs/RECYCLE BIN/`              | 41 files                                        | Remove from nav (done); archive                                                                                     | Not in nav                                                                      |
| `docs/Docs For Internal Review/` | 18 files                                        | Move off public repo                                                                                                | Not in public nav                                                               |
| `docs/Monitoring & Alerts/`      | 2 files                                         | Move                                                                                                                | Developer Tools                                                                 |
| `docs/Integration ASK AI Docs/`  | 13 files                                        | Merge                                                                                                               | Developer Tools › AI Integration                                                |
| `docs/Quick Start/`              | 7 files                                         | Consolidate                                                                                                         | Get Started section                                                             |

### Product-Level Migration (exact repo paths from tier spreadsheet)

#### Accept Payments — Tier 1: No-Code

| Product                 | Current Repo Path                                                                              | New Slug                                            |
| ----------------------- | ---------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Payment Links           | `docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/`     | `/accept-payments/payment-links/`                   |
| Payment Buttons         | `docs/Collect Payments/introduction-no-code-payments-integration/payment-buttons-dashboard.md` | `/accept-payments/payment-buttons/`                 |
| Invoices                | `docs/Collect Payments/introduction-no-code-payments-integration/invoices-dashboard/`          | `/accept-payments/invoices/`                        |
| Shopify Plugin          | `docs/Collect Payments/ecommerce-platform-plugins/shopify/`                                    | `/accept-payments/plugins/shopify/`                 |
| WooCommerce Plugin      | `docs/Collect Payments/ecommerce-platform-plugins/woocommerce/`                                | `/accept-payments/plugins/woocommerce/`             |
| Magento Plugin          | `docs/Collect Payments/ecommerce-platform-plugins/magento/`                                    | `/accept-payments/plugins/magento/`                 |
| BigCommerce Plugin      | `docs/Collect Payments/ecommerce-platform-plugins/bigcommerce/`                                | `/accept-payments/plugins/bigcommerce/`             |
| OpenCart Plugin         | `docs/Collect Payments/ecommerce-platform-plugins/opencart/`                                   | `/accept-payments/plugins/opencart/`                |
| PrestaShop Plugin       | `docs/Collect Payments/ecommerce-platform-plugins/prestashop/`                                 | `/accept-payments/plugins/prestashop/`              |
| Wix Plugin              | `docs/Collect Payments/ecommerce-platform-plugins/wix/`                                        | `/accept-payments/plugins/wix/`                     |
| Shopmatic Plugin        | `docs/Collect Payments/ecommerce-platform-plugins/shopmatic/`                                  | `/accept-payments/plugins/shopmatic/`               |
| Fynd Plugin             | `docs/Collect Payments/ecommerce-platform-plugins/fynd-integration/`                           | `/accept-payments/plugins/fynd/`                    |
| Odoo Plugin             | `docs/Collect Payments/ecommerce-platform-plugins/odoo/`                                       | `/accept-payments/plugins/odoo/`                    |
| Bagisto Plugin          | `docs/Collect Payments/ecommerce-platform-plugins/bagisto/`                                    | `/accept-payments/plugins/bagisto/`                 |
| Zoho Plugin             | `docs/Collect Payments/ecommerce-platform-plugins/zoho-integration/`                           | `/accept-payments/plugins/zoho/`                    |
| CommercePro Plugin      | `docs/Collect Payments/ecommerce-platform-plugins/commercepro-checkout/`                       | `/accept-payments/plugins/commercepro/`             |
| WhatsApp Enhanced Links | `docs/Whatsapp integration/enhanced-payment-links-on-whatsapp.md`                              | `/accept-payments/whatsapp/enhanced-payment-links/` |
| Static UPI QR           | `docs/Collect Payments/in-person-payments/integrate-upi-qr/`                                   | `/accept-payments/upi-qr/static/`                   |
| Dynamic Storefront QR   | `docs/Collect Payments/in-person-payments/integrated-dynamic-storefront/`                      | `/accept-payments/in-person/dynamic-storefront-qr/` |

#### Accept Payments — Tier 2: Prebuilt UI

| Product                  | Current Repo Path                                                                                                                     | New Slug                                        |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| PayU Hosted Checkout     | `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/`                                                               | `/accept-payments/payu-hosted-checkout/`        |
| Checkout Express         | `docs/Collect Payments/introduction-web/checkout-express/`                                                                            | `/accept-payments/checkout-express/`            |
| Checkout Plus            | `docs/Collect Payments/introduction-web/checkout-plus-integration/`                                                                   | `/accept-payments/checkout-plus/`               |
| Android CheckoutPro SDK  | `docs/Collect Payments/mobile-sdks/explore-android-sdks/`                                                                             | `/accept-payments/mobile-sdks/android/`         |
| iOS CheckoutPro SDK      | `docs/Collect Payments/mobile-sdks/explore-ios-sdks/`                                                                                 | `/accept-payments/mobile-sdks/ios/`             |
| React Native SDK         | `docs/Collect Payments/mobile-sdks/explore-reactnative-sdks/`                                                                         | `/accept-payments/mobile-sdks/react-native/`    |
| Flutter SDK              | `docs/Collect Payments/mobile-sdks/flutter-sdk-introduction/`                                                                         | `/accept-payments/mobile-sdks/flutter/`         |
| Cordova SDK              | `docs/Collect Payments/mobile-sdks/cordova-mobile-sdks/`                                                                              | `/accept-payments/mobile-sdks/cordova/`         |
| Capacitor / Ionic SDK    | `docs/Collect Payments/mobile-sdks/upi-bolt-sdk-ionic/`                                                                               | `/accept-payments/mobile-sdks/capacitor-ionic/` |
| UPI Bolt SDK             | `docs/Collect Payments/mobile-sdks/upi-bolt-sdk-ionic/`                                                                               | `/accept-payments/mobile-sdks/upi-bolt/`        |
| WhatsApp Native Payments | `docs/Whatsapp integration/whatsapp-native-payments/`                                                                                 | `/accept-payments/whatsapp/native-payments/`    |
| Interakt for WhatsApp    | `docs/Collect Payments/ecommerce-platform-plugins/interakt-for-whatsapp-business/`                                                    | `/accept-payments/whatsapp/interakt/`           |
| Affordability Widget     | `docs/Offerings/introduction-to-affordability/affordability-suite/`                                                                   | `/increase-conversion/affordability-widget/`    |
| Recommendation Engine    | `docs/Offerings/recommendation-engine/`                                                                                               | `/increase-conversion/recommendation-engine/`   |
| Payment Links API        | `docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/create-payment-link-via-bulk-upload-apis.md` | `/accept-payments/payment-links/api/`           |
| Dynamic UPI QR (API)     | `docs/Collect Payments/in-person-payments/integrate-upi-qr/`                                                                          | `/accept-payments/upi-qr/dynamic-api/`          |
| BBPS Connect Agent API   | `docs/BBPS/connect-agent-api-integration/`                                                                                            | `/bill-payments/bbps-connect-agent-api/`        |

#### Accept Payments — Tier 3: Developer Required

| Product                        | Current Repo Path                                                                                                                     | New Slug                                           |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| Merchant Hosted Checkout       | `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/`                                                             | `/accept-payments/merchant-hosted-checkout/`       |
| S2S — Standard Flow            | `docs/Collect Payments/introduction-web/server-to-server-integration/`                                                                | `/accept-payments/s2s/standard-flow/`              |
| S2S — Classic (OTP)            | `docs/Collect Payments/introduction-web/server-to-server-integration/classic-integration-for-cards-otp-integration.md`                | `/accept-payments/s2s/classic-flow/`               |
| S2S — Decoupled                | `docs/Collect Payments/introduction-web/server-to-server-integration/decoupled-flow-authentication-only-integration.md`               | `/accept-payments/s2s/decoupled-flow/`             |
| S2S — Direct Auth              | `docs/Collect Payments/introduction-web/server-to-server-integration/`                                                                | `/accept-payments/s2s/direct-authorization/`       |
| Native OTP Flow                | `docs/Offerings/native-otp-flow-integration/`                                                                                         | `/accept-payments/specialized/native-otp/`         |
| Apple Pay                      | `docs/Offerings/apple-pay-integration/`                                                                                               | `/accept-payments/specialized/apple-pay/`          |
| Pre-Authorize / Auth & Capture | `docs/Offerings/auth-and-capture-pre-authorize-card-payments/`                                                                        | `/accept-payments/specialized/auth-and-capture/`   |
| EFTNET / Bank Transfer         | `docs/Offerings/introduction-to-eftnet/`                                                                                              | `/accept-payments/specialized/eftnet/`             |
| Banking Connect (IBMB/NBBL)    | `docs/Offerings/banking-connect-ibmb-or-nbbl/`                                                                                        | `/accept-payments/specialized/banking-connect/`    |
| Mutual Fund Payments           | `docs/Offerings/mutual-funds-payments/`                                                                                               | `/accept-payments/specialized/mutual-funds/`       |
| AFT                            | `docs/Offerings/account-funding-transaction-integration/`                                                                             | `/accept-payments/specialized/aft/`                |
| Virtual Cards                  | `docs/Offerings/virtual-cards-introduction/`                                                                                          | `/accept-payments/specialized/virtual-cards/`      |
| Merchant Wallet                | `docs/Offerings/introduction-to-merchant-wallet/`                                                                                     | `/accept-payments/specialized/merchant-wallet/`    |
| TPV API                        | `docs/Offerings/introduction-to-payu-tpv/`                                                                                            | `/accept-payments/specialized/tpv/`                |
| Push Tokenization              | `docs/Offerings/introduction-save-cards/push-tokenization.md`                                                                         | `/accept-payments/save-cards/push-tokenization/`   |
| Android POS SDK                | `docs/Collect Payments/in-person-payments/android-pos-sdk/`                                                                           | `/accept-payments/in-person/android-pos/`          |
| POS Terminal                   | `docs/Collect Payments/in-person-payments/pos-terminal-integration/`                                                                  | `/accept-payments/in-person/pos-terminal/`         |
| LazyPay Pay-in-3               | `docs/Offerings/introduction-to-affordability/lazypay-pay-in-3/`                                                                      | `/accept-payments/specialized/lazypay-pay-in-3/`   |
| EMI NTB Flow                   | `docs/Offerings/introduction-to-affordability/emi-ntb-flow-integration.md`                                                            | `/accept-payments/specialized/emi-ntb/`            |
| Redemption using Prepaid       | `docs/Offerings/redemption-using-prepaid-integration/`                                                                                | `/accept-payments/specialized/prepaid-redemption/` |
| Payment Links Bulk Upload API  | `docs/Collect Payments/introduction-no-code-payments-integration/payment-links-dashboard/create-payment-link-via-bulk-upload-apis.md` | `/accept-payments/payment-links/bulk-api/`         |

#### Other Sections

| Product                      | Current Repo Path                                                                                         | New Slug                                            |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Offers Dashboard             | `docs/Offerings/introduction-to-affordability/offers-dashboard/`                                          | `/increase-conversion/offers/dashboard/`            |
| Offers API                   | `docs/Offerings/introduction-to-affordability/offers-integration-1/`                                      | `/increase-conversion/offers/api/`                  |
| Loyalty Edge API             | `docs/Offerings/introduction-to-affordability/loyalty-edge-introduction/`                                 | `/increase-conversion/rewards/loyalty-edge/`        |
| TWID Rewards                 | `docs/Offerings/twid-rewards-integration/`                                                                | `/increase-conversion/rewards/twid/`                |
| Rewards Partner              | `docs/Offerings/rewards-partner-integration/`                                                             | `/increase-conversion/rewards/partner/`             |
| RewardX / Pay with Rewards   | `docs/payu rewardsx/introduction-pay-with-rewards.md`                                                     | `/increase-conversion/rewards/rewardx/`             |
| Flipkart Supercoins          | `docs/payu rewardsx/introduction-flipkart-supercoins-pay/`                                                | `/increase-conversion/rewards/flipkart-supercoins/` |
| MobiKwik Link Pay            | `docs/Offerings/introduction-to-affordability/mobikwik-link-pay-integration/`                             | `/increase-conversion/mobikwik/`                    |
| Subscriptions Dashboard      | `docs/Offerings/introduction-recurring-payments-integration/subscription-dashboard/`                      | `/manage-subscriptions/dashboard/`                  |
| Subscriptions API            | `docs/Offerings/introduction-recurring-payments-integration/using-api-integration-recurring-payments/`    | `/manage-subscriptions/api/`                        |
| UPI AutoPay Mandate API      | `docs/Offerings/introduction-recurring-payments-integration/using-api-integration-recurring-payments/`    | `/manage-subscriptions/upi-autopay/`                |
| Zion Subscription Automation | `docs/Offerings/introduction-recurring-payments-integration/using-zion-subscription-automation-platform/` | `/manage-subscriptions/zion/`                       |
| eNACH                        | `docs/Offerings/mutual-funds-payments/enach-mutual-fund-payments-integration.md`                          | `/manage-subscriptions/enach/`                      |
| Cross-Border Payments        | `docs/Offerings/introduction-cross-border-payments-import/`                                               | `/international-payments/cross-border/`             |
| DCC                          | `docs/Offerings/introduction-dynamic-currency-conversion/`                                                | `/international-payments/dcc/`                      |
| LRS Integration              | `docs/Offerings/introduction-cross-border-payments-import/cb-lrs-integration/`                            | `/international-payments/lrs/`                      |
| Payouts Dashboard            | `docs/payouts/payouts-dashboard/`                                                                         | `/send-payouts/dashboard/`                          |
| Payouts Single Transfer      | `docs/payouts/payouts-integration/single-transfer-integration-for-payouts.md`                             | `/send-payouts/single-transfer/`                    |
| Smart Send                   | `docs/payouts/payouts-integration/smart-send-introduction/`                                               | `/send-payouts/smart-send/`                         |
| Beneficiary Registration     | `docs/payouts/payouts-integration/beneficiary-registration-framework.md`                                  | `/send-payouts/beneficiary-registration/`           |
| Pay to Phone                 | `docs/payouts/releasepending-pay-to-phone-integration/`                                                   | `/send-payouts/pay-to-phone/`                       |
| Refunds Dashboard            | `docs/Offerings/introduction-refunds/refunds-in-payu-products/`                                           | `/reconcile-manage/refunds/dashboard/`              |
| Refund API                   | `docs/Offerings/introduction-refunds/`                                                                    | `/reconcile-manage/refunds/api/`                    |
| Chargeback Dashboard         | `docs/Offerings/chargeback/`                                                                              | `/reconcile-manage/chargebacks/dashboard/`          |
| Reports Dashboard            | `docs/getting started/payu-dashboard/sales-and-earnings-dashboard.md`                                     | `/reconcile-manage/reports/dashboard/`              |
| Split Settlements Dashboard  | `docs/Offerings/split-settlments/dashboard-for-split-settlements/`                                        | `/partner-marketplace/split-settlements/dashboard/` |
| Split Settlements API        | `docs/Offerings/split-settlments/api-integration-for-split-settlements/`                                  | `/partner-marketplace/split-settlements/api/`       |
| Partner Referral Links       | `docs/partners/refer-merchants-using-referral-links.md`                                                   | `/partner-marketplace/referral-links/`              |
| Co-Branded OAuth             | `docs/partners/refer-merchants-using-co-branded-oauth-onboarding/`                                        | `/partner-marketplace/co-branded-oauth/`            |
| Partner API                  | `docs/partners/partner-payments-integration.md`                                                           | `/partner-marketplace/partner-api/`                 |
| BBPS Recharge API            | `docs/BBPS/recharge-api-integration/`                                                                     | `/bill-payments/recharge-api/`                      |
| Server-Side SDKs             | `docs/Collect Payments/explore-server-integrations/`                                                      | `/developer-tools/server-side-sdks/`                |
| Dev Guide MCP                | `docs/MCP & CLI/payu-devguide-builder-mcp-configuration.md`                                               | `/developer-tools/mcp/dev-guide-mcp/`               |
| Remote MCP                   | `docs/MCP & CLI/payu-remote-mcp-server-integration.md`                                                    | `/developer-tools/mcp/remote-mcp/`                  |
| PayU CLI                     | `docs/MCP & CLI/payu-cli.md`                                                                              | `/developer-tools/mcp/payu-cli/`                    |
| Agentic Commerce             | `docs/MCP & CLI/agentic-commerce/`                                                                        | `/developer-tools/mcp/agentic-commerce/`            |

### Redirect Strategy

Build the redirect map CSV before any file moves. Every moved URL gets a 301 — no exceptions, even for low-traffic pages.

```csv
old_slug,new_slug,http_status,reason
/docs/Collect-Payments/introduction-web/prebuilt-checkout-payu-hosted,/accept-payments/payu-hosted-checkout,301,section restructure
/docs/Collect-Payments/introduction-web/custom-checkout-merchant-hosted,/accept-payments/merchant-hosted-checkout,301,section restructure
/docs/Offerings/introduction-recurring-payments-integration,/manage-subscriptions,301,section restructure
...
```

Monitor 404 errors in GA4 for 4 weeks post-launch. Every 404 is a missing redirect.

### Content Requiring Rewrite (not just move)

These cannot be migrated by renaming — they need to be written or substantially rebuilt:

1. **Webhook Event Catalog** — stub files exist at `docs/Developer Tools/webhooks-consolidated/events-and-payloads.md`. Write from scratch with all event types.
2. **Payment Webhook Payloads** — stub at `docs/Developer Tools/webhooks-consolidated/create-and-manage-webhooks-1/sample-payloads-payment-webhooks.md`. Write from actual webhook payloads.
3. **Subscription Webhook Payloads** — stub at `docs/Developer Tools/webhooks-consolidated/subscription-webhooks/sample-payloads-subscription-webhooks.md`. Write.
4. `payu-affordability-widget.md` — 5 literal `[PLACEHOLDER: Screenshot...]` markers. Add real screenshots or remove callouts.
5. `payouts/payouts-dashboard/eftnet.md` — 79 characters, no content. Write.
6. `quickstart-code.md` — has `// TODO: verify hash` in developer-facing example code. Fix.
7. All 25 stub files under 300 chars — prioritize those in navigable sections.
8. **Multi-Tier Overview pages** — 14 products need overview pages written from scratch explaining the tier decision.
9. **"Choose Your Integration Path"** — new page, doesn't exist anywhere.
10. **Go-Live Checklist per tier** — new page, doesn't exist anywhere.

***

## Part 5 — What You've Missed

These are documentation capabilities and content types absent from both the current repo and the scope of your original ask, that belong in a world-class payment developer portal. Ordered by developer impact.

**Tier-aware Go-Live Checklist** — Not just a generic checklist, but three checklists: one per tier. A Tier 1 merchant going live with the WooCommerce plugin has completely different requirements from a Tier 3 developer going live with Merchant Hosted Checkout (PCI scope, hash validation, webhook handling, error state coverage). Every major payment gateway has this page. You don't.

**"Choose Your Integration Path" decision guide** — The most visited page on Stripe's developer docs is the one that routes developers to the right integration path. You have 107 products across 3 tiers and 9 sections. Without a routing page, every new developer reads the wrong docs first and builds the wrong thing. This page must be written before any other new content.

**Changelog** — No centralized record of API changes, SDK releases, new features, or deprecations anywhere in the repo. If a developer can't see that your API changed 3 months ago, they can't know if their integration is current. This is one of the highest trust signals for developers evaluating a platform. Every meaningful change needs: what changed, why, and what action the developer must take.

**Sandbox / Testing Reference** — Test credentials, test card numbers, test UPI IDs, test bank codes, and instructions for simulating specific outcomes (success, failure, pending, timeout) are scattered across multiple pages. A developer spends real time hunting for a test UPI ID that should take 5 seconds to find. One canonical Testing page, bookmarked and returned to throughout development. Per-tier: a Tier 1 plugin user needs different test instructions from a Tier 3 S2S developer.

**Rate Limits Reference** — Currently documented only in the Dev Guide MCP section (30 req/min, 100 req/day). Every API section should have its limits documented. A centralized Rate Limits page with a table per API category is more useful than per-page mentions. Platform builders designing retry logic need this before writing a line of code.

**Glossary** — No canonical definitions for PayU-specific terminology anywhere. Developers confuse `mihpayid` and `txnid` regularly. LLMs hallucinate on `si_details`, `SALT2`, `SALT7`, `enforce_paymethod`, `pg`, and `VAN`. A Glossary page is the single highest-ROI AI-readiness investment in the entire repo.

**Per-product Changelog / SDK Version History** — Separate from the API changelog, a version history per SDK (Android, iOS, React Native, Flutter) with breaking changes flagged and migration steps. SDK consumers need to know what changed before upgrading, especially for Tier 2 CheckoutPro integrations where PayU controls the UI layer.

**Versioning and Deprecation Policy** — No published policy on how long deprecated APIs stay live, how breaking changes are communicated, or what the migration window is. An enterprise developer cannot commit to a Tier 3 integration without knowing the answer to these questions.

**Webhook Event Catalog** — A single page listing every possible webhook event type, the payload schema, when it fires, and what action the developer should take. Currently stub files. For developers building event-driven integrations across Subscriptions, Payouts, Refunds, Chargebacks, and BBPS, this page is as important as the payment creation API.

**Compliance and Security page** — PCI DSS scope and responsibility by tier (T1: no scope; T2: minimal; T3: full scope including MHC), RBI regulations affecting integrations (tokenization mandate, recurring payment regulations, save card regulations), 3DS2 authentication requirements. Enterprise integrators verify this before committing to PayU. Currently absent.

**"Was This Helpful?" feedback on every page** — The cheapest content quality signal available. A thumbs up / thumbs down with optional text input on every page gives continuous signal. Pages with high "unhelpful" rates are your priority rewrite queue. Pages with high "helpful" rates are your templates. Costs near-zero to implement, yields permanent signal.

**Last Reviewed timestamp on every page** — Developers look at dates. A guide that says "Last reviewed: March 2026" builds more trust than an undated one. Add `last_reviewed` to frontmatter (defined in Section 3.1) and surface it visibly. Anything not reviewed in 6 months should appear in a stale-content report.

**Postman Collections as first-class resources** — Postman collection JSON files exist in the repo but are buried in `reference/` alongside OpenAPI specs with no documentation on how to find, import, or use them. A "Postman Collections" resource page with a description of each collection, an import link, and setup instructions would meaningfully reduce time-to-first-API-call for Tier 3 developers.

**International payments section** — Cross-Border Payments, DCC, and LRS are currently scattered. They're all Tier 3, RBI-regulated, and require specific agreements. A dedicated `Manage International Payments` section with an overview explaining the regulatory context before the technical docs would serve this audience far better than the current placement inside `Offerings/`.

**"Edit this page" GitHub link** — One implementation line in your docs platform. Enables community corrections, surfaces the last commit date naturally, and signals that the docs are maintained.

**Community and developer support links** — Developers who get stuck have nowhere to go from your docs except general merchant support. A developer community surface (GitHub Discussions, dedicated Stack Overflow tag, or Discord) referenced from every page reduces support tickets and builds ecosystem loyalty.

**Server-Side SDK documentation** — Five SDKs (PHP, Java, Node.js, Python, Go) exist at `docs/Collect Payments/explore-server-integrations/` but are currently grouped with no dedicated Developer Tools section in nav. These are Tier 3 tools that need their own section, per-language installation instructions, and version tables.

***

## Phased Timeline

| Phase                                                             | Duration    | Scope                                                                                                                                                                                                                                   | Owner Signal                                        |
| ----------------------------------------------------------------- | ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| **Phase 0 — Emergency**                                           | Week 1      | Remove RECYCLE BIN + internal review from nav. Fix 4 broken links. Remove 5 placeholder markers. Fix TODO in quickstart code.                                                                                                           | Done before anything else — these are live defects. |
| **Phase 1 — Foundations**                                         | Weeks 2–4   | GSC/GA snapshot. Lock canonical terminology table. Build redirect map CSV. Resolve Collect Payments vs. Payment Gateway canonical question. Write "Choose Your Integration Path" page.                                                  | No files move until Phase 1 is complete.            |
| **Phase 2 — Get Started + Accept Payments**                       | Weeks 5–12  | Restructure Overview/Get Started section. Restructure all of Accept Payments (T1, T2, T3 groups). Write Go-Live Checklist (all three tiers). Write Sandbox Reference. Fill all stubs in this section. Apply templates A–F to all pages. | Highest-traffic, highest-stakes section.            |
| **Phase 3 — Increase Conversion + Subscriptions + International** | Weeks 13–18 | Restructure these three sections. Consolidate the offers-integration triplication. Merge duplicate auth-and-capture directories. Write multi-tier Overview pages for EMI, BNPL, Save Cards.                                             |                                                     |
| **Phase 4 — Payouts + Reconcile + Partner + BBPS**                | Weeks 19–22 | Restructure remaining use-case sections. Fill Payouts stubs. Write Chargeback webhook docs. Write Split Settlements API docs.                                                                                                           |                                                     |
| **Phase 5 — Developer Tools + Resources**                         | Weeks 23–26 | Webhook Event Catalog. Webhook Payload pages. Server-Side SDK section. Rate Limits page. Glossary. Postman Collections page. Merge MCP sections.                                                                                        |                                                     |
| **Phase 6 — AI-Readiness**                                        | Weeks 27–30 | Enhanced frontmatter rollout across all pages. Semantic heading audit. MCP server alignment. Changelog structure + 6-month backfill. SDK Changelogs. Versioning/deprecation policy.                                                     |                                                     |
| **Phase 7 — Ongoing**                                             | Monthly     | GSC/GA review against baselines. Stale page report (anything `last_reviewed` > 6 months). Quarterly content audit.                                                                                                                      |                                                     |

***

_Document version 2.0 — Updated with product tier data from PayU_Product_Tiers.xlsx. Tier strategy: T1 = No-Code (27 products), T2 = Prebuilt UI (19 products), T3 = Developer Required (47 products), Multi-Tier (14 products spanning T1–T3). Total: 107 products across 9 use-case sections._
