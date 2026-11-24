---
api:
  file: partner-validate-offer-api.yaml
  operationId: partnerValidateOffer
hidden: false
---

Validate whether an offer applies to a payment. `paymentDetail.category` and `userDetail.userToken` are required.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/validateOffer
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/validateOffer' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "hash": "YOUR_HASH",
  "amount": "1000.00",
  "offerKeys": ["OFFER_KEY"],
  "paymentDetail": { "category": "CC" },
  "userDetail": { "userToken": "USER_TOKEN" }
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The HTTP 200 body is the PayU Offers validate payload, unchanged by PartnerService.validateOffer."
}
```
```json Error Response
{
  "errors": ["category is mandatory in paymentDetail."]
}
```
</Accordion>
