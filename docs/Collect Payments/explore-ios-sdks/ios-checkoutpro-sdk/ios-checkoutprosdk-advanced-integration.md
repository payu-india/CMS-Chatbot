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
---
title: Advanced Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Advanced PayU CheckoutPro iOS integration: custom UI, payment modes, offers, SKU flows, and CheckoutPro SDK configuration options.
  keywords:
    - payu ios checkoutpro advanced integration guide swift
    - ios checkout pro sdk advanced configuration payment payu
    - iphone payment sdk checkoutpro customize integration payu
    - integrate payment gateway ios advanced checkout pro payu
    - ios payment gateway sdk customization checkoutpro india
    - payu ios sdk advanced payment modes offers integration
    - mobile payment sdk ios checkoutpro advanced developer
    - payment gateway ios sdk advanced integration steps payu
    - payu checkoutpro ios sdk ui customization integration
    - native ios checkout pro advanced payment integration payu
    - ios in app payment sdk advanced checkoutpro payu india
    - swift ios payment sdk checkout pro advanced guide payu
  robots: index
next:
  description: ''
---
The iOS CheckoutPro SDK provides the following advanced integration options:

### Tip

<Callout icon="📘" theme="info">
  You can dynamically make the changes listed in this section using the PayU Dashboard. For more information, refer to Dynamic Configuration using Dashboard.
</Callout>

<Accordion title="Enable offer" icon="fa-code">
  We introduce a new offer. Now, the only thing you need to give as a distinct string key for the user is a user token.

  ```swift Swift
  paymentParam.userToken = "<userToken>"
  ```
  ```objectivec Objective-C
  paymentParam.userToken = @"<userToken>";
  ```
</Accordion>

<Accordion title="Change theme" icon="fa-code">
  You can change the primary and the secondary color of the GUI to match your app's theme:

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.customiseUI(primaryColor: <#UIColor#>, secondaryColor: <#UIColor#>)
  ```
  ```objectivec Objective-C
  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  [config customiseUIWithPrimaryColor:[UIColor blueColor] secondaryColor:[UIColor whiteColor]];
  ```
</Accordion>

<Accordion title="Configure merchant name & logo" icon="fa-code">
  You can customize the name and logo to personalize the checkout screen:

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.merchantName = <#T##String?#>
  config.merchantLogo = <#T##UIImage?#>
  ```
</Accordion>

<Accordion title="Show/Hide Merchant Logo" icon="fa-code">
  Merchants can display their logo on the PayU Hosted Page. By default, the logo is invisible.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.showMerchantLogo = true // true/false
  ```
</Accordion>

<Accordion title="Show/Hide Saved Card Features" icon="fa-code">
  Merchants can control the Saved Card feature visibility. By default, the Saved Card feature is enabled.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.enableSavedCard = true // true/false
  ```
</Accordion>

<Accordion title="Screen Protection" icon="fa-code">
  Screen protection is enabled by default to hide sensitive information during screen recording or screenshots. When enabled, card details and credentials will be protected and not visible in screen captures.

  If you need to disable this protection (not recommended), set the value to false. When disabled, sensitive information will be visible in screen recordings and screenshots.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.isProtectedScreen = false // Disable protection (NOT RECOMMENDED)
  ```

  ⚠️ **Security Warning:** Disabling screen protection may expose sensitive payment information in screenshots and recordings.
</Accordion>

<Accordion title="Customize UPI Apps Order" icon="fa-code">
  You can customize the display order of UPI payment apps. Define the sequence using a pipe-separated format to rearrange how UPI apps appear to users.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.upiAppsOrder = "phonepe|paytm|gpay"
  ```
</Accordion>

<Accordion title="Hide Checkout screen Back button dialog box" icon="fa-code">
  You can choose to hide the dialog box displayed when the back button is clicked from the L1 screen. The default value is true.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.showExitConfirmationOnCheckoutScreen = <#Bool#>
  ```
  ```objectivec Objective-C
  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  config.showExitConfirmationOnCheckoutScreen = <#(BOOL)#>;
  ```
</Accordion>

<Accordion title="Hide the Back button dialog box after Payment Initialisation" icon="fa-code">
  You can choose to hide the dialog box displayed when the back button is clicked after payment is initialized. The default value is true.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.showExitConfirmationOnCheckoutScreen = <#Bool#>
  ```
  ```objectivec Objective-C
  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  config.showExitConfirmationOnCheckoutScreen = <#(BOOL)#>;
  ```
</Accordion>

<Accordion title="Auto Select OTP" icon="fa-code">
  You can choose to auto-select OTP flow on the bank page with the following flag. The default value is false.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.autoSelectOtp = <#Bool#>
  ```
  ```objectivec Objective-C
  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  config.autoSelectOtp = <#BOOL#>;
  ```
</Accordion>

<Accordion title="Auto Submit OTP" icon="fa-code">
  You can choose to auto Submit OTP flow on the bank page with the following flag. The default value is false.

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.autoSubmitOtp = <#Bool#>
  ```
  ```objectivec Objective-C
  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  config.autoSubmitOtp = <#BOOL#>;
  ```
</Accordion>

<Accordion title="Configure merchant response timeout" icon="fa-code">
  This is the time PayU will wait for the merchant surl/furl to load before passing the transaction response back to the app. If the merchant surl/furl page takes longer to load, PayU has a response timeout of 5 seconds by default. However, if you feel that your surl/furl can take more than 5 seconds, you can configure this property:

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.merchantResponseTimeout = <#TimeInterval?#>
  ```
  ```objectivec Objective-C
  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  config.merchantResponseTimeout = <#(NSTimeInterval * _Nullable)#>;
  ```
</Accordion>

<Accordion title="Review order" icon="fa-code">
  You can pass the checkout order details to the SDK that will be displayed in the SDK during the transaction flow:

  ```swift Swift
  let config = PayUCheckoutProConfig()
  config.cartDetails = [["Milk": "1L"],["Butter": "1Kg"]]
  ```
  ```objectivec Objective-C
  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  config.cartDetails = @[@{@"Milk": @"1L"},@{@"Butter": @"1Kg"}];
  ```
</Accordion>

<Accordion title="Additional payment options on the Checkout screen" icon="fa-code">
  Consider the following example to display Google Pay, PhonePe, and PayTM on the primary checkout screen:

  ```swift Swift
  var preferredPaymentModes: [PaymentMode] = []
  preferredPaymentModes.append(PaymentMode(paymentType: .upi, paymentOptionID: BankCodes.gPayUPI))
  preferredPaymentModes.append(PaymentMode(paymentType: .wallet, paymentOptionID: BankCodes.phonePeWallet))
  preferredPaymentModes.append(PaymentMode(paymentType: .wallet, paymentOptionID: BankCodes.paytmWallet))

  let config = PayUCheckoutProConfig()
  config.paymentModesOrder = preferredPaymentModes
  ```
  ```objectivec Objective-C
  NSMutableArray<PaymentMode *> *preferredPaymentModes = [NSMutableArray new];
  [preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType:PaymentTypeUpi paymentOptionID:BankCodes.gPayUPI]];
  [preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType:PaymentTypeWallet paymentOptionID:BankCodes.phonePeWallet]];
  [preferredPaymentModes addObject: [[PaymentMode alloc] initWithPaymentType:PaymentTypeWallet paymentOptionID:BankCodes.paytmWallet]];

  PayUCheckoutProConfig *config = [PayUCheckoutProConfig new];
  config.paymentModesOrder = preferredPaymentModes;
  ```

  This will display Google Pay, PhonePe, and Paytm respectively on top of available payment options. To reorder all the payment options, check the next section.

  ***
</Accordion>

<Accordion title="Configure checkout payment modes order" icon="fa-code">
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
</Accordion>

<Accordion title="Set Native OTP Assist" icon="fa-code">
  It offers to capture OTP in the merchant app without any redirection to the bank's 3Dsecure/ACS page. This means that there's one less point of failure in the checkout process and a faster completion rate for transactions. To integrate this, please get enabled txn\_s2s\_flow on your merchant key from your Key Account Manager at PayU.

  For more information on Native OTP Assist experience, refer to [iOS Native OTP Assist SDK](doc:ios-native-otp-assist-sdk).

  Merchants can choose to auto Native OTP flow with the below flag. The default value is false.

  ```Text Swift
  paymentParam.enableNativeOTP = <#Bool#>
  ```
  ```Text Objective-C
  paymentParam.enableNativeOTP = <#(BOOL)#>;
  ```

  ***
</Accordion>

<Accordion title="Enforced payment modes" icon="fa-code">
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
</Accordion>