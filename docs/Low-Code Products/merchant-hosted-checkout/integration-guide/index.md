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

This section covers everything you need to integrate Merchant Hosted Checkout, from posting the first method to going live.<br />

<Callout icon="📘" theme="info">
  ### **API Reference**

  The APIs used here are listed on [Merchant Hosted Checkout APIs](../merchant-hosted-checkout-apis).
</Callout>

***

## Before You Build (Prerequisites)

Make sure you have:<br />

- A PayU merchant account
- Your test merchant key and salt
- A backend that generates SHA-512
- Publicly reachable HTTPS callback URLs (`surl` and `furl`)
- PCI-DSS SAQ A-EP if you collect card data on your site<br />

If you have not completed a test payment yet, start with the [Quick Start](../quick-start) first.

***

## Integration Steps

<Cards columns="3">
  <Card title="Build the Integration" href="./build-integration" icon="fa-code">
    Shared steps, then one page per method.
  </Card>
  <Card title="Test Your Integration" href="./test-integration" icon="fa-flask">
    Test credentials and scenarios from the Merchant Hosted test page.
  </Card>
  <Card title="Go-Live Checklist" href="./go-live-checklist" icon="fa-list-check">
    Production key, salt, and endpoint.
  </Card>
</Cards>

***

## Next Steps

<Cards columns="3">
  <Card title="Quick Start" href="../quick-start">
    Haven't run a test payment yet? Post one net banking payment first.
  </Card>
  <Card title="Best Practices" href="../best-practices">
    Card data, pre-checks, and callback verification.
  </Card>
  <Card title="Errors and Troubleshooting" href="../errors-and-troubleshooting">
    Hash, callback, and the error values named in the source.
  </Card>
</Cards>
