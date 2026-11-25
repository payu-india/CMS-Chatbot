---
api:
  file: partner-get-emi-amount-api.yaml
  operationId: partnerGetEmiAmount
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/getEmiAmount
  </Card>
</Cards>

## Environments

|                        |                                                        |
| :--------------------- | :----------------------------------------------------- |
| Test Environment       | `https://test-partnerapilayer.payu.in/apilayer` |
| Production Environment | `https://api.payu.in` |

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/getEmiAmount" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "merchant_id": "8739528",
      "amount": "1000.00",
      "bankcode": "HDFC",
      "tenure": "3"
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-get-emi-amount-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "EMI interest service JSON, passed through."
  }
  ```
  ```json Error Response
  {
    "error": "merchant_id or amount param is missing in body"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-get-emi-amount-api#response-schemas) section for response parameter description.
</Callout>
