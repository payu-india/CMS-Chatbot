---
title: Additional Info for Payouts APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
## Request parameters for Initiate Transfer API

[block:parameters]
{
  "data": {
    "h-0": "**Parameters**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "batchId`\nmandatory`",
    "0-1": "`String`It can be any string value. Merchants can use this value if they want to process the request in batch and also what status of transfer in batch. This can be unique for a batch or across multiple requests.  \n**Max char length**: 40.",
    "0-2": " ",
    "1-0": "amount`\nmandatory`",
    "1-1": "`Double`Indicates Amount to transfer to the beneficiary account",
    "1-2": " ",
    "2-0": "merchantRefId`\noptional`",
    "2-1": "`String`Indicates a unique reference ID at the merchant side to distinguish between multiple transfers.  \n**Max char length**: 40.  \n**Notes** :  \n   - Same value will be used by the merchant in the status check of transfer.  \n   - In case if the merchant reference ID is not passed, an auto generated ID will be used.",
    "2-2": " ",
    "3-0": "beneficiaryAccountNumber`\nmandatory in case of IMPS, NEFT and RTGS transactions otherwise Conditional`",
    "3-1": "`String` Indicates beneficiary account number to transfer money.  \n**Min Character**: 9\\*\\*  \n**Max Character**: 35",
    "3-2": " ",
    "4-0": "beneficiaryIfscCode `\nmandatory in case of IMPS, NEFT and RTGS transactions otherwise Conditional`",
    "4-1": "`String` Indicates IFSC Code of the Beneficiary Bank Account.",
    "4-2": "",
    "5-0": "beneficiaryName  \n`mandatory`",
    "5-1": "`String` Indicates name of the Beneficiary of the Beneficiary associated with Bank Account",
    "5-2": " ",
    "6-0": "beneficiaryMobile  \n`optional`",
    "6-1": "`String` Indicates Beneficiary mobile number",
    "6-2": " ",
    "7-0": "beneficiaryEmail  \n`optional`",
    "7-1": "`String` Indicates Beneficiary Email Address",
    "7-2": " ",
    "8-0": "purpose  \n`mandatory`",
    "8-1": "`String` This parameter must include the purpose of doing this transfer.  \n**Note**: Only alphanumeric characters are allowed.",
    "8-2": " ",
    "9-0": "paymentType  \n`mandatory`",
    "9-1": "`String` Specify the any of the following mode of payment in this field:  \n   - IMPS  \n   - UPI  \n   - NEFT  \n   - RTGS  \n   - MASTERCARD  \n   - VISA  \n   - CC_PAYMENT",
    "9-2": "MASTERCARD",
    "10-0": "vpa `\nmandatory in case of UPI transactions otherwise Conditional`",
    "10-1": "`String` Indicates VPA (UPI) address of Beneficiary.",
    "10-2": " ",
    "11-0": "retry  \n`mandatory`",
    "11-1": "`String`Specify the flag as either True or False to indicate whether to retry transfer or not in this field:  \n    - **true**: Specifies that retry the payment.  \n   - **false**: Specifies that do not retry the payment.  \n  \n**Note**: Default value for this will be false.",
    "11-2": "",
    "12-0": "scheduledTime  \n `optional`",
    "12-1": "`Date` Specify the date and time on which Payout scheduled in this field.  \n**Example**: 2020-10-20 15:02:11",
    "12-2": "2020-10-20 15:02:11",
    "13-0": "recipientCardNo  \n `optional`",
    "13-1": "`String`The Credit Card Number with which the payment is made by your customer is specified in this field.",
    "13-2": "",
    "14-0": "beneficiaryId  \n`conditional`",
    "14-1": "`Long` Id of beneficiary to which the payout needs to be done. This value can be passed instead of other beneficiary details.",
    "14-2": " ",
    "15-0": "vpaToken  \n `mandatory for UPI`",
    "15-1": "`String` VPA token corresponding to VPA(UPI) address of beneficiary.",
    "15-2": " ",
    "16-0": "custom1  \n`optional`",
    "16-1": "`String` This is custom parameter. No processing is done from payU side and can be used by you to pass any information they want in the reports for the transactions. Only 50 characters are allowed in this field.",
    "16-2": " ",
    "17-0": "custom2  \n`optional`",
    "17-1": "`String` This is custom parameter. No processing is done from payU side and can be used by you to pass any information they want in the reports for the transactions. Only 50 characters are allowed in this field.",
    "17-2": "",
    "18-0": "custom3  \n`optional`",
    "18-1": "`String` This is custom parameter. No processing is done from payU side and can be used by you to pass any information they want in the reports for the transactions. Only 50 characters are allowed in this field.",
    "18-2": ""
  },
  "cols": 3,
  "rows": 19,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


### Sample Request

#### IMPS, NEFT or RTGS Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For IMPS/NEFT/RTGS","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryAccountNumber\": \"51234567890\",\n \"beneficiaryIfscCode\": \"HDFC0001234\",\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"123asdfad3\",\n \"paymentType\": \"IMPS\",\n \"retry\" : false\n }\n]"},"isInline":true}
```

#### UPI Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For UPI Payment","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"123\",\n \"paymentType\": \"UPI\",\n \"vpa\" : \"ankush.pokarana@ybl\"\n \"retry\" : false\n }\n]"},"isInline":true}
```

#### MasterCard Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For MasterCard payment","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"1234\",\n \"paymentType\": \"MASTERCARD\",\n \"recipientCardNo\":\"5291170702832\"\n }\n]"},"isInline":true}
```

#### VISA Card Payment Request

```curl
{"callType":"Request","requestTitle":"Request Body For VISA card payment","requestType":"Get","requests":{"bash":"[\n {\n \"beneficiaryName\": \"Payu\",\n \"beneficiaryEmail\": \"payu@payu.in\",\n \"beneficiaryMobile\": \"9876473627\",\n \"purpose\": \"Payment from Company\",\n \"amount\": 1234.12,\n \"batchId\": \"1\",\n \"merchantRefId\": \"1234\",\n \"paymentType\": \"VISA\",\n \"recipientCardNo\":\"4012888888881882\"\n }\n]"},"isInline":true}
```

### Sample Response

- Success response

```plaintext
{"callType":"Response","responseTitle":"Sample Success Response","response":"{\n \"status\": 0,\n \"msg\": \"Requests are in process. Will send response of individual request on webhooks set by you\",\n \"code\": null,\n \"data\": []\n }","isInline":true}
```

- Failure response

````plaintext
{"callType":"Response","responseTitle":"Sample Failure Response","response":"{\n \"status\": 1,\n \"msg\": null,\n \"code\": null,\n \"data\": [\n {\n \"batchId\": \"1\",\n \"merchantRefId\": \"111\",\n \"error\": \"beneficiary account number can not be empty. \",\n \"code\": [1004]\n }\n ]\n }","isInline":true}
```plaintext

 
````

## Request Parameters in Check Transfer Status API

### Transfer Status

<table><tbody><tr><td>QUEUED/SHEDULED</td><td>It will be first state once we get transaction request from merchant.</td></tr><tr><td>IN_PROGRESS</td><td>This is an intermediary stage and can also come if merchant is not having enough balance in his virtual account.</td></tr><tr><td>PENDING</td><td>PayU has received pending status from bank.</td></tr><tr><td>FAILED</td><td>Final status will be updated once PayU get success or failure from bank.</td></tr></tbody></table>

The Status of a particular Transaction has to be determined Only from the field **txnStatus** in `transactionDetails` JSON against the `merchantRefId`.

On receiving the following JSON Response in the **Check Transfer Status** API, the transaction status is not determined and has to considered as unidentified or Pending by merchant.

```
{
    "status": 0,
    "msg": null,
    "code": null,
    "data": {
        "payoutMerchantId": null,
        "noOfPages": 0,
        "totalElements": 0,
        "currentPage": 0,
        "totalAmount": 0.0,
        "succesTxn": 0,
        "pendingTxn": 0,
        "transactionDetails": []
    }
}
```

## Headers and request parameters

> 📘 Note