---
title: v2 Get BIN Info API
deprecated: false
hidden: false
metadata:
  robots: index
---
## Sample request

```
curl --location 'https://info.payu.in/issuing-bank/v1/bin' \
--header 'Content-Type: application/json' \
--header 'date: {{date}}' \
--header 'Authorization: {{authorization}}' \
--data '{
    "bin": "512345"
  }'
```