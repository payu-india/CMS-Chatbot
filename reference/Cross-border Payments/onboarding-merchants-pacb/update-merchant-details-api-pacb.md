---
title: Update Merchant Details API - PACB
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Update Merchant Details** API is used to:

- Add or update any information about the merchant
- Update PAN details
- Authorized through User token (merchant token), obtained using Send OTP and Verify OTP APIs.

<Callout icon="📘" theme="info">
  ### Notes:

  - The Update Merchant API uses the uuid value as the path parameter. Use the uuid value that is in the **Create Merchant** API response for the corresponding merchant. For more information, refer to [Create Merchant API](ref:create_merchant_api).
  - The PAN verification will happen asynchronously, and the status will be made available in the **Get Merchant** API.
  - PAN name has to be the same as the business name for successful verification
  - Partner needs to create a form within the application to collect this information
  - All the fields in this API are not mandatory except the GST details, but when you are using this API, you must update atleast a merchant's details using a parameter.
  - The entire payload needs to be submitted for update requests as well
  - No updates are allowed after successful PAN verification. PAN verification status is available in the get merchant API. If the merchant wants to update any information after PAN verification, you need to contact the PayU Care team through help.payu.in
</Callout>

### Steps to get the Bearer token

1. Generate token using the [Get Token API](ref:get_token_api)and use it in [Send OTP API](ref:send_otp_api) with the send\_sign\_in\_otp as the scope.
2. generate token using the [Get Token API](ref:get_token_api)and use it in [Verify OTP API](ref:verify_otp_api) with the verify\_sign\_in\_otp as the scope and the the OTP received in Step 1.
3. Use the bearer token for this Update Merchant API from the response of Step 2.

<PARTNEROnboardingEnvironment />

## Request parameters

**Endpoint:** `PUT https://uat-partner.payu.in/api/v1/merchants/{product_account_uuid}/update`<br />**Content type:** `multipart/form-data` or form body.

Only the path parameter is required; all body fields are optional. Include only the fields you want to update.

### Path parameters

| Parameter                                          | Description                                                                                                             | Example                              |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------ |
| product\_account\_uuid<br /><code>mandatory</code> | <code>string</code> Unique identifier (UUID) of the merchant. Use the uuid value from the Create Merchant API response. | 11ec-ed65-770862dc-8758-026e3e71538e |

### Body parameters

| Parameter                                                                           | Description                                                                                                                                                                                                                   | Example                                                          |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| merchant\[display\_name]<br /><code>optional</code>                                 | <code>string</code> The display name of the merchant shown on PayU dashboard and reports.                                                                                                                                     | DIVY HARESHKUMAR SHAH                                            |
| merchant\[email]<br /><code>optional</code>                                         | <code>string</code> Primary email address of the merchant for communication and notifications.                                                                                                                                | [boro13@yomail.com](mailto:boro13@yomail.com)                    |
| merchant\[mobile]<br /><code>optional</code>                                        | <code>string</code> Primary mobile number of the merchant for communication and notifications.                                                                                                                                | 9916965913                                                       |
| merchant\[business\_details]\[pan]<br /><code>optional</code>                       | <code>string</code> Permanent Account Number (PAN) of the merchant business.                                                                                                                                                  | FANPS6362D                                                       |
| merchant\[business\_details]\[business\_entity\_type]<br /><code>optional</code>    | <code>string</code> Type of business entity (e.g. Sole Proprietorship, Partnership, Private Limited).                                                                                                                         | Sole Proprietorship                                              |
| merchant\[business\_details]\[pancard\_name]<br /><code>optional</code>             | <code>string</code> The name as it appears on the PAN card.                                                                                                                                                                   | DIVY HARESHKUMAR SHAH                                            |
| merchant\[business\_details]\[registered\_name]<br /><code>optional</code>          | <code>string</code> The registered legal name of the merchant business.                                                                                                                                                       | DIVY HARESHKUMAR SHAH                                            |
| merchant\[business\_details]\[business\_category]<br /><code>optional</code>        | <code>string</code> The primary business category of the merchant.                                                                                                                                                            | Arts, Gifts & Stationery                                         |
| merchant\[business\_details]\[business\_sub\_category]<br /><code>optional</code>   | <code>string</code> A more specific subcategory related to the business.                                                                                                                                                      | Art Dealers and Galleries                                        |
| merchant\[product]<br /><code>optional</code>                                       | <code>string</code> The PayU product (e.g. PayUbiz, PayUmoney).                                                                                                                                                               | PayUbiz                                                          |
| merchant\[bank\_details]\[account\_no]<br /><code>optional</code>                   | <code>string</code> Bank account number of the merchant for settlements.                                                                                                                                                      | 919010067278549                                                  |
| merchant\[bank\_details]\[account\_holder\_name]<br /><code>optional</code>         | <code>string</code> Name of the account holder as per bank records.                                                                                                                                                           | DIVY HARESHKUMAR SHAH                                            |
| merchant\[bank\_details]\[ifsc\_code]<br /><code>optional</code>                    | <code>string</code> IFSC code of the bank branch for settlements.                                                                                                                                                             | UTIB0003557                                                      |
| merchant\[website\_details]\[website\_url]<br /><code>optional</code>               | <code>string</code> The merchant's website URL.                                                                                                                                                                               | [https://www.google.com](https://www.google.com)                 |
| merchant\[monthly\_expected\_volume]<br /><code>optional</code>                     | <code>integer</code> The monthly expected transaction volume in monetary terms.                                                                                                                                               | 12000                                                            |
| merchant\[signing\_authority\_details]\[name]<br /><code>optional</code>            | <code>string</code> Name of the authorized representative or signing authority.                                                                                                                                               | DIVY HARESHKUMAR SHAH                                            |
| merchant\[signing\_authority\_details]\[pancard\_number]<br /><code>optional</code> | <code>string</code> PAN card number of the signing authority. If posted, pancard\_name is required.                                                                                                                           | FANPS6362D                                                       |
| merchant\[signing\_authority\_details]\[email]<br /><code>optional</code>           | <code>string</code> Email of the authorized representative or signing authority.                                                                                                                                              | [email\_test1213@yopmail.com](mailto:email_test1213@yopmail.com) |
| merchant\[integration\_type]<br /><code>optional</code>                             | <code>string</code> Type of integration for the merchant's account.                                                                                                                                                           | —                                                                |
| merchant\[gst\_number]<br /><code>optional</code>                                   | <code>string</code> The GST number of the merchant business.                                                                                                                                                                  | 24FANPS6362D1ZE                                                  |
| merchant\[udyam\_number]<br /><code>optional</code>                                 | <code>string</code> Udyam Registration Number for MSMEs. The Udyam Registration Number (URN) is a unique, permanent 16-digit alphanumeric or 19-digit identifier issued by the Ministry of MSME to legal enterprises in India | UDYAM-UP-19-0002053                                              |
| merchant\[gst\_consent]<br /><code>optional</code>                                  | <code>string</code> Consent for GST verification and processing (e.g. true/false).                                                                                                                                            | false                                                            |

## Sample request

```curl
curl --location --request PUT 'https://uat-partner.payu.in/api/v1/merchants/11ec-ed65-770862dc-8758-026e3e71538e/update' \
--header 'Authorization: Bearer 5a0260ef08e0a6e7b925b350521f10073a3d4713442e62c489c74e804938843d' \
--form 'merchant[business_sub_category]="Flowers and Gifts"' \
--form 'merchant[business_category]="Ecommerce"' \
--form 'merchant[business_entity]="Sole Proprietorship"' \
```

## Sample response

```json
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

<br />
