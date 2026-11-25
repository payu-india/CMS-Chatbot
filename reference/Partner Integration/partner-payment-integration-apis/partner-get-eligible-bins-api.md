---
api:
  file: partner-get-eligible-bins-api.yaml
  operationId: partnerGetEligibleBins
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/getEligibleBins
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/getEligibleBins" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "merchant_id": "8739528",
      "type": "bin",
      "var2": "EMI"
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-get-eligible-bins-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "Eligible-bins service JSON, passed through."
  }
  ```
  ```json Error Response
  {
    "error": "merchant_id, type and var2 param are mandatory params"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-get-eligible-bins-api#response-schemas) section for response parameter description.
</Callout>
