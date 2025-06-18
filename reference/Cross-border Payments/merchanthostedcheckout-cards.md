---
title: PayU Hosted Checkout - CB LRS
api:
  file: PayU_Hosted_Checkout_Non_Seamless_API_Final.json
  operationId: MerchantHostedCheckout-Cards
hidden: true
---
##Step 1: Validate the PAN Card
The PAN Card Status Check API allows merchants to verify PAN (Permanent Account Number) card details. It validates whether a given PAN number is active, confirms if the provided name and date of birth match the official PAN records, and checks the seeding status of the PAN. This API is essential for KYC (Know Your Customer) processes, identity verification, and regulatory compliance.

## Endpoint
```
https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status
```

## Request Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| pan_number\n`mandatory` | The PAN (Permanent Account Number) to be verified | `"CYCPD2784G"` |
| name\n`mandatory` | The name of the PAN card holder as it appears on the PAN card | `"AKASH DEEP"` |
| dob\n`mandatory` | Date of Birth of the PAN holder in DD/MM/YYYY format | `"15/09/1993"` |

## Response Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| id | Unique identifier for the verification request | `86235` |
| api_name | Identifier of the API that was called | `"pan_status_check"` |
| identifier | A unique hash identifier for the verification request | `"79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5"` |
| response | Contains the verification results | See result table below |
| status | Overall status of the API call | `"success"` |
| http_status | HTTP status code of the response | `200` |
| client_id | Unique identifier of the client making the request | `"195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2"` |
| created_at | Timestamp when the verification record was created | `"2025-04-30T05:51:40.000Z"` |
| updated_at | Timestamp when the verification record was last updated | `"2025-04-30T05:51:40.000Z"` |
| client_name | Name of the client account | `"SignzyClient"` |

### Response Result Object

| Parameter | Description | Example |
|-----------|-------------|---------|
| status | Status of the PAN card | `"Active"` |
| nameMatch | Indicates if the provided name matches with PAN records (Y/N) | `"Y"` |
| dobMatch | Indicates if the provided DOB matches with PAN records (Y/N) | `"Y"` |
| seedingStatus | Indicates if the PAN is seeded with additional verifications (Y/N) | `"Y"` |

## Sample Request
```bash
curl --location 'https://test10-onboarding.payu.in/dvs/kyc/check_pan_card_status' \
--header 'Content-Type: application/json' \
--header 'Date: Thu, 17 Jun 2025 08:17:59 GMT' \
--header 'Digest: DFXmqI0rFnXlmHLlsRwdDMw9vUSVzyYQzGP+MKLo8f8=' \
--header 'Authorization: hmac username="smsplus", algorithm="hmac-sha256", headers="date digest", signature="7qjgpH9B4QALxDR0nVlHdEKEYMZ0XeJ0QpnvveSyqMo="' \
--header 'platformId: 1' \
--data '{
    "pan_number": "CYCPD2784G",
    "name": "AKASH DEEP",
    "dob": "15/09/1993"
}'
```

## Sample Response
```json
{
    "id": 86235,
    "api_name": "pan_status_check",
    "identifier": "79c0d918a4f4661cb9cb17d96d24ac1cf04b6013d504cc766ac5235380bfc0d5",
    "response": {
        "result": {
            "status": "Active",
            "nameMatch": "Y",
            "dobMatch": "Y",
            "seedingStatus": "Y"
        }
    },
    "status": "success",
    "http_status": 200,
    "client_id": "195ab95fa4700eeaaf38b7f5b538d2979f0f281e0a4eaedca1aa675b79b331a2",
    "created_at": "2025-04-30T05:51:40.000Z",
    "updated_at": "2025-04-30T05:51:40.000Z",
    "client_name": "SignzyClient"
}
```
