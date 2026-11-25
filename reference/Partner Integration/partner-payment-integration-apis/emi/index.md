---
title: EMI [New]
excerpt: >-
  Read the EMI amount, the bins that can pay by EMI, or a calculated EMI plan.
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
next:
  description: Explore related information and resources.
  pages:
    - slug: partner-get-emi-amount-api
      title: Get EMI amount API [New]
      type: basic
    - slug: partner-get-eligible-bins-api
      title: Get eligible EMI bins API [New]
      type: basic
    - slug: partner-calculate-emi-api
      title: Calculate EMI API [New]
      type: basic
---
Read EMI pricing and the cards that can pay by EMI. `merchant_id` is required on every call. The other fields depend on the API.

***

## Authentication

All EMI APIs use a **Bearer token**.

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
  <Card title="Get EMI Amount" href="https://docs.payu.in/reference/partner-get-emi-amount-api" target="_blank">
    EMI amount for a merchant and a transaction amount. Bank code and tenure can be sent with the request.
  </Card>
  <Card title="Get Eligible EMI Bins" href="https://docs.payu.in/reference/partner-get-eligible-bins-api" target="_blank">
    Bins that are eligible for EMI. merchant_id, type, and var2 are required.
  </Card>
  <Card title="Calculate EMI" href="https://docs.payu.in/reference/partner-calculate-emi-api" target="_blank">
    Calculate EMI for a merchant. Amount and bank code can be sent with the request.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Check the amount" icon="fad fa-calculator">
  Call Get EMI Amount with `merchant_id` and `amount`. `merchant_id` must be digits.
</Accordion>

<Accordion title="Check the card bins" icon="fad fa-credit-card">
  Call Get Eligible EMI Bins with `merchant_id`, `type`, and `var2`.
</Accordion>

<Accordion title="Calculate a plan" icon="fad fa-list-ol">
  Call Calculate EMI with `merchant_id`. Amount and bank code are forwarded when you send them.
</Accordion>
