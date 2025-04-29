---
title: Cancel Smart Send API
excerpt: ''
api:
  file: new-payouts-api-collection-1.json
  operationId: CancelSmartSendAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to cancel a particular smart send payment link.

**Environment**

|                            |                                                                         |
| -------------------------- | ----------------------------------------------------------------------- |
| **Test Environment**       | &lt;https://uatoneapi.payu.in/payout/v2/smartSend/expiry/`{smartSendId}`&gt;    |
| **Production Environment** | &lt;https://payout.payumoney.com/payout/v2/smartSend/expiry/`{smartSendId}`&gt; |

<details>
  <summary>Sample request</summary>

```curl
curl --location --request POST 'https://test.payumoney.com/payout/smartPay/cancel?merchantRefId=Test6Sep3' \--header 'Authorization: Bearer 0eabb5d79b6324ceae72c96c6099932b219d58d293642d6b9503f5ace7e416ed' \--header 'payoutMerchantId: 1111766' \--header 'Content-Type: application/json'
```

</details>

<details>
  <summary>Sample response</summary>

**Failure scenario**

```
{
	"status": 0,
	"msg": "Smart send link cancelled",
	"code": null,
	"data": null
}
```

</details>

## Request header and parameters

> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.