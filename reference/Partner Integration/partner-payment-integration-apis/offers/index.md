---
title: Offers [New]
excerpt: >-
  Fetch offers for a merchant, or validate one offer against the payment and
  the customer.
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
These two pages talk to the PayU Offers service. Fetch Offers returns the offers for a merchant. Validate Offer checks one offer against the payment category and the customer.

***

## Authentication

Both pages use a **Bearer token**.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Send `Authorization: Bearer {access_token}` on both calls. Both require `merchant_id`, `reseller_id`, and `hash`. The hash input is `merchant_id` followed by the client secret.

| Page | Route | Required besides the token |
| :--- | :---- | :------------------------- |
| Fetch Offers | `POST /partner/fetchOffer` | `merchant_id`, `reseller_id`, `hash` |
| Validate Offer | `POST /partner/validateOffer` | `merchant_id`, `reseller_id`, `hash`, `paymentDetail.category`, `userDetail.userToken` |

***

## Endpoints

These are the Offers pages.

<Cards>
  <Card title="Fetch Offers" href="https://docs.payu.in/reference/partner-fetch-offer-api" target="_blank">
    POST /partner/fetchOffer. Returns offers for a merchant. amount, offerKeys, paymentId, userToken, and skusDetail are optional. The response is the Offers service JSON.
  </Card>
  <Card title="Validate Offer" href="https://docs.payu.in/reference/partner-validate-offer-api" target="_blank">
    POST /partner/validateOffer. Checks an offer against paymentDetail and userDetail. category and userToken are required inside those objects. The response is the Offers validate JSON.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Fetch the offers" icon="fad fa-tags">
  Call Fetch Offers with `merchant_id`, `reseller_id`, and `hash`. Add amount, offer keys, payment id, user token, or SKU details when you have them.
</Accordion>

<Accordion title="Validate one offer" icon="fad fa-badge-check">
  Call Validate Offer with the same merchant, reseller, and hash, plus `paymentDetail.category` and `userDetail.userToken`.
</Accordion>
