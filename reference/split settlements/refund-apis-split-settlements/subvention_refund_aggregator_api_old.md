---
title: Subvention Refund for Aggregators API
excerpt: sub ref
api:
  file: payu-biz-aggregator-3.json
  operationId: subventionrefundaggregator
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API will helps in posting only subvention amount refunds. Also, transaction refunds must be initiated beforehand to get these refunds processed. Subvention Refund of the given transaction will not be allowed otherwise.

> 📘 Note:
> 
> Subvention Refunds will only be processed if it is activated on the respective merchant by PayU.

**Environment**

| Test Environment       | &lt;https://test.payu.in/merchant/&gt; |
| :--------------------- | :------------------------------------- |
| Production Environment | &lt;https://info.payu.in/merchant/&gt; |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "key",
    "0-1": "`string` This parameter must contain the merchant key provided by PayU.",
    "0-2": "Your Test Key",
    "1-0": "command",
    "1-1": "`string` command to be used to invoke subvention API for aggregator merchants",
    "1-2": "subvention\\_refund\\_aggregator",
    "2-0": "hash",
    "2-1": "`string`  sha512(key|command|var1|salt)  \nsha512 is the encryption method used here.",
    "2-2": "command",
    "3-0": "var1",
    "3-1": "`string` Parent Payuid",
    "3-2": "8768769869678678",
    "4-0": "var2",
    "4-1": "`string` unique alphanumeric token to distinguish refund",
    "4-2": "PLYH68898398TGHKL",
    "5-0": "var3",
    "5-1": "`string(json)` This parameter contains the refund mode and beneficiary details in the following format:  \n  \n{\"subvention_mode\":3, \"beneficiary_full_name\":\" Nucleus\",\" beneficiary_account_no\":\" 50100002965304\",\" beneficiary_ifsc\":\"HDFC0001626\"}  \n  \nWhere:  \n- **Payout to Account Number** : \"subvention_m ode\":3  \n-** Payout to Internal Cards** : \"subvention_mode\":1",
    "5-2": " ",
    "6-0": "var4",
    "6-1": "`string(json)` This parameters contains the refunds split for each child payuid in the following format:   \n  \n{\"5\\*\\*\\*\\*8\":{\"subventionAmount\":5,\" originalRefundAmount\":1},\"73gAMf\":{\"subventionAmount\":5,\" originalRefundAmount\":3}}  \n  \nWhere,    \n**originalRefundAmount** is the value of the refund that has been fired prior to calling this API.  \n**subventionAmount **is the amount to be deducted from the subvented amount.",
    "6-2": " "
  },
  "cols": 3,
  "rows": 7,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]

The valid values for **subvention\_mode** are listed in the following table:

| **Refund mode** | **Value** | **Description**                |
| --------------- | --------- | ------------------------------ |
| Source          | 1         | Refunds with Normal or to card |
|                 |           |                                |
| UPI             | 2         | Refunds with UPI method        |
| IMPS            | 3         | Refunds with IMPS method       |
| NEFT            | 4         | Refunds with NEFT method       |

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "request\\_id",
    "0-1": "The unique reference number of the refund request is returned in this parameter.",
    "1-0": "subvention-refund\\_status",
    "1-1": "The status of Subvention refund is returned with any of the following:  \n    - **1**: Returns this values if request has been accepted  \n    - **0**: Returns this value if the request is not successful",
    "2-0": "mihpayid",
    "2-1": "The transaction reference number provided by PayU.",
    "3-0": "msg",
    "3-1": "The message statement is returned in this parameter.",
    "4-0": "txn status",
    "4-1": "The current status of the transaction for the given token is returned in this parameter.",
    "5-0": "amount",
    "5-1": "The amount of the transaction for the given token is returned in this parameter."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]

## Sample responses

- When original transaction refunds are not initiated

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":"Please initiate or get
processed the original refund of this
transaction."},"73gAMf":{"subvention_refund_status":0,"msg":"Please
initiate or get processed the original refund of
this transaction."},"mihpayid":"999000000001122"}
```

- When an invalid subvention amount is refunded

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":" Subvention Amount is
invalid"},"73gAMf":{"subvention_refund_status":0,"msg":" Subvention
Amount is invalid"},"mihpayid":"999000000001122"}
```

- Response for successful queued subvention refund

```plaintext
{"5XAPG8":{"subvention_refund_status":1,"msg":"Subvention refund will be
processed.","request_id":"698"},"73gAMf":{"subvention_refund_status":1,"
msg":"Subvention refund will be
processed.","request_id":"699"},"mihpayid":"999000000001122"}
```

- When an invalid subvention mode is requested:

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":"Invalid Subvention Mode
Received"},"73gAMf":{"subvention_refund_status":0,"msg":"Invalid
Subvention Mode
Received"},"mihpayid":"999000000001122"}
```

- When proper beneficiary details are not passed:

```plaintext
{"5XAPG8":{"subvention_refund_status":0,"msg":"Beneficiary details
missing required for Subvention
Refund."},"73gAMf":{"subvention_refund_status":0,"msg":"Beneficiary
details missing required for Subvention
Refund."},"mihpayid":"999000000001122"}
```