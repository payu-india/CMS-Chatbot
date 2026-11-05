---
title: Air India Integration APIs
deprecated: false
hidden: true
metadata:
  robots: index
---
# Air India API Reference

Use these APIs to create an order, discover and validate offers, present payment options, initiate a transaction, verify its status, and manage post-payment actions.

## Checkout and offers

1. [Create Order API](https://docs.payu.in/docs/v1-create-order-api) — Creates the checkout order and returns the access token and encrypted order ID required by subsequent checkout APIs.
2. [Fetch Offer with Order ID API](https://docs.payu.in/docs/fetch-offer-with-order-id-api) — Retrieves offers for an existing order.
3. [Fetch Offer API](https://docs.payu.in/docs/fetch-offer-api) — Retrieves offers before order creation using booking and travel context.
4. [Validate Offer API](https://docs.payu.in/docs/validate-offer-api-airindia) — Validates a selected offer against the order and payment method.

## Payment

5. [Create Transaction API](https://docs.payu.in/docs/create-transaction-api) — Initiates payment with the selected payment method.
6. [Calculate EMI API](https://docs.payu.in/docs/calculate-emi-api) — Calculates EMI options, installments, and applicable discounts.
7. [Fetch Order Status API](https://docs.payu.in/docs/fetch-order-status-api) — Retrieves order, payment, and transaction-action status.
8. [Payment Options API](https://docs.payu.in/docs/payment-options-api) — Returns the latest payment methods and configuration for checkout.

## Post-payment

9. [Capture Transaction API](https://docs.payu.in/docs/capture-transaction-api) — Captures a fully or partially authorized transaction.
10. [Cancel Pre-Authorized Transaction API](https://docs.payu.in/docs/cancel-pre-authorized-transaction-api) — Cancels an authorization before capture and releases the hold.
11. [Refund Initiation API](https://docs.payu.in/docs/refund-initiation-api) — Initiates full, partial, wallet, or split-settlement refunds.
12. [Refund Status API](./12_Refund_Status_API_v1.md) — Retrieves the current status of one or more refunds.

## Typical API sequence

1. Create the order.
2. Fetch and validate an offer, if applicable.
3. Retrieve payment options or calculate EMI details.
4. Create the transaction.
5. Fetch the order status until the final payment state is available.
6. Capture or cancel a pre-authorized transaction.
7. Initiate a refund and track its status, when required.

## Authentication models

- **SHA-512 header authentication:** Create Order, Capture Transaction, Refund Initiation, and Refund Status use the reusable `<HeaderAuthentication />` documentation.
- **Checkout session headers:** Fetch Offer with Order ID, Validate Offer, Create Transaction, Calculate EMI, Fetch Order Status, and Payment Options use the `accessToken`, encrypted `orderId`, and `X-Credential-Username` headers.
- **SHA-256 Digest authentication:** Fetch Offer without Order signs the `Date` and `Digest` headers using HMAC-SHA256.
- **Form hash authentication:** Cancel Pre-Authorized Transaction submits a SHA-512 hash with form parameters.

Use the exact endpoint, authentication method, and parameter requirements documented on each API page.
