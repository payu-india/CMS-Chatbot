---
title: '[DEFFERED]Associate Plan in Defined Subscription Interface'
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
While associating plan with subscription, the API PATH, HTTP method and Response Body remains same as that of Defined Subscription interface. So, let’s look an example where Plan created by calling Create Plan interface, with id ***5aa26aa1fbea353c71802577*** is getting associated while calling Defined Subscription interface as below -

**POST** \- [*https://subscription.citruspay.com/api/sub/v1/merchant/subscriptions*](https://subscription.citruspay.com/api/sub/v1/merchant/subscriptions)

**Content-Type** \- *application/json*

**X-PayU-Subscription-Signature -** *SHA512(“merchantId:Ysr1r| x83y3au1”)*

## Sample request

```
{
  "merchantId": "Ysr1r",
  "subscriptionPlans": [
    {
      "planId": "5aa26aa1fbea353c71802577",
      "startDate": "2019-04-05T00:00:00.000Z",
      "totalCount": 3
    }
  ],
  "authRefId": "1234321",
  "subscriberEmail": "chotabheem@gmail.com",
  "subscriberMobile": "911234567890",
  "customParameter": {
    "Policy": "41231312323"
  }
}
```

 

## Sample response

From the following sample response body, it is evident that Plan id ***5aa26aa1fbea353c71802577*** generated during Create Plan interface is getting associated with Subscription which results into creation of Subscription Id ***5c9bbe9a2fc4f831c8b4aceb*** and billing amount, cycle and interval is inherited from that plan.

```
{
  "subscriptionId": "5c9bbe9a2fc4f831c8b4aceb",
  "merchantId": "Ysr1r",
  "subscriberEmail": "chotabheem@gmail.com",
  "subscriberMobile": "911234567890",
  "authRefId": "1234321",
  "subscriptionPlans": [
    {
      "planId": "5aa26aa1fbea353c71802577",
      "startDate": "2019-04-05T00:00:00.000Z",
      "totalCount": 3,
      "numberOfPaidInvoices": 0,
      "numberOfInvoiceGenerated": 0,
      "status": "Active",
      "deleted": false,
      "nextBillingDates": "2019-04-05T00:00:00Z",
      "lastPaymentDates": null,
      "billingInterval": 2,
      "billingCycle": "WEEKLY",
      "planName": " Premium",
      "amount": {
        "value": 200,
        "currency": "INR"
      }
    }
  ],
  "createdDate": "2019-03-27T18:19:06.629Z",
  "modifiedDate": "2019-03-27T18:19:06.629Z",
  "status": "Enabled",
  "customParameter": {
    "language": "English",
    "region": "Goa"
  },
  "possibleActions": [
    {
      "action": "Update Subscription",
      "href": "{{base-url}}/api/sub/v1/subscription/5c9bbe9a2fc4f831c8b4aceb",
      "httpMethod": "PATCH"
    },
    {
      "action": "Fetch Subscription",
      "href": "{{base-url}}/api/sub/v1/subscription/5c9bbe9a2fc4f831c8b4aceb",
      "httpMethod": "GET"
    },
    {
      "action": "Delete Subscription",
      "href": "{{base-url}}/api/sub/v1/subscription/5c9bbe9a2fc4f831c8b4aceb",
      "httpMethod": "DELETE"
    }
  ]
}
```
