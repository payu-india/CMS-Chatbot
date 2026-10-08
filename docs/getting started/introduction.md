---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - checkout integration
    - ' API reference'
    - ' payment gateway API integration'
    - ' payment aggregator API integration'
    - ' payment gateway integration'
    - ' UPI payment integration'
    - ' card payment integration'
    - ' NetBanking integration'
  robots: index
next:
  description: ''
---
---
title: Introduction
deprecated: false
hidden: false
metadata:
  title: PayU payment integration introduction
  description: Understand PayU payment integration options and the resources to use before selecting an integration path.
  keywords:
    - PayU checkout integration
    - PayU API reference
    - payment gateway integration
    - UPI payment integration
    - card payment integration
    - Net Banking integration
  robots: index
next:
  description: ''
---

PayU provides payment workflows for collecting online payments. Your choice of workflow affects the customer checkout experience, the data handled by your systems, and the development effort required for integration.

## What is a payment gateway?

A payment gateway transfers payment information between a customer, a merchant, and the payment service. Depending on the integration, customers can pay using cards, UPI, wallets, EMI, Net Banking, and other supported payment methods.

## Choose an integration path

Before you start, consider:

- Which payment methods you need to accept
- Whether your customers pay on a website, mobile app, or both
- How much control you need over the checkout experience
- Which payment data your system will handle
- Whether you need features such as saved cards, retries, recurring payments, split settlements, or payment links
- The testing, security, and operational requirements of your business

Use [Choose your integration](doc:choose-your-integration) to compare the available approaches. Then use [Choose your payment gateway](doc:choose-your-payment-gateway) to review PayU products and related workflows.

## Why use v2 APIs?

PayU v2 APIs use structured JSON request objects and the v2 authentication format documented in the [PayU v2 Authentication reference](doc:v2-authentication-with-payu-apis). Existing v1 integrations should continue to follow their current documentation; migration is a separate implementation project.

### Authentication

- Use the canonical Authentication reference for the exact request-signature algorithm, required headers, and examples.
- Do not assume that a v1 authentication header or hash can be used with a v2 endpoint.
- Keep merchant credentials on the server side and use sandbox credentials while testing.

### Structured requests

v2 request examples group related data into objects such as:

- `paymentMethod` for payment-method configuration
- `paymentCard` for card-specific data where required
- `order` for order and product information
- `paymentChargeSpecification` for supported pricing or charge information
- `additionalInfo` for endpoint-specific options
- `callBackActions` for payment-flow actions or URLs
- `billingDetails` for customer billing information
- `authorization` for supported authorisation flows

The exact field names, types, required flags, and nesting are endpoint-specific. Use the relevant v2 reference page as the source of truth.

## Security and testing

- Do not place API credentials in browser or mobile-app code.
- Use synthetic or PayU-approved sandbox data in documentation and testing.
- Validate the exact request and response examples against the target sandbox endpoint before releasing an integration.
- Confirm the production environment, endpoint, required headers, and go-live checklist before switching credentials.

## Next steps

1. [Register for a merchant account](doc:register-for-a-merchant-account-on-dashboard)
2. [Check your API key and salt](doc:check-api-key-and-salt)
3. [Choose your integration](doc:choose-your-integration)
4. [Read the PayU v2 API Reference](doc:introduction-api-reference)

## Get support

If you encounter an integration issue, visit [PayU Help](https://help.payu.in) and raise a ticket.
