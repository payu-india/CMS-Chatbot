---
title: Partner Refund Callback API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
PayU receives the refund notification at POST /partner/refundCallback. PartnerController accepts a JSON object. RefundCallbackDTO is the non-migrated shape. RefundCallbackMigratedDTO is the migrated shape (paymentId, refundId, refundAmount, refundStatus). Both sets are listed. No field is required by the controller.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/refundCallback` |
| **Production** | `POST` | `https://api.payu.in/partner/refundCallback` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| mihpayid | `String` Mihpayid | 403993715521855092 |
| request_id | `String` Request id | REQ1001 |
| amt | `String` Refunded amount on the non-migrated payload. | 100.00 |
| status | `String` Non-migrated status. PartnerService treats success, queued, and failure. | success |
| token | `String` Token | refund_token_001 |
| bank_ref_num | `String` Bank ref num | 1234567890 |
| bank_arn | `String` Bank arn | ARN1001 |
| refund_mode | `String` Refund mode | CC |
| action | `String` Action | refund |
| merchantTxnId | `String` MerchantTxnId | TXN1001 |
| partnerName | `String` PartnerName | Partner |
| remark | `String` Remark | Refund completed |
| key | `String` Key | YOUR_MERCHANT_KEY |
| additionalValue1 | `String` AdditionalValue1 | value1 |
| additionalValue2 | `String` AdditionalValue2 | value2 |
| paymentId | `String` Migrated payload. Same role as mihpayid. | 403993715521855092 |
| refundId | `String` Migrated payload. Same role as request_id. | REF1001 |
| refundAmount | `String` RefundAmount | 100.00 |
| refundStatus | `String` Migrated payload. Code comment says the value is Refund Completed. | Refund Completed |
| notificationId | `String` NotificationId | NOTIF1001 |
| completedOn | `String` CompletedOn | 2026-11-25T10:00:00 |
| addedOn | `String` AddedOn | 2026-11-25T09:00:00 |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/refundCallback' \
--header 'Content-Type: application/json' \
--data '{
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

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | processRefundCallbackResponse returns void. PayU does not document a JSON acknowledgement body. |

## Sample response

### HTTP 200

processRefundCallbackResponse returns void. PayU does not document a JSON acknowledgement body.
