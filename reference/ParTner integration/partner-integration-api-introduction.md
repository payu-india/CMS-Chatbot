---
title: Introduction
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Partner Integration APIs Introduction
  description: >-
    Explore how to use the PayU Partner Integration APIs to seamlessly integrate
    partner programs. This part of the API reference provides detailed
    instructions, request parameters, and sample responses for efficient partner
    management.
  keywords:
    - Partner Integration APIs
    - ' partner programs'
    - ' integration'
    - ' secure partner management'
    - ' tokenization'
    - ' partner onboarding'
    - ' manage partners'
  robots: index
next:
  description: ''
---
This documentation includes the APIs related to Partner Program Integration. It is recommended to use the APIs in this documentation as described in the following flow diagram:

![](https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/04/Screenshot-2022-04-19-at-10.30.15-AM.png)

## List of APIs

The APIs which must be used in various parts of the above flow diagram are listed in the following table:

| **Command**                                               | **API**                                                                                      |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Get Token                                                 | [Get Token API](ref:get_token_api)                                                           |
| **Create and Update Merchant**                            |                                                                                              |
| Create Merchant                                           | [Create Merchant API](ref:create_merchant_api)                                               |
| Update and Submit Bank Details                            | [Add or Update Bank Details API](ref:add_update_bank_details_api)                            |
| Update Merchant                                           | [Update Merchant Details API](ref:update_merchant_details_api)                               |
| **Verify Bank Details and KYC**                           |                                                                                              |
| Get Merchant                                              | [Get Merchant API](ref:get_merchant_api)                                                     |
| Verify and Link Merchant                                  | [Verify and Link Merchant API](ref:verify_and_link_merchant_api)                             |
| Penny Verification                                        | [Penny Verify API](ref:penny_verify_api)                                                     |
| **User Token APIs**                                       |                                                                                              |
| Send OTP                                                  | [Send OTP API](ref:send_otp_api)                                                             |
| Verify OTP                                                | [Verify OTP API](ref:verify_otp_api)                                                         |
| **Manage KYC**                                            |                                                                                              |
| List of Documents Required                                | [Info KYC Document API](ref:info_kyc_document_api)                                           |
| Upload Documents for KYC                                  | [Create KYC Document](ref:create_kyc_document_api)                                           |
| Delete KYC Documents                                      | [Delete KYC Document API](ref:delete_kyc_document_api)                                       |
| Post CKYC to PayU                                         | [Post CKYC API](ref:post_ckyc_api)                                                           |
| Upload Aadhaar Details in XML format                      | [Upload Aadhaar XML Offline API](ref:upload_aadhaar_xml_offline_api)                         |
| **E-Sign Flow APIs**                                      |                                                                                              |
| Generate Merchant Agreement for E-sign                    | [Generate Merchant Agreement for E-sign API](ref:generate-merchant-agreement-for-e-sign-api) |
| Send OTP to Merchant (Required for Signing the Agreement) | [Send OTP to Signatory Email API](ref:send-otp-to-signatory-email-api)                       |
| E-Sign the Merchant Agreement Document                    | [E-Sign Merchant Agreement API](ref:e-sign-merchant-agreement-api)                           |