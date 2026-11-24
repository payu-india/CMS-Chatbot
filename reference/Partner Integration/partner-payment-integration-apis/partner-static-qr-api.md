---
api:
  file: partner-static-qr-api.yaml
  operationId: partnerStaticQr
hidden: false
---

Generate a reusable static QR for a merchant VPA. `X-Partner-Hash` is SHA-512 of `merchantId|rawRequestBody|clientSecret`.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/staticQr
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/staticQr' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-PayU-Merchant-ID: 8739528' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-Partner-Hash: YOUR_HASH' \
--header 'X-Partner-Request-ID: REQUEST_001' \
--data '{
  "merchantVpa": "merchant@payu"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "qrString": "merchant@payu",
  "qrId": "QR_1001",
  "merchantVpa": "merchant@payu"
}
```
```json Error Response
{
  "error": "merchantVpa is required in request body"
}
```
</Accordion>
