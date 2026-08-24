---
title: Core Integration Guide
excerpt: >-
  Comprehensive guide to integrating PayU Subscriptions via API — from choosing
  checkout type through testing and production go-live.
deprecated: false
hidden: false
metadata:
  title: PayU Subscriptions API Integration Guide
  description: >-
    Build, test, and go live with PayU Subscriptions API integration for cards,
    net banking, and UPI Autopay.
  robots: index
---
## Purpose

Central guide for **API-first** PayU Subscriptions integration. Covers build, test, and go-live — with API reference kept separate.

## When to use this

Choose this guide when you:

* Need full control over checkout UX and billing orchestration
* Are **not** using Zion automation or Dashboard-only flows
* Will call PayU APIs directly from your backend

For Zion, see [Zion Subscription Automation](doc:zion-subscription-automation). For no-code, see [Dashboard Integration](doc:dashboard-integration).

## Prerequisites

* [Quick Start Guide](doc:quick-start-guide)
* Subscriptions enabled on MID
* [API key and salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
* Webhook endpoint (production)

## Workflow

```
Choose path → Build (consent + pre-debit + debit) → Test in sandbox → Go live
```

## Core APIs

| Phase | API | Reference |
| ----- | --- | --------- |
| Registration | `_payment` (consent) | [Merchant Hosted](ref:payment-consent-transaction-merchant-hosted) / [PayU Hosted](ref:payment-consent-transaction-payu-hosted) |
| Pre-debit | `pre_debit_SI` | [Pre-Debit Notification API](ref:pre_debit_notification_api) |
| Recurring charge | `si_transaction` | [Recurring Payment Transaction API](ref:recurring_payment_api) |
| Mandate management | Varies by mode | [Cards](ref:manage-recurring-payment-for-cards), [NB](ref:manage-recurring-payments-for-net-banking), [UPI](ref:api-commands-to-manage-upi-recurring-transaction) |

`si_details` JSON schema: [SI Parameter JSON Details](ref:si-parameter-json-details).

<Callout icon="👍" theme="okay">
  **Integration Lab:** Experience PayU Hosted Subscriptions and generate sample code at [PayU Integration Lab](https://payu.in/integrationlab/subscription).
</Callout>

## Build Integration

| Topic | Page |
| ----- | ---- |
| Choose checkout type | [Choose Your Integration Path](doc:choose-your-integration-path) |
| PayU Hosted | [Build Integration — PayU Hosted](doc:build-integration-payu-hosted) |
| Cards (Merchant Hosted) | [Build Integration — Cards](doc:build-integration-cards-merchant-hosted) |
| Net Banking | [Build Integration — Net Banking](doc:build-integration-net-banking) |
| UPI Autopay | [Build Integration — UPI Autopay](doc:build-integration-upi-autopay) |
| UPI parallel sequencing | [Parallel Sequencing](doc:parallel-sequencing-upi) |
| Pay and Subscribe | [Pay and Subscribe](doc:pay-and-subscribe) |

**Content source:** Migrate from `internal-subscripions-or-recurring-payments/subscriptions-integration/*` and `using-api-integration-recurring-payments/*`.

## Test Integration

See [Test Integration](doc:test-integration) for sandbox checklist, test credentials, and verification steps.

## Go Live

See [Go-Live Checklist](doc:go-live-checklist) before switching to production keys.

## Verification

* [First Successful Subscription](doc:first-successful-subscription) completed in sandbox
* Webhooks received for success and failure paths
* Mandate management tested (cancel/modify as applicable)

## Troubleshooting

* [Troubleshooting Guide](doc:troubleshooting-guide)
* [Retry Logic](doc:retry-logic-overview)

## Related Pages

* [Subscription APIs](doc:subscription-apis) — API catalog
* [Billing Lifecycle](doc:billing-lifecycle-overview)
* [Webhooks and Events](doc:webhooks-and-events)

## Next Step

[Choose Your Integration Path](doc:choose-your-integration-path)
