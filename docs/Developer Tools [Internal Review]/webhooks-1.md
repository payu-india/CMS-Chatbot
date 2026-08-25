---
title: Webhooks
deprecated: false
hidden: true
metadata:
  robots: index
---
{/* NEW CONTENT — not from existing docs, needs SME review */}

PayU Webhooks are server-to-server HTTP notifications that PayU sends to your application when payment-related events occur. Instead of continuously checking for status updates, your server receives real-time event notifications as transactions progress through the payment lifecycle.

{/* END NEW CONTENT */}

## When to Use Webhooks

{/* NEW CONTENT — not from existing docs, needs SME review */}

Use webhooks when you want to:

<Accordion title="Webhook Usage" icon="far fa-webhook">
  - **Receive real-time payment status updates** without polling PayU APIs

  - **Handle asynchronous payment flows** where the final status is not immediately available (UPI, Net Banking, pending settlements)

  - **Update order status in your system** when customers complete payments outside your direct request flow

  - **Process refunds, chargebacks, or disputes** as they occur
</Accordion>

### Webhooks vs. Redirect URLs (`surl/furl`)

When a customer completes checkout on PayU's hosted page or returns from their bank's site, PayU redirects them back to your success URL (`surl`) or failure URL (`furl`). These are **browser redirects** that depend on the customer's session.

Webhooks are **server-to-server notifications** sent independently of the customer's browser session. Use **both:**

<Tabs>
  <Tab title="Redirect URLs (surl/furl)" icon="far fa-link">
    Show immediate feedback to customers in their browser
  </Tab>

  <Tab title="Webhooks" icon="far fa-webhook">
    Reliably receive status updates on your server (even if the customer closes their browser before the redirect completes)
  </Tab>
</Tabs>

### Webhooks vs. Verify Payment API

The [Verify Payment API](ref:verify-payment-api) lets you **pull** payment status from PayU on demand. Webhooks **push** status to you automatically when events occur.

**Use Verify Payment API when:**

- You need to check status at a specific moment (user clicks "Check Status")
- You're reconciling historical transactions
- You didn't receive a webhook and need to confirm current state

**Use Webhooks when:**

- You want automatic, real-time notifications as events happen
- You're handling thousands of transactions and polling would be inefficient
- You need to trigger immediate actions when payment status changes

{/* END NEW CONTENT */}

## How PayU Webhooks work

{/* Sourced from docs/payouts/payouts-integration/payouts-webhooks.md */}

When an event occurs in your PayU account (a payment succeeds, fails, refund processes, or dispute is raised), PayU sends an HTTPS POST request to the webhook URL you've configured.

**End-to-end flow:**

1. **You register a webhook endpoint** via [PayU Dashboard](https://onboarding.payu.in/) or API
2. **You select which events** you want to receive (payment success, failure, refund, dispute)
3. **An event occurs** (customer's payment succeeds, refund processes, etc.)
4. **PayU sends an HTTPS POST** to your registered URL with event details in the request body
5. **Your server processes the event** and responds with HTTP 200 status code
6. **If your server doesn't respond** (timeout or non-200 status), PayU retries delivery

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

Your webhook endpoint must:

- Be publicly accessible over HTTPS
- Respond with HTTP 200 within the required time window (see [Set Up & Configure Webhooks](doc:set-up-configure-webhooks))
- Process events asynchronously (return 200 immediately, then handle business logic separately)
- Verify the request is genuinely from PayU (see [Verify Webhook Requests](doc:verify-webhook-requests))

{/* END NEW CONTENT */}

## Available webhook events

{/* Sourced from docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/webhook-events-and-sample-payloads.md */}

PayU sends webhooks for these event types:

| Event Type     | Description                                      |
| -------------- | ------------------------------------------------ |
| **Successful** | Triggered when a payment succeeds                |
| **Failed**     | Triggered when a payment fails                   |
| **Refund**     | Triggered when a refund succeeds or fails        |
| **Dispute**    | Triggered when a chargeback or dispute is raised |

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

For product-specific events, see:

- [Subscription webhook events](doc:webhooks-for-subscription) — Recurring payment lifecycle events
- [Payout webhook events](doc:payouts-webhooks) — Payout transfer and balance events
- [Chargeback webhook events](doc:webhooks-for-chargeback) — Dispute lifecycle events

Complete payload structures and parameter details are in [Webhook Events Reference](doc:webhook-events-and-sample-payloads).

{/* END NEW CONTENT */}

## Next steps

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

**New to webhooks?** Start here:

1. [Set Up & Configure Webhooks](doc:set-up-configure-webhooks) — Register your endpoint and select events
2. [Verify Webhook Requests](doc:verify-webhook-requests) — Secure your endpoint
3. [Handle Webhook Events](doc:handle-webhook-events) — Process events reliably
4. [Test & Troubleshoot Webhooks](doc:test-troubleshoot-webhooks) — Test before going live

**Just need the reference?**

- [Webhook Events Reference](doc:webhook-events-and-sample-payloads) — Complete payload structures and parameters
- [Webhook Configuration API](ref:webhook-configuration-api) — Programmatically manage webhook endpoints

{/* END NEW CONTENT */}

***

**Related:**

- [PayU Dashboard Guide](doc:payu-dashboard) — Overview of dashboard features
- [API Authentication & Security](doc:api-authentication-and-security) — API key and hash validation basics
