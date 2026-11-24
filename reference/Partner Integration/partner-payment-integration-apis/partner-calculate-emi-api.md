---
api:
  file: partner-calculate-emi-api.yaml
  operationId: partnerCalculateEmi
hidden: false
---

Calculate EMI options. PartnerService checks `merchant_id` and forwards the remaining fields.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/calculateEmi
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/calculateEmi' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "merchant_id": "8739528",
  "amount": "10000.00",
  "bankcode": "HDFC"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The HTTP 200 body is the EMI calculator payload."
}
```
```json Error Response
{
  "error": "merchant_id param is missing in the body"
}
```
</Accordion>
