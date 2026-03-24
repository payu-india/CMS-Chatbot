---
title: Copy of Integration Steps
deprecated: false
hidden: true
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
---
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

**Integration Steps**

<Cards columns={3}>
  <Card title="1. Create PayU Account" href="#step-1-create-a-payu-account">
    Register for a merchant account on PayU Dashboard
  </Card>

  <Card title="2. Include SDK" href="#step-2-include-the-sdk-in-your-application">
    Add the Native OTP Assist SDK dependency
  </Card>

  <Card title="3. Setup Hash & Post Data" href="#step-3-set-up-payment-hash-and-post-data">
    Generate payment hash and prepare post data
  </Card>

  <Card title="4. Initiate Payment" href="#step-4-initiate-payment">
    Initialize SDK and handle callbacks
  </Card>

  <Card title="5. Verify Transaction" href="#step-5-verify-the-transaction-using-webhook">
    Verify payment using webhook or API
  </Card>

  <Card title="6. Test & Go-Live" href="#step-2-test-the-integration-and-go-live">
    Test your integration and go live
  </Card>
</Cards>

## Step 1. SDK Integration

Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard** > **Settings** > **Payment methods**. Cards, UPI, and other payment methods are enabled by default, and PayU recommends you to enable other payment methods that are relevant to you.

### Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

### Step 2: Include the SDK in your application

<Accordion title="Gradle Dependency" icon="fa-cog">
  Include the SDK in your application's build.gradle:

  ```gradle
  implementation 'in.payu:native-otp-assist:1.6.3'
  ```
</Accordion>

### Step 3: Set up payment hash and post data

<Accordion title="Generate Payment Hash" icon="fa-key">
  For more information on the generation of Payment Hash, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

  > 🚧 Remember
  >
  > Every transaction (payment or non-payment) needs a hash set up by you before sending the transaction details to PayU. Hash is required for PayU to validate the authenticity of the transaction. This hashing should be done on your server.
</Accordion>

<Accordion title="Payment Post Data" icon="fa-code">
  Use the Core SDK library to generate payment post data.
</Accordion>

### Step 4: Initiate payment

<Accordion title="Initialize Native OTP SDK" icon="fa-play">
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

  PayU fetches the OTP through RECEIVE\_SMS if the RECEIVE\_SMS permission is granted. Otherwise, fetch the OTP using the Google Consent API. To understand the flow, refer to PayU OTP Parser.
</Accordion>

<Accordion title="Callbacks" icon="fa-exchange">
  The following is a list of callback functions provided by PayUOtpAssistCallback class:

  * `fun onPaymentSuccess(merchantResponse: String?, payUResponse: String?)`: Called when payment succeeds. merchantResponse:
  * `fun onPaymentFailure(merchantResponse: String?, payUResponse: String?)`: Called when a payment fails.
  * `fun onError(errorCode: String?, errorMessage: String?)`: Called when we got some error, where:
    * `errorCode`: Error Code
    * `errorMessage`: Error Description
  * `fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest)`: Boolean – It's an optional callback, override when you want to handle the Bank page redirection flow. You just need to change the return value to false. You can also open CustomBrowser in fallback scenarios. The following code snippet is to launch the CustomBrowser.

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

  | PayUAcsRequest field | Description                                                                                                                                    |
  | :------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------- |
  | `issuerUrl`          | It's the Bank/ACS page Url.                                                                                                                    |
  | `issuerPostData`     | You need to load issuerUrl to the Webview along with this issuerPostdata string. Ex: webView\.postUrl(issuerUrl, issuerPostData.toByteArray()) |
  | `acsTemplate`        | If the `issuerUrl` is empty, you need to load acsTemplate to the Webview. Ex: webView\.loadData(acsTemplate, "text/html", "UTF-8");            |
  
  ```callback
  PayUOtpAssistCallback payUOtpAssistCallback = new PayUOtpAssistCallback() {
            @Override
            public void onPaymentSuccess(@Nullable String s, @Nullable String s1) {

            }

            @Override
            public void onPaymentFailure(@Nullable String s, @Nullable String s1) {

            }

            @Override
            public void onError(@Nullable String s, @Nullable String s1) {

            }

            
  };
```

</Accordion>

<Accordion title="Error Codes" icon="fa-exclamation-triangle">
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
</Accordion>

### Step 5: Verify the transaction using webhook

<Accordion title="Webhook Verification" icon="fa-check">
  After you get the response from SDK, make sure to confirm it with the PayU server.

  Note: It is recommended to implement the PayU Webhook or backend verifies calls from your backend.

  Webhook is a server-to-server callback. Once this feature is activated for merchants, PayU would send an S2S response, in addition to an SDK callback, to the merchant. It is recommended for the merchant process the transaction order status – based on the S2S response and not via the Browser Redirection/SDK callback response to ensure optimum translation outcomes. For more information on the Webhook implementation, refer to Web Checkout Integration Documentation > Webhooks,

  Also, you can verify payment through polling, the transaction status after the SDK callback from your backend. For more information, refer to [Verify Payment API](https://docs.payu.in/docs/web-services-for-android-core-sdk#verify-payment-api).
</Accordion>

## Step 2. Test the Integration and Go-Live

### Test the Integration

After the integration is complete, you must test the integration before you go live and start collecting payment. You can start accepting actual payments from your customers once the test is successful.

You can make test payments using one of the payment methods configured at the Checkout.

<UPIIntentCallout />

<TestingChecklist />

***

<TestCardsCallout />

<Accordion title="Test Credentials for Net Banking" icon="fa-university">
  Use the following credentials to test the Net Banking integration:

  * **user name:** payu
  * **password**: payu
  * **OTP**: 123456
</Accordion>

<Accordion title="Test VPA for UPI" icon="fa-mobile">
  You can use either of the following VPAs to test your UPI-related integration:

  * [anything@payu](anything@payu)
  * [9999999999@payu.in](mailto:9999999999@payu.in)

  > ❗️ Callout
  >
  > The UPI in-app and UPI intent flow is not available in the Test mode.
</Accordion>

<Accordion title="Test Cards for EMI" icon="fa-credit-card">
  You can use the following Debit and Credit cards to test Emi integration.

  |              |                                         |
  | :----------- | :-------------------------------------- |
  | Kotak DC EMI | 1. **Card Number**: 4706-1378-0509-9594 |

  2. **Expiry**: any future date (mm/yy)
  3. **CVV**: 123
  4. **OTP**: 111111
  5. **Name**: Any name
  6. **Mobile Number**: 9123412345 (mandatory for EMI) |
     \| AXIS DC EMI  | 1) **Card Number**: 4011-5100-0000-0007

  2) **Expiry**: any future date (mm/yy)
  3) **CVV**: 123
  4) **OTP**: 111111
  5) **Name**: Any name
  6) **Mobile Number**: 9123412345 (mandatory for EMI) |
     \| HDFC CC EMI  | 1. **Card Number**: 4453-3410-65876437

  2. **Expiry**: any future date (mm/yy)
  3. **CVV**: 123
  4. **OTP**: 111111
  5. **Name**: Any name
  6. **Mobile Number**: 9123412345 (mandatory for EMI)  |
     \| ICICI CC EMI | 1) **Card Number**: 4453-3410-65876437

  2) **Expiry**: any future date (mm/yy)
  3) **CVV**: 123
  4) **OTP**: 111111
  5) **Name**: Any name
  6) **Mobile Number**: 9123412345 (mandatory for EMI)  |
</Accordion>

<Accordion title="Test Wallets" icon="fa-wallet">
  You can use the following wallets and their corresponding credentials to test wallet integration.

  <Table align={["left","left","left"]}>
    <thead>
      <tr>
        <th style={{ textAlign: "left" }}>
          Wallet
        </th>

        <th style={{ textAlign: "left" }}>
          Mobile Number
        </th>

        <th style={{ textAlign: "left" }}>
          OTP
        </th>
      </tr>
    </thead>

    <tbody>
      <tr>
        <td style={{ textAlign: "left" }}>
          PayTM
        </td>

        <td style={{ textAlign: "left" }}>
          7777777777
        </td>

        <td style={{ textAlign: "left" }}>
          888888
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          PhonePe
        </td>

        <td style={{ textAlign: "left" }}>
          Use the Phonepe Pre-Prod app for testing purposes as described in the following PhonePe doc. location: [https://developer.phonepe.com/v1/docs/setting-up-test-account](https://developer.phonepe.com/v1/docs/setting-up-test-account)
          Download the app and register your mobile number and follow the instructions as described in the above PhonePe docs.
        </td>

        <td style={{ textAlign: "left" }}>
          NA
        </td>
      </tr>

      <tr>
        <td style={{ textAlign: "left" }}>
          AmazonPay
        </td>

        <td style={{ textAlign: "left" }}>
          You can test using your original Amazon account details.
        </td>

        <td style={{ textAlign: "left" }} />
      </tr>
    </tbody>
  </Table>
</Accordion>

<Go_Live_Checklist />

<br />