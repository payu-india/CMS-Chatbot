---
title: Get User Cards API
deprecated: false
hidden: false
metadata:
  robots: index
---
Use the v2 **Get User Cards** API to get the card details of a customer.

> 📘 Note
>
> While PayU token is sent in payment response, the network/issuer token creation may fail. In this case, the subsequent transaction with the said PayU token may fail. Merchant can do a **get\_user\_cards API** to fetch only active/tokenized cards or listen to notification API (to be published) to maintain state at your end.

The **Get User Cards** API is used to fetch all the cards for a customer which were saved earlier. In this API, the card number and other sensitive information are not returned.

HTTP Method: **POST**

## Request header

<br />

## Sample request

```
curl --location '<info.storecard.service.url>/storecard/instrument/v1?testuser%3Atestuser123&getSoftDeleted=1' \
--header 'mid: 2'
```

<br />

## Request parameters