---
title: Integration APIs for Payment Links
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The following APIs are used to create or update the status/expiry of payment links:

* [Create Payment Link API](ref:create-payment-links)
* [Share Payment Link API](ref:share_payment_link_api)
* [Get Single Payment Link API](ref:get-single-payment-link)
* [Get All Payment Links API](ref:get-all-payment-links-api)

> 📘 Note:
>
> All the above APIs must be used with a bearer token that must be generated using the <Anchor label="Get Token API" target="_blank" href="https://docs.payu.in/reference/generate-token-using-private-client-id">Get Token API</Anchor>, where the scope must be specified as indicated.  The [Revoke Token API](ref:revoke-token-api-payment-links)must be used to revoke or cancel the token.
