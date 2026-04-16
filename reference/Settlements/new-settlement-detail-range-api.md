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

| Parameter                             | Description                                                                                                   | Example    |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------- |
| dateFrom<br /><code>mandatory</code>  | <code>String</code> Start date in YYYY-MM-DD format.                                                          | 2025-08-26 |
| dateTo<br /><code>optional</code>     | <code>String</code>  End date in YYYY-MM-DD format. If not provided, defaults to dateFrom. Max range: 3 days. | 2025-08-26 |
| pageSize<br /><code>optional</code>   | <code>Integer</code>  Number of records per page. Default: 100, Max: 50000.                                   | 2          |
| page<br /><code>optional</code>       | <code>Integer</code> Page number for pagination. Default: 1.                                                  | 2          |
| merchantId<br /><code>optional</code> | <code>Integer</code>  Merchant identifier provided by PayU while onboarding                                   | 454541     |

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

| Parameter | Description                                                                                                                                  |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| status    | Response status and it returns either 1 or 0, where 0=Success and 1=Failure.                                                                 |
| msg       | Response message                                                                                                                             |
| data      | Main response data container in a JSON format. For more information, refer to [data JSON Fields Description](#data-json-fields-descriptions) |

### data JSON Fields description

| Field                    | Description                                                                                                                                        | Example                    |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| settlementId             | Unique identifier for the settlement batch. <code>string</code>                                                                                    | 12127298202508260245       |
| settlementCompletedDate  | Date and time when settlement was completed. <code>string</code>                                                                                   | 2025-08-26 02:51:22.000000 |
| settlementAmount         | Final net amount settled to the merchant after all deductions. <code>string</code>                                                                 | 1479.82                    |
| merchantId               | Unique identifier of the merchant. <code>integer</code>                                                                                            | 12127298                   |
| utrNumber                | Unique Transaction Reference number — bank reference for the fund transfer. <code>string</code>                                                    | 523871332950               |
| transactionAmount        | Gross transaction amount before any deductions (at UTR/settlement level). <code>string</code>                                                      | 2480.0                     |
| adjustmentAmount         | Total adjustment amount applied (negative for debits, positive for credits). <code>string</code>                                                   | -987.31                    |
| refundAmount             | Total amount deducted due to refunds. <code>string</code>                                                                                          | 0.0                        |
| chargebackAmount         | Total amount deducted due to chargebacks. <code>string</code>                                                                                      | 0.0                        |
| refundReversalAmount     | Amount credited back due to refund reversals. <code>string</code>                                                                                  | 0.0                        |
| chargebackReversalAmount | Amount credited back due to chargeback reversals. <code>string</code>                                                                              | 0.0                        |
| serviceFee               | Standard processing fee charged by PayU for the settlement/UTR. <code>string</code>                                                                | 0.0                        |
| serviceTax               | GST/Tax on the service fee. <code>string</code>                                                                                                    | 0.0                        |
| additionalServiceFee     | Additional service fee (e.g., TDR or other extra fees) applied at UTR level. <code>string</code>                                                   | 10.91                      |
| additionalServiceTax     | GST/Tax on the additional service fee. <code>string</code>                                                                                         | 1.96                       |
| numberOfTransactions     | Count of successful capture transactions included in this settlement/UTR. <code>integer</code>                                                     | 1                          |
| additionalTdrFee         | Additional TDR (Transaction Discount Rate) fee applied. <code>string</code>                                                                        | 10.91                      |
| additionalTdrTax         | Tax on the additional TDR fee. <code>string</code>                                                                                                 | 1.96                       |
| totalServiceTax          | Total tax amount (sum of SGST + CGST + IGST) applicable to fees. <code>string</code>                                                               | 1.96000                    |
| totalProcessingFee       | Total processing fee including all components (standard + additional). <code>string</code>                                                         | 10.91000                   |
| transactionCurrency      | Currency of the original transaction (e.g., INR). <code>string</code>                                                                              | INR                        |
| settlementCurrency       | Currency in which the settlement is made. <code>string</code>                                                                                      | INR                        |
| transaction              | transaction details in a JSON format. For more information, refer to  [transaction JSON Fields Description](#transaction-json-fields-description). |                            |

### transaction JSON Fields Description

| Parameter             | Description                                                                              | Example                   |
| --------------------- | ---------------------------------------------------------------------------------------- | ------------------------- |
| action                | Type of transaction (capture, refund, chargeback). <code>string</code>                   | capture                   |
| payuId                | PayU's unique transaction identifier. <code>string</code>                                | 24868774786               |
| requestId             | Internal request identifier for the transaction. <code>string</code>                     | 18044765028               |
| transactionAmount     | Amount of the individual transaction (gross). <code>string</code>                        | 2480.0                    |
| merchantServiceFee    | Service fee charged for this transaction. <code>string</code>                            | 0.00000                   |
| merchantServiceTax    | Tax on the service fee for this transaction. <code>string</code>                         | 0.00000                   |
| merchantNetAmount     | Net amount after deducting fees and taxes for this transaction. <code>string</code>      | 2467.13                   |
| sgst                  | State GST component of the tax. <code>string</code>                                      | 0.00000                   |
| cgst                  | Central GST component of the tax. <code>string</code>                                    | 0.00000                   |
| igst                  | Integrated GST component (for inter-state transactions). <code>string</code>             | 0.00000                   |
| merchantTransactionId | Merchant's own reference ID for the transaction. <code>string</code>                     | rXNmuNziG9X6UuP7LM9Imt3li |
| mode                  | Payment mode used (UPI, CC, DC, NB, WALLET, debit, credit). <code>string</code>          | UPI                       |
| paymentStatus         | Current status of the transaction (captured, settled, refund). <code>string</code>       | captured                  |
| transactionDate       | Date and time when the transaction was initiated. <code>string</code>                    | 2025-08-26 02:14:35       |
| requestDate           | Date and time when the transaction request was created. <code>string</code>              | 2025-08-26 02:15:28       |
| requestedAmount       | Original amount requested in the transaction. <code>string</code>                        | 2480.0                    |
| bankName              | Name of the bank or payment gateway (e.g., HDFC, AXIS). <code>string</code>              | INTENT                    |
| cardType              | Type of card used (VISA, MASTERCARD) — applicable for card payments. <code>string</code> |                           |
| token                 | Tokenized card reference (if card tokenization is enabled). <code>string</code>          |                           |
| offerServiceFee       | Fee related to offers/discounts applied. <code>string</code>                             | 0.00                      |
| offerServiceTax       | Tax on the offer service fee. <code>string</code>                                        | 0.00                      |
| forexAmount           | Foreign exchange amount (for international transactions). <code>string</code>            | 0.0                       |
| discount              | Discount amount applied on the transaction. <code>string</code>                          | 0.0                       |
| additionalTdrFee      | Additional TDR (Transaction Discount Rate) fee. <code>string</code>                      | 10.91                     |
| additionalTdrTax      | Tax on the additional TDR fee. <code>string</code>                                       | 1.96                      |
| totalServiceTax       | Total tax amount (SGST + CGST + IGST). <code>string</code>                               | 1.96000                   |
| totalProcessingFee    | Total processing fee including all components. <code>string</code>                       | 10.91000                  |
| transactionCurrency   | Currency of the original transaction. <code>string</code>                                | INR                       |
| settlementCurrency    | Currency in which settlement is made. <code>string</code>                                | INR                       |
