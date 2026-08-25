---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: List_Business_members_API
hidden: false
---
---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: List_Business_members_API
hidden: false
---
The **List Business Members** API retrieves business members already submitted for the merchant (Step 13 utility).

Use this after **Submit Business Members** to confirm what PayU has stored.

**HTTP Method**: GET

**Environment**

|                        | URL |
| :--------------------- | :-- |
| Test Environment       | `https://test-partner.payu.in/api/v1/merchants/{uuid}/list_business_members` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/list_business_members` |

## Sample Request

<Accordion title="Sample request" icon="fa-code">

```bash
curl --location 'https://test-partner.payu.in/api/v1/merchants/{{uuid}}/list_business_members' \
--header 'Authorization: Bearer {{access_token}}' \
--header 'Accept: application/json'
```

</Accordion>

## Sample Response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">

```json
{
  "business_members": [
    {
      "name": "Director Name",
      "pancard_number": "ABCDE1234F",
      "designation": "Director"
    }
  ]
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
| business_members | `array` — Submitted business members | `[{ name, pancard_number, designation }]` |

</Accordion>

## Request parameters

### Header parameters

<Accordion title="Header parameters" icon="fa-table">

| Header | Description | Example |
| :-------- | :-------- | :-------- |
| Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
| Accept<br /><code>optional</code> | `string` — Preferred response media type | `application/json` |

</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">

| Parameter | Description | Example |
| :-------- | :-------- | :-------- |
| uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |

</Accordion>