---
title: APIs used in Integration
deprecated: false
hidden: false
icon: fab fa-apple-pay
metadata:
  title: APIs used in Apple Pay integration
  robots: index
---
The following APIs are used for Apple Pay integration:

### Collect Payment

| Use case → Reference                                                                                                                            | `command` / primary value                             | Description                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------------------- |
| Collect payment using Merchant Hosted Checkout — [Collect Payment API – Apple Pay with Merchant Hosted](ref:_payment-apple-pay-merchant-hosted) | `_payment` with `pg=APPLEPAY` and `bankcode=APPLEPAY` | Processes an Apple Pay payment token using Merchant Hosted Checkout.              |
| Collect payment using PayU Hosted Checkout — [Collect Payment API – Apple Pay with PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)     | Browser form `POST` to `_payment`                     | Redirects customers to PayU Hosted Checkout with Apple Pay as the payment method. |

### Verify Payment

| Use case → Reference                                            | `command` / primary value | Description                                                |
| --------------------------------------------------------------- | ------------------------- | ---------------------------------------------------------- |
| Verify a payment — [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconciles the transaction status with PayU after payment. |

<br />
