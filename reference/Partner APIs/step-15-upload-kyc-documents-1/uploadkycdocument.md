---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: UploadKYCDocument
hidden: false
---
The **Upload KYC Document** API uploads one KYC document per required category from Step 14 (Step 15 of 16).

<Callout icon="📘" theme="info">
  ### Note:

  Call once for each required category. Formats: JPG, PNG, PDF; max 5 MB per file.
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                                                |
| :--------------------- | :----------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants/{mid}/kyc_document` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/{mid}/kyc_document`      |

## Sample request

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location 'https://test-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document' \
    --header 'Authorization: Bearer {{access_token}}' \
    --form 'merchant[document_category]="PAN Card of Signing Authority"' \
    --form 'merchant[document_type]="PAN Card"' \
    --form 'merchant[processed_document]=@"/path/to/pan.pdf"'
  ```
</Accordion>

## Sample response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": "8390925",
      "kyc_document_name": "PAN Card of Signing Authority",
      "kyc_document_uuid": "11ef-587e-4383...",
      "kyc_document_status": "DOCUMENT_SUBMITTED",
      "error_message": null,
      "created_at": "2024-08-12T07:41:19.000Z"
    }
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **422** — Invalid category/type, missing file, too large, or unsupported format

  ```json
  {
    "error": {
      "document": "must be present"
    }
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter                    | Description                                                                    | Example                         |
  | :--------------------------- | :----------------------------------------------------------------------------- | :------------------------------ |
  | merchant.mid                 | `string` — Merchant ID                                                         | `8390925`                       |
  | merchant.kyc_document_name   | `string` — Uploaded category name                                              | `PAN Card of Signing Authority` |
  | merchant.kyc_document_uuid   | `string` — Document UUID for show/delete                                       | `11ef-587e-4383...`             |
  | merchant.kyc_document_status | `string` — e.g. `DOCUMENT_SUBMITTED`, `DOCUMENT_APPROVED`, `DOCUMENT_REJECTED` | `DOCUMENT_SUBMITTED`            |
  | merchant.error_message       | `string`/`null` — Error detail if any                                          | `null`                          |
  | merchant.created_at          | `string` — Upload timestamp                                                    | `2024-08-12T07:41:19.000Z`      |
</Accordion>

## Additional request parameters info

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `multipart/form-data`          | `multipart/form-data`     |
</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">
  | Parameter                       | Description                                         | Example   |
  | :------------------------------ | :-------------------------------------------------- | :-------- |
  | mid<br /><code>mandatory</code> | `string` — Numeric merchant ID (`mid`) from Step 01 | `8390925` |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                                 | Description                                                 | Example                         |
  | :-------------------------------------------------------- | :---------------------------------------------------------- | :------------------------------ |
  | merchant\[document_category]<br /><code>mandatory</code>  | `string` — Exact `document_categories[i].name` from Step 14 | `PAN Card of Signing Authority` |
  | merchant\[document_type]<br /><code>mandatory</code>      | `string` — Exact `document_types[j].name` from Step 14      | `PAN Card`                      |
  | merchant\[processed_document]<br /><code>mandatory</code> | `file` — JPG/PNG/PDF, max 5 MB                              | `pan.pdf`                       |
</Accordion>
