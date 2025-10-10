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

      | Parameter     | Description                                                                                                                                            | Required |
      | :------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------- | :------- |
      | key           | Merchant Key provided by PayU during onboarding.                                                                                                       | Yes      |
      | transactionId | A unique ID passed by the merchant for each transaction.                                                                                               | Yes      |
      | amount        | The transaction amount.                                                                                                                                | Yes      |
      | productInfo   | A brief description of the product.                                                                                                                    | Yes      |
      | firstName     | Customer's first name.                                                                                                                                 | Yes      |
      | email         | Customer's email address.                                                                                                                              | Yes      |
      | phone         | Customer's phone number.                                                                                                                               | Yes      |
      | surl          | Success URL - where the customer is redirected after a successful payment                                                                              | Yes      |
      | furl          | Failure URL - where the customer is redirected after an unsuccessful/failed payment                                                                    | Yes      |
      | environment   | The environment in which the transaction is initiated. For TEST transactions, use PayUTestEnvironment. For LIVE transactions, use PayUProdEnvironment. | Yes      |
The code block for passing the parameters is similar to the following:

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

    <Accordion title="Step 2.4:For Additional Charges" icon="fa-code">
      Additional charges can be applied to transactions:

      ```swift Swift
      let payUPaymentParams = PayUPaymentParamsBuilder()
          .setKey("MERCHANT_KEY")
          .setTransactionId("TRANSACTION_ID")  
          .setAmount("100")
          .setProductInfo("PRODUCT_INFO")
          .setFirstName("FIRSTNAME")
          .setEmail("EMAIL")
          .setPhone("1234567890")
          .setSurl("SUCCESS_URL")
          .setFurl("FAILURE_URL")
          .setEnvironment(PayUTestEnvironment)
          .setAdditionalCharges("ADDITIONAL_CHARGES_JSON")
          .build()
      ```
    </Accordion>
  </Accordion>
</Accordion>

<Accordion title="Step 3: Set up the payment hashes" icon="fa-code">
  PayU uses hashes to ensure the integrity and security of the transaction.

  <Accordion title="Getting Hash Data to calculate hash" icon="fa-code">
    In order to authenticate a payment request and to ensure the data security of the payment request, PayU requires hash values to be calculated.

    ```swift Swift
    func generateHash(_ param: DictOfString, onCompletion: @escaping PayUHashGenerationCompletionBlock) {
        // Process the param dictionary and calculate hashes on your backend server
        // Return the calculated hashes
        let hashes = ["hash_key": "calculated_hash_value"]
        onCompletion(hashes)
    }
    ```
  </Accordion>

  <Accordion title="Passing generated hash to SDK" icon="fa-code">
    Once you have the hash values, pass them to the SDK:

    ```swift Swift
    PayUCheckoutPro.open(payUPaymentParams, 
                        payUConfig: payUConfig, 
                        parentVC: self, 
                        hashGenerationCompletionBlock: generateHash, 
                        paymentCompletionBlock: paymentCompletionBlock)
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 4: Initiate the payment" icon="fa-code">
  After setting up the payment parameters and hashes, initiate the payment:

  ```swift Swift
  PayUCheckoutPro.open(payUPaymentParams, 
                      payUConfig: payUConfig, 
                      parentVC: self, 
                      hashGenerationCompletionBlock: generateHash, 
                      paymentCompletionBlock: paymentCompletionBlock)
  ```
  ```objectivec Objective-C
  [PayUCheckoutPro open:payUPaymentParams 
              payUConfig:payUConfig 
                parentVC:self 
  hashGenerationCompletionBlock:generateHash 
     paymentCompletionBlock:paymentCompletionBlock];
  ```
</Accordion>

<Accordion title="Step 5: Handle the payment completion" icon="fa-code">
  Handle the response when the payment is completed:

  <Accordion title="Sample Responses" icon="fa-code">
    **Successful Payment Response:**

    ```json
    {
      "result": {
        "payuResponse": "response_data",
        "merchantResponse": "merchant_response_data"
      },
      "status": "success"
    }
    ```

    **Failed Payment Response:**

    ```json
    {
      "result": {
        "payuResponse": "response_data", 
        "merchantResponse": "merchant_response_data"
      },
      "status": "failure"
    }
    ```

    **Cancelled Payment Response:**

    ```json
    {
      "result": "Transaction was cancelled by user",
      "status": "user_cancelled"
    }
    ```
  </Accordion>
</Accordion>

<Accordion title="UPI Intent (Optional)" icon="fa-code">
  For UPI Intent functionality:

  ```swift Swift
  let payUConfig = PayUConfigBuilder()
      .setPaymentModesOrder([PayUPaymentModeConfig.upi()])
      .setShouldShowPaymentModes(false)
      .build()
  ```
</Accordion>

## Test the Integration

<Accordion title="Card/NB/Wallet and other transactions" icon="fa-code">
  For testing various payment methods, use the following test credentials:

  **Test Credit Cards:**

  * **Visa**: 4444333322221111
  * **MasterCard**: 5123456789012346
  * **Maestro**: 5081597022059105

  **Test Debit Cards:**

  * **Visa**: 4000111122223331
  * **MasterCard**: 5123456789012346

  All test cards use:

  * **CVV**: Any 3 digit number
  * **Expiry Date**: Any future date
</Accordion>

<Accordion title="UPI Collect/Intent payments" icon="fa-code">
  For testing UPI payments:

  **Test VPA**: `success@payu`

  This VPA will simulate a successful UPI transaction for testing purposes.
</Accordion>

<Accordion title="Distributing your app (App Store / Ad-hoc)" icon="fa-code">
  When distributing your app, ensure:

  1. Use production keys for live transactions
  2. Test thoroughly with production credentials
  3. Follow App Store guidelines for payment apps
  4. Ensure all required permissions are in place
</Accordion>

<Accordion title="Additional integration" icon="fa-code">
  <Accordion title="Step 1: Create a Custom Note list" icon="fa-code">
    You can create custom notes for transactions:

    ```swift Swift
    let customNoteDetails = PayUCustomNoteDetailsBuilder()
        .setCustomNote("Custom transaction note")
        .setCustomNoteCategory("CATEGORY")
        .build()
    ```
  </Accordion>

  <Accordion title="Step 2: Pass the Custom Note list to SDK" icon="fa-code">
    Pass the custom notes to the payment parameters:

    ```swift Swift
    let payUPaymentParams = PayUPaymentParamsBuilder()
        .setKey("MERCHANT_KEY")
        .setTransactionId("TRANSACTION_ID")
        // ... other parameters
        .setCustomNoteDetails([customNoteDetails])
        .build()
    ```
  </Accordion>
</Accordion>

<Accordion title="Test credentials for supported payment methods" icon="fa-code">
  <Accordion title="Test cards for EMI" icon="fa-code">
    For testing EMI transactions:

    **EMI Test Cards:**

    * **HDFC**: 4444333322221111
    * **ICICI**: 5123456789012346
    * **SBI**: 4000111122223331

    All EMI test cards use:

    * **CVV**: 123
    * **Expiry**: 12/25
  </Accordion>

  <Accordion title="Test credentials for Net Banking" icon="fa-code">
    **Net Banking Test Credentials:**

    * **SBI**: Use any valid account number
    * **HDFC**: Use any valid customer ID
    * **ICICI**: Use any valid user ID
    * **Axis**: Use any valid user ID

    For all banks, use any password for testing.
  </Accordion>

  <Accordion title="Test VPA for UPI" icon="fa-code">
    **UPI Test VPAs:**

    * Success: `success@payu`
    * Failure: `failure@payu`
    * Pending: `pending@payu`
  </Accordion>

  <Accordion title="Test wallets" icon="fa-code">
    **Wallet Test Credentials:**

    * **Paytm**: Use mobile number 7777777777
    * **PhonePe**: Use mobile number 9999999999
    * **Amazon Pay**: Use mobile number 8888888888

    Use OTP: 123456 for all wallet testing.
  </Accordion>
</Accordion>

## Go-live Checklist

<Accordion title="Collect Live Payments" icon="fa-code">
  Before going live, ensure you have:

  1. **Production Merchant Key and Salt**
  2. **KYC Completed**
  3. **Live Testing Done**
  4. **Error Handling Implemented**
  5. **Security Best Practices Followed**
</Accordion>

<Accordion title="Checklist 2: Configure environment" icon="fa-code">
  Set the environment to production:

  ```swift Swift
  .setEnvironment(PayUProdEnvironment)
  ```

  Ensure all production URLs and keys are correctly configured.
</Accordion>

<Accordion title="Checklist 3: Configure your SURL/FURL" icon="fa-code">
  Set up your production Success URL (SURL) and Failure URL (FURL):

  * **SURL**: Where users are redirected after successful payment
  * **FURL**: Where users are redirected after failed payment

  These URLs should handle payment responses appropriately and show relevant messages to users.
</Accordion>

<Accordion title="Checklist 4: Configure verify payment method" icon="fa-code">
  Implement payment verification on your backend:

  ```swift Swift
  // Always verify payment status from your backend using PayU's verify API
  // Do not rely solely on the mobile response for order fulfillment
  ```

  Use PayU's verification API to confirm payment status before order fulfillment.
</Accordion>

<Accordion title="Checklist 5: Configure Webhook" icon="fa-code">
  Set up webhooks to receive payment notifications:

  1. Configure webhook URL in PayU dashboard
  2. Implement webhook handler on your backend
  3. Verify webhook authenticity using provided hash
  4. Process payment updates asynchronously

  Example webhook structure:

  ```json
  {
    "mihpayid": "transaction_id",
    "status": "success",
    "amount": "100.00",
    "txnid": "merchant_txn_id"
  }
  ```
</Accordion>

<Accordion title="Integrate convenience fee" icon="fa-code">
  To integrate convenience fees:

  ```swift Swift
  let payUPaymentParams = PayUPaymentParamsBuilder()
      .setKey("MERCHANT_KEY")
      .setTransactionId("TRANSACTION_ID")
      // ... other parameters  
      .setConvenienceFee("CONVENIENCE_FEE_JSON")
      .build()
  ```

  The convenience fee JSON should contain fee structure for different payment modes.
</Accordion>
