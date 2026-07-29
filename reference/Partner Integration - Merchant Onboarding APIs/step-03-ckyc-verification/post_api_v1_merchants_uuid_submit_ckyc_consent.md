---
api:
  file: PayU_Partner_Onboarding_16Step_Spec.readme.openapi.renderfix.v2.json
  operationId: post_api_v1_merchants_uuid_submit_ckyc_consent
hidden: false
---
Skip CKYC Consent submits merchant/product-account level consents to skip or opt out of selected onboarding checks.

## Endpoint

`POST /api/v1/merchants/{uuid}/submit_ckyc_consent`

## Authentication Header

`Authorization:
Bearer {{access_token}}`- `Content-Type: application/json\`

## Request Body

`json{  "consents": [    {"name": "skip_ckyc_flow", "provided_by_uuid": "<partner_uuid>"},    {"name": "gst_consent", "provided_by_uuid": "<partner_uuid>"},    {"name": "ubo_not_exist", "provided_by_uuid": "<partner_uuid>"},    {"name": "digilocker_consent", "provided_by_uuid": "<partner_uuid>"}  ]}`

## Supported Consent Names

Use one or many entries in `consents[]`:

- `skip_ckyc_flow` — skip CKYC OTP/data path
- `gst_consent` — consent for GST-based flow
- `ubo_not_exist` — declare UBO does not exist / opt out of UBO submission
- `digilocker_consent` — consent for DigiLocker path`provided_by_uuid` should be the **partner UUID**.

## Response Documentation

### Success (200)

Returns:- `message`: success text- `data.consents[]`: list of active consent records on product accountEach `data.consents[]` item can include:- `uuid`, `name`, `provided_by_uuid`, `provided_by`- `record_id`, `record_type`, `active`- `product_account_uuid`, `merchant_id`, `merchant_uuid`

### Observed Success Variants

- **UBO_exist = 0 flow**: `data.consents[]` includes `ubo_not_exist`
- **UBO_exist = 1 flow**: `data.consents[]` does not include `ubo_not_exist`### Saved Examples in this request- `200 
  — Success (UBO_exist=0)`- `200 
  — Success (UBO_exist=1)`- `422 
  — Invalid consent name`- `401 — Unauthorized`

<br />