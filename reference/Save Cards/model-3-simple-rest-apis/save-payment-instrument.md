---
title: Save Payment Instrument
deprecated: false
hidden: false
metadata:
  robots: index
---
## Sample request

```
curl --location '<info.storecard.service.url>/storecard/card/v1' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data '{"userCredential":"sms:123",
"cardName":"testAll",
"cardMode":"CC",
"cardType":"CC",
"nameOnCard":"test",
"cardNo":"4761360079851258",
"cardExpiryMonth":12,
"cardExpiryYear":2025,
"authRefNumber":"asd"}'
```

## Sample response

```
{
    "message": "Card Stored Successfully.",
    "status": 1,
    "result": {
        "cardToken": "18cc810671348c3d3241",
        "cardNo": "XXXXXXXXXXXX1258",
        "cardName": "testAll",
        "networkToken": "4761360000000009"
    }
}
```

## Response parameters