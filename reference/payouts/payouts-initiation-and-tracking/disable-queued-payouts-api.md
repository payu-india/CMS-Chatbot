---
title: Disable Queued Payouts API
excerpt: ''
api:
  file: payouts-api-7.json
  operationId: DisableQueuedPayoutsAPI
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
Transactions go into the queue if the merchant is not having enough balance in his account process. You can mark the transaction as failed using the **setQueueTxnFlag** API command if enough balance is not available.

**Environment**

|                            |                                                     |
| -------------------------- | --------------------------------------------------- |
| **Test Environment**       | <https://uatoneapi.payu.in/payout/setQueueTxnFlag>  |
| **Production Environment** | <https://www.payumoney.com//payout/setQueueTxnFlag> |

## Header and request parameters

> 📘 Note:
> 
> The payoutMerchantId is different from PayU Merchant Id. Check the Payouts Dashboard or call the PayU Customer Support if you don’t know your payoutMerchantId.

<details>
  <summary>Sample request</summary>

```curl
curl --location 'https://uatoneapi.payu.in/payout/setQueueTxnFlag' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'authorization: Bearer 6e47dc301158318020af04917b256422cf7f8e11147807102abe5b984c7a03e7' \
--header 'payoutmerchantid: 2225335' \
--data-urlencode 'queueTxn=true' \
--data-urlencode 'configMerchantId=2225335'
```

</details>

<details>
  <summary>Sample response</summary>

### Success scenario

```
{
    "status": 0,
    "msg": "success",
    "code": null,
    "data": {
        "id": 22578,
        "merchantId": null,
        "entityId": 1116090,
        "entityType": "merchant_id",
        "configKey": "queue_transaction_insufficient_balance",
        "configValue": "0",
        "groupName": null,
        "isActive": true,
        "addedOn": "2023-04-17T18:22:54.470+0000",
        "updatedOn": "2023-04-17T18:22:54.470+0000",
        "isDeleted": false,
        "updatedBy": 4538
    }
}
```

### Failure scenario

```
{
 "status": 1,
 "msg": "Invalid value",
 "code": null,
 "data": null
 }
```

</details>