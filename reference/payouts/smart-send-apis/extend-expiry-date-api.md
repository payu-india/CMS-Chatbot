---
title: Extend Expiry Date API
excerpt: ''
api:
  file: extend-expiry-date-api-2.json
  operationId: ExtendexpirydateApi
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to extend the expiry date of a valid link. A valid link is one that isn't expired or a link for which the transaction is in a pending state.

**Environment**

|                            |                                                                 |
| -------------------------- | --------------------------------------------------------------- |
| **Test Environment**       | \<https://uatoneapi.payu.in/payout/v2/smartSend/extendExpiry>    |
| **Production Environment** | \<https://payout.payumoney.com/payout/v2/smartSend/extendExpiry> |

<details>
  <summary>Sample request</summary>

```
curl --location --request PUT 'https://oneapi.payu.in/payout/v2/smartSend/expiry/123' \
--header 'mid: 8000051' \
--header 'authorization: Bearer b6c0782b9eb08b43681776bad60ca1894a8421539e7c96c9aa32c0805994046d' \
--header 'pid: 1111312' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'expiryDate=2021-07-24T18:18:10.000Z'
```

</details>

<details>
  <summary>Sample response</summary>

**Failure scenario**

```
{
  "timestamp": "2024-01-30T09:07:37.189+0000",
  "status": 401,
  "error": "Unauthorized",
  "message": "Access is denied",
  "path": "/payout/v2/smartSend/expiry/123"
}
```

</details>

## Request header and parameters

For the list of error messages and their description that you may encounter when Smart Send APIs integration, refer to [Smart Send Error Codes](ref:smart-send-error-codes).

> 📘 Note:
> 
> The **pid** is **payoutMerchantId**, however it is different from the PayU merchant id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your **payoutsMerchantID**.