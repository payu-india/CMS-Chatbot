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
  color="#15C614"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
 />

{/* NEW CONTENT: Umbrella page created to support the Tier 2 Integrate section structure. */}

This section covers everything you need to integrate PayU Hosted Checkout, from building the initial connection to going live in production.

***

## Integration Steps

<Cards columns="3">
  <Card title="Build Integration" href="./build-integration">
    Request parameters, hash generation, HTML form POST, response handling, and verification. Includes multi-language code samples.
  </Card>

  <Card title="Test Integration" href="./test-integration">
    Test credentials, payment scenarios, expected responses, and how to simulate failures before going live.
  </Card>

  <Card title="Go-live Checklist" href="./go-live-checklist">
    Production credentials, security requirements, webhook configuration, and final readiness checks.
  </Card>
</Cards>

***

## Using PayU Hosted Checkout in a mobile app?

If you are integrating PayU Hosted Checkout inside a WebView in your Android, iOS, or Flutter app, refer to [WebView for Mobile Apps](./webview-for-mobile-apps). This covers WebView configuration, UPI intent handling, and platform-specific setup required for mobile use.

<Callout icon="❗️" theme="error">
  ### **NPCI UPI Collect mandate**

  If you are using PayU Hosted Checkout within a WebView, you must handle UPI deeplink URL redirects in your app. See [WebView for Mobile Apps](./webview-for-mobile-apps) for the required implementation.
</Callout>

***

## Before you build

Make sure you have:

- A PayU merchant account
- Your test merchant key and salt (from PayU Dashboard → Developer Settings)
- A backend capable of SHA-512 hash generation
- Publicly reachable HTTPS callback URLs (`surl` and `furl`)

If you haven't completed a test payment yet, start with the [Quick Start](../quick-start) first.

<br />
