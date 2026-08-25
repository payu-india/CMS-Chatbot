---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: SendCkycOtp
hidden: false
---
The **Send CKYC OTP** API sends an OTP to the merchant mobile for CKYC verification (Step 03A of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisites:** Step 01 (`mid`); Step 02 with entity type **Individual** or **Sole Proprietorship**.
  - **Entity applicability:** Individual and Sole Proprietorship only. Other entities must use **Fetch CKYC Data** (Step 03C).
</Callout>

<br />

**HTTP Method**: POST

**Environment**

|                        | URL                                                                        |
| :--------------------- | :------------------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants/kyc_document/send_ckyc_otp` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/kyc_document/send_ckyc_otp`      |

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test-partner.payu.in/api/v3/merchants/kyc_document/send_ckyc_otp' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "merchant_id": "{{mid}}",
    "mobile": "{{merchant_mobile}}",
    "consent": true
  }'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "message": "OTP sent successfully"
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **422** — Consent not `true`, invalid mobile, or PAN not yet verified

  ```json
  {
    "error": "Consent is required"
  }
  ```

  - **401 Unauthorized** — Token invalid or expired

  ```json
  {
    "error": "unauthorized",
    "message": "Invalid or expired token"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter | Description                               | Example                 |
  | :-------- | :---------------------------------------- | :---------------------- |
  | message   | `string` — Confirmation that OTP was sent | `OTP sent successfully` |
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
  | Parameter                               | Description                                    | Example      |
  | :-------------------------------------- | :--------------------------------------------- | :----------- |
  | merchant_id<br /><code>mandatory</code> | `string` — Numeric `mid` from Step 01          | `12345678`   |
  | mobile<br /><code>mandatory</code>      | `string` — 10-digit mobile used in Step 01     | `9876543210` |
  | consent<br /><code>mandatory</code>     | `boolean` — Must be `true` for CKYC compliance | `true`       |
</Accordion>