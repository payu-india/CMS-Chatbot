---
api:
  file: partner-refund-callback-api.yaml
  operationId: partnerRefundCallback
hidden: false
link:
  new_tab: false
---
<Cards>
  <Card title="Method">
    POST
  </Card>

  <Card title="Endpoint">
    /partner/refundCallback
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
  curl -X POST "https://test-partnerapilayer.payu.in/apilayer/partner/refundCallback" \
    -H "Content-Type: application/json" \
    -d '{
      "mihpayid": "403993715521855092",
      "request_id": "REQ1001",
      "amt": "100.00",
      "status": "success",
      "token": "refund_token_001",
      "bank_ref_num": "1234567890",
      "bank_arn": "ARN1001",
      "refund_mode": "CC",
      "action": "refund",
      "merchantTxnId": "TXN1001",
      "partnerName": "Partner",
      "remark": "Refund completed",
      "key": "YOUR_MERCHANT_KEY",
      "additionalValue1": "value1",
      "additionalValue2": "value2",
      "paymentId": "403993715521855092",
      "refundId": "REF1001",
      "refundAmount": "100.00",
      "refundStatus": "Refund Completed",
      "notificationId": "NOTIF1001",
      "completedOn": "2026-11-25T10:00:00",
      "addedOn": "2026-11-25T09:00:00"
    }'
```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Request Parameter Description**

  Refer to the [Request Body](https://docs.payu.in/reference/partner-refund-callback-api#body-params) section for request parameter description.
</Callout>

## Sample Response

<Accordion title="Response Payload" icon="fa-code">
  ```json Success Response
  {
    "note": "processRefundCallbackResponse returns void. PayU does not document a JSON acknowledgement body."
  }
  ```
</Accordion>

<Callout icon="📘" theme="info">
  ### **Response Parameter Description**

  Refer to the [Responses](https://docs.payu.in/reference/partner-refund-callback-api#response-schemas) section for response parameter description.
</Callout>
