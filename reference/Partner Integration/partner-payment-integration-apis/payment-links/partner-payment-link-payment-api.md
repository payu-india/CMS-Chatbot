---
title: Payment link payment API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
POST /partner/payment-link/payment. PartnerPaymentLinkTxnDTO fields are payment_link_id, phone_number, and redirect_url. validatePaymentLinkRequest requires payment_link_id and phone_number. phone_number must match (^$|[0-9]{5,16}). merchant_id, txnid, pg, bankcode, and card fields are not on this DTO.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment` |
| **Production** | `POST` | `https://api.payu.in/partner/payment-link/payment` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| Authorization<br />**mandatory** | `String` Partner access token. Send as Authorization Bearer token. | Bearer YOUR_ACCESS_TOKEN |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| payment_link_id<br />**mandatory** | `String` Payment link id | https://u.payu.in/PAYUID |
| phone_number<br />**mandatory** | `String` 5 to 16 digits, or empty. Empty is rejected by the required check. | 9999999999 |
| redirect_url<br />**optional** | `String` Optional in the DTO. When present, the domain is validated. | https://merchant.example.com/return |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/payment-link/payment' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "payment_link_id": "https://u.payu.in/PAYUID",
  "phone_number": "9999999999",
  "redirect_url": "https://merchant.example.com/return"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Downstream payment-link transaction response, after processTxnDataResponseAndInitiatePayment. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200

Downstream payment-link transaction response, after processTxnDataResponseAndInitiatePayment.

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
