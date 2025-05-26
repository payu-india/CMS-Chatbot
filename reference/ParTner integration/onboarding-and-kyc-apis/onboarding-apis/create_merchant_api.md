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

\<Accordion title="My Accordion Title" icon="fa-info-circle">

```Text JSON
{
   "merchant":{
      "name":"test",
      "email":"test@payu.in",
      "registered_mobile":"9999910014",
      "mid":129463,
      "product":"PayUbiz",
      "business_type":"LongTail",
      "business_name":"Test",
      "pancard_name":"Test",
      "pancard_number":"ABCPG1234J",
      "cin_number":"U72400MH2006PTC293037",
      "website_url":null,
      "android_url":null,
      "ios_url":null,
      "gst_number":null,
      "created_at":"2020-12-08T11:03:56.000Z",
      "mobile":"9999910014",
      "blocked":false,
      "first_name":"",
      "last_name":"test",
      "bank_detail":{
         "bank_account_number":"234567891",
         "ifsc_code":"ICIC0000734",
         "holder_name":"Test"
      },
      "operating_address":{
         "address_line":"operational addr",
         "city":"Sant Ravidas Nagar",
         "state":"UTTAR PRADESH",
         "pincode":221304
      },
      "registration_address":{
         "address_line":"busenaddres line",
         "city":"Sant Ravidas Nagar",
         "state":"UTTAR PRADESH",
         "pincode":221303
      },
      "business_entity":"LLP",
      "status":"account_created",
      "partner_source":"Create Merchant API",
      "pan_verification_status":"Pending",
      "website_approval_status":"Pending",
      "notification_email":"test@payu.in",
      "settlement_status":null,
      "is_service_agreement_accepted":false,
      "is_authorisation_letter_required":false,
      "monthly_expected_volume":120000,
      "business_category":"Ecommerce",
      "business_sub_category":"Flowers and Gifts",
      "bank_verification_status":"Pending",
      "uuid":"11eb-3945-0fcf623a-86d9-026e3e71538e",
      "penny_deposit_status":"Not Initiated",
      "signing_authority":{
         "name":"test_auth",
         "email":"test_auth@payu.in"
      },
      "director1_details":{
         "name":"test1_dir",
         "email":"test1_dir@payu.in"
      },
      "director2_details":{
         "name":"test2_dir",
         "email":"test2_dir@payu.in"
      }
   }
}
```


\</Accordion>

<br />

<br />

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

```
```

## Request Parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>