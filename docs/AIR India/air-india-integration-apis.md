---
title: Air India Integration APIs
deprecated: false
hidden: true
metadata:
  robots: index
---
Use these APIs to create an order, discover and validate offers, present payment options, initiate a transaction, verify its status, and manage post-payment actions.

## Checkout and offers

1. [Create Order API](./01_Create_Order_API%20%281%29.md) — Creates the checkout order and returns the access token and encrypted order ID required by subsequent checkout APIs.
2. [Fetch Offer (with Order ID) API](./02_Fetch_Offer_With_Order_ID_API_v1.md) — Retrieves offers for an existing order.
3. [Fetch Offer (without Order) API](./03_Fetch_Offer_Without_Order_API_v1.md) — Retrieves offers before order creation using booking and travel context.
4. [Validate Offer API](./04_Validate_Offer_API_v1.md) — Validates a selected offer against the order and payment method.

## Payment

5. [Create Transaction API](./05_Create_Transaction_API_v1.md) — Initiates payment with the selected payment method.
6. [Calculate EMI API](./06_Calculate_EMI_API_v1.md) — Calculates EMI options, installments, and applicable discounts.
7. [Fetch Order Status API](./07_Fetch_Order_Status_API_v1.md) — Retrieves order, payment, and transaction-action status.
8. [Payment Options API](./08_Payment_Options_API_v1.md) — Returns the latest payment methods and configuration for checkout.

## Post-payment

9. [Capture Transaction API](./09_Capture_Transaction_API_v1.md) — Captures a fully or partially authorized transaction.
10. [Cancel Pre-Authorized Transaction API](./10_Cancel_Pre_Authorized_Transaction_API_v1.md) — Cancels an authorization before capture and releases the hold.
11. [Refund Initiation API](./11_Refund_Initiation_API_v1.md) — Initiates full, partial, wallet, or split-settlement refunds.
12. [Refund Status API](./12_Refund_Status_API_v1.md) — Retrieves the current status of one or more refunds.

## Authentication models

- **SHA-512 header authentication:** Create Order, Capture Transaction, Refund Initiation, and Refund Status use the reusable `<HeaderAuthentication />` documentation.
- **Checkout session headers:** Fetch Offer with Order ID, Validate Offer, Create Transaction, Calculate EMI, Fetch Order Status, and Payment Options use the `accessToken`, encrypted `orderId`, and `X-Credential-Username` headers.
- **SHA-256 Digest authentication:** Fetch Offer without Order signs the `Date` and `Digest` headers using HMAC-SHA256.
- **Form hash authentication:** Cancel Pre-Authorized Transaction submits a SHA-512 hash with form parameters.

Use the exact endpoint, authentication method, and parameter requirements documented on each API page.