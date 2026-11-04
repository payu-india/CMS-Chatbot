---
title: PayU Hosted Checkout APIs
excerpt: >-
  API reference index for PayU Hosted Checkout: collect payment, verify
  transaction, check EMI eligibility, and webhook events.
deprecated: false
hidden: true
metadata:
  title: PayU Hosted Checkout APIs
  description: >-
    Complete API reference for PayU Hosted Checkout: Collect Payment API, Verify
    Payment API, Get Checkout Details, EMI eligibility APIs, and webhook events.
  keywords:
    - payu hosted checkout api reference
    - payu _payment api collect payment endpoint
    - payu verify payment api india
    - payu emi eligibility bin api
    - payu get checkout details api
    - payu webhook events hosted checkout
    - payu hosted checkout api list
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: payu-hosted-checkout-1
      title: PayU Hosted Checkout
      type: basic
    - slug: payu-hosted-checkout-workflow
      title: How PayU Hosted Checkout Works
      type: basic
    - slug: payu-hosted-checkout-quick-start
      title: Quick Start
      type: basic
    - slug: integrate-payu-hosted-checkout
      title: Integrate PayU Hosted Checkout
      type: basic
    - slug: customise-payu-hosted-checkout
      title: Customise PayU Hosted Checkout
      type: basic
    - slug: payu-hosted-checkout-webview-integration
      title: PayU Hosted Checkout WebView Integration
      type: basic
    - slug: payu-hosted-checkout-best-practices
      title: Best Practices
      type: basic
    - slug: payu-hosted-errors-troubleshooting
      title: Errors and Troubleshooting
      type: basic
    - slug: payu-hosted-checkout-faqs
      title: FAQs (Frequently Asked Questions)
      type: basic
---
These are the APIs used in a complete PayU Hosted Checkout integration.

***

## Collect Payment

| API                                                                                                                                             | Description                                                                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| <Anchor target="_blank" href="https://docs.payu.in/reference/_payment_payu_hosted_checkout">Collect Payment API - PayU Hosted Checkout</Anchor> | POST payment request to the PayU-hosted payment page. Customers complete payment and are redirected back via `surl` / `furl`. |

***

## Verify Payment

| API                                                                                                          | Description                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| <Anchor target="_blank" href="https://docs.payu.in/reference/verify_payment_api">Verify Payment API</Anchor> | Poll from your server to confirm the transaction status after payment. Use when you need programmatic confirmation beyond the browser callback. |
