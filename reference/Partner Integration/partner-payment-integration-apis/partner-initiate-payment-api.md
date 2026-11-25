---
api:
  file: partner-initiate-payment-api.yaml
  operationId: partnerInitiatePayment
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/initiatePayment
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/initiatePayment" \
    -H "X-PayU-Reseller-UUID: YOUR_RESELLER_UUID" \
    -H "X-Partner-Token: Bearer YOUR_ACCESS_TOKEN" \
    -H "Authorization: HMAC YOUR_HMAC" \
    -H "date: VALUE" \
    -H "Content-Type: application/json" \
    -d '{
      "accountId": "YOUR_MERCHANT_KEY",
      "txnId": "PARTNER_TXN_001",
      "amount": "1000.00",
      "currency": "INR"
    }'
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-initiate-payment-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "Core Payments V2 response, passed through. The Partner QR guide returns mihpayId for the next QR call."
  }
  ```
  ```json Error Response
  {
    "error": "accountId is required in request body"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-initiate-payment-api#response-schemas) section for response parameter description.
</Callout>
