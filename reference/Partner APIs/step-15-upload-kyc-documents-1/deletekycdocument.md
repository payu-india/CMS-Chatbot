---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: DeleteKYCDocument
hidden: false
---
The **Deelete KYC Document** API returns details for a previously uploaded KYC document, including a signed document URL and verification status (Step 15).

<Callout icon="📘" theme="info">
  ### Note:

  **Scope:&#x20;**`refer_merchant`
</Callout>

**HTTP Method**: GET

**Environment**

|                        | URL                                                                                    |
| :--------------------- | :------------------------------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants/{mid}/kyc_document/{kyc_document_uuid}` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/{mid}/kyc_document/{kyc_document_uuid}`      |

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location 'https://test-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document/{{kyc_document_uuid}}' \
    --header 'Authorization: Bearer {{access_token}}' \
    --header 'Accept: application/json'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "document_category_name": "PAN Card of Signing Authority",
    "document_type_name": "PAN Card",
    "status": "Approved",
    "doc_url": "https://s3.example.com/signed-url..."
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **401 Unauthorized** — Token invalid or expired; call Step 00 again

  ```json
  {
    "error": "unauthorized",
    "message": "Invalid or expired token"
  }
  ```

  - **422 Validation Failed** — Request parameters failed validation

  ```json
  {
    "error": "validation_failed",
    "message": "Check the error details in the response body"
  }
  ```

  - **404 Not Found** — Unknown `kyc_document_uuid`

  ```json
  {
    "error": "not_found",
    "message": "KYC document not found"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter              | Description                                | Example                                |
  | :--------------------- | :----------------------------------------- | :------------------------------------- |
  | document_category_name | `string` — Document category               | `PAN Card of Signing Authority`        |
  | document_type_name     | `string` — Document type                   | `PAN Card`                             |
  | status                 | `string` — Verification status             | `Approved`                             |
  | doc_url                | `string` — Signed URL to the uploaded file | `https://s3.example.com/signed-url...` |
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
  | Parameter                                     | Description                                   | Example             |
  | :-------------------------------------------- | :-------------------------------------------- | :------------------ |
  | mid<br /><code>mandatory</code>               | `string` — Numeric merchant ID from Step 01   | `8390925`           |
  | kyc_document_uuid<br /><code>mandatory</code> | `string` — Document UUID from upload response | `11ef-587e-4383...` |
</Accordion>
