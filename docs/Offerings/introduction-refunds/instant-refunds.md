---
title: Instant Refunds
deprecated: false
hidden: false
icon: fab fa-cash-app
metadata:
  robots: index
---
## What are Instant Refunds?

Instant Refunds allow merchants to refund eligible customer payments near-instantly instead of waiting for the standard refund processing cycle. This helps businesses provide faster resolution when an order is cancelled, a service is not delivered, a booking is modified, or a partial refund is required.

PayU supports merchant-initiated refunds through the **PayU Dashboard** or the **Refund Transaction API**, and refund requests are validated before being processed to the customer’s original payment source.

If Instant Refunds are enabled for a merchant, eligible refunds can be completed within **1 minute&#x20;**&#x6F;f the refund request.

 

## Key Features and Benefits

### 1. Faster Customer Refund Experience

Instant Refunds help merchants improve customer satisfaction by reducing the time customers wait for refund credit.

- **Refunds within seconds**: Eligible refunds can be completed within 1 minute of the refund request.
- **Back-to-source refunds**: Refunds are sent back to the source account used by the customer for the original payment.
- **Improved customer trust**: Faster refunds can reduce anxiety for customers after cancellations, returns, or failed service delivery.

 

### 2. Full and Partial Refund Support

Merchants can refund either the full transaction amount or a partial amount depending on the business scenario.

- **Full refund**: Use this when the complete order or service is cancelled.
- **Partial refund**: Use this when only part of the order is cancelled, returned, or adjusted.

### 3. Dashboard and API Based Refund Initiation

Instant Refunds can fit both operational and automated workflows.

- **Dashboard workflow**: Merchants can initiate refunds from the PayU Merchant Dashboard by navigating transaction details.
- **API workflow**: Merchants can use the Refund Transaction API, cancel_refund_transaction, to initiate full or partial refunds for captured transactions.
- **Status tracking**: Merchants can track refund progress using refund status APIs, webhooks, or the dashboard.

## Industry Applications

Instant Refunds can benefit businesses where speed and customer confidence are important.

### E-commerce

Merchants can provide faster refunds for order cancellations, partial returns, item unavailability, or failed delivery scenarios. PayU highlights e-commerce as a relevant use case where timely refunds can help increase repeat transactions.

### Travel and Hospitality

Travel platforms can refund booking amounts quickly when a hotel, flight, cab, or experience booking is cancelled or modified. PayU highlights travel and hospitality as a use case for instantly refunding booking amounts.

### Hyperlocal Businesses

Hyperlocal businesses can use Instant Refunds to build trust when services are cancelled, inventory is unavailable, or delivery cannot be completed. PayU identifies hyperlocal businesses as a use case for enabling faster refunds.

### Events

Event platforms can issue full or partial refunds within minutes when events are cancelled, rescheduled, or partially fulfilled. PayU highlights events as a use case for partial or full refunds within minutes. 

## How Instant Refunds Work

The typical refund journey follows these steps:

- **Customer requests a refund**<br /> The refund may be triggered by a cancellation, return, failed service, or order issue.
- **Merchant initiates the refund**<br /> The merchant initiates the refund using the PayU Dashboard or Refund Transaction API.
- **PayU validates the refund request**<br /> PayU validates the transaction, refund rules, and refund amount before processing.
- **Instant Refund is processed to the supported payment source**<br /> Instant Refunds are routed back to the customer’s original payment source.
- **Merchant tracks refund status**<br /> Merchants can monitor refund status through dashboard.

### Instant Refund Prerequisites

To use **Instant Refunds**, please ensure the following conditions are met:

- **Instant Refunds must be enabled** on your merchant account.
- **Instant Refunds are currently supported by PayU only for select payment methods.** Refunds initiated on unsupported payment methods will be processed through the standard refund flow.
- The original transaction must **meet the eligibility criteria** for Instant Refund processing.

<Callout icon="📘" theme="info">
  ### **Note:**&#x20;

  Eligibility may vary based on the payment method, transaction status, and other risk or compliance checks.
</Callout>

## Getting Started with Instant Refunds

### Request Instant Refund Activation via KAM or DIY flow from Dashboard.

Once Instant Refunds are enabled, Merchants can initiate Instant refunds using either:

- **PayU Dashboard** for manual or operations-led refund workflows.
- **Refund Transaction API** for automated refund workflows.
