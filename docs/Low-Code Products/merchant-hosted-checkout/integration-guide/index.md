---
title: Integration Guide
excerpt: >-
  Build, test, and go live with Merchant Hosted Checkout.
deprecated: false
hidden: false
next:
  pages: []
metadata:
  title: Integrate Merchant Hosted Checkout
  description: >-
    Integration guide for PayU Merchant Hosted Checkout: build each payment
    method, test in sandbox, and complete the go-live checklist.
  keywords:
    - integrate payu merchant hosted checkout
    - payu custom checkout build test go live
  robots: index
---
<Banner
  isInline={true}
  message="Integration effort: Developer required"
  color="#FFC107"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

This section covers everything you need to integrate <Anchor target="_blank" href="https://docs.payu.in/docs/merchant-hosted-checkout">Merchant Hosted Checkout</Anchor>, from posting the first payment method to going live.<br />

<Callout icon="📘" theme="info">
  ### **API Reference**

  You can integrate Merchant Hosted Checkout using APIs. Refer to the [Merchant Hosted Checkout APIs](../merchant-hosted-checkout-apis) page for more information.
</Callout>

***

## Using Merchant Hosted Checkout in a Mobile App?

Merchant Hosted Checkout posts the payment from the customer's browser. This guide does not include a WebView setup. For a native Android, iOS, React Native, or Flutter app, use the [Mobile SDKs](https://docs.payu.in/docs/mobile-sdk-integration).<br />

<Callout icon="❗️" theme="error">
  ### **NPCI UPI Collect mandate:**

  UPI Collect is allowed only for MCC 6012 and 6211. On the web and on Android, use UPI Intent S2S. A seamless form POST does not support UPI Intent. iOS may keep a deeplink and UPI Collect. See [UPI Collect](./build-integration/upi-collect).
</Callout>

<Callout icon="💡" theme="info">
  ### **Exploring Other PayU Solutions?**

  PayU offers other ways to collect a payment, depending on how much of the checkout you want to build:

  - **No code needed**: [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) — collect a payment by sharing a link
  - **PayU hosts the payment page**: [PayU Hosted Checkout](https://docs.payu.in/docs/payu-hosted-checkout-1) — the customer chooses the method on a PayU page
  - **Mobile apps**: [Mobile SDKs](https://docs.payu.in/docs/mobile-sdk-integration) — native SDKs for Android, iOS, React Native, and Flutter
  - **eCommerce platforms**: [eCommerce Plugins](https://docs.payu.in/docs/ecommerce-platform-plugins) — plugins for WooCommerce, Shopify, and Magento
</Callout>

***

## Before You Build (Prerequisites)

Make sure you have:<br />

- A PayU merchant account
- Your test merchant key and salt
- A backend capable of SHA-512 hash generation
- Publicly reachable HTTPS callback URLs (`surl` and `furl`)
- PCI-DSS SAQ A-EP if you collect card data on your site<br />

If you haven't completed a test payment yet, start with the [Quick Start](../quick-start) first.

***

## Integration Steps

<MerchantHostedCheckoutStepsHoverCards />

***

## Next Steps

<Cards columns="3">
  <Card title="Quick Start" href="../quick-start">
    Haven't run a test payment yet? Walk through a net banking test payment before you build each method.
  </Card>
  <Card title="Best Practices" href="../best-practices">
    Card data handling, transaction IDs, and what to do when the callback does not arrive.
  </Card>
  <Card title="Errors & Troubleshooting" href="../errors-and-troubleshooting">
    Diagnose and fix hash errors, callback failures, and the bank decline named in the source.
  </Card>
</Cards>
