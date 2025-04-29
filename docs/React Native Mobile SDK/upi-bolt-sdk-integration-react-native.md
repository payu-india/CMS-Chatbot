---
title: UPI Bolt SDK Integration - React Native
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section provides step-by-step for integrating the UPI Bolt SDK in React Native applications. The UPI Bolt SDK offers the following key functionalities:

- **Registration**: APIs for device binding and user registration
- **Payment**: APIs for payment processing and transaction verification
- **Management**: APIs for account management (balance checks, PIN changes, account addition/deletion)

## Prerequisites

### SDK Compatibility

- Minimum Android SDK Version: 23+
- Compile SDK Version: 31+

### Required Permissions

The following permissions need to be added to your Android Manifest file:

```xml
<uses-permission android:name="android.permission.SEND_SMS"/>
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>
<uses-permission android:name="android.permission.INTERNET"/>
<uses-permission android:name="android.permission.READ_PHONE_STATE"/>
<uses-permission android:name="android.permission.READ_PHONE_NUMBERS"/>
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION"/>
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/>
```

## Integration Steps

### 1. Install the SDK

Install the UPI Bolt SDK package using npm:

```bash
npm install payu-upi-bolt-ui-rn --save
react-native link payu-upi-bolt-ui-rn
```

### 2. Import the SDK

Import the SDK in your React Native component:

```javascript
import PayUUPIBoltUiSdk from 'payu-upi-bolt-ui-rn';
```

### 3. Add Dependencies

Add the following dependencies to your Android project's `build.gradle` file:

```gradle
implementation 'in.payu:payu-upi-bolt-axis-wrapper-sdk-android:0.0.1'
```

### 4. Add .aar Files

Add the .aar files to your Android project and include them in your app's `build.gradle` file:

> 📘 Note:
> 
> PayU will provide the required .aar files during onboarding.

```gradle
api(files("$projectDir/libs/SecureComponent-release-prod_05062024_9d3904ab.aar"))
api(files("$projectDir/libs/oliveupi-payu-release_PROD_02-12-2024_2.0.2.aar"))
```

## SDK Initialization

### Initialize the SDK

Create a configuration object and initialize the SDK:

```javascript
createSDKConfig = () => {
    let x = Math.random();
    var config = {
        merchantName: merchantName,
        merchantKey: key,
        phone: phone,
        email: email,
        requestId: 'payu_' + x,
        pluginTypes: ["AXIS"],
        isProduction: true,
        excludedBanksIINs: []
    }
    return config;
}

var initConfig = createSDKConfig();
PayUUPIBoltUiSdk.initSDK(initConfig);
```

The following fields are needed as a request for this API:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "config  \n`mandatory`",
    "0-1": "`PayUUPIBoltUIConfig` PayUUPIBoltUIConfig includes the below fields.",
    "1-0": "merchantName  \n`mandatory`",
    "1-1": "`String` Merchant Name",
    "2-0": "merchantKey  \n`mandatory`",
    "2-1": "`String` Merchant key that was provided by PayU while onboarding. Refer to [Access Production Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard).",
    "3-0": "phone  \n`mandatory`",
    "3-1": "`String` Phone number for registration",
    "4-0": "email  \n`mandatory`",
    "4-1": "`String` Customer Email Id",
    "5-0": "pluginTypes  \n`mandatory`",
    "5-1": "`String Array` List of Supported Banks (Values - PluginType.AXIS)",
    "6-0": "isProduction  \n`optional`",
    "6-1": "`Boolean` Indicates the environment:  \n  \n- **true** indicates production environment\n- **false** indicates staging or test environment",
    "7-0": "excludedBanksIINs  \n`optional`",
    "7-1": "`String` List of Bank's IIN to exclude",
    "8-0": "requestId  \n`mandatory`",
    "8-1": "`String` Unique reference ID"
  },
  "cols": 2,
  "rows": 9,
  "align": [
    null,
    null
  ]
}
[/block]


### Reset the SDK

To clear the SDK instance before creating a new one:

```javascript
PayUUPIBoltUiSdk.reset(reactContext);
```

## SDK APIs

### Check SDK Availability

Use this method to check if the UPI Bolt SDK is available on the device:

```javascript
PayUBizSdk.isUPIBoltSDKAvailable(
    (response) => {
        if (response.isSDKAvailable == 'true') {
            console.log("SDK is available for payment.");
        } else {
            console.log("UPI Bolt is not available.");
        }
    }
);
```

### Register and Pay

This API combines user registration and payment flow:

```javascript
createPaymentParams = () => {
    var txnId = new Date().getTime().toString();
    var payUPaymentParams = {
        txnId: txnId,
        amount: amount,
        firstName: firstName,
        ios_surl: sUrl,
        ios_furl: fUrl,
        surl: sUrl,
        furl: fUrl,
        productInfo: productInfo,
        udf1: udf1,
        udf2: udf2,
        udf3: udf3,
        udf4: udf4,
        udf5: udf5
    }
    return payUPaymentParams;
}

PayUUPIBoltUiSdk.payURegisterAndPay(createPaymentParams());
```

The following fields are needed as a request:

[block:parameters]
{
  "data": {
    "h-0": "Fields",
    "h-1": "Description",
    "0-0": "amount  \n`mandatory`",
    "0-1": "`String` Amount to payment",
    "1-0": "txnId  \n`mandatory`",
    "1-1": "`String` Unique transaction Id",
    "2-0": "productInfo  \n`mandatory`",
    "2-1": "`String` Product description",
    "3-0": "firstName  \n`mandatory`",
    "3-1": "`String` First name of the user",
    "4-0": "surl  \n`optional`",
    "4-1": "`String` Success URL",
    "5-0": "furl  \n`optional`",
    "5-1": "`String` Failure URL",
    "6-0": "udf1  \n`optional`",
    "6-1": "`String` User-defined field 1",
    "7-0": "udf2  \n`optional`",
    "7-1": "`String` User-defined field 2",
    "8-0": "udf3  \n`optional`",
    "8-1": "`String` User-defined field 3",
    "9-0": "udf4  \n`optional`",
    "9-1": "`String` User-defined field 4",
    "10-0": "udf5  \n`optional`",
    "10-1": "`String` User-defined field 5"
  },
  "cols": 2,
  "rows": 11,
  "align": [
    null,
    null
  ]
}
[/block]


### UPI Management

Use this API to manage UPI accounts and view transaction history:

```javascript
PayUUPIBoltUiSdk.payUUPIBoltUserSettings(<screenType>);
```

The following fields are needed as a request:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "0-0": "screenType  \n`mandatory`",
    "0-1": "`String`This field must contain any of the following screen type  \n  \n- ALL\n- TRANSACTIONHISTORY\n- MANAGEUPIACCOUNTS\n- DISPUTE\n- DEREGISTERUPI"
  },
  "cols": 2,
  "rows": 1,
  "align": [
    null,
    null
  ]
}
[/block]


## Event Listeners

Set up event listeners to handle callbacks from the SDK:

```javascript
useEffect(() => {
    const eventEmitter = new NativeEventEmitter(PayUBizSdk);
    onPayUSuccessListener = eventEmitter.addListener('onPayUSuccess', onPayUSuccess);
    onPayUFailureListener = eventEmitter.addListener('onPayUFailure', onPayUFailure);
    onPayUCancelListener = eventEmitter.addListener('onPayUCancel', onPayUCancel);
    payUGenerateHashListener = eventEmitter.addListener('generateHash', generateHash);
    permissionListener = eventEmitter.addListener('permissionCallback', permissionCallback);

    return () => {
        onPayUSuccessListener.remove();
        onPayUFailureListener.remove();
        onPayUCancelListener.remove();
        payUGenerateHashListener.remove();
        permissionCallback.remove();
    }
}, [merchantSalt]);

onPayUSuccess = (e) => {
    console.log(e);
    displayAlert('onPayUSuccess', JSON.stringify(e));
}

onPayUFailure = (e) => {
    console.log(e);
    displayAlert('onPayUFailure', JSON.stringify(e));
}

onPayUCancel = (e) => {
    console.log(e);
    displayAlert('onPayUCancel', JSON.stringify(e));
}

generateHash = (e) => {
    console.log('generateHash - ' + e);
    console.log(e.hashName);
    console.log(e.hashString);
    sendBackHash(e.hashName, e.hashString + merchantSalt);
}

displayAlert = (title, value) => {
    if (showAlert == false) {
        setShowAlert(true);
        Alert.alert(title, value);
    }
    setShowAlert(false);
}

sendBackHash = (hashName, hashData) => {
    var hashValue = calculateHash(hashData);
    var result = {'hashName': hashName, [hashName]: hashValue };
    PayUBizSdk.hashGenerated(result);
}

calculateHash = (data) => {
    var result = sha512(data);
    return result;
}
```

## Response Structure

### PayUUPIResponse

The SDK returns responses in the following format:

```json
{
  "responseType": 100,
  "code": 0,
  "message": "Success",
  "result": {
    // Response data object
  }
}
```

| Field        | Description                                                                                             |
| ------------ | ------------------------------------------------------------------------------------------------------- |
| responseType | Integer value indicating the type of response (e.g., 100 for UPI Bolt Status, 124 for Register and Pay) |
| code         | Error or success code                                                                                   |
| message      | Error or success message                                                                                |
| result       | Response data object                                                                                    |

### Response Types

| Response Type | Code | Description      |
| ------------- | ---- | ---------------- |
| 100           |      | UPI Bolt Status  |
| 124           |      | Register and Pay |

## Error Codes and Messages

| Error Code | Message                              | Description                                            |
| ---------- | ------------------------------------ | ------------------------------------------------------ |
| 0          | Success                              | Operation completed successfully                       |
| 1          | Fail/Invalid Response/Missing Params | Operation failed due to invalid parameters or response |
| 2          | User Canceled the Transaction        | User manually canceled the transaction                 |
| 100        | Transaction Timeout                  | Transaction timed out                                  |
| 101        | Hash Missing                         | Required hash is missing                               |
| 102        | Incorrect Hash                       | Provided hash is incorrect                             |
| 500        | Something Went Wrong                 | Unexpected error occurred                              |
| 501        | No Internet Connection               | Device is not connected to the internet                |

## Troubleshooting

If you encounter issues during integration, check the following:

1. Ensure all required permissions are added to the Android Manifest
2. Verify that all dependencies and .aar files are correctly added to your project
3. Check that the SDK initialization is performed with valid parameters
4. Ensure proper error handling for all SDK callbacks

> 📘 Note:
> 
> If you encounter any issues, contact [PayU Support](https://help.payu.in).