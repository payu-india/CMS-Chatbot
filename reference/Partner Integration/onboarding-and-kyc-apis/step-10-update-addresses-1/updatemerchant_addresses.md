---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: UpdateMerchant_Addresses
hidden: false
---
The **Update Merchant Addresses** API adds registration and operating addresses for the merchant (Step 10 of 16).

<Callout icon="📘" theme="info">
  ### Notes:

  - **Prerequisite:** Step 09 (DigiLocker) completed or skipped per branching rules.
  - **Entity applicability:** All entities.
</Callout>

**HTTP Method**: PUT

**Environment**

|                        | URL                                                          |
| :--------------------- | :----------------------------------------------------------- |
| Test Environment       | `https://uat-partner.payu.in/api/v1/merchants/{uuid}/update` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/update`     |

## Sample request

<Accordion title="Sample request" icon="fa-code">
  ```bash
    curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/{{uuid}}/update' \
    --header 'Authorization: Bearer {{access_token}}' \
    --form 'merchant[registration_address][address_line]="123 MG Road"' \
    --form 'merchant[registration_address][city]="Bangalore"' \
    --form 'merchant[registration_address][state]="Karnataka"' \
    --form 'merchant[registration_address][pincode]="560001"' \
    --form 'merchant[operating_address][address_line]="456 Indiranagar"' \
    --form 'merchant[operating_address][city]="Bangalore"' \
    --form 'merchant[operating_address][state]="Karnataka"' \
    --form 'merchant[operating_address][pincode]="560038"'
  ```
</Accordion>

## Sample response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "merchant": {
      "mid": 760070201,
      "operating_address": {
        "address_line": "M1704, Banashankari",
        "city": "Gurgaon",
        "state": "HARYANA",
        "pincode": 122018
      },
      "registration_address": {
        "address_line": "M1704, banashankari",
        "city": "Gurgaon",
        "state": "HARYANA",
        "pincode": 122018
      },
      "status": "third_party_on_hold"
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
  | Parameter                     | Description                            | Example                                  |
  | :---------------------------- | :------------------------------------- | :--------------------------------------- |
  | merchant.mid                  | `integer` — Merchant ID                | `760070201`                              |
  | merchant.registration_address | `object` — Registered business address | `{ address_line, city, state, pincode }` |
  | merchant.operating_address    | `object` — Operating / office address  | `{ address_line, city, state, pincode }` |
  | merchant.status               | `string` — Current onboarding status   | `third_party_on_hold`                    |
</Accordion>

## Additional request parameters info

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
  | Parameter                                                                  | Description                        | Example           |
  | :------------------------------------------------------------------------- | :--------------------------------- | :---------------- |
  | merchant\[registration_address]\[address_line]<br /><code>mandatory</code> | `string` — Registered address line | `123 MG Road`     |
  | merchant\[registration_address]\[city]<br /><code>mandatory</code>         | `string` — City                    | `Bangalore`       |
  | merchant\[registration_address]\[state]<br /><code>mandatory</code>        | `string` — Valid Indian state      | `Karnataka`       |
  | merchant\[registration_address]\[pincode]<br /><code>mandatory</code>      | `string` — 6-digit pincode         | `560001`          |
  | merchant\[operating_address]\[address_line]<br /><code>mandatory</code>    | `string` — Operating address line  | `456 Indiranagar` |
  | merchant\[operating_address]\[city]<br /><code>mandatory</code>            | `string` — City                    | `Bangalore`       |
  | merchant\[operating_address]\[state]<br /><code>mandatory</code>           | `string` — Valid Indian state      | `Karnataka`       |
  | merchant\[operating_address]\[pincode]<br /><code>mandatory</code>         | `string` — 6-digit pincode         | `560038`          |
</Accordion>
