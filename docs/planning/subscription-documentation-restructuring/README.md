# PayU Subscription Documentation Restructuring — Master Deliverable

**Status:** Ready for ReadMe CMS implementation  
**Target section slug:** `payu-subscriptions`  
**Source sections:** `introduction-recurring-payments-integration`, `internal-subscripions-or-recurring-payments`, `reference/Subscriptions`, `reference/ZION`, cross-border subscription docs, TPV recurring docs, subscription webhooks, `recurring-and-si-errors`  
**Date:** July 5, 2026

---

## 1. Updated Documentation Hierarchy

```
PayU Subscriptions (payu-subscriptions)
│
├── Getting Started
│   ├── Quick Start Guide
│   └── First Successful Subscription
│
├── Billing Lifecycle
│   ├── Subscription Lifecycle Overview
│   ├── Charge Lifecycle
│   ├── Mandate States and Transitions
│   └── Pre-Debit and Recurring Debit Flow
│
├── Subscription Use Cases
│   ├── Industry Use Cases
│   ├── Billing Models
│   └── Pay and Subscribe
│
├── Plans and Mandates
│   ├── What Is a Plan?
│   ├── Plans vs Without Plans
│   ├── Plan Lifecycle and Actions
│   └── Mandate Management
│
├── Core Integration Guide
│   ├── Choose Your Integration Path
│   ├── Build Integration
│   │   ├── PayU Hosted Checkout
│   │   ├── Merchant Hosted Checkout
│   │   │   ├── Cards
│   │   │   ├── Net Banking and eNACH
│   │   │   └── UPI Autopay
│   │   ├── Parallel Sequencing (UPI)
│   │   └── Pay and Subscribe
│   ├── Test Integration
│   └── Go-Live Checklist
│
├── Dashboard Integration (No-Code)
│   ├── Overview
│   ├── Create Subscription Payment Links
│   ├── Bulk Registration Upload
│   ├── Bulk Recurring Upload
│   ├── Manage Bulk Uploads
│   └── Access Mandates
│
├── Retry Logic
│   ├── Overview
│   ├── Cards and UPI Retry Behavior
│   ├── Net Banking Retry Behavior
│   └── Zion Automatic Retries
│
├── Supported Banks and Apps
│   ├── Cards and Networks
│   ├── Net Banking and eNACH Bank Codes
│   └── UPI Apps and Handles
│
├── Zion Subscription Automation
│   ├── Overview and When to Use Zion
│   ├── Zion Workflow
│   ├── Supported Payment Instruments
│   ├── Define and Manage Subscriptions
│   ├── Invoices and Billing
│   └── Zion FAQs
│
├── International and Special Cases
│   ├── International Cards (SI)
│   ├── Tokenization Impact on Recurring
│   ├── Cross-Border Subscriptions
│   └── TPV Recurring and Autopay
│
├── Webhooks and Events
│   ├── Subscription Webhook Overview
│   ├── Zion Subscription Webhooks
│   ├── Issuer Bank Mandate Webhooks
│   └── Sample Payloads
│
├── Troubleshooting Guide
│   ├── Mandate Registration Failures
│   ├── Pre-Debit Failures
│   ├── Recurring Debit Failures
│   └── Error Code Reference
│
├── Subscription APIs (Reference Index)
│   └── API Catalog with one-line descriptions
│
└── FAQs
    ├── General Subscriptions FAQs
    └── Tokenization FAQs
```

**API Reference (separate ReadMe Reference section — unchanged location, reordered nav):**

```
reference/Subscriptions/
├── Consent / Registration
├── Pre-Debit Notification
├── Recurring Debit (si_transaction)
├── Mandate Management (Cards, NB, UPI)
├── SI Parameter Reference
├── Update SI / Tokenization
└── Parallel Sequencing APIs

reference/ZION/
├── Manage Subscriptions
├── Manage Invoices
└── Subscription Lifecycle Webhooks
```

---

## 2. Content Mapping (Existing → New)

### Getting Started

| New Page | Source Content | Action |
|----------|----------------|--------|
| **Quick Start Guide** | `introduction-recurring-payments-integration/index.md` | Rewrite: merge value props from `internal-subscripions-or-recurring-payments/index.md`; add decision tree, supported modes table, integration path comparison |
| **First Successful Subscription** | `using-api-integration-recurring-payments/index.md`, `customer-experience-and-workflow-recurring-payments/index.md`, internal `subscriptions-integration/index.md` | **New page**: end-to-end happy path (consent → pre-debit → recurring debit) with verification checkpoints per payment mode |

### Billing Lifecycle

| New Page | Source Content | Action |
|----------|----------------|--------|
| **Subscription Lifecycle Overview** | `internal-subscripions-or-recurring-payments/understanding-subscription-workflow-and-states.md` | Rewrite; add lifecycle diagram (currently placeholder) |
| **Charge Lifecycle** | `customer-experience-and-workflow-recurring-payments/*` (cards, UPI, NB) | Split customer UX into merchant-facing charge lifecycle |
| **Mandate States and Transitions** | `understanding-subscription-states.md` | Promote from hidden internal section; expand with UPI pause/resume |
| **Pre-Debit and Recurring Debit Flow** | `using-api-integration-recurring-payments/index.md`, `recurring_payment_api.md`, `pre_debit_notification_api.md` | Guide-only narrative; link to API reference |

### Subscription Use Cases

| New Page | Source Content | Action |
|----------|----------------|--------|
| **Industry Use Cases** | `internal-subscripions-or-recurring-payments/index.md` (Industry-Specific Solutions) | Move and trim marketing examples |
| **Billing Models** | `internal-subscripions-or-recurring-payments/index.md` (Billing Models table) | Promote as standalone page with `si_details` mapping |
| **Pay and Subscribe** | `pay-and-subscribe-mandate-experience.md`, `pay-and-subscribe-consent-transaction.md` | Merge guide + link to API ref |

### Plans and Mandates

| New Page | Source Content | Action |
|----------|----------------|--------|
| **What Is a Plan?** | `using-zion-subscription-automation-platform/understanding-plan.md` | Split: conceptual plan definition |
| **Plans vs Without Plans** | `using-zion-subscription-automation-platform/index.md`, `using-api-integration-recurring-payments/index.md` | **New**: decision guide (API-only SI vs Zion plans) |
| **Plan Lifecycle and Actions** | `understanding-plan.md`, `reference/_TEST/*plan*` (deprecated) | Document Zion plan association; flag deprecated plan APIs |
| **Mandate Management** | `manage-recurring-payment-for-cards/*`, `manage-recurring-payments-for-net-banking/*`, `api-commands-to-manage-upi-recurring-transaction/*` | Task-oriented guide: pause, modify, cancel, check status |

### Core Integration Guide

| New Page | Source Content | Action |
|----------|----------------|--------|
| **Choose Your Integration Path** | `introduction-recurring-payments-integration/index.md` (Choose the Method) | Rewrite as decision matrix |
| **Build Integration → PayU Hosted** | `payment-consent-transaction-payu-hosted.md`, `payu-hosted-integration-subscriptions.md` (internal) | Consolidate; remove duplicate internal copy |
| **Build Integration → Cards (Merchant Hosted)** | `cards-subscription-integration-merchant-hosted-checkout.md` (internal), `credit-card-recurring-payment-consent-transaction.md` | Promote internal integration guide; API details stay in reference |
| **Build Integration → Net Banking** | `net-banking-subscriptions-integration-merchant-hosted.md`, `net-banking-experience.md` | Merge; **delete** `copy-of-net-banking-integration-merchant-hosted.md` |
| **Build Integration → UPI Autopay** | `upi-subscriptions-integration-merchant-hosted-checkout.md`, `upi-recurring-payment-experience-for-upi.md` | Merge guide content |
| **Parallel Sequencing (UPI)** | `integrate-parallel-sequencing-for-upi-autopay.md`, parallel sequencing API refs | Unhide; add when-to-use guidance |
| **Test Integration** | Scattered test mentions in integration guides, Integration Lab link | **New**: sandbox checklist, test cards/VPA, verify_payment |
| **Go-Live Checklist** | `review-faqs-for-recurring-payments.md` (scattered), account enablement callouts | **New**: consolidated checklist |

### Dashboard Integration (No-Code)

| New Page | Source Content | Action |
|----------|----------------|--------|
| All dashboard pages | `subscription-dashboard/*`, `create-a-payment-link-with-si.md` | Relocate under new section; deprecate `deprecated-recurring-payments-using-payubiz-dashboard/` (redirect) |

### Retry Logic

| New Page | Source Content | Action |
|----------|----------------|--------|
| **Overview** | `review-faqs-for-recurring-payments.md`, Zion FAQs, integration guides (status=0) | **New**: synthesize scattered retry guidance |
| **Cards and UPI** | `recurring-and-si-errors.md` (E4682, E4683), pre-debit status responses | Document merchant-initiated retry rules |
| **Net Banking** | NB integration guides | Document NB-specific retry (no pre-debit retry path) |
| **Zion Automatic Retries** | `faqs-zion-integration.md` (3-day retry) | Extract Zion-specific behavior |

### Supported Banks and Apps

| New Page | Source Content | Action |
|----------|----------------|--------|
| **Net Banking Bank Codes** | `bank-codes-recurring-payments.md` | Relocate; keep as reference table |
| **UPI Apps and Handles** | FAQ links to `upi-handles`, Zion supported instruments | Consolidate links |
| **Cards and Networks** | `supported-payment-instruments-by-zion.md`, BIN info references | New summary page |

### Zion Subscription Automation

| New Page | Source Content | Action |
|----------|----------------|--------|
| All Zion pages | `using-zion-subscription-automation-platform/*`, `reference/ZION/*` | Relocate guides; keep API in reference; dedupe webhooks |

### International and Special Cases

| New Page | Source Content | Action |
|----------|----------------|--------|
| **International Cards** | `international-cards-integration-recurring-payments.md` | Relocate |
| **Tokenization Impact** | `impact-of-tokenization-on-recurring-payments.md`, tokenization FAQs | Merge |
| **Cross-Border Subscriptions** | `cb-subscription-integration-seamless/*`, `reference/Cross-border Payments/subscriptions-*` | Guide in docs; API in reference; remove duplicate hidden reference hub |
| **TPV Recurring** | `tpv-recurring-payments-integration-pay-hosted-checkout.md`, UPI TPV autopay pages | Cross-link from subscriptions (not duplicate TPV section) |

### Webhooks and Events

| New Page | Source Content | Action |
|----------|----------------|--------|
| **Subscription Webhook Overview** | `webhooks-consolidated/subscription-webhooks/index.md` | Unify entry point |
| **Zion Webhooks** | `webhooks-for-subscription.md`, `subscription-life-cycle-and-role-of-webhooks-.md` | Merge; fix trailing hyphen slug |
| **Issuer Bank Webhooks** | `set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank.md` | Link from guide |
| **Sample Payloads** | `sample-payloads-subscription-webhooks.md` | **Populate** (currently empty) from `webhooks-for-subscription.md` examples |

### Troubleshooting Guide

| New Page | Source Content | Action |
|----------|----------------|--------|
| All troubleshooting | `recurring-and-si-errors.md` (680 lines), FAQ troubleshooting sections | **Unhide**; split by failure phase; keep searchable error table |

### Subscription APIs

| New Page | Source Content | Action |
|----------|----------------|--------|
| **API Catalog** | `reference/Subscriptions/_order.yaml`, `reference/ZION/_order.yaml` | New index with one-line descriptions and task-based grouping |

### FAQs

| New Page | Source Content | Action |
|----------|----------------|--------|
| **General FAQs** | `faqs-recurring-payments.md` | Keep; remove overlap with review copy |
| **Tokenization FAQs** | Section from `faqs-recurring-payments.md` | Optional split for discoverability |

### Deprecate / Remove

| Page | Reason |
|------|--------|
| `internal-subscripions-or-recurring-payments/*` | Content migrated; section hidden |
| `copy-of-using-api-integration.md` | Duplicate |
| `copy-of-net-banking-integration-merchant-hosted.md` | Duplicate |
| `payment-consent-transaction-using-payu-hosted-checkout-copy.md` | Mislabeled duplicate |
| `review-faqs-for-recurring-payments.md` | Merge into FAQs + Troubleshooting |
| `deprecated-recurring-payments-using-payubiz-dashboard/*` | Redirect to Dashboard Integration |
| `reference/_TEST/*plan*` APIs | Keep hidden; link from Plans page as deprecated |
| `validate_vpa_api-old.md` | Orphan backup |

---

## 3. Missing Documentation Report

| Priority | Gap | Recommended Action |
|----------|-----|-------------------|
| **P0** | **Retry Logic** — no dedicated guide; behavior scattered across FAQs, errors, Zion docs | Create `retry-logic/` section (included in scaffold) |
| **P0** | **Go-Live Checklist** — enablement steps only in callouts | Create checklist: account enablement, webhook URLs, test transactions, production keys, compliance |
| **P0** | **Test Integration** — no unified sandbox guide for subscriptions | Create test guide: UAT limits, test VPAs, verify_payment, mandate status polling |
| **P0** | **First Successful Subscription** — no single happy-path walkthrough | Create step-by-step with expected responses per mode |
| **P1** | **Lifecycle diagrams** — placeholders in workflow pages | Add mermaid/PNG: subscription states, charge flow, UPI pre-debit timeline |
| **P1** | **Plan APIs** — `understanding-plan.md` references APIs only in `_TEST`/deprecated | Confirm with product: publish live Plan APIs or document Zion-only plan definition via Define Subscription API |
| **P1** | **Sample webhook payloads page** — empty | Populate from existing Zion webhook doc examples |
| **P1** | **Subscription enablement self-service** — "contact KAM" with no SLA/alternatives | Add: support email, dashboard request flow, expected turnaround |
| **P2** | **iOS/Android SDK recurring setup** — only iOS doc exists | Cross-link `ios-coresdk-setup-recurring-payments.md`; add Android if available |
| **P2** | **Mutual funds recurring** — separate offering section | Cross-link from Use Cases |
| **P2** | **Saved card consent flow** — API hidden (`consenttransactionwithsavedcards.md`) | Document when to use saved-card consent vs fresh registration |
| **P2** | **UPI Collect sunset (Feb 2026)** — mentioned only on intro page | Prominent callout in UPI integration + Supported Apps |
| **P3** | **eNACH interoperability** — FAQ says "in development" | Add status tracking note; update when released |
| **P3** | **Merchant retry rate limits** — not documented | Confirm with engineering and document |

---

## 4. Duplicate Content Report

| Topic | Duplicate Locations | Canonical Page |
|-------|---------------------|----------------|
| Subscriptions introduction | `introduction-recurring-payments-integration/index.md`, `internal-subscripions-or-recurring-payments/index.md` | **Quick Start Guide** |
| API integration overview | `using-api-integration-recurring-payments/index.md`, `copy-of-using-api-integration.md` | **Core Integration → Build Integration** |
| Net Banking integration | `net-banking-subscriptions-integration-merchant-hosted.md`, `copy-of-net-banking-integration-merchant-hosted.md` | **Build Integration → Net Banking** |
| Customer experience / workflow | Public `customer-experience-and-workflow-recurring-payments/*`, internal `copy-of-customer-experience-and-workflow/*` (stubs) | **Billing Lifecycle + Use Cases** |
| Zion webhooks | `webhooks-for-subscription.md`, `subscription-life-cycle-and-role-of-webhooks-.md`, `subscription-webhooks/index.md` | **Webhooks → Zion Subscription Webhooks** |
| FAQs | `faqs-recurring-payments.md`, `review-faqs-for-recurring-payments.md`, scattered Zion FAQs | **FAQs** (split Zion to Zion section) |
| Cross-border subscriptions | `cb-subscription-integration-seamless/index.md`, `reference/.../subscriptions-with-cross-border-payments/index.md`, `_TEST/recurring-payments-cb.md` | **International → Cross-Border** (guide) + reference APIs |
| Card modify/cancel | Domestic + `cb-modify-recurring-payments-for-a-visamaster-card.md` | Reference APIs with CB variant linked from International |
| Dashboard zero-code | `subscription-dashboard/*`, `deprecated-recurring-payments-using-payubiz-dashboard/*`, `create-a-payment-link-with-si.md` | **Dashboard Integration** |
| PayU Hosted consent | `payment-consent-transaction-payu-hosted.md`, `payment-consent-transaction-using-payu-hosted-checkout-copy.md`, internal `payu-hosted-integration-subscriptions.md` | **Build Integration → PayU Hosted** |
| Subscription states | `understanding-subscription-states.md`, Zion lifecycle doc, scattered status tables | **Billing Lifecycle → Mandate States** |
| Pre-debit / recurring narrative | Every per-mode integration guide repeats same API sequence | Extract to **Billing Lifecycle → Pre-Debit and Recurring Debit Flow**; per-mode guides link back |

**Estimated duplicate content reduction:** ~35–40% fewer guide words after consolidation.

---

## 5. DevEx Improvement Summary

| Metric | Current State | After Restructure |
|--------|---------------|-------------------|
| **Time to First Successful Subscription** | Developer must read intro → choose path → per-mode docs → API ref | Quick Start → First Successful Subscription → mode-specific build page |
| **Time to Go Live** | Go-live steps buried in FAQs and callouts | Dedicated Go-Live Checklist with verification |
| **Documentation Search Time** | ~120 files across 6+ top-level sections | Single `payu-subscriptions` section with 14 top-level categories |
| **Context Switching** | Guides mixed with API params; internal review copy duplicates public | Guides vs Reference separation enforced |
| **Integration Errors** | Error doc hidden; pre-debit timing rules repeated inconsistently | Public Troubleshooting + Retry Logic with phase-based navigation |
| **Failed Go-Lives** | Missing test guide and enablement clarity | Test Integration + enablement self-service path |
| **Navigation dead ends** | Hidden pages in nav, stub customer journey pages, deprecated dashboard without redirects | Redirects, populated stubs, next-step links on every page |
| **Terminology** | "Subscripions", "Predebit", "SI" used interchangeably | Standardize: **Subscription** (product), **Mandate** (bank consent), **Standing Instruction (SI)** (API field), **Consent transaction** (first charge) |

---

## 6. AI-Readiness Assessment

| Criterion | Current Score (1–5) | Target | Gap / Fix |
|-----------|---------------------|--------|-----------|
| Clear page objective | 2 | 5 | Add **Purpose** and **When to use** blocks to every page (template in scaffold) |
| Prerequisites explicit | 2 | 5 | Account enablement, API keys, webhook URL, payment mode choice on every integration page |
| Self-contained workflows | 2 | 5 | First Successful Subscription + per-task pages |
| Request/response examples | 4 | 5 | Strong in API ref; guides need expected outcome + sample response per step |
| Failure scenarios | 3 | 5 | Unhide errors; add per-step failure table in integration guides |
| Related links | 3 | 5 | Automated "Related Pages" and "Next Step" footers |
| Hidden assumptions | 2 | 5 | Document: 24h pre-debit rule, UPI Collect sunset, tokenization requirements, TPV differences |
| Parameter explanations | 4 | 5 | `si-parameter-json-details` is good; link from every guide mentioning `si_details` |
| Verification steps | 2 | 5 | Add **Verification** section with `verify_payment`, mandate status APIs, webhook events |
| Chunking for RAG | 2 | 5 | Split 680-line error doc and 1100-line CB NB doc into phase-based pages |

**Overall AI-readiness:** 2.6 / 5 → **Target 4.5 / 5** after P0–P1 implementation.

**AI optimization patterns applied in new pages:**
- H2 sections match required template (Purpose, Prerequisites, Workflow, etc.)
- Task verbs in titles ("Create a Subscription", not "Subscription Object")
- Explicit expected outcomes after each step
- Error codes linked to Troubleshooting entries
- `llms.txt` / section index page recommended for ReadMe AI features

---

## 7. Support Ticket Reduction Opportunities

| Support Question (Inferred) | Root Documentation Gap | Fix |
|-----------------------------|------------------------|-----|
| "How do I enable Subscriptions on my account?" | Only "contact KAM" callout | Go-Live Checklist + enablement request process |
| "Why did pre-debit fail with status 0?" | Buried in integration guide tables | Troubleshooting → Pre-Debit Failures + Retry Logic |
| "Can I debit before 24 hours after pre-debit?" | Mentioned in FAQs only | Billing Lifecycle timeline + prominent callout |
| "Card not supported for recurring" | FAQ answer exists | Troubleshooting entry + link to Get BIN Info API |
| "Difference between Zion and API integration?" | Scattered comparison tables | Quick Start decision tree |
| "How to test UPI Autopay in sandbox?" | No dedicated test guide | Test Integration page |
| "Webhook not received for subscription" | Notes "contact PayU during onboarding" | Webhooks setup checklist + event list + retry delivery guidance |
| "How to migrate existing mandates after tokenization?" | FAQ only | International/Special Cases → Tokenization + Update SI workflow |
| "UPI Collect not working" | Sunset note on intro only | Supported Apps + UPI integration callout |
| "Bulk upload failed — how to retry?" | Dashboard doc mentions retry | Dashboard → Manage Bulk Uploads + Troubleshooting |
| "E4682 — debit already in progress" | Hidden error doc | Public error reference + "do not retry" guidance |
| "What billing cycle values are valid?" | Internal billing models table only | Plans and Mandates + `si_details` link |

**Estimated ticket deflection:** 60–70% of recurring-payment integration tickets address the above 12 themes.

---

## 8. Final Implementation Roadmap (Priority Order)

### Phase 1 — Foundation (P0, Week 1–2 equivalent effort)

1. Create `payu-subscriptions` ReadMe section with `_order.yaml` and 14 top-level categories
2. Publish **Quick Start Guide** and **First Successful Subscription** (rewrite from existing)
3. Publish **Billing Lifecycle** quartet (promote hidden state/workflow content)
4. Unhide and split **Troubleshooting Guide** from `recurring-and-si-errors.md`
5. Create **Retry Logic** section (new synthesis)
6. Add **Go-Live Checklist** and **Test Integration**
7. Set redirects from `introduction-recurring-payments-integration` → `payu-subscriptions`
8. Fix title typo "Subscripions" globally

### Phase 2 — Integration Guides (P0–P1)

9. Consolidate **Core Integration Guide** (promote internal `subscriptions-integration/*`)
10. Relocate **Dashboard Integration**; deprecate old dashboard section with redirects
11. Publish **Plans and Mandates** (including Zion plan gap callout)
12. Consolidate **Webhooks and Events**; populate sample payloads
13. Reorder **reference/Subscriptions** nav to match task flow (consent → pre-debit → recurring → manage)

### Phase 3 — Reference and Special Cases (P1)

14. Create **Subscription APIs** catalog index page
15. Relocate **Supported Banks and Apps**
16. Consolidate **International and Special Cases** (CB, tokenization, TPV cross-links)
17. Reorganize **Zion** guides under `payu-subscriptions/zion-subscription-automation`
18. Add lifecycle diagrams (subscription states, UPI pre-debit timeline, charge flow)

### Phase 4 — Cleanup and AI Hardening (P2–P3)

19. Remove duplicate/hidden pages listed in Section 4
20. Apply page template to all remaining pages
21. Add `llms.txt` entries for subscription section
22. Audit all pages for **Next Step** links
23. Resolve Plan API documentation gap with product team
24. iOS/Android SDK cross-links
25. Quarterly review: FAQ → Troubleshooting feedback loop

---

## ReadMe CMS Implementation Notes

- **Section slug:** `payu-subscriptions` (new); keep `introduction-recurring-payments-integration` as deprecated alias with redirects for 90 days
- **Reference separation:** Do not move API reference pages; use `ref:` links from guides
- **Page template:** Every guide page uses the 9-block structure defined in the project brief
- **Scaffold location:** `/workspace/docs/Offerings/payu-subscriptions/` (implementation scaffold)
- **Hidden internal section:** Mark `internal-subscripions-or-recurring-payments` as deprecated after content migration

---

## Appendix: File Inventory Counts

| Area | Files | Post-restructure (est.) |
|------|-------|--------------------------|
| Current subscription-related guides | ~55 | ~45 (after dedup) |
| Current API reference | ~42 | ~42 (reordered) |
| Hidden/duplicate/stub | ~23 | 0 (removed or redirected) |
| New pages to author | — | ~12 |
