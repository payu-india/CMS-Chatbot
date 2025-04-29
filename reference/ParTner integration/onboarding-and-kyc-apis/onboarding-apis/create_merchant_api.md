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
The **Create Merchant** API is used to:

- Create a new merchant account on PayU and post all KYC details
- Returns the Merchant ID (mid) in the response.

This API is authorised through a client token generated using the client ID and secret.

> 📘 Note:
> 
> The access token with the scope as **refer_merchant **is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get_token_api).

<details><summary>Sample response</summary>

```
{
  "merchant": {
    "name": "test",
    "email": "test@payu.in",
    "registered_mobile": "9999910014",
    "mid": 129463,
    "product": "PayUbiz",
    "business_type": "LongTail",
    "business_name": "Test",
    "pancard_name": "Test",
    "pancard_number": "ABCPG1234J",
    "cin_number":"U72400MH2006PTC293037",
    "website_url": null,
    "android_url": null,
    "ios_url": null,
    "gst_number": null,
    "created_at": "2020-12-08T11:03:56.000Z",
    "mobile": "9999910014",
    "blocked": false,
    "first_name": "",
    "last_name": "test",
    "bank_detail": {
      "bank_account_number": "234567891",
      "ifsc_code": "ICIC0000734",
      "holder_name": "Test"
    },
    "operating_address": {
      "address_line": "operational addr",
      "city": "Sant Ravidas Nagar",
      "state": "UTTAR PRADESH",
      "pincode": 221304
    },
    "registration_address": {
      "address_line": "busenaddres line",
      "city": "Sant Ravidas Nagar",
      "state": "UTTAR PRADESH",
      "pincode": 221303
    },
    "business_entity": "LLP",
    "status": "account_created",
    "partner_source": "Create Merchant API",
    "pan_verification_status": "Pending",
    "website_approval_status": "Pending",
    "notification_email": "test@payu.in",
    "settlement_status": null,
    "is_service_agreement_accepted": false,
    "is_authorisation_letter_required": false,
    "monthly_expected_volume": 120000,
    "business_category": "Ecommerce",
    "business_sub_category": "Flowers and Gifts",
    "bank_verification_status": "Pending",
    "uuid": "11eb-3945-0fcf623a-86d9-026e3e71538e",
    "penny_deposit_status": "Not Initiated",
    "signing_authority": {
      "name": "test_auth",
      "email": "test_auth@payu.in"
    },
    "director1_details": {
      "name": "test1_dir",
      "email": "test1_dir@payu.in"
    },
    "director2_details": {
      "name": "test2_dir",
      "email": "test2_dir@payu.in"
    }
  }
}
```

</details>

<details><summary>Response parameters<details><summary>

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "merchant",
    "0-1": "This parameter contains the following details of the merchant in an array format.",
    "1-0": "business\\_entity",
    "1-1": "This parameter contains the business entity of the merchant that was provided while onboarding.",
    "2-0": "status",
    "2-1": "This parameter contains any of the following statuses:  \n`•\tdocuments_pending\n•\tbank_verified\n•\tdocument_upload_in_progress\n•\taccount_created\n•\tdocument_verification_in_progress\n•\twebsite_verification_in_progress\n•\tdocuments_rejected\n•\tlive\n•\tsettlement_on_hold\n•\tagreement_pending\n•\tagreement_rejected\n•\tnot_available\n•\twebsite_error\n•\tprofile_rejected\n•\tdocuments_pending\n•\tbank_verified\n•\tdocument_upload_in_progress\n•\taccount_created\n•\tdocument_verification_in_progress\n•\twebsite_verification_in_progress\n•\tdocuments_rejected\n•\tlive\n•\tsettlement_on_hold\n•\tagreement_pending\n•\tagreement_rejected\n•\tnot_available\n•\twebsite_error\n•\tprofile_rejected`",
    "3-0": "partner\\_source",
    "3-1": "This parameter returns the source through which the merchant joined or onboarded.",
    "4-0": "pan\\_verification\\_status",
    "4-1": "This parameter contains any of the following PAN verification statuses:  \n  \n   \n\t•\tSuccess  \n\t•\tPending  \n\t•\tFailed",
    "5-0": "website\\_approval\\_status",
    "5-1": "This parameter contains any of the following website approval statuses:  \n  \n   \n\t•\tWebsite Not live  \n\t•\tWebsite Incomplete  \n\t•\tWebsite Under Construction  \n\t•\tWebsite Error  \n\t•\tWebsite OK  \n\t•\tVerification in Process",
    "6-0": "notification\\_email",
    "6-1": "This parameter contains the email to which the notification was sent to the merchant on onboarding.",
    "7-0": "settlement\\_status",
    "7-1": "This parameter contains any of the following settlement statuses:  \n`•\tRisk Hold\n•\tThirdparty Hold\n•\tActive\n•\tSuspended\n•\tRisk & Thirdparty hold\n•\tNEFT Return\n•\tTerminate`",
    "8-0": "is\\_service\\_agreement\\_accepted",
    "8-1": "This parameter contains the flag whether the service agreement was accepted or not.",
    "9-0": "is\\_authorisation\\_letter\\_required",
    "9-1": "This parameter contains the flag whether the authorization letter is required or not required.",
    "10-0": "monthly\\_expected\\_volume",
    "10-1": "This parameter contains the monthly expected volume from the merchant.",
    "11-0": "business\\_category",
    "11-1": "This parameter contains the business category of the merchant that was provided while onboarding.",
    "12-0": "business\\_sub\\_category",
    "12-1": "This parameter contains the business sub-category of the merchant that was provided while onboarding.",
    "13-0": "bank\\_verification\\_status",
    "13-1": "This parameter contains any of the following bank verification statuses:  \n`•\tPending\n•\tSuccess\n•\tVerification Attempts Exhausted\n•\tFailed`",
    "14-0": "penny\\_deposit\\_status",
    "14-1": "This parameter contains any of the following penny deposit statuses when bank account verification was performed:  \n`•\tNot Initiated\n•\tPending\n•\tSENT_TO_BANK\n•\tSuccess\n•\tFailed`",
    "15-0": "uuid",
    "15-1": "This parameter contains the Universal Unique Identifier (UUID).",
    "16-0": "document\\_status",
    "16-1": "This parameter contains the document status and can be any of the following:  \n  \n   \n\t•\tPending: It indicates that document not yet submitted  \n\t•\tDocs Received: It indicates that documents are submitted  \n\t•\tDocs Approved: It indicates that documents are approved  \n\t•\tDocs Error: It indicates that mismatch in data or wrong document"
  },
  "cols": 2,
  "rows": 17,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

## Request Parameters

<details><summary>Reference information for request parameters</summary>

| Parameter                                         | Reference                                                                                                                  |
| :------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------- |
| merchant[business_details][business_category]     | For the list of business categories, refer to [Business. Category List](ref:partner-category-list).                        |
| merchant[business_details][business_entity_type]  | For the list of business entity type, refer to [Business Entity Type](ref:partner-category-list#business-entity-type).     |
| merchant[business_details][business_sub_category] | For the list of business subcategories, refer to [Business Sub-Category](ref:partner-category-list#business-sub-category). |

</details>