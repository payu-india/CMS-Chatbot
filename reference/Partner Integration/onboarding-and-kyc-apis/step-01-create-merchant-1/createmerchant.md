---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: CreateMerchant
hidden: false
---
The **CreateMerchant** API creates a new merchant shell account on PayU (Step 01 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisite:** Step 00 — valid bearer token with `refer_merchant` scope.
  - **Entity applicability:** All entities.
  - Store `mid`, `uuid`, and `product_account_uuid` from the response — later steps use different identifiers.
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                            |
| :--------------------- | :--------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v3/merchants` |
| Production Environment | `https://partner.payu.in/api/v3/merchants`     |

<Callout icon="📘" theme="info">
  **Note:** `merchant[product]=PayUbiz` is required. Omitting it can cause a backend error in the test environment. Contact your **PayU Key Account Manager (KAM)** if credentials or product enablement are unclear.
</Callout>

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://uat-partner.payu.in/api/v3/merchants' \
  --header 'Authorization: Bearer {{access_token}}' \
  --form 'merchant[display_name]="Acme Stores"' \
  --form 'merchant[email]="merchant@example.com"' \
  --form 'merchant[mobile]="9876543210"' \
  --form 'merchant[product]="PayUbiz"' \
  --form 'merchant[business_details][business_entity_type]="Private Limited"'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "mid": 12345678,
    "uuid": "11ef-d968-6b042d6c-9b94-02975f21d323",
    "product_account_uuid": "11ef-d968-6b042d6c-9b94-02975f21d323"
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **422 Validation Failed** — Duplicate email or invalid mobile

  ```json
  {
    "error": "Email has already been taken"
  }
  ```

  - **401 Unauthorized** — Token invalid or expired; call Step 00 again

  ```json
  {
    "error": "unauthorized",
    "message": "Invalid or expired token"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter            | Description                                                                                   | Example                                |
  | :------------------- | :-------------------------------------------------------------------------------------------- | :------------------------------------- |
  | mid                  | `integer` — Numeric merchant ID for KYC document APIs (Steps 06, 09, 14, 15)                  | `12345678`                             |
  | uuid                 | `string` — Merchant UUID for update/signatory APIs (Steps 02, 04, 05, 07, 08, 10, 12, 13, 16) | `11ef-d968-6b042d6c-9b94-02975f21d323` |
  | product_account_uuid | `string` — Product account UUID used in E-Sign (Step 16)                                      | `11ef-d968-6b042d6c-9b94-02975f21d323` |
</Accordion>

## Additional Request parameters description

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `multipart/form-data`          | `multipart/form-data`     |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                                                      | Description                                                     | Example                |
  | :----------------------------------------------------------------------------- | :-------------------------------------------------------------- | :--------------------- |
  | merchant\[display_name]<br /><code>mandatory</code>                            | `string` — Business or display name                             | `Acme Stores`          |
  | merchant\[email]<br /><code>mandatory</code>                                   | `string` — Unique merchant email across PayU                    | `merchant@example.com` |
  | merchant\[mobile]<br /><code>mandatory</code>                                  | `string` — Exactly 10-digit Indian mobile number                | `9876543210`           |
  | merchant\[product]<br /><code>mandatory</code>                                 | `string` — Must be `PayUbiz` (required to avoid backend errors) | `PayUbiz`              |
  | merchant\[business_details]\[business_entity_type]<br /><code>mandatory</code> | `string` — Entity type; determines CKYC method and later steps  | `Private Limited`      |
</Accordion>
