---
title: APIs used in Offers Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Offers Integration
  robots: index
---
The following APIs are used for Offers integration on PayU:

### Offer APIs

| Use case → Reference                                      | `command` / primary value | Description                                                                                             |
| --------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------- |
| [Payment Transaction ](ref:_payment_payu_hosted_checkout) | `POST /_payment`          | Process a payment transaction with offers applied through PayU Hosted Checkout.                         |
| [Fetch Offers API](ref:fetch-offers-api)                  | `fetch_offers`            | Fetch all active offers for a specific Merchant ID, with optional discount calculation based on amount. |
| [Validate Offer API](ref:validate-offer-api)              | `validate_offer`          | Validate a payment request against an offer key without applying the offer.                             |
| [Check Offer Status API](ref:check-offer-status-api)      | `check_offer_status`      | Check merchant-specific or card-specific offers to retrieve offer status and details.                   |

<Callout icon="📘" theme="info">
  **Note**: The Fetch Offers API returns discount calculations when the amount is included in the request. Without the amount parameter, the response excludes discount calculation fields.
</Callout>

<Callout icon="👍" theme="okay">
  For detailed integration guides on using the **\_payment** API with offers, refer to:

  - [Integrate with PayU Hosted Checkout](https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers)
  - Integrate with Merchant Hosted Checkout
    - [Instant Discount or Cashback using Merchant Hosted Checkout](https://docs.payu.in/docs/instant-discount-or-cashback-offers-integration-using-merchant-hosted-checkout)
    - [SKU-Based Offer using Merchant Hosted Checkout](https://docs.payu.in/docs/sku-based-offer-using-merchant-hosted-checkout)
</Callout>
