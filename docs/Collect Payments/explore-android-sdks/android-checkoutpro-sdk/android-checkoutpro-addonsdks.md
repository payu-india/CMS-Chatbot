---
title: Add-on SDKs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: android-checkoutpro-custom-integrations
      title: Customise Your Integration
---
# Olamoney SDK

To integrate with Ola money SDK, the merchant can add the below gradle dependency in their app’s build.gradle file

```Text Text
implementation 'in.payu:olamoney:1.3.14'
```

On integrating, the merchant will see the native screen for entering a mobile number, verify if it is enabled for Olamoney, and do the transaction.

Refer to [Ola Money SDK ](doc:ola-money-sdk) doc for more details

# Google Pay InApp

To integrate with Google Pay InApp flow, the merchant can add the below gradle dependency in their app’s build.gradle file.

> 📘 Onboarding Requirements:
>
> To start transacting through Google Pay™, register your business on Google using the [Google Onboarding](https://pay.google.com/about/business/) form, In this registration process, you need to add the merchant VPAs created by PayU for you. In the case of multiple VPAs, all of them need to be registered with Google.
> To enable Google Pay, contact your Point of Contact at Google.
>
> For any further queries or help with onboarding, send a mail to PayU Mobile Integration Team.

```Text build.gradle
implementation 'in.payu:payu-gpay:4.0.2'
```

The merchant needs to pass Google Pay as described in [Additional payment options in the Checkout screen](doc:android-checkoutpro-custom-integrations).

> ❗️ Callout
>
> The Gpay InApp flow is not available in the Test mode.

For GPay SDK integration, refer to [Android Google Pay SDK](doc:android-google-pay-sdk).

# PhonePe InApp

To integrate with PhonePe InApp flow, the merchant can add the below gradle dependency in their root project’s build.gradle file.

```Text Text
maven { url "https://phonepe.mycloudrepo.io/public/repositories/phonepe-intentsdk-android" }
```

and add the below dependency to the app's build.gradle file

```Text Text
implementation 'in.payu:phonepe-intent:1.8.9'
```

The merchant needs to pass PhonePe. For more information, refer to [Additional payment options in the Checkout screen](doc:android-checkoutpro-custom-integrations#additional-payment-options-in-the-checkout-screen).

> ❗️ Callout
>
> The PhonePe InApp flow is not available in the Test mode.

Refer to [PhonePe SDK](doc:android-phonepe-sdk) doc for more details

# Native OTP Assist

To integrate this, please enable the`txn_s2s_flow` flag on your merchant key from your Key Account Manager at PayU and add the below dependency to apps`build.gradle` file.

To see the Native OTP Assist experience, refer to [Android Native OTP SDK](doc:native-otp-assist-sdk).

```Text Text
implementation 'in.payu:native-otp-assist:1.6.5'
```

> ❗️ Callout
>
> The Native OTP flow is not available in the Test mode

Refer to [Android Native OTP SDK ](doc:native-otp-assist-sdk) doc for more details
