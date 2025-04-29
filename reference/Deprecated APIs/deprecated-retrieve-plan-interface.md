---
title: '[DEPRECATED] Retrieve Plan Interface'
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
Retrieve plan interface returns details about created plan by HTTP Get method. The response body is same as that of create plan.

## Retrieve a plan

HTTP Method: **GET**

Path: {base_url}/api/sub/v1/merchant/plans/{planId}

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "merchantId  \n**mandatory**",
    "0-1": "Merchant Key received during onboarding.  \n**Example**: Ysr1r"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


## Retrieve all plans

Retrieve plan interface returns details about created plan by HTTP Get method. The response body is same as that of create plan.

HTTP Method: **GET**

Path: {base_url}/api/sub/v1/merchant/plans?

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "merchantId  \n**mandatory**",
    "0-1": "Merchant Key received during onboarding.  \n**Example**: Ysr1r",
    "1-0": "skip  \n**mandatory**",
    "1-1": "Skip is the number of plans to be skip from the data set fetched from database for given merchantId before applying the limit on it. It should be greater than or equal to zero.  \n**Example**: 5",
    "2-0": "limit  \n**mandatory**",
    "2-1": "_Number of plans to be fetch. It should be greater than zero.  \nMax value of limit is 50_  \n**Example**: 20"
  },
  "cols": 2,
  "rows": 3,
  "align": [
    null,
    null
  ]
}
[/block]


Example URL:

_{base\_url}/api/sub_[_/v1/merchant/plans_](https://subscriptiontest.citruspay.com/api-docs/mercury.html)_?merchantId=Ysr1r&skip=10&limit=50_

In given URL format, for merchant having key as “Ysr1r” all the plans will be returned from 11 till 60 sorted by latest date, total 50 plans

_{base\_url}/api/sub_[_/v1/merchant/plans_](https://subscriptiontest.citruspay.com/api-docs/mercury.html)_?merchantId=Ysr1r&skip=0&limit=10_

In given URL format, latest 10 plans will be returned.