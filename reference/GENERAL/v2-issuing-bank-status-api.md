---
title: v2 Issuing Bank Status API
deprecated: false
hidden: false
metadata:
  robots: index
---
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