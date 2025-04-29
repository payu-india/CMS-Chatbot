---
title: Get Invoice API
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This API is used to retrieve invoice details. You can fetch invoice details either using:

- [Invoice ID](#using-invoice-id)
- [Subscription ID](#using-subscription-id)

## Using Invoice ID

**HTTP Method**: GET

**Path**: \_{base\_url}/\_api/sub/v1/merchant/invoices/{invoiceId}

**Environment**

|            |                                           |
| :--------- | :---------------------------------------- |
| Test       | <https://subscriptiontest.citruspay.com/> |
| Production | <https://subscription.citruspay.com/>     |

### Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "merchantId  \n**mandatory**",
    "0-1": "Merchant key received during onboarding.  \n**Example**: YQeVda"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


### Sample request

```
https://subscriptiontest.citruspay.com/api/sub/v1/merchant/invoices/5c9902082fc4f831c8b4ac71
```

### Sample response body

```
{
  "invoiceId": "5c9902082fc4f831c8b4ac70",
  "subscriptionId": "5c988769652d405ed9834f67",
  "planId": "ZION155350000928619",
  "planName": "AMEXSI_155350000928610",
  "status": "Due",
  "amount": {
    "value": 1,
    "currency": "INR"
  },
  "createdOn": "2019-03-25T16:30:00.069Z",
  "modifiedOn": "2019-03-25T16:30:00.069Z",
  "retryLeft": 3,
  "authRefId": "737534002",
  "customParameter": {
    "udf1": "value"
  }
}
```

## Using Subscription ID

All the invoices for a Subscription Id can be also fetched through using Subscription ID as query string.

**Path**: \_{base\_url}/\_api/sub/v1/merchant/invoices/{invoiceId}

**Environment**

|            |                                           |
| :--------- | :---------------------------------------- |
| Test       | <https://subscriptiontest.citruspay.com/> |
| Production | <https://subscription.citruspay.com/>     |

### Request parameters

#### Header

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "merchantId  \n**mandatory**",
    "0-1": "Merchant key received during onboarding.  \n**Example**: YQeVda"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


#### Body

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "subscriptionId  \n**mandatory**",
    "0-1": "Subscription ID for which invoices needs to be fetched.",
    "1-0": "skip  \n**mandatory**",
    "1-1": "Skip is the number of subscriptions to be skip from the data-set fetched from database for given merchantId before applying the limit on it. It should be greater than or equal to zero.",
    "2-0": "limit  \n**mandatory**",
    "2-1": "Number of subscriptions to be fetch. It should be greater than zero. Max value of limit is 20"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


### Sample request

```
https://subscriptiontest.citruspay.com/api/sub/v1/merchant/invoices/?subscription Id=5c988769652d405ed9834f67&skip=0&limit=15
```

### Sample response

```
{
  "invoices": [
    {
      "invoiceId": "5c9902082fc4f831c8b4ac70",
      "subscriptionId": "5c988769652d405ed9834f67",
      "planId": "ZION155350000928619",
      "planName": "AMEXSI_155350000928610",
      "status": "Due",
      "amount": {
        "value": 1,
        "currency": "INR"
      },
      "createdOn": "2019-03-25T16:30:00.069Z",
      "modifiedOn": "2019-03-25T16:30:00.069Z",
      "retryLeft": 3,
      "authRefId": "737534002",
      "customParameter": {
        "udf1": "value"
      }
    },
    {
      "invoiceId": "5c9902082fc4f831c8b4ac6b",
      "subscriptionId": "5c988769652d405ed9834f67",
      "planId": "ZION155350000928619",
      "planName": "AMEXSI_155350000928610",
      "status": "Failed",
      "amount": {
        "value": 1,
        "currency": "INR"
      },
      "createdOn": "2019-03-25T16:30:00.034Z",
      "modifiedOn": "2019-03-25T18:00:00.531Z",
      "retryLeft": 2,
      "authRefId": "737534002",
      "customParameter": {
        "udf1": "value"
      }
    }
  ],
  "totalCount": 2,
  "page": 1
}
```