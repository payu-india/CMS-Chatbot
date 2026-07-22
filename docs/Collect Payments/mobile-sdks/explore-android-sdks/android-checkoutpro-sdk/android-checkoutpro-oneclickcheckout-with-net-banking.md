---
title: One-Click Checkout with Net Banking
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: One-Click Checkout with Net Banking
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: One-Click Net Banking - Android CheckoutPro
  description: >-
    One-click net banking with PayU CheckoutPro Android: ICICI and Axis biometric checkout without password OTP in the SDK payment flow.
  keywords:
    - payu one click checkout net banking android sdk integration
    - android checkoutpro net banking biometric integration payu
    - icici axis bank one click netbanking android payu sdk
    - payu checkout pro net banking without otp android integration
    - mobile net banking sdk android checkoutpro integration payu
    - payment gateway android one click net banking payu checkout
    - payu android sdk net banking fingerprint pin integration steps
    - android checkout pro netbanking registration flow payu sdk
    - payu one click net banking checkoutpro android india guide
    - integrate net banking android app checkout pro payu sdk
    - android native net banking payment sdk payu checkoutpro
    - net banking biometric authentication android sdk payu integration
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

<Image align="center" className="border" border={true} src="https://files.readme.io/7767f8f-Screenshot_2023-11-16_at_5.41.26_PM.png" />

#### Repeat flow

When the customer returns to make a repeat transaction and chooses the same bank under the net banking option, they don’t need to input their User ID and Password again. Instead, they can use their fingerprint or PIN to authenticate the transaction.

<Image align="center" className="border" border={true} src="https://files.readme.io/8a41557-Screenshot_2023-11-16_at_5.42.38_PM.png" />

## Integration Steps

### Integration in PayUCheckoutPro

No integration change is required to enable One Click Checkout in Checkout Pro SDK. But Merchants need to send the valid phone numbers of customers. If the customer’s phone number is registered with Bank the user will see biometric authentication for Payment.

### Integration in Custom Browser

To start One Click Checkout for NB, the merchant needs to set the following parameters in the `CustomBroswerConfig` object while initializing CB SDK:

```java Java
CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey, txnId);
customBrowserConfig.setMerchantKey( <Merchant Name>);
customBrowserConfig.setUserCredential(<unique user id>);
customBrowserConfig.setFirstName( <Customer First Name>);
customBrowserConfig.setLastName(Customer Last Name>);
customBrowserConfig.setPhoneNumber(<Mobile number>);
customBrowserConfig.setMerchantKey(<Merchant Key>);
customBrowserConfig.setOneClickPayBankCodes({"ICIB","AXIB"});
customBrowserConfig.setEmail( <Customer Email Id>)
```
```kotlin Kotlin
val customBrowserConfig = CustomBrowserConfig(merchantKey, txnId)
customBrowserConfig.merchantName = <Merchant Name>
customBrowserConfig.userCredential = <unique user id>
customBrowserConfig.firstName = <Customer First Name>
customBrowserConfig.lastName = <Customer Last Name>
customBrowserConfig.phoneNumber = <Mobile number>
customBrowserConfig.merchantKey = <Merchant Key>
customBrowserConfig.setOneClickPayBankCodes({"ICIB","AXIB"});
customBrowserConfig.email = <Customer Email Id>
```