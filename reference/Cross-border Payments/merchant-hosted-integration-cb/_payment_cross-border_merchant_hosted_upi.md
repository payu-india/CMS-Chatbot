---
title: UPI - CB
excerpt: ''
api:
  file: merchant-hosted-42.json
  operationId: MerchantHostedCheckout-UPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
PayU allows you to collect payments using UPI handles. For the list of UPI providers supported, refer to [UPI Handles](doc:upi-handles).  The **buyer_type_business** parameter is used for Cross Border payment transactions to indicate the type of business of the buyer.

After the payment is complete, you must use the [Invoice Upload API](ref:invoice_upload_api) to upload the invoices for banks processing.

### Recommended prerequisite before initiating payment

When your customer makes payment through UPI, you can validate the customer’s Virtual Payment Address (VPA) and then initiate payment. The **validateVpa** API is used to validate the UPI handle. 

Validate the VPA (UPI handle) using the **validateVpa** API.  For more information, refer to [Validate VPA Handle API](ref:validate_vpa_api).

### Environment

<PaymentAPIEnvironment />

<details>

<summary>Sample request</summary>

```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=VPA-anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=649bc87e0e8ee7bbd1e930d43c99a9165eb9fa7a3f4542a33e8d66bd207a63d631708fd9781e56b133581f7dabeaa67baa5609d5e5c9990f986792d59e7d41cb"
```

</details>

<details>  

<summary>Sample response</summary>

```
Array
(
    [mihpayid] => 403993715523409521
    [mode] => UPI
    [status] => success
    [unmappedstatus] => captured
    [key] => JPM7Fg
    [txnid] => 5jJ9xRceXX1ydT
    [amount] => 10.00
    [discount] => 0.00
    [net_amount_debit] => 1000
    [addedon] => 2021-07-02 15:03:50
    [productinfo] => iPhone
    [firstname] => PayU User
    [lastname] => 
    [address1] => 
    [address2] => 
    [city] => 
    [state] => 
    [country] => 
    [zipcode] => 
    [email] => test@gmail.com
    [phone] => 9876543210
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
    [hash] => 716f92a6452adadba68d133ba7f5ca3f3403f03f554e3ef850911f3e6727ee73402b249054170ad276c8b55ca12368a5e27cc69ffb0642ef6403dae9a5708794
    [field1] => vpa-anything@payu
    [field2] => 5jJ9xRceXX1ydT
    [field3] => 
    [field4] => PayU User
    [field5] => AXIhh4ExnaJ9dKiJvPxsewHwxMMmT3ba7UY
    [field6] => 
    [field7] => Transaction completed successfully
    [field8] => 
    [field9] => Transaction completed successfully
    [payment_source] => payu
    [PG_TYPE] => UPI-PG
    [bank_ref_num] => 5jJ9xRceXX1ydT
    [bankcode] => UPI
    [error] => E000
    [error_Message] => No Error
)
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


</details>

## Request parameters

<details> <summary> Additional info for request parameters</summary>

<Additional_paymentRequestParams />

</details>

> 📘 Reference
> 
> For the character limit of each parameter and detailed description, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).

> 🚧 You can test UPI only with the anything@payu or [9999999999@payu.in](mailto:9999999999@payu.in) as VPA.

> ❗️ Error handling
> 
> If any error message is displayed with an error code, refer to the <a href="error-codes" target="_blank">Error Codes</a> section to understand the reason for these error codes.