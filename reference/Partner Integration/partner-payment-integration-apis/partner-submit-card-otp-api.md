---
api:
  file: partner-submit-card-otp-api.yaml
  operationId: partnerSubmitCardOtp
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/submitCardOtp
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/submitCardOtp" \
    -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
    -H "Content-Type: application/json" \
    -d '{
      "merchant_id": 8739528,
      "reseller_id": "YOUR_RESELLER_UUID",
      "hash": "YOUR_HASH",
      "reference_id": "REFERENCE_ID",
      "otp": "123456"
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-submit-card-otp-api#body-params) section for request parameter description.
</Callout>

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
    "errors": [
      "reference_id is mandatory."
    ]
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-submit-card-otp-api#response-schemas) section for response parameter description.
</Callout>
