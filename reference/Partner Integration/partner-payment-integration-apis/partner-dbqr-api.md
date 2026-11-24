---
api:
  file: partner-dbqr-api.yaml
  operationId: partnerDbqr
hidden: false
---

Generate a dynamic Bharat QR for one transaction. Call this after initiate payment, using `mihpayId` from that response.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/dbqr
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/dbqr' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Merchant-Key: YOUR_MERCHANT_KEY' \
--header 'Authorization: HMAC YOUR_HMAC' \
--data '{
  "mihpayId": "403993715529984752",
  "vendorTransactionId": "PARTNER_TXN_001",
  "transactionAmount": "100.00",
  "expiryTime": "3600",
  "soundBoxTerminalId": "ABCD1234"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "status": "success",
  "result": {
    "qrString": "000201010212..."
  }
}
```
</Accordion>
