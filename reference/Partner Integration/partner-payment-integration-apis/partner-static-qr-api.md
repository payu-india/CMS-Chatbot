---
api:
  file: partner-static-qr-api.yaml
  operationId: partnerStaticQr
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/staticQr
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/staticQr" \
    -H "X-PayU-Reseller-UUID: YOUR_RESELLER_UUID" \
    -H "X-PayU-Merchant-ID: 8739528" \
    -H "X-Partner-Token: Bearer YOUR_ACCESS_TOKEN" \
    -H "X-Partner-Hash: YOUR_HASH" \
    -H "X-Partner-Request-ID: REQUEST_001" \
    -H "Content-Type: application/json" \
    -d '{
      "merchantVpa": "merchant@payu",
      "qrType": "UPI",
      "udf5": "web",
      "amount": "1000.00"
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-static-qr-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "qrString": "merchant@payu",
    "qrId": "QR_1001",
    "merchantVpa": "merchant@payu"
  }
  ```
  ```json Error Response
  {
    "error": "merchantVpa is required in request body"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-static-qr-api#response-schemas) section for response parameter description.
</Callout>
