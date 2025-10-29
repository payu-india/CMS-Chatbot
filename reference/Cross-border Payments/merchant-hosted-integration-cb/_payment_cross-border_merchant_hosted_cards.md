---
title: Cards - CB
api:
  file: cb_merchant_hosted_cards.json
  operationId: MerchantHostedCheckout-Cards
hidden: false
link:
  new_tab: false
metadata:
  title: >-
    Collect Payment API using Cards - Merchant Hosted with Cross-Border
    Payments 
---
You can collect payments from customers with leading cards using the Merchant Hosted integration for Cross Border Payments. The **buyer_type_business** parameter is used for Cross Border payment transactions to indicate the type of business of the buyer.

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.

<Callout icon="📘" theme="info">
  **Note**: PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team ([integration@pay.in](mailto:integration@pay.in)).
</Callout>

<PaymentAPIEnvironment />

<details>
  <summary>Sample request</summary>

  ```
  ```
</details>

<details>
  <summary>Sample response</summary>

  ## Normal tranasaction

  ### Response for a normal transaction

  ```
  ```

  ### Parsed response for a normal transaction

  ```
  ```

  ## Save card transaction

  ### Response for a save card transaction

  ```
  ```

  ### Parsed response for a save card transaction

  ```
  ```

  <details>
    <summary>Response parameters</summary>

    > 📘 Notes:
    > To identify a particular transaction is routed to which aggregator you have to check the udf parameters of the response. The following aggregators are showing udf parameters if the transaction are routed them:
    >
    > * PayU
    > * RazorPay
    > * BillDesk
    > * Pinelabs
    > * Paytm
  </details>
</details>

## Request parameters

> 🚧 Values to be used in Test environment
>
> For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.

<TransactionStages />

<Callout icon="📘" theme="info">
  **Reference**:

  * For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
  * Card number formats of various card types: [Card Number Formats](doc:card-number-formats).
</Callout>
