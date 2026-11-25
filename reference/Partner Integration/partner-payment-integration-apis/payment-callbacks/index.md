---
title: Payment Callbacks [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
PayU receives the payment or refund result on these routes. The success, failure, and cancelled routes are hosted-checkout redirects. The S2S route is the server-to-server payment postback. The refund route is the refund notification.

* [Payment Success Redirect Callback API](ref:partner-payment-success-api) — PayU receives a successful hosted-checkout result, then sends the customer to `surl`.
* [Payment Failure Redirect Callback API](ref:partner-payment-failed-api) — PayU receives a failed hosted-checkout result, then sends the customer to `furl`.
* [Payment Cancelled Redirect Callback API](ref:partner-payment-cancelled-api) — PayU receives the result when the customer cancels on hosted checkout.
* [Payment S2S Callback API](ref:partner-payment-callback-api) — Server-to-server payment postback. PayU returns an empty HTTP 200.
* [Partner Refund Callback API](ref:partner-refund-callback-api) — Refund notification. The body can be the standard refund callback or the migrated refund callback.
