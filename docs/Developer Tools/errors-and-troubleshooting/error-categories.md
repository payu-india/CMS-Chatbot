---
title: Error Categories
excerpt: >-
  Categorised guide to PayU authentication, hash, validation, payment, API,
  webhook, and recurring payment errors.
deprecated: false
hidden: false
metadata:
  description: >-
    Understand the main classes of PayU errors and where they occur in the
    payment flow.
  robots: index
---
Error categories lets you quickly identify whether an issue belongs to your checkout frontend, backend integration, PayU configuration, bank/issuer processing, webhook infrastructure, or recurring payment setup.

## Authentication and Authorisation Errors

These happen when PayU, the issuer, bank, PSP, or payment network cannot authenticate the customer or authorize the payment.

<Accordion title="Errors and Fixes" icon="fa-wrench">
  | Error code/type | Description                      | What to check                                       | Recommended fix                                                         |
  | --------------- | -------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------- |
  | `E306`          | Card authentication failure      | OTP, 3DS challenge, user abandonment                | Ask the customer to retry authentication or use another payment method. |
  | `E300`          | 3DS signatures did not match     | Incorrect OTP/password, issuer authentication issue | Let the customer retry 3DS; if repeated, suggest another card.          |
  | `E1000`         | 3-D secure authentication failed | Challenge failure or timeout                        | Verify final status, then allow a new attempt with a new `txnid`.       |
  | `E317`          | Payer could not be authenticated | Issuer or ACS authentication failure                | Show retry and alternate payment options.                               |
  | `E348`          | Issuer declined authorization    | Card limits, risk rules, issuer restrictions        | Ask the customer to contact the issuer or use another payment method.   |
</Accordion>

<Accordion title="Common Causes" icon="fa-question-circle">
  * Incorrect OTP, CVV, or card details.
  * Customer closed the authentication page.
  * Issuer declined due to risk, limits, or card restrictions.
  * Merchant is not enabled for the requested payment flow.
</Accordion>

## Hash and security errors

These happen when PayU cannot validate request or response integrity.

| Signal                 | What it means                       | What to check                                | Recommended fix                                                                                    |
| ---------------------- | ----------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `E700`                 | Validation of secure hash failed    | Hash sequence, key, salt, blank delimiters   | Regenerate the hash server-side using the exact posted values and correct salt.                    |
| `SECURE_HASH_FAILURE`  | Security validation failed          | Tampered request or mismatched posted values | Compare raw request fields with the hash string and remove salt from frontend exposure.            |
| Response hash mismatch | PayU response could not be verified | Reverse hash sequence and response values    | Do not update order status until reverse hash validation passes or status is verified server-side. |

Common causes:

* Incorrect SHA-512 sequence.
* Missing delimiters for empty UDF fields.
* Using Merchant ID instead of merchant key.
* Test key with production salt, or production key with test salt.
* Hash generated in frontend code.

> **Common Mistake**
>
> `10`, `10.0`, and `10.00` are different strings for hash generation. Hash and submit the exact same amount value.

## Validation errors

These happen before PayU can process the payment request.

| Signal            | What it means                     | What to check                                                                                  | Recommended fix                                                                           |
| ----------------- | --------------------------------- | ---------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| `E1101`           | Invalid params shared by merchant | Request body and field values                                                                  | Validate payload against the API reference before posting to PayU.                        |
| `E4156` / `E4373` | Validation error                  | Missing/malformed fields                                                                       | Fix missing, invalid, or unsupported fields and retry with a new valid request.           |
| Missing parameter | Mandatory field missing           | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` | Send all mandatory fields and include empty positions in the hash string.                 |
| Invalid amount    | Amount rejected                   | Format, decimals, amount used in hash                                                          | Send amount as a consistent decimal string, for example `10.00`, and hash the same value. |
| Duplicate `txnid` | Transaction ID already used       | Retry behavior and ID generation                                                               | Generate a unique `txnid` for every new payment attempt.                                  |

Common causes:

* Backend omitted required fields.
* Request was submitted with the wrong content type.
* `pg` and `bankcode` do not match the selected payment method.
* `txnid` is reused for a new payment attempt.

## Payment failures

These happen after payment initiation when the customer, issuer, bank, PSP, wallet, or UPI app declines or cannot complete the payment.

| Signal | What it means                        | What to check                                     | Recommended fix                                                                   |
| ------ | ------------------------------------ | ------------------------------------------------- | --------------------------------------------------------------------------------- |
| `E308` | Transaction failed at bank end       | Bank response and final status                    | Treat as failed unless a verified webhook/status response later confirms success. |
| `E500` | Bank failed to authenticate customer | Bank authentication page, OTP flow                | Verify final status, then allow the customer to retry.                            |
| `E227` | Transaction is pending               | Webhook/status API before retry                   | Keep the order pending and reconcile before allowing another attempt.             |
| `E507` | Transaction expired                  | Customer timeout                                  | Create a new payment attempt with a new `txnid`.                                  |
| `E231` | Transaction dropped                  | Browser close, redirect failure, no bank response | Verify status before retrying; if not successful, create a new attempt.           |

Common causes:

* Customer cancelled or abandoned the payment.
* Bank/PSP timed out.
* Issuer declined the payment instrument.
* Payment method is not enabled for the merchant.

## Network and API errors

These happen when an API request cannot be processed due to timeout, service unavailability, routing, or credential issues.

| Signal  | What it means                       | What to check                         | Recommended fix                                                           |
| ------- | ----------------------------------- | ------------------------------------- | ------------------------------------------------------------------------- |
| `E1201` | Not authorized for transaction      | Feature/payment mode enablement       | Enable the requested feature/payment mode or use an enabled route.        |
| `E1631` | Merchant validation failed          | Merchant key, environment, MID status | Verify key/salt, environment, MID status, and merchant activation.        |
| `E1621` | S2S access not enabled              | Merchant S2S configuration            | Request S2S enablement for the merchant account.                          |
| `E1622` | S2S not enabled on selected gateway | `pg`, `bankcode`, route configuration | Use an S2S-enabled gateway route or update configuration.                 |
| `E1654` | Route to merchant unavailable       | Gateway route availability            | Retry later or contact PayU if the same route keeps failing.              |
| `E4526` | Record not found                    | Identifier and environment mismatch   | Confirm `txnid`, `mihpayid`, key, and environment before retrying lookup. |

## Webhook errors

These happen when PayU cannot deliver the server-to-server notification or when your system cannot process it safely.

| Signal        | What it means             | What to check                             | Recommended fix                                                           |
| ------------- | ------------------------- | ----------------------------------------- | ------------------------------------------------------------------------- |
| `401` / `403` | Endpoint rejected request | Auth rules, firewall, WAF                 | Allow PayU webhook delivery and use webhook-safe authentication.          |
| `404`         | Endpoint not found        | Webhook URL and deployment                | Correct the configured webhook URL and deploy the route.                  |
| `405`         | Method not allowed        | Accept `POST`                             | Enable `POST` on the webhook endpoint.                                    |
| `5xx`         | Endpoint failed           | Handler exceptions, dependency outage     | Persist first, process asynchronously, and fix handler/dependency errors. |
| Timeout       | Endpoint too slow         | Queue processing and return `2xx` quickly | Return `2xx` after durable receipt and move slow work to a queue.         |

Common causes:

* Endpoint accepts JSON only, but PayU may send form data.
* PayU IPs are blocked.
* Handler requires browser session authentication.
* Duplicate webhook is not handled idempotently.

## Recurring and SI errors

These happen during Standing Instruction (SI), UPI Autopay, mandate registration, mandate modification, or recurring debit.

| Signal  | What it means                                | What to check                               | Recommended fix                                                              |
| ------- | -------------------------------------------- | ------------------------------------------- | ---------------------------------------------------------------------------- |
| `E4530` | Mandate start date is less than current date | Date and timezone handling                  | Send a valid current/future start date.                                      |
| `E4531` | Mandate end date is less than start date     | Date range validation                       | Validate mandate date range before request submission.                       |
| `E4112` | Mandate and transaction amount differ        | Billing rule and mandate amount             | Align debit amount with mandate amount and billing rule.                     |
| `E4105` | Recurring sequence mismatch                  | Sequence number and parallel debit attempts | Use the correct sequence and prevent concurrent debits for the same mandate. |
| `E4271` | Mandate declined by customer                 | Customer approval status                    | Ask the customer to approve a new mandate.                                   |
| `E4682` | Recurrence payment is in progress            | Duplicate or parallel recurring request     | Wait for webhook/status confirmation; do not retry immediately.              |
| `E4683` | Recurrence payment is already completed      | Duplicate debit for same cycle              | Treat as duplicate and reconcile the existing debit.                         |

> **Pro Tip**
>
> For recurring payments, store mandate identifiers, billing rule, billing amount, debit sequence, and latest webhook status together. Most SI issues are caused by state mismatch across these fields.
