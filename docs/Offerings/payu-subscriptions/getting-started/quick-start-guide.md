---
title: Quick Start Guide
excerpt: >-
  Start integrating PayU Subscriptions in minutes. Learn key concepts, supported
  payment modes, and choose the right integration path for your business.
deprecated: false
hidden: false
metadata:
  title: PayU Subscriptions Quick Start
  description: >-
    Quick start guide for PayU Subscriptions and recurring payments. Understand
    mandates, supported payment modes, and choose API, Zion, or Dashboard
    integration.
  robots: index
next:
  description: Complete your first end-to-end subscription charge.
  pages:
    - slug: first-successful-subscription
      type: basic
      title: First Successful Subscription
---
## Purpose

This page orients first-time developers to PayU Subscriptions (Standing Instructions / recurring payments). You will understand what a subscription is, which payment modes are supported, and which integration path fits your team.

## When to use this

Use this page when you:

* Are evaluating PayU Subscriptions for your product
* Need to choose between API, Zion, or Dashboard integration
* Want a conceptual map before writing code

Skip to [First Successful Subscription](doc:first-successful-subscription) if you already have an integration path and want the happy-path steps.

## Prerequisites

* A [PayU merchant account](doc:register-for-a-merchant-account-on-dashboard)
* **Subscriptions feature enabled** on your merchant account (contact your PayU Key Account Manager or [PayU Support](https://help.payu.in) if not enabled)
* For API integration: [merchant key and salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

## Workflow

```
Understand concepts → Compare payment modes → Choose integration path → First successful charge → Go live
```

## What are PayU Subscriptions?

PayU Subscriptions (also called **Recurring Payments** or **Standing Instructions / SI**) let you charge customers automatically on a schedule after they provide one-time consent (a **mandate**).

* Charges run on a defined billing cycle
* Customers do not re-enter payment details for each charge
* You control registration, pre-debit notification (where required), and recurring debits — or delegate automation to Zion

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=5AfrrFg6CEQ" href="https://www.youtube.com/watch?v=5AfrrFg6CEQ" />

## Supported payment modes

| Payment Mode | Consent (Registration) | Pre-Debit Notification | Typical Use |
| ------------ | ---------------------- | ---------------------- | ----------- |
| **Credit Cards** | Required (2FA) | Required (≥24h before debit) | SaaS, OTT, memberships |
| **Debit Cards** | Required (2FA) | Required (≥24h before debit) | Insurance, EMIs |
| **Net Banking / eNACH** | Required | Not required | Utility bills, loan EMIs |
| **UPI Autopay** | Required (2FA in UPI app) | Required (≥24h before debit) | Low-ticket subscriptions |

<Image align="center" border={true} src="https://files.readme.io/21e3111ac286ec2702594a9c0764ff5cec67be250de5b2f89c844abcb73dccba-subscriptions_supported_payment_modes.png" />

<Callout icon="⚠️" theme="warn">
  **UPI Collect sunset:** NPCI is sunsetting UPI Collect mandate registration (manual VPA entry) effective **28 February 2026**. Use UPI Intent or in-app flows for new integrations. See [Supported Banks and Apps](doc:supported-banks-and-apps-upi).
</Callout>

## The three phases of every subscription

Regardless of payment mode, API-based subscriptions follow three phases:

1. **Consent / registration transaction** — Customer authorizes a mandate via `_payment` API
2. **Pre-debit notification** (Cards and UPI only) — Notify customer ≥24 hours before charging
3. **Recurring debit** — Charge the customer via Recurring Payment Transaction API (`si_transaction`)

Net Banking skips phase 2. For lifecycle details, see [Billing Lifecycle](doc:billing-lifecycle-overview).

## Choose your integration path

| Path | Best for | Effort | What PayU automates |
| ---- | -------- | ------ | ------------------- |
| **[Core Integration (API)](doc:core-integration-guide)** | Teams needing full control, custom UX | High | Consent, pre-debit, and debit APIs only — you orchestrate |
| **[Zion Subscription Automation](doc:zion-subscription-automation)** | Complex billing plans, minimal backend work | Medium | Plans, invoices, pre-debit, recurring debits, retries |
| **[Dashboard (No-Code)](doc:dashboard-integration)** | Non-technical teams, payment links, bulk CSV | Minimal | Link creation, bulk registration and recurring uploads |

### Decision tree

```
Do you have engineering resources for API integration?
├── No  → Dashboard Integration
└── Yes → Do you need multi-plan billing automation and invoice management?
          ├── Yes → Zion Subscription Automation
          └── No  → Core Integration Guide (API)
```

## Implementation

No code on this page. Select your path:

* **API** → [Core Integration Guide](doc:core-integration-guide)
* **Zion** → [Zion Subscription Automation](doc:zion-subscription-automation)
* **Dashboard** → [Dashboard Integration](doc:dashboard-integration)

Then complete [First Successful Subscription](doc:first-successful-subscription).

## Verification

You are ready to proceed when you can answer:

* [ ] Subscriptions is enabled on your PayU account
* [ ] You have chosen API, Zion, or Dashboard
* [ ] You know which payment mode(s) you will support
* [ ] You understand whether pre-debit applies to your mode

## Troubleshooting

| Issue | Resolution |
| ----- | ---------- |
| Subscriptions option not visible | Contact PayU to enable SI/Subscriptions on your MID |
| Unsure which path to pick | Use the decision tree above; Zion for plan-heavy billing, API for full control |
| Need cross-border subscriptions | See [International and Special Cases](doc:international-and-special-cases) |

## Related Pages

* [First Successful Subscription](doc:first-successful-subscription)
* [Billing Lifecycle](doc:billing-lifecycle-overview)
* [Subscription Use Cases](doc:subscription-use-cases)
* [Subscription APIs](doc:subscription-apis)

## Next Step

Complete your first end-to-end subscription charge: [First Successful Subscription](doc:first-successful-subscription).
