---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: FetchCkycData
hidden: false
---
The **Fetch CKYC Data** API fetches CKYC identity data using PAN without OTP (Step 03-C of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisites:** Step 01 (`mid`); Step 02 with a non-Individual / non-Sole Prop entity type.
  - **Entity applicability:** Partnership, Pvt Ltd, Public Limited, LLP, Trust, Society, One Person Company, Government, NGO, HUF, and similar.
</Callout>

**HTTP Method**: POST

**Environment**

|                        | URL                                                                    |
| :--------------------- | :--------------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v3/merchants/kyc_document/ckyc_data` |
| Production Environment | `https://partner.payu.in/api/v3/merchants/kyc_document/ckyc_data`      |

## Sample Request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location 'https://test-partner.payu.in/api/v3/merchants/kyc_document/ckyc_data' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "merchant_id": "{{mid}}",
    "consent": true
  }'
  ```
</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "ckyc_number": "XXXXXXXXXXXX",
    "name": "ACME PRIVATE LIMITED",
    "father_name": "",
    "dob": "15-03-2020",
    "address": "123 MG Road",
    "pincode": "560001",
    "state": "Karnataka",
    "city": "Bangalore",
    "related_persons_data": []
  }
  ```
</Accordion>

### Failure scenario

<Accordion title="Failure scenario" icon="fa-file-code">
  - **422** — Consent missing or CKYC record not found

  ```json
  {
    "error": "CKYC record not found"
  }
  ```
</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">
  | Parameter            | Description                                                  | Example                |
  | :------------------- | :----------------------------------------------------------- | :--------------------- |
  | ckyc_number          | `string` — CKYC identification number from CERSAI            | `XXXXXXXXXXXX`         |
  | name                 | `string` — Entity name in CKYC                               | `ACME PRIVATE LIMITED` |
  | dob                  | `string` — Date of incorporation (`DD-MM-YYYY`)              | `15-03-2020`           |
  | address              | `string` — Registered address from CKYC                      | `123 MG Road`          |
  | pincode              | `string` — Pincode from CKYC                                 | `560001`               |
  | state                | `string` — State from CKYC                                   | `Karnataka`            |
  | city                 | `string` — City from CKYC                                    | `Bangalore`            |
  | related_persons_data | `array` — Related persons (directors/partners); may be empty | `[]`                   |
</Accordion>

## Additional Request parameters Info

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `application/json`             | `application/json`        |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                               | Description                           | Example    |
  | :-------------------------------------- | :------------------------------------ | :--------- |
  | merchant_id<br /><code>mandatory</code> | `string` — Numeric `mid` from Step 01 | `12345678` |
  | consent<br /><code>mandatory</code>     | `boolean` — Must be `true`            | `true`     |
</Accordion>