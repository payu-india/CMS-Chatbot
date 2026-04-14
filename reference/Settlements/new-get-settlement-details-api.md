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
result JSON Fields Description

| Field | Description | Example |
|---|---|---|
| txn_addedon | Timestamp when the transaction was added to the system. <code>string</code> | 2024-04-05 23:59:49 |
| settlement_addedon | Timestamp when the settlement was initiated. <code>string</code> | 2024-04-06 00:11:12 |
| settledon | Timestamp when the settlement was completed. <code>string</code> | 2024-04-08 12:45:07 |
| settlementId | Unique identifier for the settlement batch. <code>string</code> | 202404071115 |
| time_zone | Timezone used for the transaction timestamps. <code>string</code> | UTC + 05:30 |
| merchant_id | Unique identifier for the merchant account. <code>integer</code> | 135670 |
| merchantName | Display name of the merchant. <code>string</code> | Flipkart Payments |
| PSP | Payment Service Provider name. <code>string</code> | PayU India |
| action | Action performed on the transaction (capture, refund, etc.). <code>string</code> | capture |
| txnid | Unique transaction identifier provided by merchant. <code>string</code> | PZT24040523596DQOT01 |
| payu_id | PayU internal transaction identifier. <code>string</code> | 19580843982 |
| request_id | Unique request identifier for tracking. <code>string</code> | 13785835411 |
| settlementUTR | Unique Transaction Reference number for settlement. <code>string</code> | UTIBR72024040800086935 |
| pg_label | Payment gateway label/identifier. <code>string</code> | AxisCYBER |
| card_bin | Bank Identification Number of the card. <code>integer</code> | 0 |
| Scheme | Card scheme (VISA, MasterCard, etc.). <code>string</code> | VISA |
| mode | Payment mode (CC for Credit Card, DC for Debit Card, etc.). <code>string</code> | CC |
| ibibo_code | Internal payment method code. <code>string</code> | CC |
| auth_code | Authorization code from the bank. <code>string</code> | 7123418019786142605964 |
| bank_ref_no | Bank reference number for the transaction. <code>string</code> | 7123418019786142605964 |
| transaction_currency | Currency code for the transaction. <code>string</code> | INR |
| settlement_currency | Currency code for the settlement. <code>string</code> | INR |
| fx_rate | Foreign exchange rate applied. <code>string</code> | 20.00 |
| additional_service_fee | Additional service charges applied. <code>string</code> | 0.00 |
| additional_service_tax | Tax on additional services. <code>string</code> | 0.00 |
| discount | Discount amount applied to the transaction. <code>string</code> | 0.00 |
| udf2 | User defined field 2 for custom data. <code>string</code> |  |
| total_service_tax | Total service tax amount. <code>string</code> | 0.00000 |
| total_processing_fee | Total processing fee charged. <code>string</code> | 0.00000 |
| transaction_amount | Original transaction amount. <code>decimal</code> | 218.0 |
| payu_fee | PayU processing fee (negative indicates deduction). <code>string</code> | -3.16 |
| payu_fee_tax | Tax on PayU processing fee. <code>string</code> | -0.57 |
| net_amount | Final amount after deducting fees and taxes. <code>decimal</code> | 214.27 |
| ib_title | Issuing bank title/name. <code>string</code> | SBI |
| token | Token for saved card details. <code>string</code> | null |
| bank_arn | Bank Acquirer Reference Number. <code>string</code> | null |
| legal_entity | Legal entity identifier for the merchant. <code>integer</code> | 202437 |
| company_name | Legal company name of the merchant. <code>string</code> | Flipkart Internet Pvt Ltd. |
| merchant_key | Merchant's secret key identifier. <code>string</code> | BmzsVc |
| PG_TYPE | Payment gateway type/processor. <code>string</code> | AxisCYBER |
| Card Type | Type of card used (domestic/international). <code>string</code> | domestic |


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