---
title: Environments and Base URLs
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU provides separate **Test** and **Production** environments for you to test and then go-live. We recommend you to test your integration first with test key and salt values, then switch host, key, and salt together when you go-live.

PayU uses different gateway URLs for different product. Always use the base URL for the API family you are calling.

## Environment Basics

| Environment    | Purpose                                     | Required Credentials    |
| :------------- | :------------------------------------------ | :---------------------- |
| **Test**       | Build and test the PayU product integration | Test key and salt       |
| **Production** | Go-live with PayU products after testing    | Production key and salt |

<Callout icon="🚧" theme="warn">
  ### Switch as a Set

  When moving to Production, update **all** of the following together:

  - [x] Base URL / host
  - [x] Merchant key
  - [x] Salt / client secret
  - [x] Any product-specific tokens or partner credentials
</Callout>

## Product-wise Base URLs

These are the product-wise base URLs

<Accordion title="Collect Payment (_payment)" icon="far fa-money-bill-trend-up">
  | Environment | Base URL                          |
  | :---------- | :-------------------------------- |
  | Test        | `https://test.payu.in/_payment`   |
  | Production  | `https://secure.payu.in/_payment` |
</Accordion>

<Accordion title="General APIs" icon="far fa-gear-complex-api">
  | Environment | Base URL                                               |
  | :---------- | :----------------------------------------------------- |
  | Test        | `https://test.payu.in/merchant/postservice.php?form=2` |
  | Production  | `https://info.payu.in/merchant/postservice.php?form=2` |

  Append `form=2` to receive JSON responses for General APIs. Refer to the [REST API Format](doc:rest-api-format) page for more information.
</Accordion>

<Accordion title="V2 Payments" icon="far fa-code">
  | Environment | Base URL                              |
  | :---------- | :------------------------------------ |
  | Test        | `https://apitest.payu.in/v2/payments` |
  | Production  | `https://api.payu.in/v2/payments`     |
</Accordion>

<Accordion title="OAuth/Accounts (Payouts and Partner authentication)" icon="far fa-space-station-moon-construction">
  | Environment    | Base URL                                   |
  | :------------- | :----------------------------------------- |
  | **Test**       | `https://uat-accounts.payu.in/oauth/token` |
  | **Production** | `https://accounts.payu.in/oauth/token`     |
</Accordion>

<Accordion title="Partner Onboarding" icon="far fa-up-right-and-down-left-from-center">
  | Environment | Base URL                                                             |
  | :---------- | :------------------------------------------------------------------- |
  | UAT         | `uat-partner.payu.in` (and related partner hosts documented per API) |
  | Production  | `partner.payu.in` (and related partner hosts documented per API)     |
</Accordion>

<Accordion title="BBPS" icon="far fa-boxes-packing">
  | Environment | Base URL                                           |
  | :---------- | :------------------------------------------------- |
  | Test        | `https://bbps-sb.payu.in`                          |
  | Production  | Contact your Account Manager for production access |
</Accordion>

<Accordion title="Chargeback" icon="far fa-display-chart-up-circle-dollar">
  | Environment | Base URL                                  |
  | :---------- | :---------------------------------------- |
  | Test / UAT  | `chbuat.payu.in` (exact path per API)     |
  | Production  | `bankportal.payu.in` (exact path per API) |
</Accordion>

## How to Choose the Correct Base URL

To choose the correct base URL:

1. Identify the **API family** from Choose Your API.
2. Open the specific operation in [API Reference](ref:introduction-api-reference).
3. Use the environment block on that page (or this consolidated map) for Test vs Production.
4. Keep the request auth aligned with that family.

## Test limitations

Some products, APIs, and flows are not fully supported for test journey. Notable examples include certain refund flows, some UPI S2S flows, selected subscription UPI flows, some Save Cards Model 2 flows, TPV, and parts of Split Settlements and Omnichannel.<br />

See the limitations list on [PayU India API Reference](ref:introduction-api-reference) and use [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets) for supported test instruments.