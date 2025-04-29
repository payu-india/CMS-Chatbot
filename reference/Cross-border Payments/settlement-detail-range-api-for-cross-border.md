---
title: Settlement Detail Range API - Cross Border Payments
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
Settlement Details APIs are build on top of settlement data that provides transaction level data for a given date or date range or UTR. These APIs returns paginated response for the given input page and page size.

> 📘 Notes:
> 
> - Use this API for settlement date range where number of settled transactions are not more that 10K. In case if we are having more records, try to use other channel like settlement/billing report or Settlement Dashboard reports to fetch the data.
> - API will perform better if request is coming for single or non parent MID.
> - As timeout is 60 Seconds, try to keep page size not more that 500 and date range a single date (Try to avoid giving end date)

## Request parameters

### Authorization header

- Date: date time when request was triggerd (`Wed, 28 Jun 2023 11:25:19 GMT`)

```
var date = new Date().toUTCString()
```

- Authorisation: a `SHA512` token generated from the current date time, key and salt for the MID. Below is JS function to get the same.

```
var merchant_key = '<key>';
var merchant_secret = '<salt or secret>';
// date
var date = new Date();
// var date = "Wed, 28 Jun 2023 11:25:19 GMT";
date = new Date().toUTCString();
// authorization
var authorization = getAuthHeader(date);
function getAuthHeader(date) {
  var AUTH_TYPE = 'sha512';
  var data = isEmpty(request['data'])?"":request['data'];
  var hash_string = data + '|' + date + '|' + merchant_secret;
  console.log("Hash String is ", hash_string);
  var hash = CryptoJS.SHA512(hash_string).toString(CryptoJS.enc.Hex);
  var authHeader = 'hmac username="' + merchant_key + '", ' + 'algorithm="' + AUTH_TYPE + '", headers="date", signature="' + hash + '"'
  return authHeader;
}
```

### Query parameters

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "dateFrom  \n**mandatory**",
    "0-1": "This parameter must contain from date for the settlement range is required is in YYYY-MM-DD format. ",
    "0-2": "2024-03-26",
    "1-0": "dateTo  \n**optional**",
    "1-1": "This parameter must contain date for the settlement range is required is in YYYY-MM-DD format.   \n**Note**: Date range is cannot be more tha. 3 days, so **dateTo** value must be posted accordingly.",
    "1-2": "2024-03-28",
    "2-0": "pageSize  \n**optional**",
    "2-1": "This parameter must contain the number of records to be paginated on each page is specified in this parameter. By default, the value is 100. ",
    "2-2": "1000",
    "3-0": "page  \n**optional**",
    "3-1": "This parameter must contain the page to be displayed.",
    "3-2": "1"
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


## Sample request/response

### Success scenarios

### Only Start date provided

**Request**

```
curl --location 'https://info.payu.in/settlement/range/?dateFrom=2023-06-20&pageSize=200&page=1' \--header 'Authorization: {{authorization}}' \--header 'Date: {{date}}'
```

**Response**

```
{
    "status": 0,
    "result": {
        "page": 1,
        "size": 2,
        "totalCount": 2,
        "data": [
            {
                "settlementId": "8763692202306200915",
                "settlementCompletedDate": "2023-06-20 11:00:03",
                "settlementAmount": "283079197.97",
                "merchantId": 8763692,
                "utrNumber": "UTIBR72023062000022728",
                "transaction": [
                    {
                        "action": "capture",
                        "payuId": "17577006305",
                        "parentPayuId": "17577001693",
                        "requestId": "12273055103",
                        "transactionAmount": "167334.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "167334.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871992915354836",
                        "mode": "NB",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:38",
                        "requestDate": "2023-06-19 23:59:38",
                        "requestedAmount": "167334.00",
                        "bankName": "SBIB",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    },
                    {
                        "action": "capture",
                        "payuId": "17577005415",
                        "parentPayuId": "17577004788",
                        "requestId": "12273054470",
                        "transactionAmount": "17559.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "17559.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871993385972302",
                        "mode": "UPI",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:22",
                        "requestDate": "2023-06-19 23:59:22",
                        "requestedAmount": "17559.00",
                        "bankName": "INTENT",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    }               ]
            }
        ]
    }
}
```

#### Start and end date provided

**Request**

```
curl --location 'https://info.payu.in/settlement/range/?dateFrom=2023-06-20&dateTo=2023-06-21&pageSize=200&page=1' \--header 'Authorization: {{authorization}}' \--header 'Date: {{date}}'
```

**Response**

```
{
    "status": 0,
    "result": {
        "page": 1,
        "size": 2,
        "totalCount": 2,
        "data": [
            {
                "settlementId": "8763692202306200915",
                "settlementCompletedDate": "2023-06-20 11:00:03",
                "settlementAmount": "283079197.97",
                "merchantId": 8763692,
                "utrNumber": "UTIBR72023062000022728",
                "transaction": [
                    {
                        "action": "capture",
                        "payuId": "17577006305",
                        "parentPayuId": "17577001693",
                        "requestId": "12273055103",
                        "transactionAmount": "167334.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "167334.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871992915354836",
                        "mode": "NB",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:38",
                        "requestDate": "2023-06-19 23:59:38",
                        "requestedAmount": "167334.00",
                        "bankName": "SBIB",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    },
                    {
                        "action": "capture",
                        "payuId": "17577005415",
                        "parentPayuId": "17577004788",
                        "requestId": "12273054470",
                        "transactionAmount": "17559.00",
                        "merchantServiceFee": "0.00000",
                        "merchantServiceTax": "0.00000",
                        "merchantNetAmount": "17559.0",
                        "sgst": "0.00000",
                        "cgst": "0.00000",
                        "igst": "0.00000",
                        "merchantTransactionId": "16871993385972302",
                        "mode": "UPI",
                        "paymentStatus": "captured",
                        "transactionDate": "2023-06-19 23:59:22",
                        "requestDate": "2023-06-19 23:59:22",
                        "requestedAmount": "17559.00",
                        "bankName": "INTENT",
                        "offerServiceFee": "0.00",
                        "offerServiceTax": "0.00",
                        "transferCurrency":"INR",
                        "transactionCurrency":"USD",
                        "forexRate":80.45,
                        "finalSettlement": 20000.45
                    }               ]
            }
        ]
    }
}
```

### Failure scenario responses

#### Invalid response for invalid request: HTTP status 200

```
{
  "message": "Page size can't be more that 50000",
  "status": 1,
  "result": "Page size can't be more that 50000"
}
```

##### Authorization failed: HTTP status 401

```
{
    "message": "Unauthorized"
}
```

## Response parameters

The description of fields in the **data** JSON of the response:

| **Parameter**           | **Fields**                                                                                                                                                                                                   | **Sample Value**                              |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------- |
| settlementId            | This parameter contains a unique settlement ID generated by PayU.                                                                                                                                            | 8763692202306200915                           |
| settlementCompletedDate | This parameter contains settlement completion date.                                                                                                                                                          | 2023-06-20 11:00:03                           |
| settlementAmount        | This parameter contains settlement amount.                                                                                                                                                                   | 10.00                                         |
| merchantId              | This parameter contains a merchant ID that is provided by PayU.                                                                                                                                              | 8763692                                       |
| utrNumber               | This parameter contains an alphanumeric code generated by banks when a transaction is executed. This number serves as a reference code that helps track and identify specific transactions and their status. | UTIBR72023062000022728                        |
| transaction             | This parameter contains the transaction details in a JSON format. For more information, refer to [transaction JSON fields desciption](#transaction-json-fields-description).                                 | Refer to [sample response](#sample-response). |

### transaction JSON fields description

The description of fields in the **transaction** JSON of the response:

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "action",
    "0-1": "This parameter contains the action taken on the transaction. The action can be any of the following:  \n_ capture   \n_ refund   \n_ cancel  \n_ chargeback  \n_ chargeback reversal  \n_ refundreversal",
    "0-2": "refund",
    "1-0": "payuid",
    "1-1": "This parameter contains a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.",
    "1-2": "403993715521937565",
    "2-0": "parentPayuId",
    "2-1": "This parameter contains a parent PayU ID in case of Split Payment transactions.",
    "2-2": "",
    "3-0": "requestid",
    "3-1": "This parameter contains the request ID value posted by the merchant during the transaction request.",
    "3-2": "131278418",
    "4-0": "transactionAmount",
    "4-1": "This parameter contains the original amount which was sent in the transaction request by the merchant.",
    "4-2": "100",
    "5-0": "merchantServiceFee",
    "5-1": "This parameter contains the service fee paid by the merchant to the bank. for the transaction",
    "5-2": "239.6000",
    "6-0": "merchantServiceTax",
    "6-1": "This parameter contains the tax on service fee paid by the merchant to the bank. for the transaction",
    "6-2": "43.1300",
    "7-0": "merchantNetAmount",
    "7-1": "This parameter contains the net amount to be settled by bank to merchant.",
    "7-2": "100",
    "8-0": "merchantTransactionId",
    "8-1": "This parameter contains the transaction ID of the transaction.",
    "8-2": "13818",
    "9-0": "cgst",
    "9-1": "This parameter contains the CGST (Central GST) for the transaction.",
    "9-2": "43.13000",
    "10-0": "igst",
    "10-1": "This parameter contains the IGST (Integrated GST) for the transaction.",
    "10-2": "43.13000",
    "11-0": "sgst",
    "11-1": "This parameter contains the SGST (State GST) for the transaction where the supplier or merchant is from a different state of the customer.",
    "11-2": "43.13000",
    "12-0": "mode",
    "12-1": "This parameter contains the mode of the transaction such as credit card, debit card, etc. For more information, refer to [Payment Mode Codes](doc:payment-mode-codes).",
    "12-2": "CC",
    "13-0": "payemntStatus",
    "13-1": "",
    "13-2": "",
    "14-0": "transactionDate",
    "14-1": "This parameter contains the date of the transaction.",
    "14-2": "2021-08-10 23:46:25",
    "15-0": "requestDate",
    "15-1": "This parameter contains the request date and time stamp.",
    "15-2": "2021-08-10 23:49:16",
    "16-0": "requestedAmount",
    "16-1": "The parameter contains the amount requested by the merchant to the bank.",
    "16-2": "100",
    "17-0": "bankName",
    "17-1": "This parameter contains the bank name or the card type based on the transaction.",
    "17-2": "MAST",
    "18-0": "offerServiceFee",
    "18-1": "This parameter contains the service fee incurred for offer if the transaction involved offer.",
    "18-2": "2",
    "19-0": "offerServiceTax",
    "19-1": "This parameter contains service tax incurred for offer if the transaction involved offer.",
    "19-2": "0.36",
    "20-0": "transferCurrency",
    "20-1": "This parameter contain the currency to which conversion was done.",
    "20-2": "INR",
    "21-0": "transactionCurrency",
    "21-1": "This parameter contain the currency with which transaction was performed.",
    "21-2": "USD",
    "22-0": "forexRate",
    "22-1": "This parameter contain the foreign exchange rate for currency in the **transactionCurrency** to **transactionCurrency** parameter.",
    "22-2": "80.45",
    "23-0": "finalSettlement",
    "23-1": "This parameter contain the final settlement done to merchant.",
    "23-2": "20000.45"
  },
  "cols": 3,
  "rows": 24,
  "align": [
    null,
    null,
    null
  ]
}
[/block]