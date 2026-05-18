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

<Image align="center" src="https://files.readme.io/0448b6806e7c38a12a8542b86d85322ebf8ff6cab0d471d74b4d50541daec0a3-Screenshot_2025-05-12_at_12.17.17_PM.png" />

<Callout icon="👍">
  **Integration guide:** For Partner Integration, refer to [Partner Integration - Introduction](ref:partner-integration-api-introduction)
</Callout>

## List of APIs

The APIs which must be used in various parts of the above flow diagram are listed in the following table:

| Description                                                                                                            | **API**                                                                                      |
| ---------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Get Token                                                                                                              | [Get Token API](ref:get_token_api)                                                           |
| **Create and Update Merchant**                                                                                         |                                                                                              |
| Onboards a new merchant to the PayU platform.                                                                          | [Create Merchant API](ref:create_merchant_api)                                               |
| Used to add or modify the bank account information of a merchant.                                                      | [Add or Update Bank Details API](ref:add_update_bank_details_api)                            |
| Modifies the existing details of a merchant.                                                                           | [Update Merchant Details API](ref:update_merchant_details_api)                               |
| **Verify Bank Details and KYC**                                                                                        |                                                                                              |
| Retrieves the details of a specific merchant.                                                                          | [Get Merchant API](ref:get_merchant_api)                                                     |
| Verifies the information provided by the merchant and links their account to the partner.                              | [Verify and Link Merchant API](ref:verify_and_link_merchant_api)                             |
| **User Token APIs**                                                                                                    |                                                                                              |
| Sends a one-time password (OTP) to the merchant's registered mobile number or email address for verification purposes. | [Send OTP API](ref:send_otp_api)                                                             |
| Verifies the OTP entered by the merchant.                                                                              | [Verify OTP API](ref:verify_otp_api)                                                         |
| **Manage KYC**                                                                                                         |                                                                                              |
| Retrieves the list of required documents for KYC verification.                                                         | [Info KYC Document API](ref:info_kyc_document_api)                                           |
| Uploads the necessary KYC documents for the merchant.                                                                  | [Create KYC Document](ref:create_kyc_document_api)                                           |
| Deletes previously uploaded KYC documents.                                                                             | [Delete KYC Document API](ref:delete_kyc_document_api)                                       |
| Posts Central KYC (CKYC) data to PayU.                                                                                 | [Post CKYC API](ref:post_ckyc_api)                                                           |
| Uploads Aadhaar details in XML format for KYC.                                                                         | [Upload Aadhaar XML Offline API](ref:upload_aadhaar_xml_offline_api)                         |
| **E-Sign Flow APIs**                                                                                                   |                                                                                              |
| Generates the merchant agreement document for electronic signing.                                                      | [Generate Merchant Agreement for E-sign API](ref:generate-merchant-agreement-for-e-sign-api) |
| Sends an OTP to the merchant's email address for signing the agreement.                                                | [Send OTP to Signatory Email API](ref:send-otp-to-signatory-email-api)                       |
| Allows the merchant to electronically sign the agreement.                                                              | [E-Sign Merchant Agreement API](ref:e-sign-merchant-agreement-api)                           |
