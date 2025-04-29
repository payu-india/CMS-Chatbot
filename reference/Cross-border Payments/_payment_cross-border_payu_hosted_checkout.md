---
title: PayU Hosted Checkout - CB
excerpt: ''
api:
  file: merchant-hosted-40.json
  operationId: PayUHostedCheckout
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The Collect Payment API (**\_payment** API) can be used to collect payments for the Cross Border Payments. The **buyer_type_business** parameter is used for Cross Border payment transactions to indicate the type of business of the buyer.

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.

> 📘 Reference:
> 
> For an example of how to submit a payment request on your website, refer to [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website). To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](doc:handling-the-redirect-urls).

### Environment

|                            |                                   |
| :------------------------- | :-------------------------------- |
| **Test Environment**       | <https://test.payu.in/_payment>   |
| **Production Environment** | <https://secure.payu.in/_payment> |

<details>
  <summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/_payment"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&txnid=PQI6MqpYrjEefU&amount=10.00
&firstname=PayU User&email=test@gmail.com&phone=9876543210
&productinfo=iPhone&surl=
https://apiplayground-response.herokuapp.com/
&furl=https://apiplayground-response.herokuapp.com/
&buyer_type_business=Travels
&hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
```

</details>

<details>  

<summary>Sample response</summary>

#### Response

```
mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```

#### Parsed response

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
    "31-0": "field1",
    "31-1": "",
    "32-0": "field2",
    "32-1": "",
    "33-0": "field3",
    "33-1": "",
    "34-0": "field4",
    "34-1": "",
    "35-0": "field5",
    "35-1": "",
    "36-0": "field6",
    "36-1": "",
    "37-0": "field7",
    "37-1": "",
    "38-0": "field8",
    "38-1": "",
    "39-0": "field9",
    "39-1": "",
    "40-0": "success_at",
    "40-1": "This parameter contains the date and timestamp when the transaction was successful.",
    "41-0": "cardnum",
    "41-1": "The parameter contains the card number masked and only last 4 digits are returned.",
    "42-0": "issuing_bank",
    "42-1": "The parameters contains the card issuing bank."
  },
  "cols": 2,
  "rows": 43,
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

<summary>Additional information for request parameters</summary>

<AddionalCards_paymentRequestParametersInformation />

> 📘 Note:
> 
> Collecting the information for the following parameters from customers is helpful when it comes to issues related to fraud detection and chargebacks. Hence, it is must to provide the correct information:
> 
> - email
> - phone
> - address1

</details>

> 📘 Reference:
> 
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

<TransactionStages />

[block:tutorial-tile]
{
  "backgroundColor": "#018FF4",
  "emoji": "🦉",
  "id": "65af7cd8114cd8005335bc30",
  "link": "https://docs.payu.in/v1/recipes/payu-hosted-checkout-curl-request-walkthrough",
  "slug": "payu-hosted-checkout-curl-request-walkthrough",
  "title": "PayU Hosted Checkout cURL Request Walkthrough"
}
[/block]