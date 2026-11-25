---
title: Bolt [New]
excerpt: >-
  Create the Bolt checkout hash payload and receive the Bolt payment postback.
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
Hash and callback endpoints for Bolt checkout. Generate Hash returns the payload passed to `bolt.launch`. PayU receives the checkout postback on the payment callback route.

***

## Authentication

Generate Hash uses these headers on every call: `Authorization`, `X-PayU-Reseller-UUID`, and `X-PayU-Merchant-ID`.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

The payment callback is a PayU route. The partner does not call it.

***

## Endpoints

<Cards>
  <Card title="Bolt Generate Hash" href="https://docs.payu.in/reference/partner-bolt-generate-hash-api" target="_blank">
    Build the payload that is passed to bolt.launch. txnid, amount, productinfo, firstname, email, phone, surl, and furl are required.
  </Card>
  <Card title="Bolt Payment Callback" href="https://docs.payu.in/reference/partner-bolt-payment-callback-api" target="_blank">
    PayU receives the Bolt checkout postback and returns an empty body.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Generate the hash" icon="fad fa-key-skeleton-left-right">
  Call Bolt Generate Hash with the transaction fields. The response is the payload passed to `bolt.launch`.
</Accordion>

<Accordion title="Open Bolt checkout" icon="fad fa-credit-card">
  Pass that payload to `bolt.launch`. The customer pays on Bolt checkout.
</Accordion>

<Accordion title="Receive the postback" icon="fad fa-hand-point-left">
  PayU receives the checkout postback at the Bolt payment callback and returns an empty body.
</Accordion>
