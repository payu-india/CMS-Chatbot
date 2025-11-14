---
title: 'FlashPay Android SDK '
deprecated: false
hidden: false
metadata:
  robots: index
---
## What is FlashPay?

FlashPay is PayU's advanced payment solution that allows your customers to authenticate card transactions using their device biometrics (fingerprint, face recognition, or voice recognition) instead of entering OTPs. This means faster, more secure payments without customers leaving your mobile app.

**Key Features:**

* **Biometric Authentication**: Uses fingerprint, face ID, or voice recognition
* **RBI Compliant**: Meets all Reserve Bank of India guidelines for multi-factor authentication (MFA)
* **3DS Compatible**: Works with existing 3D Secure payment infrastructure
* **SDK-Based**: Single software development kit handles everything
* **End-to-End Security**: Complete authentication management from start to finish

## Why Should You Integrate FlashPay?

FlashPay delivers significant benefits for both you as a merchant and your customers:

### **For Your Business:**

1. **4x Faster Payments**: Transactions complete in seconds instead of minutes
2. **Higher Success Rates**: 1.5% to 2% improvement in successful payment completions
3. **Better Customer Experience**: No app switching or OTP delays
4. **Reduced Cart Abandonment**: Smoother checkout process
5. **Easy Implementation**: Minimal changes to your existing payment flow

### **For Your Customers:**

1. **Quick & Convenient**: Pay with just a fingerprint or face scan
2. **Enhanced Security**: Continuous monitoring and advanced fraud protection
3. **Reliable Backup**: Automatic fallback to OTP if biometrics fail
4. **Universal Support**: Works with all major card networks and bank types

### **Technical Benefits:**

1. **Broad Compatibility**: Supports all card types including guest checkout, saved cards, network tokens, and issuer tokens
2. **Pre-integrated Networks**: All major card networks are already supported
3. **Existing Infrastructure**: Uses your current 3D Secure setup

## Getting Started with FlashPay SDK

To integrate FlashPay, you'll receive detailed technical documentation covering step-by-step integration, callback functions, and communication protocols.

**Reference Document**: _"FlashPay_3DS SDK"_ (available in Annexure SDK Integration Guide)

### Device Compatibility

**Android Devices:**

* **Minimum Version**: Android 6.0 (API level 23) and above
* **Supported Devices**: Smartphones only
* **Not Supported**: Android tablets

**iOS Devices:**

* **Minimum Version**: iOS 12 and above
* **Supported Devices**: iPhones only
* **Not Supported**: iPads

**Why These Requirements?**
These versions ensure proper biometric sensor support and security features necessary for safe payment authentication.

## Which Customers Can Use FlashPay?

Not all bank cards support FlashPay yet. Banks that have partnered with PayU for FlashPay provide a list of eligible card numbers (called BIN ranges). You can check in real-time whether a customer's card supports FlashPay using our API.

### Bank Card Verification API

**What it does**: Checks if a specific bank card supports FlashPay biometric authentication

**API Name**: "Get BIN Info API"

**When to use**: Every time a customer enters card details or selects a saved card

**What you get**: Real-time eligibility status for FlashPay enrollment

**Reference Document**: Complete API specifications available in API Integration Guide

### Important Implementation Notes

1. **User Experience Management**: Use the API response to show or hide FlashPay options in your app
2. **Universal Checking**: Works for both new card entries (guest checkout) and previously saved cards
3. **Real-Time Updates**: Always check eligibility for each transaction to get the latest bank partnerships
4. **Automatic Updates**: As new banks join FlashPay, their card ranges are automatically included
5. **Performance**: The API is designed for quick responses to avoid payment delays

## How Customers Register for FlashPay

This section explains how customers can enroll their eligible bank cards for biometric payments during a regular transaction.

### User Experience Flow

**Step-by-Step Customer Journey:**

1. **Card Selection**: Customer chooses an eligible card for payment
2. **Standard Authentication**: Customer enters OTP for current transaction as usual
3. **Enrollment Offer**: System offers option to enroll for biometric payments
4. **Biometric Setup**: FlashPay SDK guides customer through biometric enrollment
5. **Mobile Verification**: System verifies customer's mobile number
6. **Biometric Capture**: Customer's fingerprint/face/voice is securely registered
7. **Enrollment Complete**: Registration successful, transaction continues normally
8. **Transaction Completion**: Current payment is processed successfully

### Technical Workflow

<br />

### Implementation Guidelines

**Registration Scenarios:**

1. **Guest Checkout**: When customers manually enter card details
2. **Saved Cards**: When customers use previously tokenized cards

**Your Integration Steps:**

1. **Continue Normal Flow**: Start card payments exactly as you do now
2. **Use 3DS SDK**: Collect device information as per current process
3. **Call Payment APIs**: Invoke your payment aggregator APIs as usual
4. **Handle Bank Response**: Bank will indicate if FlashPay enrollment is possible
5. **SDK Integration**: FlashPay SDK handles the biometric enrollment process

**Key Benefits for Implementation:**

* Minimal changes to your existing payment flow
* Automatic handling of complex biometric processes
* Seamless integration with current 3DS infrastructure

## How FlashPay Works for Transactions

This explains how customers who have enrolled for FlashPay can complete payments using biometrics without leaving your app.

### User Experience Flow

**Step-by-Step Payment Process:**

1. **Card Selection**: Customer selects a FlashPay-enrolled card
2. **Information Display**: App shows that this card is enrolled for biometric payments
3. **Authentication Screen**: Biometric authentication interface appears with backup options
4. **Biometric Verification**: Customer provides fingerprint, face scan, or voice authentication
5. **Transaction Success**: Payment completes instantly without OTP or redirections

### Technical Workflow

### Implementation Guidelines

**Supported Payment Types:**

1. **Guest Checkout**: First-time card entries with FlashPay enrollment
2. **Saved Cards**: Previously enrolled cards stored in your system

**Integration Requirements:**

1. **Standard SDK Calls**: Use the same 3DS SDK calls as your current implementation
2. **API Integration**: Standard payment aggregator API calls
3. **Fallback Handling**: Automatic switching to OTP if biometric authentication fails

**Customer Benefits:**

* No app switching or browser redirections
* Instant payment completion
* Secure biometric authentication
* Reliable backup to OTP when needed

<br />
