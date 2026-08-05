---
api:
  file: payu_partner_api_openapi_3.1_enhanced_v1.yaml
  operationId: SubmitBusinessMembers
hidden: false
---
The **Submit Business Members** API submits directors, partners, or designated partners (Step 13 of 16).

**Entity applicability:** Required for Private Limited, Public Limited, Partnership, and LLP. Not required for Individual, Sole Prop, Trust, Society, or OPC.

**HTTP Method**: PUT

**Environment**

|                        | URL                                                                            |
| :--------------------- | :----------------------------------------------------------------------------- |
| Test Environment       | `https://test-partner.payu.in/api/v1/merchants/{uuid}/submit_business_members` |
| Production Environment | `https://partner.payu.in/api/v1/merchants/{uuid}/submit_business_members`      |

## Sample request

<Accordion title="Sample request" icon="fa-code">
  ```bash
  curl --location --request PUT 'https://test-partner.payu.in/api/v1/merchants/{{uuid}}/submit_business_members' \
  --header 'Authorization: Bearer {{access_token}}' \
  --header 'Content-Type: application/json' \
  --data '{
    "business_members": [
      {
        "name": "Director Name",
        "pancard_number": "ABCDE1234F",
        "designation": "Director"
      }
    ]
  }'
  ```
</Accordion>

## Sample response

### Success scenario

<Accordion title="Success scenario" icon="fa-file-code">
  ```json
  {
    "message": "Business members submitted successfully"
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
  | Parameter | Description                        | Example                                   |
  | :-------- | :--------------------------------- | :---------------------------------------- |
  | message   | `string` — Submission confirmation | `Business members submitted successfully` |
</Accordion>

## Additional request parameters info

### Header parameters

<Accordion title="Header parameters" icon="fa-table">
  | Header                                    | Description                                       | Example                   |
  | :---------------------------------------- | :------------------------------------------------ | :------------------------ |
  | Authorization<br /><code>mandatory</code> | `string` — Bearer token from Step 00 (`GetToken`) | `Bearer {{access_token}}` |
  | Content-Type<br /><code>mandatory</code>  | `string` — Must be `application/json`             | `application/json`        |
</Accordion>

### Path parameters

<Accordion title="Path parameters" icon="fa-table">
  | Parameter                        | Description                                              | Example                                |
  | :------------------------------- | :------------------------------------------------------- | :------------------------------------- |
  | uuid<br /><code>mandatory</code> | `string` — Merchant UUID from Step 01 (`CreateMerchant`) | `11ef-d968-6b042d6c-9b94-02975f21d323` |
</Accordion>

### Body parameters

<Accordion title="Body parameters" icon="fa-table">
  | Parameter                                                      | Description                               | Example                                   |
  | :------------------------------------------------------------- | :---------------------------------------- | :---------------------------------------- |
  | business_members<br /><code>mandatory</code>                   | `array` — List of business member objects | `[{ name, pancard_number, designation }]` |
  | business_members\[].name<br /><code>mandatory</code>           | `string` — Member name                    | `Director Name`                           |
  | business_members\[].pancard_number<br /><code>mandatory</code> | `string` — Member PAN                     | `ABCDE1234F`                              |
  | business_members\[].designation<br /><code>mandatory</code>    | `string` — Role (e.g. Director, Partner)  | `Director`                                |
</Accordion>
