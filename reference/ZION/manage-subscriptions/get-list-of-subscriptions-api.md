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

**Path**: `{base_url}/api/sub/v1/merchant/subscriptions?`

X-PayU-Subscription-Signature is SHA 512 signature used to provide security layer over existing APIs. Every API will have its own logic to generate X-PayU-Subscription- Signature logic. The following logic must be used:

```plaintext
Signature = SHA512("merchantId:" + merchantId + "|subscriptionId:" + subscriptionId + "|" + merchantSalt)
```

## Request parameters

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
        `mandatory`
      </td>

      <td>
        Merchant Key received during onboarding Sample Value - YQeVda
      </td>
    </tr>

    <tr>
      <td>
        skip`  
                mandatory`
      </td>

      <td>
        Skip is the number of subscriptions to be skip from the data-set fetched from database for given merchantId before applying the limit on it.<br /><br />  <br /> <br /><br />It should be greater than or equal to zero.
      </td>
    </tr>

    <tr>
      <td>
        limit
        `mandatory`
      </td>

      <td>
        Number of subscriptions to be fetch. It should be greater than zero. Max value of limit is 20
      </td>
    </tr>

    <tr>
      <td>
        status
        `optional`
      </td>

      <td>
        Subscription status having possible values as<br />  

        * Defined
        * Enabled
        * Completed
        * Cancelled
      </td>
    </tr>

    <tr>
      <td>
        subscriberEmail
        `optional`
      </td>

      <td>
        Email id of the customer
      </td>
    </tr>

    <tr>
      <td>
        subscriberMobile
        `optional`
      </td>

      <td>
        Mobile number of the customer
      </td>
    </tr>
  </tbody>
</Table>

## Sample request

```
curl --location 'https://subscription.payu.in/api/sub/v1/merchant/subscriptions?merchantId=0BVomn&skip=0&limit=10' \
--header 'Authorization: Bearer 810aa8723c4a626bf2c157e50204aebca72d33e9f2bf350e29eade8ae912c703' \
--header 'X-PayU-Subscription-Signature: 36c0c4b22d1c616237d518c939107e3b01ed14c32147f2c79232444392e0656b040782af69cef7e0640a3f7868145695be3903eb2692a8ef5b68e4bf0a1803ff' \
--header 'Content-Type: application/json' \
--header 'Cookie: PHPSESSID=jp38t4gvop7ami1ksncksj398v; USERTXNINFO=68ed4df291d9b7.27710642'
```

## Sample response

```
{
    "subscriptions": [
        {
            "subscriptionId": "5dc170e72fc4f8363c4fe897",
            "createdDate": "2019-11-05T07:23:59.000438Z",
            "modifiedDate": "2023-11-08T13:03:54.000901Z",
            "subscriptionPlans": [
                {
                    "planId": "ZION157295843943825",
                    "startDate": "2019-12-04T00:00:00.000Z",
                    "totalCount": 60,
                    "numberOfPaidInvoices": 0,
                    "numberOfInvoiceGenerated": 46,
                    "status": "Forced_Cancel",
                    "deleted": false,
                    "nextBillingDates": "2023-10-04T00:00:00Z",
                    "lastPaymentDates": "2020-09-04T00:00:00Z",
                    "billingInterval": 1,
                    "billingCycle": "MONTHLY",
                    "planName": "ZION157295843943825",
                    "amount": {
                        "value": 69.00,
                        "currency": "INR"
                    }
                }
            ],
            "status": "403993715520077000",
            "authRefId": "Forced_Cancel",
            "subscriberEmail": "43@g.com",
            "subscriberMobile": "5555544443",
            "customParameter": "{\"memUUID\":\"68c2b97a-ad70-4652-abc9-51f36dbba924\"}"
        },
        {
            "subscriptionId": "5ead42b72fc4f8dfa72efca5",
            "createdDate": "2020-05-02T04:21:51.000781Z",
            "modifiedDate": "2025-04-08T12:01:13.000914Z",
            "subscriptionPlans": [
                {
                    "planId": "ZION158841311178122",
                    "startDate": "2020-06-01T00:00:00.000Z",
                    "totalCount": 60,
                    "numberOfPaidInvoices": 16,
                    "numberOfInvoiceGenerated": 60,
                    "status": "Active",
                    "deleted": false,
                    "nextBillingDates": "",
                    "lastPaymentDates": "2021-09-24T18:12:08.747Z",
                    "billingInterval": 30,
                    "billingCycle": "DAILY",
                    "planName": "ZION158841311178122",
                    "amount": {
                        "value": 99.00,
                        "currency": "INR"
                    }
                }
            ],
            "status": "10456115667",
            "authRefId": "Enabled",
            "subscriberEmail": "srikanth.nalla@gmail.com",
            "subscriberMobile": "9948598864",
            "customParameter": "{\"memUUID\":\"16b090d2-10a5-463e-ba1e-615feaf5ca98\"}"
        }
    ],
    "totalCount": 2,
    "page": 1
}
```
