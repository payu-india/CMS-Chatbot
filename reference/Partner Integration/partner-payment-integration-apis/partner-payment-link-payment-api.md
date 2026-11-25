---
api:
  file: partner-payment-link-payment-api.yaml
  operationId: partnerPaymentLinkPayment
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/payment-link/payment
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "payment_link_id": "https://u.payu.in/PAYUID",
      "phone_number": "9999999999",
      "redirect_url": "https://merchant.example.com/return"
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-payment-link-payment-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "Downstream payment-link transaction response, after processTxnDataResponseAndInitiatePayment."
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

  Refer to the [Responses](https://docs.payu.in/reference/partner-payment-link-payment-api#response-schemas) section for response parameter description.
</Callout>
