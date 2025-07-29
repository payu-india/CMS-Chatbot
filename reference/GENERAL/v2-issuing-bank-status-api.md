---
title: v2 Issuing Bank Status API
deprecated: false
hidden: false
metadata:
  robots: index
---
**Environment**

<br />

|            |                                                                                      |
| :--------- | :----------------------------------------------------------------------------------- |
| Production | [https://info.payu.in/issuing-bank/v1/bin](https://info.payu.in/issuing-bank/v1/bin) |
| Test       | [https://test.payu.in/issuing-bank/v1/bin](https://test.payu.in/issuing-bank/v1/bin) |

# Request header

<V2_payment_header_params />

<br />

## Request body

<HTMLBlock>{`

`}</HTMLBlock>

<br />

## Sample request

```
curl --location 'https://info.payu.in/issuing-bank/v1/bin/?bin=512345&issuing_bank_status=true' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```