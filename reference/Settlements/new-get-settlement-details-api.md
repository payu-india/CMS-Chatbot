---
title: '[NEW] Get Settlement Details API'
deprecated: false
hidden: true
metadata:
  title: Get Settlement Details API
  description: >-
    This document provides information on using an API to retrieve settlement
    details from a bank based on a specified date or Unique Transaction
    Reference number. The API can be posted with version 1 or 2 parameters.
  robots: index
---
---
title: '[NEW] Get Settlement Details API'
deprecated: false
hidden: true
metadata:
  title: Get Settlement Details API
  description: >-
    This document provides information on using an API to retrieve settlement
    details from a bank based on a specified date or Unique Transaction
    Reference number. The API can be posted with version 1 or 2 parameters.
  robots: index
---

***

You can use the **Get Settlement Details** API to retrieve settlement details which the bank has to settle for you. The input is the date for which settlement details are required, where the var1 parameter is the date you want to know the settlement status or UTR (Unique Transaction Reference number). This API can be posted with version (1 or 2) in the var5 parameter.

<br />

## Environment

| Environment            | URL                                                                                                        |
| :--------------------- | :--------------------------------------------------------------------------------------------------------- |
| Test Environment       | [https://apitest.payu.in/merchant/postservice?form=2](https://apitest.payu.in/merchant/postservice?form=2) |
| Production Environment | [https://info.payu.in/merchant/postservice?form=2](https://info.payu.in/merchant/postservice?form=2)       |

## Request Parameters

### Header Parameters

<HeaderAuthentication />

### Query Parameters

| Parameter                             | Description                                                                                     | Example    |
| ------------------------------------- | ----------------------------------------------------------------------------------------------- | ---------- |
| settledOn<br /><code>mandatory</code> | <code>String</code> Settlement date in YYYY-MM-DD format or UTR (Unique Transaction Reference). | 2023-09-26 |
| type<br /><code>optional</code>       | <code>String</code> Settlement type. Allowed values: "G" or blank.                              | G          |
| isVersion<br /><code>mandatory</code> | <code>Integer</code> API version (1 or 2). Version 2 returns enriched fields.                   | 2          |
| page<br /><code>mandatory</code>      | <code>Integer</code> Page number for pagination.                                                | 1          |
| pageSize<br /><code>mandatory</code>  | <code>Integer</code> Number of records per page. Min: 2000, Max: 50000.                         | 5000       |

## Sample Request

### Version 1 for Standard Response

```curl
curl -X GET "https://apitest.payu.in/merchant/postservice?form=2&settledOn=2023-09-26&isVersion=1&page=1&pageSize=5000" \
  --header 'Authorization: {{authorization}}' \
  --header 'Date: {{date}}'
```

### Version 1 with type=G

```curl
curl --location "https://apitest.payu.in/merchant/postservice?form=2?settledOn=2024-04-08&type=G&page=1&pageSize=30000" \
  --header 'Authorization: {{authorization}}' \
  --header 'Date: {{date}}'
```

### Version 2 for a Detailed Response

```curl
curl -X GET "https://apitest.payu.in/merchant/postservice?form=2&settledOn=2023-09-26&type=G&isVersion=2&page=1&pageSize=5000" \
  --header 'Authorization: {{authorization}}' \
  --header 'Date: {{date}}'
```

## Response Parameters

| Parameter    | Description                                                 | Example              |
| ------------ | ----------------------------------------------------------- | -------------------- |
| txnid        | Transaction ID. Type: <code>string</code>                   | TXN123456            |
| amount       | Transaction amount. Type: <code>decimal</code>              | 100.00               |
| payu_fee     | PayU processing fee. Type: <code>decimal</code>             | 2.50                 |
| payu_fee_tax | Tax on PayU fee. Type: <code>decimal</code>                 | 0.45                 |
| net_amount   | Net amount after fees and taxes. Type: <code>decimal</code> | 97.05                |
| status       | Transaction status. Type: <code>string</code>               | success              |
| utr          | Unique Transaction Reference. Type: <code>string</code>     | UTR123456789         |
| settled_at   | Settlement timestamp. Type: <code>string</code>             | 2023-09-26T10:30:00Z |

## Sample Response

### Success Response

#### Version 1

```json
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

### Version 1 with type=G

```json
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
            "fx_rate": "20.00",
            "additional_service_fee": "0.00",
            "additional_service_tax": "0.00",
            "discount": "0.00",
            "udf2": "",
            "total_service_tax": "0.00000",
            "total_processing_fee": "0.00000",
            "transaction_amount": 218.0,
            "payu_fee": "-3.16",
            "payu_fee_tax": "-0.57",
            "net_amount": 214.27,
            "ib_title": "SBI",
            "token": null,
            "bank_arn": null,
            "legal_entity": 202437,
            "company_name": "Flipkart Internet Pvt Ltd.",
            "merchant_key": "BmzsVc",
            "PG_TYPE": "AxisCYBER",
            "Card Type": "domestic"
        }
]
```

#### Version 2

```json
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

### Failure Scenario

#### Invalid Date Format

```json
{
  "status": 0,
  "message": "Invalid date format. Please use YYYY-MM-DD format.",
  "result": null
}
```

For Error Codes, refer to [PayU Error Codes](https://docs.payu.in/docs/error-codes).