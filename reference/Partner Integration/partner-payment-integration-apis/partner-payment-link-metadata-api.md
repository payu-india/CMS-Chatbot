---
api:
  file: partner-payment-link-metadata-api.yaml
  operationId: partnerPaymentLinkMetadata
hidden: false
---

Read metadata for a payment link. Pass `payment_link` as a query parameter.

<Cards>
  <Card title="Method">
    GET
  </Card>

  <Card title="Endpoint">
    /partner/payment-link/metadata
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/metadata?payment_link=https%3A%2F%2Fu.payu.in%2FPAYUID' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN'
```
</Accordion>

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
</Accordion>
