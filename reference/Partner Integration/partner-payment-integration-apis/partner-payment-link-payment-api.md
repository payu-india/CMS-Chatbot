---
api:
  file: partner-payment-link-payment-api.yaml
  operationId: partnerPaymentLinkPayment
hidden: false
---

Start payment for a payment link. Required body fields are `payment_link_id` and `phone_number`.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/payment-link/payment
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "payment_link_id": "https://u.payu.in/PAYUID",
  "phone_number": "9999999999",
  "redirect_url": "https://merchant.example.com/return"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The body is the payment-link initiation result from processTxnDataResponseAndInitiatePayment."
}
```
</Accordion>
