---
title: iOS SDK Integration
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
# iOS SDK Integration

You can integrate Virtual card using PayUPPIiOS SDK in iOS. The following sections describe the procedure to integrate and sample app. 
You can integrate Virtual card using PayUPPIiOS SDK in iOS.

## Steps to Integrate
<Cards cols={3}>
  <Card title="Add the Dependency" icon="fa-cube">
    Add `PayUIndia-PPI-SDK` to your iOS project via Cocoapods or Swift Package Manager (SPM).
  </Card>
  <Card title="SDK Initialisation" icon="fa-code">
    Import `OnePayUJSKit`, create `OnePayUJSParams`, and call `showCards` with the required delegate callbacks.
  </Card>
  <Card title="Hashing" icon="fa-lock">
    Generate SHA-512 hash on your backend using the hash string provided by PayU and return it via `OnePayUJSHashCompletion`.
  </Card>
</Cards>
<Accordion title="Step 1: Add the Dependency" icon="fa-cube">

Add the following dependency in your app.

  <Accordion title="Cocoapods" icon="fa-box">

Use PayUIndia-PPI version 1.0.0.

```plaintext
pod 'PayUIndia-PPI-SDK'
```

  </Accordion>

  <Accordion title="SPM" icon="fa-box-open">

Use PayUIndia-PPI version 1.0.0.

```plaintext
.package(name: "PayUIndia-PPI-SDK", url: "https://github.com/payu-intrepos/PayUIndia-PPI", from: "1.0.0")
```

  </Accordion>

</Accordion>

<Accordion title="Step 2: SDK Initialisation" icon="fa-code">

1. Import the `OnePayUJSKit` SDK in your project.

```swift
import OnePayUJSKit
```

2. Create the `OnePayUJSParams` object.

```swift
OnePayUJSParams(
    merchantKey = <String - Merchant Key>,
    referenceId = <String - Any unique reference id>,
    environment = <Environment - Prod or Test>,
    mobileNumber = <String - user mobile number>,
    walletUrn = <String - User wallet urn linked with above mobile number>,
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

</Accordion>

<Accordion title="Step 3: Hashing" icon="fa-lock">

Get hash string in map `"hashString"` key and hash name `"hashName"` in `generateHash`. You need to send this string to server and append salt there. After appending salt, convert string to SHA-512 hash and return back to SDK in `OnePayUJSHashCompletion` as `([<hashName>:<hash>])`.

```swift
OnePayUJSHashCompletion - (_ hashDict: [String: String]) -> Void
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

<Callout icon="📘" theme="info">
  Reference: For more information on Static Hashing, refer to <Anchor label="Generate Static Hash" target="_blank" href="https://docs.payu.in/docs/generate-static-hash-ios">Generate Static Hash</Anchor>.
</Callout>

</Accordion>

## Sample app

You can download the sample app for the Virtual Card integration on the iOS SDK platform from the following Github location:

<https://github.com/payu-intrepos/PPIManageriOS>
