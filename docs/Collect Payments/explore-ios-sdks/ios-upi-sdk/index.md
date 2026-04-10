---
title: iOS UPI SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: iOS UPI SDK
  description: >-
    PayU's UPI SDK allows for easy integration of UPI payments in your app,
    supporting intent payments, UPI collect payments, and Google Pay fallback
    options. The SDK is API-based, quick, and does not involve a WebView in any
    payment flow.
  keywords:
    - PayU India UPI SDK
    - PayU UPI SDK
    - UPI SDK integration IOS
    - IOS UPI payment SDK
    - PayU UPI payment gateway
    - How to integrate PayU UPI SDK in IOS
    - PayU India UPI SDK for IOS apps
    - Guide to PayU UPI IOS SDK
    - PayU UPI payment gateway integration IOS
    - Step-by-step PayU UPI SDK IOS integration
  robots: index
next:
  description: ''
---
PayU's UPI SDK is a framework for integrating UPI payments in your app in an easy, efficient, and stable way. The following types of payments are currently supported:

* Intent payments* (Make UPI payments by transitioning users from your app to UPI app like Google Pay/PhonePe )

<Callout icon="📘" theme="info">
  **Note**: 'intent' as in Android, not in iOS. Using this word here due to its widespread understanding across domains.)
</Callout>

* UPI Collect Payments.
* Google Pay fallback options (If Google Pay is not installed on iOS device). It can use Google Pay registered mobile number instead of VPA for UPI collect payments.

## UPI SDK frameworks

PayU provides the following UPI modular SDKs that perform different functions related to UPI Payments:

* **PayU UPI Core SDK**: This contains all APIs, Error Codes, Response Handlers etc. With this SDK alone, you can make intent payments. If you want to make UPI Collect payments also, either you can use PayU UPI SDK (given below) to collect VPA from the user or pass Core SDK the required parameters. Core SDK contains only one UI Screen, the final loader page. On this screen, we fetch the payment response from PayU.UPI Core SDK internally uses sockets to fetch payment responses as quickly as possible.
* **PayU UPI SDK**: This contains the UI screen screens and related resources to support UPI collection payment in a hassle-free way. You might find it useful to save time in creating checkout screens for UPI Collect.

The following dependencies (automatically added if integrated via Cocoapods) are required:

* **PayU Networking**: This is used by CoreSDK to handle network requests.

## Unique features of UPI SDK

There is no WebView involved in any payment flow. Every payment flow is completely API based and super quick.
Make intent Payments on iOS just like Android. The PSP app (PhonePe/Google Pay etc.) does not automatically switches the user to your app. User manually comes back to your app)
Hassle-free integration

<Accordion title="SDK Integration Steps" icon="fa-code">
  The iOS Native OTP Assist SDK integration involves the following steps:

  <Accordion title="Step 1: Integrate Cocapods" icon="fa-code">
    Add the following lines to your Podfile:

    ```
    // make sure to add below-mentioned line to use dynamic frameworks
    use_frameworks!
    // Add this to include our SDK
    pod 'PayUIndia-UPI'
    ```

    #### Swift Package Manager Integration

    You can integrate PayUIndia-PG-SDK with your app or SDK using the following methods:

    * **Using Xcode**: Navigate to File > Add Package menu and install the following package:
      [https://github.com/payu-intrepos/payu-upi-ios-sdk](https://github.com/payu-intrepos/payu-upi-ios-sdk)
    * **Using Package.Swift**: Add the following code to Package.swift dependencies:

    ```
      .package(name: "PayUIndia-UPIKit", url: "https://github.com/payu-intrepos/payu-upi-ios-sdk", from: "6.0.0")
    ```

    ***
  </Accordion>

  <Accordion title="Step 2: Make UPI Payments" icon="fa-code">
    #### Configure Mandatory Payment Parameters

    1. Set environment to test or production. You can also set the debugging level to get logs from the SDK.

    ```swift Swift
    PayUUPICore.shared.environment = .production
    PayUUPICore.shared.logLevel = .error //Other option is verbose. Logs are disabled by default
    ```

    2. Configure mandatory payment parameters required for the payment:

    ```swift Swift
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

    <Callout icon="📘" theme="info">
      **Note**: The URLs used in **surl** and **furl** are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.
    </Callout>

    #### Configure Callbacks

    Configure Callbacks to receive actionable events from SDK:

    * **paymentCompletion**: You receive the payment response here.

    ```swift Swift
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

    * **backPressed**: If the user has not yet initiated the transaction, and when the user presses the back button from the UPI payment options page, this callback is triggered. You can dismiss SDK's UI screen here.

    ```swift Swift
    PayUUPICore.shared.backPressed = {[weak self] in
    self?.navigationController?.popToRootViewController(animated: true)
    }
    ```

    * **onEnteringVPA**: For validating the VPA entered by the user, we need to hit PayU's validate VPA API. This API needs a hash. In this callback, you will get the VPA entered by the user. Use this value to generate the required hash. When the hash is received from your server, send us the updated post params with the new hash.

    ```swift Swift
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

    #### Fetch Hashes

    To fetch hashes and save them in the `paymentParams` object:

    1. Configure the hashes property in paymentParams. Hashes authenticates that API request originates from the original source to avoid a "Man-in-the-middle attack." Property hashes are of the PayUHashes type.
    2. Define the following PayUHashes properties used for a distinct API call.
       1. `paymentRelatedDetailsForMobileSDKHash`: This is required to get available UPI payment options from which payment can be made.
       2. `paymentHash`: This is required to create transactions at PayU's end.
       3. `validateVPAHash`: This is required by `validateVPA` API in UPI collect flow to check if provided VPA is registered with a bank account and is active or not. Not required in intent transactions.
    3. Provide the first two hashes before asking SDK to initiate the payment. Hashes must be generated only on your server as it needs a secret key (also known as salt). Your app must never contain salt.
    4. Command and var1 values for generating `paymentRelatedDetailsForMobileSDKHash` & `validateVPAHash` are described in the following table. For generating hashes on your server, refer to [Hash Generation](https://docs.payu.in/docs/set-up-the-payment-hashes/).

    | Hash for Parameter                    | Command                                     | Var1                                                              |
    | :------------------------------------ | :------------------------------------------ | :---------------------------------------------------------------- |
    | paymentRelatedDetailsForMobileSDKHash | payment\_related\_details\_for\_mobile\_sdk | value of the `userCredentials `(You have set it in paymentParams) |
    | validateVPAHash                       | validateVPA                                 | VPA string of your user                                           |

    5. Call the following method of the PayUAPI class to get all available payment options to "Merchant":

    ```swift Swift
    class func getUPIPaymentOptions(withPaymentParams params: PayUPaymentParams,
    completion: @escaping(Result) ->() )
    ```

    6. You will get a response of type Result with the value of the PayUUPIPaymentOptions type in the response success parameter. The sample code is similar to the following:

    ```swift Swift
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
  </Accordion>

  <Accordion title="Step 3: Process Payment" icon="fa-code">
    With the PayUUPIPaymentOptions object received in Step 5 of Fetch Hashes, you can populate relevant UPI options on your checkout screen. As stated at the beginning of this section, you have the following options to make a payment:

    * Intent
    * UPI Collect
    * Fallback for Google Pay

    Inside intent key of the PayUUPIPaymentOptions object, you get an array of objects of the type `PayUSupportedIntentApp`. These are essentially the apps that are supported by the SDK for intent payments.

    1. Query the SDK for payment options available for the "Current User" based on factors like if Bank/Payment-Service-Provider(PSP) apps are installed on the current user's device or not using the code similar to the following:

    ```swift Swift
     public class func canUseIntent(forApp app: PayUSupportedIntentApp,
                    withUpiOptions options: PayUUPIPaymentOptions) -> Bool
     public class func canUseUpiCollect(withPaymentOptions options: PayUUPIPaymentOptions) -> Bool
     public class func canUseGpayOmni(withPaymentOptions options: PayUUPIPaymentOptions) -> Bool
     public class func canUseGpayCollect(withPaymentOptions options: PayUUPIPaymentOptions) -> Bool
    ```

    Based on your priority and availability of payment options for the current user, you can order the payment options on your checkout page.

    <Callout icon="📘" theme="info">
      **Note**: The `canUseGpayOmni` and `canUseGpayCollect` methods provide you fallback options of the Google Pay intent app, which have approximately 10% more success rate when compared to general UPI collect payments. This implies that if your user does not have the Google Pay app installed, you can still show the Google Pay option on your checkout, and PayU will display these two fallback options upon Google Pay selection by the user. Google Pay omnichannel payment option takes the user's phone number for UPI collect payment.
    </Callout>

    2. Create an instance of PayUIntentPaymentVC and follow data to it if the user selects the intent app option.

    ```swift Swift
    let paymentVC = PayUIntentPaymentVC()
    paymentVC.availableUpiOptions = upiOptions
    paymentVC.paymentApp = app //object of type 'PayUSupportedIntentApp'
    paymentVC.paymentParams = params
    navigationController?.pushViewController(paymentVC, animated: false)
    ```

    3. Create an instance of `PayCollectPaymentVC` using the following code convenience method If user selects the UPI Collect or Google Pay Fallback option:

    ```swift Swift
    let collectVC = PayCollectPaymentVC()
    ```

    4. Pass the following information for payment processing:

    ```swift Swift
    collectVC.paymentParams = params
    collectVC.screenType = type // .upi or .gpayFallback
    collectVC.availablePaymentOptions = upiOptions
    self.navigationController?.pushViewController(collectVC, animated: true)
    ```

    After the payment is made, you should get the response in your payment completion callback defined above `PayUUPICore.shared.paymentCompletion`.

    5. Add the query schemes in the `info.plist` file:

    ```xml XML
    <key>LSApplicationQueriesSchemes</key>
    <array>
    <string>phonepe</string>
    <string>tez</string>
    <string>paytm</string>
    </array>
    ```

    ***

    <Accordion title="Make Payment through UPICore" icon="fa-code">
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
    </Accordion>
  </Accordion>
</Accordion>

<Accordion title="Test the Integration and Go-live" icon="fa-code">
  <IOS_Test_the_Integration />

  <IOS_Go_Live />
</Accordion>
