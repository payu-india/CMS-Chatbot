---
title: 1. SDK Integration Steps - iOS Ola Money
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
You can integrate with OlaMoney either using Cocoapods or manually.

## Integration Steps

### Cocoapods Integration

The recommended procedure to include the PayUOlaMoneySDK in your iOS app is through Cocoapods. To include the framework in your Xcode project, add the following line to your Podfile:

#### Swift 5.1

`pod 'PayUIndia-OlaMoney', '1.0.0'`

#### Swift 5.1.3

`pod 'PayUIndia-OlaMoney', '1.0.1'`

### Manual integration

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
  `paymentHash`: This is required to create transactions at PayU’s end.
  `eligibilityHash`: This is required by the checkEligibility API to check eligibility if user is eligible/registered for the Ola Money
* You need to provide hashes before asking SDK to initiate the payment and check the user’s eligibility.
* Command and var1 values for generating paymentRelatedDetailsForMobileSDKHash and validateVPAHash as defined in the following table:

| Hash for Param  | Command                        | var1                                                                                                                                                                                                                                                |
| :-------------- | :----------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| eligibilityHash | `get_eligible_payment_options` | `{\\”amount\\”:\\”1\\”,\\”txnid\\”:\\””+txid+”\\”,\\”   mobile_number\\”:\\”12345678\\”,\\”first_name\\”: \\”John\\”,\\”bankCode\\”:\\”OLAM\\”,\\”email\\”: \\”[john.smith@gmail.com](mailto:john.smith@gmail.com)\\”,\\”last_name\\”:\\”Smith\\”}` |

5. After setting the value of hashes in paymentParams, call the following method of the PayUOMCore class to check whether the user is eligible to pay through Ola Money (Postpaid and Wallet):

```node Node
public func checkEligibility(params: PayUOMPaymentParams, completion:@escaping(_ status: Bool, _ response: PayUOMEligibilityModel?, _ error: Error?) -> Void)
```

6. You will get a response of the type Result with the value of type PayUOMEligibilityModel in the response’s success param. The sample code snippet is similar to the following:

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

## Test the Integration

After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<UPIIntentCallout />

<TestingChecklist />

***

<TestCardsCallout />

### Test credentials for supported payment methods

Following are the payment methods supported in PayU Test mode.

#### Test credentials for Net Banking

Use the following credentials to test the Net Banking integration:

* **user name:** payu
* **password**: payu
* **OTP**: 123456

#### Test VPA for UPI

You can use either of the following VPAs to test your UPI-related integration:

* [anything@payu](anything@payu)
* [9999999999@payu.in](mailto:9999999999@payu.in)

> ❗️ Callout
>
> The UPI in-app and UPI intent flow is not available in the Test mode.

#### Test cards for EMI

You can use the following Debit and Credit cards to test Emi integration.

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Kotak DC EMI
      </td>

      <td>
        1. **Card Number**: 4706-1378-0509-9594
        2. **Expiry**: any future date (mm/yy)
        3. **CVV**: 123
        4. **OTP**: 111111
        5. **Name**: Any name
        6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>

    <tr>
      <td>
        AXIS DC EMI
      </td>

      <td>
        1. **Card Number**: 4011-5100-0000-0007
        2. **Expiry**: any future date (mm/yy)
        3. **CVV**: 123
        4. **OTP**: 111111
        5. **Name**: Any name
        6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>

    <tr>
      <td>
        HDFC CC EMI
      </td>

      <td>
        1. **Card Number**: 4453-3410-65876437
        2. **Expiry**: any future date (mm/yy)
        3. **CVV**: 123
        4. **OTP**: 111111
        5. **Name**: Any name
        6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>

    <tr>
      <td>
        ICICI CC EMI
      </td>

      <td>
        1. **Card Number**: 4453-3410-65876437
        2. **Expiry**: any future date (mm/yy)
        3. **CVV**: 123
        4. **OTP**: 111111
        5. **Name**: Any name
        6. **Mobile Number**: 9123412345 (mandatory for EMI)
      </td>
    </tr>
  </tbody>
</Table>

#### Test wallets

You can use the following wallets and their corresponding credentials to test wallet integration.

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Wallet
      </th>

      <th>
        Mobile Number
      </th>

      <th>
        OTP
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        PayTM
      </td>

      <td>
        7777777777
      </td>

      <td>
        888888
      </td>
    </tr>

    <tr>
      <td>
        PhonePe
      </td>

      <td>
        Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: [https://developer.phonepe.com/v1/docs/setting-up-test-account](https://developer.phonepe.com/v1/docs/setting-up-test-account)
        Download the app and register your mobile number and follow the instructions as described in the above PhonePe docs.
      </td>

      <td>
        NA
      </td>
    </tr>

    <tr>
      <td>
        AmazonPay
      </td>

      <td>
        You can test using your original Amazon account details.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>

## Go-live Checklist

Ensure these steps before you deploy the integration in a live environment.

### Collect Live Payments

After [testing the integration](https://docs.payu.in/docs/ios-olamoneysdk-test-integration) end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

> 🚧 Watch Out!
>
> Ensure that you are using the production merchant key and salt generated in the live mode.

<ProductionKeyAndSaltProcedure />

### Checklist 2: Configure setIsProduction()

Set the value of the `setIsProduction()`to `true` in the payment integration code. This enables the integration to accept live payments.

### Checklist 3: Configure verify payment method

Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.

### Checklist 4: Configure Webhook

We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).
