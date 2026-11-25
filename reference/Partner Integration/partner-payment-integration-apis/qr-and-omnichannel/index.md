---
title: QR and Omnichannel [New]
excerpt: >-
  Start an omnichannel payment, check its status, or create a dynamic Bharat
  QR or a static QR.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-initiate-payment-api
      title: Initiate payment API [New]
      type: basic
    - slug: partner-transaction-verify-status-api
      title: Verify omnichannel transaction status API [New]
      type: basic
    - slug: partner-dbqr-api
      title: Dynamic Bharat QR API [New]
      type: basic
    - slug: partner-static-qr-api
      title: Static QR API [New]
      type: basic
    - slug: partner-static-qr-callback-api
      title: Static QR callback API [New]
      type: basic
---
Omnichannel and QR endpoints on the partner layer. This section is separate from the <Anchor target="_blank" href="https://docs.payu.in/reference/partner-qr-integration-apis">Partner QR soundbox guide</Anchor>.

***

## Authentication

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Initiate payment, verify status, and dynamic Bharat QR use `X-PayU-Reseller-UUID`, `X-Partner-Token`, and `Authorization`. `X-PayU-Merchant-Key` and `X-PayU-Merchant-ID` are optional on verify status and dynamic Bharat QR. Do not send `X-PayU-Merchant-Key` on initiate payment. The merchant key is `accountId` in the body.

Static QR also requires `X-PayU-Merchant-ID`, `X-Partner-Hash`, and `X-Partner-Request-ID`. `X-Partner-Hash` is the SHA-512 of `merchantId|rawRequestBody|clientSecret`.

<Callout icon="📘" theme="info">
  ### **QR signing**

  For the soundbox OAuth and HMAC pattern, see <Anchor target="_blank" href="https://docs.payu.in/reference/authentication-for-partner-qr-apis">Authentication for Partner QR APIs</Anchor>.
</Callout>

***

## Endpoints

<Cards>
  <Card title="Initiate Payment" href="https://docs.payu.in/reference/partner-initiate-payment-api" target="_blank">
    Start an omnichannel payment. accountId is required. The body is forwarded to Core Payments.
  </Card>
  <Card title="Verify Omnichannel Transaction Status" href="https://docs.payu.in/reference/partner-transaction-verify-status-api" target="_blank">
    Check status for an omnichannel transaction. txnId is forwarded when you send it.
  </Card>
  <Card title="Dynamic Bharat QR" href="https://docs.payu.in/reference/partner-dbqr-api" target="_blank">
    Create a dynamic Bharat QR. The partner layer reads the terminal, expiry, and transaction id when they are present.
  </Card>
  <Card title="Static QR" href="https://docs.payu.in/reference/partner-static-qr-api" target="_blank">
    Create a reusable static QR. merchantVpa is required.
  </Card>
  <Card title="Static QR Callback" href="https://docs.payu.in/reference/partner-static-qr-callback-api" target="_blank">
    PayU receives the static QR payment result. field4 (merchant VPA) and key are required.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Start the payment or the QR" icon="fad fa-qrcode">
  Call Initiate Payment with `accountId`, or create a dynamic Bharat QR or a static QR.
</Accordion>

<Accordion title="Let the customer pay" icon="fad fa-credit-card">
  The customer pays from the omnichannel response or by scanning the QR.
</Accordion>

<Accordion title="Confirm the result" icon="fab fa-searchengin">
  Call Verify Omnichannel Transaction Status, or let PayU post the static QR result to the static QR callback.
</Accordion>
