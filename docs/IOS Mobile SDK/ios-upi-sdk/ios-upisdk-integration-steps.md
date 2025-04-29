---
title: 1. SDK Integration Steps - iOS UPI
excerpt: This section describes the technical integration of iOS UPI SDK with the app.
deprecated: false
hidden: false
metadata:
  title: iOS UPI SDK Integration Steps
  description: >-
    The document provides instructions on integrating PayUIndia-UPI and UPICore
    SDKs into your app using Cocoapods or Swift Package Manager, configuring
    payment parameters, callbacks, fetching hashes, processing payments through
    UPI Collect or Intent flows, and making payments through UPICore.
  keywords:
    - PayU UPI SDK integration steps
    - PayU India UPI SDK integration steps
    - ' IOS UPI SDK integration steps'
    - ' UPI SDK integration steps'
    - ' How to integrate PayU UPI SDK in IOS'
    - Step-by-step PayU UPI SDK integration
    - PayU UPI SDK integration steps for IOS apps
    - Detailed steps for PayU UPI SDK integration
  robots: index
next:
  description: ''
---
## Step 1: Integrate Cocapods

Add the following lines to your Podfile: 

```
// make sure to add below-mentioned line to use dynamic frameworks
use_frameworks!
// Add this to include our SDK
pod 'PayUIndia-UPI'
```

### Swift Package Manager Integration

You can integrate PayUIndia-PG-SDK with your app or SDK using the following methods:

- **Using Xcode**: Navigate to File > Add Package menu and install the following package:  
  <https://github.com/payu-intrepos/payu-upi-ios-sdk>
- **Using Package.Swift**: Add the following code to Package.swift dependencies:

```
  .package(name: "PayUIndia-UPIKit", url: "https://github.com/payu-intrepos/payu-upi-ios-sdk", from: "6.0.0")
```

***

## Step 2: Integrate UPICore

You can integrate UPICollet and UPIIntent with your own UI using UPICore.

### Cocoapods integration

Add the following lines into your Podfile:

```
// make sure to add below-mentioned line to use dynamic frameworks
use_frameworks!

// Add this to include our SDK
pod 'PayUIndia-UPICore'
```

### Swift Package Manager Integration

You can integrate PayUIndia-UPIKit, `PayUIndia-UPICoreKit` with your app or SDK in two ways:

Using the Xcode – Go to File-> Add Package-> <https://github.com/payu-intrepos/payu-upi-ios-sdk>  
Using `Package.Swift`, add the following line in `Package.swift `dependencies:

```
.package(name: "PayUIndia-UPICore", url: "https://github.com/payu-intrepos/payu-upi-ios-sdk", from: "6.1.0")
```

***

## Step 3: Make UPI Payments

### Configure Mandatory Payment Parameters

1. Set environment to test or production. You can also set the debugging level to get logs from the SDK.

```Text Swift
PayUUPICore.shared.environment = .production
PayUUPICore.shared.logLevel = .error //Other option is verbose. Logs are disabled by default
```

2. Configure mandatory payment parameters required for the payment:

```Text Swift
do {
paymentParams = try PayUPaymentParams(
merchantKey: "smsplus", //Your merchant key for the environment set in step 1
transactionId: "1iYJfaskjf890", //Your unique ID for this trasaction
amount: "64999", //Amount of transaction
productInfo: "iPhone", // Description of the product
firstName: "Vipin", // First name of the user
email: "johnappleseed@payu.in", // Email of the useer
//User defined parameters.
//You can save additional details with each txn if you need them for your business logic.
//You will get these details back in payment response and transaction verify API
//Like, you can add SKUs for which payment is made.
udf1: "SKU1|SKU2|SKU3",
//You can keep all udf fields blank if you do not have any requirement to save txn specific data
udf2: "",
udf3: "",
udf4: "",
udf5: "")
// Example userCredentials - "merchantKey:user'sUniqueIdentifier"
paymentParams?.userCredentials = "smsplus:myUserEmail@payu.in"
// Success URL. Not used but required due to mandatory check.
paymentParams?.surl = "https://cbjs.payu.in/sdk/success"
// Failure URL. Not used but required due to mandatory check.
paymentParams?.furl = "https://cbjs.payu.in/sdk/failure"
paymentParams?.phoneNumber = "9123456789" // "10 digit phone number here"
} catch let error {
print("Could not create post params due to: \(error.localizedDescription)")
}
```

> 📘 Note:
> 
> The URLs used in **surl** and **furl** are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.

### Configure Callbacks

Configure Callbacks to receive actionable events from SDK:

- **paymentCompletion**: You receive the payment response here.

```Text Swift
 PayUUPICore.shared.paymentCompletion = { [weak self] result in
DispatchQueue.main.async { [weak self] in
guard let self = self else {return}
self.navigationController?.popToRootViewController(animated: false)
switch result {
case .success(let response):
Helper.showAlert(String(describing: response), onController: self)
case .failure(let error):
Helper.showAlert(String(describing: error.rawValue), onController: self)
}
}
}
﻿
```

- **backPressed**: If the user has not yet initiated the transaction, and when the user presses the back button from the UPI payment options page, this callback is triggered. You can dismiss SDK’s UI screen here.

```Text Swift
PayUUPICore.shared.backPressed = {[weak self] in
self?.navigationController?.popToRootViewController(animated: true)
}
```

- **onEnteringVPA**: For validating the VPA entered by the user, we need to hit PayU’s validate VPA API. This API needs a hash. In this callback, you will get the VPA entered by the user. Use this value to generate the required hash. When the hash is received from your server, send us the updated post params with the new hash.

```Text Swift
PayUUPICore.shared.onEnteringVPA = {[weak self] vpa, completion in
guard let self = self else { return }
self.paymentParams?.vpa = vpa
self.fetchHashes(withParams: self.paymentParams!) { result in
switch result {
case .success:
completion(.success(self.paymentParams!))
case .failure(let error):
print("Could not fetch hashes \(error.description)")
completion(.failure(.noInternet()))
}
}
}
﻿
```

### Fetch Hashes

To fetch hashes and save them in the `paymentParams` object:

1. Configure the hashes property in paymentParams. Hashes authenticates that API request originates from the original source to avoid a “Man-in-the-middle attack.” Property hashes are of the PayUHashes type.
2. Define the following PayUHashes properties used for a distinct API call.
   1. `paymentRelatedDetailsForMobileSDKHash`: This is required to get available UPI payment options from which payment can be made.
   2. `paymentHash`: This is required to create transactions at PayU’s end.
   3. `validateVPAHash`: This is required by `validateVPA` API in UPI collect flow to check if provided VPA is registered with a bank account and is active or not. Not required in intent transactions.
3. Provide the first two hashes before asking SDK to initiate the payment. Hashes must be generated only on your server as it needs a secret key (also known as salt). Your app must never contain salt.
4. Command and var1 values for generating `paymentRelatedDetailsForMobileSDKHash` & `validateVPAHash` are described in the following table. For generating hashes on your server, refer to [Hash Generation](https://docs.payu.in/docs/ios-checkoutpro-generate-hash).

| Hash for Parameter                    | Command                                | Var1                                                              |
| :------------------------------------ | :------------------------------------- | :---------------------------------------------------------------- |
| paymentRelatedDetailsForMobileSDKHash | payment_related_details_for_mobile_sdk | value of the `userCredentials `(You have set it in paymentParams) |
| validateVPAHash                       | validateVPA                            | VPA string of your user                                           |

5. Call the following method of the PayUAPI class to get all available payment options to “Merchant”:

```Text Swift
class func getUPIPaymentOptions(withPaymentParams params: PayUPaymentParams,
completion: @escaping(Result) ->() )
```

6. You will get a response of type Result with the value of the PayUUPIPaymentOptions type in the response success parameter. The sample code is similar to the following:

```Text Swift
PayUAPI.getUPIPaymentOptions(withPaymentParams: self.paymentParams!, completion: { [weak self] result in
     switch result {
     case .success(let paymentOptions):
         self?.availablePaymentOptions = paymentOptions
         completion(.success(true))
     case .failure(let error):
         print(error)
         completion(.failure(error))
     }
 })
```

***

## Step 4: Process Payment

With the PayUUPIPaymentOptions object received in Step 5 of Fetch Hashes, you can populate relevant UPI options on your checkout screen. As stated at the beginning of this section, you have the following options to make a payment:

- Intent
- UPI Collect
- Fallback for Google Pay

Inside intent key of the PayUUPIPaymentOptions object, you get an array of objects of the type `PayUSupportedIntentApp`. These are essentially the apps that are supported by the SDK for intent payments.

1. Query the SDK for payment options available for the “Current User” based on factors like if Bank/Payment-Service-Provider(PSP) apps are installed on the current user’s device or not using the code similar to the following:

```Text Swift
 public class func canUseIntent(forApp app: PayUSupportedIntentApp,
                withUpiOptions options: PayUUPIPaymentOptions) -> Bool
 public class func canUseUpiCollect(withPaymentOptions options: PayUUPIPaymentOptions) -> Bool
 public class func canUseGpayOmni(withPaymentOptions options: PayUUPIPaymentOptions) -> Bool
 public class func canUseGpayCollect(withPaymentOptions options: PayUUPIPaymentOptions) -> Bool
```

Based on your priority and availability of payment options for the current user, you can order the payment options on your checkout page.

> ❗️ Callout
> 
> The `canUseGpayOmni` and `canUseGpayCollect` methods provide you fallback options of the Google Pay intent app, which have approximately 10% more success rate when compared to general UPI collect payments. This implies that if your user does not have the Google Pay app installed, you can still show the Google Pay option on your checkout, and PayU will display these two fallback options upon Google Pay selection by the user. Google Pay omnichannel payment option takes the user’s phone number for UPI collect payment.

2. Create an instance of PayUIntentPaymentVC and follow data to it if the user selects the intent app option.

```Text Swift
let paymentVC = PayUIntentPaymentVC()
paymentVC.availableUpiOptions = upiOptions
paymentVC.paymentApp = app //object of type 'PayUSupportedIntentApp'
paymentVC.paymentParams = params
navigationController?.pushViewController(paymentVC, animated: false)
```

3. Create an instance of `PayCollectPaymentVC` using the following code convenience method If user selects the UPI Collect or Google Pay Fallback option:

```Text Swift
let collectVC = PayCollectPaymentVC()
```

4. Pass the following information for payment processing:

```Text Swift
collectVC.paymentParams = params
collectVC.screenType = type // .upi or .gpayFallback
collectVC.availablePaymentOptions = upiOptions
self.navigationController?.pushViewController(collectVC, animated: true)
```

After the payment is made, you should get the response in your payment completion callback defined above `PayUUPICore.shared.paymentCompletion`.

5. Add the query schemes in the `info.plist` file:

```Text XML
<key>LSApplicationQueriesSchemes</key>
<array>
<string>phonepe</string>
<string>tez</string>
<string>paytm</string>
</array>
```

***

## Make Payment through UPICore

1. **UPI Collect Flow**: Validate VPA with `paymentparam`, it will give you a callback once it has verified VPA in the completion block.

```
PayUAPI.validateVPA(withPaymentParams: <PayUPaymentParam>, completion: <(Result<PayUValidateVPAModel, PayUError>) -> ()>)
```

> ❗️ Callout
> 
> Begin payment after validating your VPA. Set up PayUPaymentResponseHandler when the payment is successfully initiated and handle the response after the payment is completed.

```
PayUAPI.getDataForUPICollectPayment(withPaymentParams: <PayUPaymentParam>, completion: <(Result<PayUPureS2SModel, PayUError>) -> ()>)
```

2. **UPI Intent Flow**: First check which intent app are in current device(Gpay, Paytm, Phonepe).
   1. **Gpay Intent Flow**: Get data using the following:

```
PayUAPI.getDataForGpayIntentPayment(withPaymentParams: <PayUPaymentParam>, completion: <(Result<PayUPureS2SModel, PayUError>) -> ()>)
```

Make payment using the below function and wait for a response.

```
PayUThirdPartyManager.makePayment(withApp: <PayUSupportedIntentApp>, withIntentModel: <PayUPureS2SModel>, appSwitchingStatus: <((Bool) -> ())((Bool) -> ())(Bool) -> ()>)
```

```
       ii. **Other Intent Flow**: Get data using the below function:
```

```
PayUAPI.getDataForIntentPayment(withPaymentParams: <PayUPaymentParam>, completion: <(Result<PayUPureS2SModel, PayUError>) -> ()>)
```

Make payment using the below function and wait for a response.

```
PayUThirdPartyManager.makePayment(withApp: <PayUSupportedIntentApp>, withIntentModel: <PayUPureS2SModel>, appSwitchingStatus: <((Bool) -> ())((Bool) -> ())(Bool) -> ()>)
```

You will get the Socket model using the`PayUPersistentStore.getSocketConnectionModel()`.