---
title: Advanced Integrations
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
You can perform the following after completing the basic integration:

- [Change the theme](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#change-the-theme)
- [Set merchant logo](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#set-merchant-logo)
- [Set merchant name](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#set-merchant-name)
- [Hide Checkout screen Back button Dialog box](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#hide-checkout-screen-back-button-dialog-box)
- [Hide Back button dialog box after payment initialisation](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#hide-back-button-dialog-box-after-payment-initialisation)
- [Auto Select OTP](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#auto-select-otp)
- [Set merchant response timeout](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#set-merchant-response-timeout)
- [Review order](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#review-order)
- [Additional payment options on the Checkout screen](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#additional-payment-options-on-the-checkout-screen)
- [Configure checkout payment modes order](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#configure-checkout-payment-modes-order)
- [Offers](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#offers)
- [Native OTP Assist](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#native-otp-assist)
- [Custom Note integration](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#custom-note-integration)
- [Enforced payment modes](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#enforced-payment-modes)
- [Android specific configurations](https://docs.payu.in/docs/cordova-checkoutprosdk-advance-integrations#android-specific-configurations)

> 🚧 Callout
> 
> Before you begin with the advanced integration with PayUCheckoutPro, the payUCheckoutProConfig object needs to be passed with payUPaymentParams in the openCheckoutScreen method of `PayUBizSdk`. You can use the following sample code snippet:
> 
> ```
> let payuParams = {
>       payUPaymentParams: <PayUPaymentParams>,
>       payUCheckoutProConfig: <PayUCheckoutProConfig>
> }  
> ```

***

## Change the theme

**For iOS**, you can change the primary and the secondary color of the UI to match the theme of your app. Here is a sample code snippet to change the theme:

```
var payUCheckoutProConfig = { 
  primaryColor: "<Color Hex Code e.g. #aabbcc>", 
  secondaryColor: "<Color Hex Code e.g. #000000>", 
}
```

**For Android**: To change the primary color, add the color values in your Android colors.xml. For more information, refer to [Customize your Integration](<>).

***

## Set merchant logo

You can customize the logo to personalize the checkout screen. 

**For iOS**: Save the image in the images assets of your app and pass the assets name in merchantLogo.

**For Android**: Add the image in the app/res/drawable folder in the native Android app and pass the same under the merchantLogo key.

```
var payUCheckoutProConfig = {
    merchantLogo: <Image asset name like 'logo'>
}
```

***

## Set merchant name

You can customize the name to personalize the checkout screen.

```
var payUCheckoutProConfig = {
    merchant name: <String> 
}
```

***

## Hide Checkout screen Back button Dialog box

You can choose to hide the Dialog box that appears when the Back button is clicked from the L1 screen. The default value is true. 1

```
var payUCheckoutProConfig = {
    showExitConfirmationOnCheckoutScreen: <boolean>, //true:false, //Optional
}
```

***

## Hide Back button dialog box after payment initialisation

You can choose to hide the Dialog that appears when the back button is pressed after payment is initialized. The default value is true.

```
var payUCheckoutProConfig = {
    showExitConfirmationOnPaymentScreen: <boolean>, //true:false, //Optional
}
```

***

## Auto Select OTP

You can choose to auto-select OTP flow on the bank page with the flag as in the following code block. The default value is false.

```
var payUCheckoutProConfig = {
    autoSelectOtp: <boolean>, //true:false, //Optional
}
```

***

## Set merchant response timeout

The merchant response timeout is the time interval that PayU waits for merchant surl/furl to load before passing the transaction response back to the app. If merchant surl/furl pages take longer to load, PayU has a response timeout of 5000 milliseconds by default. However, if merchants feel that their surl/furl can take longer than 5000 milliseconds, they can set this flag.

```
var payUCheckoutProConfig = {
    merchantResponseTimeout: <number> //Optional e.g. 5000
}

```

***

## Review order

You can pass the checkout order details to the SDK that will be displayed in the SDK during the transaction flow.

```
var cartDetails = [
    {"GST": "5%"},
    {"Delivery Date": "25 Dec"},
    {"Status": "In Progress"}
];

var payUCheckoutProConfig = {
    cartDetails: cartDetails
}

```

***

## Additional payment options on the Checkout screen

The following code snippet is used to display Google Pay, PhonePe, and Paytm on the primary Checkout screen. This will display Google Pay, PhonePe, and Paytm respectively on top of available payment options. To reorder all the payment options, refer to Configure Checkout Payment Modes Order.

```
var paymentModesOrder = [
  {"Wallets": "PHONEPE"},
  {"UPI": "TEZ"},
  {"Wallets": ""},
  {"EMI": ""},
  {"NetBanking": ""},
];
var payUCheckoutProConfig = {
    paymentModesOrder: paymentModesOrder,
}

```

***

## Configure checkout payment modes order

Default payment modes order on the checkout screen as in the following code block: Card, NetBanking, UPI, and Wallets. 

You can specify the checkout payment options order. For this, the merchant needs to provide a list of payment modes. Checkout order will be the order of items in the list. If not all payment modes’ order is mentioned in the list, all other payment modes will be displayed in their default order as shown above. 

The following code snippet is used to order the payment modes on the L1 screen.

```
var paymentModesOrder = [
  {"Wallets": "PHONEPE"},
  {"UPI": "TEZ"},
  {"Wallets": ""},
  {"EMI": ""},
  {"NetBanking": ""},
];

var payUCheckoutProConfig = {
    paymentModesOrder: paymentModesOrder,
}
```

***

The resulting payment order on the initial Checkout screen will be: 

- Cards (Credit or Debit)
- Net Banking
- UPI
- Wallets
- EMI

## Offers

To pass offers in the CheckoutPro SDK, refer to the below code snippet.

```
var payUPaymentParams = {
      userToken: "<Pass a unique token to fetch offers>", // OPTIONAL
}
```

***

## Native OTP Assist

To Enable Native OTP assistance in iOS, use the following code.

```
var payUPaymentParams = {
    enableNativeOTP: <boolean>, //true:false, //Optional
}
```

**In Android**, This will be added by default.

***

## Custom Note integration

This sub-section describes how to integrate custom notes in PayUCheckoutPro SDK. To integrate custom notes in PayUCheckoutPro SDK:

### Step 1: Create a Custom Note list

Create a list of custom notes that you want to pass to the CheckoutPro SDK. Pass `custom_note` and `custom_note_category` parameters for each custom note.

```
class PayUPaymentTypeKeys {
    static  card =  "CARD";
    static  nb =  "NB";
    static  upi =  "UPI";
    static  upiIntent =  "UPI_INTENT";
    static  wallet =  "WALLET";
    static  emi =  "EMI";
    static  neftRtgs =  "NEFTRTGS";
    static  l1Option =  "L1_OPTION";
    static  sodexo =  "SODEXO";
}
var customNotes = [
    {
        "custom_note": "It's a Common custom note for testing purposes",
        "custom_note_category": [PayUPaymentTypeKeys.emi,PayUPaymentTypeKeys.card]
    },
    {
        "custom_note": "Payment options custom note",
        "custom_note_category": null
    }
];
```

***

### Step 2: Add in PayUCheckout config

```
var payUCheckoutProConfig = {
    customNotes: customNotes,
  }
```

***

## Enforced payment modes

You can directly open a specific payment mode like NB, WALLET, UPI, CARD, etc in SDK. Create an enforce list similar to the following code block to enforce payment modes: 

### Step 1: Create an enforced payment list

For each enforced payment, the`payment_type`  and `enforce_ibiboCode` parameters need to be passed.

```
var enforcePaymentList = [
    {"payment_type": "CARD", "enforce_ibiboCode": "UTIBENCC"},
];
```

### Step 2: Add in PayU Checkout config

```
var payUCheckoutProConfig = {
enforcePaymentList: enforcePaymentList,
}
```

***

## Android specific configurations

### Runtime SMS permission

You can set this flag to false if they do not want CheckoutPro SDK to ask for runtime SMS permission on the bank OTP page. The default value is true.

```
var payUCheckoutProConfig = {
    merchantSMSPermission: <boolean>, //true:false, //Optional
}
```

### Auto Approve OTP

You can choose to automatically approve OTP flow on the bank page with the flag specified in the following code block. The default value is false.

```
var payUCheckoutProConfig = {
    autoApprove: <boolean>, //true:false, //Optional
}

```

### Hide the toolbar in the Custom Browser (CB)

You can choose to hide the toolbar on CB. The CB toolbar is displayed by default.

```
var payUCheckoutProConfig = {
    showCbToolbar: <boolean>, //true:false, //Optional
}

```