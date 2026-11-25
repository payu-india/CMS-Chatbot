---
title: Get EMI amount API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
PartnerService.getEmiAmount requires merchant_id and amount. merchant_id must be digits. The map is forwarded to the EMI-as-per-interest service. bankcode and tenure are not checked in this method.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/getEmiAmount` |
| **Production** | `POST` | `https://api.payu.in/partner/getEmiAmount` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| Authorization<br />**mandatory** | `String` Partner access token. Send as Authorization Bearer token. | Bearer YOUR_ACCESS_TOKEN |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| merchant_id<br />**mandatory** | `String` Digits only. Parsed to an integer after the format check. | 8739528 |
| amount<br />**mandatory** | `String` Amount | 1000.00 |
| bankcode<br />**optional** | `String` Forwarded with the map. Not validated in PartnerService.getEmiAmount. | HDFC |
| tenure<br />**optional** | `String` Forwarded with the map. The method signature is Map of strings, so send tenure as a string. | 3 |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/getEmiAmount' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "merchant_id": "8739528",
  "amount": "1000.00",
  "bankcode": "HDFC",
  "tenure": "3"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | EMI interest service JSON, passed through. |
| `400` | merchant_id or amount is missing, or merchant_id is not digits. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200

EMI interest service JSON, passed through.

### HTTP 400 — error

```json
{
  "error": "merchant_id or amount param is missing in body"
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
