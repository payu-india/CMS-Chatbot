---
title: SDK-Based Wallet Checkout Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: SDK-Based Integration for Merchant Wallets
  description: ''
  robots: index
next:
  description: ''
---
PayU supports merchant wallet integrations on the following SDK platforms:

* [Android SDK](https://docs.payu.in/docs/sdk-based-integration-merchant-wallet?isFramePreview=true#android-sdk)
* [iOS SDK](https://docs.payu.in/docs/sdk-based-integration-merchant-wallet?isFramePreview=true#ios-sdk)
* [React-Native](https://docs.payu.in/docs/sdk-based-integration-merchant-wallet?isFramePreview=true#react-native)

## Android SDK

Closed-Loop wallets allow merchants to accept payments with their self-branded wallets. PayU’s Android SDK enables you to seamlessly integrate with a closed-loop wallet and start accepting payments.

<Callout icon="📘" theme="info">
  **Note**: You can enable Closed-Loop wallet payment mode from PayU’s Merchant Dashboard. Contact your key account manager in PayU if you do not see the payment mode in your Dashboard.
</Callout>

### Prerequisites

1. Enable Closed-Loop Wallet from your Dashboard. 
2. Build the payment parameters with additionalParamsMap[PayUCheckoutProConstants.WALLETURN] additional parameter. For more information, refer to [Android CheckoutPro](https://docs.payu.in/docs/android-checkoutpro-sdk) for Android.

### Customer journey

The following screens show how Closed-Loop wallet works on the PayU payment page:

1. When you enable the Closed-Loop wallet for your account, your customer sees the Closed-Loop wallet payment on top of the payment page under the **SAVED OPTION** option.
2. The wallet balance is fetched and loaded by default as shown below.

<Image align="center" border={false} width="212px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/wallet_amount-loaded-473x1024.jpeg" />

3. If the balance is not loaded due to some error, an error message is displayed as shown in the image below. The customer can tap on the wallet option to reload the amount.

<Image align="center" border={false} width="212px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/wallet-_could-not-load-473x1024.jpg" />

4. After the balance is loaded, the customer can click **Pay Now** to make the payment on your Android application**.**

## iOS SDK

Closed-Loop wallets allow merchants to accept payments with their self-branded wallets. PayU’s iOS SDK enables you to seamlessly integrate with a closed-loop wallet and start accepting payments.

> 📘 Note:
>
> You can enable Closed-Loop wallet payment mode from PayU’s Merchant Dashboard. Contact your key account manager in PayU if you do not see the payment mode in your Dashboard.

### Prerequisites

1. Enable Closed-Loop Wallet from your Dashboard.
2. Build the payment parameters with `PaymentParamConstant.walletURN` parameters. See [Integrate with PayU checkoutpro for iOS](https://docs.payu.in/docs/ios-checkoutpro-sdk) to learn more.

### Customer Journey

The following screens show how Closed-Loop wallet payment works on the PayU payment page:

1. When you enable the Closed-Loop wallet for your account, your customer sees the Closed-Loop wallet payment on top of the payment page under the **SAVED OPTION** tab.
2. The closed-loop wallet balance is fetched and loaded (see the screenshot below) by default.

<Image align="center" border={false} width="212px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/wallet_amount-loaded-473x1024.jpeg" />

3. If the balance is not loaded due to some error, an error message will be displayed (see the screenshot below). The customer can tap on the wallet option to reload the amount.

<Image align="center" border={false} width="212px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/wallet-_could-not-load-473x1024.jpg" />

4. Once the balance is loaded the customer can make the payment by clicking **Pay Now.**

## React-Native

Closed-Loop wallets allow merchants to accept payments with their self-branded wallets. PayU’s SDK enables you to seamlessly integrate with a closed-loop wallet and start accepting payments.

<Callout icon="📘" theme="info">
  **Note**: You can enable Closed-Loop wallet payment mode from PayU’s Merchant Dashboard. Contact your PayU Key Account Manager if you do not see the payment mode on your PayU Dashboard.
</Callout>

### Prerequisites

1. Enable Closed-Loop Wallet from your Dashboard.
2. Build the payment parameters with `walletURN` key in additionalParam. See [Integrate with PayU checkoutpro](https://docs.payu.in/docs/react-native-checkoutpro-sdk) to learn more.

### Workflow

The following screens show how Closed-Loop wallet payment works on the PayU payment page:

1. When you enable the Closed-Loop wallet for your account, your customer sees the Closed-Loop wallet payment on top of the payment page under the **SAVED OPTION** tab.
2. The closed-loop wallet balance is fetched and loaded (see the screenshot below) by default.

<Image align="center" border={false} width="212px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/wallet_amount-loaded-473x1024.jpeg" />

3. If the balance is not loaded due to some error, an error message will be displayed (see the screenshot below). The customer can tap on the wallet option to reload the amount.

<Image align="center" border={false} width="212px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2023/03/wallet-_could-not-load-473x1024.jpg" />

4. Once the balance is loaded the customer can make the payment by clicking **Pay Now.**