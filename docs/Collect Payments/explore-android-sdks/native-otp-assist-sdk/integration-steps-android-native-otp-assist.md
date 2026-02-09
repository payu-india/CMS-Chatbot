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
  For more information on the generation of Payment Hash, refer to [Generate Static Hash](https://docs.payu.in/docs/generate-static-hash-android-sdk-pro).

  <Callout icon="🚧" theme="warn">
    **Generate hash on your server**: Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.
  </Callout>

  **Hash Formula**: `sha512(<key>|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||<Add Salt Value>)`

  Every transaction (payment or non-payment) needs a hash set up by you before sending the transaction details to PayU. Hash is required for PayU to validate the authenticity of the transaction. This hashing should be done on your server.
</Accordion>

<Accordion title="Payment Post Data" icon="fa-code">
  Use the Core SDK library to generate payment post data.

**Example Post Data Format:**

  ```
  key=YOUR_MERCHANT_KEY
  &txnid=TXN1234567890
  &amount=100.0
  &productinfo=Product Name
  &firstname=John
  &email=user@example.com
  &phone=9999999999
  &surl=https://yourdomain.com/success
  &furl=https://yourdomain.com/failure
  &hash=GENERATED_HASH
  &ccnum=5123456789012346
  &ccname=John Doe
  &ccvv=123
  &ccexpmon=12
  &ccexpyr=2025
  &bankcode=CC
  &pg=CC
  ```

  <Callout icon="📘" theme="info">
    **Note**: The post data must include all mandatory payment parameters along with card details for card payment processing.
  </Callout>
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

### Step 5: Implement Payment Callbacks

<Accordion title="5.1: PayUOtpAssistCallback Interface" icon="fa-code">
  Implement the `PayUOtpAssistCallback` interface to handle payment responses and events.

  ```java Java
  PayUOtpAssistCallback payUOtpAssistCallback = new PayUOtpAssistCallback() {
      
      @Override
      public void onPaymentSuccess(@Nullable String merchantResponse, 
                                    @Nullable String payUResponse) {
          // Handle successful payment
      }

      @Override
      public void onPaymentFailure(@Nullable String merchantResponse, 
                                    @Nullable String payUResponse) {
          // Handle failed payment
      }

      @Override
      public void onError(@Nullable String errorCode, 
                          @Nullable String errorMessage) {
          // Handle errors
      }

      @Override
      public boolean shouldHandleFallback(PayUAcsRequest payUAcsRequest) {
          // Handle fallback to bank page
          return true;
      }
  };
  ```
  ```kotlin Kotlin
  val payUOtpAssistCallback = object : PayUOtpAssistCallback {
      
      override fun onPaymentSuccess(merchantResponse: String?, 
                                     payUResponse: String?) {
          // Handle successful payment
      }

      override fun onPaymentFailure(merchantResponse: String?, 
                                     payUResponse: String?) {
          // Handle failed payment
      }

      override fun onError(errorCode: String?, 
                           errorMessage: String?) {
          // Handle errors
      }

      override fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest): Boolean {
          // Handle fallback to bank page
          return true
      }
  }
  ```
</Accordion>

<Accordion title="5.2: shouldHandleFallback - Handle Bank Page Redirection (Optional)" icon="fa-code">
  This is an optional callback to handle scenarios where the payment needs to be redirected to the bank's authentication page (3D Secure).

  **When to Use:** Override this method when you want to handle the bank page redirection flow yourself using Custom Browser.

  ```java Java
  @Override
  public boolean shouldHandleFallback(PayUAcsRequest payUAcsRequest) {
      // Option 1: Let SDK handle fallback (default)
      // return true;
      
      // Option 2: Handle fallback yourself using CustomBrowser
      CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey, txnId);
      
      // Set the issuerUrl and issuerPostData to open in WebView
      if (payUAcsRequest.getIssuerUrl() != null && 
          payUAcsRequest.getIssuerPostData() != null) {
          customBrowserConfig.setPostURL(payUAcsRequest.getIssuerUrl());
          customBrowserConfig.setPayuPostData(payUAcsRequest.getIssuerPostData());
      } else if (payUAcsRequest.getAcsTemplate() != null) {
          customBrowserConfig.setHtmlData(payUAcsRequest.getAcsTemplate());
      } else {
          // Set the first url to open in WebView
          customBrowserConfig.setPostURL(url);
          customBrowserConfig.setPayuPostData(payuConfig.getData());
      }
      
      // Launch CustomBrowser
      new CustomBrowser().addCustomBrowser(
          this,
          customBrowserConfig,
          customBrowserCallback
      );
      
      // Return false to indicate you're handling the fallback
      return false;
  }
  ```
  ```kotlin Kotlin
  override fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest): Boolean {
      // Option 1: Let SDK handle fallback (default)
      // return true
      
      // Option 2: Handle fallback yourself using CustomBrowser
      val customBrowserConfig = CustomBrowserConfig(merchantKey, txnId)
      
      // Set the issuerUrl and issuerPostData to open in WebView
      if (!payUAcsRequest.issuerUrl.isNullOrEmpty() && 
          !payUAcsRequest.issuerPostData.isNullOrEmpty()) {
          customBrowserConfig.postURL = payUAcsRequest.issuerUrl
          customBrowserConfig.payuPostData = payUAcsRequest.issuerPostData
      } else if (!payUAcsRequest.acsTemplate.isNullOrEmpty()) {
          customBrowserConfig.htmlData = payUAcsRequest.acsTemplate
      } else {
          // Set the first url to open in WebView
          customBrowserConfig.postURL = url
          customBrowserConfig.payuPostData = payuConfig.data
      }
      
      // Launch CustomBrowser
      CustomBrowser().addCustomBrowser(
          this,
          customBrowserConfig,
          customBrowserCallback
      )
      
      // Return false to indicate you're handling the fallback
      return false
  }
  ```

  **Return Values:**

  * `true` - SDK will handle the bank page redirection (default)
  * `false` - You will handle the bank page redirection using CustomBrowser

  **PayUAcsRequest Fields:**

  | Field            | Description                                                                                               |
  | ---------------- | --------------------------------------------------------------------------------------------------------- |
  | `issuerUrl`      | Bank/ACS page URL for 3D Secure authentication                                                            |
  | `issuerPostData` | POST data to be sent to the issuer URL. Use: `webView.postUrl(issuerUrl, issuerPostData.toByteArray())`   |
  | `acsTemplate`    | HTML template to load if `issuerUrl` is empty. Use: `webView.loadData(acsTemplate, "text/html", "UTF-8")` |

  <Callout icon="📘" theme="info">
    **When is this called?** This callback is invoked when:

    * Card requires 3D Secure authentication
    * Bank needs additional verification
    * ACS (Access Control Server) page needs to be shown
  </Callout>
</Accordion>

***

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
