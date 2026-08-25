---
title: Onboarding and KYC APIs
deprecated: false
hidden: false
metadata:
  title: Onboarding and KYC APIs
  robots: index
---
These map to the **Partner APIs** reference section and follow the 16-step onboarding sequence:

| Description                                                                                                                     | **API**                                                                   |
| :------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------ |
| **Step 00 — Authentication**                                                                                                    |                                                                           |
| Obtains an OAuth bearer token for Partner Onboarding APIs. Call this first; use the returned `access_token` on all later steps. | [Get Token API](ref:get_token_partner_integration)                        |
| **Step 01 — Create Merchant**                                                                                                   |                                                                           |
| Creates a new merchant shell account on PayU. Returns `mid`, `uuid`, and `product_account_uuid`.                                | [Create Merchant API](ref:createmerchant)                                 |
| **Step 02 — Update Merchant Details**                                                                                           |                                                                           |
| Sets the merchant PAN and date of birth or incorporation.                                                                       | [Update Merchant Details API](ref:updatemerchant_pan_dob_entity)          |
| **Step 03 — CKYC Verification**                                                                                                 |                                                                           |
| Sends an OTP to the merchant mobile for CKYC verification (Individual / Sole Proprietorship).                                   | [Send CKYC OTP API](ref:sendckycotp)                                      |
| Verifies the OTP from Step 03A and returns CKYC identity data.                                                                  | [Verify CKYC OTP API](ref:verifyckycotp)                                  |
| Fetches CKYC identity data using PAN without OTP (all other entity types).                                                      | [Fetch CKYC Data API](ref:fetchckycdata)                                  |
| **Step 04 — Update: Business Details**                                                                                          |                                                                           |
| Adds business category, sub-category, expected volume, GST, business name, and CIN where required.                              | [UpdateMerchant Business Details API](ref:updatemerchant_businessdetails) |
| **Step 05 — Update Bank Details**                                                                                               |                                                                           |
| Adds settlement bank account details. PayU attempts auto-verification after this step.                                          | [UpdateMerchant Bank Details API](ref:updatemerchant_bankdetails)         |
| **Step 06 — Upload Bank Proof (Conditional)**                                                                                   |                                                                           |
| Uploads bank account proof when auto-verification from Step 05 failed.                                                          | [Upload Bank Proof API](ref:uploadbankproof)                              |
| **Step 07 — Update: Website Details**                                                                                           |                                                                           |
| Adds the merchant website and/or app store URLs.                                                                                | [Update Website Details API](ref:updatemerchant_websitedetails)           |
| **Step 08 — Add Signatory Details**                                                                                             |                                                                           |
| Submits the authorised signatory for the merchant agreement. Prerequisite for DigiLocker.                                       | [Add Signatory Details API](ref:addsignatorydetails)                      |
| **Step 09 — DigiLocker Verification**                                                                                           |                                                                           |
| Creates a DigiLocker authentication URL for Aadhaar-based verification.                                                         | [Generate DigiLocker Link API](ref:generatedigilockerlink)                |
| **Step 10 — Update: Addresses**                                                                                                 |                                                                           |
| Adds registration and operating addresses for the merchant.                                                                     | [Update Merchant Addresses API](ref:updatemerchant_addresses)             |
| **Step 11 — Video KYC (VKYC)**                                                                                                  |                                                                           |
| Creates a Video KYC profile and returns a VCIP capture link.                                                                    | [Create VKYC Profile API](ref:createvkycprofile)                          |
| **Step 12 — Add/Update UBO**                                                                                                    |                                                                           |
| Submits Ultimate Beneficial Owner details (entity-dependent).                                                                   | [Add/Update UBO API](ref:addupdateubo)                                    |
| **Step 13 — Business Members & KMP**                                                                                            |                                                                           |
| Submits directors, partners, or designated partners.                                                                            | [Submit Business Members API](ref:submitbusinessmembers)                  |
| Retrieves business members already submitted for the merchant.                                                                  | [List Business Members API](ref:list_business_members_api)                |
| **Step 14 — Fetch Required KYC Documents**                                                                                      |                                                                           |
| Returns document categories and accepted types required for the merchant.                                                       | [Fetch Required KYC Documents API](ref:fetchrequireddocs)                 |
| **Step 15 — Upload KYC Documents**                                                                                              |                                                                           |
| Uploads one KYC document per required category from Step 14.                                                                    | [Upload KYC Document API](ref:uploadkycdocument)                          |
| Returns details for a previously uploaded KYC document, including a signed URL and status.                                      | [Show KYC Document API](ref:showkycdocument)                              |
| Deletes a previously uploaded KYC document.                                                                                     | [Delete KYC Document API](ref:deletekycdocument)                          |
| **Step 16 — E-Sign Agreement**                                                                                                  |                                                                           |
| Generates the merged merchant agreement document for electronic signing (final step).                                           | [Generate Agreement for E-Sign API](ref:generateagreementforesign)        |
| **Utilities**                                                                                                                   |                                                                           |
| Retrieves the full merchant profile and verification statuses. Call between any steps to check progress.                        | [Get Merchant Details API](ref:getmerchant)                               |
