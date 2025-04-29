---
title: Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU Hosted Checkout Integration
  description: ''
  keywords:
    - PayU Hosted Checkout Integration
    - Integrate PayU Hosted Checkout
    - Steps for PayU Hosted Checkout Integration
    - PayU Hosted Checkout Integration Steps
  robots: index
next:
  description: ''
---
The PayU Hosted Checkout integration involves the following steps:

[1. API Integration Steps](doc:integrate-with-payu-hosted-checkout)

[2. Test Integration](doc:test-integration-payu-hosted-checkout)

[3. Production Checklist](doc:integration-checklist-payu-hosted-checkout)

During the **Collect Payment** (**\_payment**) API integration, refer the [Generate Hash](doc:generate-hash-payu-hosted) for hash generation details.

## Checkout page customization

After you integrate, you can perform the following customization on your Checkout page:

* [Enforce Pay Method or Remove Category](https://docs.payu.in/docs/enforce-pay-method-or-remove-category)
* [Change the Language](https://docs.payu.in/docs/changing-the-language)
* [Enable Pluxee Card on Checkout](https://docs.payu.in/docs/integrate-with-payu-hosted-checkout-sodexo)

## Recommended integrations for PayU Hosted Checkout

* **Offers**: Configure offers for cards on Dashboard and then collect payments with offers. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer) and [Offers](doc:offers-integration) .
* **Pre-authorize Credit Card Transactions**: PayU’s pre-authorization (also card authorization, authorization hold or Auth and Capture) product allows merchants two-step card payments so you can temporarily block some amount of funds when a customer places an order (authorization) and then capture the amount later.. For more information, refer to [Pre-authorize Credit Card Payments](doc:auth-and-capture-pre-authorize-credit-card-payments) .
* **Sodexo Integration**: Accept Sodexo payments by enabling Sodexo integration with PayU Hosted Checkout.  For more information, refer to [Enable Sodexo on Checkout](doc:integrate-with-payu-hosted-checkout-sodexo) .
