---
title: UPI Bolt UI SDK Integration - Ionic
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
UPI Bolt UI SDK allows you to manage the checkout options on their checkout screen. You use **PayU UPI Bolt UI SDK** for customer registration, payment, and profile management. This integration involves the following steps:

1. [Add permissions to Manifest file](#step-1-add-permissions-to-manifest-file)
2. [Include Bolt UI SDK and AAR Files](#step-2-include-bolt-ui-sdk-and-aar-files)
3. [Initialize the SDK](#step-3-initialize-the-sdk)
4. [Check for UPI Bolt SDK availability](#step-4-check-for-upi-bolt-sdk-availability)
5. [Register and pay](#step-5-register-and-pay)

For hash generation logic and Listener/Callback integration, the [Hash generation logic ](#hash-generation-logic)and o [Listener or Callback logic](#listener-or-callback-logic) sub-sections.

## Prerequisites

* Minimum Android SDK Version - 23 and above.
* Compile SDK Version - 31 and above.
* The following .aar (Android archive) files provided by PayU during onboarding:
  1. NPCI Secure Component
  2. AXIS Olive
* For iOS Minimum SDK version is 13 but you can use upi-bolt features on iOS 17 and above only.
* The following xcframework files will be provided by PayU during onboarding.
  * NPCI - CommonLibrary.xcframework
  * AXIS - OlivePayLibrary.xcframework\
    Add these frameworks to your project. The added framework is similar to the following screenshot:

<Image align="center" width="600px" src="https://files.readme.io/227250da5bb54c8967c59370aac96e27be792b9224dc4a61b536efe539aa2429-bolt_added_framework.png" />

## Step 1: Add permissions to Manifest file

Update the manifest file to include the following so that permissions are provided for SDK:

```
<uses-permission android:name="android.permission.SEND_SMS"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.READ_PHONE_STATE" />
<uses-permission android:name="android.permission.READ_PHONE_NUMBERS" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

## Step 2: Include Bolt UI SDK and AAR Files

To include the PayU UPI Bolt UI SDK in your project, add the following code snippet to your module level `package.json` inside `"dependencies"`.

```
TODO : dependecy goes here after publishing
```

Add the .aar files provided by PayU during onboading. in the **libs** directory of your android module and add these in module level **build.gradle**. For the list of files, refer to[ Prerequisites](#prerequisites).

```
api(files("$projectDir/libs/SecureComponent-release-prod_05062024_9d3904ab.aar")) // NPCI .aar
api(files("$projectDir/libs/oliveupi-plugin-release_1.0.2_prod_10-09-2024.aar")) // AXIS .aar 
```

The screenshot of libs directory is similar to the following:

<Image align="center" width="350px" src="https://files.readme.io/a02ecf05cde24c29a8a5b4ba992dde13cc092a031a3f0d69c63636db84d14eab-upi-bolt-iconic-libraries_folder.png" />

## Step 3: Initialize the SDK

 It is used to initialize the SDK. This should be called before accessing any of the API’s in the SDK

```swift
interface SdkInitParams {
  merchantName: string;
  merchantKey: string;phone: string;
  email: string;
  requestId: string;
  pluginTypes: string[];
  isProduction?: boolean;
  excludedBanksIINs?: string[];
}

const config: SdkInitParams = {
      merchantName: <merchantName>,
      merchantKey: <merchantKey>,
      phone: <phone>,
      email: <email>,
      requestId: <requestId>,
      pluginTypes: <pluginTypes>,
      isProduction: <isProduction>,
      excludedBanksIINs: <excludedBanksIINs>
};

PayUUpiPlugin.initSDK({ config: JSON.stringify(config) })
```

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
        config
        ` mandatory`
      </td>

      <td>
        `String` Config includes the below fields.
      </td>
    </tr>

    <tr>
      <td>
        merchantName\
        ` mandatory`
      </td>

      <td>
        `String`Merchant Name
      </td>
    </tr>

    <tr>
      <td>
        merchantKey\
        ` mandatory`
      </td>

      <td>
        `String`PayU Merchant Key
      </td>
    </tr>

    <tr>
      <td>
        phone\
        ` mandatory`
      </td>

      <td>
        `String`Phone number for registration
      </td>
    </tr>

    <tr>
      <td>
        email\
        ` mandatory`
      </td>

      <td>
        `String`Customer Email Id
      </td>
    </tr>

    <tr>
      <td>
        pluginTypes\
        ` mandatory`
      </td>

      <td>
        `String Array`List of Supported Banks (“AXIS, HDFC”)
      </td>
    </tr>

    <tr>
      <td>
        isProduction\
        ` optional`
      </td>

      <td>
        `Boolean`Prod - ture, staging - false
      </td>
    </tr>

    <tr>
      <td>
        excludedBanksIINs\
        ` optional`
      </td>

      <td>
        `String Array`List of Bank’s IIN to exclude
      </td>
    </tr>

    <tr>
      <td>
        requestId\
        ` mandatory`
      </td>

      <td>
        `String`Unique reference ID
      </td>
    </tr>
  </tbody>
</Table>

## Step 4: Check for UPI Bolt SDK availability

The **isUPIBoltSDKAvailable** API allows you to manage UPI accounts and transaction history.

```swift ionic
PayUUpiPlugin.isUPIBoltSDKAvailable();
```

## Step 5: Register and pay

The **registerAndPay** API allows you to initialize registration and payment flow. It will internally authenticate and register the customer. After successful authentication and registration, the user will follow the payment journey. Once payment is completed, based on the payment status the merchant will get a callback through the listener

```swift ionic
interface PaymentParams {
    amount: string;
    productInfo: string;
    firstName: string;
    surl?: string;
    furl?: string;
    udf1?: string;
    udf2?: string;
    udf3?: string;
    udf4?: string;
    udf5?: string;
    txnId: string;
    isCCTxnEnabled?: boolean;
}

const paymentParams: PaymentParams = {
    amount: <amount>,
    productInfo: <productInfo>,
    firstName: <firstName>,
    surl: <surl>,
    furl: <furl>,
    udf1: <udf1>,
    udf2: <udf2>,
    udf3: <udf3>,
    udf4: <udf4>,
    udf5: <udf5>,
    txnId: <txnId>,
    isCCTxnEnabled: <isCCTxnEnabled>
};

PayUUpiPlugin.registerAndPay({
    paymentParams: JSON.stringify(paymentParams)
});

```

> 📘 Callback reference:
>
> For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic) sub-section.

The following fields are needed as a request for this API:

<Table>
  <thead>
    <tr>
      <th>
        Field
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
        `String` Amount to be paid
      </td>
    </tr>

    <tr>
      <td>
        txnId\
        `mandatory`
      </td>

      <td>
        `String`Unique transaction ID
      </td>
    </tr>

    <tr>
      <td>
        productInfo\
        `mandatory`
      </td>

      <td>
        `String`Product description
      </td>
    </tr>

    <tr>
      <td>
        firstName\
        `mandatory`
      </td>

      <td>
        `String`First name of the user
      </td>
    </tr>

    <tr>
      <td>
        furl\
        `optional`
      </td>

      <td>
        `String`Failure URL 
      </td>
    </tr>

    <tr>
      <td>
        surl\
        `optional`
      </td>

      <td>
         `String`Success URL
      </td>
    </tr>

    <tr>
      <td>
        udf1\
        `optional`
      </td>

      <td>
         `String`User defined field
      </td>
    </tr>

    <tr>
      <td>
        udf2\
        `optional`
      </td>

      <td>
          `String`User defined field
      </td>
    </tr>

    <tr>
      <td>
        udf3\
        `optional`
      </td>

      <td>
          `String`User defined field
      </td>
    </tr>

    <tr>
      <td>
        udf4\
        `optional`
      </td>

      <td>
          `String`User defined field
      </td>
    </tr>

    <tr>
      <td>
        udf5\
        `optional`
      </td>

      <td>
          `String`User defined field
      </td>
    </tr>

    <tr>
      <td>
        isCCTxnEnabled\
        `optional`
      </td>

      <td>
          `Boolean`Specify whether CC transaction is enabled
      </td>
    </tr>
  </tbody>
</Table>

## Manage UPI accounts

The **openUPIManagement** API allows you to manage UPI accounts and transaction history.

```swift ionic
PayUUpiPlugin.openUPIManagement({ screenType: <screenType> }) 
```

> 📘 Callback reference:
>
> For callback logic refer to [Listener or Callback logic](#listener-or-callback-logic) sub-section.

The following fields are needed as a request for this API:

| Fields     | Data Type | Optional /Mandatory | Definition                                                                             |
| ---------- | --------- | ------------------- | -------------------------------------------------------------------------------------- |
| screenType | string    | M                   | `"ALL" or "TRANSACTIONHISTORY" or "MANAGEUPIACCOUNTS" or "DISPUTE" or "DEREGISTERUPI"` |

## Listener or Callback logic

The listener/callback contains 4 methods where the merchant app will get the API response and hash-related callbacks

| S.No. | Listener                                                                                      | Description                                                                               |
| ----- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| 1     | Plugins\['PayUUpiPlugin'\]\['addListener'\]\('onPayUSuccess', (data: string) => \{});         | It will contain success response. Ref. 5.1                                                |
| 2     | Plugins\['PayUUpiPlugin'\]\['addListener'\]\('onPayUFailure', (data: string) => \{});         | It will contain failure response. Ref. 5.1                                                |
| 3     | Plugins\['PayUUpiPlugin'\]\['addListener'\]\('onPayUCancel', (data: string) => \{});          | It will tell if payment was cancelled.                                                    |
| 4     | Plugins\['PayUUpiPlugin'\]\['addListener'\]\('generateHash', (data: string) => \{});          | For hash generation, refer to [Hash generation logic ](#hash-generation-logic)sub-section |
| 5     | Plugins\['PayUUpiPlugin'\]\['addListener'\]\('isUPIBoltSDKAvailable', (data: string) => \{}); | It will give response for “PayUUpiPlugin.isUPIBoltSDKAvailable();” method trigger.        |

### PayUUPIResponse

| Fields       | Data Type | Definition               |
| ------------ | --------- | ------------------------ |
| responseType | Integer   | Ref. 5.2                 |
| code         | Integer   | Error or success code    |
| message      | String?   | Error or success message |
| result       | Object?   | Response data            |

### ResponseType

| Response Type        | Response Code | Definition       |
| -------------------- | ------------- | ---------------- |
| REQUEST\_UPI\_BOLT   | 100           | UPI Bolt Status  |
| REQUEST\_TRANSACTION | 124           | Register And Pay |
| REQUEST\_MANAGE      | 125           | UPI Management   |

## Hash Generation logic

The PayU SDKs use hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification.

For generating and passing dynamic hashes, the merchant will receive a call from the `generateHash()` method of `PayUUPIBoltUiListener`. The `generateHash() `method is called by the SDK each time it needs an individual hash.

```swift ionic
Plugins['PayUUpiPlugin']'addListener' => {
    // Merchant will get JSON as string with type of hash and hash string as values of JSON.
    // They have to sign that string using salt to create hash value and pass that to "PayUUpiPlugin.hashGenerated({hashData: hashJson});".
    // In the JSON you have to check for two keys to generate hash:
    // 1. hashString
    // 2. hashName

    // Example code:
    const hashData = data['hashString'];
    const hashName = data['hashName'];

    // Generate hash
    const hash = // generate hash using SHA-512 algorithm

    // Create a map to store hash data
    const hashMap: Map<string, string> = new Map<string, string>();
    hashMap.set('hashName', hashName);
    hashMap.set(hashName, hash);

    // Convert map to JSON object
    const obj: { [key: string]: string } = {};
    hashMap.forEach((value, key) => {
        obj[key] = value;
    });

    // Convert JSON object to string
    let hashJson: string = JSON.stringify(obj);

    // Pass the generated hash to the SDK
    PayUUpiPlugin.hashGenerated({hashData: hashJson});
});
```
