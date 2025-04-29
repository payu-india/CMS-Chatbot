---
title: Get Settlement Detail API - Cross Border Payments
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
Settlement Details APIs are build on top of settlement data that provides transaction and adjustment level data for a given date or  UTR.  These APIs returns paginated response for the given input page and page size.

Endpoint

|            |                                                                                                                                            |
| :--------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Production | [\<https://info.payu.intreasury/int/payu/settlement/settlementDetails](https://info.payu.intreasury/int/payu/settlement/settlementDetails) |

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
    "h-0": "Parameter",
    "h-1": "Reference",
    "h-2": "Example",
    "0-0": "settledOn  \n`mandatory`",
    "0-1": "This parameter must either contain either date for the settlement or UTR (Unique Transaction Reference number).",
    "0-2": "2023-09-26",
    "1-0": "isVersion  \n`optional`",
    "1-1": "This parameter must contain the version of the API that can be either 1 or 2.",
    "1-2": "1",
    "2-0": "pageSize  \n`mandatory`",
    "2-1": "This parameter must contain the number of records to be paginated on each page is specified in this parameter. If not specified, 2000 records will be fetched.",
    "2-2": "1000",
    "3-0": "page  \n`mandatory`",
    "3-1": "This parameter must contain the page number to be fetched.",
    "3-2": "5",
    "4-0": "type  \n`optional`",
    "4-1": "This parameter must contain either G to get a detailed output or leave it blank.",
    "4-2": "G"
  },
  "cols": 3,
  "rows": 5,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


<br />

## Sample request/response

### Success scenarios

HTTP status is 200 for all success response

#### Date empty type and version

**Request**

```curl
curl --location 'http://127.0.0.1:8090/treasury/int/payu/settlement/settlementDetails?settledOn=2024-04-08&pageSize=20000&page=1' \
--header 'mid: 135670' \
```

**Response**

```
{
    "rows": 20000,
    "message": "20000 settled on 2024-04-08 ",
    "status": 1,
    "result": [
        {
            "payuid": "19580843982",
            "txnid": "PZT24040523596DQOT01",
            "txndate": "2024-04-05 23:59:49",
            "mode": "CC",
            "amount": "218.00",
            "requestid": "13785835411",
            "requestdate": "2024-04-06 00:00:08",
            "requestaction": "capture",
            "requestamount": "218.00",
            "mer_utr": "UTIBR72024040800086935",
            "mer_service_fee": "3.16000",
            "mer_service_tax": "0.57000",
            "mer_net_amount": "214.27",
            "bank_name": "CC",
            "issuing_bank": "SBI",
            "merchant_subvention_amount": 0.0,
            "cgst": "0.00000",
            "igst": "0.57000",
            "sgst": "0.00000",
            "PG_TYPE": "AxisCYBER",
            "Card Type": "domestic",
            "token": null
        }
]
```

#### Date empty type and version is 2

**Request**

```
curl -X POST "https://test.payu.in/merchant/postservice?form=2
-H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d

"key=JP***g&command=get_settlement_details&var1=2021-08-10&hash=259ded5457ad8d078b3c06294413680d0b9eb341682a4f0eecad17256388c2e096f37f5077480e3a56000cc0a3585f7cd73a7d2d10d8225a05b3b93cd27fd5f8&var2&var3&var4=L&var5=2"
```

**Response**

```
{
    "rows": 50002,
    "message": "50002 transaction settledOn 2024-04-08",
    "status": 1,
    "result": [
        {
            "payuid": "19588035480",
            "txnId": "PZT2404062056KJOM701",
            "txndate": "2024-04-06 20:56:50",
            "mode": "UPI",
            "amount": "188.00",
            "requestid": "13791685328",
            "requestdate": "2024-04-06 20:57:19",
            "requestaction": "capture",
            "requestamount": "188.00",
            "mer_utr": "UTIBR72024040800086935",
            "mer_service_fee": "0.00000",
            "mer_service_tax": "0.00000",
            "mer_net_amount": "188.0",
            "bank_name": "INTENT",
            "issuing_bank": null,
            "merchant_subvention_amount": 0.0,
            "cgst": "0.00000",
            "igst": "0.00000",
            "sgst": "0.00000",
            "PG_TYPE": "AIRTEL UPI ",
            "Card Type": null,
            "token": null,
            "PG": "AIRTEL UPI ",
            "SettlementType": "regular",
            "Scheme": "INTENT",
            "FeeType": "tdrFee",
            "InstantSettlementTDR": "0.00",
            "InstantSettlementTDRTax": "0.00",
            "InstantSettlementTdrType": "",
            "InstantRefundTDR": "0.00",
            "InstantRefundTDRTax": "0.00",
            "InstantRefundTdrType": "",
            "perDayServiceFee": "0.0",
            "perDayServiceTax": "0.0",
            "pricingDays": 1,
            "offerServiceFee": "0.00",
            "offerServiceTax": "0.00"
        },
       {
            "payuid": "ADJ_821142",
            "txnid": "ADJ_821142",
            "txndate": "2024-04-08 02:01:35",
            "mode": "Adjustmentdebit",
            "amount": "-23868.77",
            "requestid": "ADJ_821142",
            "requestdate": "2024-04-08 02:01:35",
            "requestaction": "debit",
            "requestamount": "-23868.77",
            "mer_utr": "UTIBR72024040800086935",
            "mer_service_fee": "-20227.77",
            "mer_service_tax": "-3641.00",
            "mer_net_amount": "-23868.77",
            "bank_name": "",
            "issuing_bank": "",
            "merchant_subvention_amount": "",
            "cgst": 0,
            "sgst": 0,
            "igst": 0,
            "PG_TYPE": "PayU",
            "Card Type": "",
            "token": "",
            "SettlementType": "",
            "PG": "",
            "Scheme": "",
            "FeeType": "",
            "InstantSettlementTDR": "",
            "InstantSettlementTDRTax": "",
            "InstantSettlementTdrType": "",
            "InstantRefundTDR": "",
            "InstantRefundTDRTax": "",
            "InstantRefundTdrType": "",
            "perDayServiceFee": "0.00",
            "perDayServiceTax": "0.00",
            "pricingDays": 1,
            "offerServiceFee": "0.0",
            "offerServiceTax": "0.0"
        }
]
```

#### Date Type G and Version Empty

**Request**

```
curl --location 'http://127.0.0.1:8090/treasury/int/payu/settlement/settlementDetails?settledOn=2024-04-08&type=G&page=1&pageSize=30000' \
```

**Response**

```
{
    "rows": 30000,
    "message": "30000 transaction settledOn 2024-04-08",
    "status": 1,
    "result": [
        {
            "txn_addedon": "2024-04-05 23:59:49",
            "settlement_addedon": "2024-04-06 00:11:12",
            "settledon": "2024-04-08 12:45:07",
            "settlementId": "202404071115",
            "time_zone": "UTC + 05:30",
            "merchant_id": 135670,
            "merchantName": "Flipkart Payments",
            "PSP": "PayU India",
            "action": "capture",
            "txnid": "PZT24040523596DQOT01",
            "payu_id": "19580843982",
            "request_id": "13785835411",
            "settlementUTR": "UTIBR72024040800086935",
            "pg_label": "AxisCYBER",
            "card_bin": 0,
            "Scheme": "VISA",
            "mode": "CC",
            "ibibo_code": "CC",
            "auth_code": "7123418019786142605964",
            "bank_ref_no": "7123418019786142605964",
            "transaction_currency": "INR",
            "settlement_currency": "INR",
            "forexRate":80.45,
            "transaction_amount": 218.0,
            "payu_fee": "-3.16",
            "payu_fee_tax": "-0.57",
            "net_amount": 214.27,
            "ib_title": "SBI",
            "token": null,
            "bank_arn": null,
            "legal_entity": 202437,
            "company_name": "Flipkart Internet Pvt Ltd.",
            "merchant_key": "JP**y",
            "PG_TYPE": "AxisCYBER",
            "Card Type": "domestic"
        }
]
```

#### Date Type G and Version 2

**Request**

```
curl --location 'http://127.0.0.1:8090/treasury/int/payu/settlement/settlementDetails?settledOn=2024-04-08&type=G&isVersion=2&pageSize=30000&page=1' \
--header 'mid: 135670' \
```

**Response**

```
{
    "rows": 30002,
    "message": "30002 transaction settledOnsettledOn",
    "status": 1,
    "result": [
        [
            {
                "txn_addedon": "2024-04-05 23:59:49",
                "settlement_addedon": "2024-04-06 00:11:12",
                "settledon": "2024-04-08 12:45:07",
                "settlementId": "202404071115",
                "time_zone": "UTC + 05:30",
                "merchant_id": 135670,
                "merchantName": "Flipkart Payments",
                "PSP": "PayU India",
                "action": "capture",
                "txnid": "PZT24040523596DQOT01",
                "payu_id": "19580843982",
                "request_id": "13785835411",
                "settlementUTR": "UTIBR72024040800086935",
                "pg_label": "AxisCYBER",
                "card_bin": 0,
                "Scheme": "VISA",
                "mode": "CC",
                "ibibo_code": "CC",
                "auth_code": "7123418019786142605964",
                "bank_ref_no": "7123418019786142605964",
                "transaction_currency": "INR",
                "settlement_currency": "INR",
                "forexRate":80.45,
                "transaction_amount": 218.0,
                "payu_fee": "-3.16",
                "payu_fee_tax": "-0.57",
                "net_amount": 214.27,
                "ib_title": "SBI",
                "token": null,
                "bank_arn": null,
                "legal_entity": 202437,
                "company_name": "Flipkart Internet Pvt Ltd.",
                "merchant_key": "JP**y",
                "PG_TYPE": "AxisCYBER",
                "Card Type": "domestic",
                "SettlementType": "regular",
                "FeeType": "tdrFee",
                "InstantSettlementTDR": "0.00",
                "InstantSettlementTDRTax": "0.00",
                "InstantSettlementTdrType": "",
                "InstantRefundTDR": "0.00",
                "InstantRefundTDRTax": "0.00",
                "InstantRefundTdrType": "",
                "perDayServiceFee": "0.0",
                "perDayServiceTax": "0.0",
                "pricingDays": 1,
                "offerServiceFee": "0.00",
                "offerServiceTax": "0.00"
            },
            {
                "txn_addedon": "2024-04-08 02:01:35",
                "settlement_addedon": "2024-04-07 00:11:12",
                "settledon": "2024-04-08 12:45:07",
                "settlementId": "202404081115",
                "time_zone": "UTC + 05:30",
                "merchant_id": "135670",
                "merchantName": "Flipkart Payments",
                "PSP": "PayU India",
                "action": "debit",
                "txnid": "ADJ_821142",
                "payu_id": "ADJ_821142",
                "request_id": "ADJ_821142",
                "settlementUTR": "UTIBR72024040800086935",
                "pg_label": "",
                "card_bin": "",
                "Scheme": "",
                "mode": "Adjustmentdebit",
                "ibibo_code": "",
                "auth_code": "",
                "bank_ref_no": "",
                "transaction_currency": "INR",
                "settlement_currency": "INR",
                "forexRate":80.45,
                "transaction_amount": "-23868.77",
                "payu_fee": "-20227.77",
                "payu_fee_tax": "-3641.00",
                "net_amount": "-23868.77",
                "ib_title": "",
                "token": "",
                "bank_arn": "",
                "legal_entity": "202437",
                "company_name": "Flipkart Internet Pvt Ltd.",
                "merchant_key": "BmzsVc",
                "PG_TYPE": "PayU",
                "Card Type": "",
                "SettlementType": "",
                "FeeType": "",
                "InstantSettlementTDR": "",
                "InstantSettlementTDRTax": "",
                "InstantSettlementTdrType": "",
                "InstantRefundTDR": "",
                "InstantRefundTDRTax": "",
                "InstantRefundTdrType": "",
                "perDayServiceFee": "20227.77",
                "perDayServiceTax": "3641.0",
                "pricingDays": "1",
                "offerServiceFee": "0.0",
                "offerServiceTax": "0.0"
            }

```

### Failure scenarios

- Invalid Response (Bad Request): HTTP status 401

```
{
    "rows": 0,
    "message": "Please check date format it should be YYYY-MM-DD or utr format which should be alphanumeric",
    "status": 0,
    "result": "validation failed"
}
```

## Response parameters description

### result JSON fields description

[block:parameters]
{
  "data": {
    "h-0": "**Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "txn\\_addedon",
    "0-1": "This parameter contains the transaction added date.",
    "0-2": " 2024-04-05 23:59:49",
    "1-0": "settlement\\_addedon",
    "1-1": "This parameter contains the settlement added date.",
    "1-2": " 2024-04-06 00:11:12",
    "2-0": "settledon",
    "2-1": "This parameter contains the date when the settled on.",
    "2-2": " 2024-04-08 12:45:07",
    "3-0": "settlementId",
    "3-1": "This parameter contains the settlement ID.",
    "3-2": " 202404071115",
    "4-0": "time\\_zone",
    "4-1": "This parameter contains the time zone in which the transaction was perform.",
    "4-2": " UTC + 05:30",
    "5-0": "merchant\\_id",
    "5-1": "This parameter contains the merchant ID.",
    "5-2": " JP\\*\\*\\*g",
    "6-0": "merchantName",
    "6-1": "This parameter contains the merchant name.",
    "6-2": " ABC company",
    "7-0": "PSP",
    "7-1": "This parameter contains the payment service provider.",
    "7-2": " PayU",
    "8-0": "action",
    "8-1": "This parameter contains the action taken on the transaction. The action can be any of the following:  \ncapture   \nrefund   \ncancel  \nchargeback  \nchargeback reversal  \nrefundreversal",
    "8-2": "capture",
    "9-0": "txnid",
    "9-1": "This parameter contains the transaction ID.",
    "9-2": " PZT24040523596DQOT01",
    "10-0": "payu\\_id",
    "10-1": "This parameter contains a unique reference number created for each transaction at PayU’s end. You must note this transaction ID as this will be used as a reference for all the future actions on this transaction like Inquiry or Refund.",
    "10-2": "403993715521937565",
    "11-0": "request\\_id",
    "11-1": "This parameter contains the request ID value posted by the merchant during the transaction request.",
    "11-2": "131278418",
    "12-0": "settlementUTR",
    "12-1": "This parameter contains the unique number generated by the bank to identify a settlement and track the amounts settled. A UTR is a 12-digit alphanumeric code that is assigned to each electronic transaction.",
    "12-2": "UTIBR72024040800086935",
    "13-0": "pg\\_label",
    "13-1": "This parameter contains the payment gateway used.",
    "13-2": "AxisCYBER",
    "14-0": "card\\_bin",
    "14-1": "This parameter contains the card BIN.",
    "14-2": " ",
    "15-0": "Scheme",
    "15-1": "This parameter contains the card scheme.",
    "15-2": "VISA",
    "16-0": "mode",
    "16-1": "This parameter contains the payment mode used.",
    "16-2": "CC",
    "17-0": "ibibo\\_code",
    "17-1": "This parameter contains the bank code.",
    "17-2": "CC",
    "18-0": "auth\\_code",
    "18-1": "This parameter contains the authorization code.",
    "18-2": "7123418019786142605964",
    "19-0": "bank\\_ref\\_no",
    "19-1": "This parameter contains the bank reference number.",
    "19-2": "7123418019786142605964",
    "20-0": "transaction\\_amount",
    "20-1": "This parameter contains the original amount which was sent in the transaction request by the merchant.",
    "20-2": "100",
    "21-0": "transfer\\_currency",
    "21-1": "This parameter contain the currency to which conversion was done.",
    "21-2": "INR",
    "22-0": "transaction\\_currency",
    "22-1": "This parameter contain the currency with which transaction was performed.",
    "22-2": "USD",
    "23-0": "forexRate",
    "23-1": "This parameter contain the foreign exchange rate for currency in the **transactionCurrency** to **transactionCurrency** parameter.",
    "23-2": "80.45",
    "24-0": "finalSettlement",
    "24-1": "This parameter contain the final settlement done to merchant.",
    "24-2": "20000.45",
    "25-0": "payu\\_fee",
    "25-1": "This parameter contains the PayU fee for this transaction.",
    "25-2": "\\-3.16",
    "26-0": "payu\\_fee\\_tax",
    "26-1": "This parameter contains the tax incurred for PayU fee.",
    "26-2": "\\-0.57",
    "27-0": "net\\_amount",
    "27-1": "This parameter contains the net amount paid to merchant.",
    "27-2": "214.27",
    "28-0": "ib\\_title",
    "28-1": "This parameter contains the bank code.",
    "28-2": "SBI",
    "29-0": "token",
    "29-1": "This parameter contains the saved card token (if any).",
    "29-2": " ",
    "30-0": "bank\\_arn",
    "30-1": "This parameter contains the unique number assigned to a credit or debit card transaction that helps banks and other parties track the transaction.",
    "30-2": " ",
    "31-0": "legal\\_entity",
    "31-1": "This parameter contains the legal entity number.",
    "31-2": "202437",
    "32-0": "company\\_name",
    "32-1": "This parameter contains the company name of the merchant.",
    "32-2": " ",
    "33-0": "merchant\\_key",
    "33-1": "This parameter contains the merchant key.",
    "33-2": " ",
    "34-0": "PG\\_TYPE",
    "34-1": "This parameter contains the PG type.",
    "34-2": "AxisCYBER",
    "35-0": "Card Type",
    "35-1": "This parameter contains whether card type is domestic or international.",
    "35-2": "domestic"
  },
  "cols": 3,
  "rows": 36,
  "align": [
    null,
    null,
    null
  ]
}
[/block]