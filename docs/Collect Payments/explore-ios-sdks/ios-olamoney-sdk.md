---
title: iOS Ola Money SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: iOS Ola Money SDK
  description: >-
    The Ola Money SDK by PayU is an iOS framework that allows for easy
    integration of Ola Money Postpaid and Wallet into your app. It provides
    access to APIs, error codes, and request builders for seamless integration
    with PayU.
  keywords:
    - PayU Ola Money SDK integration steps
    - PayU India Ola Money SDK for IOS Integration Steps
    - IOS Ola Money SDK integration Steps
    - Ola Money SDK integration steps
    - PayU Ola Money integration guide
    - >-
      How to integrate PayU Ola Money SDK in IOS.Step-by-step PayU Ola Money SDK
      integration
    - PayU Ola Money SDK integration for IOS apps
    - Detailed guide for PayU Ola Money SDK integration steps
    - PayU OlaMoney SDK integration steps
    - PayU India OlaMoney SDK steps
    - IOS OlaMoney SDK integration
    - OlaMoney SDK integration steps
    - PayU OlaMoney integration guide
  robots: index
next:
  description: ''
---
PayU's Ola Money SDK is an iOS framework for integrating Ola Money Postpaid and Wallet in your app in an easy, efficient, and stable method.

<Accordion title="Ola Money SDK Frameworks" icon="fa-code">
  PayU provides SDK that performs different functions related to Ola Money Payments

  **PayUOlaMoneySDK**: The PayUOlaMoneySDK framework gives access to the APIs, Error Codes, Request builder, etc. needed to integrate with PayU for OlaMoney Postpaid+Wallet.

  You can integrate with OlaMoney either using Cocoapods or manually.
</Accordion>

<Accordion title="Step 1. SDK Integration" icon="fa-code">
  <Accordion title="Cocoapods Integration" icon="fa-code">
    The recommended procedure to include the PayUOlaMoneySDK in your iOS app is through Cocoapods. To include the framework in your Xcode project, add the following line to your Podfile:

    #### Swift 5.1

    `pod 'PayUIndia-OlaMoney', '1.0.0'`

    #### Swift 5.1.3

    `pod 'PayUIndia-OlaMoney', '1.0.1'`
  </Accordion>

  <Accordion title="Manual integration" icon="fa-code">
    If you do not want to use Cocoapods, download the framework manually and integrate it into your mobile app. To integrate manually, please follow the steps below:

    1. Download the framework files from the following location: [https://github.com/payu-intrepos/payu-olamoney-ios/](https://github.com/payu-intrepos/payu-olamoney-ios/)
    2. Link the framework from your Xcode project

    #### Dependencies

    The PayUOlaMoneySDK framework requires the following dependencies. When integrating through Cocoapods, these dependencies are added automatically, and you do not need to take any additional action.

    If you are integrating with the PayUOlaMoneySDK manually, you will need to include the dependencies mentioned below. To include the frameworks manually, refer to the following PayU Github link: [https://github.com/payu-intrepos/payu-upi-ios-sdk/tree/master/Dependencies](https://github.com/payu-intrepos/payu-upi-ios-sdk/tree/master/Dependencies)

    1. **PayU Networking**: This is used by PayUOlaMoneySDK to handle network requests.
    2. **PayU Logger**: This is used by PayUOlaMoneySDK to log errors and verbose data.

    To integrate with OlaMoney:

    1. Set environment to Test or Production.

    `PayUOMCore.shared.environment = .production
                // PayUOMCore.shared.environment = .test`

    2. Set Logger level to verbose, error, or disabled.

    `PayUOMCore.shared.logLevel = .verbose
                // PayUOMCore.shared.logLevel = .none`

    3. Set mandatory payment parameters required for the payment.

    ```swift Swift
    do {
    paymentParams = try PayUOMPaymentParams(
    merchantKey: <Your merchant Key>, //Your merchant key for the environment set in step 1
    transactionId: String.randomString(length: 10), //A unique ID for this trasaction
    amount: "1", //Amount of transaction
    productInfo: "iPhone", // Description of the product
    firstName: "John", lastName: "Doe", // First name of the user
    email: "johndoe@example.com",// Email of the useer
    phoneNumber: phoneNumberTextField.text ?? "9876543210", // Phone of user
    //User defined parameters.
    //You can save additional details for each transaction if you need them for your business logic.
    //You will get these details back in payment response and transaction verify API
    //Like, you can add SKUs for which payment is made.
    udf1: "SKU1|SKU2|SKU3",
    //You can keep all udf fields blank if you do not have any requirement to save txn specific data
    udf2: "asdf",
    udf3: "asdf",
    udf4: "asdf",
    udf5: "asdf")
    // Example userCredentials - "merchantKey:user'sUniqueIdentifier"
    paymentParams?.userCredentials = "smsplus:myUserEmail@payu.in"
    // Success URL. Not used but required due to mandatory check.
    paymentParams?.surl = "https://cbjs.payu.in/sdk/success"
    // Failure URL. Not used but required due to mandatory check.
    paymentParams?.furl = "https://cbjs.payu.in/sdk/failure"
    paymentParams?.offerKey = "cardnumber@8370,cardnumbers2@8380,for particular bins@8427,srioffer@8428,cc2@8429"
    } catch let error {
    //Helper.showAlert("Could not create post params due to: \(error.localizedDescription)", onController: self)
    }
    ```

    4. Fetch hashes and save them in the `paymentParams` object
       * You need to set the hashes property in `paymentParams`. Hashes ensure that requests are untampered. This helps in ensuring the security of the transaction. Property hashes are of the type `PayUOMHashes`.

    <Callout icon="📘" theme="info">
      **Note**: Hashes must be generated only on your server. Your secret key (also known as salt) must never be included in your app.For more information, refer to [Set up Payment Hashes](doc:set-up-the-payment-hashes).
    </Callout>

    * PayUHashes has two properties. Each of these three is used for a distinct API call. The two properties are as follows:
      `paymentHash`: This is required to create transactions at PayU's end.
      `eligibilityHash`: This is required by the checkEligibility API to check eligibility if user is eligible/registered for the Ola Money
    * You need to provide hashes before asking SDK to initiate the payment and check the user's eligibility.
    * Command and var1 values for generating paymentRelatedDetailsForMobileSDKHash and validateVPAHash as defined in the following table:

    | Hash for Param  | Command                        | var1                                                                                                                                                                                                                      |
    | :-------------- | :----------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
    | eligibilityHash | `get_eligible_payment_options` | `{\"amount\":\"1\",\"txnid\":\""+ txid +"\",\"   mobile_number\":\"12345678\",\"first_name\": \"John\",\"bankCode\":\"OLAM\",\"email\": \"[john.smith@gmail.com](mailto:john.smith@gmail.com)\",\"last_name\":\"Smith\"}` |

    5. After setting the value of hashes in paymentParams, call the following method of the PayUOMCore class to check whether the user is eligible to pay through Ola Money (Postpaid and Wallet):

    ```node Node
    public func checkEligibility(params: PayUOMPaymentParams, completion:@escaping(_ status: Bool, _ response: PayUOMEligibilityModel?, _ error: Error?) -> Void)
    ```

    6. You will get a response of the type Result with the value of type PayUOMEligibilityModel in the response's success param. The sample code snippet is similar to the following:

    ```node Node
    PayUOMCore.shared.checkEligibility(params: self.paymentParams!, completion: { [unowned self] status, response, error in
    DispatchQueue.main.async {
    self.makePaymentButton.isEnabled = status
    if (error != nil) {
    self.elegebilityLabel.text = error?.localizedDescription
    } else {
    self.elegebilityLabel.text = response?.msg
    }
    }
    })
    ```

    7. Populate the relevant options on your checkout screen.
    8. Check the eligibility and fetch the post parameters with the method. Later, you can use the CustomBrowser or `WKWebView` to load the URL and PostData.

    ```node Node
    public func getPostData(params: PayUOMPaymentParams) -> String
    ```

    9. Use the Custom Browser to load data using the following code (Optional):

    ```node Node
    let customBrowser = try? PUCBWebVC(postParam: postData, url: PayUOMSecureEndPoint.securePayment().baseURL, merchantKey: "smsplus")
    customBrowser?.cbWebVCDelegate = self
    let navVC = UINavigationController(rootViewController: customBrowser!)
    self.present(navVC, animated: true, completion: nil)
    ```
  </Accordion>
</Accordion>

<Accordion title="Step 2. Test the Integration and Go-Live" icon="fa-code">

<IOS_Test_the_Integration />
<IOS_Go_Live />
</Accordion>
