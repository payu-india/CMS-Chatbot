---
title: Plan
deprecated: false
hidden: true
metadata:
  robots: index
---
# PayU Developer Docs — Full Restructuring Plan (v3)

**Prepared**: September 16, 2026 | **IA Source**: V7 (research-backed) | **AI-Ready Architecture**

***

## What Changed in v3

This version aligns the plan with **IA V7** — a separately produced information architecture grounded in 10 user research findings (R1–R10). V7 is the canonical IA source. Key structural differences from v2:

| What v2 had                                   | What V7 (v3) uses                                                            | Why it changes                                                         |
| --------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Tiers as top-level nav sections               | Tiers as sub-groupings _within_ Accept Payments                              | Developers browse by use case, not by effort level                     |
| Payment Methods inside Accept Payments        | Payment Methods as its own top-level umbrella                                | COD and AutoPay are discovery problems that need a dedicated home      |
| SDKs scattered under Accept Payments          | SDKs as a standalone top-level umbrella                                      | 9 Android SDKs, 5 iOS SDKs — too deep to bury inside checkout docs     |
| Go Live items scattered per-product           | Go Live as a standalone top-level umbrella                                   | R4: "Integrated and accepting payments are different journeys"         |
| No Solution Guides                            | Solution Guides by business type                                             | Marketplace, Subscription, International, D2C each need a curated path |
| Basic Developer Tools                         | Developer Tools expanded with Debugging & Logs (R6) and Quickstart Code (R7) | Top developer frustrations are debugging and copy-paste code access    |
| "Find Your Integration" as new page to create | Quick Start Wizard **already exists** at `quick-start.md` (hidden)           | P0 action: unhide — solves 3 research findings at once                 |
| COD not mentioned                             | COD as a first-class Payment Method with activation guide                    | R5: COD is completely absent from current docs                         |
| GoKwik not mentioned                          | GoKwik plugin under eCommerce Plugins                                        | R9: GoKwik docs–CPV–API loop blocks non-transacting merchants          |

***

## User Research Findings (R1–R10)

Every structural decision in V7 is backed by one or more of these findings. They are referenced throughout the plan.

| \#  | Finding                                                                                                                                                                      | IA Fix                                                                                         |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| R1  | 52% of integrations are developer-built by someone who is NOT the merchant. Developers need: prod credentials, copyable code, callbacks, errors, logs, production checklist. | `Who Is Setting This Up?` → Developer Setup Package path                                       |
| R2  | All successful developers used AI (Claude/ChatGPT/Gemini) to complete integration. DevGuide Builder MCP exists but is buried.                                                | `Ask AI First` promoted to Getting Started; also in Developer Tools                            |
| R3  | Research next step: "Create user-friendly integration video guides." Less experienced devs wanted video and layman-friendly docs.                                            | Video Guides in Getting Started                                                                |
| R4  | Confusion around the final go-live step. "Integrated and accepting payments are different journeys."                                                                         | Go Live as a standalone top-level section                                                      |
| R5  | Difficulty finding or enabling COD and AutoPay.                                                                                                                              | COD added to Payment Methods; AutoPay cross-referenced; `Enable Payment Methods` in Go Live    |
| R6  | Developer need: "callbacks, errors, logs." Error codes alone are insufficient.                                                                                               | Debugging & Logs section (6 new pages) in Developer Tools                                      |
| R7  | AI-assisted devs pasted docs into AI and needed copyable code. `recipes/` directory not referenced in IA.                                                                    | Quickstart Code section in Developer Tools AND Getting Started                                 |
| R8  | Most merchants cannot name their checkout type. PayU Hosted vs Merchant Hosted vs CommercePro confuses them.                                                                 | Checkout Type Quick Reference in Getting Started; "also known as" labels on every product page |
| R9  | GoKwik docs–CPV–API loop is a PayU-influenced wait blocking non-transacting merchants.                                                                                       | GoKwik as dedicated entry under eCommerce Plugins                                              |
| R10 | Less experienced users wanted clearer step-by-step guides. Experience level question suggested.                                                                              | Transaction Debug Checklist (step-by-step); Video Guides indexed by experience level           |

***

## Part 1 — Baseline Measurement (GSC + GA)

Do this before moving a single file. Pre-migration data is your primary validation reference.

### Google Search Console

Pull 16 weeks of data — full Indian festive season cycle. Export all reports as CSV.

**Queries Report** — Segment into four intent buckets and record: total impressions, average position, average CTR, top 10 queries per bucket.

- **Navigation**: `payu docs`, `payu developer portal`, `docs.payu.in`
- **Integration**: `payu payment integration`, `payu woocommerce plugin`, `payu android sdk`, `payu upi integration`, `payu recurring payments api`, `payu payouts api`, `payu merchant hosted checkout`
- **Troubleshooting**: `payu hash mismatch`, `payu error 422`, `payu payment failed`, `payu webhook not received`, `payu 505 error` (R6 — bank integration errors are a top frustration)
- **Checkout-type confusion** (R8): `payu hosted checkout vs merchant hosted`, `payu checkout express`, `payu commercepro integration` — measure how many developers are searching for the same product by different names

**Pages Report** — Sort by impressions descending. Top 20 URLs are your highest-value assets. Protect them through migration or guarantee 301s are live before launch.

**Coverage Report** — Download the "Not indexed" list. Start by checking these known hidden pages against it: `quick-start.md`, `who-is-setting-this-up.md`, `what-can-you-do-next.md`, webhooks section. If these are not indexed, you'll see the GSC impact the moment you unhide them.

**Core Web Vitals** — Record pass/fail rates by section.

### Google Analytics 4

**Five reports that matter most:**

**1. Top Pages by Engagement** — Views cross-referenced with Average Engagement Time. High views + low engagement = intent mismatch. High engagement + low views = underranked valuable content.

**2. Entry Pages (Organic)** — Filter by `First user medium = organic`. These are your de-facto homepages for search traffic. If developers land deep in docs with no tier indicator, no "you might need to read this first" callout — that's a structural gap the V7 IA solves.

**3. Exit Pages** — High exits mid-guide = friction point. High exits on API pages = developer couldn't find the answer. These are priority rewrite targets.

**4. Go-Live Funnel** — Build a custom GA4 funnel once the new structure is live: `[Integration guide]` → `[Test payment page]` → `[Go Live checklist]` → `[First production transaction]`. R4 found that "integrated" and "accepting payments" are different journeys. Measure where developers fall off between them.

**5. Internal Search Queries** — Top 100 internal search queries. The volume of searches for "hosted checkout" vs "payu checkout" vs "redirect checkout" directly quantifies the R8 naming confusion problem. Use this to prioritize which "also known as" labels to write first.

**Events to set up before restructuring begins:**

- `code_copy` — fires when a developer copies any code block (R7 signal)
- `wizard_completed` — fires when the Quick Start Wizard reaches its final step (once unhidden)
- `tier_path_selected` — fires when a developer clicks No-Code / Prebuilt / Custom in Accept Payments
- `ai_chat_opened` — fires when developer opens Ask AI / DevGuide Builder (R2 signal)
- `404_error` — critical during and after migration
- `feedback_helpful` / `feedback_unhelpful` — on every page

**Baseline snapshot (record before any changes):**

| Metric                                         | Today | Target (6 months post-launch) |
| ---------------------------------------------- | ----- | ----------------------------- |
| Organic sessions/month                         | —     | +40%                          |
| Avg. engagement time on integration guides     | —     | \>3 min                       |
| Exit rate on MHC/S2S guides (T3)               | —     | \<35%                         |
| Wizard completion rate (once unhidden)         | —     | \>50%                         |
| Internal search usage rate                     | —     | Decreasing                    |
| % of navigable pages indexed                   | —     | \>90%                         |
| "Was this helpful" unhelpful rate on API pages | —     | \<20%                         |

***

## Part 2 — New Information Architecture

### 2.1 Canonical Terminology

Lock before any file moves. Inconsistency is a trust signal — and R8 shows it actively causes developers to build the wrong thing.

| Current (inconsistent)                                      | Canonical Name                                                    | "Also known as" label on page                        |
| ----------------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------------- |
| PayU Hosted Checkout / Redirect Flow / Prebuilt Checkout    | **PayU Hosted Checkout**                                          | "Also called: Redirect Checkout, Prebuilt Checkout"  |
| Merchant Hosted Checkout / Custom Checkout / MHC / Seamless | **Merchant Hosted Checkout**                                      | "Also called: Custom Checkout, Seamless Integration" |
| Checkout Express / CommercePro / Checkout Plus              | **CommercePro / Checkout Plus**                                   | "Also called: Checkout Express, Embedded Checkout"   |
| S2S / Server-to-Server / Direct API                         | **Server-to-Server (S2S)**                                        |                                                      |
| Key & Salt / Merchant Key / API Key                         | **Merchant Key** (key) + **API Salt** (salt)                      |                                                      |
| Hash / Checksum / SHA512 hash                               | **Hash**                                                          |                                                      |
| txnid / transaction_id / merchant_txn_id                    | **txnid**                                                         |                                                      |
| Recurring Payments / Subscriptions / Auto-debit / SI        | **Subscriptions** (product) / **Recurring Payments** (capability) |                                                      |

**URL slug convention**: lowercase, hyphenated, `/{umbrella}/{product}/{page}`. Never include tier numbers in slugs.

**API endpoint naming**: always `Verb + Noun`. `Create a Payment`, `Register a Mandate`, `Initiate a Payout`. Never: `postservice`, `Payment APIs`, `verify_payment API`.

***

### 2.2 Global Navigation

```
[PayU Logo]    Docs    API Reference    SDKs    Changelog    Support
                                                        [🔍 Search]  [Dashboard →]
```

Five items, no dropdowns. **Dashboard →** is persistent and visually distinct.

***

### 2.3 Left Navigation — Full V7 Structure

This is the complete left nav from IA V7, preserving all umbrella terms, L0 pages, and L1–L3 sub-pages. Status annotations indicate work required. `★` = new page to create. `↑` = exists but hidden (unhide). `→` = exists, needs move. `∿` = exists, needs merge/edit.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  GETTING STARTED
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Find Your Integration                   [↑ quick-start.md — P0 UNHIDE. Solves R1+R2+R8]
  The <PayUQuickStartWizard /> component.
  Routes in ≤4 questions: intent → platform
  → branding need → who's setting this up?

• Who Is Setting This Up?                 [↑ who-is-setting-this-up.md — P0 UNHIDE + build]
    ├─ Setting Up Myself                  [★ New]
    ├─ Developer Setup Package            [★ New — R1]
    │    ├─ Prod Credentials Guide        [★ New]
    │    ├─ Quickstart Code               [★ New — surfaces recipes/]
    │    ├─ Callbacks & Webhook Ref       [★ New]
    │    └─ Production Checklist          [★ New]
    └─ Build with AI                      [★ New — R2]

• Account Setup
    ├─ Create Your Account                [→ Move from getting started/register-with-payu/]
    │    ├─ Complete KYC & Activation
    │    └─ Documents Checklist
    └─ Get Your Credentials               [∿ Merge 4 near-duplicate pages — R1]

• Your First Test Payment                 [→ Move from Collect Payments/.../test-payment-details.md]

• Ask AI First                            [→ Move to here — R2: all successful devs used AI]

• Video Guides                            [★ New — R3+R10]

• Checkout Type Quick Reference           [★ New — R8: most merchants can't name their checkout type]

• What Can You Do Next?                   [↑ what-can-you-do-next.md — UNHIDE + complete]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ACCEPT PAYMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

── NO-CODE SOLUTIONS ──────────────────── [Tier 1]

• Payment Links & Invoices
    ├─ Overview
    ├─ Create a Payment Link
    ├─ Bulk Upload
    ├─ Dashboard Management
    ├─ Payment Buttons
    ├─ Invoices
    └─ Payment Link APIs

• UPI QR
    ├─ Static QR
    └─ Dynamic QR

• WhatsApp Payments
    ├─ Enhanced Payment Links
    └─ UPI Intent (P2M)

── PREBUILT INTEGRATIONS ─────────────── [Tier 2]

• PayU Hosted Checkout
    ├─ Overview & When to Use             ["Also known as: Redirect Checkout, Prebuilt Checkout" — R8]
    ├─ Integrate
    │    ├─ Web Integration
    │    └─ Mobile WebView
    ├─ Customize the Payment Page
    ├─ Test
    └─ Go Live

• CommercePro / Checkout Plus
    ├─ Overview & When to Use             ["Also known as: Checkout Express, Embedded Checkout" — R8]
    ├─ Integrate
    ├─ Test
    └─ Go Live

• eCommerce Plugins
    ├─ Shopify
    ├─ WooCommerce
    ├─ Magento
    ├─ BigCommerce
    ├─ OpenCart
    ├─ PrestaShop
    ├─ Wix
    ├─ GoKwik                             [★ New — R9]
    └─ Others

• In-Person & POS
    ├─ Dynamic Storefront QR
    ├─ POS Terminal
    └─ Android POS SDK

── CUSTOM INTEGRATIONS ───────────────── [Tier 3]

• Merchant Hosted Checkout
    ├─ Overview & When to Use             ["Also known as: Custom Checkout, Seamless" — R8]
    ├─ Integrate by Payment Method
    │    ├─ Cards (Seamless)
    │    ├─ UPI (Collect & Intent)
    │    ├─ Net Banking
    │    ├─ Wallets
    │    ├─ EMI (Seamless)
    │    ├─ BNPL
    │    ├─ EFTNET
    │    ├─ PayPal
    │    └─ Pluxee
    ├─ Collect Additional Charges
    ├─ UPI Collect Disablement
    ├─ Integration Checklist
    ├─ Test
    └─ Go Live

• Server-to-Server (S2S)
    ├─ Overview & When to Use
    ├─ Integrate
    │    ├─ General Flow
    │    ├─ Classic (Cards + OTP)
    │    ├─ Decoupled
    │    ├─ Direct Authorization
    │    ├─ UPI Variants
    │    └─ UPI Smart Intent (Non-SDK)
    ├─ Integration Checklist
    ├─ Test
    └─ Go Live

• Advanced & Specialized
    ├─ Save Cards & Tokenization
    │    ├─ Model 1 — PayU Hosted
    │    ├─ Model 2 — Zero Code Change
    │    ├─ Model 3 — Simple REST API
    │    ├─ Collect Payments with Saved Card
    │    ├─ API Notifications for Tokenization
    │    └─ Impact on Recurring Payments
    ├─ TPV Verification
    ├─ Apple Pay
    ├─ Native OTP Flow
    ├─ Virtual Cards
    │    └─ Web Integration
    ├─ Auth & Capture (Pre-Authorize)
    ├─ Account Funding Transactions (AFT)
    ├─ Merchant Wallet
    │    └─ Closed-Loop Wallet Management
    ├─ Mutual Funds Payments
    ├─ Banking Connect (IBMB/NBBL)
    └─ Payment via Prepaid (Vouchers)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PAYMENT METHODS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Overview & Integration Matrix

• Cards
    ├─ Overview
    └─ Test Cards

• UPI
    ├─ Overview
    └─ UPI AutoPay / Mandates              [Cross-ref to Manage Subscriptions — R5]

• Net Banking

• Wallets

• EMI
    ├─ Overview
    └─ EMI NTB Flow

• Buy Now Pay Later (BNPL)

• Bank Transfer (EFTNet)

• Cash on Delivery (COD)                  [★ New — R5: completely absent from docs]
    ├─ Overview
    └─ Enable COD on Your Account         [★ New — activation steps only in support docs currently]

• International Payments (overview)
    ├─ International Cards
    ├─ Dynamic Currency Conversion
    └─ Cross-Border / LRS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SDKs
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Overview & Platform Support Matrix

• Mobile SDKs
    ├─ Android
    │    ├─ CheckoutPro SDK
    │    ├─ Google Pay SDK                 [currently in mobile-sdks/android-google-pay-sdk/]
    │    ├─ PhonePe SDK                    [currently in mobile-sdks/android-phonepe-sdk/]
    │    ├─ UPI Bolt SDK
    │    ├─ UPI SDK                        [currently in mobile-sdks/android-upi-sdk/]
    │    ├─ 3DS 2.0 / FlashPay SDK         [currently in mobile-sdks/android-3ds20-sdk/]
    │    ├─ Core SDK                       [currently in mobile-sdks/android-core-sdk/]
    │    ├─ Custom Browser SDK
    │    └─ Native OTP Assist SDK
    ├─ iOS
    │    ├─ CheckoutPro SDK
    │    ├─ 3DS 2.0 / FlashPay SDK
    │    ├─ UPI SDK
    │    ├─ Core SDK
    │    └─ Custom Browser SDK
    ├─ React Native
    │    ├─ CheckoutPro SDK
    │    └─ Core SDK
    ├─ Flutter
    │    └─ CheckoutPro SDK
    └─ Cordova
         ├─ CheckoutPro SDK
         └─ UPI Bolt SDK (Capacitor)

• Server-Side SDKs
    ├─ PHP
    ├─ Java
    ├─ Node.js
    ├─ Python
    └─ Go

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INCREASE CONVERSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Offers
    ├─ Dashboard
    ├─ API Integration
    └─ SKU-Based / Cashback / No-Cost EMI

• Affordability Widget
    ├─ Integrate with JavaScript
    └─ Integrate with ReactJS

• Loyalty Edge
    ├─ Workflow
    ├─ Enable
    └─ Launch a Program

• Recommendation Engine
    ├─ Customer Journey
    └─ API

• Rewards Partner Integration
    ├─ Redemption
    ├─ Earn
    └─ Refund

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  MANAGE SUBSCRIPTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Overview & Key Concepts

• Subscription APIs
    ├─ API Integration
    ├─ Plans
    └─ Standing Instructions (International Cards)

• Recurring by Payment Method
    ├─ Cards
    ├─ Net Banking
    ├─ UPI AutoPay
    └─ Pay-and-Subscribe

• Mandates
    ├─ eNACH Registration
    ├─ eNACH Supported Banks
    └─ Bank Codes

• Zion Subscription Platform
    ├─ Workflow
    ├─ Supported Instruments
    ├─ Plan & Subscription APIs
    └─ Webhooks

• Subscription Dashboard
    ├─ Create Link
    ├─ Bulk Upload
    └─ Manage Mandates

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SEND PAYOUTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Overview & Process Flow

• Payout Lifecycle

• Integrate
    ├─ Single Transfer
    ├─ Smart Send
    ├─ Beneficiary Registration
    └─ Pay to Phone

• Payouts Dashboard
    ├─ Account Activity
    ├─ Add Money
    ├─ Transfers
    └─ Approvals

• Test Credentials

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  INTERNATIONAL PAYMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Dynamic Currency Conversion (DCC)

• Cross-Border (Import) Payments
    ├─ Subscriptions with Cross-Border
    ├─ On-Hold & Settlement APIs
    └─ Import Plugin Integration

• Liberalised Remittance Scheme (LRS)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  RECONCILE & MANAGE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Settlements
    ├─ Dashboard
    ├─ TDR Reports
    └─ Priority Settlements

• Refunds
    ├─ Refund APIs
    ├─ Instant Refunds
    ├─ Refunds Dashboard
    └─ Product-Specific Notes

• Chargebacks
    ├─ Process & Types
    ├─ Reasons & Codes
    ├─ Closure Reasons
    ├─ Dashboard
    └─ Webhooks

• Split Settlements

• Reports
    ├─ Generate Reports
    ├─ Schedule Reports
    └─ Payouts Reports

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  PARTNER & MARKETPLACE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Partner Program
    ├─ Overview
    └─ Get Incentive

• Partner Portal
    ├─ Register
    ├─ Configure
    └─ Manage Users

• Co-Branded (OAuth) Onboarding
    ├─ Workflow
    ├─ Download Credentials
    └─ APIs

• Referral Links

• Split Settlements
    ├─ Overview — Aggregator Model       [CANONICAL OWNER]
    ├─ Onboard Sub-Merchants
    ├─ Dashboard
    └─ Payment Integration

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  BILL PAYMENTS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• BBPS
    ├─ Connect Agent API
    └─ Biller, Bill & Complaint APIs

• Recharge
    ├─ Workflow
    └─ APIs

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  API REFERENCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• API Fundamentals
    ├─ REST API Format
    ├─ Authentication & Security
    └─ Handling Redirects
         ├─ Web Checkout
         └─ Mobile SDK Checkout

• [OpenAPI Specs by Product Area]
  (auto-rendered from reference/ directory)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  DEVELOPER TOOLS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Debugging & Logs                        [★ New section — R6]
    ├─ Reading API Error Responses         [★ New]
    ├─ Common Bank Integration Errors      [★ New — bank 505 error top frustration]
    ├─ Webhook Delivery Logs              [★ New — most common debugging need]
    ├─ Transaction Debug Checklist         [★ New — step-by-step for R10]
    └─ Test vs Production Env Guide        [★ New — prevents UAT/prod confusion]

• Security & Compliance
    ├─ PCI DSS Scope by Integration Type  [★ New — T1: no scope, T2: minimal, T3: full]
    ├─ Security Checklist                 [★ New]
    ├─ Authentication Best Practices
    └─ Fraud Prevention Guidelines

• Security & Signing                      [∿ Replaces 8+ duplicate per-platform hash pages]
    └─ Hash Verification Tool

• Quickstart Code                         [★ New section — R7: surfaces recipes/ directory]
    ├─ PayU Hosted Checkout
    ├─ Merchant Hosted Checkout
    ├─ Server-to-Server (S2S)
    └─ Payment Links

• Ask AI (DevGuide Builder)               [→ Moved here + in Getting Started for dual surface]

• Webhooks                                [↑ hidden:true — P0 UNHIDE]
    ├─ Overview & Event Catalog           [fill stub HIGH PRIORITY]
    ├─ Payment Webhook Payloads           [fill stub HIGH PRIORITY]
    ├─ Subscription Webhook Payloads      [fill stub HIGH PRIORITY]
    ├─ Verify a Webhook Signature
    └─ Retry & Failure Handling           [★ New]

• Error Codes & Troubleshooting           [∿ Merge error-handling.md + payment-error-codes.json]

• Testing Reference                       [★ New — centralized sandbox page]

• Monitoring & Alerts
    ├─ PayU Overwatch
    ├─ Webhook Alerts
    └─ Incident Response                  [★ New]

• MCP & CLI
    ├─ Remote MCP Server
    │    ├─ Authentication
    │    ├─ Request Format
    │    └─ Merchant Account Management
    ├─ DevGuide Builder MCP
    ├─ PayU CLI
    └─ Agentic Commerce Suite

• Codes & Reference
    ├─ Bank Codes
    ├─ Card Type Codes
    ├─ Payment Mode Codes
    ├─ UPI Handles
    ├─ Wallet Codes
    ├─ EMI Codes
    ├─ BNPL Codes
    └─ MCC / Currency Codes

• Glossary                                [★ New — HIGH AI-READINESS IMPACT — R8]

• FAQs                                    [∿ Merge multiple FAQ files into one filterable hub]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  GO LIVE                                 [★ New top-level section — R4]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Pre-Launch Technical Checklist          [★ New — R4: top friction point #3]

• Enable Payment Methods                  [★ New — R4+R5]
    ├─ International Payments Activation
    ├─ AutoPay / UPI Mandate Activation
    ├─ COD Activation
    └─ BNPL Provider Activation

• First Production Transaction            [★ New — "integrated ≠ accepting payments" gap]

• Going Live with Webhooks                [★ New — most common go-live failure point]

• Production Monitoring Setup             [★ New]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  SOLUTION GUIDES                         [★ New top-level section]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

• Marketplace / Aggregator Business
• Subscription Business
• International Merchant
• High-Growth D2C
```

***

### 2.4 Page-Level Templates

Every page is one of seven types. Type determines structure — enforced as layouts in your docs platform, not suggestions. Templates A1 and A2 are written in production-ready MDX using the component library already in the docs platform. All other templates show the MDX component pattern to follow.

***

#### Template A1 — Tier 1 (No-Code) Product Overview Page

Used for: All 27 No-Code tier products. Entry point for non-developer merchants. Focuses on what the product does and how to start — no code, no API setup required.

**Frontmatter**

```yaml
---
title: "{Product Name}"
excerpt: "{One sentence: what it does, for whom, and one key benefit}"
tier: "tier-1"
tier_label: "No-Code"
product: "{product-slug}"
umbrella: "accept-payments"  # or whichever umbrella applies
page_type: "overview"
audience: "non-developer"
search_keywords: ["{product name}", "{alias 1}", "{alias 2}", "{key action}"]
also_known_as: ["{alias}"]  # only if needed per R8
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---
```

**Page Body**

```mdx
<Banner
  isInline={true}
  message="Integration effort: No code or website required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

## What Can I Do with {Product}?

{One sentence describing the core value. Who it's for. What problem it solves.}

- {Use case 1 — merchant-facing benefit}
- {Use case 2}
- {Use case 3}
- {Use case 4}

{Optional — embed a video if one exists:}
<Embed url="https://www.youtube.com/watch?v={video-id}" />

{Optional — CTA button linking to dashboard or an in-docs guide. Never link to Postman.}
<HTMLBlock>
  <div style="margin: 16px 0;">
    <a
      href="https://onboarding.payu.in/{relevant-section}"
      data-tooltip="{Tooltip text, e.g. 'Opens the PayU Dashboard'}"
      style="background:#15C614;color:#fff;padding:10px 20px;border-radius:6px;font-weight:bold;text-decoration:none;font-size:14px;display:inline-block;"
    >
      {CTA label, e.g. "Create a Payment Link"}
    </a>
  </div>
</HTMLBlock>

---

## Is {Product} Right for Me?

{Product} is a good choice if:

- **{Key phrase}** — {One sentence explaining this use case.}
- **{Key phrase}** — {One sentence.}
- **{Key phrase}** — {One sentence.}

Consider another PayU solution if:

- {Situation or constraint} → **{Alternative product}**
- {Situation or constraint} → **{Alternative product}**

<Callout icon="far fa-face-thinking" theme="warn">
  ### Not Sure Which PayU Solution Is Right For You?
  {Sentence about the choice being hard.} [Find the right solution →]({link to Checkout Type Quick Reference or decision guide})
</Callout>

---

## What Will I Need?

You don't need a website or developer to get started.

You'll need:

<Columns layout="fixed">
  <Column>**{Requirement 1}:** {One-sentence description. Where to get it or how to verify.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Requirement 2}:** {One-sentence description.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Requirement 3}:** {One-sentence description.}</Column>
</Columns>

{Use one flat `<Columns>` per requirement. Do NOT nest `<Columns>` inside `<Columns>`.}

---

## How do I {Core Action — e.g. "Create a Payment Link"}?

<Accordion title="1. {First step — imperative verb}" icon="far fa-{icon-name}">
  {Instructions. What to click, what to enter, what to expect.}
</Accordion>

<Accordion title="2. {Second step}" icon="far fa-{icon-name}">
  {Instructions.}
</Accordion>

<Accordion title="3. {Third step}" icon="far fa-{icon-name}">
  {Instructions.}
</Accordion>

{All Accordion titles must start with a sequential number: 1., 2., 3. — no gaps, no unnumbered steps.}

<Columns layout="fixed">
  <Column>**Need detailed steps?** See [{Guide title}]({link}) →</Column>
</Columns>

---

## How does My Customer {Action — e.g. "Pay"}?

{Include this section only for products where the merchant needs to understand the end-customer flow. Omit for purely back-office products.}

<Accordion title="1. {Customer action step 1}" icon="far fa-{icon-name}">
  {What the customer sees and does.}
</Accordion>

<Accordion title="2. {Customer action step 2}" icon="far fa-{icon-name}">
  {What the customer sees and does.}
</Accordion>

{Continue numbered steps for the full customer journey — do not skip any steps.}

{One sentence stating what the customer does NOT need — e.g. "Your customer does not need a PayU account to pay."}

---

## How do I Manage {Payments / Orders / Subscriptions}?

<Columns layout="fixed">
  <Column>**{Capability 1}:** {Description of what the merchant can do.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Capability 2}:** {Description.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Capability 3}:** {Description.}</Column>
</Columns>

{One flat `<Columns>` per capability. Never nest `<Columns>` inside `<Columns>`.}

{One sentence on what happens on payment failure or expiry and how the merchant handles it.}

---

## Next Steps

<Cards>
  <Card title="Start using {Product}" icon="far fa-{relevant-icon}">
    - **{Primary action}:** [{Link text}]({link})
    - **{Secondary action}:** [{Link text}]({link})
    - **{Tertiary action}:** [{Link text}]({link})
  </Card>
  <Card title="For Developers" icon="far fa-gear-api">
    **{API option title}:** {One sentence on what the API enables.} [{Link text}]({api-reference-link})
  </Card>
</Cards>
```

**Component rules:**

- `<Banner>` color: T1 green = `#15C614`, T2 blue = `#0077FF`, T3 orange = `#FF6B35`
- `<Accordion>` numbering must be sequential — no gaps, no unnumbered entries
- "For Developers" `<Card>` is always present even on T1 pages
- `<HTMLBlock>` CTA links only to PayU Dashboard or an in-docs guide — never Postman
- `llms.txt` routing belongs in the site-level head file, not in page body content

***

#### Template A2 — Tier 2/3 Product Overview Page

Used for: T2 (Prebuilt UI) and T3 (Developer Required) products. Audience is developers and platform builders. Emphasizes integration architecture, decision criteria, and limits.

**Frontmatter**

```yaml
---
title: "{Product Name}"
excerpt: "{One sentence: what it does, who integrates it, and the integration model}"
tier: "tier-2"           # or "tier-3" or "multi-tier"
tier_label: "Prebuilt UI"  # or "Developer Required"
product: "{product-slug}"
umbrella: "accept-payments"
page_type: "overview"
audience: "developer"    # or "platform-builder" for T3 marketplace/aggregator
experience_level: "intermediate"
prerequisites:
  - "api-authentication"
  - "hash-generation"
search_keywords: ["{product name}", "{alias}", "{integration method}"]
also_known_as: ["{alias 1}", "{alias 2}"]  # Required — R8
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---
```

**Page Body**

```mdx
<Banner
  isInline={true}
  message="{T2: 'Integration effort: A few hours with frontend code' | T3: 'Integration effort: Custom build — developer required'}"
  color="{T2: '#0077FF' | T3: '#FF6B35'}"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

<Callout icon="far fa-circle-info" theme="info">
  **Also known as**: {alias 1}, {alias 2}. Not sure which checkout to use? See the [Checkout Type Quick Reference]({link}).
</Callout>

---

## What is {Product}?

{One paragraph: technical definition, how it fits in the PayU ecosystem, and the key architectural distinction — e.g. "PayU hosts the payment page" vs "you build the payment UI."}

{Optional: flow diagram as an image or embedded visual.}

---

## When to Use {Product}

| Use this when | Consider another option if |
|---|---|
| {Condition 1 — specific, not vague} | {Alternative product} → [{link}]({link}) |
| {Condition 2} | {Alternative} |
| {Condition 3} | {Alternative} |

{T3 only — add PCI scope callout:}
<Callout icon="far fa-shield-halved" theme="warn">
  **PCI DSS scope**: Building a custom payment form means card data may touch your server. Review [PCI Scope by Integration Type]({link}) before committing to this approach.
</Callout>

---

## How It Works

{Numbered sequence for anything with more than 3 steps. Keep to essential steps only.}

1. {Step in the payment flow}
2. {Step}
3. {Step}

[→ Deep dive: Payment Flow explained]({link-to-concept-page})

---

## Prerequisites

| Requirement | Details | Where to get it |
|---|---|---|
| PayU merchant account | Active account with KYC complete | [PayU Dashboard]({link}) |
| API credentials | `key` + `salt` | Dashboard → Settings → API Keys |
| {Product-specific prereq} | {Details} | {Where} |

---

## Capabilities and Limits

**What this integration supports:**
- {Capability 1}
- {Capability 2}
- {Capability 3}

**What it does not support:**
- {Limitation 1 — important for integration commitment decisions}
- {Limitation 2}

---

## Next Steps

<Cards>
  <Card title="Integrate {Product}" icon="far fa-code">
    - **Integration guide:** [{Guide title}]({link})
    - **API reference:** [{Endpoint title}]({link})
    - **Quickstart code:** [{Language}]({link})
  </Card>
  <Card title="Test your integration" icon="far fa-flask">
    - **Test credentials:** [Get test keys]({link})
    - **Test card reference:** [Test cards]({link})
  </Card>
</Cards>
```

***

#### Template B1 — Tier 1 Dashboard Walkthrough

Used for: Step-by-step guides for non-developer merchants performing actions in the PayU Dashboard. No code. Screenshot-driven.

**Frontmatter**

```yaml
---
title: "{Action verb + outcome — e.g. 'Create a Payment Link'}"
excerpt: "{One sentence: what the merchant accomplishes and how long it takes}"
tier: "tier-1"
tier_label: "No-Code"
product: "{product-slug}"
umbrella: "{umbrella}"
page_type: "guide"
audience: "non-developer"
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---
```

**Page Body**

```mdx
<Callout icon="far fa-clock" theme="info">
  **Time**: ~{X} minutes &nbsp;|&nbsp; **What you'll need**: [{Prereq 1}]({link}), [{Prereq 2}]({link})
</Callout>

## Before You Start

{One sentence context. Link to the product overview page. Link to any account setup needed first.}

---

## Steps

<Accordion title="1. {Step — imperative verb}" icon="far fa-{icon}">
  {Where to navigate in the dashboard. What to click. What to enter.}

  {Screenshot or screen recording if available.}

  <Callout icon="far fa-lightbulb" theme="info">
    **Tip**: {Optional — useful shortcut or the most common mistake to avoid at this step.}
  </Callout>
</Accordion>

<Accordion title="2. {Step}" icon="far fa-{icon}">
  {Instructions.}
</Accordion>

<Accordion title="3. {Step}" icon="far fa-{icon}">
  {Instructions.}
</Accordion>

{All Accordion titles must be numbered consecutively — no gaps.}

---

## What Happens Next

{One paragraph: expected outcome, where to verify success, what the customer or system does after this action.}

---

## Troubleshooting

| Problem | Fix |
|---|---|
| {Common issue 1} | {Resolution — one line} |
| {Common issue 2} | {Resolution} |

---

## Related Guides

<Cards>
  <Card title="{Related action}" icon="far fa-{icon}">
    [{Link text}]({link})
  </Card>
  <Card title="{Related action}" icon="far fa-{icon}">
    [{Link text}]({link})
  </Card>
</Cards>
```

***

#### Template B2 — Tier 2/3 Integration Guide

Used for: Developer integration guides at T2 and T3. Code-first. Every step includes copyable, runnable code.

**Frontmatter**

```yaml
---
title: "{Action verb + outcome — e.g. 'Integrate Merchant Hosted Checkout'}"
excerpt: "{One sentence: what the developer builds and the concrete end state}"
tier: "tier-2"  # or tier-3
tier_label: "Prebuilt UI"  # or Developer Required
product: "{product-slug}"
umbrella: "{umbrella}"
page_type: "guide"
audience: "developer"
experience_level: "intermediate"
prerequisites:
  - "{prereq-slug}"
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---
```

**Page Body**

````mdx
<Callout icon="far fa-triangle-exclamation" theme="info">
  **Prerequisites**: [{Prereq 1}]({link}) · [{Prereq 2}]({link}) &nbsp;|&nbsp; **Time**: ~{X} hours &nbsp;|&nbsp; **Difficulty**: {Beginner / Intermediate / Advanced}
</Callout>

## What You'll Build

{One paragraph. Concrete end state. What will work when this guide is complete.}

---

## Step 1 — {Step name}

{One sentence: why this step is needed.}

{What to do.}

```{language}
// Complete, runnable code — no truncation, no ellipsis.
// Runs as-is with credentials swapped.
````

**Expected output:**

```
{What should appear in the console, browser, or API response}
```

<Callout icon="far fa-triangle-exclamation" theme="warn">
  **Common mistake**: {One-liner on the most frequent error at this step.}
</Callout>

***

## Step 2 — {Step name}

{Repeat structure: why → what → code block → expected output → common mistake callout}

***

{Repeat for all steps.}

***

## Test Your Integration

{Specific test scenario. Test credentials and test card number inline — not "see testing page."}

```{language}
// Test credentials inline here
```

Expected response:

```json
{
  "status": "success",
  "mihpayid": "..."
}
```

[Full test card reference →](\{link\})

***

## Troubleshooting

| Error                   | Likely Cause     | Fix          |
| ----------------------- | ---------------- | ------------ |
| {Error code or message} | {Why it happens} | {What to do} |
| {Error}                 | {Cause}          | {Fix}        |

Max 5 rows. [→ Full Debugging & Logs reference](\{link\}) for more.

***

## Next Steps

<Cards>
  <Card title="Verify payments" icon="far fa-circle-check">
    [\{Verify Payment API\}](\{link\})
  </Card>

  <Card title="Handle webhooks" icon="far fa-webhook">
    [\{Webhook Setup Guide\}](\{link\})
  </Card>

  <Card title="Go live" icon="far fa-rocket">
    [\{Production Checklist\}](\{link\})
  </Card>
</Cards>

````

---

#### Template C — API Endpoint Page

The most critical template for AI-readiness. Every endpoint page follows this structure exactly. LLMs parse these to generate integration code — inconsistent structure produces hallucinations.

**Frontmatter**

```yaml
---
title: "{Verb + resource — e.g. 'Create a Payment'}"
excerpt: "{Method} {endpoint path} — {one-line description of what it does}"
page_type: "api-reference"
audience: "developer"
api_method: "POST"
api_endpoint: "/merchant/postservice"
api_version: "v2"
prerequisites:
  - "api-authentication"
  - "hash-generation"
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---
````

**Page Body**

````mdx
<Banner
  isInline={true}
  message="POST  https://info.payu.in/merchant/postservice"
  color="#0077FF"
  textColor="#ffffff"
  fontSize="13px"
  fontWeight="bold"
/>

{One-line description of what this endpoint does and when to call it.}

---

## Authentication

{What credentials are required. How they are passed. The hash formula specific to this endpoint.}

[→ Hash Generation]({link})

---

## Request Headers

| Header | Type | Required | Description |
|---|---|---|---|
| Content-Type | string | Yes | `application/x-www-form-urlencoded` |
| {Header} | {type} | {Yes/No} | {description} |

---

## Request Parameters

| Parameter | Type | Required | Max Length | Description | Example |
|---|---|---|---|---|---|
| {param} | {type} | {Yes/No} | {length} | {description} | `{example}` |

All parameters documented — no "see dashboard" shortcuts.

---

## Request Example

```bash
curl -X POST https://info.payu.in/merchant/postservice \
  -d "key={your-key}" \
  -d "txnid={unique-txn-id}" \
  -d "..."
````

{Provide language toggles: cURL / PHP / Python / Java / Node.js / Go}

***

## Response Parameters

| Parameter | Type   | Description   |
| --------- | ------ | ------------- |
| {param}   | {type} | {description} |

***

## Response Examples

**200 Success**

```json
{
  "status": 1,
  "mihpayid": "...",
  "...": "..."
}
```

**Common failure cases**

```json
{
  "status": 0,
  "error": "...",
  "...": "..."
}
```

***

## Error Codes (this endpoint)

| Code   | Message   | Cause            | Fix          |
| ------ | --------- | ---------------- | ------------ |
| {code} | {message} | {why it happens} | {what to do} |

[→ Full Error Code Reference](\{link\})

***

## Code Examples

cURL first (no dependencies), then PHP, Python, Java, Node.js, Go.

***

## Related Endpoints

- [\{Endpoint name\}](\{link\})
- [\{Endpoint name\}](\{link\})
- [\{Endpoint name\}](\{link\})

***

## Changelog

| Date         | Change         |
| ------------ | -------------- |
| {YYYY-MM-DD} | {What changed} |

````

---

#### Template D — Concept Page

Used for: Hash Generation, Webhooks overview, Payment Flow, Test vs. Production.

```mdx
---
title: "How {Concept} Works"
page_type: "concept"
audience: "developer"
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---

## What It Is

{2–3 plain-language sentences. No jargon. Assume zero prior knowledge of PayU internals.}

---

## Why It Exists

{The specific problem it solves. Why PayU requires it. What would break without it.}

---

## How It Works

{Diagram for complex flows. Numbered sequence for anything with more than 3 steps.}

---

## Implementation

```{language}
{Code block — multiple languages via toggle.}
````

***

## Common Mistakes

| Mistake       | Why It Happens | Fix            |
| ------------- | -------------- | -------------- |
| {Top mistake} | {Root cause}   | {One-line fix} |
| {Mistake 2}   | {Cause}        | {Fix}          |
| {Mistake 3}   | {Cause}        | {Fix}          |

***

## Terms Defined on This Page

| Term   | Definition                                                |
| ------ | --------------------------------------------------------- |
| {term} | {Platform-specific meaning — not a dictionary definition} |
| {term} | {Definition}                                              |

**AI-readiness note:** These definitions are retrieved by the Developer MCP when generating integration code. Every concept page must have this section.

````

---

#### Template E — Troubleshooting / Error Page

Built for R6 — developers need more than just error codes; they need complete debug paths.

```mdx
---
title: "Error {Code}: {Verbatim Error Message}"
page_type: "troubleshooting"
audience: "developer"
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---

## What This Means

{Plain language — what the error tells you about the transaction state.}

---

## Common Causes

1. **{Cause 1}** — {One sentence on why this happens.}
2. **{Cause 2}** — {Why.}
3. **{Cause 3}** — {Why.}

{Ranked by frequency. 3–5 causes maximum.}

---

## How to Fix It

**If cause 1:**
{Fix — with code if applicable.}

**If cause 2:**
{Fix.}

---

## Debug Checklist

[→ Transaction Debug Checklist]({link})

---

## If You're Still Stuck

- Check [{Relevant guide}]({link})
- Contact developer support — include: `txnid`, full error response, hash input string
````

***

#### Template F — Tutorial / Recipe Page

Used for: Quickstart Code section and all `recipes/` walkthroughs. Optimized for R7 — AI-assisted developers need copyable code first, explanation second.

````mdx
---
title: "{Action} in {Language/Platform}"
excerpt: "{One sentence: what this builds and how long it takes to run}"
tier: "{tier}"
page_type: "tutorial"
audience: "developer"
experience_level: "beginner"
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---

## Full Source Code

```{language}
// Complete, runnable source code FIRST — no preamble.
// No truncation. No ellipsis. Runs as-is with credentials swapped.
````

**Prerequisites**: {Linked list}  |  **Time**: \~{X} min

***

## Overview

{What this builds, end-to-end. Where this code fits in the full payment flow.}

***

## Code Walkthrough

### {Section name — e.g. "Hash generation"}

```{language}
{Excerpt from the full code above — referenced by line numbers if helpful}
```

{Explanation of what this section does and why. No paraphrasing what the code already says.}

### {Next section}

{Continue through the complete flow.}

***

## Run It

```bash
{Install command}
{Set environment variables}
{Run command}
```

Expected output:

```
{What should appear in terminal or browser}
```

***

## What to Do Next

<Cards>
  <Card title="{Next step}" icon="far fa-{icon}">
    [\{Link text\}](\{link\})
  </Card>

  <Card title="{Next step}" icon="far fa-{icon}">
    [\{Link text\}](\{link\})
  </Card>

  <Card title="{Next step}" icon="far fa-{icon}">
    [\{Link text\}](\{link\})
  </Card>
</Cards>

````

---

## Part 3 — AI-Readiness Layer

AI-readiness is a standard applied to every page from the start of the restructure, not a separate phase.

### 3.1 Enhanced Frontmatter Schema

```yaml
---
title: "Create a Payment"
excerpt: "Submit a payment request to the PayU API and initiate a transaction."

# Tier & product classification
tier: "tier-3"                      # tier-1 | tier-2 | tier-3 | multi-tier
tier_label: "Developer Required"    # No-Code | Prebuilt UI | Developer Required
product: "merchant-hosted-checkout"
umbrella: "accept-payments"         # accept-payments | payment-methods | sdks |
                                    # increase-conversion | manage-subscriptions |
                                    # send-payouts | international-payments |
                                    # reconcile-manage | partner-marketplace |
                                    # bill-payments | api-reference |
                                    # developer-tools | go-live | solution-guides

# Page type & audience
page_type: "api-reference"          # overview | guide | api-reference | concept |
                                    # tutorial | troubleshooting
audience: "developer"               # developer | non-developer | platform-builder
experience_level: "intermediate"    # beginner | intermediate | advanced  ← R10

# Navigation
prerequisites:
  - "api-authentication"
  - "hash-generation"
related:
  - "verify-a-payment"
  - "handle-payment-response"
  - "payment-webhooks"
also_known_as:                       # R8 — drives "also known as" label on page
  - "Custom Checkout"
  - "Seamless Integration"

# Discoverability
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
````

### 3.2 Semantic Chunking

Every H2 section must be a self-contained thought answerable as a standalone RAG chunk.

Bad: `H2: Overview` / `H2: Details` / `H2: Notes`

Good: `H2: How Hash Verification Works` / `H2: Required Parameters for Hash Generation` / `H2: Common Hash Mismatch Causes`

The Debugging & Logs section (R6) is especially important here — each page answers one specific debugging question, so the chunk = the answer.

### 3.3 Glossary as Anchor Document

Minimum entries: `txnid`, `mihpayid`, `productinfo`, `salt`, `SALT2`, `SALT7`, `udf1–udf5`, `hash`, `surl`, `furl`, `postservice`, `verify_payment`, `mandate`, `si_details`, `emi_amount`, `pg`, `enforce_paymethod`, `bank_code`, `card_token`, `bnpl`, `DCC`, `LRS`, `AFT`, `VAN`, `eNACH`, `AutoPay`, `Zion`, `CheckoutPro`, `Bolt SDK`, `mihpayid vs txnid` (developers confuse these constantly). Each entry should also include its "also known as" aliases (R8).

### 3.4 MCP Server Alignment

Both MCP tools (Dev Guide MCP and Remote MCP) need: input/output schema, a worked example (prompt → tool call → response → what the agent does next), and rate limits on both. The `also_known_as` frontmatter field directly improves MCP retrieval on synonymous queries. A developer asking "how do I integrate seamless checkout?" should retrieve Merchant Hosted Checkout pages, not fail to find them.

***

## Part 4 — Migration Map

### Page Status Summary from V7

| Status                          | Count (approx.) | Action                                                 |
| ------------------------------- | --------------- | ------------------------------------------------------ |
| Exists — Unhide                 | \~8 pages       | P0: flip `hidden: false` in frontmatter                |
| Exists — Move                   | \~40+ pages     | Move file, add redirect                                |
| Exists — Merge                  | \~15 pages      | Consolidate content, add redirect from all merged URLs |
| Exists — Unhide + Build Content | \~5 pages       | Unhide and write body content                          |
| New — To Create                 | \~30+ pages     | Write from scratch                                     |

### P0 Pages: Unhide Immediately (highest impact / least effort)

These pages exist and are fully or partially built. Unhiding them is the fastest win in the entire plan.

| File                                         | Current Status                   | Action                                         | Research Impact                    |
| -------------------------------------------- | -------------------------------- | ---------------------------------------------- | ---------------------------------- |
| `docs/Quick Start/quick-start.md`            | `hidden: true`                   | Set `hidden: false`                            | Solves R1 + R2 + R8 simultaneously |
| `docs/Quick Start/who-is-setting-this-up.md` | `hidden: true`, 4-bullet shell   | Set `hidden: false` + build content            | R1                                 |
| `docs/Quick Start/what-can-you-do-next.md`   | `hidden: true`, structure exists | Set `hidden: false` + fill \[TO CONFIRM] cells | R4                                 |
| Webhooks section (`docs/Developer Tools/`)   | `hidden: true`                   | Set `hidden: false`                            | R6                                 |

### Section-Level Migration

| Current Section                                                           | Action                           | New Umbrella                                      |
| ------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------- |
| `docs/Collect Payments/introduction-no-code-payments-integration/`        | Move + restructure               | Accept Payments → No-Code                         |
| `docs/Collect Payments/ecommerce-platform-plugins/`                       | Move (add GoKwik ★)              | Accept Payments → Prebuilt → eCommerce Plugins    |
| `docs/Collect Payments/introduction-web/prebuilt-checkout-payu-hosted/`   | Move                             | Accept Payments → Prebuilt → PayU Hosted Checkout |
| `docs/Collect Payments/introduction-web/checkout-express-integration/`    | Move                             | Accept Payments → Prebuilt → CommercePro          |
| `docs/Collect Payments/introduction-web/checkout-plus-integration/`       | Move                             | Accept Payments → Prebuilt → CommercePro          |
| `docs/Collect Payments/introduction-web/custom-checkout-merchant-hosted/` | Move                             | Accept Payments → Custom → MHC                    |
| `docs/Collect Payments/introduction-web/server-to-server-integration/`    | Move                             | Accept Payments → Custom → S2S                    |
| `docs/Collect Payments/mobile-sdks/`                                      | Move, expand SDK breakdown       | SDKs → Mobile SDKs                                |
| `docs/Collect Payments/explore-server-integrations/`                      | Move                             | SDKs → Server-Side SDKs                           |
| `docs/Collect Payments/in-person-payments/`                               | Move                             | Accept Payments → Prebuilt + Custom → In-Person   |
| `docs/Offerings/introduction-to-affordability/`                           | Distribute                       | Increase Conversion                               |
| `docs/Offerings/introduction-recurring-payments-integration/`             | Move + restructure               | Manage Subscriptions                              |
| `docs/Offerings/introduction-dynamic-currency-conversion/`                | Move                             | International Payments                            |
| `docs/Offerings/introduction-cross-border-payments-import/`               | Move                             | International Payments                            |
| `docs/Offerings/introduction-refunds/`                                    | Move                             | Reconcile & Manage → Refunds                      |
| `docs/Offerings/chargeback/`                                              | Move                             | Reconcile & Manage → Chargebacks                  |
| `docs/Offerings/split-settlments/`                                        | Move (canonical owner)           | Partner & Marketplace → Split Settlements         |
| `docs/Offerings/introduction-save-cards/`                                 | Move + expand 3 models           | Accept Payments → Advanced → Save Cards           |
| `docs/Offerings/auth-and-capture-pre-authorize-card-payments/`            | Move + consolidate duplicate dir | Accept Payments → Advanced → Auth & Capture       |
| `docs/Offerings/apple-pay-integration/`                                   | Move                             | Accept Payments → Advanced → Apple Pay            |
| `docs/Offerings/native-otp-flow-integration/`                             | Move                             | Accept Payments → Advanced → Native OTP           |
| `docs/Offerings/virtual-cards-introduction/`                              | Move                             | Accept Payments → Advanced → Virtual Cards        |
| `docs/Offerings/account-funding-transaction-integration/`                 | Move                             | Accept Payments → Advanced → AFT                  |
| `docs/Offerings/introduction-to-merchant-wallet/`                         | Move                             | Accept Payments → Advanced → Merchant Wallet      |
| `docs/Offerings/mutual-funds-payments/`                                   | Move                             | Accept Payments → Advanced → Mutual Funds         |
| `docs/Offerings/banking-connect-ibmb-or-nbbl/`                            | Move                             | Accept Payments → Advanced → Banking Connect      |
| `docs/Offerings/introduction-to-payu-tpv/`                                | Move                             | Accept Payments → Advanced → TPV                  |
| `docs/Offerings/rewards-partner-integration/`                             | Move                             | Increase Conversion → Rewards                     |
| `docs/Offerings/recommendation-engine/`                                   | Move                             | Increase Conversion → Recommendation Engine       |
| `docs/Offerings/twid-rewards-integration/`                                | Move                             | Increase Conversion → Rewards                     |
| `docs/payu rewardsx/`                                                     | Add to nav + move                | Increase Conversion → Rewards                     |
| `docs/payouts/`                                                           | Move + clean stubs               | Send Payouts                                      |
| `docs/BBPS/`                                                              | Move                             | Bill Payments                                     |
| `docs/partners/`                                                          | Move + restructure               | Partner & Marketplace                             |
| `docs/MCP & CLI/` + `docs/MCP/`                                           | Merge                            | Developer Tools → MCP & CLI                       |
| `docs/Developer Tools/`                                                   | Add to nav, fill stubs           | Developer Tools → Webhooks                        |
| `docs/Whatsapp integration/`                                              | Distribute                       | Accept Payments (No-Code + Prebuilt)              |
| `docs/Payment Methods/`                                                   | Add to nav                       | Payment Methods (new umbrella)                    |
| `docs/getting started/`                                                   | Consolidate                      | Getting Started                                   |
| `docs/API basics/`                                                        | Distribute                       | API Reference + Developer Tools                   |
| `docs/Monitoring & Alerts/`                                               | Move                             | Developer Tools → Monitoring                      |
| `docs/Integration ASK AI Docs/`                                           | Merge                            | Developer Tools → Ask AI                          |
| `docs/Whatsapp integration/` (Native Payments)                            | Move                             | Accept Payments → Prebuilt                        |
| `docs/RECYCLE BIN/`                                                       | Remove from nav (done), archive  | Not in nav                                        |
| `docs/Docs For Internal Review/`                                          | Remove from public repo          | Not in public repo                                |

### Content Requiring Rewrite

These files cannot be migrated — they need to be written from scratch or substantially rebuilt:

1. **Webhook Event Catalog** — stub exists at `Developer Tools/webhooks-consolidated/events-and-payloads.md`
2. **Payment Webhook Payloads** — stub exists, write from actual payloads
3. **Subscription Webhook Payloads** — stub exists, write from actual payloads
4. `payu-affordability-widget.md` — 5 literal `[PLACEHOLDER: Screenshot]` markers in live content
5. `payouts/payouts-dashboard/eftnet.md` — 79 characters, no content
6. `quickstart-code.md` — has `// TODO: verify hash` in developer-facing example code
7. **COD documentation** — completely absent; write Overview and Enable COD pages
8. **GoKwik plugin page** — doesn't exist; write
9. **Video Guides page** — doesn't exist; write structure (links to videos, indexed by experience level)
10. **Checkout Type Quick Reference** — doesn't exist; write (addresses R8 directly)
11. **All 5 Debugging & Logs sub-pages** — new section, write all
12. **All 5 Go Live section pages** — new section, write all
13. **All 4 Solution Guides** — new section, write all
14. **Developer Setup Package + sub-pages** — new, under Who Is Setting This Up?
15. **Glossary** — write all entries; highest-ROI AI-readiness investment
16. **PCI DSS Scope by Integration Type** — write from scratch
17. All 25 sub-300-char stub files in active sections

### Redirect Strategy

Build the redirect map CSV before any file moves. Every moved URL → 301. Format:

```csv
old_slug,new_slug,http_status,reason
/docs/Collect-Payments/introduction-web/prebuilt-checkout-payu-hosted,/accept-payments/payu-hosted-checkout,301,umbrella restructure
/docs/Collect-Payments/introduction-web/custom-checkout-merchant-hosted,/accept-payments/merchant-hosted-checkout,301,umbrella restructure
/docs/Offerings/introduction-recurring-payments-integration,/manage-subscriptions,301,umbrella restructure
```

Monitor 404s in GA4 for 4 weeks post-launch. Every 404 is a missing redirect.

***

## Part 5 — What You've Missed

The V7 IA addresses most of the original gaps. The remaining items below are either still absent from V7, out of scope for V7 but needed for a world-class portal, or operational/process gaps.

**SDK version table and changelogs** — The SDKs umbrella correctly surfaces all 9 Android SDKs and 5 iOS SDKs. But there is no version table (current stable version, minimum OS requirement, last updated) on the SDK overview page, and no per-SDK changelog. Developers upgrading from v2 to v3 CheckoutPro need to know what broke. This belongs on each SDK sub-page.

**Deprecation and versioning policy** — V7 has a Changelog in the global nav, but no published policy on how long deprecated APIs remain live, how breaking changes are announced, or what the migration window is. Enterprise Tier 3 developers cannot commit without this.

**Rate Limits reference** — V7 has no Rate Limits page. Every API category needs its limits. A centralized table (API | Rate Limit | Burst Limit | Throttle Behavior | Retry guidance) is essential for platform builders designing retry logic. This should live under Developer Tools.

**Postman Collections as a first-class resource** — Postman collection JSON files exist in `reference/` but are undocumented. A sub-page under Developer Tools listing each collection with a description and import link would meaningfully reduce time-to-first-API-call.

**"Was This Helpful?" on every page** — V7 doesn't specify a per-page feedback mechanism. This is the cheapest continuous quality signal available. Pages with high "unhelpful" rates become your priority rewrite queue. Implement once at the docs platform level; costs near-zero.

**Last Reviewed timestamp surfaced visibly** — `last_reviewed` is in the proposed frontmatter schema, but V7 doesn't specify surfacing it visibly on the page. Developers look at dates. A guide with no visible date signals distrust. Surface it next to the page title or in a sidebar.

**"Edit this page" GitHub link** — One implementation line in the docs platform. Signals that docs are maintained, enables community corrections, and surfaces the last commit date naturally.

**International regulatory context page** — The International Payments umbrella has the three products (DCC, Cross-Border, LRS), but no overview page explaining the regulatory context (RBI LRS regulations, FEMA compliance, reporting requirements). Merchants integrating international payments are often blocked by compliance uncertainty before they even start the technical integration.

**Status page link** — No link to a PayU uptime/status page exists anywhere in the docs. Developers debugging a production issue need to rule out "is it me or is it PayU?" in under 30 seconds. Surface a persistent status link in the global nav or footer.

**Community surface** — Developers who exhaust the docs and support tickets have nowhere to go. A linked community (GitHub Discussions, dedicated Stack Overflow tag) referenced from the Support nav item would reduce repeat support tickets and build ecosystem trust.

***

## Phased Timeline

| Phase                                           | Duration    | Scope                                                                                                                                                                                                                                       | Unlock Condition                         |
| ----------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- |
| **Phase 0 — Immediate wins**                    | Week 1      | Unhide 4 pages (`quick-start.md`, `who-is-setting-this-up.md`, `what-can-you-do-next.md`, Webhooks). Remove RECYCLE BIN + internal review from nav. Fix 4 broken links. Remove 5 `[PLACEHOLDER]` markers. Fix `// TODO` in quickstart code. | No dependencies — do today.              |
| **Phase 1 — Foundations**                       | Weeks 2–4   | GSC/GA snapshot. Lock terminology + "also known as" table. Build redirect map CSV. Resolve Collect Payments vs. Payment Gateway canonical question. Set up GA4 events. Write Checkout Type Quick Reference (R8 — high impact, low effort).  | No files move until redirect map exists. |
| **Phase 2 — Getting Started + Accept Payments** | Weeks 5–12  | Restructure Getting Started. Restructure all of Accept Payments (No-Code, Prebuilt, Custom groups). Write Developer Setup Package (R1). Write Quickstart Code section (R7). Write GoKwik page (R9). Apply all templates.                    | Redirect map complete.                   |
| **Phase 3 — Payment Methods + SDKs**            | Weeks 13–16 | Create Payment Methods umbrella. Write COD pages (R5). Build full SDK umbrella with all Android/iOS sub-pages.                                                                                                                              | Accept Payments structure stable.        |
| **Phase 4 — Go Live section**                   | Weeks 17–19 | Write all 5 Go Live pages. Write Pre-Launch Checklist. Write Enable Payment Methods activation guides (R4+R5). Write Going Live with Webhooks.                                                                                              | —                                        |
| **Phase 5 — Remaining umbrellas**               | Weeks 20–25 | Restructure Increase Conversion, Manage Subscriptions, International, Send Payouts, Reconcile & Manage, Partner & Marketplace, BBPS.                                                                                                        | —                                        |
| **Phase 6 — Developer Tools expansion**         | Weeks 26–29 | Write Debugging & Logs (all 6 pages — R6). Write PCI DSS Scope page. Merge hash pages. Write Video Guides (R3). Write Solution Guides.                                                                                                      | —                                        |
| **Phase 7 — AI-Readiness**                      | Weeks 30–33 | Enhanced frontmatter rollout. Semantic heading audit. Write Glossary. MCP alignment. Rate Limits page. SDK Changelogs. Deprecation policy.                                                                                                  | —                                        |
| **Phase 8 — Ongoing**                           | Monthly     | GSC/GA review vs. baselines. Stale page report (`last_reviewed` > 6 months). Quarterly content audit.                                                                                                                                       | —                                        |

***

_Document version 3.0 — Updated to align with IA V7 (research-backed, 10 user research findings R1–R10). Tier strategy: T1 = No-Code, T2 = Prebuilt UI, T3 = Developer Required, used as sub-groupings within Accept Payments rather than top-level nav. Total products: 107. Top-level umbrellas: 15 (Getting Started, Accept Payments, Payment Methods, SDKs, Increase Conversion, Manage Subscriptions, Send Payouts, International Payments, Reconcile & Manage, Partner & Marketplace, Bill Payments, API Reference, Developer Tools, Go Live, Solution Guides)._
