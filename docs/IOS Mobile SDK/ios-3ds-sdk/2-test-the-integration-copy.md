---
title: 2. Test the Integration
excerpt: Use the Test mode to check if the integration is working as expected.
deprecated: false
hidden: false
metadata:
  title: iOS-3dsSdk-Test-integration
  description: ''
  robots: index
next:
  description: ''
---
After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<UPIIntentCallout />

<TestingChecklist />

***

<TestCardsCallout />



## Test credentials for supported payment methods

Following are the payment methods supported in PayU Test mode.

### Test credentials for Net Banking

Use the following credentials to test the Net Banking integration:

- **user name:** payu
- **password**: payu
- **OTP**: 123456

### Test VPA for UPI

You can use either of the following VPAs to test your UPI-related integration:

- [anything@payu](anything@payu)
- [9999999999@payu.in](mailto:9999999999@payu.in)

> ❗️ Callout
> 
> The UPI in-app and UPI intent flow is not available in the Test mode.

### Test cards for EMI

You can use the following Debit and Credit cards to test Emi integration.

[block:parameters]
{
  "data": {
    "h-0": "",
    "h-1": "",
    "0-0": "Kotak DC EMI",
    "0-1": "1. **Card Number**: 4706-1378-0509-9594  \n2. **Expiry**: any future date (mm/yy)  \n3. **CVV**: 123  \n4. **OTP**: 111111  \n5. **Name**: Any name  \n6. **Mobile Number**: 9123412345 (mandatory for EMI)",
    "1-0": "AXIS DC EMI",
    "1-1": "1. **Card Number**: 4011-5100-0000-0007  \n2. **Expiry**: any future date (mm/yy)  \n3. **CVV**: 123  \n4. **OTP**: 111111  \n5. **Name**: Any name  \n6. **Mobile Number**: 9123412345 (mandatory for EMI)",
    "2-0": "HDFC CC EMI",
    "2-1": "1. **Card Number**: 4453-3410-65876437  \n2. **Expiry**: any future date (mm/yy)  \n3. **CVV**: 123  \n4. **OTP**: 111111  \n5. **Name**: Any name  \n6. **Mobile Number**: 9123412345 (mandatory for EMI)",
    "3-0": "ICICI CC EMI",
    "3-1": "1. **Card Number**: 4453-3410-65876437  \n2. **Expiry**: any future date (mm/yy)  \n3. **CVV**: 123  \n4. **OTP**: 111111  \n5. **Name**: Any name  \n6. **Mobile Number**: 9123412345 (mandatory for EMI)"
  },
  "cols": 2,
  "rows": 4,
  "align": [
    "left",
    "left"
  ]
}
[/block]


### Test Wallets

You can use the following wallets and their corresponding credentials to test wallet integration.

[block:parameters]
{
  "data": {
    "h-0": "Wallet",
    "h-1": "Mobile Number",
    "h-2": "OTP",
    "0-0": "PayTM",
    "0-1": "7777777777",
    "0-2": "888888",
    "1-0": "PhonePe",
    "1-1": "Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: <https://developer.phonepe.com/v1/docs/setting-up-test-account>  \nDownload the app and register your mobile number and follow the instructions as described in the above PhonePe docs.",
    "1-2": "NA",
    "2-0": "AmazonPay",
    "2-1": "You can test using your original Amazon account details.",
    "2-2": ""
  },
  "cols": 3,
  "rows": 3,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]