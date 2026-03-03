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

<Callout icon="📘" theme="info">
  **Reference**: For steps to integrate Cards for Cross-Border Payments, refer to [[S2S] Plain Cards Integration - Merchant Hosted Integration](doc:plain-cards-integration-one-time-pacb) or [[S2S] Process Saved Cards with a PayU Token](doc:cards-with-payu-tokenization-one-time-pacb)
</Callout>

<PaymentAPIEnvironment />

<Accordion title="Sample Request" icon="fa-info-code">
  **With Complete Card Details**
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

  **With Saved Card**
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
````
</Accordion>

<Accordion title="Sample Response" icon="fa-info-reply">
  **Parsed response**

  ```json
 { 
    "rawBankData" : ""  
    "referenceId":  "00c44a4c8306f9cbe5ecf6133afe08a7" 
    "bankData" : { 
    "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7", 
    "messageDigest": "c2e9e456037f033e5cc3d7b6e556189adf41eeabf706844dff70aac91f6b8e73bb1846286c8f99ea768cf38f7c12369c|523727493647950f32684bd6f1ab07aa6474016f", 
    "pares": "eNrVmdeS47i2pl+lo8+loje968jOCHojGtGLvKM3opHoyacfZmZVde06PWfOzMXEjCIUgkBiYRHAWv8H4s0phyzj7CyZh+z9TcvGMSqy36r0r99jFAfhGIT/gLE8/QNNM/IPEiGoP5CUgGEwAjGCSH9/f7vRVjZ+NvgsnTVLNoxV371D/wL/Bb8B3/+exoekjLrp/S1KXoysv6MkQhHYG/Dt71ubDTL3DkMwhZIgRoIIAoL4G/BV/Qb83f42f5TG0+GtSt9Dp5gMTkMMGzxCLtm1mik1zkV02PzrDfi44y2NpuwdBuHTNgj9BiF/IsSfyOnbZ/3b88Mc3fbzaRuCwDfg54q3c2SGrEv2dwQ7nfnx7y3bnn2XnXecdn6U34C/fXtG3Tv40wcFQeK0fda+Off3t6lqf/YJ/RMi/4ShN+Cz/m2comme34M34FvpLYmW5Z2maYYVTJqWzadhJqu+0t8/57N+3vKWJdU7eA7rx+9nK7op+qGayvbD1X+veAM+XAE+p+79za6K7uxsyH7b2qYb//q9nKbnnwCwruu/VuRf/VAA8PkgAEgB5w3pWBX/8ftXqyyVu7z/32rGRl3fVUnUVEc0nQtEy6ayT3/74ds/mXGsD0sQYPHsH6epPxII7f74qAERCDttAv9s9Kcn++/08quzwxj9MZYR9NHBL4be36wszz5WRPaba8l//f4f36OAq4psnP5Puvve1c8WvtvzombO3mc3DXRwZEp92R+80+1LH1P8RNQ4/9f3dl93vgE//Pvm/NdM/TQiXzc6RMf6GG04qXdxrxgV1PAQ4FJa38tkuNT", 
    "additionalInfo": 
    { 
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
    "authenticationStatus"  :  "success", 
    "hash" : "664b8ddd1b5b2d1b68abb7eee5ea6e001a02773499ddcd86956ba0833315e7d4e69c641d7b0b3e7590532e21e71936da173f4eda716fc09f83cd1117f0d0c37c"} 
  ```
</Accordion>

<Accordion title="Response parameters" icon="fa-list">
  | **Parameter**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                            |
  | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | mihpayid           | It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.                                                                                                                                                                                                                                                                                    |
  | mode               | This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are: • Credit Card – CC • Debit Card – DC • Net Banking – NB • Cash Card – CASH • EMI – EMI • Cardless EMI – CLEMI • Buy Now Pay Later - BNPL                                                                                                                                                   |
  | bankcode           | This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.                                                                                                                                                                                                                                                                    |
  | status             | This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are: • **Success**: If the value of status parameter is 'success', the transaction is successful. • **Failed**: If the value of status parameter is 'failure' or 'pending', must only be treated as a failed transaction. |
  | unmappedstatus     | This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](ref:payment-state-explanations).                                                                                          |
  | key                | This parameter contains the merchant key.                                                                                                                                                                                                                                                                                                                                                                                  |
  | error              | For the failed transactions, this parameter provides the reason for failure.                                                                                                                                                                                                                                                                                                                                               |
  | error\_message     | This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).                                                                                                                                                                                                                                                                                                         |
  | bank\_ref\_num     | For each successful transaction – this parameter contains the bank reference number generated by the bank.                                                                                                                                                                                                                                                                                                                 |
  | txnid              | This parameter contains the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                                                                                                                                    |
  | amount             | This parameter contains the original amount which was sent in the transaction request by the merchant.                                                                                                                                                                                                                                                                                                                     |
  | cardCategory       | This parameter contains the card category to indicate whether it is domestic or international.                                                                                                                                                                                                                                                                                                                             |
  | discount           | This parameter contains the discount amount by the merchant.                                                                                                                                                                                                                                                                                                                                                               |
  | net\_amount\_debit | This parameter contains the net amount debited.                                                                                                                                                                                                                                                                                                                                                                            |
  | addedon            | The transaction date and time of the transaction.                                                                                                                                                                                                                                                                                                                                                                          |
  | productinfo        | This parameter contains the same value of product information which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                   |
  | firstname          | This parameter contains the same value of first name which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                            |
  | lastname           | This parameter contains the same value of last name which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                             |
  | email              | This parameter contains the same value of email which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                                 |
  | phone              | This parameter contains the same value of phone which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                                 |
  | hash               | This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).                                                                                                                                                                                                                                         |
  | PG\_TYPE           | This parameter gives information on the payment gateway used for the transaction.                                                                                                                                                                                                                                                                                                                                          |
  | udf1               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf2               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf3               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                       |
  | udf4               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf5               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf6               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf7               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf8               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | udf9               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |
  | success\_at        | This parameter contains the date and timestamp when the transaction was successful.                                                                                                                                                                                                                                                                                                                                        |
  | cardnum            | The parameter contains the card number masked and only last 4 digits are returned.                                                                                                                                                                                                                                                                                                                                         |
  | issuing\_bank      | The parameters contains the card issuing bank.                                                                                                                                                                                                                                                                                                                                                                             |
</Accordion>

> 🚧 Values to be used in Test environment
>
> For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.

<TransactionStages />

<Callout icon="📘" theme="info">
  **Reference**:

  * For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
  * Card number formats of various card types: [Card Number Formats](doc:card-number-formats).
</Callout>
