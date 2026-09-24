---
api:
  file: pl-test-oas.yaml
  operationId: CreatePaymentLinkAPI
hidden: false
---
Create a shareable payment link and optionally notify the customer via email, SMS, or WhatsApp.<br /><br />The link type is determined by the combination of parameters sent — there is no separate `type` field.<br /><br />**Required scope:** `create_payment_links`

<Callout icon="📘" theme="info">
  ### **10 supported link types**

  This endpoint supports 10 link types — standard, open-amount, partial payment, SI recurring, eNACH, reminder, multi-WhatsApp, offer/coupon, pre-authorisation, and payout beneficiaries. For a full breakdown and key fields for each, see the [Payment Links API Overview](https://docs.payu.in/v3.0/reference/payment-links-api-overview#use-cases).
</Callout>
