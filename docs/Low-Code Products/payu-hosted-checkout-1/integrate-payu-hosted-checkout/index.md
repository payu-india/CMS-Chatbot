---
title: Integrate PayU Hosted Checkout
excerpt: >-
  Build, test, and go live with PayU Hosted Checkout. Full technical guide for
  web and mobile app integration.
deprecated: false
hidden: true
metadata:
  title: Integrate PayU Hosted Checkout
  description: >-
    Complete integration guide for PayU Hosted Checkout: build your integration,
    test transactions, and follow the go-live checklist for production.
  keywords:
    - integrate payu hosted checkout
    - payu hosted checkout integration guide india
    - payu checkout developer setup steps
    - payu payment integration website
    - payu hosted checkout build test go live
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
---
<Banner
  isInline={true}
  message="Integration effort: Minimal technical setup required"
  color="#FFC107"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

{/* NEW CONTENT: Umbrella page created to support the Tier 2 Integrate section structure. */}

This section covers everything you need to integrate <Anchor target="_blank" href="https://docs.payu.in/docs/payu-hosted-checkout-1">PayU Hosted Checkout</Anchor>, from building the initial connection to going live in production.<br />

<Callout icon="📘" theme="info">
  ### **API Reference**

  You can integrate PayU Hosted Chekcout using APIs. Refer to the PayU Hosted Checkout API page for more information.
</Callout>

***

## Using PayU Hosted Checkout in a Mobile App?

If you are integrating PayU Hosted Checkout inside a WebView in your Android, iOS, or Flutter app, refer to [WebView for Mobile Apps](./webview-for-mobile-apps). This covers WebView configuration, UPI intent handling, and platform-specific setup required for mobile use.<br />

<Callout icon="❗️" theme="error">
  ### **NPCI UPI Collect mandate:**

  &#x20;If you are using PayU Hosted Checkout within a WebView, you must handle UPI deeplink URL redirects in your app. See [WebView for Mobile Apps](./webview-for-mobile-apps) for the required implementation.
</Callout>

<Callout icon="💡" theme="info">
  ### **Exploring Other PayU Solutions?**

  PayU offers multiple integration paths depending on how much control and setup you need:

  - **No code needed**: [Payment Links](../../../introduction-no-code-payments-integration/payment-links-dashboard) — collect payments by sharing a link, no website or code required
  - **Custom checkout UI**: [Merchant Hosted Checkout](../../../custom-checkout-merchant-hosted) — full control over the payment page design and branding
  - **Mobile apps**: [Mobile SDKs](../../../mobile-sdks) — native SDKs for Android, iOS, React Native, and Flutter
  - **eCommerce platforms**: [eCommerce Plugins](../../../ecommerce-platform-plugins) — ready-made plugins for WooCommerce, Shopify, and Magento
</Callout>

***

## Before You Build (Prerequisites)

Make sure you have:<br />

- A PayU merchant account
- Your test merchant key and salt (from PayU Dashboard → Developer Settings)
- A backend capable of SHA-512 hash generation
- Publicly reachable HTTPS callback URLs (`surl` and `furl`)<br />

If you haven't completed a test payment yet, start with the [Quick Start](../quick-start) first.

***

## Integration Steps

<HostedCheckoutStepsHoverCards />

***

## Next Steps

<Cards columns="3">
  <Card title="Quick Start" href="../payu-hosted-checkout-apis">
    Haven't run a test payment yet? Walk through all five integration steps in the sandbox before you build.
  </Card>

  <Card title="Customise Checkout" href="../customise-payu-hosted-checkout">
    Configure payment methods, branding, language, and advanced display options on the PayU checkout page.
  </Card>

  <Card title="Errors & Troubleshooting" href="../errors-and-troubleshooting">
    Diagnose and fix common integration issues — hash errors, callback failures, and payment declines.
  </Card>
</Cards>
