---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: AddUpdateUBO
hidden: false
---
---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: AddUpdateUBO
hidden: false
---
The **Add/Update UBO** API submits Ultimate Beneficial Owner details (Step 12 of 16).

**Prerequisite:** 

Step 11 (VKYC), as applicable.

**Entity applicability:** 
Required for Private Limited, Public Limited, Partnership, Trust, LLP, and Society. Not required for Individual, Sole Proprietorship, or One Person Company.

Use array indexing (`ubo[0]`, `ubo[1]`, …) for multiple UBOs.

**HTTP Method**: PUT

**Environment**

|                        | URL |
| :--------------------- | :-- |
| Test Environment       | `https://test-partner.payu.in/api/v1/merchants/{uuid}/signatory_details` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/signatory_details` |

## Sample Request

<Accordion title="Sample request" icon="fa-code">

```bash
curl --location --request PUT 'https://test-partner.payu.in/api/v1/merchants/{{uuid}}/signatory_details' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'ubo[0][name]=UBO Name' \
--data-urlencode 'ubo[0][pancard_number]=ABCDE1234F' \
--data-urlencode 'ubo[0][ownership_percentage]=30'
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

* **401 Unauthorized** — Token invalid or expired; call Step 00 again

```json
{
  "error": "unauthorized",
  "message": "Invalid or expired token"
}
```

* **422 Validation Failed** — Request parameters failed validation

```json
{
  "error": "validation_failed",
  "message": "Check the error details in the response body"
}
```

</Accordion>

## Response parameters

<Accordion title="Response parameters" icon="fa-table">

| Parameter | Description | Example |
| :-------- | :-------- | :-------- |
| merchant.mid | `integer` — Merchant ID | `12345678` |
| merchant.status | `string` — Current onboarding status | `account_created` |

</Accordion>

## Request parameters

### Header parameters

<Accordion title="Header parameters" icon="fa-table">

| Header | Description | Example |
| :-------- | :-------- | :-------- |
| Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
| Content-Type<br /><code>mandatory</code> | `string` — Must be `application/x-www-form-urlencoded` | `application/x-www-form-urlencoded` |

</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">

| Parameter | Description | Example |
| :-------- | :-------- | :-------- |
| uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |

</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">

| Parameter | Description | Example |
| :-------- | :-------- | :-------- |
| ubo[0][name]<br /><code>mandatory</code> | `string` — UBO full name | `UBO Name` |
| ubo[0][pancard_number]<br /><code>mandatory</code> | `string` — UBO PAN | `ABCDE1234F` |
| ubo[0][ownership_percentage]<br /><code>mandatory</code> | `string` — Ownership percentage (typically 25%+) | `30` |

</Accordion>
