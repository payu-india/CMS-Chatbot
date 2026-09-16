---
title: Skip VKYC
deprecated: false
hidden: false
metadata:
  robots: index
---
## Overview

The VKYC Skip API allows a partner to exempt a merchant from completing Video KYC (VCIP). It is called after Video KYC (Step 14) has been attempted and resulted in a `declined` or `failed` status, or when the merchant is eligible to bypass the video verification step altogether.

The API sets a `vkyc_exempt_status` code on the merchant record that signals the reason for the exemption. Once set, the onboarding flow can proceed to document upload (Step 15) and e-sign (Step 16) without a completed VKYC.

**When to use this API:**

| VKYC Status                           | Action                                            |
| ------------------------------------- | ------------------------------------------------- |
| `approved`                            | Skip this step — VKYC already passed              |
| `declined` or `failed`                | Call this API with the appropriate exemption code |
| `pending` or `link_generated`         | Wait or poll GetMerchant before calling           |
| Not initiated (partner-eligible skip) | Call this API directly with                       |

***

## Endpoint

```
PUT /api/v1/merchants/{uuid}/update
```

| Environment | Base URL                       |
| ----------- | ------------------------------ |
| Test        | `https://test-partner.payu.in` |
| Production  | `https://partner.payu.in`      |

**Full URL:**

- Test: `https://test-partner.payu.in/api/v1/merchants/{uuid}/update`
- Production: `https://partner.payu.in/api/v1/merchants/{uuid}/update`

Replace `{uuid}` with the merchant UUID returned in the Step 01 (Create Merchant) response.

***

## Authentication

Include the Bearer token obtained from Step 00 (Authentication) in the request header.

```
Authorization: Bearer <access_token>
```

***

## Request

### Content Type

`multipart/form-data`

### Path Parameter

| Parameter | Type   | Required | Source                    | Description   |
| --------- | ------ | -------- | ------------------------- | ------------- |
| `uuid`    | string | Yes      | Step 01 response → `uuid` | Merchant UUID |

### Body Parameters

| Parameter                      | Type   | Required | Validation                    | Description                                  |
| ------------------------------ | ------ | -------- | ----------------------------- | -------------------------------------------- |
| `merchant[vkyc_exempt_status]` | string | Yes      | The right string to be passed | Exemption reason code — see enum table below |

### Exemption Status Codes

| Value          | When to Use                                 |
| -------------- | ------------------------------------------- |
| Opted for Skip | Merchant explicitly opted to skip Video KYC |

***

## Sample Request

```bash
curl --location --request PUT \
  'https://test-partner.payu.in/api/v1/merchants/11ef-d968-6b042d6c-9b94-02975f21d323/update' \
  --header 'Authorization: Bearer 7b5843b39e5532bc...' \
  --form 'merchant[vkyc_exempt_status]= 'Opted for Skip'
```

***

## Sample Response

### 200 OK

Returns the updated merchant object with `vkyc_exempt_status` reflected.

```json
{
  "merchant": {
    "mid": 12345678,
    "uuid": "11ef-d968-6b042d6c-9b94-02975f21d323",
    "email": "merchant@example.com",
    "registered_mobile": "9876543210",
    "status": "account_created",
    "vkyc_status": "declined",
    "vkyc_exempt_status": 'Opted for Skip',
    "skip_vkyc_eligible": true,
    "pan_verification_status": "verified",
    "bank_verification_status": "verified",
    "document_status": "Pending",
    "agreement_status": "Not Generated",
    "kyc_status": {
      "kyc_status": "LOCKED",
      "ckyc_status": "COMPLETED"
    }
  }
}
```

### 422 Unprocessable Entity

```json
{
  "errors": {
    "vkyc_exempt_status": ["is not included in the list"]
  }
}
```

### 401 Unauthorized

```json
{
  "status": "Unauthorized"
}
```

***

## Response Parameter Description

| Field                               | Type    | Description                                                                           |
| ----------------------------------- | ------- | ------------------------------------------------------------------------------------- |
| `merchant.mid`                      | integer | Numeric merchant ID                                                                   |
| `merchant.uuid`                     | string  | Merchant UUID                                                                         |
| `merchant.vkyc_status`              | string  | Current VKYC status: `not_initiated`, `in_progress`, `approved`, `declined`, `failed` |
| `merchant.vkyc_exempt_status`       | string  | The value sent as skip reason                                                         |
| `merchant.skip_vkyc_eligible`       | boolean | Whether this merchant is eligible to skip VKYC — check this before calling the API    |
| `merchant.status`                   | string  | Overall onboarding status                                                             |
| `merchant.pan_verification_status`  | string  | PAN verification: `verified` / `failed` / `pending`                                   |
| `merchant.bank_verification_status` | string  | Bank verification: `verified` / `failed` / `pending`                                  |
| `merchant.document_status`          | string  | KYC document upload progress                                                          |
| `merchant.agreement_status`         | string  | E-sign agreement status                                                               |
| `merchant.kyc_status.kyc_status`    | string  | KYC lock status: `LOCKED` → `COMPLETED`                                               |
| `merchant.kyc_status.ckyc_status`   | string  | CKYC status: `PENDING` → `COMPLETED`                                                  |

***

## Error Handling

| HTTP Status | Cause                                               | Resolution                                              |
| ----------- | --------------------------------------------------- | ------------------------------------------------------- |
| `422`       | `vkyc_exempt_status` value is outside the range 0–5 | Use only integer values 0 through 5                     |
| `401`       | Access token is expired or missing                  | Re-authenticate via Step 00 and retry                   |
| `404`       | `uuid` in the URL path is incorrect                 | Verify `uuid` from the Step 01 Create Merchant response |

***

## Prerequisites

| Step    | API             | Requirement                                                                                                                         |
| ------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Step 00 | Authentication  | Valid Bearer token with `refer_merchant` scope                                                                                      |
| Step 01 | Create Merchant | `uuid` for the URL path                                                                                                             |
| Step 14 | Video KYC       | Should have been attempted (status `declined` or `failed`) before calling this step, unless the merchant is a direct skip candidate |

***

## Flow Context

```
Step 14: Create VKYC Profile
  ├── vkyc_status = approved  →  Proceed to Step 15 (skip 14A)
  └── vkyc_status = declined / failed
        │
        ▼
Step 14A: VKYC Skip (this API)
  └── Set vkyc_exempt_status (0–5)
        │
        ▼
Step 15: Upload KYC Documents
Step 16: E-Sign Agreement
```

***

## Next Step

After setting the VKYC exemption, proceed to:

- **Step 11 (UBO Details)** — if entity is Private Limited, Public Limited, Partnership, Trust, LLP, or Society
- **Step 12 (Business Members)** — if entity is Private Limited, Public Limited, Partnership, or LLP
- **Step 15 (Upload KYC Documents)** — otherwise
