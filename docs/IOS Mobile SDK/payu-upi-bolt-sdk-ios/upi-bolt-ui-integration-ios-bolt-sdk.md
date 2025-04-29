---
title: UPI Bolt UI Integration - iOS Bolt SDK
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
## Prerequisites

* SDK Compatibility  
* Supported iOS deployment target - iOS 17 and above.

## UI Bolt Integration

Merchants who want to integrate only PayU UPI Bolt with their app. They can manage the checkout options on their checkout screen. Although they can use **PayU UPI Bolt UI SDK** for customer registration, payment, and profile management. 

To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your podfile. 

```
pod 'PayUIndia-UPIBoltUIKit', '~> 1.0.0-alpha.0'
```

The following xcframework files will be provided by PayU during onboarding.

* **NPCI** - CommonLibrary.xcframework
* **AXIS** - OlivePayLibrary.xcframework 

Add these framework in your project.

The added framework is similar to the following screenshot:

<Image align="center" src="https://files.readme.io/227250da5bb54c8967c59370aac96e27be792b9224dc4a61b536efe539aa2429-bolt_added_framework.png" />

To integrate UPI Bolt UI on iOS SDK platform:

## Step 1: Initialization

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

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        parentVC
        `mandatory`
      </td>

      <td>
        `UIViewController` Calling VC of the merchant App 
      </td>
    </tr>

    <tr>
      <td>
        delegate\
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltUIDelegate` Delegates to receive response
      </td>
    </tr>

    <tr>
      <td>
        config\
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltUIConfig` PayUUPIBoltUIConfig includes the below fields. 
      </td>
    </tr>

    <tr>
      <td>
        merchantName\
        `mandatory`
      </td>

      <td>
        `String` Merchant Name
      </td>
    </tr>

    <tr>
      <td>
        merchantKey\
        `mandatory`
      </td>

      <td>
        `String` PayU Merchant Key
      </td>
    </tr>

    <tr>
      <td>
        phone\
        `mandatory`
      </td>

      <td>
        `String` Phone number for registration
      </td>
    </tr>

    <tr>
      <td>
        email\
        `mandatory`
      </td>

      <td>
        `String` Customer Email Id
      </td>
    </tr>

    <tr>
      <td>
        pluginTypes\
        `mandatory`
      </td>

      <td>
        `Array <String>` List of Supported Plugin (Values - AXIS or HDFC)
      </td>
    </tr>

    <tr>
      <td>
        isProduction\
        `mandatory`
      </td>

      <td>
        `Boolean` This parameter must contain any of the following: true - Production environment, false - Test or Staging environment
      </td>
    </tr>

    <tr>
      <td>
        excludedBanksIINs\
        `mandatory`
      </td>

      <td>
        `Array <String>` List of Bank’s IIN to exclude
      </td>
    </tr>

    <tr>
      <td>
        refId\
        `optional`
      </td>

      <td>
        `String` Unique reference ID
      </td>
    </tr>
  </tbody>
</Table>

## Step 2: Check if UPI Bolt SDK is available

      The **isUPIBoltSDKAvailable** API allows you to manage UPI accounts and transaction history.

```swift
boltUI.isUPIBoltSDKAvailable(callback: PayUUPIBoltUICallBack)
```

For callbacks, refer to [Listener or Callback logic](#listener-or-callback-logic).

 The following fields are needed as a request for this API: 

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        callback
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltUI `Callback Ref. 6
      </td>
    </tr>
  </tbody>
</Table>

## Step 3: Register and pay

The **registerAndPay** API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener. 

```swift
boltUI.registerAndPay(paymentParams PayUUPIBoltPaymentParams)
```

For paymentParams, pass `PayUUPIBoltPaymentParams` instance. For more information, refer to [ Generate PayU Payment Params](#step-5-generate-payu-payment-params).

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        paymentParams
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltPaymentParams` Ref. 5
      </td>
    </tr>
  </tbody>
</Table>

## Step 4: Open UPI Management

The **openUPIManagement** API allows you to manage UPI accounts and transaction history.

```swift
boltUI.openUPIManagement(screenType: PayUUPIBoltUIScreenType) // Screen Types enum PayUUPIBoltUIScreenType: Int {    case all    case transactionHistory    case manageUPIAccounts    case dispute    case deregisterUPI }\`
```

For callbacks, refer to [Listener or Callback logic](#listener-or-callback-logic).

 The following fields are needed as a request for this API: 

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        screenType
        `mandatory`
      </td>

      <td>
        `PayUUPIBoltUIScreenType` To enforce the management screen
      </td>
    </tr>
  </tbody>
</Table>

## Step 5: Generate PayU payment params

The **PayUPaymentParams API** is used to generate PayU payment parameters.

```swift
var paymentParams = PayUUPIBoltPaymentParams(
    transactionId: "<transactionId>", // Replace with actual transaction ID
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

<Table>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        amount
        `mandatory`
      </td>

      <td>
        `String` Amount to make payment
      </td>
    </tr>

    <tr>
      <td>
        transactionId\
        `mandatory`
      </td>

      <td>
        `String`  Unique transaction ID
      </td>
    </tr>

    <tr>
      <td>
        productInfo\
        `mandatory`
      </td>

      <td>
        `String` Product description.
      </td>
    </tr>

    <tr>
      <td>
        firstName\
        `mandatory`
      </td>

      <td>
        `String`  First name of the user
      </td>
    </tr>

    <tr>
      <td>
        furl\
        `optional`
      </td>

      <td>
        `String` Failure callback URL
      </td>
    </tr>

    <tr>
      <td>
        surl\
        `optional`
      </td>

      <td>
        `String` Success callback URL 
      </td>
    </tr>

    <tr>
      <td>
        udf1\
        `optional`
      </td>

      <td>
        `String` User-defined fields 1
      </td>
    </tr>

    <tr>
      <td>
        udf2\
        `optional`
      </td>

      <td>
        `String` User-defined fields 2
      </td>
    </tr>

    <tr>
      <td>
        udf3\
        `optional`
      </td>

      <td>
        `String` User-defined fields 3
      </td>
    </tr>

    <tr>
      <td>
        udf4\
        `optional`
      </td>

      <td>
        `String` User-defined fields 4
      </td>
    </tr>

    <tr>
      <td>
        udf5\
        `optional`
      </td>

      <td>
        `String` User-defined fields 5
      </td>
    </tr>

    <tr>
      <td>
        udf6\
        `optional`
      </td>

      <td>
        `String` User-defined fields 6
      </td>
    </tr>
  </tbody>
</Table>

## Step 6: Check PayU UPI Response

The **PayUUPIResponse** API is used to check the response.

| Fields  | Definition                        |
| ------- | --------------------------------- |
| code    | `Integer` Error or success code   |
| message | `String` Error or success message |
| result  | `Object` Response data            |

## Hash generation logic

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

### Listener or Callback logic

The listener/callback contains 4 methods where the merchant app will get the API response and hash-related callbacks.

| Method                                                                                                         | Purpose                                                                        |
| -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| func onPayUSuccess(response: PayUUPIBoltResponse)                                                              | It will contain success response.                                              |
| func onPayUFailure(response: PayUUPIBoltResponse)                                                              | It will contain failure response                                               |
| onPayUCancel(isTxnInitiated: Bool)                                                                             | It will tell if payment was cancelled                                          |
| func generateHash(for param: \[String: String\], onCompletion: @escaping PayUUPIBoltHashGenerationCompletion): | For hash generation, refer to [Hash generation logic](#hash-generation-logic). |

## Error codes and error message list

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
