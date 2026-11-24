---
api:
  file: partner-fetch-offer-api.yaml
  operationId: partnerFetchOffer
hidden: false
---

Fetch offers for a merchant. Send the bearer token from the partner token APIs.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/fetchOffer
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/fetchOffer' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "amount": "1000.00",
  "hash": "YOUR_HASH"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The HTTP 200 body is the PayU Offers service payload, unchanged by PartnerService.fetchOffer."
}
```
```json Error Response
{
  "errors": ["merchant_id is mandatory"]
}
```
</Accordion>
