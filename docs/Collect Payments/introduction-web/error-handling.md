---
title: Errors and Troubleshooting
excerpt: Practical error handling and debugging guide for PayU payment integrations.
deprecated: false
hidden: false
metadata:
  title: Errors and Troubleshooting
  description: Practical error handling and debugging guide for PayU Hosted Checkout, Merchant Hosted Checkout, S2S, webhooks, and recurring payment integrations.
  robots: index
next:
  description: ''
---

Use this guide to identify, debug, and fix PayU integration errors across Hosted Checkout, Merchant Hosted Checkout, Server-to-Server (S2S), webhooks, and recurring payment flows.

For the full error-code reference, see [Error Codes](ref:error-codes). For transaction-stage diagnostics, see [Transaction Stages - Error References on Field7 & Field8](ref:transaction-stages-error-references-field7-field8).

## Overview

Errors in PayU are signals returned during payment initiation, authentication, authorization, bank processing, webhook delivery, refund, or recurring-payment processing.

PayU errors usually fall into these high-level causes:

* **Merchant configuration issues**: invalid merchant key, disabled payment mode, missing S2S access, wrong environment, webhook URL not configured.
* **Request validation issues**: missing mandatory parameters, invalid amount, duplicate `txnid`, invalid `bankcode`, invalid VPA, invalid card details.
* **Hash or security issues**: incorrect hash sequence, wrong salt, response hash mismatch, sending salt in the request, altered response parameters.
* **Customer or issuer declines**: insufficient funds, incorrect OTP/CVV, card blocked, VPA inactive, transaction not permitted by bank.
* **Network or timeout issues**: bank unavailable, PSP timeout, no callback from bank, PayU-to-merchant webhook delivery failure.
* **Recurring or SI issues**: mandate declined, invalid billing dates, amount mismatch, sequence mismatch, mandate timeout.

> **Pro Tip**
>
> Do not rely only on browser redirects to decide order status. Always verify the final status using the payment response hash, webhooks, and Transaction Detail APIs.

## Error categories

### Authentication and authorization errors

These happen when PayU, the issuer, bank, PSP, or payment network cannot authenticate the customer or authorize the payment.

Common examples:

* Card 3D Secure or OTP failure.
* Issuer declines authorization.
* Merchant is not enabled for the requested flow or payment mode.
* S2S access is not enabled for the merchant.

### Hash and security errors

These happen when PayU cannot validate the request or response integrity.

Common examples:

* Incorrect SHA-512 hash sequence.
* Missing delimiters for empty UDF fields.
* Wrong key or salt.
* Hash generated on frontend.
* Response hash not verified before updating order status.

### Validation errors

These happen before PayU can process the payment.

Common examples:

* Missing `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, or `hash`.
* Invalid amount format.
* Duplicate `txnid`.
* Invalid payment method, `pg`, `bankcode`, card data, VPA, or SI parameters.

### Payment failures

These happen after payment initiation when the customer, issuer, bank, PSP, or payment method declines or cannot complete the transaction.

Common examples:

* Incorrect OTP, CVV, or card details.
* Insufficient funds or limit exceeded.
* Issuer declined.
* Customer cancelled or abandoned payment.
* Bank or PSP timeout.

### Network and API errors

These happen when an API request cannot be processed because of timeout, service unavailability, route issues, or invalid API credentials.

Common examples:

* HTTP 4xx from merchant endpoint.
* HTTP 5xx from merchant endpoint.
* PayU could not reach a configured route.
* Bank/PSP did not respond in time.

### Webhook errors

These happen when PayU cannot deliver the server-to-server notification to your webhook endpoint or when your system cannot process it safely.

Common examples:

* Webhook endpoint returns `405`, `401`, `403`, `404`, or `5xx`.
* Endpoint accepts JSON only, but PayU sends form data.
* PayU IPs are blocked by firewall or WAF.
* Webhook handler is not idempotent.
* Webhook response hash is not verified.

### Recurring and SI errors

These happen during Standing Instruction (SI), UPI Autopay, mandate registration, mandate modification, or recurring debit.

Common examples:

* Mandate declined by customer or PSP.
* Start date is less than current date.
* End date is less than start date.
* Debit amount differs from mandate amount.
* Sequence number mismatch.
* Recurring payment already in progress.

## Core error table

| Error code / type | Error message as returned by PayU | Description | Possible cause | Recommended fix |
| --- | --- | --- | --- | --- |
| `E000` | `No Error` | Transaction completed successfully. | Payment was authorized and captured successfully. | Mark the order as paid only after validating response hash and matching `txnid`, `amount`, and `status`. |
| `E700` | `Validation of secure hash failed` | PayU could not validate the request hash. | Wrong hash sequence, wrong salt, missing delimiters, value mismatch, environment key/salt mismatch. | Recreate the hash server-side using the exact posted values and correct salt. See [Generate Hash](doc:generate-hash-payu-hosted). |
| `SECURE_HASH_FAILURE` | `Validation of secure hash failed` | Security validation failed. | Request was tampered with or hash was generated from normalized values that differ from submitted values. | Log the raw hash string server-side and compare it with the posted request. Never send salt to frontend. |
| `E1101` | `Transaction failed due to invalid params shared by the merchant` | PayU rejected the transaction request because one or more parameters are invalid. | Invalid `amount`, `txnid`, `productinfo`, `surl`, `furl`, `pg`, `bankcode`, or unsupported combination of fields. | Validate request payload before submitting to PayU. Confirm mandatory fields for your integration type. |
| `E4156` / `E4373` | `VALIDATION ERROR` | Generic validation failure. | Missing or malformed parameter, invalid field length, invalid enum, unsupported value. | Compare request with API reference and check raw request logs. |
| Missing parameter | `One or more mandatory parameters are missing` | Required fields were not sent. | Frontend did not pass data to backend, backend omitted empty fields, or request content type is incorrect. | Send all mandatory fields and include empty UDF delimiters in the hash string. |
| Invalid amount | `Invalid amount` / `Please enter valid amount` | Amount is missing or not accepted. | Amount is blank, zero, negative, contains commas, has unsupported decimal precision, or differs between hash and request. | Send amount as a decimal string, for example `10.00`, and use the exact same value in hash generation. |
| Duplicate `txnid` | `Duplicate Transaction ID` / `THE REQUEST IS DUPLICATE` | The transaction ID was already used. | Retrying a new payment attempt with the same `txnid`, or reusing order ID as transaction ID without uniqueness. | Generate a unique `txnid` for every new payment attempt. Use Transaction Detail APIs for status checks instead of re-posting the same transaction. |
| `E4150` | `Transaction declined due to duplicate request` | PayU or bank detected a duplicate request. | Same transaction submitted multiple times in a short window. | Disable double-submit on frontend and enforce idempotency on backend. |
| `E1201` | `You are not authorized to do this transaction.` | Merchant is not authorized for requested service. | Payment mode, route, S2S flow, currency, or feature not enabled for merchant. | Confirm merchant configuration in Dashboard or with PayU Integration Team. |
| `E1631` | `Merchant Validation Failed` | Merchant-level validation failed. | Invalid merchant key, inactive merchant, invalid bank MID/terminal, or disabled configuration. | Verify key/salt, environment, MID status, and payment mode enablement. |
| `E1621` | `Merchant does not have access to S2S flow` | S2S flow is not enabled for the merchant. | Attempting S2S APIs without enablement. | Request S2S enablement and confirm production/test credentials. |
| `E1622` | `S2S flow not enabled on selected payment gateway` | Selected payment gateway does not support enabled S2S route. | Wrong `pg`/`bankcode` or payment mode not configured for S2S. | Use an enabled payment method or update gateway configuration. |
| `E1615` | `txn_s2s_flow missing parameter` | Required S2S parameter is missing. | S2S request missing flow-specific parameter. | Add the required S2S parameters from the S2S integration guide. |
| `E907` / `E1620` | `Wrong payment method selected` | Payment method does not match enforced method. | User selected a different mode than configured, or request has wrong `pg`/`bankcode`. | Pass the correct payment method parameters and validate frontend payment selection. |
| `E908` | `International cards not allowed` | Card is not allowed for this merchant/payment route. | International card attempted while international card processing is disabled. | Enable international cards if required or show a clear customer message. |
| `E306` | `Card authentication failure` | Card authentication could not be completed. | Invalid OTP, expired OTP, 3DS issue, user abandoned authentication. | Ask customer to retry; if repeated, use another card or payment method. |
| `E300` | `Card failed 3D authentication as 3 D Secure signatures did not match` | 3DS authentication failed. | Incorrect OTP/password or issuer authentication issue. | Let customer retry authentication or use another card. |
| `E1000` | `3-D secure authentication failed.` | 3DS authentication failed. | User failed challenge, challenge timed out, issuer unavailable. | Retry with the same payment method only after confirming final transaction status. |
| `E317` | `Payer could not be authenticated` | Customer authentication failed. | Issuer/ACS could not authenticate payer. | Show retry option and alternate payment methods. |
| `E1670` | `Card authentication failed at the bank due to invalid CVV` | Card security code validation failed. | Wrong CVV/CVC entered by customer. | Ask customer to re-enter card details or use another card. |
| `E348` | `Transaction declined by the issuer` | Issuer declined the payment. | Issuer risk rules, card limits, insufficient funds, card disabled for online payments. | Show issuer-decline message and suggest another payment method. |
| `E307` | `Transaction declined with do not honor` | Issuer declined without a specific reason. | Issuer risk, card restrictions, transaction pattern, bank policy. | Ask customer to contact issuer or use a different payment method. |
| `E500` | `Bank failed to authenticate the customer` | Bank could not authenticate the customer. | Bank authentication page failed, user abandoned OTP, issuer timeout. | Ask customer to retry after verifying final status. |
| `E308` | `Transaction Failed at bank end.` | Bank reported a failed transaction. | Bank declined or could not process the payment. | Treat as failed unless later webhook/status check confirms success. |
| `E227` | `Transaction is Pending` | Final status is not yet available. | Bank/PSP processing is delayed, corporate banking approval pending, or callback not received. | Do not mark failed immediately. Poll Transaction Detail APIs and listen for webhooks. |
| `E507` | `Transaction Expired` | Customer did not complete the payment in time. | Checkout session, bank page, OTP, or UPI collect expired. | Create a new payment attempt with a new `txnid`. |
| `E231` | `Transaction was marked as dropped` | Payment flow was abandoned or dropped. | User closed browser, redirect failed, or no bank response. | Verify final status before retrying. If not successful, create a new attempt. |
| `E408` | `Transaction failed. Page expired due to no user input.` | Checkout or bank page timed out. | Customer took too long or abandoned payment. | Ask customer to retry with a new transaction. |
| `E1206` | `Transaction interrupted by pressing back button` | Customer interrupted the redirect flow. | Customer used browser back button or closed page. | Treat as failed/dropped only after status verification. |
| `E4292` | `PSP TIME-OUT` | PSP did not respond in time. | PSP/UPI app/bank timeout. | Keep order pending and reconcile through status API/webhook before retry. |
| `E4177` | `REMITTER BANK NOT AVAILABLE` | Customer bank was unavailable. | Bank downtime or connectivity issue. | Suggest alternate bank/payment method. |
| `E1654` | `Route to merchant unavailable` | PayU could not route the transaction. | Gateway route unavailable or misconfigured. | Retry later or contact PayU if persistent for the same route. |
| `E4526` | `Record not found against given parameters` | Status/refund/verification lookup did not find a matching transaction. | Wrong `txnid`, wrong `mihpayid`, wrong key, environment mismatch. | Confirm identifiers and environment before retrying lookup. |
| `E1500` | `Retry not allowed` | Retry is not permitted for this transaction. | Payment network or PayU state does not allow retry on same request. | Create a new payment attempt with a new `txnid` after confirming final status. |
| Webhook delivery `4xx` | `HTTP/2 405`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found` | Merchant endpoint rejected PayU webhook. | Wrong URL, unsupported method, authentication rule, WAF/firewall, route not deployed. | Accept PayU POST requests, allow PayU IPs, and support form-encoded payloads. |
| Webhook delivery `5xx` | `500 Internal Server Error`, `502`, `503`, `504` | Merchant endpoint failed while processing webhook. | Handler exception, timeout, dependency outage, database failure. | Make webhook processing idempotent, fast, and queue-backed. Return `2xx` after durable receipt. |
| `E4530` | `Mandate request failed as start date is less than current date` | SI/mandate start date is invalid. | `startDate` is in the past or timezone conversion changed date. | Send a valid future/current mandate start date as per API requirements. |
| `E4531` | `Mandate request failed as end date is less than start date` | SI/mandate end date is invalid. | End date is before start date. | Validate mandate date range before creating mandate. |
| `E4112` | `Transaction failed as mandate and transaction amount is different` | Debit amount does not match mandate rules. | Debit exceeds fixed mandate amount or does not follow billing rule. | Align debit amount with mandate amount and billing rule. |
| `E4105` | `Transaction failed due to recurring sequence mismatch` | Recurring sequence is invalid. | Wrong sequence number or parallel debit issue. | Use the correct recurring sequence and avoid concurrent debits for the same mandate. |
| `E4271` | `Mandate request declined by the customer` | Customer declined the mandate. | Customer rejected UPI Autopay/SI approval. | Ask customer to create a new mandate. |
| `E4272` | `Transaction declined due to timeout at Issuer/Acquirer end` | Mandate authentication timed out. | Issuer/acquirer did not respond. | Keep status pending until verified; retry mandate setup if final status is failed. |
| `E4278` | `Transaction failed as mandate setup failed from customer's bank` | Mandate setup failed at customer bank. | Bank rejected mandate or account does not support it. | Ask customer to use another account/payment method. |
| `E4682` | `Recurrence Payment is in progress` | Recurring debit is already being processed. | Duplicate or parallel recurring request. | Do not retry immediately. Wait for final status or webhook. |
| `E4683` | `Recurrence Payment is already completed` | Recurring debit was already completed. | Duplicate debit request for the same cycle. | Treat as duplicate and reconcile existing debit. |

## Deep dives

### Invalid Hash Error

#### When it occurs

Invalid hash errors occur during request validation when PayU receives a `hash` that does not match the hash PayU calculates from the submitted fields.

Typical symptoms:

* Hosted Checkout page shows a hash mismatch or transaction dropped message.
* Payment request fails before bank redirection.
* Error code is `E700` or error description is `SECURE_HASH_FAILURE`.

#### Sample request

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=gtKFFx" \
  -d "txnid=txn_10001" \
  -d "amount=10.00" \
  -d "productinfo=Test Product" \
  -d "firstname=John" \
  -d "email=john@example.com" \
  -d "phone=9999999999" \
  -d "surl=https://example.com/payu/success" \
  -d "furl=https://example.com/payu/failure" \
  -d "hash=bad_hash_value"
```

#### Sample response

```json
{
  "status": "failure",
  "error": "E700",
  "error_Message": "Validation of secure hash failed",
  "unmappedstatus": "failed",
  "txnid": "txn_10001"
}
```

#### Root cause

The hash was not generated from the exact values submitted to PayU.

Common mistakes:

* Using Merchant ID instead of merchant key.
* Using key in place of salt or salt in place of key.
* Missing pipe delimiters for blank `udf1` to `udf5`.
* Generating hash before formatting `amount`, then posting a different value.
* Trimming, encoding, lowercasing, or changing `productinfo`, `firstname`, or `email` after hash generation.
* Using test key with production salt or production key with test salt.
* Generating hash on frontend and exposing salt.

#### Debugging guide

1. Log the raw server-side hash string before hashing. Do not log salt in shared logs.
2. Confirm the sequence:

   ```text
   key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
   ```

3. Confirm the posted values exactly match the values in the hash string.
4. Confirm blank UDF fields are represented by empty positions, not removed.
5. Confirm the correct environment:
   * Test: test key + test salt + test endpoint.
   * Production: production key + production salt + production endpoint.
6. Generate SHA-512 in lowercase hexadecimal.
7. Move hash generation to backend if it is currently generated in browser/mobile code.
8. Validate response hash before updating order status.

> **Common Mistake**
>
> `10`, `10.0`, and `10.00` are different strings for hash generation. If you hash `10.00`, post `10.00`.

### Payment Failed or Declined

#### When it occurs

Payment failures occur after the customer is redirected to PayU, issuer, bank, wallet, or UPI app and the payment cannot be completed.

Typical statuses:

* `status=failure`
* `unmappedstatus=failed`
* `error=E308`, `E348`, `E500`, `E306`, `E300`, `E1000`, or issuer-specific code
* `field7=AUCNEGATIVE`, `AUTHNEGATIVE`, `TXNNEGATIVE`, or `VERNEGATIVE`

#### Sample response

```json
{
  "mihpayid": "403993715525079998",
  "txnid": "txn_10002",
  "amount": "499.00",
  "status": "failure",
  "unmappedstatus": "failed",
  "error": "E348",
  "error_Message": "Transaction declined by the issuer",
  "PG_TYPE": "CC-PG",
  "field7": "AUTHNEGATIVE",
  "field8": "Refer to card issuer",
  "field9": "ISSUER_DECLINED",
  "bank_ref_num": "",
  "hash": "response_hash"
}
```

#### Root cause

Failures are commonly caused by customer action, issuer/bank rules, payment instrument restrictions, or technical timeouts.

Examples:

* Customer entered wrong OTP/CVV.
* Customer cancelled or abandoned payment.
* Issuer declined due to risk, limits, insufficient funds, or card restrictions.
* Bank/PSP was unavailable.
* Payment method is not enabled for the merchant.

#### Debugging guide

1. Verify response hash before using the payload.
2. Match `txnid`, `amount`, and `key` with your order record.
3. Read `status`, `unmappedstatus`, `error`, `error_Message`, `field7`, `field8`, and `field9`.
4. Use `field7` to identify the failed stage:
   * `AUCNEGATIVE`: authentication failed.
   * `AUTHNEGATIVE`: authorization failed.
   * `TXNNEGATIVE`: bank/wallet returned failed status.
   * `VERNEGATIVE`: verification confirmed failed status.
5. If failure is issuer/customer driven, show an actionable message and offer another payment method.
6. If failure is technical or timeout driven, verify final status before creating another attempt.
7. For repeated failures on one method, test another payment mode and check merchant configuration.

> **Pro Tip**
>
> Do not show raw bank text directly to customers if it is unclear. Map it to a clear message such as "Your bank declined the payment. Try another card or contact your bank."

### Pending Transactions

#### When it occurs

Pending transactions occur when PayU has not received a final success or failure from the bank, PSP, wallet, or UPI app.

Typical statuses:

* `status=pending`
* `unmappedstatus=in progress`
* `error=E227`
* `field7=TXNPENDING`, `VERPENDING`, `TXNERROR`, or `VERERROR`

#### Sample response

```json
{
  "mihpayid": "403993715525036528",
  "txnid": "txn_10003",
  "amount": "100.00",
  "status": "pending",
  "unmappedstatus": "in progress",
  "error": "E227",
  "error_Message": "Transaction is Pending",
  "PG_TYPE": "UPI-PG",
  "field7": "TXNPENDING",
  "field8": "Awaiting response from bank",
  "field9": "TRANSACTION_PENDING",
  "hash": "response_hash"
}
```

#### Root cause

The final state is not yet known.

Common causes:

* Bank callback is delayed.
* UPI app did not send final response yet.
* Corporate net banking transaction is waiting for checker approval.
* Browser redirect failed but bank processing continued.
* Verification call timed out.

#### Debugging guide

1. Keep the order in `payment_pending`; do not mark it paid or failed immediately.
2. Store `mihpayid`, `txnid`, `amount`, `status`, `unmappedstatus`, `error`, `field7`, `field8`, and `bank_ref_num`.
3. Listen for webhook updates.
4. Query Transaction Detail APIs using the original transaction identifiers.
5. Reconcile final status before allowing a second payment for the same order.
6. If customer retries, create a new `txnid` and link both attempts to the same merchant order.

> **Common Mistake**
>
> Treating pending as failed can create false failures. Treating pending as success can create revenue leakage. Keep a separate pending state.

### Webhook Failures

#### When it occurs

Webhook failures occur when PayU sends a server-to-server callback but your endpoint does not accept or process it successfully.

Typical symptoms:

* PayU delivery status is `Failed`.
* `response_code` is `401`, `403`, `404`, `405`, `500`, `502`, `503`, or `504`.
* `webhook_delivery_message` contains HTTP error text.
* Browser redirect was received, but server-side webhook was not.

#### Sample webhook delivery failure

```json
{
  "timestamp": "2026-02-27 14:24:45.000000",
  "event_type": "payment",
  "status": "Failed",
  "webhook_delivery_message": "HTTP/2 405",
  "http_method": "POST",
  "endpoint": "https://example.com/payu/webhook",
  "response_code": 405,
  "endpoint_latency": 7,
  "event_payload": {
    "mihpayid": "27472524682",
    "txnid": "txn_10004",
    "amount": "1.00",
    "status": "failure",
    "unmappedstatus": "failed",
    "error": "E500",
    "error_Message": "Bank failed to authenticate the customer",
    "hash": "response_hash"
  }
}
```

#### Root cause

Your webhook endpoint rejected PayU's request or failed while processing it.

Common causes:

* Endpoint does not allow `POST`.
* Endpoint accepts `application/json` only; PayU may send form data or `application/x-www-form-urlencoded`.
* WAF/firewall blocks PayU IPs.
* Endpoint requires browser session authentication.
* Handler performs slow business logic before returning response.
* Duplicate webhook caused a database uniqueness error.

#### Debugging guide

1. Confirm the webhook URL is configured for the correct merchant key.
2. Confirm endpoint is reachable publicly over HTTPS.
3. Allow PayU webhook IPs listed in [Webhooks for Payments](doc:webhooks).
4. Accept `POST` requests.
5. Accept form data and `application/x-www-form-urlencoded`.
6. Verify response hash and match `txnid`/`amount`.
7. Store the webhook payload durably before processing.
8. Return `2xx` after durable receipt.
9. Process fulfillment asynchronously.
10. Make updates idempotent using `mihpayid`, `txnid`, and event status.

> **Pro Tip**
>
> A webhook handler should be boring: authenticate, validate hash, persist, return `2xx`, then process asynchronously.

## Debugging playbook

Use this flow when a payment does not behave as expected.

### 1. Identify where the failure occurred

| Where it failed | What to inspect |
| --- | --- |
| Before redirect to PayU | Request payload, mandatory parameters, hash string, endpoint, key/salt environment |
| On PayU checkout page | `txnid`, `amount`, hash, merchant configuration, payment mode availability |
| On bank/issuer/UPI app | `error`, `error_Message`, `field7`, `field8`, issuer decline codes |
| After customer returns | Browser redirect payload, response hash, `status`, `unmappedstatus` |
| Server-to-server notification | Webhook delivery logs, HTTP status, firewall/WAF, content type handling |
| Reconciliation | Transaction Detail APIs, `mihpayid`, `txnid`, final status |

### 2. Check these fields first

Capture and log these fields for every transaction attempt:

* Merchant order ID from your system.
* PayU `txnid`.
* PayU `mihpayid`.
* `amount`.
* `status`.
* `unmappedstatus`.
* `error`.
* `error_Message` or `error_message`.
* `PG_TYPE`.
* `bank_ref_num` or `bank_ref_no`.
* `field7`, `field8`, `field9`.
* Response `hash`.
* Webhook delivery HTTP status and response body.

Do not log:

* Salt.
* Plain hash string in shared logs.
* Full card number, CVV, OTP, or sensitive customer authentication data.

### 3. Isolate frontend vs backend vs PayU

| Symptom | Likely owner | How to isolate |
| --- | --- | --- |
| Button click does nothing | Frontend | Check browser console, network tab, form submit, client-side validation. |
| Backend returns error before PayU | Backend | Check server logs, payload construction, hash generation, mandatory fields. |
| PayU shows hash/missing parameter error | Backend integration | Compare raw request with hash string and API reference. |
| Customer reaches bank but payment fails | Bank/customer/payment method | Inspect `error`, `field7`, `field8`, and issuer decline reason. |
| Redirect not received | Customer browser/network | Use webhook and Transaction Detail APIs as source of truth. |
| Webhook not received | Merchant infrastructure | Check endpoint URL, firewall, WAF, HTTP method, content type, TLS, application logs. |
| Status differs between redirect and webhook | Race condition or late bank update | Use verified server-side status and reconciliation rules. |

### 4. Inspect logs in this order

1. Backend payment-initiation logs.
2. Raw request sent to PayU, excluding salt and sensitive payment data.
3. Server-side hash-generation logs.
4. Browser redirect response logs.
5. Webhook receipt and delivery logs.
6. Transaction Detail API response.
7. Order state transition logs.
8. Refund or recurring debit logs if applicable.

### 5. Use these tools

* **PayU Dashboard**: Check transaction status, payment mode enablement, key/salt, webhook configuration.
* **Transaction Detail APIs**: Verify final status for `txnid` or `mihpayid`.
* **Server logs**: Confirm request values and hash generation.
* **Webhook logs**: Confirm delivery, HTTP status, and handler errors.
* **Browser DevTools**: Debug frontend submit, redirects, blocked requests, and callback pages.
* **API client**: Reproduce request using form-encoded payloads.

## Integration best practices

### Generate and validate hash correctly

* Generate hashes only on your backend.
* Use the exact values that will be posted to PayU.
* Preserve pipe delimiters for blank fields.
* Keep test and production keys/salts separate.
* Never send salt to frontend, mobile apps, URLs, logs, or analytics tools.
* Validate PayU response hash before updating order status.

### Separate backend and frontend responsibilities

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

### Handle retries and idempotency

* Use a unique `txnid` for every new payment attempt.
* Keep a stable merchant order ID in your system and map multiple PayU attempts to it.
* Do not retry a pending transaction blindly.
* Before creating a new attempt, check whether the previous attempt succeeded, failed, or is still pending.
* Make webhook processing idempotent with a unique key such as `mihpayid` + `txnid` + final status.
* Protect the checkout button from double-click submissions.
* Do not create duplicate fulfillment on duplicate redirects or duplicate webhooks.

### Build clear status handling

Recommended merchant-side states:

| Merchant state | PayU signal | Action |
| --- | --- | --- |
| `payment_initiated` | Request created | Await redirect/webhook/status. |
| `payment_pending` | `status=pending` or `E227` | Do not fulfill. Poll/reconcile. |
| `payment_success` | `status=success` and hash valid | Fulfill order. |
| `payment_failed` | `status=failure` and final status verified | Show retry options. |
| `payment_dropped` | `E231`, timeout, abandoned flow | Verify status before retry. |
| `payment_review` | Conflicting redirect/webhook/status | Hold fulfillment and reconcile. |

## Sample error responses

The following examples are shown as JSON for readability. Depending on your integration, PayU may return fields through browser redirect, form post, webhook, or API response.

### Success

```json
{
  "mihpayid": "403993715525079998",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "gtKFFx",
  "txnid": "txn_10005",
  "amount": "10.00",
  "productinfo": "Test Product",
  "firstname": "John",
  "email": "john@example.com",
  "phone": "9999999999",
  "error": "E000",
  "error_Message": "No Error",
  "bank_ref_num": "123456789",
  "PG_TYPE": "CC-PG",
  "hash": "response_hash"
}
```

### Failed transaction

```json
{
  "mihpayid": "403993715525080001",
  "mode": "DC",
  "status": "failure",
  "unmappedstatus": "failed",
  "key": "gtKFFx",
  "txnid": "txn_10006",
  "amount": "250.00",
  "productinfo": "Test Product",
  "firstname": "John",
  "email": "john@example.com",
  "phone": "9999999999",
  "error": "E500",
  "error_Message": "Bank failed to authenticate the customer",
  "PG_TYPE": "DC-PG",
  "field7": "AUCNEGATIVE",
  "field8": "Message Received Invalid",
  "field9": "UNKNOWN",
  "hash": "response_hash"
}
```

### Invalid hash

```json
{
  "status": "failure",
  "unmappedstatus": "failed",
  "txnid": "txn_10007",
  "error": "E700",
  "error_Message": "Validation of secure hash failed"
}
```

### Authentication failure

```json
{
  "mihpayid": "403993715525080002",
  "status": "failure",
  "unmappedstatus": "failed",
  "txnid": "txn_10008",
  "amount": "999.00",
  "error": "E300",
  "error_Message": "Card failed 3D authentication as 3 D Secure signatures did not match",
  "PG_TYPE": "CC-PG",
  "field7": "3DS_CHALLENGE_NEGATIVE",
  "field8": "Authentication failed",
  "field9": "SECURE_3D_PASSWORD_ERROR",
  "hash": "response_hash"
}
```

## Escalation checklist

If you need PayU Support or Integration Team assistance, include:

* Merchant key, not salt.
* Environment: test or production.
* `txnid`.
* `mihpayid`, if generated.
* Timestamp with timezone.
* Payment mode and `PG_TYPE`.
* Error code and `error_Message`.
* `field7`, `field8`, and `field9`.
* Webhook endpoint and delivery HTTP status, if relevant.
* Sanitized request payload.
* Confirmation that response hash validation was performed.

If you are unable to resolve the issue, contact [PayU Support](https://help.payu.in/).
