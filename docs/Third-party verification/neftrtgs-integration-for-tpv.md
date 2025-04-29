---
title: NEFT/RTGS Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  keywords:
    - NEFT Integration for TPV
    - ' Third Party Validation NEFT Integration'
    - API Integration for NEFT TPV
    - ' PayU NEFT TPV Integration'
    - TPV NEFT Setup Guide
    - RTGS Integration for TPV
    - ' Third Party Validation RTGS Integration'
    - API Integration for RTGS TPV
    - ' PayU RTGS TPV Integration'
    - TPV RTGS Setup Guide
  robots: index
next:
  description: ''
---
Integrate <<glossary:TPV>> through NEFT/RTGS using the procedure described in this section.

## Step 1: List the Account Numbers

Collect or prepare a list of account numbers that must be posted to PayU for TPV at step 2.

## Step 2: Post the parameters to PayU

With the following additional parameters, make the transaction request with the customer’s bank account number to the PayU using the Collect Payment (**\_payment**) API. For more information, refer to <a href="ref:_payment_merchant_hosted" target="_blank"> Collect Payment API - Merchant Hosted Checkiout</a>.

<PaymentAPIEnvironment />

### Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "<<glossary:pg>>",
    "0-1": "It defines the payment category for which you wish to perform TPV. For Net Banking, pg= ’NEFTRTGS.",
    "0-2": "NEFTRTGS",
    "1-0": "<<glossary:bankcode>>",
    "1-1": "The bankcode for the NEFT/RTGS transaction. For more information, refer to [Bank Codes for TPV](doc:bank-codes-for-tpv).  \nThis parameter defines the bankcode for NEFT/RTGS. **EFTAXTPV** must be used as bankcode for NEFT/RTGS.",
    "1-2": "EFTAXTPV",
    "2-0": "beneficiarydetail",
    "2-1": "This is a JSON format text and there should be key named beneficiaryAccountNumber with account number as value and ifscCode with customer IFSC code as value.",
    "2-2": "{\"beneficiaryAccountNumber\":\"6612262\\*\\*\\*5|323132312\\*\\*\\*3123\",  \n\"ifscCode\":\"KKBK0006749|HDFC000231|SBIN213213213\"}",
    "3-0": "api_version",
    "3-1": "The api_version “6” must be passed fro this parameter.",
    "3-2": "6"
  },
  "cols": 3,
  "rows": 4,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


#### Checksum Logic for Hash

The following hash logic must be used for the parameters posted:

> 📘 beneficiarydetail parameter in Hashing:
> 
> The **beneficiarydetail** parameter value will be at last or the last value to be appended.
> 
> ```plaintext
> key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT
> ```

> 📘 Notes:
> 
> - For NEFT/RTGS TPV, merchant should always send both customer account no and customer IFSC Code in Request.
> - For NEFT/RTGS TPV, the flow will work for **txn\_s2s\_flow = 1** or **txn\_s2s\_flow =** 4 as is. For **txn\_s2s\_flow = 1**, the condition is **payus2s** flag needs to be enabled for that merchant

### Optional configuration

PayU provides an optional **Back to Merchant** button on the payment challan of a NEFT/RTGS payment. This button enables your customer to go back to the merchant portal once the transaction is done.

_Sample challan of a NEFT/RTGS transaction_

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4f959a8-neftrtgs_challan.jpeg",
        "",
        ""
      ],
      "align": "center",
      "sizing": "400px"
    }
  ]
}
[/block]


### Sample request

```
curl -X POST "https://test.payu.in/_payment
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&txnid=blMwz0rgz9udtp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=&productinfo=iPhone&pg=NEFTRTGS&bankcode=EFTAXTPV&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&api_version=6&beneficiarydetail='{\"beneficiaryAccountNumber\":\"002001600674\",\"ifscCode\":\"KTKB0000046\"}&hash="
```

## Step 3: Check the response from PayU

### Hash validation logic for payment response (Reverse Hashing)

While sending the response, PayU takes the exact same parameters that were sent in the request (in reverse order) to calculate the hash and returns it to you. You must verify the hash and then mark a transaction as a success or failure. This is to make sure the transaction has not tampered within the response.

The order of the parameters is similar to the following code block:

```
sha512(SALT|beneficiarydetail|status||||||udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### Response parameters

The following table describes the parameters in the response from PayU:

| **Param Name**   | **Description**                                                                                                                                                                                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| mihpayid         | It is a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.                                                                                                 |
| merchantid       | It is the unique ID of the merchant.                                                                                                                                                                                                                                                                                     |
| txnid            | This parameter would contain the transaction ID value posted by the merchant during the transaction request.                                                                                                                                                                                                             |
| transaction\_fee | The transaction fee for the TPV transaction. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                                              |
| discount         | The discount amount given by bank on the transaction fee (if any).                                                                                                                                                                                                                                                       |
| amount           | The net amount after discount (if any) is displayed in this parameter. For Net Banking, INR 10 is charged by default.                                                                                                                                                                                                    |
| paymentgatewayid | The payment gateway identifier for the bank sending the response.                                                                                                                                                                                                                                                        |
| pg               | The payment gateway used for the transaction. In case of NEFT/RTGS, it is “NEFTRTGS.”                                                                                                                                                                                                                                    |
| status           | This parameter gives the status of the transaction as either success, failed or pending. Possible values: success, failure, pending If the value of the ‘status’ parameter is ’success’, the transaction is successful. If the value of ‘status’ is ‘failure’ or ‘pending’, must be treated as a failed transaction only |
| PG\_Type         | The bankcode (as in Merchant Hosted Checkout integration) of the bank is returned in the parameter.                                                                                                                                                                                                                      |
| key              | This parameter contains the merchant key for the merchant’s account at PayU. It would be the same as the key used while the transaction request is being posted from the merchant’s end to PayU.                                                                                                                         |
| riskactionStr    | This parameter contains risk action (if any) taken on the account holder.                                                                                                                                                                                                                                                |
| addedon          | The transaction timestamp is returned in this parameter.                                                                                                                                                                                                                                                                 |

> 📘 Store **mihpayid** and **txnid** parameter in response:
> 
> PayU recommends you to make provisions to store the **mihpayid** and **txnid** parameter values (in the response) in your server as proof that TPV has been completed for a customer.

> 📘 Note on Response:
> 
> For security reasons, the sample response or URL is not included here.

> 📘 Payment verification:
> 
> PayU recommends you. to verify the transaction details using the **Verification Payment** API. For more information, For API reference, refer to <a href="verify_payment_api" target="_blank">Verify Payment API</a>.