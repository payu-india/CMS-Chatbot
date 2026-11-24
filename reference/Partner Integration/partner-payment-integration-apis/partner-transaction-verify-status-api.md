---
api:
  file: partner-transaction-verify-status-api.yaml
  operationId: partnerTransactionVerifyStatus
hidden: false
---

Check Bharat QR transaction status. `txnId` is an array of transaction ids.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/transaction/verifyStatus
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/transaction/verifyStatus' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Merchant-Key: YOUR_MERCHANT_KEY' \
--header 'Authorization: HMAC YOUR_HMAC' \
--data '{
  "txnId": ["PARTNER_TXN_001"]
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The body is the Bharat QR status payload from the downstream status command."
}
```
</Accordion>
