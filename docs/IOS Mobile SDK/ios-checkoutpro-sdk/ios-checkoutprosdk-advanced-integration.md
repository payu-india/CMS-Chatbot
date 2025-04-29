---
title: Advanced Integration
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
The iOS CheckoutPro SDK provides the following advanced integration options:

* [Enable offer](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#enable-offer)
* [Change theme](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#change-theme)
* [Configure merchant name & logo](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#configure-merchant-name--logo)
* [Hide Checkout screen Back button dialog box](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#hide-checkout-screen-back-button-dialog-box)
* [Hide the Back button dialog box after Payment Initialisation](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#hide-the-back-button-dialog-box-after-payment-initialisation)
* [Auto Select OTP](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#auto-select-otp)
* [Auto Submit OTP](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#auto-submit-otp)
* [Configure merchant response timeout](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#configure-merchant-response-timeout)
* [Review order](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#review-order)
* [Additional payment options on the Checkout screen](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#additional-payment-options-on-the-checkout-screen)
* [Configure checkout payment modes order](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#configure-checkout-payment-modes-order)
* [Set Native OTP Assist](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#set-native-otp-assist)
* [Enforced payment modes](https://docs.payu.in/docs/ios-checkoutprosdk-advanced-integration#enforced-payment-modes)

> 📘 Tip
>
> You can dynamically make the changes listed in this section using the PayU Dashboard. For more information, refer to Dynamic Configuration using Dashboard.

## Enable offer

We introduce a new offer. Now, the only thing you need to give as a distinct string key for the user is a user token.

```Text Swift
paymentParam.userToken = "<userToken>"
```
```Text Objective-C
paymentParam.userToken = @"<userToken>";
```

## Change theme

You can change the primary and the secondary color of the GUI to match your app’s theme:

```Text Swift
let config = PayUCheckoutProConfig()
config.customiseUI(primaryColor: <#UIColor#>, secondaryColor: <#UIColor#>)
```
```Text Objective-C
PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
[config customiseUIWithPrimaryColor:[UIColor blueColor] secondaryColor:[UIColor whiteColor]];
```

## Configure merchant name & logo

You can customize the name and logo to personalize the checkout screen:

```Text Swift
let config = PayUCheckoutProConfig()
config.merchantName = <#T##String?#>
config.merchantLogo = <#T##UIImage?#>
```

## Hide Checkout screen Back button dialog box

You can choose to hide the dialog box displayed when the back button is clicked from the L1 screen. The default value is true.

```Text Swift
let config = PayUCheckoutProConfig()
config.showExitConfirmationOnCheckoutScreen = <#Bool#>
```
```Text Objective-C
PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.showExitConfirmationOnCheckoutScreen = <#(BOOL)#>;
```

## Hide the Back button dialog box after Payment Initialisation

You can choose to hide the dialog box displayed when the back button is clicked after payment is initialized. The default value is true.

```Text Swift
let config = PayUCheckoutProConfig()
config.showExitConfirmationOnCheckoutScreen = <#Bool#>
```
```Text Objective-c
PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.showExitConfirmationOnCheckoutScreen = <#(BOOL)#>;
```

## Auto Select OTP

You can choose to auto-select OTP flow on the bank page with the following flag. The default value is false.

```Text Swift
let config = PayUCheckoutProConfig()
config.autoSelectOtp = <#Bool#>
```
```Text Objective-C
PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.autoSelectOtp = <#BOOL#>;
```

## Auto Submit OTP

You can choose to auto Submit OTP flow on the bank page with the following flag. The default value is false.

```Text Swift
let config = PayUCheckoutProConfig()
config.autoSubmitOtp = <#Bool#>
```
```Text Objective-C
PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.autoSubmitOtp = <#BOOL#>;
```

## Configure merchant response timeout

This is the time PayU will wait for the merchant surl/furl to load before passing the transaction response back to the app. If the merchant surl/furl page takes longer to load, PayU has a response timeout of 5 seconds by default. However, if you feel that your surl/furl can take more than 5 seconds, you can configure this property:

```Text Swift
let config = PayUCheckoutProConfig()
config.merchantResponseTimeout = <#TimeInterval?#>
```
```Text Objective-C
PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.merchantResponseTimeout = <#(NSTimeInterval * _Nullable)#>;
```

## Review order

You can pass the checkout order details to the SDK that will be displayed in the SDK during the transaction flow:

```Text Swift
let config = PayUCheckoutProConfig()
config.cartDetails = [["Milk": "1L"],["Butter": "1Kg"]]
```
```Text Objective-C
PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.cartDetails = @[@{@"Milk": @"1L"},@{@"Butter": @"1Kg"}];
```

## Additional payment options on the Checkout screen

Consider the following example to display Google Pay, PhonePe, and PayTM on the primary checkout screen:

```Text Swift
var preferredPaymentModes: [PaymentMode] = []
preferredPaymentModes.append(PaymentMode(paymentType: .upi, paymentOptionID: BankCodes.gPayUPI))
preferredPaymentModes.append(PaymentMode(paymentType: .wallet, paymentOptionID: BankCodes.phonePeWallet))
preferredPaymentModes.append(PaymentMode(paymentType: .wallet, paymentOptionID: BankCodes.paytmWallet))

let config = PayUCheckoutProConfig()
config.paymentModesOrder = preferredPaymentModes
```
```Text Objective-C
NSMutableArray<PaymentMode *> *preferredPaymentModes = [NSMutableArray new];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType:PaymentTypeUpi paymentOptionID:BankCodes.gPayUPI]];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType:PaymentTypeWallet paymentOptionID:BankCodes.phonePeWallet]];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType:PaymentTypeWallet paymentOptionID:BankCodes.paytmWallet]];

PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.paymentModesOrder = preferredPaymentModes;
```

This will display Google Pay, PhonePe, and Paytm respectively on top of available payment options. To reorder all the payment options, check the next section.

***

## Configure checkout payment modes order

The default payment modes order on the checkout screen is as follows:

* Card
* NetBanking
* UPI
* Wallets

You can configure the above checkout payment options order. For this, you need to provide a list of payment modes. Checkout order will be the order of items in the list. If not all payment modes' order is mentioned in the list, other payment modes will be displayed in their default order as shown above.

For example, to order Cards and UPI on the L1 screen:

```Text Swift
var preferredPaymentModes: [PaymentMode] = []
preferredPaymentModes.append(PaymentMode(paymentType: .ccdc))
preferredPaymentModes.append(PaymentMode(paymentType: .netBanking))
preferredPaymentModes.append(PaymentMode(paymentType: .upi))
preferredPaymentModes.append(PaymentMode(paymentType: .wallet))
preferredPaymentModes.append(PaymentMode(paymentType: .emi))

let config = PayUCheckoutProConfig()  
config.paymentModesOrder = preferredPaymentModes
```
```Text Objective-C
NSMutableArray<PaymentMode *> *preferredPaymentModes = [NSMutableArray new];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType: PaymentTypeCcdc paymentOptionID: nil]];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType: PaymentTypeNetBanking paymentOptionID: nil]];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType: PaymentTypeUpi paymentOptionID: nil]];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType: PaymentTypeWallet paymentOptionID: nil]];
[preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType: PaymentTypeEmi paymentOptionID: nil]];

PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
config.paymentModesOrder = preferredPaymentModes;
```

The resulting order on the initial checkout screen will be:

* Cards (credit/debit)
* Net Banking
* UPI
* Wallets
* EMI

***

## Set Native OTP Assist

It offers to capture OTP in the merchant app without any redirection to the bank’s 3Dsecure/ACS page. This means that there’s one less point of failure in the checkout process and a faster completion rate for transactions. To integrate this, please get enabled txn\_s2s\_flow on your merchant key from your Key Account Manager at PayU.

For more information on Native OTP Assist experience, refer to [iOS Native OTP Assist SDK](doc:ios-native-otp-assist-sdk).

Merchants can choose to auto Native OTP flow with the below flag. The default value is false.

```Text Swift
paymentParam.enableNativeOTP = <#Bool#>
```
```Text Objective-C
paymentParam.enableNativeOTP = <#(BOOL)#>;
```

***

## Enforced payment modes

You can directly open a specific payment mode like NB, WALLET, UPI, CARD, etc in SDK. Create an enforce payment list similar to the following code block to enforce payment modes:

```Text Swift
var enforcePaymentList = [[String: Any]]()
          
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.nb])
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.card, PaymentParamConstant.cardType: PaymentParamConstant.cc])
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.upi])
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.wallet])
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.emi])
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.neftrtgs])
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.sodexo])
enforcePaymentList.append([PaymentParamConstant.paymentType: PaymentParamConstant.lazypay])
 
config.enforcePaymentList = enforcePaymentList
```
```Text Objective-C
NSMutableArray * enforcePaymentList = [NSMutableArray new];
    
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.nb}];
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.card, PaymentParamConstant.cardType: PaymentParamConstant.cc}];
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.upi}];
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.wallet}];
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.emi}];
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.neftrtgs}];
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.sodexo}];
[enforcePaymentList addObject:@{PaymentParamConstant.paymentType: PaymentParamConstant.lazypay}];
 
config.enforcePaymentList = enforcePaymentList;
```

> 📘 Note:
>
> To enforce CC or DC we can add PaymentParamConstant.cc or PaymentParamConstant.dc in the key PaymentParamConstant.cardType. This is an optional parameter. To support both you can ignore this parameter.
