---
title: Dynamic Configuration using Dashboard
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
When using checkout pro SDK, you can customize the configurations dynamically. This can be done without updating or releasing your application release. You can update the order of payment options listed on the app, color theme, logo, and other configurations can be updated remotely. This will reduce your effort and time to update these configurations and provides flexibility to all the possible changes you wish to make.

This feature is specifically intended to dynamically fetch the details from the server based on the values you have saved and want the SDK to adopt. It will replace/override only those configurations that you will update using the PayU Dashboard of the local configuration provided during the integration of SDK with your application.

## How dynamic configuration works?

* The existing local config will work as it is, no change is required from the merchant side to support dynamic configuration.
* As soon as you add or update the config values on PayU Dashboard and start a new transaction on SDK. It will fetch the config from the server.
* If the dashboard configuration is not available, the local configuration will be used, which was passed while initializing the SDK.
* If the dashboard configuration is received it will override the local configuration.

## How to enable dynamic updates?

Use the latest version of the Checkout Pro SDK and add/update the config on One Dashboard. The changes will automatically reflect in your app. To enable this configuration, navigate to the following PayU Dashboard page: [https://www.payu.in/business/payment-gateway/sdk-settings](https://www.payu.in/business/payment-gateway/sdk-settings)

**Supported configurations in the dynamic update**: PayU has divided configuration into General and Advanced configurations.

### General

* Brand Name
* Logo
* Modify Theme Color
* Primary
* Accent (Applied only in Android SDK)
* Primary Dark (Applied only in Android SDK)
* Base Text Color

<Image align="center" className="border" border={true} src="https://files.readme.io/84e6265-Screenshot_2023-08-11_at_12.37.19_AM.png" />

### Advance

* The toolbar in the Custom Browser (Applied only in Android SDK)
* Checkout Screen Back Button Dialog Box
* Cross Browser Back Button Dialog Box
* Runtime SMS Permission (Applied only in Android SDK)
* OTP Auto Submit
* Auto Select OTP
* Response Timeout
* Waiting for OTP Timeout (Applied only in Android SDK)
* Payment Modes Sort Order

<Image align="center" className="border" border={true} src="https://files.readme.io/3bd6f67-Screenshot_2023-08-11_at_12.38.27_AM.png" />

> 📘 Remember:
>
> * The local configuration will be updated with the dashboard configuration. So, if you face any difference between local and dashboard configuration try to update the dashboard configuration.
> * To start using dynamic config use the latest version of SDK 1.8.5. Also, if you are using PayU OTP assist SDK please update its version to 1.2.2.
