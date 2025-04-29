---
title: Account Discovery API
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is to validate if user's account/customer profile exists or not with the merchant basis mobile number or email id identifiers.

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "phone  \n`mandatory`",
    "0-1": "The customer phone number.",
    "1-0": "email  \n`mandatory`",
    "1-1": "The customer email ID.",
    "2-0": "key  \n`mandatory`",
    "2-1": "The merchant key used for encryption that was provided by PayU."
  },
  "cols": 2,
  "rows": 3,
  "align": [
    "left",
    "left"
  ]
}
[/block]


## Sample request

```
curl --location -g --request POST 'https://{host}/payu/accountDiscovery' \
--header 'Content-Type: application/json' \
--data-raw '{
    "phone": "12345678",//AES encrypted
    "email": "jagadesh@reddy.com", //AES encrypted
    "key": "encryption key"
}'
```

## Sample response

```
{
    "success": true|false,
    "data":{
      "customerId": "jagadesh33445"
      },
    "message": "SUCCESS"
}
```