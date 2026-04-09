---
title: View KFS and APR API
deprecated: false
hidden: true
metadata:
  robots: index
---
This API allows you to view Key Fact Statement (KFS) and Annual Percentage Rate (APR) information for EMI products by providing transaction details and lender information.

## Environment

| Environment    | Base URL                           |
| -------------- | ---------------------------------- |
| **Production** | `https://api.payu.in/emi/view-kfs` |

## Request Parameters

### Query Parameters

| Parameter                            | Description                                                                                             | Example                                                                                                            |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| payload<br /><code>mandatory</code>  | `String` Base64-encoded JSON string containing the request fields (amount, ibibo_code, key, requestId). | `eyJhbW91bnQiOiAyNjQ2MiwiaWJpYm9fY29kZSI6ICJIREZDRDAzIiwia2V5IjogIkpQKioqZyIsInJlcXVlc3RJZCI6ICJUZXN0MjEyMzQ1In0=` |
| checksum<br /><code>mandatory</code> | `String` SHA-512 checksum calculated using the formula: sha512(key\|JSON.stringify(payload)\|salt).     | `S/5vQbPGWC1ilyizrmM/1mPI9ORCLH0Wp92vV0VMiHw=`                                                                     |

### Payload Fields (JSON before Base64 encoding)

| Parameter                              | Description                                                                                      | Example        |
| -------------------------------------- | ------------------------------------------------------------------------------------------------ | -------------- |
| amount<br /><code>mandatory</code>     | `Number` Transaction amount for which KFS and APR information is requested.                      | `26462.00`     |
| ibibo_code<br /><code>mandatory</code> | `String` Lender identifier code to specify which lender's KFS/APR information to retrieve.       | `"HDFCD03"`    |
| key<br /><code>mandatory</code>        | `String` Merchant key provided by PayU during onboarding for authentication.                     | `"JP***g"`     |
| requestId<br /><code>mandatory</code>  | `String` Unique request identifier. Must be unique for each API call to ensure request tracking. | `"Test212345"` |

## Sample Request

**HTTP Method**: `GET`

**Request URL**:

```
https://api.payu.in/emi/view-kfs?payload=eyJhbW91bnQiOiAyNjQ2MiwiaWJpYm9fY29kZSI6ICJIREZDRDAzIiwia2V5IjogIkpQKioqZyIsInJlcXVlc3RJZCI6ICJUZXN0MjEyMzQ1In0=&checksum=S%2F5vQbPGWC1ilyizrmM%2F1mPI9ORCLH0Wp92vV0VMiHw%3D
```

**Decoded Payload** (for reference):

```json
{
  "amount": 26462.00,
  "ibibo_code": "HDFCD03",
  "key": "JP***g",
  "requestId": "Test212345"
}
```

**Checksum Calculation**:

1. Create checksum string: `key|JSON.stringify(payload)|salt`
2. Calculate SHA-512 hash of the checksum string
3. URL encode the hash for query parameter

## Sample Response

```json
{
  "status": 1,
  "message": "Success",
  "data": {
    "requestId": "Test212345",
    "kfs_url": "https://api.payu.in/documents/kfs/HDFCD03_26462_KFS.pdf",
    "apr_details": {
      "annual_percentage_rate": "12.5%",
      "processing_fee": "2%",
      "interest_rate": "11.5%"
    },
    "lender_details": {
      "lender_name": "HDFC Bank",
      "lender_code": "HDFCD03"
    }
  }
}
```

## Response Parameters

| Parameter | Description                                                                  | Example                          |
| --------- | ---------------------------------------------------------------------------- | -------------------------------- |
| status    | `Number` Response status code. `1` indicates success, `0` indicates failure. | `1`                              |
| message   | `String` Response message describing the result of the API call.             | `"Success"`                      |
| data      | `Object` Container for the response data when the request is successful.     | See data object parameters below |

### data Object Parameters

| Parameter      | Description                                                                                                                                                                                   | Example                                                                                                                 |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| requestId      | `String` Echoes the request identifier from the input for tracking purposes.                                                                                                                  | `"Test212345"`                                                                                                          |
| kfs_url        | `String` URL to download or view the Key Fact Statement document for the specified lender and amount.                                                                                         | Result KFS URL                                                                                                          |
| apr_details    | `Object` Annual Percentage Rate details and related fee information. Refer to [apr_details JSON Field Descriptions](pr_details-json-field-descriptions#apr_details-json-field-descriptions)   | Refer to [apr_details JSON Field Descriptions](pr_details-json-field-descriptions#apr_details-json-field-descriptions)  |
| lender_details | `Object` Information about the lender for which KFS and APR data is provided. Refer to [lender_details JSON Field Descriptions](lender_detials-object-json-field-descriptions)                | Refer to [lender_details JSON Field Descriptions](lender_detials-object-json-field-descriptions)                        |

#### apr_details JSON Field Descriptions

| Parameter              | Description                                                                    | Example   |
| ---------------------- | ------------------------------------------------------------------------------ | --------- |
| annual_percentage_rate | `String` The calculated Annual Percentage Rate including all fees and charges. | `"12.5%"` |
| processing_fee         | `String` Processing fee percentage charged by the lender.                      | `"2%"`    |
| interest_rate          | `String` Base interest rate charged by the lender before additional fees.      | `"11.5%"` |

#### lender_details Object Parameters

| Parameter   | Description                                                            | Example       |
| ----------- | ---------------------------------------------------------------------- | ------------- |
| lender_name | `String` Full name of the lending institution.                         | `"HDFC Bank"` |
| lender_code | `String` Echoes the ibibo_code from the request to confirm the lender. | `"HDFCD03"`   |
