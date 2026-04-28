---
title: Debugging Playbook
excerpt: Step-by-step troubleshooting flow for PayU payment issues.
deprecated: false
hidden: false
metadata:
  title: Debugging Playbook
  description: Step-by-step troubleshooting flow for PayU Hosted Checkout, Merchant Hosted Checkout, S2S, webhooks, and recurring payments.
  robots: index
next:
  description: ''
---

Use this flow when a payment does not behave as expected.

## 1. Identify where the failure occurred

| Where it failed | What to inspect |
| --- | --- |
| Before redirect to PayU | Request payload, mandatory parameters, hash string, endpoint, key/salt environment |
| On PayU checkout page | `txnid`, `amount`, hash, merchant configuration, payment mode availability |
| On bank/issuer/UPI app | `error`, `error_Message`, `field7`, `field8`, issuer decline codes |
| After customer returns | Browser redirect payload, response hash, `status`, `unmappedstatus` |
| Server-to-server notification | Webhook delivery logs, HTTP status, firewall/WAF, content type handling |
| Reconciliation | Transaction Detail APIs, `mihpayid`, `txnid`, final status |

## 2. Check these fields first

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

## 3. Isolate frontend vs backend vs PayU

| Symptom | Likely owner | How to isolate |
| --- | --- | --- |
| Button click does nothing | Frontend | Check browser console, network tab, form submit, client-side validation. |
| Backend returns error before PayU | Backend | Check server logs, payload construction, hash generation, mandatory fields. |
| PayU shows hash/missing parameter error | Backend integration | Compare raw request with hash string and API reference. |
| Customer reaches bank but payment fails | Bank/customer/payment method | Inspect `error`, `field7`, `field8`, and issuer decline reason. |
| Redirect not received | Customer browser/network | Use webhook and Transaction Detail APIs as source of truth. |
| Webhook not received | Merchant infrastructure | Check endpoint URL, firewall, WAF, HTTP method, content type, TLS, application logs. |
| Status differs between redirect and webhook | Race condition or late bank update | Use verified server-side status and reconciliation rules. |

## 4. Inspect logs in this order

1. Backend payment-initiation logs.
2. Raw request sent to PayU, excluding salt and sensitive payment data.
3. Server-side hash-generation logs.
4. Browser redirect response logs.
5. Webhook receipt and delivery logs.
6. Transaction Detail API response.
7. Order state transition logs.
8. Refund or recurring debit logs if applicable.

## 5. Use these tools

* **PayU Dashboard**: Check transaction status, payment mode enablement, key/salt, webhook configuration.
* **Transaction Detail APIs**: Verify final status for `txnid` or `mihpayid`.
* **Server logs**: Confirm request values and hash generation.
* **Webhook logs**: Confirm delivery, HTTP status, and handler errors.
* **Browser DevTools**: Debug frontend submit, redirects, blocked requests, and callback pages.
* **API client**: Reproduce request using form-encoded payloads.

## Quick triage checklist

| Check | Pass condition |
| --- | --- |
| Environment | Test key/salt used only with test endpoint; production key/salt used only with production endpoint. |
| Transaction identity | `txnid`, merchant order ID, and `mihpayid` are stored and searchable. |
| Hash | Request hash and response hash validation use the exact documented sequence. |
| Status | Merchant system has separate success, failed, pending, dropped, and review states. |
| Webhook | Endpoint accepts PayU POST callbacks and returns `2xx` quickly after durable receipt. |
| Retry | New customer attempt uses a new `txnid`; previous attempt is reconciled first. |

> **Pro Tip**
>
> Most production escalations become faster when every order timeline has three linked records: merchant order ID, PayU `txnid`, and PayU `mihpayid`.
