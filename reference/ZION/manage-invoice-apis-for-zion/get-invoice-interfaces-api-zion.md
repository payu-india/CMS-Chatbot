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

**Path**: _\{base\_url}/_api/sub/v1/merchant/invoices/`{invoiceId}`

**Environment**

|            |                                           |
| :--------- | :---------------------------------------- |
| Test       | \<https://subscriptiontest.citruspay.com/> |
| Production | \<https://subscription.citruspay.com/>     |

### Request parameters

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant key received during onboarding.<br><strong>Example</strong>: YQeVda</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

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

**Path**: _\{base\_url}/_api/sub/v1/merchant/invoices/`{invoiceId}`

**Environment**

|            |                                           |
| :--------- | :---------------------------------------- |
| Test       | \<https://subscriptiontest.citruspay.com/> |
| Production | \<https://subscription.citruspay.com/>     |

### Request parameters

#### Header

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Merchant key received during onboarding.<br><strong>Example</strong>: YQeVda</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

#### Body

<HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
<thead>
<tr>
  <th style="border: 1px solid #ddd; padding: 8px;">Parameter</th>
  <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
</tr>
</thead>
<tbody>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>subscriptionId<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Subscription ID for which invoices needs to be fetched.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>skip<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Skip is the number of subscriptions to be skip from the data-set fetched from database for given merchantId before applying the limit on it. It should be greater than or equal to zero.</p>
</td>
</tr>
<tr>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>limit<br><strong>mandatory</strong></p>
</td>
  <td style="border: 1px solid #ddd; padding: 8px;"><p>Number of subscriptions to be fetch. It should be greater than zero. Max value of limit is 20</p>
</td>
</tr>
</tbody>
</table>
`}</HTMLBlock>

### Sample request

```
https://subscriptiontest.citruspay.com/api/sub/v1/merchant/invoices/?subscriptionId=5c988769652d405ed9834f67&skip=0&limit=15
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