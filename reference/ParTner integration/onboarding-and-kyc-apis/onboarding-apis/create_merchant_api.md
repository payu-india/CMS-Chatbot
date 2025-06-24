---
title: Create Merchant API
api:
  file: create_merchant.json
  operationId: CreateMerchant
hidden: false
metadata:
  title: Create Merchant API
  description: >-
    Learn how to use the PayU Create Merchant API to create new merchant
    accounts. This API reference page provides detailed instructions, request
    parameters, and sample responses for efficient merchant onboarding
  keywords:
    - Create Merchant API
    - merchant onboarding
    - KYC details
    - secure merchant creation
    - tokenization
    - manage merchants
    - create merchant accounts
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

## Authentication

This API is authorised through a client token generated using the client ID and secret. To create a token, call the get token API with `refer merchant` as a scope.  Refer to the  [Get Token API](ref:get_token_api) doc for more information.

> ❗️ Important considerations for using this API
>
> 1. The mobile, Pan number, GSTIN passed in the request has to be valid as checks are performed in real time.
> 2. If Business Entity type is passed in the create merchant API, ensure that the PAN also belong to the same entity.

<PARTNEROnboardingEnvironment />

## Sample Request

```curl
curl --location 'https://uat-partner.payu.in/api/v3/merchants' \
--header 'accept: application/json' \
--header 'authorization: Bearer 74ff89df8ff4aeb3d7cb2c0297cfcb358a8c4c1d69b3980d509bf300c5e82e5f' \
--header 'content-type: application/x-www-form-urlencoded' \
--data-urlencode 'merchant%5Bdisplay_name%5D=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant%5Bemail%5D=borosil96@yomail.com' \
--data-urlencode 'merchant%5Bmobile%5D=9911100364' \
--data-urlencode 'merchant%5Bbusiness_details%5D%5Bpan%5D=FANPS6362D' \
--data-urlencode 'merchant%5Bbusiness_details%5D%5Bbusiness_entity_type%5D=Sole Proprietorship' \
--data-urlencode 'merchant%5Bbank_details%5D%5Baccount_no%5D=919010067278549' \
--data-urlencode 'merchant%5Bbank_details%5D%5Baccount_holder_name%5D=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant%5Bbank_details%5D%5Bifsc_code%5D=UTIB0003557' \
--data-urlencode 'merchant%5Bbusiness_details%5D%5Bregistered_name%5D=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant%5Bbusiness_details%5D%5Bbusiness_category%5D=Arts, Gifts & Stationery' \
--data-urlencode 'merchant%5Bbusiness_details%5D%5Bbusiness_sub_category%5D=Art Dealers and Galleries' \
--data-urlencode 'merchant%5Bwebsite_details%5D%5Bwebsite_url%5D=https://www.google.com' \
--data-urlencode 'merchant%5Bmonthly_expected_volume%5D=12000' \
--data-urlencode 'merchant%5Bsigning_authority_details%5D%5Bname%5D=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant%5Bbusiness_details%5D%5Bpancard_name%5D=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant%5Bsigning_authority_details%5D%5Bemail%5D=email_test1213@yopmail.com' \
--data-urlencode 'merchant%5Bsigning_authority_details%5D%5Bpancard_number%5D=FANPS6362D'
```

<br />

## Sample response

### Success scenario

```
{
  "merchant": {
    "mid": "8390925",
    "kyc_document_name": "PAN Card of Signing Authority",
    "kyc_document_uuid": "11ef-587e-43837330-95b0-021ec077a271",
    "kyc_document_status": "DOCUMENT_SUBMITTED",
    "error_message": null,
    "created_at": "2024-08-12T07:41:19.000Z"
  }
}
```

### Failure scenario

* Duplicate merchant or merchant already exists

```
{
  "errors": {
    "error": [
      "Account already exists for given user"
    ]
  },
  "product_account": {
    "identifier": 8245177,
    "product": "PayUbiz"
  }
}
```

<br />

## Response parameters

### Fields in the merchant object

| Parameter             | Description                                                                        | Example                              |
| :-------------------- | :--------------------------------------------------------------------------------- | :----------------------------------- |
| mid                   | Unique merchant identifier                                                         | 8390925                              |
| kyc\_document\_name   | Name of the KYC document category                                                  | PAN Card of Signing Authority        |
| kyc\_document\_uuid   | Unique identifier for the KYC document submission                                  | 11ef-587e-43837330-95b0-021ec077a271 |
| kyc\_document\_status | Current status of the KYC document (e.g., DOCUMENT\_SUBMITTED, VERIFIED, REJECTED) | DOCUMENT\_SUBMITTED                  |
| error\_message        | Error message if document verification failed, null otherwise                      | null                                 |
| created\_at           | Timestamp when the KYC document was created/submitted.                             | 2024-08-12T07:41:19.000Z             |

> 📘 Notes:
>
> * The `kyc_document_status` field can have the following values:
>   * `DOCUMENT_SUBMITTED`: Document has been submitted but not yet verified
>   * `VERIFIED`: Document has been verified and approved
>   * `REJECTED`: Document was rejected during verification
>   * `PENDING`: Document is pending verification
> * The `error_message` field will only contain a value if the document was rejected or there was an issue with the submission.
> * All timestamps are in ISO 8601 format with UTC timezone.

## Request parameters

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>