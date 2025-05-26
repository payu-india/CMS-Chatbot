---
title: Update Merchant Details API
excerpt: ''
api:
  file: partner-integration-updated-2.json
  operationId: UpdateMerchantDetails
deprecated: false
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
    - ' merchant information'
    - ' PAN details'
    - ' secure merchant management'
    - ' tokenization'
    - ' update merchant'
    - ' manage merchants'
  robots: index
next:
  description: ''
---
The **Update Merchant Details** API is used to:

* Add or update any information about the merchant
* Update PAN details
* Authorized through User token (merchant token), obtained using Send OTP and Verify OTP APIs.

> 📘 Notes:
>
> * The PAN verification will happen asynchronously, and the status will be made available in the Get Merchant API.
> * PAN name has to be the same as the business name for successful verification
> * Partner needs to create a form within the application to collect this information
> * All the fields in this API are mandatory except the GST details
> * The entire payload needs to be submitted for update requests as well
> * No updates are allowed after successful PAN verification. PAN verification status is available in the get merchant API. If the merchant wants to update any information after PAN verification, you need to contact the PayU Care team through help.payu.in

> 📘 Bearer Token:
>
> The access token with the scope as **referer\_merchant** is required on the header. For more information on getting the access token, refer to [Get Token API](ref:get-token-api).

| \*\* Environment\*\* | \*\* URL\*\*                                                                         |
| :------------------- | :----------------------------------------------------------------------------------- |
| production           | [https://partner.payu.in/api/v3/merchants](https://partner.payu.in/api/v3/merchants) |
| UAT                  | uat-partner.payu.in/api/v3/merchants                                                 |

<details>
  <summary>Sample request</summary>

```curl
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/11ec-ed65-770862dc-8758-026e3e71538e/update' \
--header 'Authorization: Bearer 5a0260ef08e0a6e7b925b350521f10073a3d4713442e62c489c74e804938843d' \
--form 'merchant[business_sub_category]="Flowers and Gifts"' \
--form 'merchant[business_category]="Ecommerce"' \
--form 'merchant[business_entity]="Sole Proprietorship"' \
--form 'merchant[business_name]="Harsh Agarwal"' \
--form 'merchant[pancard_number]="AUKPA1386M"' \
--form 'merchant[signing_authority_details][email]="kycsanity9@yopmail.com"' \
--form 'merchant[signing_authority_details][name]="Harsh Agarwal"' \
--form 'merchant[signing_authority_details][pancard_number]="AUKPA1386M"' \
--form 'merchant[signing_authority_details][email]="ashsih@payu.in"' \
--form 'merchant[signing_authority_details][name]="Ashish Kumar"' \
--form 'merchant[signing_authority_details][pancard_number]="OPSPS0921B"' \
--form 'merchant[signing_authority_details][cin_number]="U72400MH2006PTC293037"' \
--form 'merchant[director1_details][name]="John Doe"' \
--form 'merchant[director1_details][email]="john_dir@payu.in"' \
--form 'merchant[director2_details][name]="Jane Doe"' \
--form 'merchant[director2_details][email]="jane_dir@payu.in"' \
--form 'merchant[monthly_expected_volume]="60000"' \
--form 'merchant[operating_address][address_line]="Sector 98"' \
--form 'merchant[operating_address][city]="Noida"' \
--form 'merchant[operating_address][state]="UTTAR PRADESH"' \
--form 'merchant[operating_address][pincode]="201307"' \
--form 'merchant[registration_address][address_line]="Sector 98"' \
--form 'merchant[registration_address][city]="Noida"' \
--form 'merchant[registration_address][state]="UTTAR PRADESH"' \
--form 'merchant[registration_address][pincode]="201306"'
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