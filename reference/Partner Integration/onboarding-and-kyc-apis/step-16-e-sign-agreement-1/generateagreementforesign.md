---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: GenerateAgreementForESign
hidden: false
---
The **Generate Agreement for E-Sign** API generates the merged merchant agreement document for electronic signing (Step 16 of 16 — final step).

<Callout icon="📘" theme="info">
  ### Notes:

  - After successful e-sign, the merchant can be activated.
  - **Scope:** `refer_merchant`
</Callout>

**HTTP Method**: GET

**Environment**

|                        | URL                                                                                      |
| :--------------------- | :--------------------------------------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v1/merchants/{uuid}/generate_merged_document_for_esign` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/generate_merged_document_for_esign`     |

<Callout icon="📘" theme="info">
  **Note:** Ensure the token includes `refer_merchant` and either `client_manage_agreement` or `client_manage_kyc_details`. Contact your **PayU Key Account Manager (KAM)** if scopes need enablement.
</Callout>

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/generate_merged_document_for_esign' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Accept: application/json'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "agreement_url": "https://esign.example.com/document/...",
    "agreement_status": "Generated",
    "message": "Agreement generated successfully"
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **401 Unauthorized** — Missing required scopes (`client_manage_agreement` or `client_manage_kyc_details`)

  ```json
  {
    "error": "unauthorized",
    "message": "Insufficient scope"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter        | Description                                        | Example                                  |
  | :--------------- | :------------------------------------------------- | :--------------------------------------- |
  | agreement_url    | `string` — URL for the merchant to complete e-sign | `https://esign.example.com/document/...` |
  | agreement_status | `string` — Agreement status after generation       | `Generated`                              |
  | message          | `string` — Status message                          | `Agreement generated successfully`       |
</Accordion>

## Request parameters

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Accept<br /><code>optional</code>         | `string` — Preferred response media type          | `application/json`        |
</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">
  | Parameter                        | Description                                              | Example                                |
  | :------------------------------- | :------------------------------------------------------- | :------------------------------------- |
  | uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |
</Accordion>
