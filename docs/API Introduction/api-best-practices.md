---
title: API Best Practices
excerpt: >-
  Recommended practices for secure, reliable PayU API integrations — hashing,
  verification, webhooks, retries, logging, and go-live hygiene.
deprecated: false
hidden: false
metadata:
  title: PayU API Best Practices
  description: >-
    Follow PayU API best practices for authentication, unique txnids, reverse
    hash validation, webhook idempotency, retries, logging, and Production
    cutover.
  keywords:
    - PayU API best practices
    - PayU integration best practices
    - PayU payment security best practices
    - PayU webhook best practices
  robots: index
next:
  description: ''
---
These best practices apply across PayU API families. Product guides may add stricter requirements for subscriptions, payouts, or partner onboarding.

## Authentication and secrets

* Generate hashes and OAuth tokens **only on your server**.
* Never ship salt, client secret, or Production keys in frontend or mobile binaries.
* Rotate credentials immediately if leaked.
* Keep Test and Production secrets in separate configuration spaces.

See [API Authentication and Security](doc:api-authentication-and-security).

## Payment creation

* Use a new unique `txnid` for every new payment attempt.
* Persist `txnid` before calling PayU so callbacks can be correlated.
* Send mandatory fields exactly as documented; avoid unused dummy values that break hash input.
* Prefer HTTPS absolute URLs for `surl` and `furl`.

## Status confirmation

* Treat redirect callbacks as **untrusted user browser events**.
* Validate reverse hash on callbacks.
* Confirm final success with [Verify Payment](ref:verify_payment) or equivalent server APIs.
* Design for pending states — especially UPI and some bank flows.

## Webhooks

* Configure webhooks in the Dashboard for asynchronous reliability.
* Verify signatures/reverse hashes.
* Process events idempotently.
* Return 2xx quickly; continue heavy fulfillment asynchronously.

See [Webhooks and Callbacks](doc:webhooks-and-callbacks).

## Retries and timeouts

* Use reasonable timeouts on server-to-server calls.
* Retry transient network failures with backoff.
* Do not blindly retry payment creation with the same `txnid` after an unknown result — verify first.
* If you see throttling/rate-limit style errors, wait and retry with backoff.

## Logging and observability

* Log request IDs, `txnid`, `mihpayid`, and response status codes.
* Never log full card data, CVV, salt, or raw secrets.
* Alert on spikes in hash mismatches, open pending payments, and webhook delivery failures.

## Environment hygiene

* Develop against Test hosts and Test credentials.
* Switch host + key + salt together at go-live.
* Re-test callbacks and webhooks on Production URLs.

See [API Environments and Base URLs](doc:api-environments-and-base-urls) and [Testing PayU APIs](doc:testing-payu-apis).

## Design for reconciliation

* Run periodic reconciliation jobs using transaction/settlement APIs.
* Build admin tools to re-verify ambiguous orders.
* Store raw PayU payloads for dispute and support windows.

## Product-specific caution

| If you integrate… | Extra care |
| :---------------- | :--------- |
| S2S card flows | PCI scope, OTP/native flows, and data handling |
| Subscriptions | Consent state machine and recurring failure handling |
| Split settlements | Child merchant mapping and refund split behavior |
| Payouts | OAuth token lifecycle and beneficiary validation |
| Cross-border | Additional compliance documents and on-hold settlement states |

## What to read next

* [API Troubleshooting](doc:api-troubleshooting)
* [Common API Workflows](doc:common-api-workflows)
* [Error Handling for APIs](doc:error-handling-for-apis)
* [API Introduction FAQs](doc:api-introduction-faqs)

## Related APIs

* [Verify Payment API](ref:verify_payment)
* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Check Transaction APIs](ref:check-transaction-apis)
