---
title: PayU India API Reference - v2 APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU API Documentation
  description: >-
    This document is the PayU India API Reference documentation, which provides
    developers with information on how to integrate PayU's payment processing
    capabilities into their applications and websites. It includes a list of
    APIs and instructions on how to use them.
  keywords:
    - PayU APIs
    - ' PayU API documentation'
    - ' PayU API reference'
  robots: index
next:
  description: ''
---
---
title: PayU India API Reference - v2 APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU API Documentation
  description: PayU India API Reference documentation for v2 payment integrations, including authentication, environments, payment APIs, post-payment operations, and supporting utilities.
  keywords:
    - PayU APIs
    - PayU API documentation
    - PayU API reference
    - PayU v2 APIs
  robots: index
next:
  description: ''
---

This reference documents PayU v2 payment APIs. Follow the integration journey in order: prepare access, choose an integration, submit payments, complete post-payment operations, and then use supporting utilities and reference material.

## Getting started

1. [Overview](https://docs.payu.in/v2/reference)
2. [Choose an integration](https://docs.payu.in/v2/reference)
3. [Credentials and environments](https://docs.payu.in/v2/reference)
4. Authentication (`/v2/docs/authentication`)
5. [Testing and test data](https://docs.payu.in/v2/reference)
6. [Go-live checklist](https://docs.payu.in/v2/reference)

> **Link maintenance:** The routes shown in code formatting are the proposed canonical routes. Create the corresponding pages and redirects before converting these route labels into links. The supplied files did not include the target pages, so this implementation does not claim that these routes currently resolve.

## Accept payments

### Hosted Checkout

- Hosted Checkout (`/v2/reference/payments-create-hosted`)

### Merchant-hosted integrations

- Cards (`/v2/reference/payments-create-cards`)
- UPI (`/v2/reference/payments-create-upi`)
- Net Banking (`/v2/reference/payments-create-netbanking`)
- Wallets (`/v2/reference/payments-create-wallet`)
- EMI (`/v2/reference/payments-create-emi`)
- BNPL (`/v2/reference/payments-create-bnpl`)

### Server-to-server flows

- Cards Classic (`/v2/reference/cards-classic`)
- Cards Decoupled Flow (`/v2/reference/cards-decoupled-s2s`)
- Cards Direct Authorisation Flow (`/v2/reference/cards-direct-authorization-s2s`)
- UPI S2S (`/v2/reference/upi-s2s`)

## After the payment

- Verify Payment (`/v2/reference/payments-verify`)
- Webhooks (`/v2/reference/webhooks`)
- Create Refund (`/v2/reference/refunds-create`)
- Get Refund Status (`/v2/reference/refunds-get-status`)

## Cards and tokenisation

- Saved-card REST APIs (`/v2/reference/saved-cards-rest`)
- Get Payment Instrument (`/v2/reference/saved-cards-get-instrument`)
- Save Card (`/v2/reference/saved-cards-create`)
- Delete a Saved Card (`/v2/reference/saved-cards-delete`)
- Get User Cards (`/v2/reference/saved-cards-get-user-cards`)
- Payments with Saved Cards (`/v2/reference/saved-cards-payment`)
- Using Network Tokens (`/v2/reference/saved-cards-network-tokens`)

## Third-party verification

- TPV overview (`/v2/reference/tpv-overview`)
- TPV seamless integration (`/v2/reference/tpv-seamless`)
- NEFT TPV (`/v2/reference/tpv-neft`)
- UPI TPV (`/v2/reference/tpv-upi`)

## Pre-authorisation and capture

- Pre-authorisation: non-seamless (`/v2/reference/preauthorization-nonseamless`)
- Pre-authorisation: seamless (`/v2/reference/preauthorization-seamless`)
- Capture Transaction (`/v2/reference/payments-capture`)

## Utilities

- Validate VPA (`/v2/reference/vpa-validate`)
- Eligible BIN for EMI (`/v2/reference/bin-eligible-emi`)
- Get BIN information (`/v2/reference/bin-get-info`)
- Check domestic card (`/v2/reference/cards-check-domestic`)
- Issuing bank status (`/v2/reference/issuing-bank-get-status`)
- S2S eligible BINs (`/v2/reference/bin-eligible-s2s`)
- Generate UPI intent (`/v2/reference/upi-generate-intent`)
- Get checkout details (`/v2/reference/checkout-get-details`)

## Reference

- API errors and error codes (`/v2/reference/errors`)
- Glossary (`/v2/docs/glossary`)

## Get support

If you encounter an integration issue, visit [PayU Help](https://help.payu.in) and raise a ticket.

> **Migration note:** The canonical slugs in this index follow `/v2/reference/{resource}-{action}` and `/v2/docs/{topic}`. Existing legacy URLs must be redirected to these destinations after the corresponding pages are created and validated. The route labels above are not live-link claims.
