---
title: Get eligible EMI bins API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
PartnerService.getEligibleBins requires merchant_id, type, and var2. pg and offer_type are not read by this method. The map is forwarded to the eligible-bins service.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/getEligibleBins` |
| **Production** | `POST` | `https://api.payu.in/partner/getEligibleBins` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| Authorization<br />**mandatory** | `String` Partner access token. Send as Authorization Bearer token. | Bearer YOUR_ACCESS_TOKEN |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| merchant_id<br />**mandatory** | `String` Digits only. | 8739528 |
| type<br />**mandatory** | `String` Required by PartnerService. Forwarded to the eligible-bins service. | bin |
| var2<br />**mandatory** | `String` Required by PartnerService. Forwarded to the eligible-bins service. | EMI |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/getEligibleBins' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--data '{
  "merchant_id": "8739528",
  "type": "bin",
  "var2": "EMI"
}'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | Eligible-bins service JSON, passed through. |
| `400` | merchant_id, type, or var2 is missing. |
| `401` | Invalid bearer token. |

## Sample response

### HTTP 200

Eligible-bins service JSON, passed through.

### HTTP 400 — error

```json
{
  "error": "merchant_id, type and var2 param are mandatory params"
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
