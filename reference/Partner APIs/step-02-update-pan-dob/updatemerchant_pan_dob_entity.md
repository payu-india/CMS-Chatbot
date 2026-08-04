---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: UpdateMerchant_PAN_DOB_Entity
hidden: false
---
The **UpdateMerchant PAN + DOB** API sets the merchant PAN and date of birth or incorporation (Step 02 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - Refer to ​[Step 01 — Create Merchant](ref:step-01-create-merchant-1) to create a merchant to get the **uuid** value from the response.
  - This is applicable to all entities.
</Callout>

<br />

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
    --form 'merchant[pancard_number]="ABCDE1234F"' \
    --form 'merchant[pancard_name]="MERCHANT LEGAL NAME"' \
    --form 'merchant[dob]="2000-01-06"'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": 12345678,
      "pan_verification_status": "Pending",
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

  - **422** — PAN format invalid

  ```json
  {
    "error": "PAN is invalid"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter                        | Description                                         | Example           |
  | :------------------------------- | :-------------------------------------------------- | :---------------- |
  | merchant.mid                     | `integer` — Merchant ID                             | `12345678`        |
  | merchant.pan_verification_status | `string` — PAN verification status after submission | `Pending`         |
  | merchant.status                  | `string` — Current onboarding status                | `account_created` |
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
  | Parameter                        | Description                                              | Example                                |
  | :------------------------------- | :------------------------------------------------------- | :------------------------------------- |
  | uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                             | Description                                                         | Example               |
  | :---------------------------------------------------- | :------------------------------------------------------------------ | :-------------------- |
  | merchant\[pancard_number]<br /><code>mandatory</code> | `string` — PAN in `ABCDE1234F` format                               | `ABCDE1234F`          |
  | merchant\[pancard_name]<br /><code>mandatory</code>   | `string` — Name on PAN card (must match registry)                   | `MERCHANT LEGAL NAME` |
  | merchant\[dob]<br /><code>mandatory</code>            | `string` — DOB (Individual) or date of incorporation (`YYYY-MM-DD`) | `2000-01-06`          |
</Accordion>
