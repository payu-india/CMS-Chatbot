---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: UpdateMerchant_WebsiteDetails
hidden: false
---
The **UpdateMerchant Website Details** API adds the merchant website and/or app store URLs (Step 07 of 16).

<Callout icon="📘" theme="info">
  **Prerequisite:** Step 05 (bank details) or Step 06 (bank proof), as applicable.

  **Entity applicability:** All entities.
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
    --form 'merchant[website_details][website_url]="https://www.example.com"' \
    --form 'merchant[website_details][android_url]="https://play.google.com/store/apps/details?id=com.example"' \
    --form 'merchant[website_details][ios_url]="https://apps.apple.com/app/example/id123456"'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": 12345678,
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
  | Parameter       | Description                          | Example           |
  | :-------------- | :----------------------------------- | :---------------- |
  | merchant.mid    | `integer` — Merchant ID              | `12345678`        |
  | merchant.status | `string` — Current onboarding status | `account_created` |
</Accordion>

## Additional Request Parameters Info

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
  | Parameter                                                              | Description                      | Example                                                     |
  | :--------------------------------------------------------------------- | :------------------------------- | :---------------------------------------------------------- |
  | merchant\[website_details]\[website_url]<br /><code>conditional</code> | `string` — Merchant website URL  | `https://www.example.com`                                   |
  | merchant\[website_details]\[android_url]<br /><code>optional</code>    | `string` — Android app store URL | `https://play.google.com/store/apps/details?id=com.example` |
  | merchant\[website_details]\[ios_url]<br /><code>optional</code>        | `string` — iOS App Store URL     | `https://apps.apple.com/app/example/id123456`               |
</Accordion>
