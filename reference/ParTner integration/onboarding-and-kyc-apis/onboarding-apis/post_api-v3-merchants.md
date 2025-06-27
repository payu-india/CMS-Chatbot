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

{/* Replace the custom component with regular markdown content */}
## Environment
- **Test Environment**: https://uat-partner.payu.in/api/v3/merchants
- **Production Environment**: https://partner.payu.in/api/v3/merchants

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

* With all the parameters posted in request

```json
{
  "merchant": {
    "name": "DIVY HARESHKUMAR SHAH",
    "email": "merchant@example.com",
    "registered_mobile": "9916965913",
    "mid": 8791789,
    "product": "PayUbiz",
    "business_type": "LongTail",
    "business_name": "DIVY HARESHKUMAR SHAH",
    "pancard_name": "DIVY HARESHKUMAR SHAH",
    "pancard_number": "FANPS6362D",
    "website_url": "https://www.example.com",
    "android_url": null,
    "ios_url": null,
    "gst_number": "24FANPS6362D1ZE",
    "created_at": "2025-06-26T07:13:35.000Z",
    "mobile": "9916965913",
    "blocked": false,
    "first_name": "DIVY",
    "last_name": "HARESHKUMAR SHAH",
    "bank_detail": {
      "bank_account_number": "919010067278549",
      "ifsc_code": "UTIB0003557",
      "holder_name": "DIVY HARESHKUMAR SHAH",
      "nodal_code": null,
      "nodal_status": "Not Activated"
    },
    "operating_address": {
      "address_line": null,
      "city": null,
      "state": null,
      "pincode": null
    },
    "registration_address": {
      "address_line": null,
      "city": null,
      "state": null,
      "pincode": null
    },
    "business_entity": "Sole Proprietorship",
    "status": "live",
    "partner_source": "Create Merchant API",
    "pan_verification_status": "Success",
    "website_approval_status": "Pending",
    "notification_email": "merchant@example.com",
    "settlement_status": "Active",
    "is_service_agreement_accepted": false,
    "is_authorisation_letter_required": false,
    "monthly_expected_volume": 12000,
    "business_category": "Arts, Gifts & Stationery",
    "business_sub_category": "Art Dealers and Galleries",
    "bank_verification_status": "Pending",
    "uuid": "11f0-525d-1033b9d4-a277-021ec077a271",
    "penny_deposit_status": "Not Initiated",
    "document_status": "Docs Approved",
    "kyc_status": {
      "kyc_status": "PENDING",
      "adhaar_kyc_status": "PENDING",
      "ckyc_status": "PENDING"
    },
    "agreement_status": "Approved",
    "integration_type": "ThirdParty",
    "service_intent": "default"
  }
}
```

* With only the mandatory parameters

```json
{
  "merchant": {
    "name": "DIVY HARESHKUMAR SHAH",
    "email": "boro15@yomail.com",
    "registered_mobile": "9916965913",
    "mid": 8791796,
    "product": "PayUbiz",
    "business_entity": "Sole Proprietorship",
    "status": "account_created",
    "partner_source": "Create Merchant API",
    "uuid": "11f0-525d-76182ba4-954a-021ec077a271",
    "document_status": "Docs Approved",
    "agreement_status": "Approved",
    "integration_type": "Not Selected",
    "service_intent": "default"
  }
}
```

### Failure scenario

## Response parameters

### Fields in the merchant object

| Parameter             | Description                                                                        | Example                              |
| :-------------------- | :--------------------------------------------------------------------------------- | :----------------------------------- |
| mid                   | Unique merchant identifier                                                         | 8390925                              |
| kyc_document_name     | Name of the KYC document category                                                  | PAN Card of Signing Authority        |
| kyc_document_uuid     | Unique identifier for the KYC document submission                                  | 11ef-587e-43837330-95b0-021ec077a271 |
| kyc_document_status   | Current status of the KYC document (e.g., DOCUMENT_SUBMITTED, VERIFIED, REJECTED) | DOCUMENT_SUBMITTED                  |
| error_message        | Error message if document verification failed, null otherwise                      | null                                 |
| created_at           | Timestamp when the KYC document was created/submitted.                             | 2024-08-12T07:41:19.000Z             |

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

### Additional info

| Parameter | Reference |
|:--------------------------|:----------------------------------------------------------|
| merchant[business_category] | For the list of business categories, refer to [Business Category List](ref:partner-category-list). |
| merchant[business_entity_type] | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type). |
| merchant[business_sub_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |