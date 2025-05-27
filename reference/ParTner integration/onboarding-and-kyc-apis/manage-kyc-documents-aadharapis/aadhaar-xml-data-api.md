---
title: Aadhaar XML Data API
api:
  file: Partner_Onboarding_APIs_with_Aadhaar_APIs.json
  operationId: post_api-v3-merchants-kyc-document-aadhaar-xml-data
hidden: false
---
The Aadhaar XML Data API allows merchants to retrieve Aadhaar data after OTP verification. This API is used in the Aadhaar e-KYC process to fetch the XML data from UIDAI after the user has provided the OTP sent to their registered mobile number.

<PARTNEROnboardingEnvironment />

## Request Parameters

### Authorization header

Authorization Bearer token must be generated using \*\*Aadhaar OTP Generation API \*\* with the scope as . For more information, refer to [Aadhaar OTP generation](ref:post_api-v3-merchants-kyc-document-aadhaar-xml-consent).

### Body

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        merchant\_id
        `mandatory`
      </td>

      <td>
        Unique identifier for the merchant
      </td>

      <td>
        20997866
      </td>
    </tr>

    <tr>
      <td>
        otp
        `mandatory`
      </td>

      <td>
        One-time password received on the user's registered mobile number
      </td>

      <td>
        123456
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```bash
curl --location 'https://partner.payu.in/api/v3/merchants/kyc_document/aadhaar_xml_data' \
--header 'Authorization: Bearer dummy' \
--form 'merchant_id="20997866"' \
--form 'otp="123456"'
```

## Sample response

### Success scenario

```json
{
  "status": "success",
  "code": 200,
  "message": "Aadhaar XML data retrieved successfully",
  "data": {
    "reference_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "merchant_id": "20997866",
    "timestamp": "2023-05-27T10:15:30Z",
    "aadhaar_data": {
      "name": "John Doe",
      "dob": "1990-01-01",
      "gender": "M",
      "address": {
        "house": "123",
        "street": "Main Street",
        "locality": "Sample Locality",
        "district": "Sample District",
        "state": "Sample State",
        "pincode": "123456"
      },
      "photo": "base64_encoded_image",
      "email": "masked_email@example.com",
      "mobile": "masked_mobile_number"
    }
  }
}
```

### Failure scenarios

* Invalid OTP

```json
{
  "status": "error",
  "code": 400,
  "message": "Invalid OTP",
  "data": null
}
```

* OTP expired

```json
{
  "status": "error",
  "code": 400,
  "message": "OTP expired",
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

* Failed to fetch Aadhaar data

```json
{
  "status": "error",
  "code": 500,
  "message": "Failed to fetch Aadhaar data",
  "data": null
}
```