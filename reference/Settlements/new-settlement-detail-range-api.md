---
title: Settlement Detail Range API
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

<Callout icon="📮" theme="default">
  **Postman Collection**: Access the **Settlement Detail Range API Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/lc2xiuz/settlementrangeapi](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/request/lc2xiuz/settlementrangeapi)
</Callout>

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
| dateFrom<br /><code>mandatory</code> | Start date in YYYY-MM-DD format. Type: <code>string</code>                                                         | 2023-09-26 |
| dateTo<br /><code>optional</code>    | End date in YYYY-MM-DD format. If not provided, defaults to dateFrom. Max range: 3 days. Type: <code>string</code> | 2023-09-28 |
| pageSize<br /><code>optional</code>  | Number of records per page. Default: 100, Max: 50000. Type: <code>integer</code>                                   | 500        |
| page<br /><code>optional</code>      | Page number for pagination. Default: 1. Type: <code>integer</code>                                                 | 1          |

## Sample Request

```bash
curl --location 'https://apitest.payu.in/settlement/range?dateFrom=2023-09-26&dateTo=2023-09-28&page=1&pageSize=500' \
--header 'Authorization: {{authorization}}' \
--header 'Date: {{date}}'
```

## Sample Response

### Success Response with UTR-Level Breakdown

```json
{
  "status": 1,
  "message": "Settlement details retrieved successfully", 
  "result": {
    "page": 1,
    "pageSize": 500,
    "totalCount": 2,
    "data": [
      {
        "utr": "UTR123456789",
        "transactionAmount": 1000.00,
        "adjustmentAmount": -50.00,
        "refundAmount": 100.00,
        "chargebackAmount": 25.00,
        "refundReversalAmount": 10.00,
        "chargebackReversalAmount": 5.00,
        "serviceFee": 20.00,
        "serviceTax": 3.60,
        "additionalServiceFee": 5.00,
        "additionalServiceTax": 0.90,
        "numberOfTransactions": 15,
        "GET_SETTLEMENT_DETAILS_TXNS": [
          {
            "txnid": "TXN123456",
            "amount": 100.00,
            "additionalTdrFee": 1.50,
            "additionalTdrTax": 0.27,
            "totalProcessingFee": 2.00,
            "totalServiceTax": 0.36,
            "status": "success",
            "settled_at": "2023-09-26T10:30:00Z"
          }
        ],
        "GET_SETTLEMENT_DETAILS_ADJUSTMENT": [
          {
            "txnid": "TXN123456",
            "adjustmentType": "refund",
            "adjustmentAmount": -50.00,
            "adjustmentDate": "2023-09-26T12:00:00Z"
          }
        ]
      }
    ]
  }
}
```

### Failure Scenarios

#### Exceeds Date Range Limit

```json
{
  "status": 0,
  "message": "Date range exceeds maximum limit of 3 days",
  "result": null
}
```

#### Authorization Failed Response

```json
{
  "status": 0,
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