---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: VerifyCkycOtp
hidden: false
---
The **Verify CKYC OTP** API verifies the OTP from Step 03A and returns CKYC identity data (Step 03B of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisite:** Step 03A — OTP sent successfully.
  - **Entity applicability:** Individual and Sole Proprietorship only.
  - CKYC success for these entities can make DigiLocker (Step 09) optional.
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                                                         |
| :--------------------- | :-------------------------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v3/merchants/kyc_document/verify_ckyc_otp` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/kyc_document/verify_ckyc_otp`     |

<Callout icon="📘" theme="info">
  **Note:** Send `otp` as a JSON string, not a number. Parsing with `parseInt()` strips leading zeros and causes validation errors.
</Callout>

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test-partner.payu.in/api/v3/merchants/kyc_document/verify_ckyc_otp' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "merchant_id": "{{mid}}",
    "otp": "123456"
  }'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "name": "MERCHANT LEGAL NAME",
    "dob": "06-01-2000",
    "address": "123 MG Road",
    "city": "Bangalore",
    "state": "Karnataka",
    "pincode": "560001",
    "mobile": "******3210"
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **422** — OTP invalid, expired, or not sent as a string

  ```json
  {
    "error": "OTP is invalid"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter | Description                             | Example               |
  | :-------- | :-------------------------------------- | :-------------------- |
  | name      | `string` — Name from CKYC registry      | `MERCHANT LEGAL NAME` |
  | dob       | `string` — Date of birth (`DD-MM-YYYY`) | `06-01-2000`          |
  | address   | `string` — Address from CKYC            | `123 MG Road`         |
  | city      | `string` — City from CKYC               | `Bangalore`           |
  | state     | `string` — State from CKYC              | `Karnataka`           |
  | pincode   | `string` — Pincode from CKYC            | `560001`              |
  | mobile    | `string` — Masked mobile number         | `******3210`          |
</Accordion>

## Additional Request parameters Info

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `application/json`             | `application/json`        |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                               | Description                                                                                  | Example    |
  | :-------------------------------------- | :------------------------------------------------------------------------------------------- | :--------- |
  | merchant_id<br /><code>mandatory</code> | `string` — Numeric `mid` from Step 01                                                        | `12345678` |
  | otp<br /><code>mandatory</code>         | `string` — Exactly 6 digits; **must be a string** (preserves leading zeros, e.g. `"014645"`) | `123456`   |
</Accordion>
