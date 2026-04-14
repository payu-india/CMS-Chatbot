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

| Parameter                             | Description                                                                                           | Example    |
| ------------------------------------- | ----------------------------------------------------------------------------------------------------- | ---------- |
| settledOn<br /><code>mandatory</code> | Settlement date in YYYY-MM-DD format or UTR (Unique Transaction Reference). Type: <code>string</code> | 2023-09-26 |
| type<br /><code>optional</code>       | Settlement type. Allowed values: "G" or blank. Type: <code>string</code>                              | G          |
| isVersion<br /><code>mandatory</code> | API version (1 or 2). Version 2 returns enriched fields. Type: <code>integer</code>                   | 2          |
| page<br /><code>mandatory</code>      | Page number for pagination. Type: <code>integer</code>                                                | 1          |
| pageSize<br /><code>mandatory</code>  | Number of records per page. Min: 2000, Max: 50000. Type: <code>integer</code>                         | 5000       |

## Sample Request

### Version 1 for Standard Response

```bash
curl -X GET "https://apitest.payu.in/merchant/postservice?form=2&settledOn=2023-09-26&isVersion=1&page=1&pageSize=5000" \
  -H "Authorization: Bearer <sha512_signature>" \
  -H "Date: 2023-09-26T10:30:00Z"
```

### Version 2 for a Detailed Response

```bash
curl -X GET "https://apitest.payu.in/merchant/postservice?form=2&settledOn=2023-09-26&type=G&isVersion=2&page=1&pageSize=5000" \
  -H "Authorization: Bearer <sha512_signature>" \
  -H "Date: 2023-09-26T10:30:00Z"
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
  "status": 1,
  "message": "Settlement details retrieved successfully",
  "result": {
    "page": 1,
    "pageSize": 5000,
    "totalRecords": 2,
    "data": [
      {
        "txnid": "TXN123456",
        "amount": "100.00",
        "status": "success",
        "utr": "UTR123456789",
        "settled_at": "2023-09-26T10:30:00Z"
      }
    ]
  }
}
```

#### Version 2

```json
{
  "status": 1,
  "message": "Settlement details retrieved successfully",
  "result": {
    "page": 1,
    "pageSize": 5000,
    "totalRecords": 2,
    "data": [
      {
        "txnid": "TXN123456",
        "amount": "100.00",
        "payu_fee": "2.50",
        "payu_fee_tax": "0.45",
        "net_amount": "97.05",
        "status": "success",
        "utr": "UTR123456789",
        "settled_at": "2023-09-26T10:30:00Z"
      }
    ]
  }
}
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
