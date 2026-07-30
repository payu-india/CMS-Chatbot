---
title: Error Handling for APIs
excerpt: >-
  Learn how to interpret PayU API errors, hash mismatches, duplicate txnids, and
  where to find complete payment error codes.
deprecated: false
hidden: false
metadata:
  title: PayU API Error Handling
  description: >-
    Handle PayU API errors effectively — hash mismatch, duplicate txnid, missing
    parameters, invalid amount, and links to complete PayU error codes.
  keywords:
    - PayU API errors
    - PayU error handling
    - PayU hash mismatch
    - PayU error codes
    - PayU duplicate txnid
  robots: index
next:
  description: ''
---
PayU API errors usually fall into a few categories: authentication/hash issues, validation problems, payment declines, and product-specific failures. Handle them deliberately so customers are not left in an unknown payment state.

## Where to find error codes

| Resource | Use it for |
| :------- | :--------- |
| [Error Codes](ref:error-codes) | Complete payment error code reference |
| [Error Handling (Hosted Checkout)](doc:error-handling) | Common checkout integration failures with screenshots |
| Product-specific error pages | Refunds, pre-auth, split settlements, partner KYC, and more |

This page is the API Introduction overview. Use the references above for exhaustive code lists.

## How PayU surfaces errors

| Layer | What you receive |
| :---- | :--------------- |
| **General API response** | `status=0` with `msg` explaining the failure |
| **Checkout / `_payment`** | Error page, redirect to `furl`, or API error payload depending on integration |
| **Bank/UPI/wallet decline** | Payment failure with PayU/bank error codes after the request was accepted |
| **OAuth / product APIs** | HTTP status + product error body (follow that API Reference) |

## Common integration errors

### Hash mismatch

**Symptom:** Transaction fails because the `hash` parameter is incorrect.

**Fix:**

1. Regenerate hash with the exact field order for your API family.
2. Ensure salt matches the key/environment.
3. Recalculate whenever request parameters change.

See [Generate Hash](doc:hashing-request-and-response) and [API Authentication and Security](doc:api-authentication-and-security).

### Duplicate transaction ID (`txnid`)

**Symptom:** Request rejected because `txnid` was used earlier or already captured.

**Fix:** Generate a new unique `txnid` for every new payment attempt.

### Invalid amount

**Symptom:** Amount missing, malformed, or rejected.

**Fix:** Send amount in the format required by the API Reference. Include all mandatory amount-related fields.

### Mandatory parameters missing

**Symptom:** PayU rejects the request before payment processing.

**Fix:** Compare your payload with the required fields on the target API Reference page.

### Incorrect payment details

**Symptom:** Card/UPI/wallet details invalid in Merchant Hosted or S2S flows.

**Fix:** Validate client-side inputs and use Test instruments only in Test.

## Recommended error-handling pattern

```
1. Validate request locally (mandatory fields, amount, unique txnid)
2. Generate auth (hash/token)
3. Call PayU
4. Branch on transport success vs business failure
5. Persist raw response + mapped order state
6. For uncertain states, call Verify Payment
7. Show customer-safe messages; log raw codes internally
```

## Customer-safe messaging

* Do **not** expose salt, hash strings, or internal stack traces to customers.
* Map bank/PayU decline codes to clear retry guidance.
* For pending states, tell customers the payment is being confirmed and reconcile asynchronously.

## Refunds, chargebacks, and product errors

| Domain | Start here |
| :----- | :--------- |
| Refunds | [Refunds introduction](doc:introduction-refunds), refund error docs under Refunds |
| Chargebacks | [Chargeback](doc:chargeback) |
| Pre-authorize | [Pre-authorize payment error codes](ref:error-codes-pre-authorize-payment) |
| Split settlements | Split settlement refund/error docs under [Split Settlements](doc:split-settlments) |

## What to read next

* [API Troubleshooting](doc:api-troubleshooting)
* [Testing PayU APIs](doc:testing-payu-apis)
* [Common API Workflows](doc:common-api-workflows)
* [Error Codes](ref:error-codes)

## Related APIs

* [Verify Payment API](ref:verify_payment)
* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Error Codes](ref:error-codes)
