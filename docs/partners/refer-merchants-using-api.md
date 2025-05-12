---
title: Refer merchants using APIs
excerpt: ''
deprecated: false
hidden: false
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

* Onboard merchants to the PayU platform
* Manage merchant KYC processes
* Verify bank account details
* Handle electronic signatures for agreements
* Receive real-time status updates via webhooks

\<Accordion title="Token Management Flow" icon="fa-info-circle">
&#x20; The token-based authentication works as follows:

&#x20; \* Partners obtain an access token using their credentials
&#x20; \* This token is included in subsequent API requests
&#x20; \* Tokens expire after a set period and must be refreshed

&#x20; \> \*\*Important\*\*: Access tokens should be securely stored and never exposed in client-side code.
\</Accordion>

\<Tabs>
&#x20; \<Tab title="Authentication and Authorization">
&#x20;   \## Authentication and Authorization

PayU Merchant Onboarding employs token-based authentication with OAuth 2.0 standards. Partners must obtain tokens through appropriate authentication endpoints before accessing the API resources.

\### Token Management Flow

The token-based authentication works as follows:

\* Partners obtain an access token using their credentials
\* This token is included in subsequent API requests
\* Tokens expire after a set period and must be refreshed

\> \*\*Important\*\*: Access tokens should be securely stored and never exposed in client-side code.

\### User Token APIs

The Merchant Onboarding Integration offers several token-related endpoints for authentication purposes. These endpoints handle token generation, refresh, and OTP verification when required.

For detailed request and response specifications, please refer to:

\* \[Partner Integration User Token APIs]\(https\://docs.payu.in/reference/partner-integration-user-token-apis#/)
\* \[Get Token API]\(https\://docs.payu.in/reference/get\_token\_api#/)
\* \[Refresh Token API]\(https\://docs.payu.in/reference/refresh\_token\_api#/).
&#x20; \</Tab>

&#x20; \<Tab title="Second Tab">
&#x20;   Here's content that's only inside the second Tab.
&#x20; \</Tab>

&#x20; \<Tab title="Third Tab">
&#x20;   Here's content that's only inside the third Tab.
&#x20; \</Tab>
\</Tabs>

## Authentication and Authorization

PayU Merchant Onboarding employs token-based authentication with OAuth 2.0 standards. Partners must obtain tokens through appropriate authentication endpoints before accessing the API resources.

### Token Management Flow

The token-based authentication works as follows:

* Partners obtain an access token using their credentials
* This token is included in subsequent API requests
* Tokens expire after a set period and must be refreshed

> **Important**: Access tokens should be securely stored and never exposed in client-side code.

### User Token APIs

The Merchant Onboarding Integration offers several token-related endpoints for authentication purposes. These endpoints handle token generation, refresh, and OTP verification when required.

For detailed request and response specifications, please refer to:

* [Partner Integration User Token APIs](https://docs.payu.in/reference/partner-integration-user-token-apis#/)
* [Get Token API](https://docs.payu.in/reference/get_token_api#/)
* [Refresh Token API](https://docs.payu.in/reference/refresh_token_api#/)

## Merchant Onboarding Process

The Merchant Onboarding flow consists of several key steps:

1. Create a merchant record with basic details
2. Update additional merchant information as needed
3. Add and verify bank account details
4. Upload the required KYC documents
5. Complete e-signature process for merchant agreement
6. Monitor merchant status through webhooks

### Creating and Managing Merchants

The APIs for merchant creation and management allow partners to register new merchants and update their information.

For detailed specifications on merchant onboarding, please refer to:

* [Create Merchant API](https://docs.payu.in/reference/create_merchant_api#/)
* [Update Merchant Details API](https://docs.payu.in/reference/update_merchant_details_api#/)
* [Get Merchant API](https://docs.payu.in/reference/get_merchant_api#/)

### Bank Account Verification

Bank account verification is a critical step in the merchant onboarding process. PayU provides specific APIs for adding, updating, and verifying bank details.

For specifications on bank verification, please refer to:

* [Bank Details API](https://docs.payu.in/reference/bank-details-api#/)
* [Add Update Bank Details API](https://docs.payu.in/reference/add_update_bank_details_api#/)
* [Penny Verify API](https://docs.payu.in/reference/penny_verify_api#/)
* [Verify and Link Merchant API](https://docs.payu.in/reference/verify_and_link_merchant_api#/)

## KYC Document Management

The KYC process requires merchants to provide various identification and business documents. These APIs facilitate document upload and verification.

### Document Requirements

Different merchant types require different documentation. The exact requirements should be determined by referencing the official PayU documentation.

### Document Upload APIs

For specifications on KYC document management, please refer to:

* [Manage KYC Documents](https://docs.payu.in/reference/manage-kyc-documents#/)
* [Docs Required API](https://docs.payu.in/reference/docs_required_api#/)
* [Create KYC Document API](https://docs.payu.in/reference/create_kyc_document_api#/)

### Document Types and Guidelines

PayU accepts various document types for KYC verification, including:

* Identity proofs (PAN Card, Aadhaar, etc.)
* Address proofs
* Business registration documents
* Bank account proofs

Documents must meet specific format and quality requirements to be accepted.

## E-Sign Flow

The electronic signature process is required to complete merchant agreements. PayU provides specific APIs to manage this workflow.

For e-signature specifications, please refer to:

* [E-Sign Flow APIs](https://docs.payu.in/reference/e-sign-flow-apis#/)
* [Generate Merchant Agreement for E-Sign API](https://docs.payu.in/reference/generate-merchant-agreement-for-e-sign-api#/)
* [Send OTP to Signatory Email API](https://docs.payu.in/reference/send-otp-to-signatory-email-api#/)
* [E-Sign Merchant Agreement API](https://docs.payu.in/reference/e-sign-merchant-agreement-api#/)

## Webhooks for Real-Time Updates

Webhooks allow partners to receive notifications about changes in merchant status without polling the API.

For webhook integration details, please refer to:

* [Using Webhooks for Merchant Status](https://docs.payu.in/reference/using-webhooks-for-merchant-status#/)
* [Register Webhooks API](https://docs.payu.in/reference/register-webhooks-api-to-get-real-time-merchant-status#/)
* [Get Real-Time Merchant Status Using Webhooks](https://docs.payu.in/reference/get-real-time-merchant-status-using-webhooks#/)

### Security Considerations for Webhooks

Webhook requests should be authenticated to ensure they come from PayU. Implementation details can be found in the webhook documentation.

## Error Handling and Troubleshooting

### Common KYC Errors and Solutions

KYC document verification can encounter various issues. For detailed information on common errors and their solutions, please refer to:

* [KYC Errors and Solutions](https://docs.payu.in/reference/kyc-errors-and-solutions#/)

Common issues include:

* Document quality problems
* Information mismatches
* Missing required fields
* Format incompatibility

## Flow Diagram

Here is a diagram for the high-level integration flow:

<Image align="center" src="https://files.readme.io/c8dadf9a8456cf38beec1f5464cb0e78a277fe681bcb9105c981521178b42526-Screenshot_2025-05-13_at_1.39.39_AM.png" />

<br />

## Security Best Practices

When integrating with PayU's APIs, follow these security best practices:

* Implement proper token management
* Use HTTPS for all communications
* Validate webhook signatures
* Securely store sensitive data
* Implement proper error handling

## Testing Recommendations

Testing is essential before moving to production. PayU provides a sandbox environment for testing purposes. Test key aspects including:

* Authentication flows
* Merchant creation and updates
* Document uploads
* Bank verification
* Error handling
* Webhook processing