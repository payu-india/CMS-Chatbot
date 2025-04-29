---
title: Cards
excerpt: ''
api:
  file: merchant-hosted-13.json
  operationId: MerchantHostedCheckout-Cards
deprecated: false
hidden: false
metadata:
  title: Collect Payments using Cards using Merchant Hosted Checkout
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
    - ' Credit Cards Merchant Hosted Checkout Collect Payment API'
    - Simulator for PayU payment collection
    - Credit Cards Custom Checkout integration with PayU
    - Collect payments using PayU API
    - Collect Payment API for Credit Cards Merchant Hosted Checkout
    - _payment API for Credit Cards Merchant Hosted Checkout
    - _payment API simulation for Credit Cards Custom Checkout
    - _payment API simulation for Credit Cards Merchant Hosted Checkout
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: collect-payments-with-cards-seamless
      title: Cards Integration
    - type: endpoint
      slug: process-transaction-with-a-saved-card
      title: Process Transaction with a Saved Card
---
You can collect payments from customers with leading cards using the Merchant Hosted integration. You need to ensure that **CC** or **DC** for the **<<glossary:pg>>** parameter and  card code based on the desired card provider for the **<<glossary:bankcode>>** parameter is posted.

> 📘 Note:
> 
> PayU accepts domestic and international transactions, but international transactions need to be enabled by writing to PayU Integration Team ([integration@pay.in](mailto:integration@pay.in)).

<PaymentAPIEnvironment />

<details>

<summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
```

</details>

<details>  

<summary>Sample response</summary>

## Normal tranasaction

### Response for a normal transaction

```
mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```

### Parsed response for a normal transaction

```
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

## Save card transaction

### Response for a save card transaction

```
mihpayid=403993715532392220&mode=CC&status=success&key=gtKFFx&txnid=05539c1e8d56c0bf4f2e&amount=10.00&addedon=2024-09-26+16%3A39%3A03&productinfo=Product+Info&firstname=CARDHOLDERXXXXXXXXNAME-Admin&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40example.com&"phone":"##########"&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&card_token=96f5e43b7fa3c78b93656&card_no=XXXXXXXXXXXX0008&field0=&field1=6MAESTROMAESTRO0&field2=696292&field3=10.00&field4=&field5=00&field6=02&field7=AUTHPOSITIVE&field8=AUTHORIZED&field9=Transaction+is+Successful&payment_source=sist&PG_TYPE=CC-PG&error=E000&error_Message=No+Error&issuing_bank=YES&card_type=MAST&cardToken=&net_amount_debit=10&discount=0.00&offer_key=&offer_availed=&unmappedstatus=captured&hash=14b08bf22072fde0a6a59cac5826d386e107dd8dce058d1a457b102e624aa729b0119d8b7920354ee0d6e6541af2851f7b88e9332eda8fd79c556a5ea6babe4c&bank_ref_no=6MAESTROMAESTRO0&bank_ref_num=6MAESTROMAESTRO0&bankcode=CC&surl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&curl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&furl=https%3A%2F%2Ftest.payu.in%2Fadmin%2Ftest_response&card_hash=46261359f70225c5ed11ef395058f3b2f7d003280bb4feb2f21e41aac113a252&pa_name=CARDHOLDERXXXXXXXXNAME
```

### Parsed response for a save card transaction

```
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

<br />

</details>

<details>
  <summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "mihpayid",
    "0-1": "It is a unique reference number created for each transaction at PayU’s end which is used to identify a transaction in case of a refund.",
    "1-0": "mode",
    "1-1": "This parameter describes the payment category by which the transaction was completed/attempted by the customer. The values are:    \n\t•\tCredit Card – CC   \n\t•\tDebit Card – DC   \n\t•\tNet Banking – NB  \n\t•\tCash Card – CASH  \n\t•\tEMI – EMI   \n\t•\tCardless EMI – CLEMI  \n\t•\tBuy Now Pay Later - BNPL",
    "2-0": "bankcode",
    "2-1": "This parameter contains the code indicating the payment option used for the transaction. For example, Visa Debit Card – VISA, Master Debit Card – MAST.",
    "3-0": "status",
    "3-1": "This parameter returns the status of the transaction and must be used to map the order status. Possible values are success, failure, or pending. The significance of the values for these values are:    \n\t•\t**Success**: If the value of status parameter is ’success’, the transaction is successful.   \n\t•\t**Failed**: If the value of status parameter is ‘failure’ or ‘pending’, must only be treated as a failed transaction.",
    "4-0": "unmappedstatus",
    "4-1": "This parameter holds the status of a transaction in PayU's internal database, which can include intermediate states. Possible values include: dropped, bounced, captured, auth, failed, usercancelled, or pending. For information on status description, refer to  [Payment State Explanations](ref:payment-state-explanations).",
    "5-0": "key",
    "5-1": "This parameter contains the merchant key.",
    "6-0": "error",
    "6-1": "For the failed transactions, this parameter provides the reason for failure.",
    "7-0": "error\\_message",
    "7-1": "This parameter contains the error message. For the list of error message, refer to [Error Codes](ref:error-codes).",
    "8-0": "bank\\_ref\\_num",
    "8-1": "For each successful transaction – this parameter contains the bank reference number generated by the bank.",
    "9-0": "txnid",
    "9-1": "This parameter contains the transaction ID value posted by the merchant during the transaction request.",
    "10-0": "amount",
    "10-1": "This parameter contains the original amount which was sent in the transaction request by the merchant.",
    "11-0": "cardCategory",
    "11-1": "This parameter contains the card category to indicate whether it is domestic or international.",
    "12-0": "discount",
    "12-1": "This parameter contains the discount amount by the merchant.",
    "13-0": "net_amount_debit",
    "13-1": "This parameter contains the net amount debited.",
    "14-0": "addedon",
    "14-1": "The transaction date and time of the transaction.",
    "15-0": "productinfo",
    "15-1": "This parameter contains the same value of product information which was sent in the transaction request from the merchant’s end to PayU.",
    "16-0": "firstname",
    "16-1": "This parameter contains the same value of first name which was sent in the transaction request from the merchant’s end to PayU.",
    "17-0": "lastname",
    "17-1": "This parameter contains the same value of last name which was sent in the transaction request from the merchant’s end to PayU.",
    "18-0": "email",
    "18-1": "This parameter contains the same value of email which was sent in the transaction request from the merchant’s end to PayU.",
    "19-0": "phone",
    "19-1": "This parameter contains the same value of phone which was sent in the transaction request from the merchant’s end to PayU.",
    "20-0": "hash",
    "20-1": "This parameter is crucial and is similar to the hash parameter used in the transaction request. For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).",
    "21-0": "PG\\_TYPE",
    "21-1": "This parameter gives information on the payment gateway used for the transaction.",
    "22-0": "udf1",
    "22-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "23-0": "udf2",
    "23-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "24-0": "udf3",
    "24-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5 which was sent in the transaction request from the merchant’s end to PayU.",
    "25-0": "udf4",
    "25-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "26-0": "udf5",
    "26-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "27-0": "udf6",
    "27-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "28-0": "udf7",
    "28-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.\\*\\*\\*\\*",
    "29-0": "udf8",
    "29-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "30-0": "udf9",
    "30-1": "This parameter contains the same value of udf1, udf2, udf3, udf4, or udf5, which was sent in the transaction request from the merchant’s end to PayU.",
    "31-0": "success_at",
    "31-1": "This parameter contains the date and timestamp when the transaction was successful.",
    "32-0": "cardnum",
    "32-1": "The parameter contains the card number masked and only last 4 digits are returned.",
    "33-0": "issuing_bank",
    "33-1": "The parameters contains the card issuing bank."
  },
  "cols": 2,
  "rows": 34,
  "align": [
    null,
    null
  ]
}
[/block]


> 📘 Notes:
> 
> To identify a particular transaction is routed to which aggregator you have to check the udf parameters of the response. The following aggregators are showing udf parameters if the transaction are routed them: 
> 
> - PayU
> - RazorPay  
> - BillDesk
> - Pinelabs  
> - Paytm

</details>

## Request parameters

<details>
  <summary>Additional info for request parameters </summary>

<AddionalCards_paymentRequestParametersInformation />

</details>

> 🚧 Values to be used in Test environment
> 
> For values to be used in Test environment, refer to <a href="test-cards-upi-id-and-wallets#web-checkout" target="_blank">Test Cards</a>.

<TransactionStages />

> 📘 Reference
> 
> - For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
> - Card number formats of various card types: [Card Number Formats](doc:card-number-formats).