---
title: BNPL
api:
  file: updated_bnpl_merchant_hosted.json
  operationId: MerchantHostedCheckout-Cards
hidden: false
metadata:
  title: Collect Payments using BNPL - Merchant Hosted Checkout
  description: >-
    This section describes step-by-step procedure to integrate _payment API for
    seamless integration.
  keywords:
    - BNPL Seamless Integration
    - Buy Now Pay Later Seamless Integration
    - BNPL Mechant Hosted Integration
    - Buy Now Pay Later Merchant Hosted Integration
    - ''
---
Buy Now Pay Later (<Glossary>BNPL</Glossary>) allows your customers to spread their payments over a relatively short period instead of paying upfront. You can collect payments from customers with BNPL using the Merchant Hosted Checkout integration.

You can collect payments from customers in EMI using the Merchant Hosted integration. You need to ensure that **BNPL** for the **pg** parameter and BNPL code based on the provider and tenure for the **bankcode** parameter is posted.

## Postman Collection

<Postman_collection />

<Payment_Environment />

<br />

<Accordion title="Sample Request" icon="fa-calendar">
  ```curl
  curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d '{
  "key":"J****g",
  "txnid":"5jJ9xYceXX1ydT",
  "amount":"1000.00",
  "firstname":"Ashish",
  "email":"test@gmail.com",
  "phone":"9876543210",
  "productinfo":"iPhone",
  "pg":"BNPL",
  "bankcode":"LAZYPAY",
  "surl":"https://apiplayground-response.herokuapp.com/",
  "furl":"https://apiplayground-response.herokuapp.com/",
  "hash":"6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
  }'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-info-circle">
  ```
  Array
  (
      [mihpayid] => 403993715523409521
      [mode] => BNPL
      [status] => success
      [unmappedstatus] => captured
      [key] => J****g
      [txnid] => 5jJ9xYceXX1ydT
      [amount] => 1000.00
      [discount] => 0.00
      [net_amount_debit] => 1000
      [addedon] => 2021-07-02 15:03:50
      [productinfo] => iPhone
      [firstname] => PayU User
      [lastname] => 
  		[address1] =>
	)

  ```
</Accordion>

## Request parameters

> 📘 Reference
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

<Accordion title="Values to be used in Test environment" icon="fa-flask">
  * To use your mobile number for testing with Lazypay as **bankcode**, contact PayU Support to whitelist your mobile number.
  * Use the following values with HDFC as BNPL provider:
    * Card number: 4234567890056334
    * Phone number: 9123412345
    * OTP: 123456
  * For the complete test credentials, refer to <a href="test-cards-upi-id-and-wallets#test-bnpl-credentials" target="_blank">Test Cards</a>.
</Accordion>

> ❗️ Error handling
>
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.
