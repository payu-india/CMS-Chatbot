---
title: '[NEW]Settlement Detail Range API'
deprecated: false
hidden: true
metadata:
  title: Settlement Detail Range API
  keywords:
    - Settlement Detail Range API
    - Merchant settlement range details API
    - Retrieve settlement range details API
    - API for transaction settlement range
  robots: index
---
---
title: Settlement Detail Range API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Settlement Detail Range API
  description: ''
  keywords:
    - Settlement Detail Range API
    - Merchant settlement range details API
    - Retrieve settlement range details API
    - API for transaction settlement range
  robots: index
next:
  description: ''
---

Settlement Details Range API provides transaction level data for a given date or date range. This API returns paginated response for the given input page and page size.

**Environment**

|                        |                                                                                      |
| :--------------------- | :----------------------------------------------------------------------------------- |
| Test Environment       | [https://apitest.payu.in/settlement/range](https://apitest.payu.in/settlement/range) |
| Production Environment | [https://info.payu.in/settlement/range](https://info.payu.in/settlement/range)       |

<Callout icon="📘" theme="info">
  **Note**: Use the endpoint as per above [https://\<environment base URL>/settlement/range](https://apitest.payu.in/settlement/range) and do not append slash (/) at the end of it.
</Callout>

## Request Parameters

### Header Parameters

<HeaderAuthentication />

### Query Parameters

| Parameter                            | Description                                                                                                        | Example    |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ---------- |
| dateFrom<br /><code>mandatory</code> | Start date in YYYY-MM-DD format. Type: <code>string</code>                                                         | 2025-08-26 |
| dateTo<br /><code>optional</code>    | End date in YYYY-MM-DD format. If not provided, defaults to dateFrom. Max range: 3 days. Type: <code>string</code> | 2025-08-26 |
| pageSize<br /><code>optional</code>  | Number of records per page. Default: 100, Max: 50000. Type: <code>integer</code>                                   | 2        |
| page<br /><code>optional</code>      | Page number for pagination. Default: 1. Type: <code>integer</code>                                                 | 2          |
| merchantId<br /><code>optional</code>      | Merchant identifier provided by PayU while onboarding                                                 | 454541          |

## Sample Request

```curl
curl --location 'https://apitest.payu.in/settlement/range?dateFrom=2025-08-26&dateTo=2025-08-26&page=1&pageSize=2' \
--header 'Authorization: {{authorization}}' \
--header 'Date: {{date}}'
```

## Sample Response

### Success Response with UTR-Level Breakdown

```json
{
  "status": 0,
  "result": {
    "page": 1,
    "size": 2,
    "totalCount": 2,
    "data": [
      {
        "settlementId": "12127298202508260245",
        "settlementCompletedDate": "2025-08-26 02:51:22.000000",
        "settlementAmount": "1479.82",
        "merchantId": 12127298,
        "utrNumber": "523871332950",
        "transactionAmount": "2480.0",
        "adjustmentAmount": "-987.31",
        "refundAmount": "0.0",
        "chargebackAmount": "0.0",
        "refundReversalAmount": "0.0",
        "chargebackReversalAmount": "0.0",
        "serviceFee": "0.0",
        "serviceTax": "0.0",
        "additionalServiceFee": "10.91",
        "additionalServiceTax": "1.96",
        "numberOfTransactions": 1,
        "transaction": [
          {
            "action": "capture",
            "payuId": "24868774786",
            "requestId": "18044765028",
            "transactionAmount": "2480.0",
            "merchantServiceFee": "0.00000",
            "merchantServiceTax": "0.00000",
            "merchantNetAmount": "2467.13",
            "sgst": "0.00000",
            "cgst": "0.00000",
            "igst": "0.00000",
            "merchantTransactionId": "rXNmuNziG9X6UuP7LM9Imt3li",
            "mode": "UPI",
            "paymentStatus": "captured",
            "transactionDate": "2025-08-26 02:14:35.000000",
            "requestDate": "2025-08-26 02:15:28.000000",
            "requestedAmount": "2480.0",
            "bankName": "INTENT",
            "offerServiceFee": "0.00",
            "offerServiceTax": "0.00",
            "forexAmount": "0.0",
            "discount": "0.0",
            "additionalTdrFee": "10.91",
            "totalServiceTax": "1.96000",
            "transactionCurrency": "INR",
            "settlementCurrency": "INR",
            "totalProcessingFee": "10.91000",
            "additionalTdrTax": "1.96"
          },
          {
            "action": "ADJ_debit",
            "payuId": "ADJ_2574282",
            "transactionAmount": "987.31",
            "merchantNetAmount": "",
            "sgst": "",
            "cgst": "",
            "igst": "",
            "merchantTransactionId": "ADJ_2574282",
            "cardType": "",
            "mode": "debit",
            "paymentStatus": "settled",
            "transactionDate": "2025-08-26 02:26:35",
            "requestDate": "2025-08-26 02:26:35",
            "requestedAmount": "987.31",
            "bankName": "",
            "token": "",
            "forexAmount": "0.0",
            "transactionCurrency": "INR",
            "settlementCurrency": "INR"
          }
        ]
      }
    ]
  }
}
```

### Failure Scenarios
#### No Data Found
```json
{
  "status": 1,
  "message": "No data found",
  "result": "No data found"
}
```
#### Exceeds Date Range Limit

```json
{
  "status": 1,
  "message": "Date range exceeds maximum limit of 3 days",
  "result": null
}
```

#### Authorization Failed Response

```json
{
  "status": 1,
  "message": "Unauthorized: Invalid signature",
  "result": null
}
```

## Response Parameters

### UTR-Level Settlement Components

| Parameter                                           | Description                                                               | Example      |
| --------------------------------------------------- | ------------------------------------------------------------------------- | ------------ |
| utr<br /><code>mandatory</code>                     | Unique Transaction Reference. Type: <code>string</code>                   | UTR123456789 |
| transactionAmount<br /><code>mandatory</code>       | Total transaction amount for this UTR. Type: <code>decimal</code>         | 1000.00      |
| adjustmentAmount<br /><code>optional</code>         | Total adjustment amount for this UTR. Type: <code>decimal</code>          | -50.00       |
| refundAmount<br /><code>optional</code>             | Total refund amount for this UTR. Type: <code>decimal</code>              | 100.00       |
| chargebackAmount<br /><code>optional</code>         | Total chargeback amount for this UTR. Type: <code>decimal</code>          | 25.00        |
| refundReversalAmount<br /><code>optional</code>     | Total refund reversal amount for this UTR. Type: <code>decimal</code>     | 10.00        |
| chargebackReversalAmount<br /><code>optional</code> | Total chargeback reversal amount for this UTR. Type: <code>decimal</code> | 5.00         |
| serviceFee<br /><code>mandatory</code>              | Service fee charged for this UTR. Type: <code>decimal</code>              | 20.00        |
| serviceTax<br /><code>mandatory</code>              | Service tax on the fee for this UTR. Type: <code>decimal</code>           | 3.60         |
| additionalServiceFee<br /><code>optional</code>     | Additional service fee for this UTR. Type: <code>decimal</code>           | 5.00         |
| additionalServiceTax<br /><code>optional</code>     | Additional service tax for this UTR. Type: <code>decimal</code>           | 0.90         |
| numberOfTransactions<br /><code>mandatory</code>    | Total number of transactions in this UTR. Type: <code>integer</code>      | 15           |

### Transaction-Level Data

| Parameter                                      | Description                                                           | Example              |
| ---------------------------------------------- | --------------------------------------------------------------------- | -------------------- |
| txnid<br /><code>mandatory</code>              | Transaction ID. Type: <code>string</code>                             | TXN123456            |
| amount<br /><code>mandatory</code>             | Individual transaction amount. Type: <code>decimal</code>             | 100.00               |
| additionalTdrFee<br /><code>optional</code>    | Additional TDR fee for this transaction. Type: <code>decimal</code>   | 1.50                 |
| additionalTdrTax<br /><code>optional</code>    | Additional TDR tax for this transaction. Type: <code>decimal</code>   | 0.27                 |
| totalProcessingFee<br /><code>mandatory</code> | Total processing fee for this transaction. Type: <code>decimal</code> | 2.00                 |
| totalServiceTax<br /><code>mandatory</code>    | Total service tax for this transaction. Type: <code>decimal</code>    | 0.36                 |
| status<br /><code>mandatory</code>             | Transaction status. Type: <code>string</code>                         | success              |
| settled_at<br /><code>mandatory</code>         | Settlement timestamp. Type: <code>string</code>                       | 2023-09-26T10:30:00Z |
