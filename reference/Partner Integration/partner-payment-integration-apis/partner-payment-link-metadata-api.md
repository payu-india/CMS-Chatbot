---
api:
  file: partner-payment-link-metadata-api.yaml
  operationId: partnerPaymentLinkMetadata
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /partner/payment-link/metadata
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
  curl -X GET "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=https://u.payu.in/PAYUID" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Query Parameters](https://docs.payu.in/reference/partner-payment-link-metadata-api#query-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "amount": 1000.0,
    "currency": "INR",
    "description": "Order 1001",
    "payment_link_id": "https://u.payu.in/PAYUID",
    "payment_link_status": "active",
    "expiry_time": 1735689600
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

  Refer to the [Responses](https://docs.payu.in/reference/partner-payment-link-metadata-api#response-schemas) section for response parameter description.
</Callout>
