---
title: EMI [New]
excerpt: >-
  Get an EMI amount, the bins eligible for EMI, or a calculated EMI plan.
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
These three pages answer an EMI question for a merchant. Get EMI Amount returns the EMI for an amount. Get Eligible EMI Bins returns the bins that can pay by EMI. Calculate EMI calculates a plan for that merchant.

***

## Authentication

All three pages use a **Bearer token**.

| Environment | Base URL |
| :---------- | :------- |
| Test        | `https://test-partnerapilayer.payu.in/apilayer` |
| Production  | `https://api.payu.in` |

Send `Authorization: Bearer {access_token}` on every call. `merchant_id` is required on all three pages.

| Page | Route | Required body |
| :--- | :---- | :------------ |
| Get EMI Amount | `POST /partner/getEmiAmount` | `merchant_id` (digits), `amount` |
| Get Eligible EMI Bins | `POST /partner/getEligibleBins` | `merchant_id`, `type`, `var2` |
| Calculate EMI | `POST /partner/calculateEmi` | `merchant_id` (digits) |

***

## Endpoints

These are the EMI pages.

<Cards>
  <Card title="Get EMI Amount" href="https://docs.payu.in/reference/partner-get-emi-amount-api" target="_blank">
    POST /partner/getEmiAmount. EMI for a merchant and an amount. bankcode and tenure can be sent with the request. The request is forwarded to the EMI-as-per-interest service.
  </Card>
  <Card title="Get Eligible EMI Bins" href="https://docs.payu.in/reference/partner-get-eligible-bins-api" target="_blank">
    POST /partner/getEligibleBins. Bins eligible for EMI. Requires merchant_id, type, and var2. The request is forwarded to the eligible-bins service.
  </Card>
  <Card title="Calculate EMI" href="https://docs.payu.in/reference/partner-calculate-emi-api" target="_blank">
    POST /partner/calculateEmi. Calculates EMI for a merchant. amount and bankcode can be sent with the request. reseller_id is not forwarded.
  </Card>
</Cards>

***

## How It Works

<Accordion title="Get the EMI amount" icon="fad fa-calculator">
  Call Get EMI Amount with `merchant_id` and `amount`. Add `bankcode` and `tenure` when you want them included.
</Accordion>

<Accordion title="Check eligible bins" icon="fad fa-credit-card">
  Call Get Eligible EMI Bins with `merchant_id`, `type`, and `var2`.
</Accordion>

<Accordion title="Calculate a plan" icon="fad fa-list-ol">
  Call Calculate EMI with `merchant_id`. Add `amount` and `bankcode` when you want them included.
</Accordion>
