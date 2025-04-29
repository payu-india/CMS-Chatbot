---
title: Get List of Subscriptions API
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
Sometimes it is required to get list of subscriptions with certain criteria. Zion today supports getting list through four parameters individually or together through simple HTTP GET method and query string. Merchant Id mandatory to fetch the list but other three can be used together as well to form desired query.

**Post Method**: GET

**Path**:{base_url}/api/sub/v1/merchant/subscriptions?

X-PayU-Subscription-Signature is SHA 512 signature used to provide security layer over existing APIs. Every API will have its own logic to generate X-PayU-Subscription- Signature logic. The following logic must be used:

```plaintext
Signature = SHA512("merchantId:" + merchantId + "|subscriptionId:" + subscriptionId + "|" + merchantSalt)
```

## Request parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "merchantId  \n**mandatory**",
    "0-1": "Merchant Key received during onboarding Sample Value - YQeVda",
    "1-0": "skip  \n**mandatory**",
    "1-1": "Skip is the number of subscriptions to be skip from the data-set fetched from database for given merchantId before applying the limit on it.<br><br>  <br> <br><br>It should be greater than or equal to zero.",
    "2-0": "limit  \n**mandatory**",
    "2-1": "Number of subscriptions to be fetch. It should be greater than zero. Max value of limit is 20",
    "3-0": "status  \n**optional**",
    "3-1": "Subscription status having possible values as<br><br>_ Defined<br>_ Enabled<br>_ Completed<br>_ Cancelled",
    "4-0": "subscriberEmail  \n**optional**",
    "4-1": "Email id of the customer",
    "5-0": "subscriberMobile  \n**optional**",
    "5-1": "Mobile number of the customer"
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample request

```
https://subscription.citruspay.com/api/sub/v1/merchant/subscriptions?merchantId=YQeV da&status=Enabled&skip=0&limit=15
```

## Sample response

```
{
  "subscriptions": [
    {
      "subscriptionId": "5c97c51a652d405ed9834f58",
      "createdDate": "2019-03-24T17:57:46.875Z",
      "modifiedDate": "2019-03-24T18:33:46.406Z",
      "subscriptionPlans": [
        {
          "planId": "ZION155345026687548",
          "startDate": null,
          "totalCount": 0,
          "numberOfPaidInvoices": 0,
          "numberOfInvoiceGenerated": 0,
          "status": "Inactive",
          "deleted": false,
          "nextBillingDates": null,
          "lastPaymentDates": null,
          "billingInterval": 0,
          "billingCycle": "ADHOC",
          "planName": "Premium",
          "amount": {
            "value": 2,
            "currency": "INR"
          }
        }
      ],
      "authRefId": "7375340021",
      "status": "Defined",
      "subscriberEmail": "chota.bheem@pogo.com",
      "subscriberMobile": "9999999999",
      "customParameter": {
        "Policynumber": "12743123111",
        "Policytype": "Life Insurance"
      }
    },
    {
      "subscriptionId": "5c95d46a2fc4f831c8b4ac1c",
      "createdDate": "2019-03-23T06:38:34.828Z",
      "modifiedDate": "2019-03-23T06:38:34.828Z",
      "subscriptionPlans": [
        {
          "planId": "ZION155332311482827",
          "startDate": "2019-03-26T11:00:00.000Z",
          "totalCount": 5,
          "numberOfPaidInvoices": 0,
          "numberOfInvoiceGenerated": 0,
          "status": "Inactive",
          "deleted": false,
          "nextBillingDates": null,
          "lastPaymentDates": null,
          "billingInterval": 1,
          "billingCycle": "DAILY",
          "planName": "Premium",
          "amount": {
            "value": 2,
            "currency": "INR"
          }
        }
      ],
      "authRefId": null,
      "status": "Defined",
      "subscriberEmail": "chota.bheem@pogo.com",
      "subscriberMobile": "9999999999",
      "customParameter": {
        "Policynumber": "12743123133",
        "Policytype": "Terms Insurance"
      }
    },
    {
      "subscriptionId": "5c9517f2652d405ed9834f3f",
      "createdDate": "2019-03-22T17:14:26.428Z",
      "modifiedDate": "2019-03-22T17:14:26.428Z",
      "subscriptionPlans": [
        {
          "planId": "ZION15532748664281",
          "startDate": null,
          "totalCount": null,
          "numberOfPaidInvoices": 0,
          "numberOfInvoiceGenerated": 0,
          "status": "Inactive",
          "deleted": false,
          "nextBillingDates": null,
          "lastPaymentDates": null,
          "billingInterval": 1,
          "billingCycle": "MONTHLY",
          "planName": "Premium",
          "amount": {
            "value": 200,
            "currency": "INR"
          }
        }
      ],
      "authRefId": null,
      "status": "Defined",
      "subscriberEmail": "chota.bheem@pogo.com",
      "subscriberMobile": "9999999999",
      "customParameter": {
        "Policynumber": "12743123133",
        "Policytype": "Terms Insurance"
      }
    }
  ],
  "totalCount": 3,
  "page": 1
}
```