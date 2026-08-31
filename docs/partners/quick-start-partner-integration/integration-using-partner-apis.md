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

Creates a new merchant shell account on PayU. Pass display name, email, mobile, product (`PayUbiz`), and business entity type. Store `mid`, `uuid`, and `product_account_uuid` from the response — later steps use these identifiers. For the full parameter list and Try It experience, see [CreateMerchant API](ref:createmerchant).

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

Adds the merchant website and/or app store URLs. At least one channel URL is typically required depending on how the merchant sells. For the full parameter list and Try It experience, see [UpdateMerchant Website Details API](ref:updatemerchant_websitedetails).

**HTTP Method**: PUT

**Environment**

|                        | URL                                                          |
| :--------------------- | :----------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v1/merchants/{uuid}/update` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/update`     |

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

After you complete the steps 6, you can start collecting payments. To collect payments, you can integrate using PayU Hosted Checkout or Pre-Built Checkout or UPI S2S Checkout integration based on your requirements.&#x20;

#### Hosted Checkout Integration

For detailed steps to integrate, refer to [Hosted Checkout Integration](ref:hosted-checkout-api-partner-integration)

**Sample Request**

```curl
curl --location --request POST \
'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer <ROTATED_BEARER_TOKEN>' \
--data-raw '{
  "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
  "amount": 1090.33,
  "productinfo": "whatsapp",
  "firstname": "Manikanta",
  "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
  "merchant_id": "8238480",
  "phone": 7036722360,
  "hash": "52f45927e221a16bd5372709516de5110c06c55e0057f8a18a3b9b9f2c2f176870af276274709910f27d7c5df44822777542e3d4b86f29e8304e17fcb373133c",
  "lastname": "CHeruku",
  "email": "manik.cr24@gmail.com",
  "curl": "<YOUR_CANCEL_URL>",
  "furl": "<YOUR_FAILURE_URL>",
  "surl": "<YOUR_SUCCESS_URL>",
  "udf1": "whatsapp"
}'
```

#### Sample Response

```text
{
    "redirectUri": "https://apitest.payu.in/public/#/35de666bac018494a06205addba2962cdb8d03ca9c2fa7954807098709f1b6dc"
}
```

#### UPI S2S Integration

For detailed steps, refer to [UPI S2S Integration API.](ref:upi-s2s-partner-integration-api)

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/payments' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer 9d2ab8e1b99aa02f6b827af5b5000b277d9cb1cd037acb7cb31436a5b0da4f74' \
--data-raw '{
    "txnid": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
    "amount": 1090.33,
    "productinfo": "whatsapp",
    "firstname": "Manikanta",
    "reseller_id": "83fe-eb64-021844d8-9397-26535b1bf0c2",
    "merchant_id": 8238480,
    "phone": 7036722360,
    "hash": "5aadceaf6bec9158ccba8ec0dab32debcacbfd50e3587c077fa11107a5be0ac26712fae230522afb8908d068122c02f2d5c733a46c33ace0f66e5cc9d2ae4714",
    "lastname": "CHeruku",
    "email": "manik.cr24@gmail.com",
    "curl": "https://www.google.com",
    "furl": "https://www.google.com",
    "surl": "https://www.youtube.com",
    "txn_s2s_flow": "4",
    "s2s_device_info": "ewew",
    "s2s_client_ip": "ewew"
}'
```

**Sample Response**

```text
{
    "metaData": {
        "message": null,
        "referenceId": "024d9afbdbf85bd35b25649ccf983e16ee3d4646c2cdcffada88bd2df371fd43",
        "statusCode": null,
        "txnId": "nY3tkz3vciHFGTjblyFeycL2Zn1m",
        "txnStatus": "pending",
        "unmappedStatus": "pending"
    },
    "result": {
        "paymentId": 403993715529028543,
        "merchantName": "Merchant",
        "merchantVpa": null,
        "amount": "1090.33",
        "intentURIData": "pa=&pn=&tr=403993715529028543&tid=PPPL403993715529028543290523133325&am=1090.33&cu=INR&tn=UPI Transaction for PPPL403993715529028543290523133325",
        "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0icGF5bWVudF9wb3N0IiBhY3Rpb249Imh0dHBzOi8vdGVzdC5wYXl1LmluLzAyNGQ5YWZiZGJmODViZDM1YjI1NjQ5Y2NmOTgzZTE2NGQ0YTUxYzYzNjcyODAxNjRkMDlkNDg2YjRkYWI1ZmEvaW50ZW50U2VhbWxlc3NIYW5kbGVyLnBocCIgbWV0aG9kPSJwb3N0Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJ0b2tlbiIgdmFsdWU9IjE2NTIyQTgxLTUwMjYtMUUyRi0zNDFCLTJFQ0MyQ0Y5RTE1QyI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iYW1vdW50IiB2YWx1ZT0iMTA5MC4zMyI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0ibWlocGF5aWQiIHZhbHVlPSIwMjRkOWFmYmRiZjg1YmQzNWIyNTY0OWNjZjk4M2UxNmVlM2Q0NjQ2YzJjZGNmZmFkYTg4YmQyZGYzNzFmZDQzIj48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJkaXNhYmxlSW50ZW50U2VhbWxlc3NGYWlsdXJlIiB2YWx1ZT0iMSI+PGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0icGF5ZWVWcGEiIHZhbHVlPSIiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InBheWVlTmFtZSIgdmFsdWU9Ik1lcmNoYW50Ij48aW5wdXQgdHlwZT0iaGlkZGVuIiBuYW1lPSJhZGRpdGlvbmFsQ2hhcmdlcyIgdmFsdWU9IjAiPjxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9InRyYW5zYWN0aW9uRmVlIiB2YWx1ZT0iMTA5MC4zMyI+PC9mb3JtPjxzY3JpcHQgdHlwZT0ndGV4dC9qYXZhc2NyaXB0Jz4KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHdpbmRvdy5vbmxvYWQ9ZnVuY3Rpb24oKXsKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBkb2N1bWVudC5mb3Jtc1sncGF5bWVudF9wb3N0J10uc3VibWl0KCk7CiAgICAgICAgICAgICAgICAgICAgICAgICAgICB9CiAgICAgICAgICAgICAgICAgICAgICAgIDwvc2NyaXB0PjwvYm9keT48L2h0bWw+",
        "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
}
```

<br />

## Next Steps

Refer to the APIs in the [APIs used in Partner Integration](doc:apis-used-in-partner-integration) for detailed API reference. After you complete the integration in the Test environment, refer to [Testing and Go Live - Partner Integration.](doc:testing-and-go-live-partner-integration)

<br />
