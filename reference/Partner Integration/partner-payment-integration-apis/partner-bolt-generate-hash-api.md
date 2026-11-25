---
api:
  file: partner-bolt-generate-hash-api.yaml
  operationId: partnerBoltGenerateHash
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/bolt/generateHash
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/bolt/generateHash" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "X-PayU-Reseller-UUID: YOUR_RESELLER_UUID" \
    -H "X-PayU-Merchant-ID: 8739528" \
    -H "Content-Type: application/json" \
    -d '{
      "txnid": "TXN1001",
      "amount": "1000.00",
      "productinfo": "Order",
      "firstname": "John",
      "email": "customer@example.com",
      "phone": "9999999999",
      "surl": "https://merchant.example.com/success",
      "furl": "https://merchant.example.com/failure"
    }'
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-bolt-generate-hash-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "key": "YOUR_MERCHANT_KEY",
    "hash": "YOUR_SHA512_HASH",
    "txnid": "TXN1001",
    "amount": "10.00",
    "productinfo": "Order",
    "firstname": "John",
    "email": "customer@example.com",
    "phone": "9999999999",
    "surl": "https://merchant.example.com/success",
    "furl": "https://merchant.example.com/failure"
  }
  ```
  ```json Error Response
  {
    "errors": [
      "txnid is mandatory param."
    ]
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-bolt-generate-hash-api#response-schemas) section for response parameter description.
</Callout>
