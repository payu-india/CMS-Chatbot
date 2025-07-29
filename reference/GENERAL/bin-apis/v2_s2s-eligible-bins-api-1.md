---
title: S2S Eligible BINs API
deprecated: false
hidden: false
metadata:
  robots: index
---
The **S2S Eligible BINs** API is similar to the **Get BIN Info** API, but used in S2S environment. For more information on Get BIN Info API, refer to [Get Bin Info API](ref:v2-get-bin-info-api).

## Environment

| Environment            | URL                                                                                          |
| :--------------------- | :------------------------------------------------------------------------------------------- |
| Production Environment | [https://info.payu.in/issuing-bank/v1/bin?s2s](https://info.payu.in/issuing-bank/v1/bin?s2s) |
| Test Environment       | [https://test.payu.in/issuing-bank/v1/bin?s2s](https://test.payu.in/issuing-bank/v1/bin?s2s) |

## Request header

<V2_payment_header_params />

## Request body

## Sample request

```
curl --location 'https://info.payu.in/issuing-bank/v1/bin?s2s' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```