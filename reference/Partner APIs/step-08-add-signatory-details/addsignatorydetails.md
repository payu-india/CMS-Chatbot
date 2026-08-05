---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: AddSignatoryDetails
hidden: false
---
The **Add Signatory Details** API submits the authorised signatory for the merchant agreement (Step 08 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisite:** Step 07 (website details).
  - **Entity applicability:** All entities.
  - This step is **mandatory before DigiLocker (Step 09)**. CIN in signatory details applies only to CIN-eligible entities (Pvt Ltd, Public Limited, OPC).
</Callout>

<br />

**HTTP Method**: PUT

**Environment**

|                        | URL                                                                      |
| :--------------------- | :----------------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v1/merchants/{uuid}/signatory_details` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/signatory_details`      |

<Callout icon="📘" theme="info">
  **Note:** DigiLocker (Step 09) and VKYC (Step 11) fail if signatory details are missing. Complete this step before those APIs.
</Callout>

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location --request PUT 'https://test-partner.payu.in/api/v1/merchants/{{uuid}}/signatory_details' \
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

## Additional request parameters info

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
