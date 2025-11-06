---
title: Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integration Steps - iOS Checkout Pro SDK
  description: >-
    The iOS Checkout Pro SDK integration involves following specific steps for
    integration, testing, and a go-live checklist, with additional guidance on
    generating a dynamic hash.
  keywords:
    - Integration Steps for iOS Checkout Pro SDK
    - ' iOS Checkout Pro SDK Integration Steps'
    - ' Checkout Pro SDK Integration for Mobile iOS'
  robots: index
next:
  description: ''
---
The iOS Checkout Pro SDK integration involves the following steps:

## SDK Integration

Prerequisite: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

<Accordion title="Step 1: Set up pod" icon="fa-code">
  The CheckoutPro SDK is offered through CocoaPods. To add the SDK in your app project:

  Include the SDK framework in your podfile.

  ```
  // make sure to add below-mentioned line to use dynamic frameworks
  use_frameworks!
  // Add this to include our SDK
  pod 'PayUIndia-CheckoutPro' 
  ```

  * Install dependency using the pod install command in terminal
  * Add the following imports in the class where you need to initiate a payment.

  ```swift Swift
  import PayUCheckoutProKit
  import PayUCheckoutProBaseKit
  import PayUParamsKit
  ```
  ```objectivec Objective-C
  #import <PayUCheckoutProKit/PayUCheckoutProKit.h>
  #import <PayUCheckoutProBaseKit/PayUCheckoutProBaseKit.h>
  #import <PayUBizCoreKit/PayUBizCoreKit.h>
  #import <PayUParamsKit/PayUParamsKit.h>
  ```

  * Refer to the following Test the key and salt environments:
    * **Production**: [Generate Production Merchant Key and Salt](https://onboarding.payu.in/app/account/signup)
    * **Test**: [Generate Test Merchant Key and Salt](https://uat-onepayuonboarding.payu.in/app/account/signup)

  <Accordion title="Swift Package Manager Integration" icon="fa-code">
    You can integrate PayUIndia-Checkoutpro with your app or SDK using the following methods:

    * Using Xcode: Navigate to File > Add Package menu and add the following package:
      [https://github.com/payu-intrepos/PayUCheckoutPro-iOS](https://github.com/payu-intrepos/PayUCheckoutPro-iOS)
    * Using Package.Swift: Add the following line in the Package.swift dependencies: `.package(name: "PayUCheckoutProKit", url: "https://github.com/payu-intrepos/PayUCheckoutPro-iOS", from: "7.4.0")`
  </Accordion>

  <Accordion title="CrashReporter" icon="fa-code">
    In order to receive all the crashes related to our SDKs, add the following line to your AppDelegate `didFinishLaunchingWithOptions` method:

    ```swift Swift
    PayUCheckoutPro.start()
    ```
    ```objectivec Objective-C
    [PayUCheckoutPro start];
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 2: Build the payment parameters (mandatory step)" icon="fa-code">
  <Accordion title="Step 2.1: Basic Integration" icon="fa-code">
    PayU SDK needs certain inputs from the merchant app to authenticate and initiate a transaction.

    ```Text Swift
    let paymentParam = PayUPaymentParam(key: <String>,
                                        transactionId: <String>,
                                        amount: <String>,
                                        productInfo: <String>,
                                        firstName: <String>,
                                        email: <String>,
                                        phone: <String>,
                                        surl: <String>,//Pass your own surl
                                        furl: <String>,//Pass your own furl
                                        environment: <Environment> /*.production or .test*/)
                                        
    paymentParam.userCredential = <String> // For saving and fetching user’s saved card
    ```
    ```Text Onjective-C
    PayUPaymentParam *paymentParam = [[PayUPaymentParam alloc] initWithKey:<#(NSString * _Nonnull)#>
                                                             transactionId:<#(NSString * _Nonnull)#>
                                                                    amount:<#(NSString * _Nonnull)#>
                                                               productInfo:<#(NSString * _Nonnull)#>
                                                                 firstName:<#(NSString * _Nonnull)#>
                                                                     email:<#(NSString * _Nonnull)#>
                                                                     phone:<#(NSString * _Nonnull)#>
                                                                      surl:<#(NSString * _Nonnull)#>
                                                                      furl:<#(NSString * _Nonnull)#>
                                                               environment:<#(enum Environment)#> /*EnvironmentProduction or EnvironmentTest*/];

    paymentParam.userCredential = <#(NSString)#>; // For saving and fetching use saved card
    ```

    > 📘 Notes:
    >
    > * The URL used in **surl** and **furl** are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed.
    > * Kindly refer the below to[Generate own SURL/FURL](https://docs.payu.in/docs/handling-redirect-surlfurl-urls-with-ios)
    > * The **TransactionId** parameter cannot have a special character and not more than 25 characters.

    <Accordion title="Mandatory parameters" icon="fa-code">
      Use the following table to pass the mandatory parameters in the PayU SDK:

      | Parameter                                                              | Description                                                                                                                                            | Required |
      | :--------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
      | key                                                                    | Merchant Key provided by PayU during onboarding.                                                                                                       | Yes      |
      | transactionId                                                          | A unique ID passed by the merchant for each transaction.                                                                                               | Yes      |
      | amount                                                                 | The transaction amount.                                                                                                                                | Yes      |
      | productInfo                                                            | A brief description of the product.                                                                                                                    | Yes      |
      | firstName                                                              | Customer's first name.                                                                                                                                 | Yes      |
      | email                                                                  | Customer's email address.                                                                                                                              | Yes      |
      | phone                                                                  | Customer's phone number.                                                                                                                               | Yes      |
      | surl                                                                   | Success URL - where the customer is redirected after a successful payment                                                                              | Yes      |
      | furl                                                                   | Failure URL - where the customer is redirected after an unsuccessful/failed payment                                                                    | Yes      |
      | environment                                                            | The environment in which the transaction is initiated. For TEST transactions, use PayUTestEnvironment. For LIVE transactions, use PayUProdEnvironment. | Yes      |
      | The code block for passing the parameters is similar to the following: |                                                                                                                                                        |          |

      If you required any value in the response then pass the below value

      ```Text Swift
      paymentParam.additionalParam[PaymentParamConstant.udf1] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf2] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf3] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf4] = <String>
      paymentParam.additionalParam[PaymentParamConstant.udf5] = <String>
      paymentParam.additionalParam[PaymentParamConstant.walletURN] = <String>  // Required for Amul Wallet
      ```
      ```Text Objective-C
      paymentParam.additionalParam = [[NSDictionary alloc] initWithObjectsAndKeys:
                                          <#(NSString)#>, PaymentParamConstant.udf1,
                                          <#(NSString)#>, PaymentParamConstant.udf2,
                                          <#(NSString)#>, PaymentParamConstant.udf3,
                                          <#(NSString)#>, PaymentParamConstant.udf4,
                                          <#(NSString)#>, PaymentParamConstant.udf5,
                                          <#(NSString)#>, PaymentParamConstant.walletURN,
                                          nil];
      ```
    </Accordion>
  </Accordion>

  <Accordion title="Step 2.2:For Recurring Payments(SI) (Optional)" icon="fa-code">
    For setting up Standing Instructions (SI) or recurring payments, you can refer to the [Recurring Payments Documentation](doc:ios-recurring-payments-si).

    Use the following sample code:

    ```Text Swift
     let siInfo = PayUSIParams(billingAmount: <String>,
                               paymentStartDate: <Date>,
                               paymentEndDate: <Date>,
                               billingCycle: <PayUBillingCycle>,
                               billingInterval: <NSNumber>)

                siInfo.billingLimit = <PayuBillingLimit>
                siInfo.billingRule = <PayuBillingRule>
                
                paymentParam.siParam = siInfo
    ```
    ```Text Onjective-C
    paymentParam.siParams = siParam;
    ```
  </Accordion>

  <Accordion title="Step 2.3:For UPI One Time Mandate Payments (Optional)" icon="fa-code">
    For UPI One Time Mandate (OTM) payments, use the following parameters:

    ```Text Swift
     let siInfo = PayUSIParams(billingAmount: <String>,
                               paymentStartDate: <Date>,
                               isPreAuthTxn:<Bool>)
                
                paymentParam.siParam = siInfo
     #isPreAuthTxn must be true for OTM transactions
    ```
    ```Text Onjective-C
    paymentParam.siParams = siParam;
    ```
  </Accordion>

  <Accordion title="Step 2.4: For Split Payments details (Optional)" icon="fa-code">
    Split payments allow you to distribute the payment amount between a parent merchant and sub-merchants.

    <Accordion title="JSON request structure of splitInfo field" icon="fa-code">
      ```json
      {
        "type": "absolute",
        "splitInfo": {
          "merchant_05Apr16_126800": {
            "aggregatorSubTxnId": "aggregatorSubTxnId1",
            "aggregatorSubAmt": "50"
          },
          "merchant_05Apr16_780908": {
            "aggregatorSubTxnId": "aggregatorSubTxnId2", 
            "aggregatorSubAmt": "30"
          }
        }
      }
      ```

      Example implementation:

      ```Text Swift
      paymentParam.splitPaymentDetails = ""
      ```
      ```Text Objective-C
      paymentParam.splitPaymentDetails = @"";
      ```
    </Accordion>

    <Accordion title="Step 2.5:For Additional Charges" icon="fa-code">
      Additional charges can be applied to transactions:

      ```Text Swift
      paymentParam.additionalCharges = "CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55"
      paymentParam.percentageAdditionalCharges = "CC:50,SBIB:100,DINR:100,DC:25,NB:50"
      ```
      ```Text Objective-C
      paymentParam.additionalCharges = @"CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55";
      paymentParam.percentageAdditionalCharges = @"CC:50,SBIB:100,DINR:100,DC:25,NB:50";
      ```
    </Accordion>
  </Accordion>
</Accordion>

<Accordion title="Step 3: Generate the hash" icon="fa-code">
  This integration requires dynamic hashes. You must get hash string in map again `HashConstant.hashString` key in `generateHash`.  You need to send this string to server and append salt there, after appending salt convert string to sha512 hash and return back to SDK.

  ```swift
  /// Use this function to provide hashes
  /// - Parameters:
  ///   - param: Dictionary that contains key as HashConstant.hashName & HashConstant.hashString
  ///   - onCompletion: Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
  func generateHash(for param: DictOfString, onCompletion: @escaping PayUHashGenerationCompletion) {
      // Send this string to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashStringWithoutSalt = param[HashConstant.hashString] ?? ""
      // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashName = param[HashConstant.hashName] ?? ""

      // Set the hash in below string which is fetched from your server
      let hashFetchedFromServer = <#T##String#>
      
      onCompletion([hashName : hashFetchedFromServer])
  }
  ```
</Accordion>

<Accordion title="Step 4: Initiate the payment" icon="fa-code">
  After setting up the payment parameters and hashes, initiate the payment:

  ```Text Swift
  PayUCheckoutPro.open(on: self, paymentParam: paymentParam, config: <PayUCheckoutProConfig>, delegate: self)
  ```
  ```Text Objective-C
  [PayUCheckoutPro openOn:self paymentParam:paymentParam config:<#(PayUCheckoutProConfig * _Nullable)#> delegate:self];
  ```
</Accordion>

<Accordion title="Step 5: Handle the payment completion" icon="fa-code">
  Handle the response when the payment is completed:
  Confirm to PayUCheckoutProDelegate and use these functions to get appropriate callbacks from the SDK:

  ```Text Swift
  /// This function is called when we successfully process the payment
  /// - Parameter response: success response
  func onPaymentSuccess(response: Any?) {
      
  }

  /// This function is called when we get failure while processing the payment
  /// - Parameter response: failure response
  func onPaymentFailure(response: Any?) {
      
  }

  /// This function is called when the user cancel’s the transaction
  /// - Parameter isTxnInitiated: tells whether payment cancelled after reaching bankPage
  func onPaymentCancel(isTxnInitiated: Bool) {
      
  }

  /// This function is called when we encounter some error while fetching payment options or there is some validation error
  /// - Parameter error: This contains error information
  func onError(_ error: Error?) {
      
  }

  /// Use this function to provide hashes
  /// - Parameters:
  ///   - param: Dictionary that contains key as HashConstant.hashName & HashConstant.hashString
  ///   - onCompletion: Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
  func generateHash(for param: DictOfString, onCompletion: @escaping PayUHashGenerationCompletion) {
      // Send this string to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashStringWithoutSalt = param[HashConstant.hashString] ?? ""
      // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      let hashName = param[HashConstant.hashName] ?? ""
      let postSalt = param[HashConstant.postSalt] ?? "" //// compulsory for Additional Charges and Split Payment
      // Set the hash in below string which is fetched from your server
  		//  "<create SHA -512 hash of 'hashString+salt+postSalt'>" 
      let hashFetchedFromServer = <#T##String#>
      
      onCompletion([hashName : hashFetchedFromServer])
  }
  ```
  ```Text Objective-C
  /// This function is called when we successfully process the payment
  /// @param response  success response
  - (void)onPaymentSuccessWithResponse:(id _Nullable)response {
      
  }

  /// This function is called when we get failure while processing the payment
  /// @param response failure response
  - (void)onPaymentFailureWithResponse:(id _Nullable)response {
      
  }

  /// This function is called when the user cancel’s the transaction
  /// @param isTxnInitiated tells whether payment cancelled after reaching bankPage
  - (void)onPaymentCancelWithIsTxnInitiated:(BOOL)isTxnInitiated {
      
  }

  /// This function is called when we encounter some error while fetching payment options or there is some validation error
  /// @param error This contains error information
  - (void)onError:(NSError * _Nullable)error {
      
  }

  /// Use this function to provide hashes
  /// @param param NSDictionary that contains key as HashConstant.hashName & HashConstant.hashString
  /// @param onCompletion Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
  - (void)generateHashFor:(NSDictionary<NSString *, NSString *> * _Nonnull)param onCompletion:(void (^ _Nonnull)(NSDictionary<NSString *, NSString *> * _Nonnull))onCompletion {
      // Send below string hashStringWithoutSalt to your backend and append the salt at the end and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      NSString *hashStringWithoutSalt = [param objectForKey:HashConstant.hashString];
      // Or you can send below string hashName to your backend and send the sha512 back to us, do not calculate the hash at your client side, for security is reasons, hash has to be calculated at the server side
      NSString * hashName = [param objectForKey:HashConstant.hashName];
      
      // Set the hash in below string which is fetched from your server
      NSString *hashFetchedFromServer = <#(NSString)#>;
      
      NSDictionary *hashResponseDict = [NSDictionary dictionaryWithObjectsAndKeys:hashFetchedFromServer, hashName, nil];
      onCompletion(hashResponseDict);
  }
  ```

  <Accordion title="UPI Intent (Optional)" icon="fa-code">
    Currently, PayU supports only PhonePe and GooglePay through Intent. Add the query schemes in the`info.plist`:

    ```Text Info.plist Code for Intent
    	<key>LSApplicationQueriesSchemes</key>
    	<array>
    		<string>phonepe</string>
    		<string>tez</string>
    		<string>paytm</string>
    		<string>bhim</string>
    		<string>credpay</string>
    	</array>
    ```

    # Sample Responses

    > 🚧 Watch Out
    >
    > * In case of UPI intent/Collect flow, you will not receive a callback response in surl or furl. In this case, the format of PayU response received will be different from other payment options that you need to handle at your end.
    > * Consider the **mihpayid** in the PayU response as **PayU ID/ID**
  </Accordion>

  <Accordion title="Card/NB/Wallet and other transactions" icon="fa-code">
    ```Text Success
    {
      "id": 403993715526319631,
      "mode": "CC",
      "status": "success",
      "unmappedstatus": "captured",
      "key": "gtKFFx",
      "txnid": "iOS220530192146",
      "transaction_fee": "1.00",
      "amount": "1.00",
      "cardCategory": "domestic",
      "discount": "0.00",
      "addedon": "2022-05-30 19:22:39",
      "productinfo": "Nokia",
      "firstname": "Umang",
      "email": "umang@arya.com",
      "phone": "9876543210",
      "udf1": "udf11",
      "udf2": "udf22",
      "udf3": "udf33",
      "udf4": "udf44",
      "udf5": "udf55",
      "hash": "35e9b2f143abb2bcfbbe5e1b3fb7d95a8a2fad3b8e0fc2d737aa087b52a2f620847048e2794bfcfd06708e8095428314268a88867fffa30430275c496dc70847",
      "field1": "718984",
      "field2": "617544",
      "field3": "20220530",
      "field4": "0",
      "field5": "172989726099",
      "field6": "00",
      "field7": "AUTHPOSITIVE",
      "field8": "Approved or completed successfully",
      "field9": "No Error",
      "payment_source": "payu",
      "PG_TYPE": "CC-PG",
      "bank_ref_no": "718984",
      "ibibo_code": "MASTCC",
      "error_code": "E000",
      "Error_Message": "No Error",
      "offer_key": "CardsOfferKey@11311",
      "offer_failure_reason": "Invalid Offer Key.",
      "name_on_card": "PayUUser",
      "card_no": "512345XXXXXX2346",
      "issuing_bank": "HDFC",
      "card_type": "MAST",
      "is_seamless": 2,
      "surl": "https://payu.herokuapp.com/ios_success",
      "furl": "https://payu.herokuapp.com/ios_failure"
    }
    ```
    ```Text Failure
    {
      "id": 403993715530851078,
      "mode": "CC",
      "status": "failure",
      "unmappedstatus": "failed",
      "key": "gtKFFx",
      "txnid": "iOS240117182325",
      "transaction_fee": "1.00",
      "amount": "1.00",
      "cardCategory": "domestic",
      "discount": "0.00",
      "addedon": "2024-01-17 18:23:43",
      "productinfo": "Nokia",
      "firstname": "Umang",
      "email": "umang@arya.com",
      "phone": "9999999999",
      "udf1": "udf11",
      "udf2": "udf22",
      "udf3": "udf33",
      "udf4": "udf44",
      "udf5": "udf55",
      "hash": "0503b628ba7fe4716a7a96ac6b2c668634200419416af887766a417f3fc048200b155b04ccd3f4f5f601f5a22c3fb3af571773499605ee0446c98fe541b089f9",
      "field1": 793583808525231700,
      "field2": 833617,
      "field5": "63",
      "field6": "02",
      "field7": "AUTHNEGATIVE",
      "field9": "Bank was unable to authenticate.",
      "payment_source": "payu",
      "PG_TYPE": "CC-PG",
      "bank_ref_no": 793583808525231700,
      "ibibo_code": "CC",
      "error_code": "E308",
      "Error_Message": "Transaction Failed at bank end.",
      "card_no": "XXXXXXXXXXXX2346",
      "issuing_bank": "AXIS",
      "card_type": "MAST",
      "is_seamless": 2,
      "surl": "https://cbjs.payu.in/sdk/success",
      "furl": "https://cbjs.payu.in/sdk/failure"
    }
    ```
  </Accordion>

  <Accordion title="UPI Collect/Intent payments" icon="fa-code">
    ```Text Success
    {
      "txnid": "iOS240117183850",
      "address1": "",
      "udf1": "udf11",
      "furl": "https://cbjs.payu.in/sdk/failure",
      "address2": "",
      "field6": "NA!NA!NA!NA",
      "lastname": "",
      "zipcode": "",
      "status": "success",
      "offer_key": null,
      "udf5": "udf55",
      "city": "",
      "udf9": "",
      "field2": "87768967657",
      "udf4": "udf44",
      "field7": "APPROVED OR COMPLETED SUCCESSFULLY|00",
      "addedon": "2024-01-17 18:39:13",
      "state": "",
      "field0": "",
      "udf6": "",
      "card_no": "",
      "discount": "0.00",
      "udf10": "",
      "hash": "44161a41207d4bc29ad802ecd6e06f0b350930fa539675bdd24ba8321e22972d2d12fee84a02af549717a5e52fd93db56be5f1c89388eaf2a2740b20491f8bac",
      "field4": "",
      "mode": "UPI",
      "bank_ref_num": "401789868507",
      "field9": "SUCCESS|Completed Using Callback",
      "offer_availed": null,
      "udf3": "udf33",
      "payment_source": "payuPureS2S",
      "key": "smsplus",
      "productinfo": "Nokia",
      "field1": "",
      "bank_ref_no": "401789868507",
      "mihpayid": 18978067105,
      "field8": "Phone Pe",
      "country": "",
      "curl": "https://cbjs.payu.in/sdk/failure",
      "bankcode": "INTENT",
      "udf2": "udf22",
      "field3": "8700908382@ybl",
      "phone": "9999999999",
      "email": "umang@arya.com",
      "net_amount_debit": 1,
      "amount": "1.00",
      "firstname": "Umang",
      "field5": "PPPL18978067105170124183913",
      "card_token": "",
      "unmappedstatus": "captured",
      "surl": "https://cbjs.payu.in/sdk/success",
      "udf8": "",
      "error": "E000",
      "error_Message": "No Error",
      "udf7": "",
      "PG_TYPE": "UPI-PG"
    }
    ```
    ```Text Failure
    {
      "address2": "",
      "field0": "",
      "field1": "",
      "udf9": "",
      "udf1": "udf11",
      "hash": "f995befdf65dacf0b71db83a94776efe9154ab9f0c5a378f4f07821fd61088a6f0a9cedbbf273df9048df64c4a4adb071701e9b2136e0b3e60f3c30e21aaa1ca",
      "txnid": "iOS220706164103",
      "field3": "",
      "mode": "UPI",
      "field5": "",
      "surl": "https://payu.herokuapp.com/ios_success",
      "udf7": "",
      "bankcode": "TEZ",
      "amount": "1.00",
      "udf5": "udf55",
      "additionalCharges": "0.59",
      "bank_ref_no": null,
      "payment_source": "payuPureS2S",
      "zipcode": "",
      "firstname": "Umang",
      "lastname": "",
      "net_amount_debit": 0,
      "productinfo": "Nokia",
      "city": "",
      "udf2": "udf22",
      "mihpayid": 15463188898,
      "email": "umang@arya.com",
      "field4": "",
      "state": "",
      "phone": "9876543210",
      "furl": "https://payu.herokuapp.com/ios_failure",
      "curl": "https://payu.herokuapp.com/ios_failure",
      "card_token": "",
      "PG_TYPE": "UPI-PG",
      "field6": "",
      "addedon": "2022-07-06 16:41:28",
      "udf6": "",
      "udf8": "",
      "bank_ref_num": null,
      "field7": "",
      "udf10": "",
      "error": "E308",
      "field2": "",
      "udf3": "udf33",
      "card_no": "",
      "field9": "P|PENDING|Completed Using Verify API",
      "field8": "INTENT",
      "unmappedstatus": "failed",
      "key": "3TnMpV",
      "udf4": "udf44",
      "country": "",
      "status": "failure",
      "address1": "",
      "error_Message": "Transaction Failed at bank end."
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 6: Custom Note Integration" icon="fa-info-circle">
  This section describes how to integrate custom notes in PayUCheckoutPro SDK.

  <Accordion title="Create a Custom Note List and Pass to SDK" icon="fa-info-circle">
    Create a list of custom notes that you want to pass to the CheckoutPro SDK. For each custom note, custom_note and custom_note_category need to be passed.To pass the custom note list, Create a PayUCheckoutProConfig object and set the CustomNoteDetails similar to the following code block:

    ```swift Swift
    var customNotes = [PayUCustomNote]()
    let customNote1 = PayUCustomNote()
    customNote.note = “<your note message>”
    customNote.noteCategories =  [] // Empty to show notes on L1 screen
    customNotes.append(customNote)

    let customNote2 = PayUCustomNote()
    customNote.note = “<your note message>”
    customNote.noteCategories =  [PaymentType.ccdc, PaymentType.NB, PaymentType.wallet, PaymentType.emi, PaymentType.savedCard, PaymentType.sodexo, PaymentType.upi, PaymentType.neftRtgs] 
// pass Payment type to show notes on specific payment mode screen
    customNotes.append(customNote)

    // Initialize the PayU CheckoutPro Configuration
    let config = PayUCheckoutProConfig()

    // Assign the custom notes to the config
    config.customNotes = customNotes

    ```
  </Accordion>
</Accordion>

## Test the integration and Go-Live

<IOS_Test_the_Integration />

<IOS_Go_Live />
