---
api:
  file: partner-static-qr-callback-api.yaml
  operationId: partnerStaticQrCallback
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/staticQrCallback
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/staticQrCallback" \
    -H "Content-Type: application/json" \
    -d '{
      "txnid": "TXN1001",
      "field4": "merchant@payu",
      "key": "YOUR_MERCHANT_KEY"
    }'
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-static-qr-callback-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "Accepted, including a duplicate txnid. Empty body."
  }
  ```
  ```json Error Response
  "field4 (merchantVpa) is required"
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-static-qr-callback-api#response-schemas) section for response parameter description.
</Callout>
