---
title: Subscription APIs
excerpt: >-
  Catalog of PayU Subscription APIs with one-line descriptions, grouped by
  developer task. Full specs are in API Reference.
deprecated: false
hidden: false
metadata:
  title: PayU Subscription APIs
  description: >-
    Index of PayU Subscription and recurring payment APIs including consent,
    pre-debit, recurring debit, and mandate management.
  robots: index
---
## Purpose

Task-oriented index of all Subscription APIs. Use this page to find the right endpoint; use linked **API Reference** pages for parameters, requests, and responses.

## When to use this

* You know **what you want to do** (e.g., cancel mandate) but not which API to call
* You are scoping integration work
* An AI assistant needs a map of available endpoints

Guides explain **why** and **how**; this page and Reference explain **what each API does**.

---

## Register a mandate (consent transaction)

| API | Description |
| --- | ----------- |
| [Payment Consent — PayU Hosted](ref:payment-consent-transaction-payu-hosted) | Register mandate via PayU Hosted Checkout |
| [Payment Consent — Merchant Hosted](ref:payment-consent-transaction-merchant-hosted) | Register mandate via your checkout (hub) |
| [Cards Consent Transaction](ref:credit-card-recurring-payment-consent-transaction) | Card SI registration (merchant hosted) |
| [Net Banking Consent Transaction](ref:netbanking-recurring-payment-consent-transaction) | NB/eNACH mandate registration |
| [UPI Consent Transaction](ref:upi-recurring-payment-consent-transaction) | UPI Autopay mandate registration |
| [Pay and Subscribe Consent](ref:pay-and-subscribe-consent-transaction) | One-time payment + optional mandate |
| [Consent with Saved Cards](ref:consenttransactionwithsavedcards) | Consent using stored card token |

---

## Notify before debit

| API | Description |
| --- | ----------- |
| [Pre-Debit Notification API](ref:pre_debit_notification_api) | Send pre-debit alert to customer (Cards/UPI) |
| [Pre-Debit SI API — Parallel Sequencing](ref:pre-debit-si-api-parallel-sequencing) | Pre-debit with UPI parallel sequencing |

---

## Charge the customer (recurring debit)

| API | Description |
| --- | ----------- |
| [Recurring Payment Transaction API](ref:recurring_payment_api) | Execute recurring debit against active mandate |
| [SI Transaction API — Parallel Sequencing](ref:si-transaction-api-parallel-sequencing) | Recurring debit with UPI parallel sequencing |

---

## Manage mandates

### Cards

| API | Description |
| --- | ----------- |
| [Check Mandate Status](ref:check-mandate-status-api) | Get card mandate status |
| [Modify Recurring Payment — Visa/Master](ref:modify-the-recurring-payments-for-a-card) | Change card mandate parameters |
| [Cancel Recurring Payment — Visa/Master](ref:cancel-the-recurring-payment-for-cards) | Revoke card mandate |
| [Modify — AMEX](ref:modify-recurring-payments-for-amex-card) | Modify AMEX mandate |
| [Cancel — AMEX](ref:cancel-recurring-payment-for-a-amex-card) | Cancel AMEX mandate |
| [Update SI API](ref:update-si-api) | Update mandate with network token |

### Net Banking

| API | Description |
| --- | ----------- |
| [Check NB Mandate Status](ref:net_banking_mandate_status_api) | Get net banking mandate status |
| [Cancel NB Recurring Payment](ref:cancel-the-recurring-payment-for-net-banking) | Revoke NB/eNACH mandate |

### UPI

| API | Description |
| --- | ----------- |
| [Get UPI Mandate Status](ref:get-mandate-status-api-for-upi-only) | Get UPI Autopay mandate status |
| [Modify UPI Recurring Payment](ref:modify-the-recurring-payment-for-upi) | Modify UPI mandate |
| [Cancel UPI Recurring Payment](ref:cancel-the-recurring-payment-for-upi) | Revoke UPI mandate |
| [Validate VPA API](ref:validate_vpa_api) | Validate UPI ID before registration |

---

## Reference data

| API / Doc | Description |
| --------- | ----------- |
| [SI Parameter JSON Details](ref:si-parameter-json-details) | `si_details` field reference |
| [Issuer Bank Webhook Setup](ref:set-up-webhook-to-receive-cancellation-or-modification-update-from-the-issuer-bank) | Receive bank-initiated mandate updates |

---

## Zion APIs

| API | Description |
| --- | ----------- |
| [Define Subscription](ref:create-a-subscription) | Create Zion subscription with billing plan |
| [Update Subscription](ref:update-subscription-api) | Update subscription configuration |
| [Get Subscription Details](ref:get-subscription-details-api) | Fetch single subscription |
| [List Subscriptions](ref:get-list-of-subscriptions-api) | List merchant subscriptions |
| [Cancel Subscription](ref:cancel-subscription-api) | Cancel Zion subscription |
| [Create Invoice](ref:create-invoice-api-zion) | Trigger invoice charge |
| [Get Invoice](ref:get-invoice-interfaces-api-zion) | Retrieve invoice details |

---

## Related Pages

* [Core Integration Guide](doc:core-integration-guide)
* [First Successful Subscription](doc:first-successful-subscription)
* [Webhooks and Events](doc:webhooks-and-events)

## Next Step

[Core Integration Guide](doc:core-integration-guide) for end-to-end implementation.
