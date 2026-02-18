---
title: Suggested Integration Videos Based on Support Tickets Analysis
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

**Source:** All_Integration_Closed_Monthly_Cases-Nov_and_Dec25.csv (Nov–Dec 2025)  
**Purpose:** Reduce support tickets by covering the most-requested and most-failing topics in short, clear videos.

***

## Priority 1 – Highest impact (Web & API)

### 1. Web Integration Quick Start – Hosted Checkout (Redirect Flow)

**Target audience:** Developers integrating PayU for the first time (web).  
**Suggested duration:** 8–12 min.  
**Ticket driver:** 73 Doc Requirement (Web) + 1,220 Integration issues (many callback/redirect).

**Important points to highlight in the video:**

| # | Point                                              | Why it matters (from tickets)                                                                                                                                                        |
| - | -------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | **Where to get test key & salt**                   | Link to onboarding/UAT signup and to the doc “Generate test merchant key and salt”; avoid “key/salt issue” tickets.                                                                  |
| 2 | **Exact parameters for redirect to PayU**          | Show `key`, `salt`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, **surl**, **furl**, `hash` (and optional like `udf1` for order ID).                             |
| 3 | **How to build the hash (field order & encoding)** | Show the exact string order and that it’s UTF-8; mention “hash not matching” is usually wrong order or encoding.                                                                     |
| 4 | **Success and failure URLs (surl/furl)**           | Explain surl = success redirect, furl = failure redirect; must be HTTPS in production; no query params needed unless you use them.                                                   |
| 5 | **What happens after payment**                     | User is redirected to surl/furl with **post data**; show sample response fields (`status`, `mihpayid`, `txnid`, `amount`, etc.) and that verification must be server-side with hash. |
| 6 | **Verifying response on your server**              | Never trust only status in URL; always verify hash (or use verify API) before updating order status.                                                                                 |
| 7 | **Test vs live**                                   | Test URL (`https://test.payu.in/_payment`), test key/salt; switch to live URL and live credentials when going live.                                                                  |
| 8 | **One common mistake**                             | Callbacks “not working” often = surl/furl wrong, not whitelisted, or server not accepting POST; show where to whitelist and how to test locally (e.g. ngrok).                        |

***

### 2. Generating Dynamic Payment Links (Unique Link per Customer/Order)

**Target audience:** Merchants with a single CTA who need a unique payment link per customer/order.  
**Suggested duration:** 5–8 min.  
**Ticket driver:** Multiple “unique payment link for each customer” requests.

**Important points to highlight in the video:**

| # | Point                                | Why it matters                                                                                                           |
| - | ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| 1 | **Why dynamic links**                | One link per order/customer for correct tracking and reconciliation.                                                     |
| 2 | **Parameters that must be unique**   | `txnid` (unique per transaction), optional `udf1`/`udf2` for your order ID/customer ID.                                  |
| 3 | **Where txnid is used**              | In redirect, in callback, in settlement; show how it appears in PayU dashboard and in reconciliation.                    |
| 4 | **Server-side generation**           | Link must be built on server (never expose salt); show minimal server snippet (e.g. Node/PHP) that builds form and hash. |
| 5 | **Payment Links (dashboard) vs API** | When to use “Payment Links” product vs your own form; link to Payment Links doc if applicable.                           |

***

### 3. Callback and Response Handling – Success & Failure

**Target audience:** Developers who have redirect working but are unsure about handling surl/furl.  
**Suggested duration:** 6–10 min.  
**Ticket driver:** “Success callbacks not working”, “response format”, “what data is returned”.

**Important points to highlight in the video:**

| # | Point                                      | Why it matters                                                                                                                                                                                               |
| - | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | **Callback = redirect with POST**          | PayU redirects user’s browser to surl/furl with POST body; your page must accept POST and read the same fields.                                                                                              |
| 2 | **List of response fields**                | Show table/list: `status`, `unmappedstatus`, `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `mihpayid`, `mode`, `bank_ref_num`, `error`, `error_Message`, `hash`, etc., and what each means. |
| 3 | **Success vs failure**                     | `status` = success vs failed; show both flows and that failure can still hit surl in some cases (e.g. user closed); so always verify with hash/verify API.                                                   |
| 4 | **Server-side verification**               | Recompute hash from response (same key + salt + field order) and compare with received `hash`; if mismatch, reject.                                                                                          |
| 5 | **Idempotency**                            | Callback can be retried or opened multiple times; use `txnid`/`mihpayid` to avoid double-fulfilment.                                                                                                         |
| 6 | **Troubleshooting “callback not working”** | Checklist: correct surl/furl in request, URL whitelisted if required, server accepts POST, no firewall blocking PayU IPs; suggest testing with ngrok for local.                                              |

***

### 4. Test Setup: Key, Salt, Hash & UAT vs Production

**Target audience:** All developers before first integration.  
**Suggested duration:** 6–8 min.  
**Ticket driver:** 105 Credentials Issues (Key/salt UAT & Prod), “hash not matching”, “test vs live”.

**Important points to highlight in the video:**

| #  | Point                              | Why it matters                                                                                        |       |        |             |           |       |      |      |     |                                     |
| :- | :--------------------------------- | :---------------------------------------------------------------------------------------------------- | :---- | :----- | :---------- | :-------- | :---- | :--- | :--- | :-- | :---------------------------------- |
| 1  | **Where to get test credentials**  | UAT/onboarding signup link; generate test key & salt from dashboard; link to doc.                     |       |        |             |           |       |      |      |     |                                     |
| 2  | **Hash structure and field order** | Exact sequence for payment request hash (e.g. key                                                     | txnid | amount | productinfo | firstname | email | udf1 | udf2 | ... | salt); show one example end-to-end. |
| 3  | **Encoding**                       | UTF-8; no extra spaces; empty optional fields still included in sequence.                             |       |        |             |           |       |      |      |     |                                     |
| 4  | **Switching to production**        | New key/salt from production dashboard; use live payment URL; never use test key/salt in prod.        |       |        |             |           |       |      |      |     |                                     |
| 5  | **Key/salt in Prod (31 tickets)**  | When to rotate (compromise, policy); how to get new key/salt and update integration without downtime. |       |        |             |           |       |      |      |     |                                     |

***

### 5. API Integration Basics – Authentication, Parameters & Responses

**Target audience:** Backend developers doing server-to-server or verify/refund APIs.  
**Suggested duration:** 10–14 min.  
**Ticket driver:** 57 Doc Requirement (API) + API-related Integration issues.

**Important points to highlight in the video:**

| # | Point                                     | Why it matters                                                                                                      |
| - | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 1 | **Salt vs salt-less**                     | When PayU uses salt in request hash vs when it uses other auth (e.g. OAuth); point to doc for each flow.            |
| 2 | **Verify payment API**                    | Why and when to call verify; request (e.g. key, salt, command, var1); response fields and how to map to your order. |
| 3 | **PG fees and tax in response**           | Which response/API fields represent PG fees and PG tax; where they appear (e.g. settlement, reports).               |
| 4 | **VPA validation**                        | If supported, mention `/v3/verify/instrument` (or current API) for UPI VPA validation; link to API reference.       |
| 5 | **Error handling**                        | Common HTTP and business error codes; retry logic and idempotency.                                                  |
| 6 | **Where to find latest integration kits** | Single place (docs/developer portal) for server kits; version and changelog.                                        |

***

## Priority 2 – Webhooks & Plugins

### 6. Webhooks: Events, Payloads & Local Testing

**Target audience:** Developers implementing webhooks (e.g. payment success, mandate, refund).  
**Suggested duration:** 8–10 min.  
**Ticket driver:** 76 Webhook Issues (payloads, “no response”, local dev).

**Important points to highlight in the video:**

| # | Point                                      | Why it matters                                                                                                  |
| - | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------- |
| 1 | **What webhooks are for**                  | Async server-to-server notifications (payment success, failure, mandate, refund, etc.) vs redirect callback.    |
| 2 | **Where to set webhook URL**               | Dashboard vs API; which events need which URL.                                                                  |
| 3 | **List of events and sample payloads**     | At least: payment success/failure, refund, e-mandate; mention e-mandate vs QR payload difference if applicable. |
| 4 | **Security**                               | Verify webhook signature/hash if provided; never trust payload without verification.                            |
| 5 | **Local / dev testing**                    | Webhook URL must be publicly reachable; use ngrok or similar; whitelist if required; show one test flow.        |
| 6 | **Troubleshooting “payload not received”** | URL updated in dashboard, whitelist, HTTPS, server returns 2xx quickly; retries and timeout from PayU side.     |

***

### 7. Plugin Integration – Shopify, WooCommerce, OpenCart

**Target audience:** Merchants using Shopify, WooCommerce, or OpenCart.  
**Suggested duration:** 6–8 min per platform (or one 12–15 min video covering all three).  
**Ticket driver:** 206 Plugin Integration (136 Shopify, 52 WooCommerce, OpenCart).

**Important points to highlight in the video:**

| # | Point                        | Why it matters                                                                                               |
| - | ---------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1 | **Where to get the plugin**  | Official link from docs/developer portal; version compatibility (e.g. WooCommerce 4.x, 8.x; OpenCart 4).     |
| 2 | **Install and activate**     | Step-by-step; where to enter key, salt, and test vs live mode.                                               |
| 3 | **Success and failure URLs** | How plugin sets surl/furl (e.g. order success/cancel page); ensure they are correct and HTTPS in production. |
| 4 | **Webhook (if applicable)**  | For Shopify/WooCommerce, if webhook is used for confirmation, where to configure and test.                   |
| 5 | **Testing**                  | Use test key/salt and test card/UPI; confirm order status updates after success/failure.                     |
| 6 | **Common issues**            | Wrong key/salt, wrong mode (test/live), cache clearing after config change.                                  |

***

## Priority 3 – Subscriptions, Refunds, Payouts & Split

### 8. Subscription Integration – UPI & Card Mandates

**Target audience:** Developers building recurring payments.  
**Suggested duration:** 10–12 min.  
**Ticket driver:** 8 Doc Requirement (Subscription) + SI APIs in Integration issues.

**Important points to highlight in the video:**

| # | Point                              | Why it matters                                                            |
| - | ---------------------------------- | ------------------------------------------------------------------------- |
| 1 | **Subscription flow overview**     | Mandate first, then charge; link to subscription/recurring doc.           |
| 2 | **UPI mandate creation**           | Steps and required parameters; where to find UPI mandate docs and sample. |
| 3 | **eNACH mandate**                  | High-level flow and where eNACH mandate doc lives.                        |
| 4 | **Card SI (standing instruction)** | When to use; one-time auth and subsequent charges.                        |
| 5 | **Webhooks for mandate**           | Which webhook events to handle for mandate success/failure.               |

***

### 9. Refund API – Enablement, Request & UAT

**Target audience:** Backend developers and ops.  
**Suggested duration:** 6–8 min.  
**Ticket driver:** 4 Doc Requirement (Refunds) + Refund APIs in Integration issues.

**Important points to highlight in the video:**

| # | Point                            | Why it matters                                                                                |
| - | -------------------------------- | --------------------------------------------------------------------------------------------- |
| 1 | **How to get refund API access** | Enablement process (dashboard/contact); typical turnaround.                                   |
| 2 | **Refund request**               | Key parameters: payment ref (e.g. mihpayid), amount, reason; idempotency for partial refunds. |
| 3 | **Refund status API**            | How to check status of a refund request.                                                      |
| 4 | **UAT for refunds**              | Test key/salt and test refund flow; no real money in UAT.                                     |

***

### 10. Payouts & Penny Drop API (Overview)

**Target audience:** Developers integrating payouts.  
**Suggested duration:** 8–10 min.  
**Ticket driver:** 5 Doc Requirement (Payouts).

**Important points to highlight in the video:**

| # | Point                       | Why it matters                                                          |
| - | --------------------------- | ----------------------------------------------------------------------- |
| 1 | **Payout product overview** | When to use payouts; link to payouts section.                           |
| 2 | **Send money / payout API** | High-level flow; required params; where to find full API reference.     |
| 3 | **Penny drop API**          | Purpose (account verification); request/response overview; link to doc. |
| 4 | **Testing**                 | UAT/sandbox for payouts if available.                                   |

***

### 11. Split Settlement – Sub-merchant Onboarding & Flow

**Target audience:** Platforms/aggregators.  
**Suggested duration:** 8–10 min.  
**Ticket driver:** 6 Doc Requirement (Split-settlement).

**Important points to highlight in the video:**

| # | Point                               | Why it matters                                            |
| - | ----------------------------------- | --------------------------------------------------------- |
| 1 | **Split settlement flow**           | Parent vs sub-merchant; when money is split.              |
| 2 | **Sub-merchant onboarding via API** | When to use API vs dashboard; link to onboarding API doc. |
| 3 | **Sub-merchant management**         | Create, update, status check; link to API reference.      |
| 4 | **Testing**                         | How to test split in UAT.                                 |

***

## Priority 4 – Mobile & Optional

### 12. Mobile SDK Integration – Android & iOS (Overview)

**Target audience:** Mobile developers.  
**Suggested duration:** 10–12 min.  
**Ticket driver:** 9 Doc Requirement (Mobile) + 147 SDK integration issues.

**Important points to highlight in the video:**

| # | Point                         | Why it matters                                                             |
| - | ----------------------------- | -------------------------------------------------------------------------- |
| 1 | **Where to get SDK and docs** | Android, iOS; link to current SDK doc.                                     |
| 2 | **Basic integration steps**   | Init, start payment, handle callback; post params and dependency versions. |
| 3 | **Test mode**                 | Test key/salt and test cards in SDK.                                       |
| 4 | **Save card / tokenisation**  | High-level flow; link to detailed doc.                                     |
| 5 | **Upgrading SDK**             | Changelog and migration notes; where to check version.                     |

***

### 13. Server-to-Server (S2S) and UPI Collect – When & How

**Target audience:** Backend developers choosing S2S or UPI Collect.  
**Suggested duration:** 8–10 min.  
**Ticket driver:** Payment Flow Issues (S2S, UPI Collect).

**Important points to highlight in the video:**

| # | Point                           | Why it matters                                                                 |
| - | ------------------------------- | ------------------------------------------------------------------------------ |
| 1 | **When to use S2S vs redirect** | Server-to-server for server-initiated flows; redirect for browser flow.        |
| 2 | **S2S request/response**        | Main parameters and response; link to S2S doc.                                 |
| 3 | **UPI Collect**                 | When customer gets “collect request”; typical flow and timing.                 |
| 4 | **Diners / TAVV**               | If TAVV or additional_info is required for Diners, mention it and link to doc. |

***

### 14. Payment Method Restriction (e.g. AMEX-only)

**Target audience:** Merchants with specific payment method requirements.  
**Suggested duration:** 3–5 min.  
**Ticket driver:** Integration issues (AMEX-only, bankcode).

**Important points to highlight in the video:**

| # | Point                     | Why it matters                                                             |
| - | ------------------------- | -------------------------------------------------------------------------- |
| 1 | **Parameters**            | `pg`, `bankcode`, `enforce_paymethod`; show example for cards (e.g. AMEX). |
| 2 | **Behaviour on checkout** | That method is pre-selected or only option.                                |
| 3 | **Limitations**           | Where to find list of supported bank codes and any product limits.         |

***

### 15. Order ID and Reconciliation

**Target audience:** Backend developers and finance/ops.  
**Suggested duration:** 4–6 min.  
**Ticket driver:** “Order ID not in settlement”, reconciliation difficulties.

**Important points to highlight in the video:**

| # | Point                     | Why it matters                                                                                           |
| - | ------------------------- | -------------------------------------------------------------------------------------------------------- |
| 1 | **Passing your order ID** | Use `txnid` and/or `udf1`; ensure unique and consistent.                                                 |
| 2 | **Where it appears**      | Callback response, verify API, dashboard, settlement/report files.                                       |
| 3 | **Reconciliation**        | Match your order ID (udf1/txnid) with PayU txnid/mihpayid in reports; best practice (one mapping table). |

***

## Suggested publishing order

| Order | Video                                               | Rationale                                   |
| ----- | --------------------------------------------------- | ------------------------------------------- |
| 1     | Test Setup: Key, Salt, Hash & UAT vs Production     | Needed for every integration.               |
| 2     | Web Integration Quick Start – Hosted Checkout       | Highest volume (Web + callbacks).           |
| 3     | Callback and Response Handling                      | Directly addresses “callbacks not working”. |
| 4     | Generating Dynamic Payment Links                    | Frequent explicit doc request.              |
| 5     | Webhooks: Events, Payloads & Local Testing          | High confusion and “no response” tickets.   |
| 6     | API Integration Basics                              | Covers API auth, verify, fees, VPA.         |
| 7     | Plugin Integration (Shopify, WooCommerce, OpenCart) | Large plugin ticket volume.                 |
| 8     | Subscription – UPI & Card Mandates                  | Recurring payments demand.                  |
| 9     | Refund API                                          | Common post-go-live need.                   |
| 10    | Mobile SDK Overview                                 | Covers mobile + SDK issues.                 |
| 11    | Payouts & Penny Drop                                | Smaller but clear demand.                   |
| 12    | Split Settlement                                    | Platform/aggregator segment.                |
| 13    | S2S and UPI Collect                                 | Payment flow clarity.                       |
| 14    | Payment Method Restriction                          | Short, high-impact.                         |
| 15    | Order ID and Reconciliation                         | Reduces reconciliation tickets.             |

***

## Quick reference – “Must cover” per video type

* **Every integration video:** Test vs live URL and credentials; where to find docs and support.
* **Every API/backend video:** Auth (key/salt or OAuth), error handling, and link to latest integration kit/API reference.
* **Every callback/webhook video:** Exact fields, verification (hash/signature), and troubleshooting “not receiving”.
* **Every plugin video:** Where to download, version support, and success/failure URL and webhook config.

***

**Document version:** 1.0  
**Based on:** Nov–Dec 2025 integration support tickets (CSV analysis).