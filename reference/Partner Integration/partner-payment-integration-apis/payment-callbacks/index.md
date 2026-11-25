---
title: Payment Callbacks [New]
excerpt: >-
  PayU routes for the hosted-checkout result, the server-to-server payment
  postback, and the refund notification.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-payment-success-api
      title: Payment Success Redirect Callback API [New]
      type: basic
    - slug: partner-payment-failed-api
      title: Payment Failure Redirect Callback API [New]
      type: basic
    - slug: partner-payment-cancelled-api
      title: Payment Cancelled Redirect Callback API [New]
      type: basic
    - slug: partner-payment-callback-api
      title: Payment S2S Callback API [New]
      type: basic
    - slug: partner-refund-callback-api
      title: Partner Refund Callback API [New]
      type: basic
---
These pages are the routes PayU calls with a payment or refund result. Success, failure, and cancelled are hosted-checkout redirects. The S2S page is the server-to-server payment postback. The refund page is the refund notification. The partner does not host these URLs.

***

## Authentication

PayU calls these routes. A partner Bearer token is not sent to them.

| Page | Route | What PayU does |
| :--- | :---- | :------------- |
| Payment Success Redirect Callback | `POST /partner/paymentSuccess` | Receives a successful hosted-checkout result, then sends the customer to `surl`. |
| Payment Failure Redirect Callback | `POST /partner/paymentFailed` | Receives a failed result. `error` and `error_Message` carry the gateway reason. The customer is sent to `furl`. |
| Payment Cancelled Redirect Callback | `POST /partner/paymentCancelled` | Receives the result when the customer cancels. |
| Payment S2S Callback | `POST /partner/paymentCallback` | Accepts the server-to-server postback and returns HTTP 200 with an empty body. |
| Partner Refund Callback | `POST /partner/refundCallback` | Accepts the refund notification as the standard body or the migrated body. |

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

***

## Endpoints

These are the Payment Callback pages.

<Cards>
  <Card title="Payment Success Redirect Callback" href="https://docs.payu.in/reference/partner-payment-success-api" target="_blank">
    POST /partner/paymentSuccess. PayU receives the hosted-checkout result after a successful payment, then sends the customer to surl.
  </Card>
  <Card title="Payment Failure Redirect Callback" href="https://docs.payu.in/reference/partner-payment-failed-api" target="_blank">
    POST /partner/paymentFailed. PayU receives the failed result. error and error_Message carry the gateway reason, then the customer is sent to furl.
  </Card>
  <Card title="Payment Cancelled Redirect Callback" href="https://docs.payu.in/reference/partner-payment-cancelled-api" target="_blank">
    POST /partner/paymentCancelled. PayU receives the hosted-checkout result when the customer cancels.
  </Card>
  <Card title="Payment S2S Callback" href="https://docs.payu.in/reference/partner-payment-callback-api" target="_blank">
    POST /partner/paymentCallback. Server-to-server payment postback. PayU returns HTTP 200 with an empty body after it notifies the partner webhook configured for the reseller.
  </Card>
  <Card title="Partner Refund Callback" href="https://docs.payu.in/reference/partner-refund-callback-api" target="_blank">
    POST /partner/refundCallback. Refund notification. The body can be the standard refund callback or the migrated callback with paymentId, refundId, refundAmount, and refundStatus. No field is required.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Successful hosted checkout" icon="fad fa-circle-check">
  PayU posts the result to Payment Success Redirect Callback, then sends the customer to the `surl` from the payment request.
</Accordion>

<Accordion title="Failed hosted checkout" icon="fad fa-circle-xmark">
  PayU posts the result to Payment Failure Redirect Callback. The page carries `error` and `error_Message`, then the customer is sent to `furl`.
</Accordion>

<Accordion title="Customer cancels" icon="fad fa-ban">
  PayU posts the result to Payment Cancelled Redirect Callback.
</Accordion>

<Accordion title="Server-to-server postback" icon="fad fa-hand-point-left">
  PayU posts the payment result to Payment S2S Callback. The response is HTTP 200 with an empty body. The partner webhook URL is configured for the reseller. It is not this path.
</Accordion>

<Accordion title="Refund notification" icon="fad fa-rotate-left">
  PayU posts the refund result to Partner Refund Callback. Use the standard body or the migrated body. Both are documented on that page.
</Accordion>
