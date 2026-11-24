---
api:
  file: partner-initiate-payment-api.yaml
  operationId: partnerInitiatePayment
hidden: false
---

Create a payment and receive a PayU payment id. Authentication is the partner HMAC headers, not a bearer token alone. The body field for the merchant is `accountId`.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/initiatePayment
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/initiatePayment' \
--header 'Content-Type: application/json' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-Partner-Token: Bearer YOUR_ACCESS_TOKEN' \
--header 'Authorization: HMAC YOUR_HMAC' \
--data '{
  "accountId": "YOUR_MERCHANT_KEY",
  "txnId": "PARTNER_TXN_001",
  "amount": 10000,
  "currency": "INR",
  "order": {
    "productInfo": "Product description",
    "paymentChargeSpecification": { "price": 10000 }
  },
  "additionalInfo": { "txnFlow": "nonseamless", "createOrder": "false" },
  "callBackActions": {
    "successAction": "https://merchant.example.com/success",
    "failureAction": "https://merchant.example.com/failure",
    "cancelAction": "https://merchant.example.com/cancel",
    "returnAction": "https://merchant.example.com/return"
  },
  "billingDetails": {
    "firstName": "John",
    "phone": "9999999999",
    "email": "customer@example.com",
    "address1": "Address line 1",
    "city": "Bengaluru",
    "state": "Karnataka",
    "country": "India",
    "zipCode": "560001"
  }
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "note": "The body is the Core Payments POST /v2/payments response. The Partner QR guide uses mihpayId from this response in the dynamic QR call."
}
```
```json Error Response
{
  "error": "accountId is required in request body"
}
```
</Accordion>
