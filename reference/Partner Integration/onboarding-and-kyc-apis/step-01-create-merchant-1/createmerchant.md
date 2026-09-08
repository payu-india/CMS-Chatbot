---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: CreateMerchant
hidden: false
link:
  new_tab: false
---
The **CreateMerchant** API creates a new merchant shell account on PayU (Step 01 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisite:** Step 00 — valid bearer token with `refer_merchant` scope.
  - **Entity applicability:** All entities.
  - Store `mid` and `uuid` from the response. The saved response for this collection item does not contain `product_account_uuid`.
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                                                                            |
| :--------------------- | :--------------------------------------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants`                                                |
| Production Environment | `https://partner.payu.in/api/v3/merchants` _(not verified by the supplied Postman collection)_ |

<Callout icon="📘" theme="info">
  **Note:** `merchant[product]=PayUbiz` is required in the supplied collection request. The supplied collection also sends `merchant[business_details][business_entity_type]` in this request.
</Callout>

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test-partner.payu.in/api/v3/merchants' \
  --header 'Authorization: Bearer {{access_token}}' \
  --form 'merchant[display_name]="Test Merchant"' \
  --form 'merchant[email]="testmerchant@yopmail.com"' \
  --form 'merchant[mobile]="9876543210"' \
  --form 'merchant[product]="PayUbiz"' \
  --form 'merchant[business_details][business_entity_type]="Private Limited"'
  ```

  The request uses `POST`, the `Authorization: Bearer {{access_token}}` header, and multipart form-data.
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  **HTTP 200 OK** — saved response for the `Step 01 — Create Merchant/CreateMerchant` Postman item.

  ```json
  {
    "merchant": {
        "name": "PAYU PAYMENTS PRIVATE LIMITED",
        "email": "payuonb_mar02_v9@yopmail.com",
        "registered_mobile": "6976543219",
        "mid": 760070201,
        "product": "PayUbiz",
        "business_type": "LongTail",
        "business_name": null,
        "pancard_name": null,
        "pancard_number": null,
        "website_url": null,
        "android_url": null,
        "ios_url": null,
        "gst_number": null,
        "gst_verification_status": "Pending",
        "created_at": "2026-03-02T16:36:46.000Z",
        "mobile": "6976543219",
        "blocked": false,
        "first_name": "PAYU",
        "last_name": "PAYMENTS PRIVATE LIMITED",
        "bank_detail": {
            "bank_account_number": null,
            "ifsc_code": null,
            "holder_name": null,
            "nodal_code": null,
            "nodal_status": null
        },
        "operating_address": {
            "address_line": null,
            "city": null,
            "state": null,
            "pincode": null
        },
        "registration_address": {
            "address_line": null,
            "city": null,
            "state": null,
            "pincode": null
        },
        "business_entity": "Individual",
        "status": "account_created",
        "partner_source": "Create Merchant API",
        "pan_verification_status": "Pending",
        "website_approval_status": null,
        "notification_email": "payuonb_mar02_v9@yopmail.com",
        "settlement_status": null,
        "is_service_agreement_accepted": false,
        "is_authorisation_letter_required": false,
        "monthly_expected_volume": null,
        "business_category": null,
        "business_sub_category": null,
        "bank_verification_status": null,
        "uuid": "11f1-1655-ff305e86-ae3d-02f4a48620c1",
        "penny_deposit_status": null,
        "document_status": "Pending",
        "kyc_status": {
            "status": "LOCKED",
            "kyc_status": "LOCKED",
            "ckyc_status": "PENDING"
        },
        "agreement_status": "Not Generated",
        "integration_type": "Not Selected",
        "cin_number": null,
        "vkyc_exempt_status": null,
        "lob_status_prerisk": null,
        "dob": null,
        "vkyc_status": "pending",
        "vkyc": {
            "status": "pending",
            "completed_at": null,
            "kyc_type": "video_kyc",
            "capture_link": null,
            "expires_at": null,
            "link_created_at": null,
            "consent_given": null
        },
        "skip_vkyc_eligible": false,
        "ckyc_skipped": false,
        "cpv_status": null,
        "digilocker_status": null,
        "ckyc_status": null,
        "service_intent": "default"
    }
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  The supplied Postman item does not include a saved failure response. Any 401, 422, or other failure examples are not verified by this collection item.
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  The response contains a `merchant` object. The table below documents the fields present in the saved response. `mid` is the numeric merchant identifier; `uuid` is the merchant UUID. `product_account_uuid` is not present in the saved response.

  | Parameter                                           | Description                                            | Example                                  |
  | :-------------------------------------------------- | :----------------------------------------------------- | :--------------------------------------- |
  | `merchant.name`                                     | `string` — Returned in the saved `merchant` response.  | `"PAYU PAYMENTS PRIVATE LIMITED"`        |
  | `merchant.email`                                    | `string` — Returned in the saved `merchant` response.  | `"payuonb_mar02_v9@yopmail.com"`         |
  | `merchant.registered_mobile`                        | `string` — Returned in the saved `merchant` response.  | `"6976543219"`                           |
  | `merchant.mid`                                      | `integer` — Numeric merchant identifier (`mid`).       | `760070201`                              |
  | `merchant.product`                                  | `string` — Returned in the saved `merchant` response.  | `"PayUbiz"`                              |
  | `merchant.business_type`                            | `string` — Returned in the saved `merchant` response.  | `"LongTail"`                             |
  | `merchant.business_name`                            | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.pancard_name`                             | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.pancard_number`                           | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.website_url`                              | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.android_url`                              | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.ios_url`                                  | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.gst_number`                               | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.gst_ verification_status`                  | `string` — Returned in the saved `merchant` response.  | `"Pending"`                              |
  | `merchant.created_at`                               | `string` — Returned in the saved `merchant` response.  | `"2026-03-02T16:36:46.000Z"`             |
  | `merchant.mobile`                                   | `string` — Returned in the saved `merchant` response.  | `"6976543219"`                           |
  | `merchant.blocked`                                  | `boolean` — Returned in the saved `merchant` response. | `false`                                  |
  | `merchant.first_name`                               | `string` — Returned in the saved `merchant` response.  | `"PAYU"`                                 |
  | `merchant.last_name`                                | `string` — Returned in the saved `merchant` response.  | `"PAYMENTS PRIVATE LIMITED"`             |
  | `merchant.bank_ detail.bank_account_number`   | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.bank_ detail.ifsc_code`             | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.bank_ detail.holder_name`           | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.bank_ detail.nodal_code`            | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.bank_ detail.nodal_status`          | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.operating_ address.address_line`    | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.operating_ address.city`            | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.operating_ address.state`           | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.operating_ address.pincode`          | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.registration_ address.address_line` | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.registration_ address.city`         | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.registration_ address.state`        | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.registration_ address.pincode`      | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.business_ entity`                          | `string` — Returned in the saved `merchant` response.  | `"Individual"`                           |
  | `merchant.status`                                   | `string` — Returned in the saved `merchant` response.  | `"account_created"`                      |
  | `merchant.partner_ source`                           | `string` — Returned in the saved `merchant` response.  | `"Create Merchant API"`                  |
  | `merchant.pan_ verification_status`           | `string` — Returned in the saved `merchant` response.  | `"Pending"`                              |
  | `merchant.website_ approval_status`           | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.notification_ email`                | `string` — Returned in the saved `merchant` response.  | `"payuonb_mar02_v9@yopmail.com"`         |
  | `merchant.settlement_status`                        | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.is_service_ agreement_accepted`     | `boolean` — Returned in the saved `merchant` response. | `false`                                  |
  | `merchant.is_authorisation_ letter_required`  | `boolean` — Returned in the saved `merchant` response. | `false`                                  |
  | `merchant.monthly_ expected_volume`           | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.business_ category`                 | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.business_ sub_category`             | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.bank_ verification_status`          | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.uuid`                                     | `string` — Merchant UUID (`uuid`).                     | `"11f1-1655-ff305e86-ae3d-02f4a48620c1"` |
  | `merchant.penny_ deposit_status`              | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.document_ status`                   | `string` — Returned in the saved `merchant` response.  | `"Pending"`                              |
  | `merchant.kyc_ status.status`                 | `string` — Returned in the saved `merchant` response.  | `"LOCKED"`                               |
  | `merchant.kyc_ status.kyc_status`             | `string` — Returned in the saved `merchant` response.  | `"LOCKED"`                               |
  | `merchant.kyc_ status.ckyc_status`            | `string` — Returned in the saved `merchant` response.  | `"PENDING"`                              |
  | `merchant.agreement_ status`                         | `string` — Returned in the saved `merchant` response.  | `"Not Generated"`                        |
  | `merchant.integration_ type`                         | `string` — Returned in the saved `merchant` response.  | `"Not Selected"`                         |
  | `merchant.cin_number`                               | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.vkyc_ exempt_status`                | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.lob_ status_prerisk`                | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.dob`                                      | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.vkyc_status`                              | `string` — Returned in the saved `merchant` response.  | `"pending"`                              |
  | `merchant.vkyc.status`                              | `string` — Returned in the saved `merchant` response.  | `"pending"`                              |
  | `merchant.vkyc. completed_at`                 | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.vkyc. kyc_type`                     | `string` — Returned in the saved `merchant` response.  | `"video_kyc"`                            |
  | `merchant.vkyc. capture_link`                 | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.vkyc. expires_at`                   | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.vkyc. link_created_at`              | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.vkyc. consent_given`                | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.skip_ vkyc_eligible`                | `boolean` — Returned in the saved `merchant` response. | `false`                                  |
  | `merchant.ckyc_ skipped`                      | `boolean` — Returned in the saved `merchant` response. | `false`                                  |
  | `merchant.cpv_status`                               | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.digilocker_ status`                 | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.ckyc_ status`                              | `null` — Returned in the saved `merchant` response.    | `null`                                   |
  | `merchant.service_ intent`                           | `string` — Returned in the saved `merchant` response.  | `"default"`                              |
</Accordion>

## Additional Request parameters description

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                                                         | Example                   |
  | :---------------------------------------- | :---------------------------------------------------------------------------------- | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`)                                   | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `multipart/form-data` — request body encoding used by the Postman form-data request | `multipart/form-data`     |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                                                      | Description                                     | Example                    |
  | :----------------------------------------------------------------------------- | :---------------------------------------------- | :------------------------- |
  | merchant\[display_name]<br /><code>mandatory</code>                            | `string` — Business or display name             | `Test Merchant`            |
  | merchant\[email]<br /><code>mandatory</code>                                   | `string` — Merchant email                       | `testmerchant@yopmail.com` |
  | merchant\[mobile]<br /><code>mandatory</code>                                  | `string` — 10-digit Indian mobile number        | `9876543210`               |
  | merchant\[product]<br /><code>mandatory</code>                                 | `string` — PayU product type; must be `PayUbiz` | `PayUbiz`                  |
  | merchant\[business_details]\[business_entity_type]<br /><code>mandatory</code> | `string` — Business entity type                 | `Private Limited`          |
</Accordion>
