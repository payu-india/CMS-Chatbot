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

Path: \{base\_url}/api/sub/v1/merchant/plans/\{planId}

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        merchantId
        **mandatory**
      </td>

      <td>
        Merchant Key received during onboarding.  

        * \*Example\*\*: Ysr1r
      </td>
    </tr>
  </tbody>
</Table>

## Retrieve all plans

Retrieve plan interface returns details about created plan by HTTP Get method. The response body is same as that of create plan.

HTTP Method: **GET**

Path: \{base\_url}/api/sub/v1/merchant/plans?

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        merchantId
        **mandatory**
      </td>

      <td>
        Merchant Key received during onboarding.  

        * \*Example\*\*: Ysr1r
      </td>
    </tr>

    <tr>
      <td>
        skip\
        **mandatory**
      </td>

      <td>
        Skip is the number of plans to be skip from the data set fetched from database for given merchantId before applying the limit on it. It should be greater than or equal to zero.  

        * \*Example\*\*: 5
      </td>
    </tr>

    <tr>
      <td>
        limit\
        **mandatory**
      </td>

      <td>
        * Number of plans to be fetch. It should be greater than zero.\
          Max value of limit is 50\_  
        * \*Example\*\*: 20
      </td>
    </tr>
  </tbody>
</Table>

Example URL:

*\{base\_url}/api/sub*[*/v1/merchant/plans*](https://subscriptiontest.citruspay.com/api-docs/mercury.html)*?merchantId=Ysr1r\&skip=10\&limit=50*

In given URL format, for merchant having key as “Ysr1r” all the plans will be returned from 11 till 60 sorted by latest date, total 50 plans

*\{base\_url}/api/sub*[*/v1/merchant/plans*](https://subscriptiontest.citruspay.com/api-docs/mercury.html)*?merchantId=Ysr1r\&skip=0\&limit=10*

In given URL format, latest 10 plans will be returned.
