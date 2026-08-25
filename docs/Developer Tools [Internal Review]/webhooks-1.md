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

The [Verify Payment API](ref:verify-payment-api) lets you check the payment status by polling an API. Webhooks push status to you automatically when events occur.

<Tabs>
  <Tab title="Verify Payment API" icon="📎">
    - To check status at a specific moment
    - You are reconciling historical transactions
    - You did not receive a webhook and need to confirm current state
  </Tab>

  <Tab title="Webhooks" icon="far fa-webhook">
    - Automatic, real-time notifications as events happen
    - Handling thousands of transactions and polling would be inefficient
    - Trigger immediate actions when payment status changes
  </Tab>
</Tabs>

{/* END NEW CONTENT */}

## How PayU Webhooks Work

{/* Sourced from docs/payouts/payouts-integration/payouts-webhooks.md */}

When an event occurs in your PayU account (a payment succeeds, fails, refund processes, or dispute is raised), PayU sends an HTTPS POST request to the webhook URL you have configured.

**Here is an end-to-end flow:**

1. **Setup a webhook** via [PayU Dashboard](https://onboarding.payu.in/)
2. **Select events** you want to receive (payment success, failure, refund, dispute)
3. **An event occurs** (customer's payment succeeds, refund processes, etc.)
4. **PayU sends an HTTPS POST** to your registered URL with event details in the request body
5. **Your server processes the event** and responds with HTTP 200 status code
6. **If your server does not respond** (timeout or non-200 status), PayU retries delivery

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

Your webhook endpoint must:

- Be publicly accessible over HTTPS
- Respond with HTTP 200 within the required time window (see [Set Up & Configure Webhooks](doc:set-up-configure-webhooks))
- Process events asynchronously (return 200 immediately, then handle business logic separately)
- Verify the request is genuinely from PayU (see [Verify Webhook Requests](doc:verify-webhook-requests))

{/* END NEW CONTENT */}

## Available Webhook Events

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
