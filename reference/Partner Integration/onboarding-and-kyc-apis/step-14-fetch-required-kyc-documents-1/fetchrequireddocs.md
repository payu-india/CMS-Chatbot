---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: FetchRequiredDocs
hidden: false
---
The **Fetch Required KYC Documents** API returns document categories and accepted types for the merchant (Step 14 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Entity applicability:** All entities — the required list differs by entity type.
  - Use each category `name` as `merchant[document_category]` and each type `name` as `merchant[document_type]` in Step 15.
</Callout>

**HTTP Method**: GET

**Environment**

|                        | URL                                                                              |
| :--------------------- | :------------------------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants/{mid}/kyc_document/required_docs` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/{mid}/kyc_document/required_docs`      |

<Callout icon="📘" theme="info">
  ### **Mapping to Step 15 - Upload KYC Documents:**&#x20;

  `document_categories[i].name` → `merchant[document_category]`; `document_categories[i].document_types[j].name` → `merchant[document_type]`.
</Callout>

## Sample request

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location 'https://test-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document/required_docs' \
    --header 'Authorization: Bearer {{access_token}}' \
    --header 'Accept: application/json'
  ```
</Accordion>

## Sample response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "document_categories": [
      {
        "uuid": "11e8-748f-297824ce-9081-020aca9875be",
        "name": "PAN Card of Signing Authority",
        "document_types": [
          {
            "uuid": "11e8-748f-2946799c-9081-020aca9875be",
            "name": "PAN Card"
          }
        ],
        "kyc_document": null
      }
    ]
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
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter                                     | Description                                                         | Example                                          |
  | :-------------------------------------------- | :------------------------------------------------------------------ | :----------------------------------------------- |
  | document_categories                           | `array` — Required document categories for this merchant            | `[{ uuid, name, document_types, kyc_document }]` |
  | document_categories\[].name                   | `string` — Category name → `merchant[document_category]` in Step 15 | `PAN Card of Signing Authority`                  |
  | document_categories\[].document_types\[].name | `string` — Type name → `merchant[document_type]` in Step 15         | `PAN Card`                                       |
  | document_categories\[].kyc_document           | `object`/`null` — Existing upload status when already submitted     | `null` or `{ "status": "Approved" }`             |
</Accordion>

## Additional request parameters info

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Accept<br /><code>optional</code>         | `string` — Preferred response media type          | `application/json`        |
</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">
  | Parameter                       | Description                                         | Example   |
  | :------------------------------ | :-------------------------------------------------- | :-------- |
  | mid<br /><code>mandatory</code> | `string` — Numeric merchant ID (`mid`) from Step 01 | `8390925` |
</Accordion>