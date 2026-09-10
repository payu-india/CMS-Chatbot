---
title: Fetch Settlement API for Partners
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  robots: index
---
## Overview

The Fetch Settlement API is a `GET` endpoint for retrieving paginated settlement information for a merchant through a reseller portal. Use it to request settlement data for a reseller, merchant, and date range.

The endpoint returns settlement-level values and nested transaction objects in a successful response. The response examples below are sanitized documentation examples; replace request placeholders with values from your integration and never place a real token in documentation or source control.

**Contents:** [Overview](#overview) · [Endpoints (UAT and Production)](#endpoints-uat-and-production) · [Authentication](#authentication) · [Query Parameters & Description](#query-parameters--description) · [Sample Request](#sample-request) · [Request Description](#request-description) · [Sample Response](#sample-response) · [Response Description](#response-description)

## Endpoints (UAT and Production)

The endpoint path is the same in both environments:

```text
GET /api/v1/merchants/fetch_settlement
```

| Environment | Base URL                       | Full endpoint                                                    |
| ----------- | ------------------------------ | ---------------------------------------------------------------- |
| UAT         | `https://test-partner.payu.in` | `https://test-partner.payu.in/api/v1/merchants/fetch_settlement` |
| Production  | `https://partner.payu.in`      | `https://partner.payu.in/api/v1/merchants/fetch_settlement`      |

## Authentication

Obtain the token through the **get token API** with the `client_read_settlements` scope. Send the returned token as a Bearer token in the `Authorization` header:

```http
Authorization: Bearer ${TOKEN}
```

`${TOKEN}` is a sanitized placeholder. Do not include a real credential in documentation or source control.

## Query Parameters & Description

The endpoint accepts the following query parameters. Values shown as `YOUR_...` are sanitized placeholders and must be replaced before making a request.

| Parameter       | Description                                                       | Placeholder guidance                                                         |
| --------------- | ----------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `reseller_uuid` | Identifies the reseller for which the settlement request is made. | Replace `YOUR_RESELLER_UUID` with the reseller UUID.                         |
| `merchant_id`   | Identifies the merchant whose settlement data is requested.       | Replace `YOUR_MERCHANT_MID` with the merchant ID.                            |
| `date_from`     | The start date of the requested settlement range.                 | Replace `YOUR_DATE_FROM` with the start-date value used by your integration. |
| `date_to`       | The end date of the requested settlement range.                   | Replace `YOUR_DATE_TO` with the end-date value used by your integration.     |

The request example uses all four parameters. The examples do not include credentials or real reseller or merchant identifiers.

## Sample Request

The following sanitized cURL request uses the UAT endpoint. To call Production, replace the UAT base URL with `https://partner.payu.in`.

```bash
curl --request GET \
  "https://test-partner.payu.in/api/v1/merchants/fetch_settlement?reseller_uuid=YOUR_RESELLER_UUID&merchant_id=YOUR_MERCHANT_MID&date_from=YOUR_DATE_FROM&date_to=YOUR_DATE_TO" \
  --header "Authorization: Bearer ${TOKEN}" \
  --header "Accept: application/json"
```

## Request Description

| Request component              | Description                                                                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `curl --request GET`           | Sends a `GET` request to fetch settlement data.                                                                                |
| UAT base URL and endpoint path | Targets `https://test-partner.payu.in/api/v1/merchants/fetch_settlement`. Use the Production base URL when calling Production. |
| `reseller_uuid`                | Identifies the reseller and is populated with `YOUR_RESELLER_UUID` in the sanitized example.                                   |
| `merchant_id`                  | Identifies the merchant and is populated with `YOUR_MERCHANT_MID` in the sanitized example.                                    |
| `date_from` and `date_to`      | Supply the requested date range using the `YOUR_DATE_FROM` and `YOUR_DATE_TO` placeholders in the example.                     |
| `Authorization`                | Carries the token obtained through the get token API with the `client_read_settlements` scope as a Bearer token.               |
| `Accept: application/json`     | Requests a JSON response.                                                                                                      |

Replace every `YOUR_...` placeholder and `${TOKEN}` before making the request.

## Sample Response

### Successful response

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

### Failure scenarios

#### No data found

```json
{
  "status": 1,
  "message": "No data found",
  "result": "No data found"
}
```

#### Date range exceeds maximum limit of 3 days

```json
{
  "status": 1,
  "message": "Date range exceeds maximum limit of 3 days",
  "result": null
}
```

#### Authorization failed

```json
{
  "status": 1,
  "message": "Unauthorized: Invalid signature",
  "result": null
}
```

## Response Description

### Top-level response fields

| Field     | Description                                                                                                                               |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `status`  | Indicates the response outcome in the supplied examples: `0` appears in the successful response and `1` appears in the failure responses. |
| `result`  | Contains the successful paginated response. In the failure examples it contains either the `No data found` text or `null`.                |
| `message` | Present in the supplied failure responses and contains the failure message. It is not a field in the supplied successful response.        |

The successful response uses `result` as its response container; it does not contain top-level `msg` or top-level `data` fields. The failure examples use `message` and `result`.

### `result` and pagination fields

| Field               | Description                                                           |
| ------------------- | --------------------------------------------------------------------- |
| `result.page`       | The page number returned in the successful response.                  |
| `result.size`       | The page size returned in the successful response.                    |
| `result.totalCount` | The total count returned for the successful response.                 |
| `result.data`       | The array of settlement objects returned for the successful response. |

### Settlement-level fields in `result.data[]`

| Field                      | Description                                               |
| -------------------------- | --------------------------------------------------------- |
| `settlementId`             | Settlement identifier.                                    |
| `settlementCompletedDate`  | Date and time shown for settlement completion.            |
| `settlementAmount`         | Settlement amount.                                        |
| `merchantId`               | Merchant identifier.                                      |
| `utrNumber`                | UTR number associated with the settlement.                |
| `transactionAmount`        | Transaction amount reported at settlement level.          |
| `adjustmentAmount`         | Adjustment amount reported at settlement level.           |
| `refundAmount`             | Refund amount reported at settlement level.               |
| `chargebackAmount`         | Chargeback amount reported at settlement level.           |
| `refundReversalAmount`     | Refund reversal amount reported at settlement level.      |
| `chargebackReversalAmount` | Chargeback reversal amount reported at settlement level.  |
| `serviceFee`               | Service fee reported at settlement level.                 |
| `serviceTax`               | Service tax reported at settlement level.                 |
| `additionalServiceFee`     | Additional service fee reported at settlement level.      |
| `additionalServiceTax`     | Additional service tax reported at settlement level.      |
| `numberOfTransactions`     | Number of transactions reported for the settlement.       |
| `transaction`              | Array of transaction objects nested under the settlement. |

### Transaction-level fields in `result.data[].transaction[]`

| Field                   | Description                                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------------------------ |
| `action`                | Action associated with the transaction, such as `capture` or `ADJ_debit` in the supplied examples.     |
| `payuId`                | PayU identifier for the transaction entry.                                                             |
| `requestId`             | Request identifier. It appears in the `capture` example and is not present in the `ADJ_debit` example. |
| `transactionAmount`     | Transaction amount.                                                                                    |
| `merchantServiceFee`    | Merchant service fee.                                                                                  |
| `merchantServiceTax`    | Merchant service tax.                                                                                  |
| `merchantNetAmount`     | Merchant net amount. The adjustment example preserves this as an empty string.                         |
| `sgst`                  | SGST value. The adjustment example preserves this as an empty string.                                  |
| `cgst`                  | CGST value. The adjustment example preserves this as an empty string.                                  |
| `igst`                  | IGST value. The adjustment example preserves this as an empty string.                                  |
| `merchantTransactionId` | Merchant transaction identifier.                                                                       |
| `cardType`              | Card type field; it is an empty string in the adjustment example.                                      |
| `mode`                  | Transaction mode, such as `UPI` or `debit` in the supplied examples.                                   |
| `paymentStatus`         | Payment status, such as `captured` or `settled` in the supplied examples.                              |
| `transactionDate`       | Date and time of the transaction.                                                                      |
| `requestDate`           | Date and time of the request.                                                                          |
| `requestedAmount`       | Requested amount.                                                                                      |
| `bankName`              | Bank name. The capture example contains `INTENT`; the adjustment example preserves an empty string.    |
| `token`                 | Token field; it is an empty string in the adjustment example.                                          |
| `offerServiceFee`       | Offer service fee.                                                                                     |
| `offerServiceTax`       | Offer service tax.                                                                                     |
| `forexAmount`           | Forex amount.                                                                                          |
| `discount`              | Discount amount. It appears in the `capture` example.                                                  |
| `additionalTdrFee`      | Additional TDR fee. It appears in the `capture` example.                                               |
| `totalServiceTax`       | Total service tax. It appears in the `capture` example.                                                |
| `transactionCurrency`   | Currency of the transaction.                                                                           |
| `settlementCurrency`    | Currency of the settlement.                                                                            |
| `totalProcessingFee`    | Total processing fee. It appears in the `capture` example.                                             |
| `additionalTdrTax`      | Additional TDR tax. It appears in the `capture` example.                                               |

Empty-string values in the successful response are preserved as returned in the adjustment transaction. The `null` values shown in the examples occur in the failure responses for `result`.
