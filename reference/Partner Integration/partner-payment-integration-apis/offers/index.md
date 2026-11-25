---
title: Offers [New]
excerpt: >-
  Fetch the offers available for a merchant, or validate one offer before
  payment.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-fetch-offer-api
      title: Fetch offers API [New]
      type: basic
    - slug: partner-validate-offer-api
      title: Validate offer API [New]
      type: basic
---
Fetch the offers available for a merchant, or validate one offer against the payment and the customer before you collect payment.

***

## Authentication

All Offers APIs use a **Bearer token**.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Send the token on every call as `Authorization: Bearer {access_token}`. `merchant_id`, `reseller_id`, and `hash` are required on both requests.

<Callout icon="📘" theme="info">
  ### **Access token**

  Older partner accounts generate this token with the <Anchor target="_blank" href="https://docs.payu.in/reference/token-generation-flow-for-old-partner-merchants">token generation flow for partner payments</Anchor>.
</Callout>

***

## Endpoints

<Cards>
  <Card title="Fetch Offers" href="https://docs.payu.in/reference/partner-fetch-offer-api" target="_blank">
    Return offers for a merchant. Amount, offer keys, payment id, user token, and SKU details are optional.
  </Card>
  <Card title="Validate Offer" href="https://docs.payu.in/reference/partner-validate-offer-api" target="_blank">
    Check an offer against the payment category and the customer. userToken is required inside userDetail.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Fetch the offers" icon="fad fa-tags">
  Call Fetch Offers with `merchant_id`, `reseller_id`, and `hash`. Add amount, offer keys, or SKU details when you have them.
</Accordion>

<Accordion title="Validate before payment" icon="fad fa-badge-check">
  Call Validate Offer with the payment category and the customer `userToken`. The partner layer forwards the body to the PayU Offers service.
</Accordion>
