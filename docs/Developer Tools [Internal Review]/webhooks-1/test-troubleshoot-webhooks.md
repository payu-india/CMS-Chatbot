---
title: Test and Troubleshoot Webhooks
excerpt: >-
  Inspect delivery history, test your endpoint locally, and diagnose why
  webhooks are failing or not arriving.
deprecated: false
hidden: true
metadata:
  title: Test and Troubleshoot Webhooks
  description: >-
    How to test your PayU webhook endpoint, inspect delivery logs, diagnose
    non-delivery and verification failures, and debug common issues across
    payment, payout, and dispute webhooks.
  robots: index
---
{/*
=============================================================================
CONTENT PROVENANCE — for SME / editorial review
=============================================================================
Every section below is tagged with one of:

  SOURCE      — drawn directly from an existing repo file (file path shown).
                Content was reorganised or lightly rewritten for tone/clarity
                but the facts are as documented.

  SYNTHESISED — compiled from two or more existing pages (listed).
                No new facts invented; wording is new.

  NEW CONTENT — does not exist in any repo file.
                Must be validated by a PayU SME before publishing.
                Also marked inline with the <!-- NEW CONTENT */}

comment.

\=============================================================================
\-->

{/* NEW CONTENT — page-scope framing. No equivalent intro exists in the repo.
     Needs SME review. */}

Test your endpoint before it receives real events, inspect what PayU sent and why delivery failed, and diagnose the most common failure modes. For signature verification specifically, see [Verify Webhook Requests](doc:verify-webhook-requests). For the event catalog and payload field reference, see Webhook Events and Payloads.

***

## Test Your Endpoint Before Going Live

{/* SYNTHESISED — tools and approach synthesised from:
     docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/webhook-alerts.md (ngrok, webhook.site, Postman, curl test approach)
     docs/Payment Gateway/introduction-web/webhooks.md (test webhook request from support)
     docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/webhook-events-and-sample-payloads.md (Transaction Callback API callout)
     ngrok / webhook.site are mentioned explicitly in the OverWatch page; applicability to payment webhooks is editorial. */}

### Expose a local endpoint with a tunnel

If your handler runs on a local development machine, PayU cannot reach it directly. Use a tunnelling tool to create a temporary public HTTPS URL that forwards to your localhost port.

{/* SOURCE — tools and URLs sourced from:
     docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/webhook-alerts.md
     (ngrok explicitly listed with https://ngrok.com; webhook.site listed as alternative) */}

**ngrok** ([https://ngrok.com](https://ngrok.com)) is the most common choice:

```bash
# Expose local port 3000 over HTTPS
ngrok http 3000
```

This gives you a public URL like `https://abc123.ngrok.io` — use that as your webhook URL in the PayU Dashboard while developing. Once your endpoint is deployed to a stable server, update the URL.

<Callout icon="📘" theme="info">
  ### **HTTPS is required.** PayU only delivers to HTTPS endpoints. ngrok provides a valid TLS certificate automatically; a self-hosted tunnel must present a valid certificate from a trusted CA.
</Callout>

**webhook.site** ([https://webhook.site](https://webhook.site)) provides a ready-made public URL you can inspect in a browser — useful for quickly checking what PayU actually sends without writing any handler code first.

***

### Trigger a test delivery

{/* SOURCE — "request a test webhook from PayU support" sourced from:
     docs/Payment Gateway/introduction-web/webhooks.md ("Testing Your webhook" section, step 3)

     "Transaction Callback API" sourced from:
     docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/webhook-events-and-sample-payloads.md
     (inline callout: "You can view the webhook logs... Transaction Callback API")

     NEW CONTENT — the note about no self-serve "Send test event" button is editorial
     but reflects the confirmed absence of such a feature in all repo pages.
     Needs SME confirmation. */}

PayU does not currently have a self-serve "Send test event" button in the Dashboard. Your options for triggering a test delivery are:

1. **Complete a test transaction.** With your endpoint registered in the Dashboard and your application running in test mode, make a payment using [test credentials and test cards](doc:test-cards-and-credentials). PayU will fire a webhook to your registered URL on completion, the same as a live payment.

2. **Use the Transaction Callback API.** The Transaction Callback API returns the webhook payload for a given transaction ID. This is useful for replaying or inspecting the payload for a specific transaction without making a new one. See the [Transaction Callback API reference](ref:transaction-callback-api).

3. **Request a test webhook from PayU Support.** For payment webhooks, PayU Support can send a test delivery to your registered endpoint on request. Contact your integration team or raise a support ticket.

***

### Validate your endpoint responds correctly

{/* SOURCE — response requirements per product sourced from:
     docs/Payment Gateway/introduction-web/webhooks.md: "200 OK; retries 3 times"
     docs/payouts/payouts-integration/payouts-webhooks.md: "200 within 10 seconds; retried max 2 more times"
     docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/webhook-alerts.md: "5 seconds; retried immediate, +1m, +5m, +15m"

     NEW CONTENT — the curl snippet for simulating a form-encoded payment webhook locally is new.
     The content-type facts (form-encoded for payments, JSON for refund/dispute) are sourced from:
     docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/webhook-events-and-sample-payloads.md */}

Before registering your endpoint with PayU, verify manually that it:

- Returns HTTP `200 OK` (not `201`, `204`, or a redirect) for a valid delivery
- Returns `200 OK` within the timeout for the webhook family you are integrating:

{/* SOURCE — timeout/retry table: three source files listed above */}

| Webhook family              | Must respond within                                         | PayU retries on non-200 or timeout      |
| --------------------------- | ----------------------------------------------------------- | --------------------------------------- |
| Payment / Refund            | Not explicitly documented — design for well under 5 seconds | Up to **3 retries**                     |
| Payouts                     | **10 seconds**                                              | **2 more attempts** after the first     |
| OverWatch monitoring alerts | **5 seconds**                                               | Immediate, then +1 min, +5 min, +15 min |

<Callout icon="🚧" theme="warn">
  ### **Payment webhook timeout is not documented.** The payment webhook page states PayU retries up to 3 times but does not specify the timeout window per attempt. Design your handler to respond in well under 5 seconds and confirm the exact SLA with PayU if it is business-critical. See also [Handle Webhook Events — Acknowledge fast](doc:handle-webhook-events#acknowledge-fast-process-reliably).
</Callout>

You can simulate a form-encoded payment webhook delivery locally with curl to confirm your endpoint accepts the right content type:

{/* NEW CONTENT — curl test snippet for simulating payment webhook POST.
     Content-type sourced from webhook-events-and-sample-payloads.md;
     field names from sample payloads in same file. Snippet is new.
     Needs SME review of field names and values. */}

```bash
# Simulate a payment webhook POST to your local handler
curl -X POST http://localhost:3000/webhooks/payu \
  -H "Content-Type: application/x-www-form-urlencoded" \
  --data-urlencode "mihpayid=403993715529929" \
  --data-urlencode "status=success" \
  --data-urlencode "txnid=your-txn-id-here" \
  --data-urlencode "amount=100.00" \
  --data-urlencode "key=your-test-key" \
  --data-urlencode "hash=placeholder"
```

<Callout icon="📘" theme="info">
  ### Refund and dispute webhooks are delivered as JSON (`application/json`), not form-encoded. Make sure your handler parses both content types if you subscribe to multiple event types.
</Callout>

***

## Inspect delivery history in Webhook Logs

{/* SOURCE — content sourced from:
     docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/using-webhook-logs.md
     (hidden: true — content reproduced here; recommend publishing the source page or
     keeping this as the canonical reference and deprecating the hidden page)

     The inline callout "You can view webhook logs by navigating to Dashboard → Developers → Webhook logs"
     is also sourced from webhook-events-and-sample-payloads.md. */}

The PayU Dashboard records every webhook delivery attempt. To access the log:

1. Log in to the [PayU Dashboard](https://merchant.payu.in/).
2. Select **Developer** from the left menu.
3. Open the **Webhook Logs** tab.

Each log entry shows:

| Column        | What it tells you                                                       |
| ------------- | ----------------------------------------------------------------------- |
| Timestamp     | When PayU attempted delivery                                            |
| Webhook URL   | The endpoint PayU sent to                                               |
| Event Type    | The event that triggered the delivery (e.g., Payment Successful)        |
| Status        | Whether delivery was acknowledged (Success / Failed)                    |
| Response Code | The HTTP status code your endpoint returned (e.g., `200`, `500`, `405`) |

Click any log entry to see the full event payload PayU sent and the `webhook_delivery_message` — the raw HTTP response line your endpoint returned (e.g., `"HTTP/2 405 "`). This is the fastest way to confirm exactly what PayU received in return.

**Filters available:** Date range, Customer Name, Customer Email, Phone Number.

{/* NEW CONTENT — "what to look for" guidance. The source page lists columns but
     does not explain how to interpret them for debugging. This interpretation is new.
     Needs SME review. */}

<Callout icon="📘" theme="info">
  ### **What to look for when debugging**

  - **Response Code&#x20;**`405` — your endpoint doesn't accept `POST` requests on that path. Check your routing.
  - **Response Code&#x20;**`500` — your handler threw an unhandled exception before returning. Check your application logs for the stack trace.
  - **Response Code&#x20;**`200`**&#x20;but event not processed** — your handler acknowledged but your business logic failed silently. Add explicit logging inside the handler before the `200` return.
  - **No entry in the log at all** — PayU never attempted delivery. Check that the correct webhook URL is registered for the event type in Developer → Webhooks.
</Callout>

***

## Delivery is failing — common causes

{/* SOURCE — common failure causes sourced from:
     docs/Monitoring & Alerts/payu-monitoring-alerts-overwatch/webhook-alerts.md
     ("Common Issues & Solutions" accordion — non-200, timeout, network/firewall, URL format, TLS cert)
     Scoped to OverWatch in the source, but causes apply to all webhook types.
     NEW CONTENT marker applied to any item not confirmed for payment webhooks specifically. */}

### Your endpoint is returning a non-200 status

PayU treats any response other than `200 OK` as a failure. This includes `201 Created`, `204 No Content`, `301`/`302` redirects, and any `4xx` or `5xx` error. Check the Response Code column in Webhook Logs and fix the handler to return exactly `200 OK`.

### Your endpoint is timing out

If your handler performs slow work (database writes, downstream API calls, sending email) synchronously before returning, it may exceed the acknowledgment window and PayU will mark the delivery as failed — even if your handler eventually succeeds. Move slow work off the request path: acknowledge with `200 OK` immediately, then process asynchronously. See [Handle Webhook Events — Acknowledge fast](doc:handle-webhook-events#acknowledge-fast-process-reliably).

### Network or firewall is blocking PayU's delivery

{/* SOURCE — IP whitelist for debugging sourced from:
     docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/webhook-events-and-sample-payloads.md
     docs/Payment Gateway/introduction-web/webhooks.md
     docs/payouts/payouts-integration/payouts-webhooks.md */}

If your endpoint is not publicly reachable or sits behind a firewall that doesn't allow PayU's IPs, deliveries will fail silently from PayU's side (connection refused or no response). Allow inbound traffic from PayU's webhook delivery IPs:

{/* SOURCE — IP addresses sourced from webhook-events-and-sample-payloads.md (payment)
     and payouts-webhooks.md (payouts). Listed separately per product as the IPs differ. */}

**Payment webhooks — Production:**

| Data Centre | IP addresses                                                                                      |
| ----------- | ------------------------------------------------------------------------------------------------- |
| DC          | 3.7.89.1, 3.7.89.2, 3.7.89.3                                                                      |
| DR          | 52.140.8.88, 52.140.8.89, 52.140.8.64                                                             |
| Additional  | 180.179.174.2, 180.179.165.250, 3.6.73.183, 3.6.83.44, 3.7.89.8, 3.7.89.9, 3.7.89.10, 52.140.8.65 |

**Payment webhooks — Test:**

180.179.174.1, 3.6.73.183, 3.6.83.44

**Payout webhooks — Production:**

180.179.168.225, 13.71.57.148, 52.140.8.68, 180.179.174.1

**Payout webhooks — Test:**

180.179.165.250, 13.71.57.148, 13.235.110.253

<Callout icon="🚧" theme="warn">
  ### **IP allowlisting is a hardening measure, not the primary authentication mechanism.** Always verify the webhook signature or reverse hash before trusting the payload, regardless of source IP. See [Verify Webhook Requests](doc:verify-webhook-requests).
</Callout>

### Webhook URL is wrong or not registered for this event type

{/* SOURCE — dashboard config sourced from create-a-new-webhook.md */}

Check that:

1. The correct URL is registered in Dashboard → Developer → Webhooks.
2. The URL is registered for the specific event type you expect (Successful Payment, Failed Payment, Refund, Dispute are configured separately).
3. The URL is an HTTPS endpoint — PayU does not deliver to plain HTTP.

### TLS certificate is not trusted

{/* SOURCE — HTTPS + valid cert requirement sourced from webhook-alerts.md */}

If your endpoint uses a self-signed certificate or a certificate from an untrusted CA, PayU's delivery will fail at the TLS handshake. Use a certificate from a trusted CA (Let's Encrypt is free and widely supported).

### The payload content type is not what your handler expects

{/* SOURCE — content type facts sourced from webhook-events-and-sample-payloads.md */}

Payment webhooks are delivered as `application/x-www-form-urlencoded`. Refund and dispute webhooks are delivered as `application/json`. If your framework's body parser is configured for JSON only, it will silently ignore or reject payment webhook payloads — check that your handler explicitly parses form-encoded bodies for payment events.

***

## Webhooks aren't arriving at all

{/* NEW CONTENT — diagnostic flow. The repo does not have a single "webhook not arriving" diagnostic guide.
     Steps reference confirmed facts from the repo. Needs SME review. */}

Work through this in order:

1. **Check Webhook Logs** (Dashboard → Developer → Webhook Logs). If there is no entry for the expected event, PayU either did not attempt delivery or the event did not fire.

2. **Confirm the event fired.** Use the [Transaction Callback API](ref:transaction-callback-api) to retrieve the webhook payload for the transaction ID. If the API returns a payload, PayU has data for that transaction — the issue is delivery, not the event itself.

3. **Confirm your URL is registered for that event type.** A URL registered for Payment Successful will not receive Payment Failed events. Check each event type independently in the Dashboard.

4. **Check for&#x20;**`callback_on_failure`**.** Payment webhooks for pending/failed transactions are only sent if the `callback_on_failure` flag is enabled on your account. This flag is off by default and must be activated by the PayU support team. If you are not receiving failure-state webhooks, contact PayU Support to verify this flag.

{/* SOURCE — callback_on_failure sourced from:
     docs/Payment Gateway/introduction-web/webhooks.md */}

5. **Confirm your endpoint is reachable.** Test with curl from a machine outside your network, or use webhook.site as a temporary replacement URL to confirm PayU can reach the endpoint at all.

6. **Check that all retries are exhausted.** If delivery failed on the first attempt, PayU retries automatically. Allow time for retries to complete before concluding the webhook is lost. After all retries are exhausted, the delivery is flagged as timed out in Webhook Logs with no further attempts.

***

## Verification is failing — quick reference

{/* NEW CONTENT — cross-link summary. The actual verification debugging content lives in
     Verify Webhook Requests. This section is a quick redirect with the most common causes
     summarised to save a developer from loading the full verification page mid-debug.
     Needs SME review of cause list. */}

If your verification check is failing (hash mismatch, signature invalid), the most common causes are:

- **Wrong Salt.** You are verifying with Test Salt but the webhook came from a Production payment (or vice versa). Check that your handler loads the correct Salt for the environment.
- **Body was mutated before verification.** Some frameworks (e.g., Express with `bodyParser`) re-encode the body on parse. Verify against the raw request body, not the parsed object.
- **Wrong field order.** The reverse-hash formula requires fields in an exact order. A single missing or transposed field produces a different hash. See [Verify Webhook Requests](doc:verify-webhook-requests) for the exact formula.
- **Dispute signature not enabled.** Dispute webhook signatures are not enabled by default. If `X-PayU-Dispute-Webhook-Signature-V2` is absent from the headers, signing has not been activated on your account — contact your KAM or PayU Support.

For the full verification procedure and code samples, see [Verify Webhook Requests](doc:verify-webhook-requests).

***

## Still stuck?

{/* NEW CONTENT — escalation path. The repo mentions contacting support in several places
     but does not have a single consolidated "escalation path" section. Needs SME review. */}

- **PayU Support:** [https://help.payu.in/knowledge-center](https://help.payu.in/knowledge-center)
- **Integration queries:** [integration@payu.in](mailto:integration@payu.in)
- **Account-specific issues:** Contact your PayU Key Account Manager

When contacting support about a webhook delivery issue, include: the transaction ID (`txnid`), the PayU payment ID (`mihpayid`), the timestamp of the expected delivery, and the Response Code shown in Webhook Logs (if any).
