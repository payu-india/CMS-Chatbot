---
title: Buy Now Pay Later (BNPL)
deprecated: false
hidden: false
metadata:
  robots: index
---
Buy Now Pay Later (BNPL) is a payment method that allows your customers to purchase goods or services and defer payment for a period of time, usually ranging from a few weeks to several months. With BNPL, your customers can make a purchase without paying the full amount upfront, and instead, pay the cost of the purchase in installments over a set period of time.

<Note>
  Register for an account with PayU before you start integration. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Note>

## How it works?

PayU aggregates top BNPL lenders (such as LazyPay, Simpl, and others) into a single integration, handling the complex routing, eligibility checks, and authentication flows behind the scenes. The merchant receives the full transaction amount upfront (minus standard processing fees), while the lender assumes the consumer credit risk.

## Customer Journey

The BNPL ecosystem supports two primary checkout journeys depending on whether the customer has linked their account:

### First-Time User Flow

1. **Eligibility Check:** The merchant app calls the Eligibility API before rendering the payment page.
2. **Account Linking:** If eligible, the customer selects their preferred BNPL lender (e.g., LazyPay) and initiates linking by entering their mobile number.
3. **OTP Authentication:** An OTP is sent to the customer's registered mobile number. The customer enters the OTP to authorize both the account link and the initial transaction.
4. **Token Generation:** Upon successful verification, an access token is generated and stored securely for future transactions.

### Repeat User Flow (1-Click Checkout)

1. **Eligibility Check:** The merchant app verifies the customer's current eligibility status.
2. **One-Click Payment:** The customer selects the pre-linked BNPL option.
3. **Direct Debit:** The transaction is processed instantly without requiring another OTP, utilizing the securely stored access token.

## Features of BNPL

* **Instant Credit Decisions:** Real-time eligibility checks ensure customers are approved instantly at checkout.
* **Flexible Repayment Windows:** Customers can choose between 15-day interest-free cycles or multi-month installment plans.
* **OTP-Less Repeat Checkout:** True one-click checkout experience for returning, pre-linked customers.
* **Unified API Stack:** Access multiple BNPL lenders through a single, standardized integration contract.

## Benefits of BNPL

### For Merchants

* **Higher Conversion Rates:** Eliminating payment friction reduces cart abandonment at the final checkout step.
* **Increased Average Order Value (AOV):** Customers are more willing to make larger purchases when flexible payment options are available.
* **Upfront Settlement:** Merchants get paid upfront, while the lender manages the collection risk.

### For Customers

* **Frictionless Checkout:** Complete transactions in seconds with minimal input.
* **Zero Interest Options:** Access short-term credit with no hidden fees or interest charges when paid on time.
* **Safe & Secure:** Transactions are backed by PayU's robust fraud prevention and secure tokenization systems.

## Next Steps

To begin integrating BNPL on your platform, choose the integration path that matches your checkout architecture:

* [PayU Hosted Checkout BNPL Workflow](doc:bnpl-workflow-payu-hosted-checkout) — Easiest integration; PayU hosts the payment page and handles the entire UI flow.
* [Merchant Hosted BNPL Workflow](doc:general-flow-bnpl-integration-with-merchant-hosted) — Full control over the checkout UI; collect customer details natively and post them to PayU.
* [BNPL Link and Pay Integration](doc:link-and-pay) — Enable seamless, one-click repeat checkouts using native OTP linking.
