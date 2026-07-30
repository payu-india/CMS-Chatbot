---
title: API Troubleshooting
excerpt: >-
  Diagnose common PayU API integration issues — hash failures, wrong
  environments, callback problems, pending payments, and auth errors.
deprecated: false
hidden: false
metadata:
  title: PayU API Troubleshooting
  description: >-
    Troubleshoot PayU API issues including hash mismatch, incorrect base URL,
    callback failures, pending payments, OAuth errors, and duplicate txnid
    rejections.
  keywords:
    - PayU API troubleshooting
    - PayU hash mismatch fix
    - PayU payment pending
    - PayU callback not working
    - PayU API integration issues
  robots: index
next:
  description: ''
---
Use this page to diagnose the most common PayU API integration failures. For exhaustive payment error codes, see [Error Codes](ref:error-codes).

## Quick triage checklist

1. Are you calling the correct **API family** and **base URL**?
2. Are key, salt, and host all from the **same environment** (Test vs Production)?
3. Is the **hash/token** generated with the documented formula for this request?
4. Is `txnid` unique for a new payment?
5. Did you validate reverse hash and then **Verify Payment**?

## Issue — Hash mismatch

**Likely causes**

* Wrong salt for the key
* Incorrect pipe-separated field order
* Missing empty UDF placeholders
* Feature fields (SI/TPV/split/offers) omitted from hash input
* `api_version`-dependent fields not included

**Fix**

* Re-read [Generate Hash](doc:hashing-request-and-response)
* Use [Hash Verification Tool](doc:using-payu-hash-verification-tool)
* Compare against [API Authentication and Security](doc:api-authentication-and-security)

## Issue — Wrong environment or base URL

**Symptoms**

* Auth failures
* Unexpected HTML/login responses
* Works in docs Try It but fails in your code (or reverse)

**Fix**

* Confirm hosts in [API Environments and Base URLs](doc:api-environments-and-base-urls)
* Ensure General APIs use `postservice.php?form=2`
* Ensure `_payment` calls use `/_payment`, not the General API host

## Issue — Callback (`surl`/`furl`) not received

**Likely causes**

* URL not publicly reachable
* HTTPS/certificate issues
* Firewall blocking PayU posts
* App expecting JSON while receiving form POST

**Fix**

* Test with a public HTTPS endpoint
* Log raw body/headers temporarily in Test
* Follow [Handling Web Checkout](doc:handling-web-checkout)
* Rely on webhooks + Verify Payment as backup

## Issue — Payment stuck in pending

**Likely causes**

* Customer dropped off before completing bank/UPI journey
* Async authorization still in progress
* Callback missed and status never reconciled

**Fix**

* Call [Verify Payment](ref:verify_payment)
* Wait/retry according to product guidance for that payment mode
* Use webhooks for later terminal updates

## Issue — Duplicate `txnid`

**Fix**

* Generate a new `txnid` for each new attempt
* If the previous attempt result is unknown, verify that `txnid` before creating another payment

## Issue — OAuth token errors (Payouts/Partner)

**Likely causes**

* Wrong token URL (UAT vs Production)
* Expired token
* Incorrect client/merchant credentials
* Calling resource API without token

**Fix**

* Regenerate token via the product token API
* Confirm hosts in the environments page
* Start from [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api) or [Get Token API](ref:get_token_api)

## Issue — Try It works, integration fails

Compare these differences:

* Static docs Test key vs your merchant key
* Hash generation code vs playground-generated hash
* Missing headers/`Content-Type`
* Incorrect escaping of JSON fields inside form params (`si_details`, `beneficiarydetail`, `splitRequest`)

## Escalation information to collect

Before contacting [PayU Support](https://help.payu.in):

* Environment (Test/Production)
* Merchant key (not salt)
* `txnid` / `mihpayid` / request IDs
* Approximate timestamp (with timezone)
* API endpoint called
* Sanitized request/response (secrets removed)
* Whether callback/webhook was received

## What to read next

* [Error Handling for APIs](doc:error-handling-for-apis)
* [Testing PayU APIs](doc:testing-payu-apis)
* [API Best Practices](doc:api-best-practices)
* [API Introduction FAQs](doc:api-introduction-faqs)

## Related APIs

* [Verify Payment API](ref:verify_payment)
* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Error Codes](ref:error-codes)
