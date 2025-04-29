---
title: Virtual Cards Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Virtual Cards Integration - iOS SDK
  description: ''
  robots: index
next:
  description: ''
---
You can integrate Virtual card using PayUPPIiOS SDK in iOS. 

## Step 1: Add the dependency

Add the following dependency in your app. 

### Cocoapods

Use PayUIndia-PPI version 1.0.0.

```plaintext
pod 'PayUIndia-PPI-SDK'
```

### SPM

Use PayUIndia-PPI version 1.0.0.

```plaintext
.package(name: "PayUIndia-PPI-SDK", url: "https://github.com/payu-intrepos/PayUIndia-PPI", from: "1.0.0")
```

## Step 2: SDK initialisation

1. import the `OnePayUJSKit` SDK in your project

```swift
import OnePayUJSKit
```

2. Create the `OnePayUJSParams` object

```swift
OnePayUJSParams(
    merchantKey = <String - Merchant Key>,
    referenceId = <String - Any unique reference id>,
    environment = <Environment - Prod or Test>,
    mobileNumber = <String - user mobile number>,
    walletUrn = <String - User wallet urn linked with aboved mobile number>,
    walletIdentifier = <String - merchant wallet Identifier>
)

```

3. Create a `OnePayUJSSDK` object using the `getInstance` call `showCards` function similar to the following code block:

```swift
OnePayUJSSDK.showCards(
    parentVC: <current view Controller>,
    params: OnePayUJSParams,
    delegate: OnePayUJSSDKDelegate
)

// Params:
// parentVC: Current Viewcontroller in which want to open cards page
// onePayUJSParams: OnePayUJSModel object with all parameters and hash
// OnePayUJSSDKDelegate: This is a delegate class in which you will get below callbacks
// 1. onCancel() - If user presses back button on card page or verify OTP page
// 2. func onError(code: Int, message: String) - If any error occurs
// 3. func generateHash(for param: [String : String], onCompletion: @escaping OnePayUJSHashCompletion) - Create and send dynamic hash.

```

## Step 3: Hashing

Get hash string in map "hashString" key and hash name "hashName" in generateHash.  You need to send this string to server and append salt there, after appending salt convert string to sha512 hash and return back to SDK in `OnePayUJSHashCompletion`  as  (\[\<hashName>:\<hash>\]).

```swift
OnePayUJSHashCompletion -     (_ hashDict: [String: String]) -> Void
```

**Sample Code**

```swift
func generateHash(
    for param: [String : String],
    onCompletion: @escaping OnePayUJSKit.OnePayUJSHashCompletion
) {
    let commandName = param["hashName"] ?? ""
    let hashStringWithoutSalt = param["hashString"] ?? ""
    
    // get hash for "commandName" from server
    // get hash for "hashStringWithoutSalt" from server
    // After fetching hash set its value in below variable "hashValue"
    let hashValue = <fetch hash from server, on server add salt in last of hashStringWithoutSalt and create sha512 Hash>
    
    onCompletion([commandName : hashValue])
}

```

> 📘 Reference:
> 
> For more information on Static Hashing, refer to [Generate Static Hash](doc:generate-static-hash-ios).