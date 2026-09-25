---
title: Payment Links
excerpt: >-
  Create, share, fetch, and manage shareable payment links programmatically
  using PayU's OneAPI platform.
hidden: false
---
The <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">Payment Links</Anchor> APIs let you issue payment requests directly from your backend and deliver them to customers over SMS, email, or WhatsApp. Your customer receives a URL, taps it, and pays the amount.

<Callout icon="📘" theme="info">
  ### **Prefer a No-code Approach?**

  Payment Links can be created and managed entirely from the <Anchor target="_blank" href="https://docs.payu.in/docs/create-a-payment-link">PayU Dashboard</Anchor>. If you would rather skip the integration and get started immediately, see <Anchor target="_blank" href="https://docs.payu.in/docs/payment-links">Payment Links</Anchor>.
</Callout>

***

## Authentication

All Payment Links APIs use **OAuth 2.0 Bearer token** authentication.

| Environment | Base URL                    |
| :---------- | :-------------------------- |
| Test        | `https://uatoneapi.payu.in` |
| Production  | `https://oneapi.payu.in`    |

Each token is scoped to specific operations. You must request the right scope when generating the token, and include the token in every API call as `Authorization: Bearer {access_token}`.

| Scope                  | Required for                                                      |
| :--------------------- | :---------------------------------------------------------------- |
| `create_payment_links` | Create Payment Link                                               |
| `update_payment_links` | Update / Cancel Payment Link                                      |
| `read_payment_links`   | Fetch Payment Link · Fetch All Payment Links · Share Payment Link |

<Callout icon="📘" theme="info">
  ### **Mutiple Scopes**:&#x20;

  A single token can carry up to three scopes simultaneously. Pass scopes space-separated:<br />`scope=create_payment_links update_payment_links read_payment_links`
</Callout>

***

## Endpoints

### Authentication

<Cards>
  <Card title="Get Access Token" href="ref:get-token-api-for-payment-links">
    `POST /oauth/token`

    Generate a Bearer token with one or more Payment Links scopes. Required before calling any other endpoint.
  </Card>

  <Card title="Revoke Token API" href="ref:revoke-token-api-payment-links">
    `POST /oauth/revoke`

    Invalidate an existing access token before its natural expiry.
  </Card>
</Cards>

### Create & Share

<Cards>
  <Card title="Create Payment Link" href="ref:create-payment-links">
    `POST /payment-links`

    Generate a new shareable payment link. Supports one-time, partial-payment, open-amount, recurring (SI), and eNACH links.
  </Card>

  <Card title="Share Payment Link" href="ref:share_payment_link_api">
    `POST /payment-links/{invoiceNumber}/notify`

    Send an existing payment link to a customer via SMS, email, or WhatsApp.
  </Card>
</Cards>

### Fetch

<Cards>
  <Card title="Fetch All Payment Links" href="ref:get-all-payment-links-api">
    `GET /payment-links`

    List all payment links for a date range. Supports pagination, sorting, and filtering by status (`active`, `inactive`, `expired`).
  </Card>

  <Card title="Fetch Payment Link" href="ref:get-single-payment-link">
    `GET /payment-links/{invoiceNumber}`

    Retrieve the full details and current status of a specific payment link by its invoice number.
  </Card>

  <Card title="Get Transaction Details" href="ref:get-transaction-details-api">
    `GET /payment-links/{invoiceNumber}/transactions`

    Fetch the payment history for a specific link — including all attempts, their status, and transaction IDs.
  </Card>
</Cards>

### Manage

<Cards>
  <Card title="Update / Cancel Payment Link" href="ref:change-status-of-a-payment-link-api">
    `PUT /payment-links/{invoiceNumber}`

    Update a link's amount, expiry date, partial payment settings, or UDF fields. Set `active: false` to cancel/deactivate a link.
  </Card>
</Cards>

***

## How It Works

A typical payment links integration flow looks like this:

1. **Generate a token** — Call `/oauth/token` with your `client_id`, `client_secret`, and the scopes you need.
2. **Create the link** — Call `POST /payment-links` with the amount, description, customer details, and delivery preferences (`viaEmail`, `viaSms`, `viaWhatsapp`).
3. **Share the link** — Either pass delivery flags at creation time, or call `/notify` later to send the link on-demand.
4. **Receive payment notification** — PayU sends a webhook to your server when the customer pays. Always verify payment server-side.
5. **Fetch status** — Call `GET /payment-links/{invoiceNumber}` or `GET /payment-links/{invoiceNumber}/transactions` to reconcile payment state in your system.

***

## Webhooks

When a customer completes or attempts payment via a link, PayU dispatches a webhook to the endpoint configured in your PayU Dashboard.

| Event             | Triggered when                                      |
| :---------------- | :-------------------------------------------------- |
| `payment_success` | Customer completes payment via the link             |
| `payment_failure` | Payment attempt fails (bank decline, timeout, drop) |
| `payment_pending` | Payment initiated but awaiting bank confirmation    |

<Callout icon="📘" theme="info">
  ### Webhooks

  For the full webhook payload, signature verification, and retry policy, see [Payment Events](doc:webhook-events-and-sample-payloads).
</Callout>
