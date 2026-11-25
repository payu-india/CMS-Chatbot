---
title: Bolt [New]
excerpt: >-
  Generate the Bolt checkout hash payload, and receive the Bolt payment
  postback.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-bolt-generate-hash-api
      title: Bolt generate hash API [New]
      type: basic
    - slug: partner-bolt-payment-callback-api
      title: Bolt payment callback API [New]
      type: basic
---
These two pages cover Bolt checkout on the partner layer. Bolt Generate Hash returns the payload passed to `bolt.launch`. Bolt Payment Callback is the route where PayU receives the checkout postback.

***

## Authentication

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

| Page | Route | What the page uses |
| :--- | :---- | :----------------- |
| Bolt Generate Hash | `POST /partner/bolt/generateHash` | `Authorization`, `X-PayU-Reseller-UUID`, and `X-PayU-Merchant-ID` |
| Bolt Payment Callback | `POST /partner/bolt/paymentCallback` | PayU receives the postback. The response is an empty body. |

Generate Hash requires `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, and `furl`.

***

## Endpoints

These are the Bolt pages.

<Cards>
  <Card title="Bolt Generate Hash" href="https://docs.payu.in/reference/partner-bolt-generate-hash-api" target="_blank">
    POST /partner/bolt/generateHash. Returns the bolt.launch payload, not a status wrapper. The hash is the payment hash: key, txnid, amount, productinfo, firstname, email, udf1 to udf5, then the salt.
  </Card>
  <Card title="Bolt Payment Callback" href="https://docs.payu.in/reference/partner-bolt-payment-callback-api" target="_blank">
    POST /partner/bolt/paymentCallback. PayU receives the same form postback fields as the standard payment callback and returns an empty body.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Generate the hash" icon="fad fa-key-skeleton-left-right">
  Call Bolt Generate Hash with `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, and `furl`. The 200 body is the payload passed to `bolt.launch`.
</Accordion>

<Accordion title="Open Bolt checkout" icon="fad fa-credit-card">
  Pass that payload to `bolt.launch`. This step uses the response from Bolt Generate Hash.
</Accordion>

<Accordion title="Receive the postback" icon="fad fa-hand-point-left">
  PayU receives the checkout result at Bolt Payment Callback and returns an empty body.
</Accordion>
