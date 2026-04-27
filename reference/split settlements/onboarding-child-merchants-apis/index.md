---
title: Onboarding Child Merchants APIs
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
## Onboarding Child Merchants

The steps involved in creating a child merchant are:

1. [Get Client Token API](ref:get-client-token-api)
2. [Create Child Merchant API](ref:create-child-merchant-api)

<Callout icon="📘" theme="info">
  **Note**: Before you onboard child merchants, ensure you have followed the [Prerequisites](#prerequisites) (one-time).
</Callout>

<Callout icon="📮" theme="default">
  **Postman Collection**: Download the **Split Settlements > Onboarding Child Merchants Postman Collection** from the following location:

  [https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/ghidoum/onboarding-child-merchants-api-s](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/ghidoum/onboarding-child-merchants-api-s)
</Callout>

## Domains

### Common Onboarding

|                        |                                                                                   |
| ---------------------- | --------------------------------------------------------------------------------- |
| UAT Environment        | \<[https://uat-onepayuonboarding.payu.in](https://uat-onepayuonboarding.payu.in)> |
| Production Environment | \<[https://onboarding.payu.in](https://onboarding.payu.in)>                       |

### Hub Service Domains

|                        |                                                                 |
| ---------------------- | --------------------------------------------------------------- |
| UAT Environment        | \<[https://uat-accounts.payu.in](https://uat-accounts.payu.in)> |
| Production Environment | \<[https://accounts.payu.in](https://accounts.payu.in)>         |

## Prerequisites

Before you onboard child merchants, you need to ensure the following (one-time process):

* Caller client service should be registered on Hub (PayU’s oAuth2 Service ) with the details as described in the following table:

| Field                       | Description                                                                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Customer Name               | The legal name of the customer.                                                                                                               |
| Customer Service Name       | The service name of the customer.                                                                                                             |
| Customer Owner phone number | The phone number of the owner who is assigned for the customer.                                                                               |
| Customer Owner Email        | The customer owner’s email ID.                                                                                                                |
| Scopes                      | The scope to be whitelisted on the client must be **refer_child_merchant**                                                                    |
| Grant type                  | The grant type must be specified as **client_credentials** in this field.                                                                     |
| Client type                 | Post **External** as input since you are outside the PayU ecosystem.                                                                          |
| Access Token Expiry Time    | The access token expiry time from the times of creation (in seconds). There is no defined limit for configuring the access token expiry time. |

* **refer_child_merchant** scope should be whitelisted on caller client on Hub
* **Get Aggregator** flag enabled on the parent merchant

## Step 1: Get client token

Use the **Get Client Token** API with the scope as **refer_child_merchant** to create a client token from Hub. For more information, refer to [Get Client Token API](ref:get-client-token-api)

## **Step 2: Create a child merchant**

You can create child merchants using the **Create Child Merchant** API. For more information, refer to [Create Child Merchant API](ref:create-child-merchant-api)

After you onboard your child merchants, you can fetch the child merchant details as described in the following API reference:

* [Sub Account Listing API](ref:sub-account-listing-api)
