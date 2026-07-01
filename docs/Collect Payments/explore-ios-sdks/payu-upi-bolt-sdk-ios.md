---
title: iOS UPI Bolt SDK
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
title: iOS UPI Bolt SDK
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
title: iOS UPI Bolt SDK
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

PayU UPI Bolt SDK will provide a simpler and more efficient payment experience to the merchants. It will eliminate any third-party redirection and higher success rate. Profile management including accounts and balances for users. Enhancing the overall customer experience and decreasing customer drop-offs. This section describes the advantages and user journeys. For steps to integrate UPI Bolt UI, refer to [UPI Bolt UI Integration](doc:upi-bolt-ui-integration-ios-bolt-sdk).

## UPI Bolt UI advantages

1. One-click payment journey and no hassle of redirection to a third-party UPI application.
2. Quick completion of transactions because of direct integration with the bank.
3. Seamless user experience to the customers with in-app payment.
4. Easy to integrate and get the advantage of existing customer profiles created with banks.
5. 5-6% higher success rate and better transaction conversion..
6. Merchants can take advantage of a complete user funnel to understand user behavior. 

## UPI Bolt UI user journeys

<Accordion title="Registration and Pay" icon="fa-info-circle">
  1. Merchant Application can do the User registration for customers who are coming first time for PayU UPI Bolt. The Registration can be done during the checkout process or it can be called in a separate user journey. In case of Merchant is using PayU Checkout Pro SDK, PayU will take care of customer registration.
  2. Once the registration process is initiated, the user will be asked to accept the SMS sending permissions required to verify the SIM card.  If the phone has dual SIM, the SIM card selection screen will be shown to customers to select the specific SIM card.
  3. After the device verification, UPI ID creation and the Bank selection will be done. Add bank journey will be completed after adding a bank account connected to the same mobile number used for device verification.
  4. Finally, customers can do a transaction using the added bank account. In case the customer is using the bank account for the first time they will need to set the MPIN as well.

  <Image align="center" src="https://files.readme.io/6c8ab77aaa068c2667ab98f46c81e24f881e3255566bdff3d6bb84130587dd4f-bolt_reg_and_pay_flow.jpeg" />
</Accordion>

<Accordion title="Pay" icon="fa-info-circle">
  1. Customers who are already registered with PayU UPI Bolt can make a One-click payment.
  2. The customer needs to select the already added bank account and enter the MPIN and the transaction will be completed.
  3. The customer can also check the balance before making a transaction to avoid low-balance transaction failure.

  <Image align="center" src="https://files.readme.io/253c320479271a77460a628915a381d0fcfbfc1cab71e93e46704127689b382a-bolt_pay_flow.jpeg" />
</Accordion>

<Accordion title="Profile Management Journey" icon="fa-info-circle">
  1. Customers can add new bank accounts, set MPIN, change MPIN, reset MPIN, delete accounts, and check the balance of already added bank accounts.
  2. Transaction history can be seen and queries can be raised and resolved within the PayU UI Bolt SDK.
  3. Customers can see all the raised disputes from the Dispute history screen.
  4. Customers can also deregister their all accounts with PayU UI Bolt SDK.

  <Image align="center" src="https://files.readme.io/85fc63476b9a08cd16d8d51d5e3f03c1744f82d0ce104186286268ae16ece310-bolt_profile_mgmt_flow.jpeg" />
</Accordion>

<br />

## Steps to Integrate

<Accordion title="Prerequisites" icon="fa-info-circle">
  * SDK Compatibility
  * Supported iOS deployment target - iOS 17 and above.

  Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use **PayU UPI Bolt UI SDK** for customer registration, payment, and profile management.

  To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your podfile.

  ```
  pod 'PayUIndia-UPIBoltUIKit', '~> 3.1'
  pod 'PayUIndia-UPIBoltCoreKit', '~> 2.1'
  ```

  The following xcframework files will be provided by PayU during onboarding.

  * **NPCI** - CommonLibrary.xcframework

  Add these framework in your project.

  The added framework is similar to the following screenshot:

  <Image align="center" src="https://files.readme.io/227250da5bb54c8967c59370aac96e27be792b9224dc4a61b536efe539aa2429-bolt_added_framework.png" />

  To integrate UPI Bolt UI on iOS SDK platform:
</Accordion>

<Accordion title="Step 1: Initialization" icon="fa-info-circle">
  It is used to initialize the SDK. This method returns a object that will be used to access other methods available in `PayUUPIBoltUI`.

  ```swift
  let config = PayUUPIBoltUIConfig(
                merchantName: "<merchantName>", // String
                merchantKey: "<merchantKey>" // String,
                phone: "<phone>", // String
                email: "<email>", // String
                refId: "<refId>", // String
                pluginTypes: ["<pluginType>"], // Array<String>
                excludedBanksIINs: ["<excludedBanksIIN>"], // Array<String>
                isProduction: <isProduction> // Bool
               )

  // To initialize the SDK
  val boltUI = PayUUPIBoltUI.initSDK(
              parentVC: <parentVC>, // UIViewController
              config: <config>, // PayUUPIBoltUIConfig
              delegate: <self> // Reference to delegate
            )

  // To get the already initialised object
  let boltUI = PayUUPIBoltUI.getInstance()

  // To clear the SDK Instance
  PayUUPIBoltUI.reset() 

  ```

  The following fields are needed as a request for this API:

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Fields</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Description</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>parentVC<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>UIViewController</code> Calling VC of the merchant App</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>delegate<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>PayUUPIBoltUIDelegate</code> Delegates to receive response</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>config<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>PayUUPIBoltUIConfig</code> PayUUPIBoltUIConfig includes the below fields.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantName<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Merchant Name</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>merchantKey<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> PayU Merchant Key</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>phone<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Phone number for registration</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>email<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Customer Email Id</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>pluginTypes<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Array&lt;String&gt;</code> List of Supported Plugin (Values - AXIS or HDFC)</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>isProduction<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Boolean</code> This parameter must contain any of the following: true - Production environment, false - Test or Staging environment</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>excludedBanksIINs<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Array&lt;String&gt;</code> List of Bank's IIN to exclude</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>refId<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Unique reference ID</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Step 2: Check if UPI Bolt SDK is available" icon="fa-info-circle">
  The **isUPIBoltSDKAvailable** API allows you to manage UPI accounts and transaction history.

  ```swift
  boltUI.isUPIBoltSDKAvailable(callback: PayUUPIBoltUICallBack)
  ```

  For callbacks, refer to [Listener or Callback logic](#listener-or-callback-logic).

  The following fields are needed as a request for this API:

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Fields</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>callback<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>PayUUPIBoltUI</code> Callback Ref. 6</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Step 3: Register and pay" icon="fa-info-circle">
  The **registerAndPay** API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener.

  ```swift
  boltUI.registerAndPay(paymentParams PayUUPIBoltPaymentParams)
  ```

  For paymentParams, pass `PayUUPIBoltPaymentParams` instance. For more information, refer to [ Generate PayU Payment Params](#step-5-generate-payu-payment-params).

  The following fields are needed as a request for this API:

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Fields</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>paymentParams<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>PayUUPIBoltPaymentParams</code> Ref. 5</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Step 4: Open UPI Management" icon="fa-info-circle">
  The **openUPIManagement** API allows you to manage UPI accounts and transaction history.

  ```swift
  boltUI.openUPIManagement(screenType: PayUUPIBoltUIScreenType) // Screen Types enum PayUUPIBoltUIScreenType: Int {    case all    case transactionHistory    case manageUPIAccounts    case dispute    case deregisterUPI }\`
  ```

  For callbacks, refer to [Listener or Callback logic](#listener-or-callback-logic).

  The following fields are needed as a request for this API:

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Fields</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>screenType<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>PayUUPIBoltUIScreenType</code> To enforce the management screen</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Step 5: Generate PayU payment params" icon="fa-info-circle">
  The **PayUPaymentParams API** is used to generate PayU payment parameters.

  ```swift
  var paymentParams = PayUUPIBoltPaymentParams(
      txnId: "<transactionId>", // Replace with actual transaction ID
      amount: "<amount>", // Replace with actual amount
      productInfo: "<productInfo>", // Replace with actual product info
      firstName: "<firstName>", // Replace with actual first name
      surl: "<surl>", // Replace with actual success URL
      furl: "<furl>" // Replace with actual failure URL
  )

  paymentParams.additionalParam = ["key": "value"] // Optional to pass any additional information

  let udfs = PayUUPIBoltUserDefines()
  udfs.udf1 = "<udf1>" // Replace with actual value or nil
  udfs.udf2 = "<udf2>" // Replace with actual value or nil
  udfs.udf3 = "<udf3>" // Replace with actual value or nil
  udfs.udf4 = "<udf4>" // Replace with actual value or nil
  udfs.udf5 = "<udf5>" // Replace with actual value or nil
  udfs.udf6 = "<udf6>" // Replace with actual value or nil

  paymentParams.udfs = udfs // Optional User defined fields
  ```

  The following fields are needed as a request:

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Fields</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>amount<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Amount to make payment</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>txnId<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Unique transaction ID</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>productInfo<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Product description.</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>firstName<br><code>mandatory</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> First name of the user</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>furl<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Failure callback URL</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>surl<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Success callback URL</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf1<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields 1</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf2<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields 2</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf3<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields 3</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf4<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields 4</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>udf5<br><code>optional</code></p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> User-defined fields 5</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Step 6: Check PayU UPI Response" icon="fa-info-circle">
  The **PayUUPIResponse** API is used to check the response.

  <HTMLBlock>{`
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Fields</strong></th>
      <th style="border: 1px solid #ddd; padding: 8px;"><strong>Definition</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>code</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Integer</code> Error or success code</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>message</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>String</code> Error or success message</p></td>
    </tr>
    <tr>
      <td style="border: 1px solid #ddd; padding: 8px;"><p>result</p></td>
      <td style="border: 1px solid #ddd; padding: 8px;"><p><code>Object</code> Response data</p></td>
    </tr>
  </tbody>
</table>
`}</HTMLBlock>
</Accordion>

<Accordion title="Hash generation logic" icon="fa-info-circle">
  The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

  To generate and pass dynamic hashes, the merchant will receive a call from the `generateHash` method of **PayUUPIBoltUIDelegate**. The SDK calls the `generateHash` method each time it needs an individual hash.

  ```swift
  func generateHash(for param: [String: String], 
                    onCompletion: @escaping PayUUPIBoltHashGenerationCompletion) {
      // Your implementation here
  }
  ```

  The merchant receives a dictionary containing the type of hash and the corresponding hash string as its values. The merchant needs to sign the provided hash string using their salt to create the final hash and pass it back via the completion handler. param: This dictionary contains two keys:

  * **hashName** - The name of the command.
  * **hashString** - The hash string, without the salt. PayUUPIBoltHashGenerationCompletion: This completion handler contains the hashDict parameter.
  * **hashDict**: Provide a dictionary where the hashName is the key, and the generated hash is the value. To generate the hash, you need to combine the hashString with the salt on your server and apply the SHA-512 algorithm and pass it back via the completion handler

  <Accordion title="Listener or Callback logic" icon="fa-info-circle">
    The listener/callback contains 4 methods where the merchant app will get the API response and hash-related callbacks.

    | Method                                                                                                        | Purpose                                                                        |
    | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
    | func onPayUSuccess(response: PayUUPIBoltResponse)                                                             | It will contain success response.                                              |
    | func onPayUFailure(response: PayUUPIBoltResponse)                                                             | It will contain failure response                                               |
    | onPayUCancel(isTxnInitiated: Bool)                                                                            | It will tell if payment was cancelled                                          |
    | func generateHash(for param: \[String: String], onCompletion: @escaping PayUUPIBoltHashGenerationCompletion): | For hash generation, refer to [Hash generation logic](#hash-generation-logic). |
  </Accordion>
</Accordion>

<Accordion title="Error codes and error message list" icon="fa-info-circle">
  | Codes | Message                                |
  | ----- | -------------------------------------- |
  | 0     | Success                                |
  | 1     | Fail/ Invalid Response/ Missing params |
  | 2     | User canceled the transaction          |
  | 100   | Transaction timeout                    |
  | 101   | Hash missing                           |
  | 102   | Incorrect Hash                         |
  | 103   | Handshake failed                       |
  | 104   | UPI bolt not supported                 |
  | 105   | Device not supported for UPI Bolt      |
  | 106   | Permission missing                     |
  | 107   | Sim info not available                 |
  | 108   | Device binding failed                  |
  | 500   | Something went wrong                   |
  | 501   | No internet connection                 |
</Accordion>
