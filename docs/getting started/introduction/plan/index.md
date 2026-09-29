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

Used for: All 27 No-Code tier products. Entry point for non-developer merchants. Primary objective: help the merchant understand the product and reach their first payment. No code, no API setup required.

**Frontmatter**

```yaml
---
title: "{Product Name}"
excerpt: "{One sentence: business outcome — e.g. 'Collect payments from customers without needing a website or developer.'}"
tier: "tier-1"
tier_label: "No-Code"
product: "{product-slug}"
umbrella: "accept-payments"  # or whichever umbrella applies
page_type: "overview"
audience: "non-developer"
search_keywords: ["{product name}", "{alias 1}", "{alias 2}", "{key action}"]
also_known_as: ["{alias}"]  # only where naming is ambiguous — R8
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---
```

**Page Body**

```mdx
<Banner
  isInline={true}
  message="🟢 No coding required"
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

{One-line business outcome — e.g. "Collect payments from customers without a website, app, or developer."}

---

## Is This Right for Me?

{Who should use it — one sentence.}

Common use cases:
- {Use case 1}
- {Use case 2}
- {Use case 3}

This is NOT the right solution if:
- {Constraint or situation} → [{Alternative product}]({link})
- {Constraint or situation} → [{Alternative product}]({link})

---

## What Can I Do with {Product}?

Focus on business outcomes, not features.

- {Outcome 1 — what the merchant accomplishes}
- {Outcome 2}
- {Outcome 3}
- {Outcome 4}

{Optional — embed a video if one exists:}
<Embed url="https://www.youtube.com/watch?v={video-id}" />

---

## What Will I Need?

You don't need a website or developer to get started.

<Columns layout="fixed">
  <Column>**{Requirement 1}:** {One sentence. Where to get it.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Requirement 2}:** {One sentence.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Requirement 3}:** {One sentence.}</Column>
</Columns>

{One flat `<Columns>` per requirement. No technical prerequisites unless genuinely required.}

---

## How Does It Work?

{Simple business flow — use → to show the sequence. Keep to one line.}

**{Create}** → **{Share}** → **{Customer pays}** → **{Payment received}**

{One sentence expanding on each step if needed. No technical detail here.}

---

## How Do I Get Started?

<HTMLBlock>
  <div style="margin: 16px 0;">
    <a
      href="https://onboarding.payu.in/{relevant-section}"
      data-tooltip="{Tooltip — e.g. 'Opens the PayU Dashboard'}"
      style="background:#15C614;color:#fff;padding:10px 20px;border-radius:6px;font-weight:bold;text-decoration:none;font-size:14px;display:inline-block;"
    >
      {CTA — e.g. "Create your first Payment Link →"}
    </a>
  </div>
</HTMLBlock>

The detailed steps are in [{Guide title}]({link-to-dedicated-guide}).

---

## How Does My Customer Pay?

<Accordion title="1. {First customer action}" icon="far fa-{icon-name}">
  {What the customer sees and does.}
</Accordion>

<Accordion title="2. {Second customer action}" icon="far fa-{icon-name}">
  {What the customer sees and does.}
</Accordion>

{Continue numbered steps through the full customer journey — no gaps, no unnumbered steps.}

{One sentence on what the customer does NOT need — e.g. "Your customer does not need a PayU account to pay."}

---

## How Do I Manage Payments?

<Columns layout="fixed">
  <Column>**{Capability 1 — e.g. "View payment status"}:** {One-sentence description.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Capability 2 — e.g. "Export transactions"}:** {One sentence.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Capability 3 — e.g. "Deactivate a link"}:** {One sentence.}</Column>
</Columns>

{One sentence: what happens on payment failure or expiry and how the merchant handles it.}

---

## Not Sure Which PayU Solution Is Right for You?

<Callout icon="far fa-face-thinking" theme="warn">
  ### Tell us what you're trying to achieve
  {One sentence: "We'll recommend the right PayU solution for your situation."}
  [Find the right solution →]({link to Quick Start Wizard / Checkout Type Quick Reference})
</Callout>

---

## Next Steps

<Cards>
  <Card title="{Primary CTA — e.g. 'Create your first payment'}" icon="far fa-{relevant-icon}">
    - **{Primary action}:** [{Link text}]({link})
    - **{Bulk / advanced action}:** [{Link text}]({link})
    - **{Related product}:** [{Link text}]({link})
  </Card>
  <Card title="For Developers" icon="far fa-gear-api">
    **{API option title}:** {One sentence on what the API enables.} [{Link text}]({api-reference-link})
  </Card>
</Cards>
```

**Component rules:**

- Banner color: T1 green = `#15C614`. Always use 🟢 emoji in the message for T1.
- `<Accordion>` numbering must be sequential — no gaps, no unnumbered entries.
- "For Developers" `<Card>` always present even on T1 — developers sometimes manage merchant integrations.
- `<HTMLBlock>` CTA links only to the PayU Dashboard or an in-docs guide — never Postman.
- `llms.txt` routing belongs in the site-level head file, not in page body content.

***

#### Template A2 — Tier 2 (Minimal Technical Effort) Product Overview Page

Used for: All 19 Prebuilt UI tier products. Primary audience: merchant + self-builder + developer. Primary objective: help the user decide whether this product is appropriate and understand what is involved before entering the technical guide.

**Frontmatter**

```yaml
---
title: "{Product Name}"
excerpt: "{One sentence: what it does and the integration model — e.g. 'Accept payments on your website through a PayU-hosted checkout page.'}"
tier: "tier-2"
tier_label: "Prebuilt UI"
product: "{product-slug}"
umbrella: "accept-payments"
page_type: "overview"
audience: "developer"
experience_level: "beginner"
prerequisites:
  - "api-authentication"
search_keywords: ["{product name}", "{alias 1}", "{alias 2}", "{integration method}"]
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
  message="🟡 Some technical setup required"
  color="#F5A623"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

<Callout icon="far fa-circle-info" theme="info">
  **Also known as**: {alias 1}, {alias 2}. Not sure which checkout to use? See the [Checkout Type Quick Reference]({link}).
</Callout>

{One-line business outcome — e.g. "Accept payments on your website through a PayU-hosted checkout."}

---

## Is This Right for Me?

Choose {Product} when:
- {Condition 1 — specific, not vague}
- {Condition 2}
- {Condition 3}

This is NOT the right solution if:
- Need a completely custom checkout → [Merchant Hosted Checkout]({link})
- No website / no technical setup → [Payment Links]({link})
- {Other constraint} → [{Alternative}]({link})

---

## What Can I Do with {Product}?

Combination of business capabilities and important product capabilities.

- {Business outcome 1}
- {Business outcome 2}
- {Product capability — e.g. "Apply your branding to the checkout page"}
- {Product capability — e.g. "Accept cards, UPI, wallets, net banking, EMI"}

---

## What Will I Need?

<Columns layout="fixed">
  <Column>**PayU merchant account:** Active account with KYC complete. [Get started]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**API credentials:** Merchant key + salt. Dashboard → Settings → API Keys.</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Website or application:** Ability to add code to your checkout page.</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Product-specific requirement}:** {One sentence.}</Column>
</Columns>

{Still an overview — not a complete technical prerequisite document. The integration guide has the full list.}

---

## How Does It Work?

{Conceptual payment/integration flow. Use → to show sequence.}

**Customer** → **Your website** → **PayU Checkout** → **Payment processed** → **Return to your site + verification**

{Optional: embed a flow diagram or architecture image here.}

{One sentence on what PayU handles vs. what the merchant is responsible for.}

[→ Deep dive: Payment Flow explained]({link-to-concept-page})

---

## How Do I Get Started?

<HTMLBlock>
  <div style="margin: 16px 0;">
    <a
      href="{link-to-integration-guide}"
      style="background:#F5A623;color:#fff;padding:10px 20px;border-radius:6px;font-weight:bold;text-decoration:none;font-size:14px;display:inline-block;"
    >
      Start {Product} integration →
    </a>
  </div>
</HTMLBlock>

The integration guide covers: **Credentials** → **Integration code** → **Hash generation** → **Testing** → **Go live**

---

## How Does My Customer Pay?

{Optional — include only if understanding the customer experience is important for this product. Keep shorter than T1. If PayU fully controls the checkout UI, this section can be a single paragraph rather than Accordions.}

{Customer reaches your checkout} → {Redirected to PayU payment page} → {Chooses payment method and pays} → {Redirected back to your site}

{One sentence on what the customer does NOT need.}

---

## What Happens After Payment?

Before entering the integration guide, understand these concepts:

<Columns layout="fixed">
  <Column>**Payment response:** {One sentence on what PayU returns and where.} [{Link to docs}]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Verification:** {One sentence on why you must verify server-side.} [{Link}]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Webhooks:** {One sentence on server-to-server notification.} [{Link}]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Success/failure handling:** {One sentence.} [{Link}]({link})</Column>
</Columns>

{Overview only — complete specifications are in the integration guide.}

---

## Not Sure Which PayU Solution Is Right for You?

<Callout icon="far fa-face-thinking" theme="warn">
  ### Not sure which PayU checkout is right for your situation?
  [Use the Quick Start Wizard →]({link}) — answer 4 questions and get a recommendation.
</Callout>

---

## Next Steps

<Cards>
  <Card title="Start integration" icon="far fa-code">
    - **Integration guide:** [{Guide title}]({link})
    - **API reference:** [{Endpoint title}]({link})
    - **Testing:** [Test your integration]({link})
  </Card>
  <Card title="Explore options" icon="far fa-arrows-left-right">
    - **Related solution:** [{Alternative product}]({link})
    - **All checkout options:** [Checkout Type Quick Reference]({link})
  </Card>
</Cards>
```

***

#### Template A3 — Tier 3 (Substantial Development Effort) Product Overview Page

Used for: All 47 Developer Required tier products. Primary audience: developer / technical integrator / agency. Primary objective: help the technical user make the correct architectural decision and enter the right implementation path quickly.

**Frontmatter**

```yaml
---
title: "{Product Name}"
excerpt: "{One sentence: technical/business outcome — e.g. 'Build a fully customized payment experience using PayU APIs.'}"
tier: "tier-3"
tier_label: "Developer Required"
product: "{product-slug}"
umbrella: "accept-payments"
page_type: "overview"
audience: "developer"  # or "platform-builder" for marketplace/aggregator products
experience_level: "intermediate"  # or "advanced" for S2S, SDKs
prerequisites:
  - "api-authentication"
  - "hash-generation"
search_keywords: ["{product name}", "{alias 1}", "{alias 2}", "{integration method}"]
also_known_as: ["{alias 1}", "{alias 2}"]  # Required — R8 (naming confusion is worst at T3)
last_reviewed: "YYYY-MM-DD"
deprecated: false
hidden: false
---
```

**Page Body**

```mdx
<Banner
  isInline={true}
  message="🔴 Significant development effort"
  color="#E53935"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

<Callout icon="far fa-circle-info" theme="info">
  **Also known as**: {alias 1}, {alias 2}. Not sure which integration to use? See the [Checkout Type Quick Reference]({link}).
</Callout>

{One-line technical/business outcome — e.g. "Build a fully customized payment experience where you control every aspect of the checkout UI."}

---

## Is This Right for Me?

{Product} is designed for:
- {What it is designed for — specific use case}
- {Situation that requires this level of control}

Choose {Product} when:
- {Condition 1 — architectural requirement}
- {Condition 2}

This is NOT the right solution if:
- Want PayU to host the checkout UI → [PayU Hosted Checkout]({link})
- Want a prebuilt embedded checkout → [CommercePro / Checkout Plus]({link})
- No developer available → [Payment Links]({link})

{This section is especially important at T3 — choosing a technically complex integration unnecessarily increases Integration TAT.}

<Callout icon="far fa-shield-halved" theme="warn">
  **PCI DSS scope note:** Building a custom payment form means card data may touch your server. Review [PCI Scope by Integration Type]({link}) before committing to this approach.
</Callout>

---

## What Can I Do with {Product}?

Focus on capabilities and control the developer gains — not marketing features.

- {Capability 1 — e.g. "Customize every aspect of the checkout UI"}
- {Capability 2 — e.g. "Control the payment experience within your application"}
- {Capability 3 — e.g. "Integrate with your existing application architecture"}
- {Capability 4 — e.g. "Control payment method selection and flows"}

---

## What Will I Need?

Still an overview — not a prerequisite manual. The integration guide has the complete list.

<Columns layout="fixed">
  <Column>**PayU merchant account:** Active account with KYC complete and production credentials. [Dashboard]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**API credentials:** Merchant key + salt + SALT2/SALT7 where applicable. Dashboard → Settings → API Keys.</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Backend server:** Ability to make server-side API calls and handle callbacks securely.</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Programming environment:** {Language/framework requirements for this specific product.}</Column>
</Columns>
<Columns layout="fixed">
  <Column>**{Product-specific technical requirement}:** {One sentence.}</Column>
</Columns>

---

## How Does It Work?

{Technical conceptual flow — not a request/response spec. Use → for sequence.}

**Your application** → **PayU API** → **Payment provider / bank** → **PayU** → **Your application (response + webhook)**

{Optional: embed an architecture or sequence diagram — use `<Embed>` for a hosted diagram or an image block.}

{One sentence on where your responsibility starts and ends vs. PayU's responsibility.}

[→ Payment Flow deep dive]({link-to-concept-page})

---

## How Do I Get Started?

<HTMLBlock>
  <div style="margin: 16px 0;">
    <a
      href="{link-to-integration-guide}"
      style="background:#E53935;color:#fff;padding:10px 20px;border-radius:6px;font-weight:bold;text-decoration:none;font-size:14px;display:inline-block;"
    >
      Start {Product} integration →
    </a>
  </div>
</HTMLBlock>

Choose the appropriate integration route:

- [{API integration guide}]({link}) — {One sentence on when to choose this route}
- [{SDK guide}]({link}) — {One sentence}
- [{Server-to-server guide}]({link}) — {One sentence}
- [{Web integration guide}]({link}) — {One sentence}

---

## How Does the Payment Flow Work?

{Technical stages at a conceptual level — NOT complete request/response specifications. Those are in the integration guide.}

**Initiate** → **Authenticate** → **Process** → **Receive response** → **Verify**

<Accordion title="1. Initiate — {brief description}" icon="far fa-play">
  {What your application does. What PayU API is called. What parameters matter. One paragraph.}
</Accordion>

<Accordion title="2. Authenticate — {brief description}" icon="far fa-lock">
  {How authentication works at this stage. Hash formula if relevant. One paragraph.}
</Accordion>

<Accordion title="3. Process — {brief description}" icon="far fa-gear">
  {What happens at the payment provider. What your application's role is. One paragraph.}
</Accordion>

<Accordion title="4. Receive response — {brief description}" icon="far fa-arrow-left">
  {How the response reaches you — surl/furl, webhook, or both. One paragraph.}
</Accordion>

<Accordion title="5. Verify — {brief description}" icon="far fa-circle-check">
  {Why you must verify server-side. What API to call. One paragraph.}
</Accordion>

---

## What Happens After Payment?

Understand these before entering the integration guide:

<Columns layout="fixed">
  <Column>**Payment response:** {One sentence.} [{Link to docs}]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Server-side verification:** {One sentence — why client-side response alone is insufficient.} [{Link}]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Webhooks:** {One sentence on server-to-server notification and when to rely on it.} [{Link}]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Idempotency:** {One sentence on duplicate payment handling.} [{Link}]({link})</Column>
</Columns>
<Columns layout="fixed">
  <Column>**Failure handling:** {One sentence on retry logic and partial failures.} [{Link}]({link})</Column>
</Columns>

{Overview only — complete specifications are in the integration guide.}

---

## Not Sure Which PayU Solution Is Right for You?

<Callout icon="far fa-face-thinking" theme="warn">
  ### Looking for a simpler integration?
  [PayU Hosted Checkout]({link}) handles the payment UI for you — less code, faster integration. [Compare options →]({link to Checkout Type Quick Reference})
</Callout>

---

## Next Steps

<Cards>
  <Card title="Start integration" icon="far fa-code">
    - **Integration guide:** [{Guide title}]({link})
    - **API reference:** [{Primary endpoint}]({link})
    - **SDK documentation:** [{SDK name}]({link})
  </Card>
  <Card title="Validate and ship" icon="far fa-rocket">
    - **Testing:** [Test your integration]({link})
    - **Go live:** [Production checklist]({link})
    - **Troubleshooting:** [Debugging & Logs]({link})
  </Card>
</Cards>
```

**Component rules across all three overview templates:**

- Banner emoji + color: 🟢 `#15C614` = T1, 🟡 `#F5A623` = T2, 🔴 `#E53935` = T3
- `also_known_as` `<Callout>` — required for T2 and T3, optional for T1
- `<HTMLBlock>` CTA button color matches the tier Banner color
- `<Accordion>` in "How Does the Payment Flow Work?" (A3) — numbered stages, not steps
- "For Developers" `<Card>` in A1 Next Steps — always present; "Explore options" `<Card>` in A2; "Validate and ship" `<Card>` in A3
- `llms.txt` routing belongs in the site-level head file, not in any page body

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

## What Do I Need Before I Start?

{One sentence context. Link to the product overview page. Link to any account setup needed first.}

---

## How Do I {Core Action — e.g. "Create a Payment Link"}?

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

## What Happens After I Complete These Steps?

{One paragraph: expected outcome, where to verify success, what the customer or system does after this action.}

---

## Something Isn't Working — What Do I Do?

| Problem | Fix |
|---|---|
| {Common issue 1} | {Resolution — one line} |
| {Common issue 2} | {Resolution} |

---

## What Should I Do Next?

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

## What Will I Build?

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

## How Do I Test My Integration?

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

## Something Isn't Working — What Do I Do?

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

## How Do I Authenticate?

{What credentials are required. How they are passed. The hash formula specific to this endpoint.}

[→ Hash Generation]({link})

---

## What Headers Do I Need to Send?

| Header | Type | Required | Description |
|---|---|---|---|
| Content-Type | string | Yes | `application/x-www-form-urlencoded` |
| {Header} | {type} | {Yes/No} | {description} |

---

## What Parameters Does This Endpoint Accept?

| Parameter | Type | Required | Max Length | Description | Example |
|---|---|---|---|---|---|
| {param} | {type} | {Yes/No} | {length} | {description} | `{example}` |

All parameters documented — no "see dashboard" shortcuts.

---

## What Does a Request Look Like?

```bash
curl -X POST https://info.payu.in/merchant/postservice \
  -d "key={your-key}" \
  -d "txnid={unique-txn-id}" \
  -d "..."
````

{Provide language toggles: cURL / PHP / Python / Java / Node.js / Go}

***

## What Does the Response Contain?

| Parameter | Type   | Description   |
| --------- | ------ | ------------- |
| {param}   | {type} | {description} |

***

## What Does the Response Look Like?

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

## What Errors Can This Endpoint Return?

| Code   | Message   | Cause            | Fix          |
| ------ | --------- | ---------------- | ------------ |
| {code} | {message} | {why it happens} | {what to do} |

[→ Full Error Code Reference](\{link\})

***

## How Do I Call This Endpoint?

cURL first (no dependencies), then PHP, Python, Java, Node.js, Go.

***

## What Else Might I Need?

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

## What Is {Concept}?

{2–3 plain-language sentences. No jargon. Assume zero prior knowledge of PayU internals.}

---

## Why Does PayU Require This?

{The specific problem it solves. Why PayU requires it. What would break without it.}

---

## How Does {Concept} Work?

{Diagram for complex flows. Numbered sequence for anything with more than 3 steps.}

---

## How Do I Implement This?

```{language}
{Code block — multiple languages via toggle.}
````

***

## What Are the Most Common Mistakes?

| Mistake       | Why It Happens | Fix            |
| ------------- | -------------- | -------------- |
| {Top mistake} | {Root cause}   | {One-line fix} |
| {Mistake 2}   | {Cause}        | {Fix}          |
| {Mistake 3}   | {Cause}        | {Fix}          |

***

## What Do These Terms Mean?

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

## What Does This Error Mean?

{Plain language — what the error tells you about the transaction state.}

---

## What Causes This Error?

1. **{Cause 1}** — {One sentence on why this happens.}
2. **{Cause 2}** — {Why.}
3. **{Cause 3}** — {Why.}

{Ranked by frequency. 3–5 causes maximum.}

---

## How Do I Fix It?

**If cause 1:**
{Fix — with code if applicable.}

**If cause 2:**
{Fix.}

---

## Where Do I Start Debugging?

[→ Transaction Debug Checklist]({link})

---

## Still Stuck?

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

## What Does the Complete Code Look Like?

```{language}
// Complete, runnable source code FIRST — no preamble.
// No truncation. No ellipsis. Runs as-is with credentials swapped.
````

**Prerequisites**: {Linked list}  |  **Time**: \~{X} min

***

## What Does This Build?

{What this builds, end-to-end. Where this code fits in the full payment flow.}

***

## How Does the Code Work?

### {Section name — e.g. "Hash generation"}

```{language}
{Excerpt from the full code above — referenced by line numbers if helpful}
```

{Explanation of what this section does and why. No paraphrasing what the code already says.}

### {Next section}

{Continue through the complete flow.}

***

## How Do I Run It?

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

## What Should I Do Next?

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
