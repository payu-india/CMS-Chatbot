---
title: PayU OTP Parser
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
PayU OTP Parser SDK was built to read the OTP from the SMS and pass it to the user. It is also implemented in PayU OTP Assist SDK that makes the OTP reading process very simple. It fetches the OTP through RECEIVE\_SMS if RECEIVE\_SMS permission is granted. Otherwise, fetch the OTP using Google Consent API.

**Selecting OTP Fetch Method**

<Image align="center" src="https://files.readme.io/a689e0e-Screenshot_2023-11-21_at_3.34.20_PM.png" />

## Steps to integrate

1. Include the SDK in your application
2. Initiate the SDK
3. Override these callbacks

***

## Step 1: Include the SDK in your Application

Add below dependency in the application’s build.gradle:

`implementation 'in.payu:native-otp-reader:1.2.5'`

## Step 2: Initiate the SDK
