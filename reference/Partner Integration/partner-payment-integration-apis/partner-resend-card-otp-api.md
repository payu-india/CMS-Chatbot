---
api:
  file: partner-resend-card-otp-api.yaml
  operationId: partnerResendCardOtp
hidden: false
---

Resend the card OTP for `reference_id`.

<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/resendCardOtp
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
curl --location 'https://test-partnerapilayer.payu.in/apilayer/partner/resendCardOtp' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
  "merchant_id": 8739528,
  "reseller_id": "YOUR_RESELLER_UUID",
  "hash": "YOUR_HASH",
  "reference_id": "REFERENCE_ID"
}'
```
</Accordion>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
```json Success Response
{
  "status": "success",
  "message": "OTP resent successfully",
  "attemptsLeft": 2,
  "isSupported": true
}
```
```json Error Response
{
  "status": "failed",
  "message": "Error processing OTP resend"
}
```
</Accordion>
