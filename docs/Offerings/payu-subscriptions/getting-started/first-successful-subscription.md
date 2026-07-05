---
title: First Successful Subscription
excerpt: >-
  Step-by-step happy path to register a mandate, send pre-debit (if required),
  and execute your first recurring charge with verification at each step.
deprecated: false
hidden: false
metadata:
  title: First Successful PayU Subscription
  description: >-
    Complete guide to your first successful PayU subscription charge including
    consent transaction, pre-debit notification, and recurring debit.
  robots: index
next:
  description: Understand the full subscription and charge lifecycle.
  pages:
    - slug: billing-lifecycle-overview
      type: basic
      title: Billing Lifecycle Overview
---
## Purpose

Walk through the **happy path** for your first successful subscription charge. This page is the fastest route from zero to a verified recurring debit.

## When to use this

Use this page when you:

* Have chosen [API integration](doc:core-integration-guide) or are validating Zion/Dashboard setup
* Need a checklist with expected outcomes at each step
* Want to test in sandbox before go-live

For conceptual background, start with [Quick Start Guide](doc:quick-start-guide).

## Prerequisites

* [PayU merchant account](doc:register-for-a-merchant-account-on-dashboard) with **Subscriptions enabled**
* [API key and salt](doc:generate-merchant-key-and-salt-on-payu-dashboard) (API path)
* [Webhook endpoint](doc:webhooks) configured (recommended for production)
* Payment mode selected: Cards, Net Banking, or UPI Autopay

## Workflow

```
Consent transaction → (Pre-debit if Cards/UPI) → Recurring debit → Verify status
```

## Implementation

### Step 1 — Create a consent (registration) transaction

Register the customer mandate using the `_payment` API.

| Payment Mode | Guide | API Reference |
| ------------ | ----- | ------------- |
| Cards (Merchant Hosted) | [Cards Integration](doc:build-integration-cards-merchant-hosted) | [Cards Consent Transaction](ref:credit-card-recurring-payment-consent-transaction) |
| Cards (PayU Hosted) | [PayU Hosted Integration](doc:build-integration-payu-hosted) | [Payment Consent Transaction - PayU Hosted](ref:payment-consent-transaction-payu-hosted) |
| Net Banking | [Net Banking Integration](doc:build-integration-net-banking) | [Net Banking Consent Transaction](ref:netbanking-recurring-payment-consent-transaction) |
| UPI Autopay | [UPI Integration](doc:build-integration-upi-autopay) | [UPI Consent Transaction](ref:upi-recurring-payment-consent-transaction) |

**Key parameters:** Include `si_details` JSON with billing amount, cycle, start date, and end date. See [SI Parameter JSON Details](ref:si-parameter-json-details).

**Expected outcome:**

* Transaction status = success
* You receive `mihpayid` / `authpayuid` (save this — required for recurring debits)
* For UPI/Cards: customer completes 2FA in bank or UPI app

**Common mistakes:**

* Invalid `si_details` date range → error `E4530` / `E4531`
* Card does not support recurring → "Card not supported" (use [Get BIN Info API](ref:get_bin_info_api))

---

### Step 2 — Send pre-debit notification (Cards and UPI only)

Skip this step for **Net Banking**.

Call the [Pre-Debit Notification API](ref:pre_debit_notification_api) **at least 24 hours** before the recurring charge.

**Expected outcome:**

* Response `status` = `1` (notification triggered successfully)
* Customer receives pre-debit alert in bank/UPI app

**Common mistakes:**

* Sending pre-debit less than 24 hours before debit → debit may fail
* `status` = `0` → retry after a short interval (see [Retry Logic](doc:retry-logic-overview))

---

### Step 3 — Execute the recurring debit

Call the [Recurring Payment Transaction API](ref:recurring_payment_api) (`si_transaction`) with:

* `authpayuid` from Step 1
* Debit amount matching mandate rules
* Correct billing sequence

**Expected outcome:**

* Transaction success
* Funds debited per mandate
* Webhook or [Verify Payment API](ref:verify-payment-api) confirms final status

**Common mistakes:**

* Debit amount mismatch → `E4112`
* Parallel debits for same cycle → `E4682` / `E4105`
* Debit while first attempt in progress → wait for final status (see [Troubleshooting](doc:troubleshooting-guide))

---

### Step 4 — Verify success

| Check | How |
| ----- | --- |
| Transaction status | [Verify Payment API](ref:verify-payment-api) or transaction webhook |
| Mandate state | [Check Mandate Status](ref:check-mandate-status-api) (cards), [UPI Mandate Status](ref:get-mandate-status-api-for-upi-only), or [NB Mandate Status](ref:net_banking_mandate_status_api) |
| Customer notification | Pre-debit and debit alerts (Cards/UPI) |

## Verification checklist

* [ ] Consent transaction succeeded; `authpayuid` stored securely
* [ ] Pre-debit sent ≥24h before debit (Cards/UPI)
* [ ] Recurring debit succeeded
* [ ] Mandate status = Active
* [ ] Webhook received and processed (if configured)

## Troubleshooting

| Failure | Likely cause | Recovery |
| ------- | ------------ | -------- |
| Consent failed (`E4278`) | Bank rejected mandate | Ask customer to try another account or payment mode |
| Pre-debit `status=0` | Transient failure | Retry pre-debit; see [Pre-Debit Failures](doc:pre-debit-failures) |
| Debit `E4682` | Debit already in progress | Poll status; do not send duplicate request |
| Debit `E4112` | Amount outside mandate | Align amount with `si_details` billing rule |

Full error reference: [Troubleshooting Guide](doc:troubleshooting-guide).

## Related Pages

* [Quick Start Guide](doc:quick-start-guide)
* [Billing Lifecycle](doc:billing-lifecycle-overview)
* [Test Integration](doc:test-integration)
* [Go-Live Checklist](doc:go-live-checklist)
* [Core Integration Guide](doc:core-integration-guide)

## Next Step

Understand ongoing operations: [Billing Lifecycle Overview](doc:billing-lifecycle-overview).
