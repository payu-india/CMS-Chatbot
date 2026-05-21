---
title: Android SDK Integration
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
You can integrate Virtual card using PayUPPIAndroidSDK in Android. The following sections describe the procedure to integrate and sample app.
You can integrate Virtual card using PayUPPIAndroidSDK in Android.
## Steps to Integrate
<Cards cols={3}>
  <Card title="Gradle Changes" icon="fa-cube">
    Add the `payu-ppi-sdk` dependency to your app-level Gradle file to get started.
  </Card>
  <Card title="SDK Initialisation" icon="fa-code">
    Create a `OnePayUJSParams` object and call `showCards` with the required activity, params, and listener.
  </Card>
  <Card title="Construct Hash" icon="fa-lock">
    Generate SHA-512 hash on your backend using the hash string from PayU and return it via `OnePayUJSHashGenerationListener`.
  </Card>
</Cards>

<Accordion title="Step 1: Gradle Changes" icon="fa-cube">

Add the following dependency in your app level gradle file.

```plaintext
implementation 'in.payu:payu-ppi-sdk:1.0.1'
```

</Accordion>

<Accordion title="Step 2: SDK Initialisation" icon="fa-code">

1. Create a `OnePayUJSParams` object.

```kotlin
OnePayUJSParams(
    environment = <Environment - Prod or Test>,
    merchantKey = <String - Merchant Key>,
    mobileNumber = <String - user mobile number>,
    walletIdentifier = <String - merchant wallet Identifier>,
    walletUrn = <String - User wallet urn linked with above mobile number>,
    referenceId = <String - Any unique reference id>
)
```

2. Call the `showCards` function.

```kotlin
onePayUJSSDK.showCards(
    activity,
    onePayUJSParams,
    onePayUJSListener
) {
    val hashMap = HashMap<String, String?>()
    val hashGenerationOnePayUJKListener = OnePayUJSHashGenerationListener()
    // 1. onCancel() - If user press back button on card page or verify otp page
    // 2. fun onError(code: Int, message: String) - If any error occurred
    // 3. fun generateHash(map: HashMap<String, String?>, hashGenerationOnePayUJKListener: OnePayUJSHashGenerationListener) - Create and send dynamic hash
}.linkToText()
```

</Accordion>

<Accordion title="Step 3: Construct Hash" icon="fa-lock">

You will get the hash string in map `hashString` key and hash name `hashName` in `generateHash`. You need to send this string to server and append salt there. After appending salt, convert string to SHA-512 hash and return back to SDK in `OnePayUJSHashGenerationListener` `onHashGenerated` as `([<hashName>:<hash>])`. For more information, refer to [Generate Static Hash](https://docs.payu.in/docs/generate-static-hash-android-sdk-pro).

```kotlin
OnePayUJSHashGenerationListener - fun onHashGenerated(map: HashMap<String, String>)
```

**Sample Code**

```kotlin
override fun generateHash(map: HashMap<String, String?>, hashGenerationOnePayUJKListener: OnePayUJSHashGenerationListener) {
    if (map.containsKey("hashString") && map.containsKey("hashName")) {
        val hashStringWithoutSalt = map["hashString"]
        val commandName = map["hashName"]
        // get hash for "commandName" from server
        // get hash for "hashStringWithoutSalt" from server
        // After fetching hash set its value in below variable "hashValue"
        val hash = <fetch hash from server, on server add salt in last of hashStringWithoutSalt and create sha512 Hash>
        if (!TextUtils.isEmpty(hash)) {
            val hashMap: HashMap<String, String> = HashMap()
            hashMap[hashName ?: ""] = hash ?: ""
            hashGenerationOnePayUJKListener.onHashGenerated(hashMap)
        }
    }
}
```

</Accordion>

## Sample app

You can download the sample app for Virtual Card integration for Android SDK from the following Github location:

<https://github.com/payu-intrepos/PPIManagerAndroid>
