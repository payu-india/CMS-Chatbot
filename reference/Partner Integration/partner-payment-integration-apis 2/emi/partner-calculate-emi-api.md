---
title: Calculate EMI API [New]
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
PartnerService.calculateEmi requires merchant_id (digits). reseller_id is removed before the downstream call. Other fields are forwarded after merchant_id is removed. amount and bankcode are not validated here.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/calculateEmi` |
| **Production** | `POST` | `https://api.payu.in/partner/calculateEmi` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| Authorization<br />**mandatory** | `String` Partner access token. Send as Authorization Bearer token. | Bearer YOUR_ACCESS_TOKEN |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| merchant_id<br />**mandatory** | `String` Merchant id | 8739528 |
| amount<br />**optional** | `String` Forwarded. Not validated in PartnerService.calculateEmi. | 1000.00 |
| bankcode<br />**optional** | `String` Forwarded. Not validated in PartnerService.calculateEmi. | HDFC |
| reseller_id<br />**optional** | `String` Removed before the downstream EMI call. | YOUR_RESELLER_UUID |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/calculateEmi' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "merchant_id": "8739528",
  "amount": "1000.00",
  "bankcode": "HDFC",
  "reseller_id": "YOUR_RESELLER_UUID"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | EMI calculator JSON, passed through. |
| `400` | merchant_id is missing or not digits. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200

EMI calculator JSON, passed through.

### HTTP 400 — error

```json
{
  "error": "merchant_id param is missing in the body"
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
