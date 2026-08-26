---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: CreateVKYCProfile
hidden: false
---
The **Create VKYC Profile** API creates a Video KYC profile and returns a VCIP capture link (Step 11 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisite:** Step 10 (addresses). Signatory details (Step 08) must also be completed.
  - **Entity applicability:** All entities — PayU may trigger VKYC based on risk profile; some merchants can skip.
  - Share `capture_link` with the merchant to complete video verification. Track status via **GetMerchant** (`vkyc_status`).
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                                                             |
| :--------------------- | :------------------------------------------------------------------------------ |
| Test Environment       | `https://uat-partner.payu.in/api/v3/merchants/kyc_document/create_vkyc_profile` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/kyc_document/create_vkyc_profile`     |

## Sample request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://uat-partner.payu.in/api/v3/merchants/kyc_document/create_vkyc_profile' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "merchant_id": "{{mid}}"
  }'
  ```
</Accordion>

## Sample response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "uuid": "11ef-vkyc-profile-uuid",
    "status": "link_generated",
    "profile_id": "vendor-profile-id",
    "capture_link": "https://vcip.example.com/session/...",
    "scheduled_at": null
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **422** — Signatory details not completed

  ```json
  {
    "error": "Please complete (Signing authority details captured step) before initiating VKYC"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter    | Description                                                     | Example                                |
  | :----------- | :-------------------------------------------------------------- | :------------------------------------- |
  | uuid         | `string` — VKYC profile UUID                                    | `11ef-vkyc-profile-uuid`               |
  | status       | `string` — e.g. `link_generated`; later `approved` / `declined` | `link_generated`                       |
  | profile_id   | `string` — Vendor profile ID                                    | `vendor-profile-id`                    |
  | capture_link | `string` — VCIP video call URL to share with the merchant       | `https://vcip.example.com/session/...` |
  | scheduled_at | `string`/`null` — Scheduled time if applicable                  | `null`                                 |
</Accordion>

## Additional request parameters info

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `application/json`             | `application/json`        |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                               | Description                            | Example   |
  | :-------------------------------------- | :------------------------------------- | :-------- |
  | merchant_id<br /><code>mandatory</code> | `string` — Numeric merchant ID (`mid`) | `8390925` |
</Accordion>
