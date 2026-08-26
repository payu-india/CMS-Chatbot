---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: UpdateMerchant_BusinessDetails
hidden: false
---
The **Update Business Details** API adds business category, sub-category, expected volume, GST, business name, and CIN where required (Step 04 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisites:** Step 02 (entity type set); Step 03 (CKYC attempted).
  - **Entity applicability:** All entities. `cin_number` is required for Pvt Ltd, Public Limited, and One Person Company.
</Callout>

**HTTP Method**: PUT

**Environment**

|                        | URL                                                           |
| :--------------------- | :------------------------------------------------------------ |
| Test Environment       | `https://test-partner.payu.in/api/v1/merchants/{uuid}/update` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/update`      |

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location --request PUT 'https://test-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
    --header 'Authorization: Bearer {{access_token}}' \
    --form 'merchant[business_category]="Arts, Gifts & Stationery"' \
    --form 'merchant[business_sub_category]="Art Dealers and Galleries"' \
    --form 'merchant[monthly_expected_volume]="500000"' \
    --form 'merchant[gst_number]="29ABCDE1234F1Z5"' \
    --form 'merchant[gst_consent]="true"' \
    --form 'merchant[business_name]="MERCHANT BUSINESS NAME"' \
    --form 'merchant[cin_number]="U74999KA2020PTC123456"'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": 12345678,
      "business_name": "MERCHANT BUSINESS NAME",
      "status": "account_created"
    }
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
  | Parameter              | Description                          | Example                  |
  | :--------------------- | :----------------------------------- | :----------------------- |
  | merchant.mid           | `integer` — Merchant ID              | `12345678`               |
  | merchant.business_name | `string` — Updated business name     | `MERCHANT BUSINESS NAME` |
  | merchant.status        | `string` — Current onboarding status | `account_created`        |
</Accordion>

## All Request parameters Info

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `multipart/form-data`          | `multipart/form-data`     |
</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">
  | Parameter                        | Description                                              | Example                                |
  | :------------------------------- | :------------------------------------------------------- | :------------------------------------- |
  | uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                                      | Description                                      | Example                     |
  | :------------------------------------------------------------- | :----------------------------------------------- | :-------------------------- |
  | merchant\[business_category]<br /><code>mandatory</code>       | `string` — Business category                     | `Arts, Gifts & Stationery`  |
  | merchant\[business_sub_category]<br /><code>mandatory</code>   | `string` — Business sub-category                 | `Art Dealers and Galleries` |
  | merchant\[monthly_expected_volume]<br /><code>mandatory</code> | `string` — Expected monthly volume               | `500000`                    |
  | merchant\[gst_number]<br /><code>optional</code>               | `string` — GSTIN when available                  | `29ABCDE1234F1Z5`           |
  | merchant\[gst_consent]<br /><code>conditional</code>           | `string` — GST consent (`true` / `false`)        | `true`                      |
  | merchant\[business_name]<br /><code>mandatory</code>           | `string` — Legal / business name                 | `MERCHANT BUSINESS NAME`    |
  | merchant\[cin_number]<br /><code>conditional</code>            | `string` — Required for Pvt Ltd, Public Ltd, OPC | `U74999KA2020PTC123456`     |
</Accordion>