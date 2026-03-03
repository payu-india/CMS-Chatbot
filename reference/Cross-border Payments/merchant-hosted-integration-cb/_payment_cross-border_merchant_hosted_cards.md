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

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload invoices / AWBs (Air-way bill number). AWB details are mandatory for Goods transactions.

<PaymentAPIEnvironment />

<details>
  <summary>Sample request</summary>

  ```curl
curl --location --request POST 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JPM7Fg' \
--data-urlencode 'txnid=payuTestTransaction12345' \
--data-urlencode 'amount=100.00' \
--data-urlencode 'firstname=Ashish' \
--data-urlencode 'lastname=Kumar' \
--data-urlencode 'email=test@payu.in' \
--data-urlencode 'phone=9988776655' \
--data-urlencode 'productinfo=Product Info' \
--data-urlencode 'address1=123 Main Street' \
--data-urlencode 'city=New York' \
--data-urlencode 'state=NY' \
--data-urlencode 'country=US' \
--data-urlencode 'zipcode=10001' \
--data-urlencode 'surl=https://test.payu.in/admin/test_response' \
--data-urlencode 'furl=https://test.payu.in/admin/test_response' \
--data-urlencode 'pg=CC' \
--data-urlencode 'bankcode=CC' \
--data-urlencode 'ccnum=5506900480000008' \
--data-urlencode 'ccname=Test User' \
--data-urlencode 'ccvv=123' \
--data-urlencode 'ccexpmon=09' \
--data-urlencode 'ccexpyr=2026' \
--data-urlencode 'udf1=AELPR1234E' \
--data-urlencode 'udf2=' \
--data-urlencode 'udf3=02-02-1980' \
--data-urlencode 'udf4=XYZ Pvt. Ltd.' \
--data-urlencode 'udf5=INV123456' \
--data-urlencode 'buyer_type_business=1' \
--data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 's2s_client_ip=10.200.12.12' \
--data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
--data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</details>

<details>
  <summary>Sample response</summary>

  ```
{
  "metaData": {
    "message": null,
    "referenceId": "5a3e7cb9884e003dce1f28f965478a9a12fb9244fc15be91b0b3de48763a12e7",
    "statusCode": null,
    "txnId": "payuTestTransaction12345",
    "txnStatus": "Enrolled",
    "unmappedStatus": "pending",
    "resendOtp": {
      "isSupported": true,
      "attemptsLeft": 2
    },
    "submitOtp": {
      "attemptsLeft": 3
    }
  },
  "result": {
    "otpPostUrl": "https://test.payu.in/ResponseHandler.php",
    "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0i..."
  },
  "binData": {
    "pureS2SSupported": true,
    "issuingBank": "AXIS",
    "category": "creditcard",
    "cardType": "MAST",
    "isDomestic": true
  }
}
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
