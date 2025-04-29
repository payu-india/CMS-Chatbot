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

## Customisation Options

* [Customisation Options](https://docs.payu.in/docs/ios-nativeotpassistsdk-customise-your-integration#customisation-options)
* [Change theme colour](https://docs.payu.in/docs/ios-nativeotpassistsdk-customise-your-integration#change-theme-colour)
* [Change Waiting for OTP timeout](https://docs.payu.in/docs/ios-nativeotpassistsdk-customise-your-integration#change-waiting-for-otp-timeout)
* [Disable Auto-Submit OTP flag](https://docs.payu.in/docs/ios-nativeotpassistsdk-customise-your-integration#disable-auto-submit-otp-flag)
* [Card BIN eligibility check](#card-bin-eligibility-check)

***

### Update merchant logo

You can display your brand logo in the PayU Native OTP Assist SDK to reinforce trust and branding. To set a logo in the SDK, you need to pass the drawable ID of the logo image resource from your app.

```Text Objective-C
let config = PayUOtpAssistConfig()
config.merchantLogo = #imageLiteral(resourceName: "logo")
```

***

## Change theme colour

Our SDK allows you to change the theme color, and you need to set this primary color in your color file.

```
let config = PayUOtpAssistConfig()
config.themeColor = #colorLiteral(red: 0.01960784314, green: 0.231372549, blue: 0.7568627451, alpha: 1)
```

***

## Change Waiting for OTP timeout

PayU will wait for a specified time for the OTP, after which the SDK falls back to the manual OTP screen. The default time is 30 seconds; you may change it to any other duration. PayU recommends you configure the timeout to less than 60 seconds for a better user experience.

```Text Objective-C
let config = PayUOtpAssistConfig()
config.merchantResponseTimeout = 10000 // In milliseconds
```

***

## Disable Auto-Submit OTP flag

Merchant can enable/disable the auto-submit OTP flow using the following flag. The default value is set to true.

```Text Objective-C
let config = PayUOtpAssistConfig()
config.shouldShowMerchantSummary = true
```

***

## Card BIN eligibility check

You can check the card whether your card bin eligible or not for the OTP on the Merchant App.
