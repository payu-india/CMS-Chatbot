---
title: Create Merchant API
excerpt: ''
api:
  file: partner-apis-26.json
  operationId: create_merchantv3
deprecated: false
hidden: false
metadata:
  title: Create Merchant API
  description: >-
    Learn how to use the PayU Create Merchant API to create new merchant
    accounts. This API reference page provides detailed instructions, request
    parameters, and sample responses for efficient merchant onboarding
  keywords:
    - Create Merchant API
    - ' merchant onboarding'
    - ' KYC details'
    - ' secure merchant creation'
    - ' tokenization'
    - ' manage merchants'
    - ' create merchant accounts'
  robots: index
next:
  description: ''
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

## Authentication

This API is authorised through a client token generated using the client ID and secret. To create a token, call the get token API with `refer merchant` as a scope.  Refer to the  [Get Token API](ref:get_token_api) doc for more information.

> ❗️ Important considerations for using this API
>
> 1. The mobile, Pan number, GSTIN passed in the request has to be valid as checks are performed in real time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belong to the same entity.

<br />

\<Tabs>
&#x20; \<Tab title="Sample Request">
&#x20; &#x20;
&#x20; \</Tab>

&#x20; \<Tab title="Sample Response">
&#x20;  \{
&#x20;  "merchant":\{
&#x20;     "name":"test",
&#x20;     "email":"test\@payu.in",
&#x20;     "registered\_mobile":"9999910014",
&#x20;     "mid":129463,
&#x20;     "product":"PayUbiz",
&#x20;     "business\_type":"LongTail",
&#x20;     "business\_name":"Test",
&#x20;     "pancard\_name":"Test",
&#x20;     "pancard\_number":"ABCPG1234J",
&#x20;     "cin\_number":"U72400MH2006PTC293037",
&#x20;     "website\_url":null,
&#x20;     "android\_url":null,
&#x20;     "ios\_url":null,
&#x20;     "gst\_number":null,
&#x20;     "created\_at":"2020-12-08T11:03:56.000Z",
&#x20;     "mobile":"9999910014",
&#x20;     "blocked":false,
&#x20;     "first\_name":"",
&#x20;     "last\_name":"test",
&#x20;     "bank\_detail":\{
&#x20;        "bank\_account\_number":"234567891",
&#x20;        "ifsc\_code":"ICIC0000734",
&#x20;        "holder\_name":"Test"
&#x20;     },
&#x20;     "operating\_address":\{
&#x20;        "address\_line":"operational addr",
&#x20;        "city":"Sant Ravidas Nagar",
&#x20;        "state":"UTTAR PRADESH",
&#x20;        "pincode":221304
&#x20;     },
&#x20;     "registration\_address":\{
&#x20;        "address\_line":"busenaddres line",
&#x20;        "city":"Sant Ravidas Nagar",
&#x20;        "state":"UTTAR PRADESH",
&#x20;        "pincode":221303
&#x20;     },
&#x20;     "business\_entity":"LLP",
&#x20;     "status":"account\_created",
&#x20;     "partner\_source":"Create Merchant API",
&#x20;     "pan\_verification\_status":"Pending",
&#x20;     "website\_approval\_status":"Pending",
&#x20;     "notification\_email":"test\@payu.in",
&#x20;     "settlement\_status":null,
&#x20;     "is\_service\_agreement\_accepted":false,
&#x20;     "is\_authorisation\_letter\_required":false,
&#x20;     "monthly\_expected\_volume":120000,
&#x20;     "business\_category":"Ecommerce",
&#x20;     "business\_sub\_category":"Flowers and Gifts",
&#x20;     "bank\_verification\_status":"Pending",
&#x20;     "uuid":"11eb-3945-0fcf623a-86d9-026e3e71538e",
&#x20;     "penny\_deposit\_status":"Not Initiated",
&#x20;     "signing\_authority":\{
&#x20;        "name":"test\_auth",
&#x20;        "email":"test\_auth\@payu.in"
&#x20;     },
&#x20;     "director1\_details":\{
&#x20;        "name":"test1\_dir",
&#x20;        "email":"test1\_dir\@payu.in"
&#x20;     },
&#x20;     "director2\_details":\{
&#x20;        "name":"test2\_dir",
&#x20;        "email":"test2\_dir\@payu.in"
&#x20;     }
&#x20;  }
}
&#x20; \</Tab>
\</Tabs>

<br />

## Request Parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>