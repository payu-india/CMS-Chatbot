---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: GenerateDigilockerLink
hidden: false
---
The **Generate DigiLocker Link** API creates a DigiLocker authentication URL for Aadhaar-based verification (Step 09 of 16).

<Callout icon="📘" theme="info">
  - **Prerequisite:** Step 08 (Signatory Details) — mandatory.
  - **Branching:**
    - Individual / Sole Prop — skip if CKYC succeeded; required if CKYC was skipped or failed
    - All other entities — always required
  - Redirect the merchant to the returned URL to complete DigiLocker authentication.
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                                                                         |
| :--------------------- | :------------------------------------------------------------------------------------------ |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants/{mid}/kyc_document/generate_digilocker_link` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/{mid}/kyc_document/generate_digilocker_link`      |

<Callout icon="📘" theme="info">
  **Note:** DigiLocker fails without Step 08 (Signatory Details). Use **GetMerchant** to check `entity_type` and `ckyc_status` before deciding whether DigiLocker is required.
</Callout>

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document/generate_digilocker_link' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "consent": true
  }'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "url": "https://digilocker.example.com/auth/...",
    "message": "Digilocker link generated successfully"
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **422** — Signatory details missing

  ```json
  {
    "error": "Signatory details required"
  }
  ```

  - **200** — Already completed (idempotent)

  ```json
  {
    "message": "Digilocker KYC is already completed"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter | Description                                                       | Example                                   |
  | :-------- | :---------------------------------------------------------------- | :---------------------------------------- |
  | url       | `string` — DigiLocker authentication URL to open for the merchant | `https://digilocker.example.com/auth/...` |
  | message   | `string` — Status message                                         | `Digilocker link generated successfully`  |
</Accordion>

## Request parameters

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `application/json`             | `application/json`        |
</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">
  | Parameter                       | Description                                         | Example   |
  | :------------------------------ | :-------------------------------------------------- | :-------- |
  | mid<br /><code>mandatory</code> | `string` — Numeric merchant ID (`mid`) from Step 01 | `8390925` |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                           | Description                                                 | Example |
  | :---------------------------------- | :---------------------------------------------------------- | :------ |
  | consent<br /><code>mandatory</code> | `boolean` — Must be `true` for Aadhaar verification consent | `true`  |
</Accordion>
