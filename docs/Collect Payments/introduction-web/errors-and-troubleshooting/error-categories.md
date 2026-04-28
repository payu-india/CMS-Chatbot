---
title: Error Categories
excerpt: Understand the main classes of PayU errors and where they occur in the payment flow.
deprecated: false
hidden: false
metadata:
  title: Error Categories
  description: Categorized guide to PayU authentication, hash, validation, payment, API, webhook, and recurring payment errors.
  robots: index
next:
  description: ''
---

Use categories to quickly identify whether an issue belongs to your checkout frontend, backend integration, PayU configuration, bank/issuer processing, webhook infrastructure, or recurring payment setup.

## Authentication and authorization errors

These happen when PayU, the issuer, bank, PSP, or payment network cannot authenticate the customer or authorize the payment.

| Signal | What it means | What to check |
| --- | --- | --- |
| `E306` | Card authentication failure | OTP, 3DS challenge, user abandonment |
| `E300` | 3DS signatures did not match | Incorrect OTP/password, issuer authentication issue |
| `E1000` | 3-D secure authentication failed | Challenge failure or timeout |
| `E317` | Payer could not be authenticated | Issuer or ACS authentication failure |
| `E348` | Issuer declined authorization | Card limits, risk rules, issuer restrictions |

Common causes:

* Incorrect OTP, CVV, or card details.
* Customer closed the authentication page.
* Issuer declined due to risk, limits, or card restrictions.
* Merchant is not enabled for the requested payment flow.

## Hash and security errors

These happen when PayU cannot validate request or response integrity.

| Signal | What it means | What to check |
| --- | --- | --- |
| `E700` | Validation of secure hash failed | Hash sequence, key, salt, blank delimiters |
| `SECURE_HASH_FAILURE` | Security validation failed | Tampered request or mismatched posted values |
| Response hash mismatch | PayU response could not be verified | Reverse hash sequence and response values |

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

| Signal | What it means | What to check |
| --- | --- | --- |
| `E1101` | Invalid params shared by merchant | Request body and field values |
| `E4156` / `E4373` | Validation error | Missing/malformed fields |
| Missing parameter | Mandatory field missing | `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash` |
| Invalid amount | Amount rejected | Format, decimals, amount used in hash |
| Duplicate `txnid` | Transaction ID already used | Retry behavior and ID generation |

Common causes:

* Backend omitted required fields.
* Request was submitted with the wrong content type.
* `pg` and `bankcode` do not match the selected payment method.
* `txnid` is reused for a new payment attempt.

## Payment failures

These happen after payment initiation when the customer, issuer, bank, PSP, wallet, or UPI app declines or cannot complete the payment.

| Signal | What it means | What to check |
| --- | --- | --- |
| `E308` | Transaction failed at bank end | Bank response and final status |
| `E500` | Bank failed to authenticate customer | Bank authentication page, OTP flow |
| `E227` | Transaction is pending | Webhook/status API before retry |
| `E507` | Transaction expired | Customer timeout |
| `E231` | Transaction dropped | Browser close, redirect failure, no bank response |

Common causes:

* Customer cancelled or abandoned the payment.
* Bank/PSP timed out.
* Issuer declined the payment instrument.
* Payment method is not enabled for the merchant.

## Network and API errors

These happen when an API request cannot be processed due to timeout, service unavailability, routing, or credential issues.

| Signal | What it means | What to check |
| --- | --- | --- |
| `E1201` | Not authorized for transaction | Feature/payment mode enablement |
| `E1631` | Merchant validation failed | Merchant key, environment, MID status |
| `E1621` | S2S access not enabled | Merchant S2S configuration |
| `E1622` | S2S not enabled on selected gateway | `pg`, `bankcode`, route configuration |
| `E1654` | Route to merchant unavailable | Gateway route availability |
| `E4526` | Record not found | Identifier and environment mismatch |

## Webhook errors

These happen when PayU cannot deliver the server-to-server notification or when your system cannot process it safely.

| Signal | What it means | What to check |
| --- | --- | --- |
| `401` / `403` | Endpoint rejected request | Auth rules, firewall, WAF |
| `404` | Endpoint not found | Webhook URL and deployment |
| `405` | Method not allowed | Accept `POST` |
| `5xx` | Endpoint failed | Handler exceptions, dependency outage |
| Timeout | Endpoint too slow | Queue processing and return `2xx` quickly |

Common causes:

* Endpoint accepts JSON only, but PayU may send form data.
* PayU IPs are blocked.
* Handler requires browser session authentication.
* Duplicate webhook is not handled idempotently.

## Recurring and SI errors

These happen during Standing Instruction (SI), UPI Autopay, mandate registration, mandate modification, or recurring debit.

| Signal | What it means | What to check |
| --- | --- | --- |
| `E4530` | Mandate start date is less than current date | Date and timezone handling |
| `E4531` | Mandate end date is less than start date | Date range validation |
| `E4112` | Mandate and transaction amount differ | Billing rule and mandate amount |
| `E4105` | Recurring sequence mismatch | Sequence number and parallel debit attempts |
| `E4271` | Mandate declined by customer | Customer approval status |
| `E4682` | Recurrence payment is in progress | Duplicate or parallel recurring request |
| `E4683` | Recurrence payment is already completed | Duplicate debit for same cycle |

> **Pro Tip**
>
> For recurring payments, store mandate identifiers, billing rule, billing amount, debit sequence, and latest webhook status together. Most SI issues are caused by state mismatch across these fields.
