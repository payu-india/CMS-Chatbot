---
api:
  file: partner-dbqr-api.yaml
  operationId: partnerDbqr
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/dbqr
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/dbqr" \
    -H "X-PayU-Reseller-UUID: YOUR_RESELLER_UUID" \
    -H "X-Partner-Token: Bearer YOUR_ACCESS_TOKEN" \
    -H "Authorization: HMAC YOUR_HMAC" \
    -H "X-PayU-Merchant-Key: VALUE" \
    -H "X-PayU-Merchant-ID: VALUE" \
    -H "date: VALUE" \
    -H "Content-Type: application/json" \
    -d '{
      "mihpayId": "403993715529984752",
      "vendorTransactionId": "PARTNER_TXN_001",
      "transactionAmount": "100.00",
      "expiryTime": "3600",
      "soundBoxTerminalId": "ABCD1234"
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-dbqr-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "status": "success",
    "result": {
      "qrString": "000201010212..."
    }
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-dbqr-api#response-schemas) section for response parameter description.
</Callout>
