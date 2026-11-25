---
title: Payment Links [New]
excerpt: >-
  Read a partner payment link, start payment on it, and verify the transaction.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-payment-link-metadata-api
      title: Payment link metadata API [New]
      type: basic
    - slug: partner-payment-link-payment-api
      title: Payment link payment API [New]
      type: basic
    - slug: partner-payment-link-verify-payment-api
      title: Verify payment link transaction API [New]
      type: basic
---
Read a payment link, collect payment on it, and verify the result. These pages are the partner-layer payment link APIs. They are separate from the WhatsApp payment link guides.

***

## Authentication

All Payment Link APIs use a **Bearer token**.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Send the token on every call as `Authorization: Bearer {access_token}`.

<Callout icon="📘" theme="info">
  ### **Access token**

  Older partner accounts generate this token with the <Anchor target="_blank" href="https://docs.payu.in/reference/token-generation-flow-for-old-partner-merchants">token generation flow for partner payments</Anchor>.
</Callout>

***

## Endpoints

<Cards>
  <Card title="Payment Link Metadata" href="https://docs.payu.in/reference/partner-payment-link-metadata-api" target="_blank">
    Amount, currency, description, status, and expiry for a payment link. Pass the link in the payment_link query parameter.
  </Card>
  <Card title="Payment Link Payment" href="https://docs.payu.in/reference/partner-payment-link-payment-api" target="_blank">
    Start payment with payment_link_id and the customer phone number. redirect_url is optional.
  </Card>
  <Card title="Verify Payment Link Transaction" href="https://docs.payu.in/reference/partner-payment-link-verify-payment-api" target="_blank">
    Payment status for order_ref_id and payment_link_id. Both query parameters are required.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Read the link" icon="fad fa-link">
  Call Payment Link Metadata with the `payment_link` query parameter. The response includes amount, currency, description, status, and expiry.
</Accordion>

<Accordion title="Start payment" icon="fad fa-credit-card">
  Call Payment Link Payment with `payment_link_id` and `phone_number`. The phone number is 5 to 16 digits.
</Accordion>

<Accordion title="Verify the transaction" icon="fab fa-searchengin">
  Call Verify Payment Link Transaction with `order_ref_id` and `payment_link_id`.
</Accordion>
