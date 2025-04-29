---
title: Integrate with Closed Loop Wallet
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
Closed-Loop wallets allow merchants to accept payments with their self-branded wallets. PayU’s Android SDK enables you to seamlessly integrate with a closed-loop wallet and start accepting payments.

> 📘 Note
>
> You can enable Closed-Loop wallet payment mode from PayU’s Merchant Dashboard. Contact your key account manager in PayU if you do not see the payment mode in your Dashboard.

## Prerequisites

1. Enable Closed-Loop Wallet from your Dashboard.
2. Build the payment parameters with `additionalParamsMap[PayUCheckoutProConstants.WALLET_URN]` additional parameter. For more information, refer to [Integration Steps](https://docs.payu.in/docs/android-checkoutpro-integration-steps) of Android checkout pro SDK.

## Customer Journey

The following screens show how Closed-Loop wallet works on the PayU payment page:

1. When you enable the Closed-Loop wallet for your account, your customer sees the Closed-Loop wallet payment on top of the payment page under the **SAVED OPTION** option.
2. The wallet balance is fetched and loaded by default as shown below.

<Image align="center" width="30% " src="https://files.readme.io/db9e252-Screenshot_2023-11-16_at_5.36.13_PM.png" />

3. If the balance is not loaded due to some error, an error message is displayed as shown in the image below. The customer can tap on the wallet option to reload the amount.

<Image align="center" width="30% " src="https://files.readme.io/e1e2bc5-Screenshot_2023-11-16_at_5.38.09_PM.png" />

4. After the balance is loaded, the customer can click Pay Now to make the payment on your Android application.
