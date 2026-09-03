---
api:
  file: Partner_Onboarding_APIs_with_Aadhaar_APIs.json
  operationId: post_api-v3-merchants-kyc-document-aadhaar-xml-consent
hidden: true
link:
  new_tab: false
---
The Aadhar OTP Generation API allows merchants to generate OTP for Aadhaar verification purposes. This API is used to initiate the authentication process by sending an OTP to the mobile number registered with the Aadhaar.

<PartnerAuthenticationEnvironement />

## Request Parameters

### Authorization header

Authorization Bearer token must be generated using **Get Token API** with the scope as . For more information, refer to [Get Token API - Partner Integration](ref:get_token_api).

### Body

| Parameter                      | Description                         | Example      |
| :----------------------------- | :---------------------------------- | :----------- |
| merchant_id<br />`mandatory`   | Unique identifier for the merchant  | 20997866     |
| aadhar_number<br />`mandatory` | 12-digit Aadhaar number of the user | bbbbbbbbbbbb |

## Sample request

```bash
curl --location 'https://api-example.com/api/v3/merchants/kyc_document/aadhaar_xml_consent' \
--header 'Authorization: Bearer dummy' \
--form 'merchant_id="20997866"' \
--form 'aadhar_number="bbbbbbbbbbbb"'
```

## Sample response

### Success scenario

```json
{
  "status": "success",
  "code": 200,
  "message": "OTP sent successfully",
  "data": {
    "reference_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "merchant_id": "20997866",
    "timestamp": "2023-05-27T10:15:30Z"
  }
}
```

### Failure scenario

* Invalid Aadhaar number

```json
{
  "status": "error",
  "code": 400,
  "message": "Invalid Aadhaar number",
  "data": null
}
```

* Unauthorized access

```json
{
  "status": "error",
  "code": 401,
  "message": "Unauthorized access",
  "data": null
}
```

* Failed to generate OTP

```json
{
  "status": "error",
  "code": 500,
  "message": "Failed to generate OTP",
  "data": null
}
```
