---
title: UPI Bolt UI SDK Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: UPI Bolt UI SDK integration
  description: >-
    Integrate UPI Bolt UI SDK on Android with native flow. Steps for PayUBolt
    SDK setup and UPI intent/collect.
  keywords:
    - UPI Bolt UI SDK integration
    - PayUBolt Android
    - UPI native integration Android
    - PayU Bolt SDK
  robots: index
next:
  description: ''
---
UPI Bolt UI SDK allows you to manage the checkout options on their checkout screen. You use **PayU UPI Bolt UI SDK** for customer registration, payment and profile management. This integration involves the following steps:

1. [Add permissions to Manifest file](#step-1-add-permissions-to-manifest-file)
2. [Include Bolt UI SDK and AAR Files](#step-2-include-bolt-ui-sdk-and-aar-files)
3. [Initialize the SDK](#step-3-initialize-the-sdk)
4. [Check for UPI Bolt SDK availability](#step-4-check-for-upi-bolt-sdk-availability)
5. [Register and pay](#step-5-register-and-pay)

For hash generation logic and Listener/Callback integration, the [Hash generation logic ](#hash-generation-logic)and  [Listener or Callback logic](#listener-or-callback-logic) sub-sections.

## Prerequisites

- Minimum Android SDK Version - 23 and above.
- Compile SDK Version - 31 and above.
- The following .aar (Android archive) files provided by PayU during onboarding:
  1. NPCI Secure Component
  2. AXIS Olive

## Step 1: Add permissions to Manifest file

Update the manifest file to include the following so that permissions are provided for SDK:

```
// To send SMS for device binding
<uses-permission android:name="android.permission.SEND_SMS"/>
// To check current network state
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
// To access internet for API calls 
<uses-permission android:name="android.permission.INTERNET" />
// To get sim details from devices below or equal to 29
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
// Too get sim details from devices above 29
<uses-permission android:name="android.permission.READ_PHONE_NUMBERS" />
// To provide location details for transaction
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

## Step 2: Include Bolt UI SDK and AAR Files

To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your app’s `build.gradle`.

```
implementation 'in.payu:payu-upi-bolt-ui-sdk:1.3.0' // PayU Bolt SDK
implementation 'in.payu:payu-upi-bolt-core-sdk:1.3.0'
```

Add the .aar files provided by PayU during onboarding. in the **libs** directory of your android module and add these in module level **build.gradle**. For the list of files, refer to[ Prerequisites](#prerequisites).

```
api(files("$projectDir/libs/SecureComponent-release-prod_05062024_9d3904ab.aar")) // NPCI .aar
```

The screenshot of libs directory is similar to the following:


<Image src="https://files.readme.io/1af3684beef4a3b10716b5fc7de478bc9a07ff6f82ae0cec8041bbb94d8c754c-bolt_native_flow_aar_directory_structure.png" align="center" width="360px" />


## Step 3: Initialize the SDK

It is used to initialize the SDK. This method returns a object that will be used to access other methods available in `PayUUPIBoltUI`.

```kotlin
val bolt = PayUUPIBoltUI.getInstance(
    activity: AppCompatActivity,
    config: PayUUPIBoltConfig,
    hashGenerationListener: PayUHashGenerationListener
)
```

The following fields are needed as a request for this API:

| Fields                              | Definition                                                                       |
| ----------------------------------- | -------------------------------------------------------------------------------- |
| activity ` mandatory`               | `AppCompatActivity` Calling activity of the merchant App                         |
| config ` mandatory`                 | `PayUUPIBoltUIConfig` Config includes the below fields.                          |
| hashGenerationListener ` mandatory` | `PayUHashGenerationListener` Callback listener for hash generation               |
| merchantKey ` mandatory`            | `String`PayU Merchant Key                                                        |
| phone ` mandatory`                  | `String`Phone number for registration                                            |
| email ` mandatory`                  | `String`Customer Email Id                                                        |
| pluginType ` mandatory`             | `String Array`List of Supported Banks (“AXIS, HDFC”)                             |
| isProd ` optional`                  | `Boolean`Production  environment - `true`, Test or Staging environment - `false` |
| excludedBanksIINs ` optional`       | `String Array`List of Bank’s IIN to exclude                                      |
| requestId ` mandatory`              | `String`Unique reference ID                                                      |

<Accordion title="Response" icon="fa-reply">
  | Response Params | Definition                                 |
  | --------------- | ------------------------------------------ |
  | `PayUUPIBoltUI` | PayUUPIBoltUI object for invoking SDK APIs |

  > 📘 Callback:
  >
  > After the SDK is initialised, use the same object to call the sdk methods.
</Accordion>

## De-initialise PayUBolt UI SDK

`reset`: This method is used to deinitailise the bolt object. 

```
`PayUUPIBoltUI.reset()`
```

## Step 4: Check for UPI Bolt SDK availability

The **isUpiBoltEnabled** API allows you to manage UPI accounts and transaction history.

```kotlin
boltUI.isUpiBoltEnabled(callback: (PayUUPIBoltResponse) -> Unit)
```

## Step 5: Register and Pay

The **registerAndPay** API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener.

```swift ionic
boltUI.registerAndPay(paymentParams PayUUPIBoltPaymentParams, callback: PayUUPIBoltUICallBack)

```

<Callout icon="📘" theme="info">
  ### Callback reference:

  For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic) sub-section.
</Callout>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        paymentParams `mandatory`
      </td>

      <td>
        - _Object_\* This parameter includes the fields listed in [paymentParams object](#generate-payment-params).
      </td>
    </tr>

    <tr>
      <td>
        callback<br />`mandatory`
      </td>

      <td>
        - _PayUUPIBoltUICallBack_\* This parameter contains the callback. For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic)  sub-section.
      </td>
    </tr>
  </tbody>
</Table>

## Manage UPI accounts

The **openUPIManagement** API allows you to manage UPI accounts and transaction history.

```kotlin
boltUI.openUPIManagement(enforceScreenType: EnforceScreenType, callback: PayUUPIBoltUICallBack)
```

<Callout icon="📘" theme="info">
  ### Callback reference:

  For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic) sub-section.
</Callout>

The following fields are needed as a request for this API:

<Table align={["left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Fields
      </th>

      <th>
        Data Type
      </th>

      <th>
        Optional /Mandatory
      </th>

      <th>
        Definition
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        enforceScreenType
      </td>

      <td>
        EnforceScreenType
      </td>

      <td>
        O
      </td>

      <td>
        `"ALL" or "TRANSACTIONHISTORY" or "MANAGEUPIACCOUNTS" or "DISPUTE" or "DEREGISTERUPI"`
      </td>
    </tr>

    <tr>
      <td>
        callback `mandatory`
      </td>

      <td>
        PayUUPIBoltUICallBack
      </td>

      <td>
        M
      </td>

      <td>
        - _PayUUPIBoltUICallBack_\* This parameter contains the callback. For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic)   sub-section.
      </td>
    </tr>
  </tbody>
</Table>

## Generate Payment Params

```Text Kotlin
val paymentParams = PayUUPIBoltPaymentParams.Builder()
    .amount(<amount>)
    .productInfo(<productInfo>)
    .firstName(<firstName>)
    .surl(<surl>)
    .furl(<furl>)
    .udf1(<udf1>)
    .udf2(<udf2>)
    .udf3(<udf3>)
    .udf4(<udf4>)
    .udf5(<udf5>)
    .txnId(<uniqueTxnId>)
    .isCCTxnEnabled(<Bool>)
    .build()
```

The following fields are needed as a request:

<Table>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        amount<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Transaction amount.
      </td>
    </tr>

    <tr>
      <td>
        productInfo<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Information about the product or service.
      </td>
    </tr>

    <tr>
      <td>
        firstName<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Customer's first name.
      </td>
    </tr>

    <tr>
      <td>
        surl<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Android success URL.
      </td>
    </tr>

    <tr>
      <td>
        furl<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Android failure URL.
      </td>
    </tr>

    <tr>
      <td>
        ios\_surl<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        iOS success URL.
      </td>
    </tr>

    <tr>
      <td>
        ios\_furl<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        iOS failure URL.
      </td>
    </tr>

    <tr>
      <td>
        initiationMode<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Mode of initiation (e.g., "10").
      </td>
    </tr>

    <tr>
      <td>
        purpose<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Purpose code (e.g., "00").
      </td>
    </tr>

    <tr>
      <td>
        txnId<br /> <code>mandatory</code>
      </td>

      <td>
        <code>String</code><br />
        Unique transaction ID.
      </td>
    </tr>

    <tr>
      <td>
        udf1 - udf6<br /> <code>optional</code>
      </td>

      <td>
        <code>Any</code><br />
        User-defined fields for additional transaction metadata.
      </td>
    </tr>

    <tr>
      <td>
        isCCTxnEnabled<br /> <code>optional</code>
      </td>

      <td>
        <code>Boolean</code><br />
        Enables card fallback if supported – true or false.
      </td>
    </tr>
  </tbody>
</Table>

<br />

## Listener or Callback logic

Listener/Callback contains 3 methods where the merchant app will get the API response and hash-related callbacks

| S.No. | Listener                                                                                           | Description                                                                               |
| ----- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1     | fun generateHash(map: HashMap\<String, String>, hashGenerationListener: PayUHashGeneratedListener) | For hash generation, refer to [Hash generation logic ](#hash-generation-logic)sub-section |
| 2     | fun onPayUSuccess(response: PayUUPIBoltResponse)                                                   | It will contain success response.                                                         |
| 3     | fun onPayUFailure(response: PayUUPIBoltResponse)                                                   | It will contain failure response.                                                         |

<Accordion title="PayUUPIResponse" icon="fa-code">
  | Fields       | Data Type | Definition               |
  | ------------ | --------- | ------------------------ |
  | responseType | Integer   | f. ResponseType section  |
  | code         | Integer   | Error or success code    |
  | message      | String    | Error or success message |
  | result       | Object    | Response data            |
</Accordion>

<Accordion title="ResponseType" icon="fa-list">
  | Response Type        | Response Code | Definition       |
  | -------------------- | ------------- | ---------------- |
  | REQUEST\_UPI\_BOLT   | 100           | UPI Bolt Status  |
  | REQUEST\_TRANSACTION | 124           | Register And Pay |
  | REQUEST\_MANAGE      | 125           | UPI Management   |
</Accordion>

## Hash Generation logic

The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

For generating and passing dynamic hashes, the merchant will receive a call from the `generateHash()` method of `PayUUPIBoltUiListener`. The `generateHash() `method is called by the SDK each time it needs an individual hash.

```kotlin
fun generateHash(map: HashMap<String, String>, hashGenerationListener: PayUHashGeneratedListener): Merchant will get map with type of hash and hash string as value of map.
  
  They have to sign that string using salt to create hash value and pass that to hashGenerationListener.onHashGenerated().
      In the map you have to check for three keys to generate hash.
      1. hashString
      2. hashName
      3. postSalt
  At the end of that hashString append your salt and use SHA-512 algo on that final string to generate hash.
  Note: If you got postSalt also in the map, first use hash string append salt and then append postSalt value to that string and use SHA-512 algo on that final string to generate hash.
  Once the hash is generated use hashGenerationListener parameter to pass the hash to SDK. Example code:
         val hashMap: HashMap<String, String> = HashMap()
         hashMap[hashName] = hash //hashName is the value you got in map and hash is the hash value.
         hashGenerationListener.onHashGenerated(hashMap)     

```

<br />
