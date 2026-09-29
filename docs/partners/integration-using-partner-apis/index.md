---
title: Integration using Partner APIs
deprecated: false
hidden: false
metadata:
  robots: index
---
Get a merchant onboarded with a small set of API calls: create merchant, update PAN/bank/business, CKYC OTP, upload KYC documents, initialize e-sign.

## Onboarding flow

```mermaid
flowchart TD
    A[1. Create Merchant] --> B[2. Update Website/App Details]
    B --> C[3. Update Business Details]
    C --> D[4. Submit Signing Authority]
    D --> E[5. Upload KYC Documents]
    E --> F[6. KYC Verification]
    F --> G[7. Add/Update UBO]
    G --> H[8. E-Sign Agreement]
    H --> I[Merchant Activated]
    
    style A fill:#e1f5ff
    style I fill:#d4edda
```

## Steps to integrate

Obtain a bearer token with the `refer_merchant` scope before these steps. See [GetToken API](ref:get_token_partner_integration). Each step below includes the environment URL and sample request/response. Request parameters are listed for Step 1; for later steps, use the linked API reference.

### Step 1. Create Merchant (Name, Email, Phone)

Creates a new merchant shell account on PayU. Pass display name, email, mobile, product (`PayUbiz`), and business entity type. Store `mid`, `uuid`, and `product_account_uuid` from the response — later steps use these identifiers. For the full parameter list and Try It experience, see [Create Merchant API](ref:createmerchant).

**HTTP Method**: POST

**Environment**

|                        | URL                                            |
| :--------------------- | :--------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v3/merchants` |
| Production Environment | `https://partner.payu.in/api/v3/merchants`     |

<Accordion title="Request parameters" icon="fa-table">
  | Parameter                                                                      | Description                                                     | Example                |
  | :----------------------------------------------------------------------------- | :-------------------------------------------------------------- | :--------------------- |
  | merchant\[display_name]<br /><code>mandatory</code>                            | `string` — Business or display name                             | `Acme Stores`          |
  | merchant\[email]<br /><code>mandatory</code>                                   | `string` — Unique merchant email across PayU                    | `merchant@example.com` |
  | merchant\[mobile]<br /><code>mandatory</code>                                  | `string` — Exactly 10-digit Indian mobile number                | `9876543210`           |
  | merchant\[product]<br /><code>mandatory</code>                                 | `string` — Must be `PayUbiz` (required to avoid backend errors) | `PayUbiz`              |
  | merchant\[business_details]\[business_entity_type]<br /><code>mandatory</code> | `string` — Entity type; determines CKYC method and later steps  | `Private Limited`      |
</Accordion>

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

<Accordion title="Sample response" icon="fa-file-code">
  ```json
  {
    "mid": 12345678,
    "uuid": "11ef-d968-6b042d6c-9b94-02975f21d323",
    "product_account_uuid": "11ef-d968-6b042d6c-9b94-02975f21d323"
  }
  ```
</Accordion>

### Step 2. Update Merchant Details (Business Info)

Adds business category, sub-category, expected monthly volume, GST, business name, and CIN where required (for Private Limited, Public Limited, and One Person Company). Use the merchant `uuid` from Step 1. For the full parameter list and Try It experience, see [UpdateMerchant Business Details API](ref:updatemerchant_businessdetails).

**HTTP Method**: PUT

**Environment**

|                        | URL                                                          |
| :--------------------- | :----------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v1/merchants/{uuid}/update` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/update`     |

<Accordion title="Request Parameters" icon="far fa-table-cells">
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
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
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

<Accordion title="Sample response" icon="fa-file-code">
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

### Step 3. Update Website/App Details

Adds the merchant website and/or app store URLs. At least one channel URL is typically required depending on how the merchant sells. For the full parameter list and Try It experience, see [Update Merchant Website Details API](ref:updatemerchant_websitedetails).

<Callout icon="📘" theme="info">
  ### Skip Website Details:&#x20;

  If you are willing to skip updating the website details, refer to [Skip Website Details API.](ref:skip_merchant_website_details) If you skjp this step or don't update website/app, you cannot accept payments through Partner Payments or Payment Links.
</Callout>

**HTTP Method**: PUT

**Environment**

|                        | URL                                                          |
| :--------------------- | :----------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v1/merchants/{uuid}/update` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/update`     |

<Accordion title="Request Parameters" icon="far fa-table-cells-header">
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
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
    --header 'Authorization: Bearer {{access_token}}' \
    --form 'merchant[website_details][website_url]="https://www.example.com"' \
    --form 'merchant[website_details][android_url]="https://play.google.com/store/apps/details?id=com.example"' \
    --form 'merchant[website_details][ios_url]="https://apps.apple.com/app/example/id123456"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": 12345678,
      "status": "account_created"
    }
  }
  ```
</Accordion>

### Step 4. Submit Signing Authority Details

Submits the authorised signatory for the merchant agreement. Complete this step before DigiLocker or Video KYC — those APIs fail if signatory details are missing. For the full parameter list and Try It experience, see [Add Signatory Details API](ref:addsignatorydetails).

**HTTP Method**: PUT

**Environment**

|                        | URL                                                                     |
| :--------------------- | :---------------------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v1/merchants/{uuid}/signatory_details` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/signatory_details`     |

<Accordion title="Request Parameters" icon="far fa-table-cells-header">
  ### Header parameters

  <Accordion title="Header parameters" icon="fa-table">
    | Header                                    | Description                                            | Example                             |
    | :---------------------------------------- | :----------------------------------------------------- | :---------------------------------- |
    | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`)      | `Bearer {{access_token}}`           |
    | Content-Type<br /><code>mandatory</code>  | `string` — Must be `application/x-www-form-urlencoded` | `application/x-www-form-urlencoded` |
  </Accordion>

  ### Path parameters

  <Accordion title="Path parameters" icon="fa-table">
    | Parameter                        | Description                                              | Example                                |
    | :------------------------------- | :------------------------------------------------------- | :------------------------------------- |
    | uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |
  </Accordion>

  ### Body parameters

  <Accordion title="Body parameters" icon="fa-table">
    | Parameter                                                                                              | Description                                        | Example                  |
    | :----------------------------------------------------------------------------------------------------- | :------------------------------------------------- | :----------------------- |
    | merchant\[signatory_contact_details_attributes\[0]\[authorised_signatory]]<br /><code>mandatory</code> | `string` — `true` for the authorised signatory     | `true`                   |
    | merchant\[signatory_contact_details_attributes\[0]\[name]]<br /><code>mandatory</code>                 | `string` — Signatory full name                     | `Signatory 1 Name`       |
    | merchant\[signatory_contact_details_attributes\[0]\[pancard_number]]<br /><code>mandatory</code>       | `string` — Signatory PAN                           | `ABCDE1234F`             |
    | merchant\[signatory_contact_details_attributes\[0]\[email]]<br /><code>mandatory</code>                | `string` — Signatory email                         | `signatory1@yopmail.com` |
    | merchant\[signatory_contact_details_attributes\[0]\[contact_detail_type]]<br /><code>mandatory</code>  | `string` — e.g. `Signing Authority`                | `Signing Authority`      |
    | merchant\[signatory_contact_details_attributes\[0]\[cin_number]]<br /><code>conditional</code>         | `string` — CIN only for Pvt Ltd / Public Ltd / OPC | `(empty for others)`     |
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/signatory_details' \
    --header 'Authorization: Bearer {{access_token}}' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'merchant[signatory_contact_details_attributes[0][authorised_signatory]]=true' \
    --data-urlencode 'merchant[signatory_contact_details_attributes[0][name]]=Signatory 1 Name' \
    --data-urlencode 'merchant[signatory_contact_details_attributes[0][pancard_number]]=ABCDE1234F' \
    --data-urlencode 'merchant[signatory_contact_details_attributes[0][email]]=signatory1@yopmail.com' \
    --data-urlencode 'merchant[signatory_contact_details_attributes[0][contact_detail_type]]=Signing Authority' \
    --data-urlencode 'merchant[signatory_contact_details_attributes[0][cin_number]]='
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": 12345678,
      "status": "account_created"
    }
  }
  ```
</Accordion>

### Step 5. Upload KYC Documents

Uploads one KYC document per required category (JPG, PNG, or PDF; max 5 MB). Call this API once for each required category. Use numeric `mid` from Step 1 in the path. For the full parameter list and Try It experience, see [Upload KYC Document API](ref:uploadkycdocument).

**HTTP Method**: POST

**Environment**

|                        | URL                                                               |
| :--------------------- | :---------------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v3/merchants/{mid}/kyc_document` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/{mid}/kyc_document`     |

<Accordion title="Request Parameters" icon="far fa-table-cells">
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
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location 'https://uat-partner.payu.in/api/v3/merchants/{{mid}}/kyc_document' \
    --header 'Authorization: Bearer {{access_token}}' \
    --form 'merchant[document_category]="PAN Card of Signing Authority"' \
    --form 'merchant[document_type]="PAN Card"' \
    --form 'merchant[processed_document]=@"/path/to/pan.pdf"'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
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

### Step 6. Request E-Sign Agreement

Generates the merged merchant agreement for electronic signing. After successful e-sign, the merchant can be activated. Ensure the token includes `refer_merchant` and either `client_manage_agreement` or `client_manage_kyc_details`. Contact your **PayU Key Account Manager (KAM)** if scopes need enablement. For the full parameter list and Try It experience, see [Generate Agreement for E-Sign API](ref:generateagreementforesign).

**HTTP Method**: GET

**Environment**

|                        | URL                                                                                      |
| :--------------------- | :--------------------------------------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v1/merchants/{uuid}/generate_merged_document_for_esign` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/generate_merged_document_for_esign`     |

<Accordion title="Request Parameters" icon="far fa-table-cells">
  ### Header parameters

  <Accordion title="Header parameters" icon="fa-table">
    | Header                                    | Description                                       | Example                   |
    | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
    | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
    | Accept<br /><code>optional</code>         | `string` — Preferred response media type          | `application/json`        |
  </Accordion>

  ### Path parameters

  <Accordion title="Path parameters" icon="fa-table">
    | Parameter                        | Description                                              | Example                                |
    | :------------------------------- | :------------------------------------------------------- | :------------------------------------- |
    | uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |
  </Accordion>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/generate_merged_document_for_esign' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Accept: application/json'
  ```
</Accordion>

<Accordion title="Sample response" icon="fa-file-code">
  ```json
  {
    "agreement_url": "https://esign.example.com/document/...",
    "agreement_status": "Generated",
    "message": "Agreement generated successfully"
  }
  ```
</Accordion>

### Step 7: Collect Payments

After you complete the steps 6, you can start collecting payments. To collect payments, you can integrate using PayU Hosted Checkout or Pre-Built Checkout or UPI S2S Checkout integration based on your requirements:

* [Hosted Checkout - Partner Payments](https://docs.payu.in/docs/hosted-integration-partner-payments)

* [S2S Integration - Partner Integration](https://docs.payu.in/docs/s2s-integration-partner-integration)

  * [UPI Intent Integration - Partner Payments](https://docs.payu.in/docs/partner-payments-upi-intent-integration)
  * [UPI TPV Integration - Partner Payments](https://docs.payu.in/docs/partner-payments-upi-tpv-integration)

## Next Steps

Refer to the APIs in the [APIs used in Partner Integration](doc:apis-used-in-partner-integration) for detailed API reference. After you complete the integration in the Test environment, refer to [Testing and Go Live - Partner Integration.](doc:testing-and-go-live-partner-integration)

<br />
