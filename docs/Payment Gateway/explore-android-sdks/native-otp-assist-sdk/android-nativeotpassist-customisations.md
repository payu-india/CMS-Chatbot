---
title: Customise your Integration
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
The Native OTP Assist SDK provides several customization options allowing you to make the SDK closer to the look & feel of your app and work as per your business requirements.

## Update merchant logo

You can display your brand logo in the PayU Native OTP Assist SDK to reinforce trust and branding. To set a logo in the SDK, you need to pass the drawable ID of the logo image resource from your app.

```Text Kotlin
val payUOtpAssistConfig = PayUOtpAssistConfig() 
payUOtpAssistConfig.merchantLogo = R.drawable.merchant_logo 
```
```Text JAVA
PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig(); 
payUOtpAssistConfig.setMerchantLogo(R.drawable.merchant_logo); 
```

## Change theme colour

Our SDK allows you to change the theme color, and you need to set this primary color in your color file.

```Text XML
<color name="payu_otp_assist_primary_color">#fd416d</color>
```

## Change waiting for OTP timeout

PayU will wait for a specified time for the OTP, after which the SDK falls back to the manual OTP screen. The default time is 30 seconds; you may change it to any other duration. PayU recommends you configure the timeout to less than 60 seconds for a better user experience.

```Text JAVA
PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig(); 
payUOtpAssistConfig.setWaitingTime(45000); 
```
```Text Kotlin
val payUOtpAssistConfig = PayUOtpAssistConfig() 
payUOtpAssistConfig.waitingTime = 45000 
```

## Disable Auto-Submit OTP flag

Merchants can enable/disable the auto-submit OTP flow using the following flag. The default value is set to true.

```Text Node
PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig();
payUOtpAssistConfig.setShouldAllowAutoSubmit(true); 
```

## Update merchant response timeout

Merchant response timeout is the duration PayU will wait for merchant surl/furl to load before passing the transaction response back to the app. If merchant surl/furl pages take longer to load, PayU has a response timeout of 10 sec by default. However, if you feel that the surl/furl can take longer than 10 seconds, you can configure this flag.

```Text JAVA
PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig();
payUOtpAssistConfig.setMerchantResponseTimeout(25000); 
// for 25 seconds timeout 
```
```Text Kotlin
PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig();
payUOtpAssistConfig.setMerchantResponseTimeout(25000); 
// for 25 seconds timeout 
```

## Disable or enable vibration after a successful transaction

After the payment gets successful, the user's mobile vibrates for 0.5Sec. You need to Add the VIBRATE permission in your Manifest file.

## Vibrate permission

```Text XML
<uses-permission android:name="android.permission.VIBRATE"/>
```

> 📘 Tip
>
> You can disable the vibration behavior from PayUOtpAssistConfig also.

## Disable merchant summary from UI

You can disable merchant summary from the UI.

```Text JAVA
PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig();
payUOtpAssistConfig.setShouldShowMerchantSummary(false);
```
```Text Kotlin
val payUOtpAssistConfig = PayUOtpAssistConfig() 
payUOtpAssistConfig.shouldShowMerchantSummary=false   
```

## Card BIN eligibility check

You can check the card whether your card bin eligible or not for the OTP on the Merchant App. For more information, refer to the ~~Zero Redirect Eligible Bins API.~~
