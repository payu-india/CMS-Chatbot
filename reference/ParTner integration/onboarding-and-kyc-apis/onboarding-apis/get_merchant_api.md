---
title: Get Merchant API
excerpt: ''
api:
  file: partner-apis-6.json
  operationId: get_merchant
deprecated: false
hidden: false
metadata:
  title: Get Merchant Details API
  description: >-
    Learn how to use the PayU Get Merchant Details API to retrieve detailed
    information about merchants. This API Reference page provides comprehensive
    instructions, request parameters, and sample responses for efficient
    merchant management.
  robots: index
next:
  description: ''
---
The **Get Merchant** API is used to get the merchant details. You require the access token to get the merchant details using this API. The access token can be fetched using the Get Token API. For more information, refer to Get Token API.

> 📘 Note:
> 
> The access token with the scope as **refer_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

<PARTNEROnboardingEnvironment />

<details><summary>Sample request<details><summary>

```curl
curl --location -g --request GET '{{partner_base_url}}/api/v1/merchants/7060013' \
--header 'Authorization: bearer {{access_token}}'
```

</details>

<details><summary>Sample response<details><summary>

**Success scenario**

```
{
  "merchant": {
    "name": "test7_6july20",
    "email": "test3_6july20.aman.garg@payutest.in",
    "registered_mobile": "9466811031",
    "mid": 7060013,
    "product": "PayUmoney",
    "business_type": "LongTail",
    "business_name": null,
    "pancard_name": null,
    "pancard_number": null,
    "website_url": null,
    "android_url": null,
    "ios_url": null,
    "gst_number": null,
    "created_at": "2020-07-06T12:58:17.000Z",
    "mobile": "9466811031",
    "blocked": false,
    "first_name": "",
    "last_name": "test7_6july20",
    "bank_detail": {
      "bank_account_number": null,
      "ifsc_code": null,
      "holder_name": null,
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
    "business_entity": null,
    "status": "account_created",
    "partner_source": "Create Merchant API",
    "pan_verification_status": "Pending",
    "website_approval_status": "Not Applicable",
    "notification_email": "test3_6july20.aman.garg@payutest.in",
    "settlement_status": null,
    "is_service_agreement_accepted": false,
    "is_authorisation_letter_required": true,
    "monthly_expected_volume": null,
    "business_category": null,
    "business_sub_category": null,
    "bank_verification_status": null,
    "penny_deposit_status": null,
    "uuid": "11ea-bf88-5c1eb1f4-9363-0acb18027a2a",
    "document_status": "Pending"
  }
}
```

**Failure Scenarios**

- 401: Unauthorised request

```plaintext
{
  "status": "Unauthorized"
}
```

- 404: When merchant was not referred by partner

```plaintext
{
  "data": {
    "message": "Invalid merchant mid"
  }
}
```

- 422: When token is not of partner or not valid

```plaintext

  "error": "Partner Not Found"
}
```

- 404: When merchant is not found:

```plaintext
{
  "status": "NotFound"
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

## Request parameters

<br>