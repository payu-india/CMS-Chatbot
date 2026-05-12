---
api:
  file: updated_cards_merchant_hosted.json
  operationId: MerchantHostedCheckout-Cards
hidden: false
link:
  new_tab: false
metadata:
  description: >-
    Access the PayU API Reference for collecting card payments with Merchant
    Hosted Checkout. Find detailed documentation on integrating debit or card
    payments and secure authentication. Utilize the interactive simulator to
    test API calls, ensuring smooth and efficient payment processing. Perfect
    for developers aiming to integrate robust card payment solutions into their
    custom checkout systems.
  keywords:
    - Cards Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Cards Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Cards Merchant Hosted Checkout
    - _payment API for Cards Merchant Hosted Checkout
    - _payment API simulation for Cards Custom Checkout
    - _payment API simulation for Cards Merchant Hosted Checkout
    - Credit Cards Merchant Hosted Checkout Collect Payment API
    - Simulator for PayU payment collection
    - Credit Cards Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Credit Cards Merchant Hosted Checkout
    - _payment API for Credit Cards Merchant Hosted Checkout
    - _payment API simulation for Credit Cards Custom Checkout
    - _payment API simulation for Credit Cards Merchant Hosted Checkout
---
You can collect payments from customers with leading cards using the Merchant Hosted integration. You need to ensure that **CC** or **DC** for the {/* Fixed Glossary component syntax */}<Glossary>pg</Glossary> parameter and card code based on the desired card provider for the {/* Fixed Glossary component syntax */}<Glossary>bankcode</Glossary> parameter is posted.

<Callout icon="📘" theme="info">
  **Note**: PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team ([integration@pay.in](mailto:integration@pay.in)).
</Callout>

<br />

<Cards_PayU_Labs />

<br />

## Postman Collection

<Postman_collection />

<br />

<PaymentAPIEnvironment />

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ### Normal tranasaction

  ```
  mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
  ```

  ### Parsed response for a normal transaction

  ```json
  {
    "mihpayid": "403993715531077182",
    "mode": "CC",
    "status": "success",
    "unmappedstatus": "captured",
    "key": "JPM7Fg",
    "txnid": "ypl938459435dfdfdf",
    "amount": "1000.00",
    "cardCategory": "domestic",
    "discount": "0.00",
    "net_amount_debit": "1000",
    "addedon": "2024-02-27 15:00:42",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "lastname": "",
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": "",
    "zipcode": "",
    "email": "ashish@gmail.com",
    "phone": "9876543210",
    "udf1": "",
    "udf2": "",
    "udf3": "",
    "udf4": "",
    "udf5": "",
    "udf6": "",
    "udf7": "",
    "udf8": "",
    "udf9": "",
    "udf10": "",
    "hash": "84bbbf0fa3ba2a39942f6c3deab234c4d00bc5b6aceee5cda3c8200d6e1714e19c224d47e24d0c4a9a0cce40eddbae1dc46455c69e5e7d5dd62f6636bfab337c",
    "field1": "896193988312194700",
    "field2": "857712",
    "field3": "1000.00",
    "field4": "",
    "field5": "00",
    "field6": "02",
    "field7": "AUTHPOSITIVE",
    "field8": "AUTHORIZED",
    "field9": "Transaction is Successful",
    "payment_source": "payu",
    "PG_TYPE": "CC-PG",
    "bank_ref_num": "896193988312194700",
    "bankcode": "CC",
    "error": "E000",
    "error_Message": "No Error",
    "cardnum": "XXXXXXXXXXXX2346",
    "cardhash": "This field is no longer supported in postback params.",
    "splitInfo": "{"splitStatus":"splitNotReceived","splitSegments":[]}"
  }
  ```

  ### Response for a save card transaction

  ```
  mihpayid=403993715532392220&mode=CC&status=success&key=gtKFFx&txnid=05539c1e8d56c0bf4f2e&amount=10.00&addedon=2024-09-26+16%3A39%3A03&productinfo=Product+Info&firstname=CARDHOLDERXXXXXXXXNAME-Admin&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40example.com&"phone":"##########"&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&card_token=96f5e43b7fa3c78b93656&card_no=XXXXXXXXXXXX0008&field0=&field1=6MAESTROMAESTRO0&field2=696292&field3=10.00&field4=&field5=00&field6=02&field7=AUTHPOSITIVE&field8=AUTHORIZED&field9=Transaction+is+Successful&payment_source=sist&PG_TYPE=CC-PG&error=E000&error_Message=No+Error&issuing_bank=YES&card_type=MAST&cardToken=&net_amount_debit=10&discount=0.00&offer_key=&offer_availed=&unmappedstatus=captured&hash=14b08bf22072fde0a6a59cac5826d386e107dd8dce058d1a457b102e624aa729b0119d8b7920354ee0d6e6541af2851f7b88e9332eda8fd79c556a5ea6babe4c&bank_ref_no=6MAESTROMAESTRO0&bank_ref_num=6MAESTROMAESTRO0&bankcode=CC&surl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&curl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&furl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&card_hash=46261359f70225c5ed11ef395058f3b2f7d003280bb4feb2f21e41aac113a252&pa_name=CARDHOLDERXXXXXXXXNAME
  ```

  ### Parsed response for a save card transaction

  ```php
  [mihpayid] => 403993715532392220
      [mode] => CC
      [status] => success
      [unmappedstatus] => captured
      [key] => gtKFFx
      [txnid] => 05539c1e8d56c0bf4f2e
      [amount] => 10.00
      [cardCategory] => domestic
      [discount] => 0.00
      [net_amount_debit] => 10
      [addedon] => 2024-09-26 16:39:03
      [productinfo] => Product Info
      [firstname] => Payu-Admin
      [lastname] => 
      [address1] => 
      [address2] => 
      [city] => 
      [state] => 
      [country] => 
      [zipcode] => 
      [email] => test@example.com
      [phone] => 1234567890
      [udf1] => 
      [udf2] => 
      [udf3] => 
      [udf4] => 
      [udf5] => 
      [udf6] => 
      [udf7] => 
      [udf8] => 
      [udf9] => 
      [udf10] => 
      [hash] => 14b08bf22072fde0a6a59cac5826d386e107dd8dce058d1a457b102e624aa729b0119d8b7920354ee0d6e6541af2851f7b88e9332eda8fd79c556a5ea6babe4c
      [field1] => 639639309044936000
      [field2] => 696292
      [field3] => 10.00
      [field4] => 
      [field5] => 00
      [field6] => 02
      [field7] => AUTHPOSITIVE
      [field8] => AUTHORIZED
      [field9] => Transaction is Successful
      [payment_source] => sist
      [pa_name] => PayU
      [PG_TYPE] => CC-PG
      [bank_ref_num] => 639639309044936000
      [bankcode] => CC
      [error] => E000
      [error_Message] => No Error
      [cardToken] => 96f5e43b7fa3c78b93656
      [cardnum] => XXXXXXXXXXXX0008
      [cardhash] => This field is no longer supported in postback params.
      [issuing_bank] => YES
      [card_type] => MAST
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

## Request parameters

<Callout icon="🚧" theme="warn">
  **Values to be used in Test environment**: For values to be used in Test environment, refer to <Anchor label="Test Cards, UPI ID and Wallets" target="_blank" href="doc:test-cards-upi-id-and-wallets">Test Cards, UPI ID and Wallets</Anchor>.
</Callout>

{/* Properly formatted JSX component */}

<TransactionStages />

<Callout icon="📘" theme="info">
  **References:**

  * For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
  * Card number formats of various card types: [Card Number Formats](doc:card-number-formats).
</Callout>
