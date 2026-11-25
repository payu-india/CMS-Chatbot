---
title: Payment S2S Callback API
deprecated: false
hidden: false
link:
  new_tab: false
metadata:
  robots: index
---
Server-to-server postback to PayU at POST /partner/paymentCallback. PartnerService.paymentCallback returns HTTP 200 with an empty body after it notifies the partner webhook. The partner webhook URL is configured for the reseller. It is not this path.

## Environment

| Environment    | Method | URL |
| :------------- | :----- | :-- |
| **Test**       | `POST` | `https://test-partnerapilayer.payu.in/apilayer/partner/paymentCallback` |
| **Production** | `POST` | `https://api.payu.in/partner/paymentCallback` |

## Request parameters

### Request headers

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| Content-Type<br />**mandatory** | `String` Send the body as `application/x-www-form-urlencoded`. | application/x-www-form-urlencoded |

### Form parameters

| **Parameter** | **Description** | **Example** |
| :------------ | :-------------- | :---------- |
| mihpayid | `String` PayU payment id. | 403993715521855092 |
| txnid | `String` Merchant transaction id. The handler also accepts `txnId`. | TXN1001 |
| amount | `String` Amount | 1000.00 |
| status | `String` Payment status posted by PayU, such as success or failure. | success |
| mode | `String` Mode | CC |
| productinfo | `String` Productinfo | Order |
| firstname | `String` Firstname | John |
| email | `String` Email | customer@example.com |
| phone | `String` Phone | 9999999999 |
| hash | `String` Response hash. Verify with SHA-512 before trusting the postback. See custom_blocks/HashingSample.md for the payment hash preimage. | YOUR_HASH |
| bankcode | `String` Bankcode | HDFC |
| bank_ref_num | `String` Bank ref num | 1234567890 |
| udf1 | `String` Udf1 | custom_value_1 |
| udf2 | `String` Udf2 | custom_value_2 |
| udf3 | `String` Udf3 | custom_value_3 |
| udf4 | `String` Udf4 | custom_value_4 |
| udf5 | `String` Udf5 | web |
| error | `String` Error | E000 |
| error_Message | `String` Error Message | No Error |
| net_amount_debit | `String` Net amount debit | 1000.00 |
| PG_TYPE | `String` PG TYPE | CC-PG |
| unmappedstatus | `String` Read by PartnerService.paymentCallback when verifying status. | captured |
| key | `String` Merchant key. Used to look up the partner transaction. | YOUR_MERCHANT_KEY |

## Sample request

```curl
curl --location --request POST 'https://test-partnerapilayer.payu.in/apilayer/partner/paymentCallback' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data 'mihpayid=403993715521855092' \
--data 'txnid=TXN1001' \
--data 'amount=1000.00' \
--data 'status=success' \
--data 'mode=CC' \
--data 'productinfo=Order' \
--data 'firstname=John' \
--data 'email=customer@example.com' \
--data 'phone=9999999999' \
--data 'hash=YOUR_HASH' \
--data 'bankcode=HDFC' \
--data 'bank_ref_num=1234567890' \
--data 'udf1=custom_value_1' \
--data 'udf2=custom_value_2' \
--data 'udf3=custom_value_3' \
--data 'udf4=custom_value_4' \
--data 'udf5=web' \
--data 'error=E000' \
--data 'error_Message=No Error' \
--data 'net_amount_debit=1000.00' \
--data 'PG_TYPE=CC-PG' \
--data 'unmappedstatus=captured' \
--data 'key=YOUR_MERCHANT_KEY'
```

## Response parameters

| HTTP status | Description |
| :---------- | :---------- |
| `200` | PayU accepted the postback. paymentCallback returns an empty 200 body. |
| `400` | paymentCallback returns this when payment status validation fails. |

## Sample response

### HTTP 200

PayU accepted the postback. paymentCallback returns an empty 200 body.

### HTTP 400 — error

```
payment status validation failed
```
