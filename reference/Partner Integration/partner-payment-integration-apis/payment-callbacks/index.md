---
title: Payment Callbacks [New]
excerpt: >-
  Routes where PayU receives the hosted-checkout result, the server-to-server
  payment postback, and the refund notification.
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
PayU receives the payment or refund result on these routes. The success, failure, and cancelled routes are hosted-checkout redirects. The S2S route is the server-to-server payment postback. The refund route is the refund notification.

<Callout icon="📘" theme="info">
  ### **These are PayU routes**

  The partner does not host these URLs. After a hosted-checkout success or failure, PayU sends the customer to the `surl` or `furl` from the payment request.
</Callout>

***

## Endpoints

<Cards>
  <Card title="Payment Success Redirect Callback" href="https://docs.payu.in/reference/partner-payment-success-api" target="_blank">
    PayU receives a successful hosted-checkout result, then sends the customer to surl.
  </Card>
  <Card title="Payment Failure Redirect Callback" href="https://docs.payu.in/reference/partner-payment-failed-api" target="_blank">
    PayU receives a failed hosted-checkout result, then sends the customer to furl.
  </Card>
  <Card title="Payment Cancelled Redirect Callback" href="https://docs.payu.in/reference/partner-payment-cancelled-api" target="_blank">
    PayU receives the result when the customer cancels on hosted checkout.
  </Card>
  <Card title="Payment S2S Callback" href="https://docs.payu.in/reference/partner-payment-callback-api" target="_blank">
    Server-to-server payment postback. PayU returns an empty HTTP 200.
  </Card>
  <Card title="Partner Refund Callback" href="https://docs.payu.in/reference/partner-refund-callback-api" target="_blank">
    Refund notification. The body can be the standard refund callback or the migrated refund callback.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Customer finishes hosted checkout" icon="fad fa-credit-card">
  PayU posts the result to the success, failure, or cancelled route, then redirects the customer to `surl` or `furl`.
</Accordion>

<Accordion title="Server-to-server payment postback" icon="fad fa-hand-point-left">
  PayU accepts the postback at the payment callback route and returns an empty HTTP 200 after it notifies the partner webhook configured for the reseller.
</Accordion>

<Accordion title="Refund notification" icon="fad fa-rotate-left">
  PayU posts the refund result to the refund callback. The body may be the standard shape or the migrated shape.
</Accordion>
