---
api:
  file: partner-submit-card-otp-api.yaml
  operationId: partnerSubmitCardOtp
hidden: false
---

Submit the card OTP for a transaction identified by `reference_id`.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/submitCardOtp
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/submitCardOtp' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "hash": "YOUR_HASH",
  "reference_id": "REFERENCE_ID",
  "otp": "123456"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "status": "success",
  "attemptsLeft": 2,
  "isSupported": true,
  "txnStatus": "success",
  "mihpayid": "403993715521855092",
  "message": "OTP verified successfully"
}
```
```json Error Response
{
  "status": "failed",
  "message": "Invalid OTP",
  "attemptsLeft": 2
}
```
</Accordion>
