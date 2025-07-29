---
title: Delete Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
## Sample request

```
curl --location --request DELETE '<info.storecard.service.url>/storecard/card/v1?userCredential=sms%3A123&cardToken=18c7804aafdac732b5e8&networkTokenissuerToken=null&bankType=null' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data '{"userCredential":"sms:123",
"cardToken" : "1f4463abae4175a70516",
"networkToken" : "4489682380100740",
"issuerToken":"src_wqe47hxfjksor89y4",
"bankType":"SODEXO"
}'
```