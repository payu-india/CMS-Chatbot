---
api:
  file: partner-get-emi-amount-api.yaml
  operationId: partnerGetEmiAmount
hidden: false
---

Get the EMI instalment for a merchant and amount. `merchant_id` and `amount` are the fields PartnerService checks.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/getEmiAmount
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/getEmiAmount' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "merchant_id": "8739528",
  "amount": "10000.00"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The HTTP 200 body is the EMI-as-per-interest service payload."
}
```
```json Error Response
{
  "error": "merchant_id or amount param is missing in body"
}
```
</Accordion>
