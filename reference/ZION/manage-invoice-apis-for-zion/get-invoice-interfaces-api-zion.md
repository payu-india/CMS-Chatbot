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

* [Invoice ID](#using-invoice-id)
* [Subscription ID](#using-subscription-id)

## Using Invoice ID

**HTTP Method**: GET

**Path**: _\{base_url}/_api/sub/v1/merchant/invoices/`{invoiceId}`

**Environment**

|            |                                                                                        |
| :--------- | :------------------------------------------------------------------------------------- |
| Test       | \<[https://subscriptiontest.citruspay.com/>](https://subscriptiontest.citruspay.com/>) |
| Production | \<[https://subscription.citruspay.com/>](https://subscription.citruspay.com/>)         |

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

**Path**: _\{base_url}/_api/sub/v1/merchant/invoices/`{invoiceId}`

**Environment**

|            |                                                                                        |
| :--------- | :------------------------------------------------------------------------------------- |
| Test       | \<[https://subscriptiontest.citruspay.com/>](https://subscriptiontest.citruspay.com/>) |
| Production | \<[https://subscription.citruspay.com/>](https://subscription.citruspay.com/>)         |

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
curl --location 'https://subscription.payu.in/api/sub/v1/merchant/invoices/6522d9af2fc4f8dee476695c' \
--header 'Authorization: Bearer 810aa8723c4a626bf2c157e50204aebca72d33e9f2bf350e29eade8ae912c703' \
--header 'merchantId: aTh61r' \
--header 'X-PayU-Subscription-Signature: 36c0c4b22d1c616237d518c939107e3b01ed14c32147f2c79232444392e0656b040782af69cef7e0640a3f7868145695be3903eb2692a8ef5b68e4bf0a1803ff' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642'
```

### Sample response

```
{
    "invoiceId": "6522d9af2fc4f8dee476695c",
    "subscriptionId": "5cbe8d982fc4f8bf774d43af",
    "planId": "ZION155599196011028",
    "status": "Failed",
    "amount": {
        "value": 99.00,
        "currency": "INR"
    },
    "createdOn": "2023-10-08 16:32:47.375",
    "modifiedOn": "2023-10-11 18:25:58.894",
    "retryLeft": 0,
    "authRefId": "8347443919",
    "subscriberEmail": "amolr9999@gmail.com",
    "subscriberMobile": "91-8879211929",
    "customParameter": {},
    "refId": ""
}
```
