---
title: MerchantHostedCheckout-Cards
api:
  file: Updated_Merchant_Hosted_Card_Checkout_API_v0.json
  operationId: MerchantHostedCheckout-Cards
hidden: false
---
PayU’s **\_payment** API supports LRS implementation using the following parameters:

* buyer\_type\_business
* lrs\_mandatory\_limit\_declaration
* lrs\_tnc
* lrs\_tcs\_declaration\_under\_limit

## Sample Request

<details>
  <summary>Sample request</summary>

  ```bash
  curl --location 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=PRiQvJ' \
  --data-urlencode 'txnid=my_order_64240' \
  --data-urlencode 'amount=5' \
  --data-urlencode 'productinfo=asfas' \
  --data-urlencode 'email=test@test.com' \
  --data-urlencode 'phone=8688359250' \
  --data-urlencode 'txn_s2s_flow=4' \
  --data-urlencode 'hash={{hash}}' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
  --data-urlencode 'udf1=' \
  --data-urlencode 'udf2=' \
  --data-urlencode 'udf3=' \
  --data-urlencode 'udf4=' \
  --data-urlencode 'udf5=' \
  --data-urlencode 'ccnum=5506900480000008' \
  --data-urlencode 'ccexpyr=2025' \
  --data-urlencode 'ccexpmon=09' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccname=test' \
  --data-urlencode 'api_version=7' \
  --data-urlencode 'firstname=sudhanshu' \
  --data-urlencode 'user_credentials=T58CQx:sudhanshu' \
  --data-urlencode 'lastname=kr' \
  --data-urlencode 'address1=308,third floor' \
  --data-urlencode 'address2=testing' \
  --data-urlencode 'city=ggn' \
  --data-urlencode 'state=UP' \
  --data-urlencode 'country=IND' \
  --data-urlencode 'zipcode=122018' \
  --data-urlencode 'buyer_type_business=1' \
  --data-urlencode 'lrs_mandatory_limit_declaration=I declare that the remittance is within my annual LRS limit' \
  --data-urlencode 'lrs_tnc=I agree to the terms and conditions for LRS transactions' \
  --data-urlencode 'lrs_tcs_declaration_under_limit=I declare that this transaction is under the specified limit'


  ```
</details>

## Sample Response

<details>
  <summary>Sample response</summary>

  ### Raw Response

  ```
  mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
  ```

  ### Parsed Response

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
    "splitInfo": "{\"splitStatus\":\"splitNotReceived\",\"splitSegments\":[]}"
  }
  ```
</details>

## Response Parameters

<details>
  <summary>Response parameters</summary>

  | **Parameter**      | **Description**                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | :----------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -- |
  | mihpayid           | It is a unique reference number created for each transaction at PayU's end which is used to identify a transaction in case of a refund.                                                                                                                                                                                                                                                                                    |    |
  | mode               | This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are: •	Credit Card – CC •	Debit Card – DC •	Net Banking – NB •	Cash Card – CASH •	EMI – EMI •	Cardless EMI – CLEMI •	Buy Now Pay Later - BNPL                                                                                                                                                   | \` |
  | bankcode           | This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.                                                                                                                                                                                                                                                                    |    |
  | status             | This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are: •	**Success**: If the value of status parameter is 'success', the transaction is successful. •	**Failed**: If the value of status parameter is 'failure' or 'pending', must only be treated as a failed transaction. |    |
  | unmappedstatus     | This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to [Payment State Explanations](ref:payment-state-explanations).                                                                                           |    |
  | key                | This parameter contains the merchant key.                                                                                                                                                                                                                                                                                                                                                                                  |    |
  | error              | For the failed transactions, this parameter provides the reason for failure.                                                                                                                                                                                                                                                                                                                                               |    |
  | error\_message     | This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).                                                                                                                                                                                                                                                                                                         |    |
  | bank\_ref\_num     | For each successful transaction – this parameter contains the bank reference number generated by the bank.                                                                                                                                                                                                                                                                                                                 |    |
  | txnid              | This parameter contains the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                                                                                                                                    |    |
  | amount             | This parameter contains the original amount which was sent in the transaction request by the merchant.                                                                                                                                                                                                                                                                                                                     |    |
  | cardCategory       | This parameter contains the card category to indicate whether it is domestic or international.                                                                                                                                                                                                                                                                                                                             |    |
  | discount           | This parameter contains the discount amount by the merchant.                                                                                                                                                                                                                                                                                                                                                               |    |
  | net\_amount\_debit | This parameter contains the net amount debited.                                                                                                                                                                                                                                                                                                                                                                            |    |
  | addedon            | The transaction date and time of the transaction.                                                                                                                                                                                                                                                                                                                                                                          |    |
  | productinfo        | This parameter contains the same value of product information which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                   |    |
  | firstname          | This parameter contains the same value of first name which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                            |    |
  | lastname           | This parameter contains the same value of last name which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                             |    |
  | email              | This parameter contains the same value of email which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                                 |    |
  | phone              | This parameter contains the same value of phone which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                                                 |    |
  | hash               | This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).                                                                                                                                                                                                                                         |    |
  | PG\_TYPE           | This parameter gives information on the payment gateway used for the transaction.                                                                                                                                                                                                                                                                                                                                          |    |
  | udf1               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | udf2               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | udf3               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                       |    |
  | udf4               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | udf5               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | udf6               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | udf7               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | udf8               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | udf9               | This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant's end to PayU.                                                                                                                                                                                                                                                                      |    |
  | field1             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field2             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field3             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field4             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field5             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field6             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field7             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field8             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | field9             |                                                                                                                                                                                                                                                                                                                                                                                                                            |    |
  | success\_at        | This parameter contains the date and timestamp when the transaction was successful.                                                                                                                                                                                                                                                                                                                                        |    |
  | cardnum            | The parameter contains the card number masked and only last 4 digits are returned.                                                                                                                                                                                                                                                                                                                                         |    |
  | issuing\_bank      | The parameters contains the card issuing bank.                                                                                                                                                                                                                                                                                                                                                                             |    |
</details>

## Request Parameters

<details>
  <summary>Additional information for request parameters</summary>

  ### Payment Request Parameters Information

  The payment request parameters contain important information for processing payments securely and efficiently. Please refer to the API documentation for the full list of required and optional parameters.
</details>

> 📘 **Reference:**
>
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).