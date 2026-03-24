---
title: One-click checkout with Net Banking
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
PayU offers Net banking transactions using biometrics without the need of a username/user ID, password, and OTP. Currently available for ICICI and Axis Bank in PayUCheckoutPro and Custom Browser SDK.

## Customer Journey

#### Registration flow

1. From the list of net banking options, the user chooses ICICI or Axis Bank.
2. As soon as the customer is redirected to the bank login page, SDK verifies the customer’s mobile number with the bank. If user’s phone number is registered with the bank, the registration flow will trigger after user validation.
3. Customers will see the OTP screen on SDK for the first time and after OTP verification they will be prompted to set a pin to authenticate for their subsequent transactions. If their device allows biometric authentication, they can set up their fingerprint.
4. In the repeat transaction, the user may authenticate using a pin or fingerprint (depending on the device’s capabilities).

<Image align="center" src="https://files.readme.io/7767f8f-Screenshot_2023-11-16_at_5.41.26_PM.png" />

#### Repeat flow

When the customer returns to make a repeat transaction and chooses the same bank under the net banking option, they don’t need to input their User ID and Password again. Instead, they can use their fingerprint or PIN to authenticate the transaction.

<Image align="center" src="https://files.readme.io/8a41557-Screenshot_2023-11-16_at_5.42.38_PM.png" />

## Integration Steps

### Integration in PayUCheckoutPro

No integration change is required to enable One Click Checkout in Checkout Pro SDK. But Merchants need to send the valid phone numbers of customers. If the customer’s phone number is registered with Bank the user will see biometric authentication for Payment.
