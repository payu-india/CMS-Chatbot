---
title: Bolt generate hash API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
POST /partner/bolt/generateHash. BoltConstants.API_BASE_PATH is /partner/bolt. Headers: Authorization, X-PayU-Reseller-UUID, and X-PayU-Merchant-ID. The 200 body is BoltLaunchPayloadDTO (the object passed to bolt.launch), not a status wrapper. Hash preimage, quoted from BoltHashUtil: key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT, with |additional_charges and |paisa_mecode appended only when those values are present. This is the payment hash in custom_blocks/HashingSample.md.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/bolt/generateHash` |
| **Production** | `POST` | `https://api.payu.in/partner/bolt/generateHash` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/json`. | application/json |
| Authorization<br />**mandatory** | `String` Bearer access token. | Bearer YOUR_ACCESS_TOKEN |
| X-PayU-Reseller-UUID<br />**mandatory** | `String` X-PayU-Reseller-UUID | YOUR_RESELLER_UUID |
| X-PayU-Merchant-ID<br />**mandatory** | `String` X-PayU-Merchant-ID | VALUE |

### Request body

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| txnid<br />**mandatory** | `String` Txnid | TXN1001 |
| amount<br />**mandatory** | `String` Amount | 1000.00 |
| productinfo<br />**mandatory** | `String` Productinfo | Order |
| firstname<br />**mandatory** | `String` Letters and spaces, 1 to 128 characters. | John |
| lastname<br />**optional** | `String` Letters and spaces, up to 128 characters. | Doe |
| email<br />**mandatory** | `String` Email | customer@example.com |
| phone<br />**mandatory** | `String` 5 to 16 digits. | 9999999999 |
| surl<br />**mandatory** | `String` Surl | https://merchant.example.com/success |
| furl<br />**mandatory** | `String` Furl | https://merchant.example.com/failure |
| udf1<br />**optional** | `String` Udf1 | custom_value_1 |
| udf2<br />**optional** | `String` Udf2 | custom_value_2 |
| udf3<br />**optional** | `String` Udf3 | custom_value_3 |
| udf4<br />**optional** | `String` Udf4 | custom_value_4 |
| udf5<br />**optional** | `String` Udf5 | web |
| additional_charges<br />**optional** | `String` Additional charges | 0.00 |
| paisa_mecode<br />**optional** | `String` Paisa mecode | paisa_mecode |
| pg<br />**optional** | `String` Pg | CC |
| bankcode<br />**optional** | `String` Bankcode | HDFC |
| drop_category<br />**optional** | `String` Drop category | NB |
| enforce_paymethod<br />**optional** | `String` Enforce paymethod | UPI |
| custom_note<br />**optional** | `String` Custom note | Deliver before 6 PM |
| note_category<br />**optional** | `String` Note category | delivery |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/bolt/generateHash' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
--header 'X-PayU-Reseller-UUID: YOUR_RESELLER_UUID' \
--header 'X-PayU-Merchant-ID: VALUE' \
--data '{
  "txnid": "TXN1001",
  "amount": "1000.00",
  "productinfo": "Order",
  "firstname": "John",
  "lastname": "Doe",
  "email": "customer@example.com",
  "phone": "9999999999",
  "surl": "https://merchant.example.com/success",
  "furl": "https://merchant.example.com/failure",
  "udf1": "custom_value_1",
  "udf2": "custom_value_2",
  "udf3": "custom_value_3",
  "udf4": "custom_value_4",
  "udf5": "web",
  "additional_charges": "0.00",
  "paisa_mecode": "paisa_mecode",
  "pg": "CC",
  "bankcode": "HDFC",
  "drop_category": "NB",
  "enforce_paymethod": "UPI",
  "custom_note": "Deliver before 6 PM",
  "note_category": "delivery"
}'
```

## Response parameters

### HTTP 200

Checkout Plus launch payload. Only non-null fields are serialized.

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| key | `String` Key | YOUR_MERCHANT_KEY |
| hash | `String` Hash | YOUR_HASH |
| txnid | `String` Txnid | TXN1001 |
| amount | `String` Amount | 1000.00 |
| productinfo | `String` Productinfo | Order |
| firstname | `String` Firstname | John |
| email | `String` Email | customer@example.com |
| phone | `String` Phone | 9999999999 |
| surl | `String` Surl | https://merchant.example.com/success |
| furl | `String` Furl | https://merchant.example.com/failure |

## Sample response

### HTTP 200 — success

```json
{
  "key": "YOUR_MERCHANT_KEY",
  "hash": "YOUR_SHA512_HASH",
  "txnid": "TXN1001",
  "amount": "10.00",
  "productinfo": "Order",
  "firstname": "John",
  "email": "customer@example.com",
  "phone": "9999999999",
  "surl": "https://merchant.example.com/success",
  "furl": "https://merchant.example.com/failure"
}
```

### HTTP 400 — error

```json
{
  "errors": [
    "txnid is mandatory param."
  ]
}
```

### HTTP 401 — error

```json
{
  "error": "Invalid Auth token"
}
```
