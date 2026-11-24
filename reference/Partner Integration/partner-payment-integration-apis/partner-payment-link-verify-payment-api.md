---
api:
  file: partner-payment-link-verify-payment-api.yaml
  operationId: partnerPaymentLinkVerifyPayment
hidden: false
---

Verify a payment-link order. Query parameters are `order_ref_id` and `payment_link_id`.

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /partner/payment-link/verifyPayment
  </Card>
</Cards>


## Environment

| Environment | Base URL |
| --- | --- |
| Production | `https://api.payu.in` |
| UAT | `https://test-partnerapilayer.payu.in/apilayer` |



## Sample Request

<Accordion title="Request Payload" icon="fa-code">
```curl
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/verifyPayment?order_ref_id=ORDER1001&payment_link_id=https%3A%2F%2Fu.payu.in%2FPAYUID' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```
</Accordion>

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
</Accordion>
