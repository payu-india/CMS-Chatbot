---
title: Settlement Reconciliation API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API reconciles the settlements for a given parent mid and specified period (date range).

HTTP Method: **POST**

**Environment**

|                        |                                  |
| :--------------------- | :------------------------------- |
| Test Environment       | <https://test.payu.in/merchant/> |
| Production Environment | <https://info.payu.in/merchant/> |

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "Merchant key  \n**mandatory**",
    "0-1": "`varchar` The merchant key is included in this parameter.",
    "0-2": "Your Test Key",
    "1-0": "command  \n**mandatory**",
    "1-1": "`varchar` The API command name **get\\_settlement\\_details\\_range** must be included in this parameter.",
    "1-2": "get\\_settlement\\_details\\_range",
    "2-0": "hash  \n**mandatory**",
    "2-1": "`varchar` The hash string encryption is specified in this parameter. The format of the hash is:  \n`string key\\|command\\|var1\\|salt  \n`Where var1 is the date is the date range.",
    "2-2": "string tXjTgO",
    "3-0": "var1: datefrom  \n**mandatory**",
    "3-1": "`varchar` The parameter contains the date on which the range starts or particular date.",
    "3-2": "2022-08-22",
    "4-0": "var2: dateTo  \n**optional**",
    "4-1": "`varchar` The parameter contains the end date until which the statement is required.",
    "4-2": "2022-08-25",
    "5-0": " var3: aggregator  \n**optional**",
    "5-1": "`boolean` This parameter can contain any of the following values:  \n- **true**: It will return the information of the children as well.  \n- **false**: It will return the information of the parent only.",
    "5-2": "true",
    "6-0": "var4: page  \n**optional**",
    "6-1": " `integer`This parameter can include the page number that is used if the API returns several pages as a result ",
    "6-2": "2"
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


## Sample request

```curl
curl -X POST "https://info.payu.in/merchant/postservice?form=2"
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d
"key=JP***g&command=get_settlement_details_range&var1=2022-07-23&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8var2=2021-08-12"
```

## Response parameters

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "rows",
    "0-1": "The number of rows returned.",
    "0-2": "2",
    "1-0": "message",
    "1-1": "The summary of the response that includes the number of settlements and date of them.",
    "1-2": "2 Settlements found for the 2022-07-23T00:00 and 2022-07-26T23:59:59.999999999",
    "2-0": "status",
    "2-1": "This response can contain any of the following:  \n   - **1** if API call is a success  \n   - **0** in case of failure you'll get system handled failure reasons in this case",
    "2-2": "1",
    "3-0": "result",
    "3-1": "This parameter contains the settlements in a JSON format. For detailed information, refer to [result JSON Fields Description](#resul-json-fields-description).",
    "3-2": " Refer to [Sample Response](#sample_response)",
    "4-0": "guid",
    "4-1": " This parameter contains the geographically unique ID of the transaction.",
    "4-2": "",
    "5-0": "sessionId",
    "5-1": " This parameter contains the session ID of the transaction",
    "5-2": "",
    "6-0": "errorCode",
    "6-1": "This parameter contains the error code if the transaction had failed. The error can be any of the following: | Please pass valid merchant key",
    "6-2": ""
  },
  "cols": 3,
  "rows": 7,
  "align": [
    null,
    null,
    null
  ]
}
[/block]




### result JSON fields description

The **result** parameter contains the following fields in a JSON format:

| **Field**               | **Description**                                                                                                                                                           | **Example**                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| settlementId            | This field contains the settlement ID                                                                                                                                     | 8599910202207241245                          |
| settlementCompletedDate | This field contains the settlement completion date and time.                                                                                                              | 2022-07-23 17:35:06                          |
| settlementAmount        | This field contains the settlement amount to the child merchant.                                                                                                          | 122185.00                                    |
| merchantId              | This field contains the child merchant ID.                                                                                                                                | 8599910                                      |
| utrNumber               | This field contains the merchant Unique Transaction Reference (UTR) number.                                                                                               | ijklmn                                       |
| transaction             | This field contains the transaction details in a JSON format. For more information, refer to [transaction JSON Fields Description](#transaction_json-fields-description). | Refer to [Sample Response](#sample_response) |
| utrnumber               | This field contains the unique transaction number of the transaction.                                                                                                     | 123456                                       |

### transaction JSON fields description

The **transaction** field contains the following fields in a JSON format:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "action",
    "0-1": "This field contains the purpose of the transaction. This field can contain any of the following values:  \n- Capture  \n- Adjustment_credit  \n- Adjustment_debit  \n- Refund  \n- Failed",
    "0-2": "Adjustment\\_credit",
    "1-0": "payuId",
    "1-1": "This field contains the PayU ID of the child merchant.",
    "1-2": "ADJ122538",
    "2-0": "transactionAmount",
    "2-1": "This field contains the transaction amount that needs to be settled.",
    "2-2": "6942.00",
    "3-0": "merchantServiceFee",
    "3-1": "This field contains the merchant service fee.",
    "3-2": "8.0000",
    "4-0": "merchantServiceTax",
    "4-1": "This field contains merchant service tax.",
    "4-2": "8.0000",
    "5-0": "merchantNetAmount",
    "5-1": "This field contains the net amount settled to the merchant.",
    "5-2": " ",
    "6-0": "cgst",
    "6-1": "This field contains the CGST amount part of the transaction.",
    "6-2": " ",
    "7-0": "igst",
    "7-1": "This field contains the IGST amount pat of the transation",
    "7-2": " ",
    "8-0": "transactionsgst",
    "8-1": "This field contains the SGST part of the transaction",
    "8-2": " ",
    "9-0": "merchantTransactionId",
    "9-1": "This field contains the merchant transaction ID",
    "9-2": "ADJ122538",
    "10-0": "<h3>For Adjustment Status Transactions</h3>",
    "10-1": "",
    "10-2": "",
    "11-0": "adjustmentType",
    "11-1": "This field contains the adjustment type",
    "11-2": "credit",
    "12-0": "referenceId",
    "12-1": "This field contains the reference ID.",
    "12-2": "1",
    "13-0": "blockType",
    "13-1": "This field contains the block type.",
    "13-2": " ",
    "14-0": "adjustmentAction",
    "14-1": " ",
    "14-2": "TDR Adjustment",
    "15-0": "<h3>For Adjustment Credit Status Transactions</h3>",
    "15-1": "",
    "15-2": "",
    "16-0": "mode",
    "16-1": "This field contains the payment mode for the tranaction.",
    "16-2": "credit",
    "17-0": "cardType",
    "17-1": "This field contains the card type used for the transaction.",
    "17-2": " ",
    "18-0": "paymentStatus",
    "18-1": "This field contains the payment status to the child merchant.",
    "18-2": "inProgress",
    "19-0": "transactionDate",
    "19-1": "This field contains the transaction date and time.",
    "19-2": "2022-07-23 01:45:43",
    "20-0": "requestedAmount",
    "20-1": "This field contains the amount requested by the child merchant.",
    "20-2": "6942.00",
    "21-0": "requestDate",
    "21-1": "This field contains the date when the child merchant requested the amount.",
    "21-2": "2022-07-23 01:45:43",
    "22-0": "bankName",
    "22-1": "This field contains the bank involved in card, Net Banking or UPI transaction.",
    "22-2": " ",
    "23-0": "token",
    "23-1": "This field contains the card token if the card is tokenised.",
    "23-2": " ",
    "24-0": "<h3>For Refund Status Transactions</h3>",
    "24-1": "",
    "24-2": "",
    "25-0": "paymentId",
    "25-1": "This field contains the payment ID of the transaction.",
    "25-2": "58871981",
    "26-0": "refundStatus",
    "26-1": "This field contains the refund status",
    "26-2": "refundinprogress",
    "27-0": "paymentAddedOn",
    "27-1": "This field contains the date when the payment was added on.",
    "27-2": "2017-12-08",
    "28-0": "paymentAmount",
    "28-1": "This field contains the payment amount.",
    "28-2": "200.00",
    "29-0": "saleAmount",
    "29-1": "This field contains the original sale amount.",
    "29-2": "200.00"
  },
  "cols": 3,
  "rows": 30,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


## Sample response

```plaintext
{
  "rows": 2,
  "message": "2 Settlements found for the 2022-07-23T00:00 and 2022-07-26T23:59:59.999999999",
  "status": 1,
  "result": [
    {
      "settlementId": "8599910202207241245",
      "settlementCompletedDate": "2022-07-23 17:35:06",
      "settlementAmount": "122185.00",
      "merchantId": 8599910,
      "utrNumber": "ijklmn",
      "transaction": [
        {
          "action": "Adjustment_credit",
          "payuId": "ADJ122538",
          "transactionAmount": "6942.00",
          "merchantNetAmount": "",
          "cgst": "",
          "igst": "",
          "sgst": "",
          "merchantTransactionId": "ADJ122538",
          "mode": "credit",
          "cardType": "",
          "paymentStatus": "inProgress",
          "transactionDate": "2022-07-23 01:45:43",
          "requestedAmount": "6942.00",
          "requestDate": "2022-07-23 01:45:43",
          "bankName": "",
          "token": ""
        }
      ]
    },
    {
      "settlementId": "8597923202207251245",
      "settlementCompletedDate": "2022-07-23 17:40:06",
      "settlementAmount": "18.88",
      "merchantId": 8593059,
      "utrNumber": "abcdef",
      "transaction": [
        {
          "action": "capture",
          "payuId": "15553396797",
          "parentPayuId": "15553211345",
          "requestId": "10801247706",
          "transactionAmount": "4.72",
          "merchantServiceFee": "8.0000",
          "merchantServiceTax": "8.0000",
          "merchantNetAmount": "4.7200",
          "cgst": "0.00000",
          "igst": "1.44000",
          "sgst": "0.00000",
          "merchantTransactionId": "216245453",
          "paymentStatus": "captured",
          "transactionDate": "2022-07-23 10:15:43",
          "requestedAmount": "14.16",
          "requestDate": "2022-07-23 10:15:38",
          "bankName": "IDBB"
        },
        {
          "action": "capture",
          "payuId": "15553398000",
          "parentPayuId": "15553287497",
          "requestId": "10801248633",
          "transactionAmount": "4.72",
          "merchantServiceFee": "8.0000",
          "merchantServiceTax": "8.0000",
          "merchantNetAmount": "4.7200",
          "cgst": "0.00000",
          "igst": "1.44000",
          "sgst": "0.00000",
          "merchantTransactionId": "216249103",
          "paymentStatus": "captured",
          "transactionDate": "2022-07-23 10:15:53",
          "requestedAmount": "14.16",
          "requestDate": "2022-07-23 10:15:48",
          "bankName": "BOIB"
        }
      ]
    }
  ]
}

```