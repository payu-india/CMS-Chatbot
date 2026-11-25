---
api:
  file: partner-resend-card-otp-api.yaml
  operationId: partnerResendCardOtp
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/resendCardOtp
  </Card>
</Cards>

## Environments

|                        |                                                        |
| :--------------------- | :----------------------------------------------------- |
| Test Environment       | `https://test-partnerapilayer.payu.in/apilayer` |
| Production Environment | `https://api.payu.in` |

## Sample Request

<Accordion title="Request Payload" icon="fa-code">
  ```curl
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/resendCardOtp" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "merchant_id": 8739528,
      "reseller_id": "YOUR_RESELLER_UUID",
      "hash": "YOUR_HASH",
      "reference_id": "REFERENCE_ID"
    }'
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-resend-card-otp-api#body-params) section for request parameter description.
</Callout>

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
    "errors": [
      "reference_id is mandatory."
    ]
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-resend-card-otp-api#response-schemas) section for response parameter description.
</Callout>
