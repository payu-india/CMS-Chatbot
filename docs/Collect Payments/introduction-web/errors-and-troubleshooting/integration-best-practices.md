---
title: Integration Best Practices
excerpt: Prevent common PayU integration errors with secure hash handling, idempotency, retries, and clean status management.
deprecated: false
hidden: false
metadata:
  title: Integration Best Practices
  description: Best practices to prevent PayU payment integration errors across Hosted Checkout, Merchant Hosted Checkout, S2S, webhooks, and recurring payments.
  robots: index
next:
  description: ''
---

Use these practices to prevent common PayU payment errors before they reach production.

## Generate and validate hash correctly

* Generate request hashes only on your backend.
* Use the exact values that will be posted to PayU.
* Preserve pipe delimiters for blank fields.
* Keep test and production keys/salts separate.
* Never send salt to frontend, mobile apps, URLs, logs, or analytics tools.
* Validate PayU response hash before updating order status.

> **Common Mistake**
>
> Hashing `10.00` and posting `10` causes hash validation failure because hashes are generated from strings, not numeric values.

## Separate frontend and backend responsibilities

| Responsibility | Frontend | Backend |
| --- | --- | --- |
| Collect customer input | Yes | Optional |
| Validate basic form fields | Yes | Yes |
| Generate `txnid` | No | Yes |
| Generate request hash | No | Yes |
| Store order attempt | No | Yes |
| Submit to PayU | Yes, for Hosted Checkout form post | Yes, for S2S and server-mediated flows |
| Verify response hash | No | Yes |
| Decide final order status | No | Yes |
| Process webhook | No | Yes |

## Handle retries and idempotency

* Use a unique `txnid` for every new payment attempt.
* Keep a stable merchant order ID in your system and map multiple PayU attempts to it.
* Do not retry a pending transaction blindly.
* Before creating a new attempt, check whether the previous attempt succeeded, failed, or is still pending.
* Make webhook processing idempotent with a unique key such as `mihpayid` + `txnid` + final status.
* Protect the checkout button from double-click submissions.
* Do not create duplicate fulfillment on duplicate redirects or duplicate webhooks.

## Build clear status handling

Recommended merchant-side states:

| Merchant state | PayU signal | Recommended fix |
| --- | --- | --- |
| `payment_initiated` | Request created | Await redirect, webhook, or status API update before fulfillment. |
| `payment_pending` | `status=pending` or `E227` | Do not fulfill. Poll/reconcile and wait for webhook/status confirmation. |
| `payment_success` | `status=success` and hash valid | Fulfill order after matching `txnid`, `amount`, and response hash. |
| `payment_failed` | `status=failure` and final status verified | Show retry options and create a new `txnid` for a new attempt. |
| `payment_dropped` | `E231`, timeout, abandoned flow | Verify final status before retrying or closing the order. |
| `payment_review` | Conflicting redirect/webhook/status | Hold fulfillment and reconcile using Transaction Detail APIs. |

## Webhook handler checklist

* Accept `POST`.
* Accept form data and `application/x-www-form-urlencoded`.
* Allow PayU webhook IPs.
* Verify response hash.
* Persist payload before processing.
* Return `2xx` after durable receipt.
* Process fulfillment asynchronously.
* Make all state updates idempotent.

## Recurring and SI checklist

* Validate mandate start and end dates before sending request.
* Prevent duplicate debit requests for the same mandate cycle.
* Store `authpayuid` or `authPayuId` against the customer mandate.
* Reconcile all recurring debits through webhook/status APIs.
* Treat mandate setup pending states separately from payment pending states.
