---
title: Refer merchants using APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: Refer Merchants using Integration APIs
  description: >-
    Efficiently onboard referral merchants with PayU's Partner Integration API.
    Follow our detailed guide to integrate the referral process seamlessly,
    manage referrals, and optimize your partnership benefits. Discover how to
    use PayU's API for streamlined referral onboarding today.
  keywords:
    - PayU API referral onboarding
    - PayU Partner integration API
    - API merchant referral onboarding
    - PayU referral API integration.Merchant onboarding PayU API
    - PayU partner program API.Referral onboarding via PayU API
    - API-based referral onboarding PayU
    - Integrate PayU referral API
    - PayU partner API guide
  robots: index
next:
  description: ''
---
This documentation provides comprehensive guidance for integrating with PayU's Partner Integration API. This API enables businesses and individual partners to integrate PayU's payment solutions into their platforms, onboard merchants, and manage the complete merchant lifecycle.

## Overview

PayU merchant onboarding APIs allows partners to:

- Onboard merchants to the PayU platform
- Manage merchant KYC processes
- Verify bank account details
- Handle electronic signatures for agreements
- Receive real-time status updates via webhooks

## Authentication and Authorization

PayU Merchant Onboarding employs token-based authentication with OAuth 2.0 standards. Partners must obtain tokens through appropriate authentication endpoints before accessing the API resources.

### Token Management Flow

The token-based authentication works as follows:

- Partners obtain an access token using their credentials
- This token is included in subsequent API requests
- Tokens expire after a set period and must be refreshed

> **Important**: Access tokens should be securely stored and never exposed in client-side code.

<Accordion title="User Token APIs" icon="fa-info-circle">
  The Merchant Onboarding Integration offers several token-related endpoints for authentication purposes. These endpoints handle token generation, refresh, and OTP verification when required.

  * [Partner Integration User Token APIs](https://docs.payu.in/reference/partner-integration-user-token-apis#/)
  * [Get Token API](https://docs.payu.in/reference/get_token_api#/)
  * [Refresh Token API](https://docs.payu.in/reference/refresh_token_api#/)
</Accordion>

## Merchant Onboarding Process

The Merchant Onboarding flow consists of several key steps:

1. Create a merchant record with basic details
2. Update additional merchant information as needed
3. Add and verify bank account details
4. Upload the required KYC documents
5. Complete e-signature process for merchant agreement
6. Monitor merchant status through webhooks

<Accordion title="Create, Update, and Manage Merchants" icon="fa-info-circle">
  The APIs for merchant creation and management allow partners to register new merchants and update their information.

  For detailed specifications on merchant onboarding, please refer to:

  * [Create Merchant API](https://docs.payu.in/reference/create_merchant_api#/)
  * [Update Merchant Details API](https://docs.payu.in/reference/update_merchant_details_api#/)
  * [Get Merchant API](https://docs.payu.in/reference/get_merchant_api#/)
</Accordion>

<Accordion title="Bank Account Verification" icon="fa-info-circle">
  Bank account verification is a critical step in the merchant onboarding process. PayU provides specific APIs for adding, updating, and verifying bank details.

  For specifications on bank verification, please refer to:

  * [Add Update Bank Details API](https://docs.payu.in/reference/add_update_bank_details_api#/)
</Accordion>

## KYC Document Management

The KYC process requires merchants to provide various identification and business documents. These APIs facilitate document upload and verification.

### Document Requirements

Different merchant types require different documentation. The exact requirements should be determined by referencing the official PayU documentation.

<Accordion title="Document Upload APIs" icon="fa-info-circle">
  For specifications on KYC document management, please refer to:

  * [Docs Required API](https://docs.payu.in/reference/docs_required_api#/)
  * [Create KYC Document API](https://docs.payu.in/reference/create_kyc_document_api#/)
  * [Delete KYC Document API](https://docs.payu.in/reference/delete_kyc_document_api#/)
  * [Upload Aadhar XML Offline API](https://docs.payu.in/reference/upload_aadhaar_xml_offline_api#/)
</Accordion>

### Document Types and Guidelines

PayU accepts various document types for KYC verification, including:

- Identity proofs (PAN Card, Aadhaar, etc.)
- Address proofs
- Business registration documents
- Bank account proofs

For an exhaustive list of documents required for an entity, please refer to [KYC Checklist](https://docs.payu.in/docs/documents-checklist-for-account-activation#/).

For an the business category & subcategory details, please refer to [Partner Category List](https://docs.payu.in/reference/partner-category-list#/).

## E-Sign Flow

The electronic signature process is required to complete merchant agreements. PayU provides specific APIs to manage this workflow.

For e-signature specifications, please refer to:

<Accordion title="E-sign APIs" icon="fa-info-circle">
  * [E-Sign Flow APIs](https://docs.payu.in/reference/e-sign-flow-apis#/)
  * [Generate Merchant Agreement for E-Sign API](https://docs.payu.in/reference/generate-merchant-agreement-for-e-sign-api#/)
  * [Send OTP to Signatory Email API](https://docs.payu.in/reference/send-otp-to-signatory-email-api#/)
  * [E-Sign Merchant Agreement API](https://docs.payu.in/reference/e-sign-merchant-agreement-api#/)
</Accordion>

## Webhooks for Real-Time Updates

Webhooks allow partners to receive notifications about changes in merchant status without polling the API.

For webhook integration details, please refer to:

- [Register Webhooks API](https://docs.payu.in/reference/register-webhooks-api-to-get-real-time-merchant-status#/)
- [Get Real-Time Merchant Status Using Webhooks](https://docs.payu.in/reference/get-real-time-merchant-status-using-webhooks#/)

### Security Considerations for Webhooks

Webhook requests should be authenticated to ensure they come from PayU. Implementation details can be found in the webhook documentation.

## Error Handling and Troubleshooting

### Common KYC Errors and Solutions

KYC document verification can encounter various issues. For detailed information on common errors and their solutions, please refer to:

<Accordion title="KYC errors" icon="fa-info-circle">
  | **Error**                                                                                 | **Solution**                                                                                                                                    |
  | ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
  | <h3>Authorisation Letter Document</h3>                                                    |                                                                                                                                                 |
  | Not all partners have signed on authorization letter                                      | Re-upload the authorization letter copy with name and signature from all the partners                                                           |
  | Names of all partners are not mentioned in authorization Letter                           | Re-upload the authorization letter copy with name and signature from all the partners                                                           |
  | Authorization Letter copy uploaded is not on firm's letterhead                            | Re-upload the authorization letter copy on firm's letterhead                                                                                    |
  | Company stamp is missing on uploaded copy of Authorization letter                         | Re-upload Authorization letter with signature and stamp                                                                                         |
  | Authorization letter copy not uploaded                                                    | Upload copy of authorization letter with signature and stamp                                                                                    |
  | Not all member have signed on authorization letter                                        | Re-upload the authorization letter copy with name and signature from all the member                                                             |
  | Names of all member are not mentioned in authorization Letter                             | Re-upload the authorization letter copy with name and signature from all the member                                                             |
  | signature is missing on uploaded copy of Authorization letter                             | Re-upload Authorization letter with signature and stamp                                                                                         |
  | Not all directors have signed on authorization letter                                     | Re-upload the authorization letter copy with name and signature from all the directors                                                          |
  | Names of all directors are not mentioned in authorization Letter                          | Re-upload the authorization letter copy with name and signature from all the directors                                                          |
  | Uploaded Authorisation letter is not in correct format                                    | Re-upload Authorisation letter in correct format.                                                                                               |
  | Authorised person name mismatch with the provided KYC                                     | Re-upload the Authorisation letter with correct authorised person name.                                                                         |
  | Unauthorised person digital sign received on agreement                                    | Re-upload service agreement with Authorised person digital sign.                                                                                |
  | Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents | Re-upload correct document as per the Entity.                                                                                                   |
  | Authorized person signature mismatch with the provided KYC signature                      | Re-upload the Authorization letter with correct authorised person signature.                                                                    |
  | Mentioned director's name in authorization letter is not listed with MCA site             | Re-upload the authorization letter copy with registered director name and signature                                                             |
  | Uploaded Authorization letter is not clear                                                | Re-upload clear authrization letter copy                                                                                                        |
  | Date not mentioned in board resolution letter                                             | Re-upload board resolution letter with board resolution date                                                                                    |
  | <h3>PAN Card of Partnership Document</h3>                                                 |                                                                                                                                                 |
  | Mismatch in business name on agreement and PAN card                                       | Re-upload the PAN card copy with correct business Name or get the business name changed on your profile.                                        |
  | PAN Number not clear on the uploaded PAN card                                             | Re-upload the readable copy of PAN card                                                                                                         |
  | Company PAN card copy not upload                                                          | Upload copy of company PAN card.                                                                                                                |
  | PAN name mismatch with profile details                                                    | Re-upload correct PAN card or update your correct PAN name on your profile.                                                                     |
  | Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents | Re-upload correct document as per the Entity.                                                                                                   |
  | Uploaded PAN card is not clear                                                            | Re-upload the clear copy of PAN card                                                                                                            |
  | <h3>Government Issued Certificate Document</h3>                                           |                                                                                                                                                 |
  | Mismatch in business name on profile and govt. proof copy                                 | Re-upload govt. proof copy with correct legal name or get the business name changed on your profile as per your Govt. proof.                    |
  | Invalid govt proof, not verified by govt official                                         | Upload the valid govt. proof copy like GST , Udhyog aadhar, registration certificate etc. and same should be verified by govt. official.        |
  | Partnership deed is not verified by registrar                                             | Upload the partnership deed verified by registrar                                                                                               |
  | Society deed is not verified by registrar                                                 | Upload the society deed verified by registrar                                                                                                   |
  | Details on certificate of Incorporation mismatch with available details on MCA            | Upload the form 18 or 22 and certificate of incorporation.                                                                                      |
  | Certificate of Incorporation copy not uploaded                                            | Upload copy of certificate of Incorporation with sign and stamp                                                                                 |
  | 80G copy not received                                                                     | Re-upload signed and stamped copy of 80G                                                                                                        |
  | 12AA copy not received                                                                    | Re-upload signed and stamped copy of 12AA                                                                                                       |
  | Trust deed is not verified by registrar                                                   | Upload the Trust deed verified by registrar                                                                                                     |
  | govt. proof copy uploaded is expired                                                      | Re-upload a valid govt proof as uploaded proof is expired.                                                                                      |
  | Address written on Govt. proof mismatch with profile address                              | Update address details as per the attached govt. proof on your profile or reupload your govt. proof                                             |
  | Address not written on attached govt. proof                                               | Re-upload govt. proof with complete address visible.                                                                                            |
  | Incomplete govt. proof uploaded                                                           | Re-upload govt. proof with all pages.                                                                                                           |
  | Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents | Re-upload correct document as per your Business Entity.                                                                                         |
  | Govt proof copy not upload                                                                | Upload government proof copy.                                                                                                                   |
  | Mismatch in legal name on agreement and govt. proof copy                                  | Re-upload govt. proof copy with correct legal name                                                                                              |
  | <h3>Bank Account Proof Document</h3>                                                      |                                                                                                                                                 |
  | A/c no. not printed on uploaded bank proof                                                | Re-upload the bank proof with complete details like Account name/Account no. and IFSC code.                                                     |
  | Mismatch in bank account holder name on profile details and uploaded bank Proof           | Re-upload the Bank proof with bank a/c holder name completely visible or get your bank details changed on your profile as per your bank proof.  |
  | Mismatch in bank account IFSC code on profile and uploaded bank proof                     | Re-upload the Bank proof with IFSC code completely visible or get your bank details changed on your profile as per your bank proof.             |
  | Mismatch in bank account number on profile and uploaded bank proof                        | Re-upload the Bank proof with Bank a/c no. completely visible or get your bank details changed on your profile as per your bank proof.          |
  | Bank Proof copy not uploaded                                                              | Upload copy of bank account proof                                                                                                               |
  | Bank Signature and stamp are missing on Bank Verification letter                          | Re-upload the Bank Verification letter with Sign and stamp from bank                                                                            |
  | Bank Verification letter is not on Bank letter head                                       | Upload the bank verification letter on your Bank's letter head                                                                                  |
  | Bank Stamp missing on Passbook provided                                                   | Re-upload the verified copy of bank passbook                                                                                                    |
  | IFSC code not printed on uploaded bank proof                                              | Re-upload the bank proof with complete details like account name or account number and IFSC code.                                               |
  | Attached bank proof is not valid                                                          | Re-upload valid bank proof ( ex. Cancel cheque/passbook/BVL/bank statement ) with complete details like Account name/Account no. and IFSC code. |
  | Uploaded Bank proof copy is not readable/Clear                                            | Re-upload a readable or clear bank proof copy.                                                                                                  |
  | Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents | Re-upload correct document as per the Entity.                                                                                                   |
  | Account name not printed on uploaded bank proof                                           | Re-upload the bank proof with complete details like Account name/Account no. and IFSC code.                                                     |
  | <h3>Address Proof of Signing Authority Document</h3>                                      |                                                                                                                                                 |
  | Mismatch in Address on profile and uploaded address proof                                 | Please re-upload the proof of address or get your address changed in your profile details.                                                      |
  | Incomplete address proof uploaded                                                         | Please re-upload the complete copy of address proof                                                                                             |
  | Address proof copy not uploaded                                                           | Please upload the copy of address proof                                                                                                         |
  | Address proof copy uploaded is not clear                                                  | Please re-upload a readable copy of address proof with signature                                                                                |
  | Attached address proof is not valid                                                       | Re-upload valid address proof ( ex. Aadhar card/Voter Id/Passport/ DL etc. )                                                                   |
  | Incomplete address written on your profile                                                | Update address details as per the attached address proof on your profile.                                                                       |
  | Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents | Re-upload correct document as per the Entity.                                                                                                   |
  | <h3>PAN Card of Signing Authority Document</h3>                                           |                                                                                                                                                 |
  | Business name mismatch with attached PAN card                                             | Re-upload the correct PAN card or update correct business name on profile.                                                                      |
  | PAN card name mismatch with profile PAN name                                              | Re-upload the correct PAN card or update correct PAN name on profile.                                                                           |
  | PAN Number not clear on the uploaded PAN card                                             | Re-upload the readable copy of PAN card.                                                                                                        |
  | PAN card copy not upload                                                                  | Upload a copy of PAN card.                                                                                                                      |
  | Entity ( Individual/proprietor/Pvt ltd etc ) written mismatch with the provided documents | Re-upload the correct document as per the business Entity.                                                                                      |
  | Physically signed is missing on the uploaded PAN card                                     | Re-upload the copy of PAN card with physical signed.                                                                                            |
</Accordion>

Common issues include:

- Document quality problems
- Information mismatches
- Missing required fields
- Format incompatibility

## Flow Diagram

Here is a diagram for the high-level integration flow:


<Image src="https://files.readme.io/c8dadf9a8456cf38beec1f5464cb0e78a277fe681bcb9105c981521178b42526-Screenshot_2025-05-13_at_1.39.39_AM.png" align="center" />


<br />

## Security Best Practices

When integrating with PayU's APIs, follow these security best practices:

- Implement proper token management
- Use HTTPS for all communications
- Validate webhook signatures
- Securely store sensitive data
- Implement proper error handling

## Testing Recommendations

Testing is essential before moving to production. PayU provides a sandbox environment for testing purposes. Test key aspects including:

- Authentication flows
- Merchant creation and updates
- Document uploads
- Bank verification
- Error handling
- Webhook processing

<br />
