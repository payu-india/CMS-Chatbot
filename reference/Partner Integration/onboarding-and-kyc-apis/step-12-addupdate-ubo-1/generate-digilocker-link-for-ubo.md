---
title: 'Generate DigiLocker Link for UBO '
deprecated: false
hidden: false
metadata:
  robots: index
---
Use this API to verify the Aadhar of each UBO members.&#x20;

## Endpoint

| Environment | Endpoint                                                                                   |
| ----------- | ------------------------------------------------------------------------------------------ |
| UAT         | `uat-partner.payu.in/api/v3/merchants/{mid}/kyc_document/generate_digilocker_link_for_ubo` |
| Production  | `partner.payu.in/api/v3/merchants/{mid}/kyc_document/generate_digilocker_link_for_ubo`     |

## Prerequisites

- **Step 15** (Add/Update UBO) must be completed — the UBO must exist and its `ultimate_beneficiary_uuid` must be available from the Step 15 response.

## Authentication

| Header          | Value                                              |
| --------------- | -------------------------------------------------- |
| `Authorization` | `Bearer {{access_token}}` — must include KYC scope |
| `Content-Type`  | `application/json`                                 |
| `Accept`        | `application/json`                                 |

## Path Parameters

| Parameter | Description                                  |
| --------- | -------------------------------------------- |
| `mid`     | Merchant's numeric MID from Step 01 response |

## Request Body — `multipart/form-data`

| Parameter                   | Type    | Required | Description                                                      |
| --------------------------- | ------- | -------- | ---------------------------------------------------------------- |
| `consent`                   | boolean | Yes      | Must be `true` — UBO's explicit consent for Aadhaar verification |
| `ultimate_beneficiary_uuid` | string  | Yes      | UUID of the UBO from the Step 15 response                        |

## Sample Request

```
POST {{partner_base_url}}/api/v3/merchants/{{mid}}/kyc_document/generate_digilocker_link_for_ubo

consent                    = true
ultimate_beneficiary_uuid  = 11f1-7b73-baa4b522-ab88-020deca221a9
```

## Responses

### 200 OK

```json
{
  "status": "link_generated",
  "capture_link": "https://api.digitallocker.gov.in/public/oauth2/1/authorize?response_type=code&client_id=JZ352A2C49&redirect_uri=https%3A%2F%2Fapi-in-uat.perfios.com%2Fkyc%2Fapi%2Fv1%2Fdigilocker%2Fget-token&state=eyJ0eXAi..."
}
```

Redirect the UBO to the `capture_link` URL to complete Aadhaar OTP authentication on DigiLocker.

### 422 — Missing `ultimate_beneficiary_uuid`

```json
{
  "ultimate_beneficiary_uuid": "ultimate_beneficiary_uuid must be passed."
}
```

### 422 — Missing `consent`

```json
{
  "consent": "consent must be passed."
}
```

## Next Step

After the UBO completes DigiLocker authentication, proceed to **Step 16**. If the online flow is not usable, fall back to **AadhaarXmlOfflineForUBO**.
