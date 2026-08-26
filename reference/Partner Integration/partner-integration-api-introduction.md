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


<Image src="https://files.readme.io/0448b6806e7c38a12a8542b86d85322ebf8ff6cab0d471d74b4d50541daec0a3-Screenshot_2025-05-12_at_12.17.17_PM.png" align="center" />


<Callout icon="👍" theme="okay">
  **Integration guide:** For Partner Integration, refer to [Partner Integration - Introduction](ref:partner-integration-api-introduction)
</Callout>

## List of APIs

The APIs which must be used in various parts of the above flow diagram are listed in the following tables.&#x20;

## Onboarding APIs

The following APIs are used to onboard and manage merchants through Partner Integration:

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

## Manage Invoices or Payment Links

| Description                                                            | **API**                                                                                          |
| :--------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| Creates a new payment link for a customer through Partner Integration. | [Create Payment Link - Partner Integration](https://docs.payu.in/reference/createpaymentlinkapi) |
| Retrieves a single payment link using its invoice number.              | [Get Single Payment Link API](https://docs.payu.in/reference/get_single_payment_link_api)        |
| Updates a payment link's status and expiry date.                       | [Update Payment Link API](https://docs.payu.in/reference/update_invoice_api)                     |

## Partner Payment Integration APIs

| Description                                                                                                               | **API**                                                                                                                     |
| :------------------------------------------------------------------------------------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- |
| Provides the access-token flow for Partner Integration.                                                                   | [Get Access Token - Partner Integration](https://docs.payu.in/reference/getting-access-token)                               |
| Integrates PayU Hosted Checkout by redirecting customers to PayU's payment page and handling the response.                | [Hosted Checkout Integration - Partner Integration](https://docs.payu.in/reference/hosted-checkout-api-partner-integration) |
| Initiates server-to-server UPI payments for Partner Integration and supports payment verification and callbacks.          | [UPI S2S Integration API - Partner Integration](https://docs.payu.in/reference/upi-s2s-partner-integration-api)             |
| Integrates third-party validation through UPI by including the customer's bank account number in the transaction request. | [UPI TPV Integration API - Partner Integration](https://docs.payu.in/reference/upi-tpv-integration-api-partner)             |
| Cancels an authorised transaction or refunds a captured transaction for Partner Integration.                              | [Partner Refund Transaction API](https://docs.payu.in/reference/refund-transaction-api-partner-integration)                 |
| Checks the status of a refund transaction.                                                                                | [Partner Refund Status API](https://docs.payu.in/reference/refund-status-api-partner-integration)                           |

## Using Webhooks for Merchant Status

| Description                                                                                 | **API**                                                                                                                                         |
| :------------------------------------------------------------------------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------- |
| Registers a partner webhook URL using a hub token to receive merchant status notifications. | [Register Webhooks API to Get Real-Time Merchant Status](https://docs.payu.in/reference/register-webhooks-api-to-get-real-time-merchant-status) |
| Receives real-time merchant onboarding status updates through registered webhooks.          | [Get Real-Time Merchant Status using Webhooks](https://docs.payu.in/reference/get-real-time-merchant-status-using-webhooks)                     |
| Lists KYC errors and corresponding solutions.                                               | [KYC Errors and Solutions](https://docs.payu.in/reference/kyc-errors-and-solutions)                                                             |

## OAuth API

| Description                                                           | **API**                                                                                              |
| :-------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| Validates an authorisation code and client.                           | [Validate Auth Code and Client API](https://docs.payu.in/reference/validate_authcode_and_client_api) |
| Retrieves merchant credentials used to generate the API key and salt. | [Get Merchant Credentials API](https://docs.payu.in/reference/get_merchant_credentials_api)          |