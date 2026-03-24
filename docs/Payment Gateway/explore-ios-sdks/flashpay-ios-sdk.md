---
title: Flashpay iOS SDK
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU's FlashPay SDK solution provides a robust biometric authentication solution for card transactions. FlashPay is a secure and efficient SDK that facilitates device biometric authentication for card transactions while being compliant with RBI guidelines for multi-factor authentication (MFA). The solution operates on existing 3DS protocols and includes advanced biometric-based out-of-band authentication (OOB).

This section outlines the technical specifications and integration requirements for implementing the PayU FlashPay SDK into merchant mobile applications. The document covers the following key integration touchpoints:

* Customer eligibility for FlashPay
* Customer registration flow
* Transaction authentication flow

The scenarios outlined are designed to work seamlessly with PayU or other Payment Aggregators (PA).

## Benefits

FlashPay offers significant advantages for both merchants and customers:

1. **Enhanced Performance**: Split-second biometric card payments with 4x reduced transaction latency
2. **Improved Success Rates**: 1.5-2% higher authentication success rates compared to traditional methods
3. **Enhanced Security**: Continuous monitoring and lifecycle management for secure transactions
4. **Seamless Fallback**: Automatic fallback to OTP-based authentication in case of biometric failures
5. **Minimal Integration**: Operates on existing 3DS infrastructure with minimal changes required
6. **Universal Support**: Compatible with all major card networks and supports various card types including:
   * Guest checkout
   * Alternative IDs
   * Network tokens
   * Issuer tokens
   * Tokenized cards

## SDK Integration

To integrate the FlashPay SDK into your mobile application, refer to the comprehensive integration documentation titled **"FlashPay_3DS SDK"** which contains detailed implementation steps, callback mechanisms, and communication protocols.

* Supported Operating Systems

| Platform | Version        | Device Support                           |
| -------- | -------------- | ---------------------------------------- |
| Android  | 6.0 and above  | Smartphones only (tablets not supported) |
| iOS      | 12.0 and above | iPhones only (iPads not supported)       |

* Customer Eligibility for FlashPay

Issuing banks provide a list of Bank Identification Numbers (BINs) that are eligible for the FlashPay Biometric MFA Solution. Merchants can use the BIN Info API to verify card eligibility in real-time.

### Key Pointers for Consideration

1. **Real-time Management**: Merchants can dynamically manage customer UX based on API responses
2. **Universal Application**: Can be used for both guest checkout scenarios and saved card transactions
3. **Mandatory Invocation**: API must be called every time card details are entered or selected
4. **Scalable Configuration**: System is configurable to automatically include BIN data for newly onboarded banks

## Customer Journey

This section details the step-by-step process for registering a customer's card for FlashPay biometric authentication during an inline transaction.

### Registration Workflow

The technical Implementation steps involves:

1. Checkout page is displayed with payment modes

<Image align="center" border={true} width="250px" src="https://files.readme.io/1ecd2143e141c7f95dc6af8af4917ec539f75c5cb2eda5101080c353753afe00-Flashpay_SDK_registration_flow_checkout_page.png" className="border" />

2. Customer selects eligible card for authentication.

<Image align="center" border={true} width="250px" src="https://files.readme.io/9a195225492306df95631d21b8db1b0fda12caba0d5dfb140344e213553bc45f-Flashpay_SDK_registration_flow_eligible_card_selection.png" className="border" />

3. Enters OTP for transaction authentication & opts to enroll for biometric authentication. Customer must select the **Set up your Face ID or Fingerprint for quick and secure payments** check box.

<Image align="center" border={true} width="250px" src="https://files.readme.io/dc14398d54d33890cde207fabccaa07f7ac400caf73508d00c18cc6a7120f4fb-Flashpay_SDK_registration_flow_otp-input.png" className="border" />

<Callout icon="📘" theme="info">
  **Note**: If the customer has not selected the **Set up your Face ID or Fingerprint for quick and secure payments** check box,  FlashPay SDK initiates biometric enrollment:

  <Image align="center" border={false} width="250px" src="https://files.readme.io/955ec58c28e9428b15f1acd6a8eb0b8bc1011df6ad6a910b635b8a35485e0a34-Flashpay_SDK_registraction_flow_biometric.png" />
</Callout>

5. Biometric credential is registered

<Image align="center" border={true} width="250px" src="https://files.readme.io/cb10d627d74c852966eb74f9d110a290c0013e4711eac08994b6c39e9aca7aef-Flashpay_SDK_registraction_flow_faceid.png" className="border" />

6. Mobile verification is done

<Image align="center" border={true} width="250px" src="https://files.readme.io/7023dd572c886b5280cb4bde0e23d65bb55df2656d5ecdab96827ae9e93ce66e-Flashpay_SDK_registration_flow_device_setting_up.png" className="border" />

7. FlashPay registration is complete

<Image align="center" border={true} width="250px" src="https://files.readme.io/afde344f38ca6e0ef3cbefdc4201b95335c84ee044948a57d2f292ee0369d072-Flashpay_SDK_registration_flow_device_success.png" className="border" />

### Key Registration Considerations

1. **Universal Application**: Registration process applies to both guest checkout and saved card scenarios
2. **Consent-Based Enrollment**: Biometric enrollment occurs post-OTP validation with explicit customer consent
3. **Status Management**: Enrollment status must be stored and managed by merchant in customer records
4. **Seamless Integration**: Process integrates seamlessly with existing transaction workflows

### Transaction Authentication Workflow

Customers who have successfully registered their cards with FlashPay can authenticate subsequent transactions using biometric authentication directly within the merchant application.

The technical implementation steps involves:

1. Customer selects enrolled card for authentication.

<Image align="center" border={true} width="250px" src="https://files.readme.io/9a195225492306df95631d21b8db1b0fda12caba0d5dfb140344e213553bc45f-Flashpay_SDK_registration_flow_eligible_card_selection.png" className="border" />

2. Authentication screen with auto-fallback capability

<Image align="center" border={true} width="250px" src="https://files.readme.io/f70f570575b4fccce24a8d3ab58c642d7ea98def1979668d63b35395c7475250-Flashpay_SDK_registration_flow_educate_about_biometrtic.png" className="border" />

3. Customer validation & biometric capture

<Image align="center" border={true} width="250px" src="https://files.readme.io/cb10d627d74c852966eb74f9d110a290c0013e4711eac08994b6c39e9aca7aef-Flashpay_SDK_registraction_flow_faceid.png" className="border" />

4. Transaction is complete.

<Image align="center" border={true} width="250px" src="https://files.readme.io/5c44d95ed40b62fd80467b939341bc1531f1311dc2ee5a99968c58d20f326aad-Flashpay_SDK_registration_flow_transaction_success.png" className="border" />

### Key Authentication Considerations

1. **Comprehensive Support**: Supports both guest checkout and saved card scenarios
2. **Robust Fallback**: Automatic fallback to OTP authentication when biometric validation is unavailable
3. **Multiple Communication Channels**: Validation statuses available via both SDK callbacks and webhooks
4. **Seamless Experience**: Authentication occurs entirely within merchant application environment

## Related Flows and APIs

### Merchant Integration with FlashPay SDK

For detailed SDK integration guidelines, implementation steps, callback configurations, and communication protocols, refer to [FlashPay Coupled Flow iOS 3DS 2.0 SDK Integration](doc:3ds-20-flashpay-coupled-flow-ios-integration).

### Merchant Integration with Payment Aggregator APIs

The following APIs are required for complete Payment Aggregator integration:

1. **Get BIN Info API**: Fetch BIN eligibility status for FlashPay authentication
2. **Payment API**: Initiate authentication request with payment aggregator
3. **AuthN Callback**: Receive authentication status via webhook mechanism
4. **AuthN Data API**: Retrieve detailed authentication results from payment aggregator
5. **AuthZ API**: Process customer account debit following successful authentication

This part of the document contains detailed API specifications, request/response formats, error handling procedures, and integration examples for seamless payment aggregator connectivity.

***

**Document Information**:

* **Title**: PayU FlashPay Product Specification Document
* **Version**: 1.2
* **Focus**: Technical specifications for FlashPay SDK integration
* **Scope**: Customer eligibility, registration flows, and transaction authentication processes
* **Compliance**: RBI guidelines for Multi-Factor Authentication (MFA)
* **Protocol**: 3D Secure (3DS) with biometric-based out-of-band authentication

### BIN Info API

**API Name**: Get BIN Info API

This API provides access to the latest BIN data authorized by participating banks for FlashPay authentication. The API delivers real-time responses to help merchants manage customer user experience effectively.

**Key Features**:

* Real-time BIN eligibility verification
* Support for both guest checkout and saved cards
* Dynamic updates as new issuing banks are onboarded
* Configurable to include additional BIN data
