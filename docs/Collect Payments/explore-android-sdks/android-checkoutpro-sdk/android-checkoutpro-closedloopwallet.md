---
title: Integrate with Closed Loop Wallet
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
title: Integrate with Closed Loop Wallet
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Closed Loop Wallet - Android CheckoutPro
  description: >-
    Integrate closed-loop wallet payments with PayU CheckoutPro on Android: enable wallet mode, WALLET_URN params, and checkout flow.
  keywords:
    - payu checkoutpro closed loop wallet android integration
    - android closed loop wallet payment sdk payu checkoutpro
    - integrate closed loop wallet android checkout pro payu sdk
    - payu android sdk branded wallet payment integration india
    - mobile wallet checkoutpro android integration guide payu
    - payment gateway android closed loop wallet payu sdk
    - payu checkout pro wallet urn payment parameters android
    - android in app closed loop wallet integration payu gateway
    - payu android checkoutpro wallet mode enable dashboard
    - closed loop wallet sdk android payment integration payu
    - payu merchant wallet android sdk integration steps checkout
    - android payment sdk self branded wallet payu checkoutpro
  robots: index
next:
  description: ''
---
Closed-Loop wallets allow merchants to accept payments with their self-branded wallets. PayU’s Android SDK enables you to seamlessly integrate with a closed-loop wallet and start accepting payments.

<Callout icon="📘" theme="info">
  **Note**: You can enable Closed-Loop wallet payment mode from PayU’s Merchant Dashboard. Contact your key account manager in PayU if you do not see the payment mode in your Dashboard.
</Callout>

## Prerequisites

1. Enable Closed-Loop Wallet from your Dashboard.
2. Build the payment parameters with `additionalParamsMap[PayUCheckoutProConstants.WALLET_URN]` additional parameter. For more information, refer to [Integration Steps](doc:integration-steps-android-checkout-pro).

## Customer Journey

The following screens show how Closed-Loop wallet works on the PayU payment page:

1. When you enable the Closed-Loop wallet for your account, your customer sees the Closed-Loop wallet payment on top of the payment page under the **Saved Option** option.
2. The wallet balance is fetched and loaded by default as shown below.

<Image align="center" border={false} width="30% " src="https://files.readme.io/db9e252-Screenshot_2023-11-16_at_5.36.13_PM.png" />

3. If the balance is not loaded due to some error, an error message is displayed as shown in the following screenshot. The customer can tap on the wallet option to reload the amount.

<Image align="center" border={false} width="30% " src="https://files.readme.io/e1e2bc5-Screenshot_2023-11-16_at_5.38.09_PM.png" />

4. After the balance is loaded, the customer can click Pay Now to make the payment on your Android application.