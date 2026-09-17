---
title: 'IA Framework: Tier-Based Product Guide Patterns'
deprecated: false
hidden: true
metadata:
  robots: index
---
## Purpose

This document defines the canonical Information Architecture (IA) patterns for PayU product documentation, organised by tier. Use it when designing the page structure for any new or restructured product section.

The framework rests on one principle: **the reader thinks in terms of outcomes, not documents**. They want to accept payments, not read an Integration Guide. Every IA decision should serve that perspective.

***

## The Three Tiers

| Tier | Label                | Who It Serves                                            | Example Products                                          |
| ---- | -------------------- | -------------------------------------------------------- | --------------------------------------------------------- |
| T1   | No Technical Setup   | Merchant sets it up themselves via dashboard — no code   | Payment Links, UPI QR, COD, WhatsApp Payments             |
| T2   | Some Technical Setup | Developer or merchant with developer support — some code | Hosted Checkout, Checkout Plus, eCommerce Plugins         |
| T3   | Developer Required   | Developer-only integration — significant code            | Merchant Hosted Checkout, S2S, Mobile SDKs, Subscriptions |

The tier label is for **internal planning only**. Do not expose tiers as navigation labels. The depth of the documentation naturally communicates the complexity to the reader.

***

## Tier 1 — No Technical Setup

### Journey

```
Understand → Start → Use → Manage
```

### IA Pattern

```
[Product]
│
├── Overview
├── Get Started
├── Create / Set Up
├── How It Works         (add when the mechanism needs explanation)
├── Manage
├── Options / Capabilities
├── Troubleshooting
└── FAQs
```

### Specific Example: Payment Links

```
Payment Links
│
├── Overview
├── Get Started
├── Create a Payment Link
├── Manage Payment Links
├── Payment Link Options
├── Troubleshooting
└── FAQs
```

**Launch scope (initial version):** These 7 pages. The full IA (with sub-pages for individual dashboard actions) comes after the core pages are stable.

### Specific Example: UPI QR

```
UPI QR
│
├── Overview
├── Get Started
├── Create / Set Up UPI QR
├── Manage UPI QR
├── How It Works
├── Troubleshooting
└── FAQs
```

### What each T1 page does

**Overview** — Decision and orientation, not the complete manual. Answers: What is this? Is it right for me? What will I need? How does it work broadly? How does my customer pay? How do I manage payments? Ends with Next Steps.

**Get Started** — Action-oriented entry point. Gets the user to their first successful outcome (first payment received) as fast as possible. Structure: What you need → Create your first \[item] → Send it / Share it.

**Create / Set Up** — The actual task guide. Shows the creation workflow step by step. If there are multiple creation methods, split them into sub-pages only when the workflows are materially different.

**Manage** — Dashboard-driven workflow: view, edit, cancel, resend, deactivate, check status. Start as one page, split to child pages only when individual tasks become sufficiently complex.

**Options / Capabilities** — Configuration concepts: expiry, partial payments, notifications, customer details, payment methods. Task = page. Configuration concept = section within this page, unless complexity justifies its own page.

**Troubleshooting** — Separate because the user intent is different: "I already tried it and something isn't working." Structure by symptom, not by system component.

**FAQs** — Questions that don't naturally belong to any workflow page. Not a dumping ground for documentation that should have its own page.

### Key principles for T1

- Do not turn a no-code product into a pseudo-developer guide. The merchant should reach their first payment without seeing API or SDK concepts.
- Do not create a 15-page IA because there are 15 possible topics. Start with the minimum set; split pages only when content volume and user intent justify it.
- API reference for T1 products is advanced/secondary. It does not belong in the main product nav. Link to it from a "For Developers" callout or the Developer Tools section.

***

## Tier 2 — Some Technical Setup

### Journey

```
Understand → Decide → Prepare → Integrate → Test → Go Live
```

### IA Pattern

```
[Product]
│
├── Overview
├── Get Started
│   ├── Is [Product] Right for Me?
│   ├── What You Will Need
│   ├── Choose Your Integration
│   └── Quick Start
├── How It Works
│   ├── Payment Flow
│   ├── Request and Response Flow
│   └── Payment Status
├── Integration Guide
│   ├── Prerequisites
│   ├── Build the Integration
│   ├── Handle Payment Response
│   ├── Verify Payment
│   └── Handle Webhooks
├── Customize
├── Test Your Integration
│   ├── Test Environment
│   ├── Test Payments
│   └── Test Scenarios
├── Go Live
│   ├── Go-Live Checklist
│   ├── Switch to Production
│   └── Production Validation
├── Best Practices
├── Troubleshooting
├── FAQs
└── Related Solutions
```

### Specific Example: Hosted Checkout

```
PayU Hosted Checkout
│
├── Overview
├── Get Started
│   ├── Is Hosted Checkout Right for Me?
│   ├── What You Will Need
│   ├── Choose Your Integration
│   └── Quick Start
├── How Hosted Checkout Works
│   ├── Payment Flow
│   ├── Request and Response Flow
│   └── Payment Status
├── Integration Guide
│   ├── Prerequisites
│   ├── Set Up Credentials
│   ├── Build the Integration
│   ├── Handle Payment Response
│   ├── Verify Payment
│   └── Handle Webhooks
├── Customize Checkout
│   ├── Checkout Configuration
│   ├── Branding / Customization
│   └── Payment Methods
├── Test Your Integration
│   ├── Test Environment
│   ├── Test Payments
│   └── Test Scenarios
├── Go Live
│   ├── Go-Live Checklist
│   ├── Switch to Production
│   └── Production Validation
├── Best Practices
├── Troubleshooting
├── FAQs
└── Related Solutions
    ├── Payment Links
    └── Merchant Hosted Checkout
```

### Specific Example: Plugins (Tier 2B)

Do not treat every plugin as an independent product guide. One parent page + platform-specific child pages:

```
Plugins
│
├── Overview
├── Choose Your Platform
├── Shopify
│   ├── Overview
│   ├── Prerequisites
│   ├── Install
│   ├── Configure
│   ├── Test
│   ├── Go Live
│   └── Troubleshooting
├── WooCommerce
│   ├── (same 7-page structure)
├── Magento
│   ├── (same 7-page structure)
└── Other Platforms
```

The parent "Overview" answers: "Can I connect PayU to my existing platform without building from scratch?"
Each platform page answers: "How do I connect PayU to \[Platform]?"

**Plugin page template (every platform, no exceptions):**
Overview → Prerequisites → Install → Configure PayU → Test Payments → Go Live → Troubleshooting → FAQs

Do not add "What is a payment gateway?" or "How payments work?" to individual plugin pages. Those belong in shared conceptual documentation.

### What each T2 page does (vs T1)

**Overview vs Integration Guide** — Keep these strictly separate.

- Overview answers: "Should I use this, and what does it involve?"
- Integration Guide answers: "How exactly do I integrate it?"
- Hash generation, every API parameter, complete request/response specs, every callback field — these go in the Integration Guide, not the Overview.

**How It Works** — T2 users need to understand the architecture before coding. Show the complete data flow: Customer → Your Website → PayU → Payment → PayU → Response/Webhook → Your System. This is a conceptual page, not implementation instructions.

**Integration Guide** — The technical core. Structure: Prerequisites → Build → Handle → Verify. Then Test and Go Live are separate steps, not sub-sections of Integration Guide.

**The developer journey:**

```
Prepare (Prerequisites + Credentials)
  ↓
Build (Integration Guide)
  ↓
Handle (Payment Response + Verify + Webhooks)
  ↓
Test (Test Your Integration)
  ↓
Go Live
```

***

## Tier 3 — Developer Required

The Subscriptions documentation provides the reference model for T3 complexity. Key additions over T2:

```
[Product]
│
├── Getting Started
├── Use Cases
├── Architecture / Lifecycle
├── Core Integration Guide
├── Product Concepts (domain-specific)
├── Configuration
├── APIs / SDKs
├── Webhooks & Events (detailed event catalog)
├── Testing
├── Best Practices
├── Advanced / Special Cases
├── Troubleshooting
├── Production / Go Live
├── Reference
└── FAQs
```

T3 adds: domain lifecycle, product concepts, detailed webhooks and event catalog, retry logic, advanced/special cases, and a full reference section.

### Applying the right depth by section

| Section           | T1                   | T2                | T3       |
| ----------------- | -------------------- | ----------------- | -------- |
| Getting Started   | ✅                    | ✅                 | ✅        |
| Use Cases         | ✅                    | ✅                 | ✅        |
| Lifecycle         | Simple               | Conceptual        | Detailed |
| Integration Guide | ❌ / light            | ✅                 | ✅        |
| Dashboard         | ✅                    | Maybe             | Maybe    |
| Best Practices    | Light                | ✅                 | ✅        |
| Retry Logic       | Only if relevant     | If relevant       | ✅        |
| Webhooks          | Usually separate     | Conceptual + link | Detailed |
| Troubleshooting   | ✅                    | ✅                 | ✅        |
| APIs              | Advanced / secondary | Reference link    | Core     |
| FAQs              | ✅                    | ✅                 | ✅        |
| Special Cases     | Rare                 | Some              | ✅        |

***

## Principles That Apply to All Tiers

### 1. Task = page; concept = section

Create a page when a user has a distinct job to be done. Do not create a page for every parameter or configuration option — those are sections within the relevant task page.

### 2. Don't create the full IA on launch

Start with the minimum page set. A compact, complete 7-page T1 guide is better than a 15-page guide where 8 pages are stubs. Split pages only when content volume and user intent justify a separate page.

### 3. One canonical solution-selection experience

The Integration Path Recommender (`/start-here` → `<PayUQuickStartWizard />`) is the single decision tree. Product pages do not replicate it. Product overview pages have one contextual CTA:

> "Not sure if Hosted Checkout is right for you? → Choose a PayU solution"

Do not embed a separate decision tree inside every product.

### 4. Make Integration Guide the path, not the product

Old structure (avoid):

```
Payment Gateway
├── Integration Guide
├── API Reference
├── Webhooks
└── FAQs
```

New structure (use):

```
Payment Gateway
├── Overview
├── Get Started
├── How It Works
├── Integration Guide
├── Customize
├── Test
├── Go Live
└── Troubleshooting
```

The user thinks "I want to accept payments," not "I want to read the Integration Guide."

### 5. "Also known as" labels on aliased products

PayU has naming inconsistency (Hosted Checkout / Standard Checkout; Checkout Plus / CommercePro). Every overview page for an aliased product must include a `<Callout>` naming all known aliases on the first screen. This directly addresses research finding R8 (checkout naming confusion).

### 6. API reference placement by tier

| Tier | API Reference Placement                                                                   |
| ---- | ----------------------------------------------------------------------------------------- |
| T1   | Not in main product nav. Link from a "For Developers" callout or Developer Tools section. |
| T2   | Under Integration Guide as a sub-page or linked reference.                                |
| T3   | Core section of the product guide.                                                        |

***

## Competitor Reference

These patterns are consistent with how Razorpay and Adyen structure equivalent documentation:

- **Razorpay** explicitly separates Web Integration, eCommerce Plugins, and Mobile Integration rather than forcing plugins into the same technical flow as custom API integrations. Standard Checkout has a dedicated integration sequence: Build Integration → Test Integration → Go-live Checklist.

- **Adyen** separates conceptual integration architecture from detailed implementation. Its integration page compares Hosted Checkout and Drop-in based on implementation effort, UI, server-side requirements, and capabilities before routing the user into the selected path. Online-payments documentation explicitly describes the payment server, client website/app, and webhook server as distinct integration components.
