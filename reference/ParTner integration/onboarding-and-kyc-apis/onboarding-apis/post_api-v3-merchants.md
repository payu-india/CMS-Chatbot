---
title: Create Merchant API
excerpt: Creates a new merchant in the PayU system
api:
  file: create_merchant_api_oas_final.json
  operationId: post_api-v3-merchants
hidden: true
---
The **Create Merchant** API creates a new merchant account on PayU and posts all KYC details. This API returns the Merchant ID (MID) in the response.

> 📘 Note:
>
> After using this API to create merchants, you can use the Update Merchant API to update the merchant details. For more information, refer to [Update Merchant Details API](ref:update_merchant_details_api).

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
--data-urlencode 'merchant[display_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[email]=merchant@example.com' \
--data-urlencode 'merchant[mobile]=9911100364' \
--data-urlencode 'merchant[business_details][pan]=FANPS6362D' \
--data-urlencode 'merchant[business_details][business_entity_type]=Sole Proprietorship' \
--data-urlencode 'merchant[business_details][registered_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[business_details][business_category]=Arts, Gifts & Stationery' \
--data-urlencode 'merchant[business_details][business_sub_category]=Art Dealers and Galleries' \
--data-urlencode 'merchant[business_details][pancard_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[product]=PayUbiz' \
--data-urlencode 'merchant[bank_details][account_no]=919010067278549' \
--data-urlencode 'merchant[bank_details][account_holder_name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[bank_details][ifsc_code]=UTIB0003557' \
--data-urlencode 'merchant[website_details][website_url]=https://www.example.com' \
--data-urlencode 'merchant[monthly_expected_volume]=12000' \
--data-urlencode 'merchant[signing_authority_details][name]=DIVY HARESHKUMAR SHAH' \
--data-urlencode 'merchant[signing_authority_details][pancard_number]=FANPS6362D' \
--data-urlencode 'merchant[signing_authority_details][email]=auth_email@example.com' \
--data-urlencode 'merchant[integration_type]=ThirdParty' \
--data-urlencode 'merchant[gst_number]=24FANPS6362D1ZE' \
--data-urlencode 'merchant[udyam_number]=UDYAM-UP-19-0002053' \
--data-urlencode 'merchant[gst_consent]=false'

```

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

> 📘 Mandatory and interdependent parameters:
>
> The merchant display name, email, mobile and business entity type parameters are mandatory. If the if the Pan No is posted, Pan Name also need to be posted along with it, otherwise will result in error. When posting bank account details, all the bank account details should be sent, which is, account no, IFSC, account holder name.

<details>
  <summary>Reference information for request parameters</summary>

  | Parameter                          | Reference                                                                                                                  |
  | :--------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
  | merchant\[business\_category]      | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
  | merchant\[business\_entity\_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
  | merchant\[business\_sub\_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |
</details>