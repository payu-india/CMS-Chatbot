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

<br />
