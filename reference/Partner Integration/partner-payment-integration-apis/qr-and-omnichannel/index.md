---
title: QR and Omnichannel [New]
excerpt: >-
  Initiate an omnichannel payment, verify it, create a dynamic Bharat QR, or
  create and receive a static QR.
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
These five pages cover omnichannel payment and QR on the partner layer. Initiate Payment starts the payment. Verify Omnichannel Transaction Status checks it. Dynamic Bharat QR creates a dynamic QR. Static QR creates a reusable QR for a merchant VPA, and Static QR Callback is the result PayU receives for that QR.

***

## Authentication

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

| Page | Route | Headers |
| :--- | :---- | :------ |
| Initiate Payment | `POST /partner/initiatePayment` | `X-PayU-Reseller-UUID`, `X-Partner-Token`, `Authorization`. Body field `accountId` is required. |
| Verify Omnichannel Transaction Status | `POST /partner/transaction/verifyStatus` | `X-PayU-Reseller-UUID`, `X-Partner-Token`, `Authorization`. `X-PayU-Merchant-Key` and `X-PayU-Merchant-ID` are optional. |
| Dynamic Bharat QR | `POST /partner/dbqr` | Same headers as Verify Omnichannel Transaction Status. |
| Static QR | `POST /partner/staticQr` | `X-PayU-Reseller-UUID`, `X-PayU-Merchant-ID`, `X-Partner-Token`, `X-Partner-Hash`, `X-Partner-Request-ID`. |
| Static QR Callback | `POST /partner/staticQrCallback` | PayU calls this route. `field4` (merchant VPA) and `key` are required on the post. |

`X-Partner-Hash` on Static QR is the SHA-512 of `merchantId|rawRequestBody|clientSecret`.

***

## Endpoints

These are the QR and Omnichannel pages.

<Cards>
  <Card title="Initiate Payment" href="https://docs.payu.in/reference/partner-initiate-payment-api" target="_blank">
    POST /partner/initiatePayment. Requires accountId, a merchant key or a numeric merchant id. txnId, amount, and callBackActions are read when sent. The body is forwarded to Core Payments POST /v2/payments.
  </Card>
  <Card title="Verify Omnichannel Transaction Status" href="https://docs.payu.in/reference/partner-transaction-verify-status-api" target="_blank">
    POST /partner/transaction/verifyStatus. Forwards the body, including txnId when you send it, to the Bharat QR status command.
  </Card>
  <Card title="Dynamic Bharat QR" href="https://docs.payu.in/reference/partner-dbqr-api" target="_blank">
    POST /partner/dbqr. Reads vendorTransactionId, soundBoxTerminalId, expiryTime, and mihpayId when they are sent. The body is forwarded to POST /v1/partner/qr/dbqr.
  </Card>
  <Card title="Static QR" href="https://docs.payu.in/reference/partner-static-qr-api" target="_blank">
    POST /partner/staticQr. Requires merchantVpa. Creates a reusable static QR. A cached success returns qrString, qrId, and merchantVpa.
  </Card>
  <Card title="Static QR Callback" href="https://docs.payu.in/reference/partner-static-qr-callback-api" target="_blank">
    POST /partner/staticQrCallback. PayU receives the static QR result. field4 (merchant VPA) and key are required. txnid is used to detect a duplicate.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Start an omnichannel payment" icon="fad fa-credit-card">
  Call Initiate Payment with `accountId`. The page reads `txnId`, `amount`, and `callBackActions` when you send them.
</Accordion>

<Accordion title="Check that payment" icon="fab fa-searchengin">
  Call Verify Omnichannel Transaction Status. `txnId` is forwarded with the rest of the body.
</Accordion>

<Accordion title="Create a dynamic Bharat QR" icon="fad fa-qrcode">
  Call Dynamic Bharat QR. The page reads `vendorTransactionId`, `soundBoxTerminalId`, `expiryTime`, and `mihpayId` when they are present.
</Accordion>

<Accordion title="Create a static QR and receive the result" icon="fad fa-hand-point-left">
  Call Static QR with `merchantVpa` and `X-Partner-Hash`. PayU later posts the payment result to Static QR Callback, which requires `field4` and `key`.
</Accordion>
