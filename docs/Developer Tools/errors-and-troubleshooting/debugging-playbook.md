---
title: Debugging Playbook
excerpt: >-
  Step-by-step troubleshooting flow for PayU Hosted Checkout, Merchant Hosted
  Checkout, S2S, Webhooks, and Recurring Payments.
deprecated: false
hidden: false
metadata:
  robots: index
---
Use this flow when you get errors during transactions.

## Step 1. Identify the Failure Step

<Accordion title="Where the Failure Happened" icon="fa-info-circle">
  | Where it Failed               | What to Inspect                                                                    | Recommended Fix                                                                                        |
  | ----------------------------- | ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
  | Before redirect to PayU       | Request payload, mandatory parameters, hash string, endpoint, key/salt environment | Fix backend payload construction and regenerate hash from exact posted values.                         |
  | On PayU checkout page         | `txnid`, `amount`, hash, merchant configuration, payment mode availability         | Validate merchant configuration, payment mode enablement, and request/hash values.                     |
  | On bank/issuer/UPI app        | `error`, `error_Message`, `field7`, `field8`, issuer decline codes                 | Show customer-safe retry guidance and offer alternate payment methods after final status verification. |
  | After customer returns        | Browser redirect payload, response hash, `status`, `unmappedstatus`                | Verify response hash and reconcile with webhook/status API before fulfilling.                          |
  | Server-to-server notification | Webhook delivery logs, HTTP status, firewall/WAF, content type handling            | Fix endpoint availability, method/content-type handling, IP allowlisting, and idempotency.             |
  | Reconciliation                | Transaction Detail APIs, `mihpayid`, `txnid`, final status                         | Use verified final status as source of truth and update the merchant order state idempotently.         |
</Accordion>

## Step 2. Check these Fields First

Capture and log these fields for every transaction attempt:

<Accordion title="Fields to Check" icon="fa-info-circle">
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
</Accordion>

**Do not log:**

<Accordion title="Do Not Log These" icon="fa-info-circle">
  * Salt.
  * Plain hash string in shared logs.
  * Full card number, CVV, OTP, or sensitive customer authentication data.
</Accordion>

## 3. Isolate Frontend vs Backend vs PayU

<Accordion title="Error Categories" icon="fa-list">
  | Error Scenarios                                     | Team                               | How to Isolate                                                                       | Recommended Fix                                                                                                                                                       |
  | --------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Button not working                                  | Frontend                           | Check browser console, network tab, form submit, client-side validation.             | Fix client validation, form submit, or JavaScript errors before creating a PayU request.                                                                              |
  | Backend returns error before PayU                   | Backend                            | Check server logs, payload construction, hash generation, mandatory fields.          | Correct payload validation and return actionable errors to frontend.                                                                                                  |
  | PayU shows hash/missing parameter error             | Backend integration                | Compare raw request with hash string and API reference.                              | Add missing fields, preserve delimiters, and regenerate hash server-side. Use the PayU in-house hash generator tool to generate a hash value depending on your logic. |
  | Customer reaches the bank website but payment fails | Bank/customer/payment method       | Inspect `error`, `field7`, `field8`, and issuer decline reason.                      | Verify final status, then ask customer to retry or use another payment method.                                                                                        |
  | Redirect not received                               | Customer browser/network           | Use webhook and Transaction Detail APIs as source of truth.                          | Do not depend on redirect alone; reconcile through webhook/status API.                                                                                                |
  | Webhook not received                                | Merchant infrastructure            | Check endpoint URL, firewall, WAF, HTTP method, content type, TLS, application logs. | Fix endpoint delivery path and allow PayU POST callbacks.                                                                                                             |
  | Status differs between redirect and webhook         | Race condition or late bank update | Use verified server-side status and reconciliation rules.                            | Resolve order state using the latest verified webhook/status API result.                                                                                              |
</Accordion>

## 4. Inspect Logs in this Order

Start inspecting logs in the below order:

<Accordion title="Logs Order" icon="fa-list">
  1. Backend payment-initiation logs.
  2. Raw request sent to PayU, excluding salt and sensitive payment data.
  3. Server-side hash-generation logs.
  4. Browser redirect response logs.
  5. Webhook receipt and delivery logs.
  6. Transaction Detail API response.
  7. Order state transition logs.
  8. Refund or recurring debit logs if applicable.
</Accordion>

## Quick Triage Checklist

<Accordion title="Triage Checklist" icon="fa-list">
  | Check                | Pass condition                                                                                      | Recommended fix                                                                      |
  | -------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ |
  | Environment          | Test key/salt used only with test endpoint; production key/salt used only with production endpoint. | Separate environment config and block mixed key/salt/endpoint combinations.          |
  | Transaction identity | `txnid`, merchant order ID, and `mihpayid` are stored and searchable.                               | Persist all identifiers at initiation and update records on redirect/webhook/status. |
  | Hash                 | Request hash and response hash validation use the exact documented sequence.                        | Centralize hash generation/validation in backend code.                               |
  | Status               | Merchant system has separate success, failed, pending, dropped, and review states.                  | Add explicit state mapping for PayU `status`, `unmappedstatus`, and error codes.     |
  | Webhook              | Endpoint accepts PayU POST callbacks and returns `2xx` quickly after durable receipt.               | Persist payload first, queue downstream processing, and return fast `2xx`.           |
  | Retry                | New customer attempt uses a new `txnid`; previous attempt is reconciled first.                      | Enforce idempotency and create a fresh PayU attempt only after status check.         |
</Accordion>

<Callout icon="👍" theme="okay">
  **Pro Tips:**

  Most production escalations become faster when every order timeline has three linked records: merchant order ID, PayU `txnid`, and PayU `mihpayid`.
</Callout>

<br />
