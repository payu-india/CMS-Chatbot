---
api:
  file: cb_merchant_hosted_cards.json
  operationId: merchantHostedCheckoutCards
hidden: true
---
---
title: Cards - CB
api:
  file: Merchant Hosted Cards API.json
  operationId: merchantHostedCheckoutCards
hidden: false
link:
  new_tab: false
metadata:
  title: >-
    Collect Payment API using Cards - Merchant Hosted with Cross-Border
    Payments
---
You can collect payments from customers with leading cards using the Merchant Hosted integration for Cross-Border Payments. Post to **`/_payment`** with **`txn_s2s_flow=4`** for the Cross-Border Cards server-to-server (S2S) flow. The **buyer_type_business** parameter indicates the type of business of the buyer.

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload invoices / AWBs (Air-way bill number). AWB details are mandatory for Goods transactions.

<Callout icon="📘" theme="info">
  **Reference**: For steps to integrate Cards for Cross-Border Payments, refer to [[S2S] Plain Cards Integration - Merchant Hosted Integration](doc:plain-cards-integration-one-time-pacb) or [[S2S] Process Saved Cards with a PayU Token](doc:cards-with-payu-tokenization-one-time-pacb)
</Callout>

<PaymentAPIEnvironment />

<Accordion title="Sample Request" icon="fa-info-code">
  **With complete card details**

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

  **With saved card**

  ```curl
  curl --location --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JPM7Fg' \
  --data-urlencode 'txnid=payuTestTransaction12345' \
  --data-urlencode 'amount=100.00' \
  --data-urlencode 'firstname=Ashish' \
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
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 's2s_client_ip=10.200.12.12' \
  --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64) PayU-API-Test/1.0' \
  --data-urlencode 'user_credentials=JPM7Fg:customer_1112' \
  --data-urlencode 'storecard_token_type=0' \
  --data-urlencode 'store_card_token=10a7d7a45b72644460f108' \
  --data-urlencode 'udf1=AELPR1234E' \
  --data-urlencode 'udf3=02-02-1980' \
  --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
  --data-urlencode 'udf5=INV123456' \
  --data-urlencode 'buyer_type_business=1' \
  --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
  --data-urlencode 'hash=YOUR_CALCULATED_HASH'
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-info-reply">
  **S2S collect-payment response** (`txn_s2s_flow=4`)

  ```json
  {
    "rawBankData": "",
    "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7",
    "bankData": {
      "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7",
      "messageDigest": "c2e9e456037f033e5cc3d7b6e556189adf41eeabf706844dff70aac91f6b8e73bb1846286c8f99ea768cf38f7c12369c|523727493647950f32684bd6f1ab07aa6474016f",
      "pares": "eNrVmdeS47i2pl+lo8+loje968jOCHojGtGLvKM3opHoyacfZmZVde06PWfOzMXEjCIUgkBiYRHAWv8H4s0phyzj7CyZh+z9TcvGMSqy36r0r99jFAfhGIT/gLE8/QNNM/IPEiGoP5CUgGEwAjGCSH9/f7vRVjZ+NvgsnTVLNoxV371D/wL/Bb8B3/+exoekjLrp/S1KXoysv6MkQhHYG/Dt71ubDTL3DkMwhZIgRoIIAoL4G/BV/Qb83f42f5TG0+GtSt9Dp5gMTkMMGzxCLtm1mik1zkV02PzrDfi44y2NpuwdBuHTNgj9BiF/IsSfyOnbZ/3b88Mc3fbzaRuCwDfg54q3c2SGrEv2dwQ7nfnx7y3bnn2XnXecdn6U34C/fXtG3Tv40wcFQeK0fda+Off3t6lqf/YJ/RMi/4ShN+Cz/m2comme34M34FvpLYmW5Z2maYYVTJqWzadhJqu+0t8/57N+3vKWJdU7eA7rx+9nK7op+qGayvbD1X+veAM+XAE+p+79za6K7uxsyH7b2qYb//q9nKbnnwCwruu/VuRf/VAA8PkgAEgB5w3pWBX/8ftXqyyVu7z/32rGRl3fVUnUVEc0nQtEy6ayT3/74ds/mXGsD0sQYPHsH6epPxII7f74qAERCDttAv9s9Kcn++/08quzwxj9MZYR9NHBL4be36wszz5WRPaba8l//f4f36OAq4psnP5Puvve1c8WvtvzombO3mc3DXRwZEp92R+80+1LH1P8RNQ4/9f3dl93vgE//Pvm/NdM/TQiXzc6RMf6GG04qXdxrxgV1PAQ4FJa38tkuNT",
      "additionalInfo": {
        "authUdf1": "",
        "authUdf2": "",
        "authUdf3": "",
        "authUdf4": "",
        "authUdf5": "",
        "authUdf6": "",
        "authUdf7": "",
        "authUdf8": "",
        "authUdf9": "",
        "authUdf10": ""
      }
    },
    "authenticationStatus": "success",
    "hash": "664b8ddd1b5b2d1b68abb7eee5ea6e001a02773499ddcd86956ba0833315e7d4e69c641d7b0b3e7590532e21e71936da173f4eda716fc09f83cd1117f0d0c37c"
  }
  ```

  Validate the response **`hash`** before consuming the payload. Hash formula: `sha512(authenticationStatus|bankData|rawBankData|referenceId|SALT)`.
</Accordion>

<Accordion title="S2S response parameters" icon="fa-list">
  | **Parameter** | **Description** |
  | --- | --- |
  | rawBankData | Raw bank authentication response, URL-encoded in query-string format. |
  | referenceId | Reference ID for the transaction returned by PayU. |
  | bankData | JSON object used for the authorisation step. Contains `referenceId`, `messageDigest`, `pares`, and `additionalInfo` when authentication succeeds. |
  | authenticationStatus | Authentication status of the transaction (for example, `success`). |
  | hash | Response hash. Validate using `sha512(authenticationStatus\|bankData\|rawBankData\|referenceId\|SALT)` before consuming the response. |
</Accordion>

<Accordion title="Redirect response parameters" icon="fa-list">
  Parameters posted to **surl** or **furl** after the customer completes or abandons payment in browser-based flows.

  | **Parameter** | **Description** |
  | --- | --- |
  | mihpayid | Unique reference number created for each transaction at PayU's end; used to identify a transaction for refunds. |
  | mode | Payment category: CC (credit card), DC (debit card), NB (net banking), CASH, EMI, CLEMI, BNPL. |
  | bankcode | Code for the payment option used (for example, CC, VISA, MAST). |
  | status | Transaction status: `success`, `failure`, or `pending`. Treat `failure` and `pending` as failed for order mapping unless your integration guide specifies otherwise. |
  | unmappedstatus | Internal PayU status (for example, dropped, bounced, captured, auth, failed, usercancelled, pending). See [Payment State Explanations](ref:payment-state-explanations). |
  | key | Merchant key. |
  | error | Failure reason for failed transactions. |
  | error\_message | Error message. See [Error Codes](ref:error-codes). |
  | bank\_ref\_num | Bank reference number for successful transactions. |
  | txnid | Transaction ID posted by the merchant in the request. |
  | amount | Amount sent in the transaction request. |
  | cardCategory | Card category (domestic or international). |
  | discount | Discount amount applied by the merchant. |
  | net\_amount\_debit | Net amount debited. |
  | addedon | Transaction date and time. |
  | productinfo | Product information echoed from the request. |
  | firstname | First name echoed from the request. |
  | lastname | Last name echoed from the request. |
  | email | Email echoed from the request. |
  | phone | Phone echoed from the request. |
  | hash | Response hash. Verify using PayU post-response hash rules. See [Generate Hash](doc:generate-hash-merchant-hosted). |
  | PG\_TYPE | Payment gateway used for the transaction. |
  | udf1 | Echo of **udf1** from the request (buyer PAN for Cross-Border). |
  | udf2 | Echo of **udf2** from the request. |
  | udf3 | Echo of **udf3** from the request (buyer DOB for Cross-Border). |
  | udf4 | Echo of **udf4** from the request (merchant name for PA2PA). |
  | udf5 | Echo of **udf5** from the request (invoice ID). |
  | udf6 | Echo of **udf6** from the request. |
  | udf7 | Import or export code when passed via **udf_params**. |
  | udf8 | Airway bill / consignment number when passed via **udf_params**. |
  | udf9 | Echo of **udf9** from the request. |
  | success\_at | Date and timestamp when the transaction succeeded. |
  | cardnum | Masked card number (last four digits). |
  | issuing\_bank | Card issuing bank. |
</Accordion>

> 🚧 Values to be used in Test environment
>
> For values to be used in the test environment, refer to [Test Cards](doc:test-cards-upi-id-and-wallets#web-checkout).

<TransactionStages />

<Callout icon="📘" theme="info">
  **Reference**:

  * For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
  * Card number formats of various card types: [Card Number Formats](doc:card-number-formats).
</Callout>