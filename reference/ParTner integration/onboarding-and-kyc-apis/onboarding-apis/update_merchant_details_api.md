---
api:
  file: payu_merchant_api_final.json
  operationId: updateMerchantById
hidden: false
metadata:
  title: Update Merchant Details API
  description: >-
    Learn how to use the PayU Update Merchant Details API to add or update
    merchant information, including PAN details. This API Reference page
    provides detailed instructions, request parameters, and sample responses for
    efficient merchant management.
  keywords:
    - Update Merchant Details API
    - merchant information
    - PAN details
    - secure merchant management
    - tokenization
    - update merchant
    - manage merchants
---
The **Update Merchant Details** API is used to:

* Add or update any information about the merchant
* Update PAN details
* Authorized through User token (merchant token), obtained using Send OTP and Verify OTP APIs.

> 📘 Notes:
>
> * The Update Merchant API uses the uuid value as the path parameter. Use the uuid value that is in the **Create Merchant** API response for the corresponding merchant. For more information, refer to [Create Merchant API](ref:create_merchant_api).
> * The PAN verification will happen asynchronously, and the status will be made available in the **Get Merchant** API.
> * PAN name has to be the same as the business name for successful verification
> * Partner needs to create a form within the application to collect this information
> * All the fields in this API are not mandatory except the GST details, but when you are using this API, you must update atleast a merchant's details using a parameter.
> * The entire payload needs to be submitted for update requests as well
> * No updates are allowed after successful PAN verification. PAN verification status is available in the get merchant API. If the merchant wants to update any information after PAN verification, you need to contact the PayU Care team through help.payu.in

<br />

<Partner_Postman />

<br />

### Steps to get the Bearer token

1. Generate token using the [Get Token API](ref:get_token_api)and use it in [Send OTP API](ref:send_otp_api) with the send_sign_in_otp as the scope.
2. generate token using the [Get Token API](ref:get_token_api)and use it in [Verify OTP API](ref:verify_otp_api) with the verify_sign_in_otp as the scope and the the OTP received in Step 1.
3. Use the bearer token for this Update Merchant API from the response of Step 2.

<PARTNEROnboardingEnvironment />

<details>
  <summary>Sample request</summary>

  ```curl
  curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/11ec-ed65-770862dc-8758-026e3e71538e/update' \
  --header 'Authorization: Bearer 5a0260ef08e0a6e7b925b350521f10073a3d4713442e62c489c74e804938843d' \
  --form 'merchant[business_sub_category]="Flowers and Gifts"' \
  --form 'merchant[business_category]="Ecommerce"' \
  --form 'merchant[business_entity]="Sole Proprietorship"' \
  ```
</details>

<details>
  <summary>Sample response</summary>

  ```
  {
  "merchant": {
  "name": "Merchant",
  "email": "kycsanity9@yopmail.com",
  "registered_mobile": "8447641351",
  "mid": 5018124,
  "product": "PayUbiz",
  "business_type": "LongTail",
  "business_name": "Harsh Agarwal",
  "pancard_name": "Harsh Agarwal",
  "pancard_number": "AUKPA1386M",
  "website_url": null,
  "android_url": null,
  "ios_url": null,
  "gst_number": null,
  "created_at": "2022-06-16T11:14:19.000Z",
  "mobile": "8447641351",
  "blocked": false,
  "first_name": "",
  "last_name": "Merchant",
  "bank_detail": {
  "bank_account_number": "8388282849123",
  "ifsc_code": "SBIN0008239",
  "holder_name": "Harsh Agarwal",
  "nodal_code": null,
  "nodal_status": null
  },
  "operating_address": {
  "address_line": "Sector 98",
  "city": "Noida",
  "state": "UTTAR PRADESH",
  "pincode": "201307"
  },
  "registration_address": {
  "address_line": "Sector 98",
  "city": "Noida",
  "state": "UTTAR PRADESH",
  "pincode": "201307"
  },
  "business_entity": "Sole Proprietorship",
  "status": "account_created",
  "partner_source": "Create Merchant API",
  "pan_verification_status": "Pending",
  "website_approval_status": null,
  "notification_email": "kycsanity9@yopmail.com",
  "settlement_status": null,
  "is_service_agreement_accepted": false,
  "is_authorisation_letter_required": false,
  "monthly_expected_volume": "60000",
  "business_category": "Ecommerce",
  "business_sub_category": "Flowers and Gifts",
  "bank_verification_status": null,
  "uuid": "11ec-ed65-770862dc-8758-026e3e71538e",
  "penny_deposit_status": null,
  "service_intent": "default",
  "signing_authority": {
  "name": "Harsh Agarwal",
  "email": "kycsanity9@yopmail.com"
  }
  }
  }
  ```
</details>

## Request parameters
