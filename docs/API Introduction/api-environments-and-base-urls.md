---
title: API Environments and Base URLs
excerpt: >-
  Find PayU Test and Production base URLs for Collect Payment, General APIs, v2
  payments, Payouts, Partner, BBPS, and other API families.
deprecated: false
hidden: false
metadata:
  title: PayU API Environments and Base URLs
  description: >-
    Complete map of PayU API environments and base URLs for Test and Production
    across Collect Payment, General APIs, OAuth, Payouts, Partner, BBPS, and
    more.
  keywords:
    - PayU API base URL
    - PayU test environment
    - PayU production URL
    - PayU sandbox
    - test.payu.in
    - secure.payu.in
  robots: index
next:
  description: ''
---
PayU provides separate **Test** and **Production** environments. Most integrations should start in Test with Test key/salt values, then switch host, key, and salt together when you go live.

PayU does **not** use one universal gateway URL for every product. Always use the base URL for the API family you are calling.

## Environment basics

| Environment | Purpose | Credentials |
| :---------- | :------ | :---------- |
| **Test** | Build, Try It playground, and UAT validation | Test merchant key and salt |
| **Production** | Live customer traffic | Production merchant key and salt |

> 🚧 Switch as a set
>
> When moving to Production, update **all** of the following together:
>
> * Base URL / host
> * Merchant key
> * Salt / client secret
> * Any product-specific tokens or partner credentials

## Collect Payment (`_payment`)

| Environment | Base URL |
| :---------- | :------- |
| Test | `https://test.payu.in/_payment` |
| Production | `https://secure.payu.in/_payment` |

Related references:

* [Collect Payment — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Collect Payment — Merchant Hosted Checkout](ref:_payment_merchant_hosted)
* [Collect Payment — S2S](ref:_payment_server_to_server)

## General APIs

| Environment | Base URL |
| :---------- | :------- |
| Test | `https://test.payu.in/merchant/postservice.php?form=2` |
| Production | `https://info.payu.in/merchant/postservice.php?form=2` |

Append `form=2` to receive JSON responses for General APIs. See [REST API Format](doc:rest-api-format).

## v2 Payments

| Environment | Base URL |
| :---------- | :------- |
| Test | `https://apitest.payu.in/v2/payments` |
| Production | `https://api.payu.in/v2/payments` |

## OAuth / Accounts (Payouts and Partner auth)

| Environment | Token host example |
| :---------- | :----------------- |
| Test / UAT | `https://uat-accounts.payu.in/oauth/token` |
| Production | `https://accounts.payu.in/oauth/token` |

Product resource hosts can differ from the token host. Confirm the exact endpoint on the API Reference page for the operation you are calling.

Related:

* [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
* [Get Token API](ref:get_token_api)

## Partner onboarding

| Environment | Host pattern |
| :---------- | :----------- |
| UAT | `uat-partner.payu.in` (and related partner hosts documented per API) |
| Production | `partner.payu.in` (and related partner hosts documented per API) |

Start with [Partner Integration — Authentication](ref:step-00-authentication).

## BBPS

| Environment | Base URL |
| :---------- | :------- |
| Test | `https://bbps-sb.payu.in` |
| Production | Contact your Account Manager for production access |

## Chargeback

| Environment | Host pattern |
| :---------- | :----------- |
| Test / UAT | `chbuat.payu.in` (exact path per API) |
| Production | `bankportal.payu.in` (exact path per API) |

## How to choose the correct base URL

1. Identify the **API family** from [Which API should I use?](doc:which-api-should-i-use).
2. Open the specific operation in [API Reference](ref:introduction-api-reference).
3. Use the environment block on that page (or this consolidated map) for Test vs Production.
4. Keep request auth aligned with that family — hash, OAuth, or HMAC.

## Test limitations

Some APIs and flows are not fully supported in Test or in the API Reference Try It playground. Notable examples include certain refund flows, some UPI S2S flows, selected subscription UPI flows, some Save Cards Model 2 flows, TPV, and parts of Split Settlements and Omnichannel.

See the limitations list on [PayU India API Reference](ref:introduction-api-reference) and use [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) for supported test instruments.

## What to read next

* [API Authentication and Security](doc:api-authentication-and-security)
* [Making Your First API Request](doc:making-your-first-api-request)
* [Testing PayU APIs](doc:testing-payu-apis)
* [REST API Format](doc:rest-api-format)

## Related APIs

* [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
* [Verify Payment API](ref:verify_payment)
* [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)
