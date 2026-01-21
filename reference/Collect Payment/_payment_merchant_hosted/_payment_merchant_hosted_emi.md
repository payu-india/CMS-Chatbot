---
title: EMI
api:
  file: updated_emi_merchant_hosted.json
  operationId: MerchantHostedCheckout-EMI
hidden: false
metadata:
  title: Collect Payments using EMI - Merchant Hosted Checkout
  description: >-
    Explore PayU's Merchant Hosted EMI solutions, enabling easy integration of
    EMI payment options for e-commerce platforms. Learn about API integration,
    supported banks, and flexible installment plans to enhance customer
    experience and boost sales.
  keywords:
    - EMI Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - EMI Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for EMI Merchant Hosted Checkout
    - _payment API for EMI Merchant Hosted Checkout
    - _payment API simulation for EMI Custom Checkout
    - _payment API simulation for EMI Merchant Hosted Checkout
    - "Equated Monthly Installment\_Merchant Hosted Checkout Collect Payment API"
    - Simulator for PayU payment collection
    - "Equated Monthly Installment\_Custom Checkout integration with PayU"
    - "Collect Payment API for Equated Monthly Installment\_Merchant Hosted Checkout"
---
EMI as a payment option gives your customers the freedom and affordability to purchase expensive items without having to deal with banks or NBFCs as intermediaries.

You can collect payments from customers in EMI using the Merchant Hosted integration. You need to ensure that **EMI** for the **pg** parameter and EMI code based on the card issuer and tenure for the **bankcode** parameter is posted.

<PaymentAPIEnvironment />

## Request parameters

<Callout icon="📘" theme="info">
  **Reference**: For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

<Accordion title="Values to be used in Test environment" icon="fa-flask">
  * You can used any EMI code listed in the <a href="emi-codes" target="_blank">EMI Codes</a> section. section and test cards listed in the <a href="https://docs.payu.in/docs/test-cards-upi-id-and-wallets#emi-test-cards" target="_blank">Test Cards</a> section. For example, the following values can be used:

  |                   |                         |                   |
  | :---------------- | :---------------------- | :---------------- |
  | bankcode: EMIA3   | ccnum: 5123456789012346 | ccexpmon: 05      |
  | ccexpyr: 2025     | ccvv: 123               | ccname: Any value |
  | phone: 9123412345 |                         |                   |

  * For the **amount** parameter, use **>=INR 1000** in the Test environment.
</Accordion>

> ❗️ Error handling
>
> If any error message is displayed with an error code, refer to the [Error Codes](ref:error-codes) section. to understand the reason for these error codes.
