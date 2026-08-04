---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: UploadBankProof
hidden: false
---
The **Upload Bank Proof** API uploads bank account proof when auto-verification from Step 05 failed (Step 06 of 16 — conditional).

<Callout icon="📘" theme="info">
  ### Notes:

  - **When to call:** Only if **GetMerchant** shows `bank_verification_status` as `failed` or `pending`.
  - **Accepted types (examples):** Cancelled Cheque, Bank Verification Letter, Bank Statement, Passbook.
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                                                |
| :--------------------- | :----------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants/{mid}/kyc_document` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/{mid}/kyc_document`      |

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document' \
  --header 'Authorization: Bearer {{access_token}}' \
  --form 'merchant[document_category]="Bank Account Proof"' \
  --form 'merchant[document_type]="Cancelled Cheque"' \
  --form 'merchant[processed_document]=@"/path/to/cancelled_cheque.pdf"'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": "8390925",
      "kyc_document_name": "Bank Account Proof",
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
  - **422** — Invalid document category/type, file missing, too large, or unsupported format

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
  | Parameter                    | Description                                   | Example                    |
  | :--------------------------- | :-------------------------------------------- | :------------------------- |
  | merchant.mid                 | `string` — Merchant ID                        | `8390925`                  |
  | merchant.kyc_document_name   | `string` — Uploaded document category name    | `Bank Account Proof`       |
  | merchant.kyc_document_uuid   | `string` — Document UUID for show/delete APIs | `11ef-587e-4383...`        |
  | merchant.kyc_document_status | `string` — Document status after upload       | `DOCUMENT_SUBMITTED`       |
  | merchant.error_message       | `string`/`null` — Error detail if any         | `null`                     |
  | merchant.created_at          | `string` — Upload timestamp (ISO 8601)        | `2024-08-12T07:41:19.000Z` |
</Accordion>

## Request parameters

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
  | Parameter                                                 | Description                                                      | Example                |
  | :-------------------------------------------------------- | :--------------------------------------------------------------- | :--------------------- |
  | merchant\[document_category]<br /><code>mandatory</code>  | `string` — Use `Bank Account Proof`                              | `Bank Account Proof`   |
  | merchant\[document_type]<br /><code>mandatory</code>      | `string` — e.g. `Cancelled Cheque`, `Bank Statement`, `Passbook` | `Cancelled Cheque`     |
  | merchant\[processed_document]<br /><code>mandatory</code> | `file` — JPG/PNG/PDF, max 5 MB                                   | `cancelled_cheque.pdf` |
</Accordion>