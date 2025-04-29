---
title: 1. Integration Steps
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
Before you start with the integration, enable the payment methods that you want to offer to your customers from Dashboard > Settings > Payment methods. We enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you.

## Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

## Step 2: Set up build.gradle

Add the following dependency in the application’s build.gradle:

`implementation 'in.payu:native-otp-reader:1.1.1'`

## Step 3: Initialize the SDK

Initiate the SDK similar to the following sample code block:

```Text Node

OtpParser otpParser = OtpParser.Companion.getInstance(ComponentActivity activity);
otpParser.startListening(OtpCallback otpCallback)
OtpCallback otpCallback = new OtpCallback() {
@Override
public void onOtpReceived(@NotNull String otp) {
//When user gets the OTP 
}
@Override
public void onUserDenied() {
//User user denied the permission
}
};
```

## Step 4: Step 3: Override these Callbacks

You need to override these ActivityCompat callbacks and call OtpParser methods similar to the following code block:

```Text Node
@Override
public void onRequestPermissionsResult(int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
super.onRequestPermissionsResult(requestCode, permissions, grantResults);
otpParser.onRequestPermissionsResult(requestCode, permissions, grantResults);
//calling OtpParser onRequestPermissionsResult
}
@Override
protected void onActivityResult(int requestCode, int resultCode, @Nullable Intent data) {
super.onActivityResult(requestCode, resultCode, data);
otpParser.onActivityResult(requestCode, resultCode, data);
//calling OtpParser onActivityResult
}
```
