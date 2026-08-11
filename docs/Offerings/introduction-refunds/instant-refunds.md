---
title: Instant Refunds
deprecated: false
hidden: true
icon: fab fa-cash-app
metadata:
  robots: index
---
---
title: Instant Refunds
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Instant Refunds
  description: >-
    Learn how PayU Instant Refunds return eligible customer payments near-instantly
    through the PayU Dashboard or Refund Transaction API.
  keywords:
    - PayU Instant Refunds
    - Instant Refund
    - Refund Transaction API
    - cancel_refund_transaction
  robots: index
next:
  description: ''
---
Instant Refunds allow merchants to refund eligible customer payments near-instantly instead of waiting for the standard refund processing cycle. Use them when an order is cancelled, a service is not delivered, a booking is modified, or a partial refund is required.

PayU supports merchant-initiated refunds through the [PayU Dashboard](doc:refunds-dashboard) or the [Refund Transaction API](ref:refund_transaction_api) (`cancel_refund_transaction`). Refund requests are validated before funds are returned to the customer’s original payment source.

If Instant Refunds are enabled for your merchant account, eligible refunds can be completed within **5 minutes** of the refund request.

## Overview

Instant Refunds accelerate the standard refund journey for supported payment methods. Unsupported methods continue on the standard refund flow (typically 5–21 days). For supported channels and alternate refund modes, refer to [Partner Refunds](doc:partner-refunds).

<Callout icon="👍" theme="okay">
  ### Before you begin

  Instant Refunds must be enabled on your merchant account. Contact your PayU Key Account Manager (KAM) to request activation, or enable Instant Refunds from the PayU Dashboard when the DIY option is available for your account. For merchant registration, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Benefits for your customers

- **Faster credit**: Eligible refunds can complete within 5 minutes of the refund request.
- **Back-to-source refunds**: Funds return to the account used for the original payment.
- **Clearer post-purchase experience**: Faster resolution after cancellations, returns, or failed service delivery.

## Benefits for your business

- **Full and partial refunds**: Refund the full transaction amount or a partial amount.
- **Dashboard and API initiation**: Run operations-led refunds from the dashboard or automate with the Refund Transaction API.
- **Status tracking**: Monitor progress from the dashboard, refund status APIs, or [webhooks](doc:webhooks-for-refunds).

## Industry applications

### E-commerce

Issue faster refunds for cancellations, partial returns, item unavailability, or failed delivery.

### Travel and hospitality

Refund booking amounts quickly when a hotel, flight, cab, or experience booking is cancelled or modified.

### Hyperlocal businesses

Rebuild trust when services are cancelled, inventory is unavailable, or delivery cannot be completed.

### Events

Issue full or partial refunds when events are cancelled, rescheduled, or partially fulfilled.

## How Instant Refunds work

1. **Customer requests a refund**: Triggered by a cancellation, return, failed service, or order issue.
2. **Merchant initiates the refund**: Use the [PayU Dashboard](doc:refunds-dashboard) or [Refund Transaction API](ref:refund_transaction_api).
3. **PayU validates the refund request**: PayU checks the transaction, refund rules, and refund amount.
4. **Instant Refund is processed**: Eligible refunds are routed back to the customer’s original payment source on a supported channel.
5. **Merchant tracks refund status**: Monitor progress from the dashboard, [Refund APIs](doc:refund-apis-doc), or [Webhooks for Refunds](doc:webhooks-for-refunds).

### Prerequisites

- Instant Refunds are enabled on your merchant account.
- The payment method is supported for Instant Refunds. Unsupported methods use the standard refund flow. See [Partner Refunds](doc:partner-refunds) for supported channels.
- The original transaction meets Instant Refund eligibility criteria.

<Callout icon="📘" theme="info">
  ### Note

  Eligibility may vary based on the payment method, transaction status, and risk or compliance checks.
</Callout>

## Getting started with Instant Refunds

1. **Activate Instant Refunds** — Contact your PayU Key Account Manager (KAM), or use the DIY enablement option in the PayU Dashboard when available for your account.
2. **Initiate a refund** — After enablement:
   - **Dashboard**: Initiate full or partial refunds from transaction details. For more information, refer to [Refunds Dashboard](doc:refunds-dashboard).
   - **API**: Call the [Refund Transaction API](ref:refund_transaction_api) (`cancel_refund_transaction`) for automated full or partial refunds on captured transactions. For the API list, refer to [Refund APIs](doc:refund-apis-doc).
3. **Track status** — Use the dashboard, [Check Refund Status APIs](doc:refund-apis-doc), or [Webhooks for Refunds](doc:webhooks-for-refunds).

If your account already uses PayU refunds, Instant Refunds usually need only activation—not a separate integration. For channel-level enablement and alternate refund modes, refer to [Partner Refunds](doc:partner-refunds).

## Related documentation

| Resource | Description |
| -------- | ----------- |
| [Partner Refunds](doc:partner-refunds) | Supported payment channels, merchant- and transaction-level enablement, and alternate refund modes |
| [Refunds Dashboard](doc:refunds-dashboard) | Initiate and track refunds from the PayU Merchant Dashboard |
| [Refund APIs](doc:refund-apis-doc) | Refund initiation and status APIs |
| [Refund Transaction API](ref:refund_transaction_api) | `cancel_refund_transaction` reference |
| [Webhooks for Refunds](doc:webhooks-for-refunds) | Refund status callbacks |
| [Refunds](doc:introduction-refunds) | Refunds overview and standard turnaround times |

<br />