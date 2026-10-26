---
title: Cards Authentication Suite
deprecated: false
hidden: false
metadata:
  robots: index
---
PayU's Cards Authentication Suite helps you offer faster, more secure card payments by reducing your customers' reliance on one-time passwords (OTPs). OTPs can be delayed, mistyped or shared, which leads to checkout drop-offs and fraud. The suite replaces the OTP step with authentication your customers already use every day: fingerprint, Face ID or device PIN.

The suite includes two solutions:

- [**Visa Payment Passkey**](#visa-payment-passkey)**:** customers confirm Visa card payments with a passkey stored on their device, built on the FIDO2 standard. PayU handles the passkey flow during card authentication.
- [**FlashPay**](#flashpay)**:** customers confirm card payments with biometrics directly inside your mobile app, through the PayU 3DS SDK.

Both solutions work on top of 3DS 2.0 and fall back automatically to the standard OTP flow if biometric authentication can't be completed, so your customers can always finish their payment.

## Which solution is right for you?

|                         | Visa Payment Passkey                                                                | FlashPay                                                                                          |
| ----------------------- | ----------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Best for**            | Merchants who want OTP-free Visa card authentication without building anything new  | Merchants with a mobile app who want in-app biometric card authentication                         |
| **Customer experience** | Confirms the payment with fingerprint, Face ID or device PIN using a device passkey | Confirms the payment with fingerprint or Face ID inside your app, with no redirect to a bank page |
| **Channel**             | Wherever PayU handles card authentication                                           | Mobile app only (Android and iOS)                                                                 |
| **Integration**         | No extra integration work; PayU handles the flow                                    | PayU 3DS SDK, in a coupled or decoupled flow                                                      |
| **Cards covered**       | India-issued Visa cards from supported issuing banks                                | Cards (BINs) enabled by issuing banks, across major card networks; check with the BIN Info API    |
| **First-time setup**    | One-time OTP verification, then passkey creation                                    | One-time OTP verification, then consent and biometric registration                                |
| **Fallback**            | Automatic switch to the standard OTP flow                                           | Automatic switch to OTP authentication                                                            |
| **How to enable**       | Contact [PayU Support](https://help.payu.in)                                        | Contact [PayU Support](https://help.payu.in)                                                      |

***

## Visa Payment Passkey

Visa Payment Passkey lets your customers authenticate Visa card payments with the same method they use to unlock their phone or laptop: fingerprint, Face ID or device PIN. They don't need to enter a one-time password (OTP) on the bank's page.

Visa Payment Passkey is built on the FIDO2 industry standard. The passkey stays on the customer's device and can't be shared or phished the way an OTP can. This makes checkout faster and more secure.

### How it works

Visa Payment Passkey has two parts:

**1. Setting up the passkey (first payment)**

- The customer pays with an eligible Visa card as usual.
- They complete the standard OTP verification once.
- They're then asked to create a passkey on their device using fingerprint, Face ID or device PIN.

**2. Paying with the passkey (later payments)**

- When the customer pays with the same card on the same device, they're asked to confirm the payment with biometrics or device PIN.
- Authentication takes a few seconds and doesn't need an OTP.

### Benefits

**For your customers**

- **Faster checkout:** they don't wait for an OTP, switch apps or type a code.
- **Familiar experience:** it works the same way as unlocking their device.
- **Better security:** the passkey is tied to their device and can't be shared or intercepted.

**For you**

- **Less checkout friction:** fewer steps at authentication, so fewer drop-offs from OTP delays or failures.
- **Lower fraud risk:** authentication can't be phished, which reduces fraud from shared or stolen OTPs.
- **No extra integration work:** PayU handles the passkey flow during card authentication.

### Eligibility

Visa Payment Passkey is available when:

- The customer pays with an **India-issued Visa card** from a **supported issuing bank**.
- Your account is enabled for **3DS 2.0 card authentication** through PayU.
- Your account is processed through an **acquiring bank that supports Visa Payment Passkey**.

Other cards continue to use the standard 3DS/OTP flow.

### Fallback

If passkey authentication can't be completed, the payment automatically switches to the standard OTP flow. This covers cases such as an unsupported device, the customer cancelling, or a technical error. The customer can still finish the payment, and you don't need to do anything.

### How to enable

To enable Visa Payment Passkey for your account, contact [PayU Support](https://help.payu.in). The team will check whether your account is eligible and turn on the feature.

***

## FlashPay

FlashPay lets your customers authenticate card payments with device biometrics, such as fingerprint or Face ID, directly inside your mobile app. They don't need to enter an OTP or leave your app for a bank page.

FlashPay is delivered as a PayU SDK that works on the existing 3DS 2.0 protocol. It meets RBI guidelines for multi-factor authentication (MFA) for card payments, and uses biometric-based out-of-band (OOB) authentication to verify the customer.

### How it works

FlashPay has two parts:

**1. Registration (first payment)**

- The customer selects an eligible card at checkout.
- They complete the standard OTP verification for the payment.
- They give consent to set up biometric authentication by selecting **Set up your Face ID or Fingerprint for quick and secure payments**.
- Their biometric credential is registered, their mobile number is verified, and FlashPay registration is complete.

**2. Authentication (later payments)**

- The customer selects their registered card at checkout.
- They confirm the payment with fingerprint or Face ID inside your app.
- The payment is completed, and you receive the authentication status through SDK callbacks and webhooks.

### Benefits

- **Faster payments:** split-second biometric card payments with up to 4x lower authentication latency.
- **Higher success rates:** 1.5–2% higher authentication success rates compared to traditional methods.
- **In-app experience:** authentication happens entirely within your app, with no redirect to a bank page.
- **Stronger security:** registered devices and cards are monitored on an ongoing basis.
- **Automatic fallback:** if biometric authentication isn't available or fails, the payment switches to OTP authentication.
- **Minimal integration:** it works on your existing 3DS 2.0 setup with minimal changes.

### Supported cards and checkout types

FlashPay works with all major card networks and supports:

- Guest checkout
- Saved cards
- Alternative IDs
- Network tokens and issuer tokens
- Tokenized cards

### Eligibility

**Card eligibility**

Issuing banks decide which cards (BINs) are eligible for FlashPay. Use the **BIN Info API** to check whether a card is eligible in real time.

- Call the API every time a customer enters or selects card details.
- Use the response to decide whether to show FlashPay or standard OTP in your checkout.
- Newly onboarded banks are added automatically, so you don't need to make changes when more banks go live.

**Device support**

| Platform | Version        | Devices                                  |
| -------- | -------------- | ---------------------------------------- |
| Android  | 6.0 and above  | Smartphones only (tablets not supported) |
| iOS      | 12.0 and above | iPhones only (iPads not supported)       |

The device must support fingerprint or Face ID.

### Integration options

FlashPay is available through the PayU 3DS SDK in two models:

- **Coupled flow:** PayU handles the full payment, from authentication to authorization, with built-in authentication handling.
- **Decoupled flow:** you collect device details, handle authentication requests and control the UI, then authorize the payment separately.

If you integrate through a payment aggregator, you also need these APIs:

| API              | Purpose                                                       |
| ---------------- | ------------------------------------------------------------- |
| Get BIN Info API | Check whether a card is eligible for FlashPay                 |
| Payment API      | Start the authentication request                              |
| AuthN Callback   | Receive the authentication status through a webhook           |
| AuthN Data API   | Get detailed authentication results                           |
| AuthZ API        | Authorize (debit) the payment after successful authentication |

<Callout icon="far fa-circle-info" theme="info">
  ### Notes:

  - **Customer consent is required:** biometric registration happens only after OTP validation and with the customer's explicit consent.
  - **Store the registration status:** save each customer's FlashPay registration status in your customer records.
  - **Automatic de-registration:** if the device's biometrics change or the SIM moves, the card is de-registered automatically. The customer will need to register again.


</Callout>

### How to enable

To enable FlashPay for your account, contact [PayU Support](https://help.payu.in). The team will check whether your account is eligible and turn on the feature. For implementation steps, see the FlashPay SDK integration guides for Android and iOS.
