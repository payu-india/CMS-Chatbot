---
api:
  file: partner-payment-link-verify-payment-api.yaml
  operationId: partnerPaymentLinkVerifyPayment
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /partner/payment-link/verifyPayment
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
  curl -X GET "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=ORDER1001&payment_link_id=https://u.payu.in/PAYUID" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Query Parameters](https://docs.payu.in/reference/partner-payment-link-verify-payment-api#query-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "order_ref_id": "ORDER1001",
    "payment_link_id": "https://u.payu.in/PAYUID",
    "order_status": "success",
    "payments": [
      {
        "payment_id": "403993715521855092",
        "status": "success",
        "method": "UPI"
      }
    ]
  }
  ```
  ```json Error Response
  {
    "error": "Invalid Auth token"
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-payment-link-verify-payment-api#response-schemas) section for response parameter description.
</Callout>
