---
title: Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integration Steps - Android Native OTP Assist
  description: >-
    The Android Native OTP Assist SDK integration involves following specific
    steps, testing the integration, and completing a go-live checklist, with
    additional guidance on generating a static hash.
  keywords:
    - Android Native OTP Assist Integration Steps
    - Steps to integrate Android Native OTP Assist
  robots: index
next:
  description: ''
---
The Android Native OTP Assist SDK integration involves the following steps:

## SDK Integration

Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard** > **Settings** > **Payment methods**. Cards, UPI, and other payment methods are enabled by default, and PayU recommends you to enable other payment methods that are relevant to you.

### Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

***

### Step 2: Include the SDK in your application

Include the SDK in your application’s build.gradle:

```Text build.gradle
implementation 'in.payu:native-otp-assist:1.6.2'
```

### Step 3: Set up payment hash and post data

### Generate payment hash

For more information on the generation of Payment Hash, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

> 🚧 Remember
>
> Every transaction (payment or non-payment) needs a hash set up by you before sending the transaction details to PayU. Hash is required for PayU to validate the authenticity of the transaction. This hashing should be done on your server.

#### Payment post data

Use the Core SDK library to generate payment post data.

### Step 4: Initiate payment

#### Initialize Native OTP SDK

Initialize the Native OTP Assist SDK by providing the PayUOtpAssistConfig object having post data and reference to PayUOtpAssistCallback to listen to the SDK events similar to the following code block:

```java Java
PayUOtpAssistConfig payUOtpAssistConfig = PayUOtpAssistConfig();
payUOtpAssistConfig.setPostData("POST_DATA_FOR_TRANSACTION");
PayUOtpAssist.open(
Context context, 
PayUOtpAssistCallback payUOtpAssistCallback, 
PayUOtpAssistConfig payUOtpAssistConfig);
```
```kotlin Kotlin
val payUOtpAssistConfig = PayUOtpAssistConfig()
payUOtpAssistConfig.postData = "POST_DATA_FOR_TRANSACTION"
PayUOtpAssist.open(
    context: Context, 
    payUOtpAssistCallback: PayUOtpAssistCallback,  
    payUOtpAssistConfig: PayUOtpAssistConfig
) 
```

<Callout icon="📘" theme="info">
  **Remember**: This SDK will work only if the customer or the user provides consent for the app to read the SMS on their device.
</Callout>

PayU fetches the OTP through RECEIVE_SMS if the RECEIVE_SMS permission is granted. Otherwise, fetch the OTP using the Google Consent API. To understand the flow, refer to PayU OTP Parser.

#### Callbacks

The following is a list of callback functions provided by PayUOtpAssistCallback class:

* `fun onPaymentSuccess(merchantResponse: String?, payUResponse: String?)`: Called when payment succeeds. merchantResponse:
* `fun onPaymentFailure(merchantResponse: String?, payUResponse: String?)`: Called when a payment fails.
* `fun onError(errorCode: String?, errorMessage: String?)`: Called when we got some error, where:
  * `errorCode`: Error Code
  * `errorMessage`: Error Description
* `fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest)`: Boolean – It’s an optional callback, override when you want to handle the Bank page redirection flow. You just need to change the return value to false. You can also open CustomBrowser in fallback scenarios. The following code snippet is to launch the CustomBrowser.

```java Java
boolean shouldHandleFallback(PayUAcsRequest payUAcsRequest) {
  CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey, txnId);
  //Set the issuerUrl and issuerPostData to open in WebView for otp assist redirection to bank page
  if (payUAcsRequest.getIssuerUrl() != null && payUAcsRequest.getIssuerPostData() != null) {
    customBrowserConfig.setPostURL(payUAcsRequest.getIssuerUrl());
    customBrowserConfig.setPayuPostData(payUAcsRequest.getIssuerPostData());
  } else if (payUAcsRequest.getAcsTemplate() != null) {
    customBrowserConfig.setHtmlData(payUAcsRequest.getAcsTemplate());
  } else {
    //Set the first url to open in WebView
    customBrowserConfig.setPostURL(url);
    customBrowserConfig.setPayuPostData(payuConfig.getData);
  }
  return false;
}
```
```kotlin Kotlin
fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest): Boolean {
  val customBrowserConfig = CustomBrowserConfig(merchantKey, txnId)
   
  //Set the issuerUrl and issuerPostData to open in WebView for otp assist redirection to bank page
  if (!payUAcsRequest?.issuerUrl.isNullOrEmpty() && !payUAcsRequest?.issuerPostData.isNullOrEmpty()) {
    customBrowserConfig.postURL = payUAcsRequest?.issuerUrl
    customBrowserConfig.payuPostData = payUAcsRequest?.issuerPostData
  } else if (!payUAcsRequest?.acsTemplate.isNullOrEmpty()) {
    customBrowserConfig.htmlData = payUAcsRequest?.acsTemplate
  } else {
    //Set the first url to open in WebView
    customBrowserConfig.postURL = url
    customBrowserConfig.payuPostData = payuConfig.data
  }
  return false
}
```

You will get PayUAcsRequest on `shouldHandleFallback()` callback. Whether you will get `issuerUrl` and `issuerPostData` or acsTemplate on `PayUAcsRequest.acsTemplate` is the HTML string that you need to load to the Web view.

| PayUAcsRequest field | Description                                                                                                                                   |
| :------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| `issuerUrl`          | It’s the Bank/ACS page Url.                                                                                                                   |
| `issuerPostData`     | You need to load issuerUrl to the Webview along with this issuerPostdata string. Ex: webView.postUrl(issuerUrl, issuerPostData.toByteArray()) |
| `acsTemplate`        | If the `issuerUrl` is empty, you need to load acsTemplate to the Webview. Ex: webView.loadData(acsTemplate, “text/html”, “UTF-8”);            |

The following table lists error codes and their description:

| Error Code | Description                                              |
| :--------- | :------------------------------------------------------- |
| 1001       |                                                          |
| 1002       | Network timeout, please verify with your server.         |
| 1003       | Gateway timeout, please verify with your server.         |
| 1004       | User canceled it, please verify with your server.        |
| 1005       | Something went wrong, please verify with your server.    |
| 1006       | The bank page timed out, please verify with your server. |

<Callout icon="🚧" theme="warn">
  **Remember**: After you get the response from SDK, make sure to confirm it with the PayU server. It is recommended to implement the PayU Webhook or backend verify call from your backend.
</Callout>

### Step 5: Verify the transaction using webhook

After you get the response from SDK, make sure to confirm it with the PayU server.

Note: It is recommended to implement the PayU Webhook or backend verifies calls from your backend.

Webhook is a server-to-server callback. Once this feature is activated for merchants, PayU would send an S2S response, in addition to an SDK callback, to the merchant. It is recommended for the merchant process the transaction order status – based on the S2S response and not via the Browser Redirection/SDK callback response to ensure optimum translation outcomes. For more information on the Webhook implementation, refer to Web Checkout Integration Documentation > Webhooks,

Also, you can verify payment through polling, the transaction status after the SDK callback from your backend. For more information, refer to [Verify Payment API](https://docs.payu.in/docs/web-services-for-android-core-sdk#verify-payment-api).

[Test the Integration](https://docs.payu.in/docs/android-nativeotpassist-test-the-integration)

1. [Go-live Checklist](https://docs.payu.in/docs/android-nativeotpassist-go-live-checklist)

During the integration, refer the [Generate Static Hash](doc:generate-static-hash-android-sdk-pro) for hash generation details.
