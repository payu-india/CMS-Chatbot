---
api:
  file: partner-bolt-generate-hash-api.yaml
  operationId: partnerBoltGenerateHash
hidden: false
---

Ask PayU to build the Checkout Plus launch payload, including the SHA-512 payment hash. You still send `X-PayU-Reseller-UUID` and `X-PayU-Merchant-ID` with the bearer token.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/bolt/generateHash
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/bolt/generateHash' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-PayU-Merchant-ID: 8739528' \
--header 'Content-Type: application/json' \
--data '{
  "txnid": "TXN1001",
  "amount": "10.00",
  "productinfo": "Order",
  "firstname": "John",
  "email": "customer@example.com",
  "phone": "9999999999",
  "surl": "https://merchant.example.com/success",
  "furl": "https://merchant.example.com/failure"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "key": "YOUR_MERCHANT_KEY",
  "hash": "YOUR_SHA512_HASH",
  "txnid": "TXN1001",
  "amount": "10.00",
  "productinfo": "Order",
  "firstname": "John",
  "email": "customer@example.com",
  "phone": "9999999999",
  "surl": "https://merchant.example.com/success",
  "furl": "https://merchant.example.com/failure"
}
```
```json Error Response
{
  "errors": ["txnid is mandatory param."]
}
```
</Accordion>
