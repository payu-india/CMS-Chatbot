---
title: Integration Steps
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Integration Steps - Android Customer Browser
  description: >-
    Step-by-step guide to integrate Android Custom Browser SDK with PayU. Covers
    build.gradle, test credentials, and go-live checklist.
  keywords:
    - Integration Steps - Android Customer Browser
    - Android Customer Browser Integration Steps
    - Integrate Android Customer Browser
    - ' Android Customer Browser Integration Steps'
    - ' Custom Browser Android Integration Steps'
    - Custom Browser Mobile SDK - Android Integration Steps
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
  title: Integration Steps - Android Customer Browser
  description: ''
  keywords:
    - Integration Steps - Android Customer Browser
    - Android Customer Browser Integration Steps
    - Integrate Android Customer Browser
    - ' Android Customer Browser Integration Steps'
    - ' Custom Browser Android Integration Steps'
    - Custom Browser Mobile SDK - Android Integration Steps
  robots: index
next:
  description: ''
---

The Android Customer Browser integration involves the following steps:

<Cards columns={3}>
  <Card title="1. SDK Integration" href="#sdk-integration">
    Set up build.gradle, check payment availability, and invoke CustomBrowser

    <br />
  </Card>

  <Card title="2. Test the Integration" href="#test-the-integration">
    Test the integration with test credentials before going live

    <br />
  </Card>

  <Card title="3. Go-live Checklist" href="#go-live-checklist">
    Configure production settings, verify payment method, and webhooks
  </Card>

  <br />
</Cards>

## SDK Integration

Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard** > **Settings** > **Payment methods**. PayU enable Cards, UPI, and other payment methods by default, and we recommend that you enable other payment methods that are relevant to you. For more information, refer to <Anchor label="Configure Checkout Payment Methods" target="_blank" href="https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings">Configure Checkout Payment Methods</Anchor>.

### Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

***

### Step 2: Include the SDK in your app build.gradle

<Accordion title="2.1: Add SDK Dependency" icon="fa-code">
  Add the following dependency in your application's `build.gradle`:

  ```gradle
  implementation 'in.payu:payu-custom-browser:7.16.3'
  ```

  <Callout icon="❗️" theme="error">
    **Maven Central**: PayU has moved to Maven Central, update your existing dependency with the above configuration.
  </Callout>
</Accordion>

<Accordion title="2.2: Configure Java 8 Compatibility (If Required)" icon="fa-code">
  <Callout icon="🚧" theme="warn">
    **Watch Out**: If you are getting the following error: `Default interface methods are only supported starting with Android N (--min-api 24)`
  </Callout>

  Add the following compileOptions in your app's `build.gradle`:

  ```gradle
  android {
      compileOptions {
          sourceCompatibility JavaVersion.VERSION_1_8
          targetCompatibility JavaVersion.VERSION_1_8
      }
      kotlinOptions {
          jvmTarget = '1.8'
      }
  }
  ```

  > ❗️ **Compatibility Requirements:**
  >
  > 1. **Android SDK** — Version 21 and above
  > 2. **Compile SDK** — version 31 and above
</Accordion>

<Accordion title="2.3: Add SMS Permission (For OTP Assist)" icon="fa-code">
  Add the following permission in your application's `AndroidManifest.xml`:

  ```xml
  <uses-permission android:name="android.permission.RECEIVE_SMS" />
  ```

  <Callout icon="👍" theme="okay">
    **Tip**: Merchants are advised to add this permission to support OTP assist feature. In case your application supports a minimum SDK of less than 20, handle permission requests in your surl/furl.
  </Callout>
</Accordion>

<Accordion title="2.4: Add UPI SDK Dependency (Version 7.4.0+ - Only For UPI)" icon="fa-code">
  **Mandatory for UPI Payments**: From version 7.4.0 onwards, if you want to accept payments through any of the following UPI options, you must import the UPI SDK dependency:

  * UPI Intent
  * UPI Collect
  * Google Pay
  * PhonePe

  Add the following dependency in your application's `build.gradle`:

  ```gradle
  implementation 'in.payu:upisdk:1.8.8'
  ```
</Accordion>

***

### Step 3: Check Payment Option Availability (Optional)

<Accordion title="3.1: Overview" icon="fa-info">
  Before displaying payment options like Samsung Pay, PhonePe, or Google Pay, you must check if they are available on the user's device.
</Accordion>

<Accordion title="3.2: Method Signature" icon="fa-code">
  ```java
  new CustomBrowser().checkForPaymentAvailability(
      Activity activity,
      PaymentOption paymentOption,
      PayUCustomBrowserCallback payUCustomBrowserCallback,
      String paymentOptionHash,
      String merchantKey,
      String user_credentials
  )
  ```

  **Parameters:**

  | Parameter                   | Type                      | Description                                                                     |
  | --------------------------- | ------------------------- | ------------------------------------------------------------------------------- |
  | `activity`                  | Activity                  | Current activity instance                                                       |
  | `paymentOption`             | PaymentOption             | Payment option type (e.g., `PaymentOption.SAMSUNGPAY`, `PaymentOption.PHONEPE`) |
  | `payUCustomBrowserCallback` | PayUCustomBrowserCallback | Callback interface for handling responses                                       |
  | `paymentOptionHash`         | String                    | SHA-512 hash for payment option verification                                    |
  | `merchantKey`               | String                    | Your PayU merchant key                                                          |
  | `user_credentials`          | String                    | User credentials or use "default"                                               |
</Accordion>

<Accordion title="3.3: Generate PaymentOption Hash" icon="fa-code">
  **Hash Formula**: `sha512(key|command|var1|salt)`

  Where:

  * `key` = Your merchant key
  * `command` = `"payment_related_details_for_mobile_sdk"`
  * `var1` = User credentials or "default"
  * `salt` = Your merchant salt

  For more information, refer to [Generate Static Hash](https://docs.payu.in/docs/generate-static-hash).
</Accordion>

<Accordion title="3.4: Example Implementation" icon="fa-code">
  ```java
  new CustomBrowser().checkForPaymentAvailability(
      this,
      PaymentOption.PHONEPE,
      payUCustomBrowserCallback,
      paymentOptionHash,
      merchantKey,
      "default"
  );
  ```
</Accordion>

***

### Step 4: Build Payment Configuration

<Accordion title="4.1: Create CustomBrowserConfig" icon="fa-code">
  Create a basic configuration object with mandatory parameters:

  ```java
  CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey, txnId);
  customBrowserConfig.setPayuPostData(postData);
  customBrowserConfig.setPostUrl(postUrl);
  ```

  **Post URLs:**

  | Environment    | URL                               |
  | -------------- | --------------------------------- |
  | **Production** | `https://secure.payu.in/_payment` |
  | **Staging**    | `https://test.payu.in/_payment`   |
</Accordion>

<Accordion title="4.2: Mandatory Configuration Parameters" icon="fa-code">
  #### Set Post Data

  ```java
  customBrowserConfig.setPayuPostData(String postData);
  ```

  **Description**: Contains all payment parameters including transaction details, user information, and hash.

  #### Set Post URL

  ```java
  customBrowserConfig.setPostUrl(String postUrl);
  ```

  **Values**:

  * Production: `https://secure.payu.in/_payment`
  * Staging: `https://test.payu.in/_payment`
</Accordion>

<Accordion title="4.3: Optional Configuration Parameters" icon="fa-code">
  #### HTML Data (Available from v7.2.2+)

  Set HTML string received from PayU web service using Server-to-Server call:

  ```java
  customBrowserConfig.setHtmlData(String htmlData);
  ```

  #### ViewPort Enable

  Control viewport settings for the web view:

  ```java
  customBrowserConfig.setViewPortWideEnable(boolean viewPortWide);
  ```

  | Value   | Description                     |
  | ------- | ------------------------------- |
  | `true`  | Enable wide viewport            |
  | `false` | Disable wide viewport (default) |

  #### Progress Dialog Custom View

  Set a custom view for the progress dialog:

  ```java
  customBrowserConfig.setProgressDialogCustomView(View progressDialogCustomView);
  ```

  **Use Case**: Brand the loading experience with your custom UI.

  #### Auto Approve

  Control OTP auto-fill and approval behavior:

  ```java
  customBrowserConfig.setAutoApprove(boolean isAutoApprove);
  ```

  | Value   | Description                                                |
  | ------- | ---------------------------------------------------------- |
  | `true`  | OTP will be fetched and approved automatically             |
  | `false` | OTP will be fetched but requires manual approval (default) |

  **Requirements**: Requires `RECEIVE_SMS` permission.

  #### Merchant Response Timeout

  Set timeout for success/failure URL response:

  ```java
  customBrowserConfig.setMerchantResponseTimeout(int merchantResponseTimeout);
  ```

  **Parameter**: Timeout in milliseconds\
  **Default**: System default timeout

  #### Auto Select OTP

  Automatically select OTP option when available:

  ```java
  customBrowserConfig.setAutoSelectOTP(boolean isAutoSelect);
  ```

  | Value   | Description                                        |
  | ------- | -------------------------------------------------- |
  | `true`  | OTP option will be selected automatically          |
  | `false` | User will choose between password or OTP (default) |

  #### Merchant SMS Permission

  Control SMS permission dialog display (Android M only):

  ```java
  customBrowserConfig.setMerchantSMSPermission(boolean showPermission);
  ```

  | Value   | Description               |
  | ------- | ------------------------- |
  | `true`  | Shows permission dialog   |
  | `false` | No dialog shown (default) |

  #### Package Name for Specific App

  Specify a particular UPI app to invoke instead of showing generic intent chooser:

  ```java
  customBrowserConfig.setPackageNameForSpecificApp(String packageName);
  ```

  **Common Package Names**:

  * PhonePe: `com.phonepe.app`
  * Google Pay: `com.google.android.apps.nbu.paisa.user`
  * Paytm: `net.one97.paytm`

  **Requirements**: Must include UPI SDK dependency.

  #### Disable Intent Seamless Failure

  Disable manual VPA fallback option from generic Intent tray:

  ```java
  customBrowserConfig.setDisableIntentSeamlessFailure(CustomBrowserConfig.DISABLE);
  ```

  **Values**:

  * `CustomBrowserConfig.DISABLE` - Disable manual VPA fallback
  * `CustomBrowserConfig.ENABLE` - Enable manual VPA fallback (default)

  **Requirements**: Must include UPI SDK dependency.

  #### Domain URL List to Unclear

  Specify URLs for which cookies should not be cleared:

  ```java
  ArrayList<String> protectedUrls = new ArrayList<>();
  protectedUrls.add("https://yourdomain.com");
  customBrowserConfig.setDomainUrlListToUnclear(protectedUrls);
  ```

  **Use Case**: Preserve session cookies for specific domains during payment flow.

  #### Enable SSL Dialog

  Show a popup message when SSL errors occur:

  ```java
  customBrowserConfig.setEnableSslDialog(boolean enable);
  ```

  | Value   | Description                          |
  | ------- | ------------------------------------ |
  | `true`  | Show SSL error dialog to user        |
  | `false` | Handle SSL errors silently (default) |

  **Note**: PayU automatically redirects users to bank pages even with SSL errors.
</Accordion>

***

### Step 5: Prepare Post Data Parameters

Use the Core SDK library to generate payment post data

<Callout icon="🚧" theme="warn">
  **Payment Mode-Specific Parameters Required**: You **MUST** configure the `pg` (Payment Gateway) and `bankcode` parameters in your post data based on the payment method selected by the user. Each payment mode requires specific parameters.
</Callout>

<Accordion title="5.1: Understanding Post Data Structure" icon="fa-info">
  Post data contains all payment parameters that will be sent to PayU payment gateway. The required parameters vary based on the selected payment mode (Card, Net Banking, UPI, Wallet, etc.).

  <Callout icon="📘" theme="info">
    **Recommended Approach**: Use the **Core SDK library** to generate payment post data. This ensures correct parameter formatting and reduces the risk of errors.
  </Callout>

  **Basic Structure:**

  ```
  key=YOUR_KEY
  &txnid=UNIQUE_TXN_ID
  &amount=100.0
  &productinfo=Product Name
  &firstname=John
  &email=user@example.com
  &phone=9999999999
  &surl=https://yourdomain.com/success
  &furl=https://yourdomain.com/failure
  &hash=GENERATED_HASH
  &pg=PAYMENT_GATEWAY_CODE
  &bankcode=BANK_OR_METHOD_CODE
  &[additional payment-specific parameters]
  ```

  <Callout icon="❗️" theme="error">
    **Important**: The `pg` and `bankcode` values must match the selected payment method. Incorrect values will cause payment failures.
  </Callout>
</Accordion>

<Accordion title="5.2: Common Mandatory Parameters" icon="fa-list">
  These parameters are required for **all payment modes**:

  | Parameter     | Description               | Example                          |
  | ------------- | ------------------------- | -------------------------------- |
  | `key`         | Your PayU merchant key    | `gtKFFx`                         |
  | `txnid`       | Unique transaction ID     | `TXN1234567890`                  |
  | `amount`      | Transaction amount        | `100.0`                          |
  | `productinfo` | Product description       | `Macbook Pro`                    |
  | `firstname`   | Customer first name       | `John`                           |
  | `email`       | Customer email            | `user@example.com`               |
  | `phone`       | Customer phone number     | `9999999999`                     |
  | `surl`        | Success callback URL      | `https://yourdomain.com/success` |
  | `furl`        | Failure callback URL      | `https://yourdomain.com/failure` |
  | `hash`        | SHA-512 hash for security | Generated hash string            |

  <Callout icon="📘" theme="info">
    **Optional Parameters**: `udf1` to `udf5` (User Defined Fields), `device_type`, and other custom fields can be added based on your requirements.
  </Callout>
</Accordion>

<Accordion title="5.3: Payment Mode-Specific Parameters (CRITICAL)" icon="fa-exclamation-triangle">
  Each payment mode requires specific parameters in addition to the common mandatory parameters. You must add the correct `pg`, `bankcode`, and mode-specific fields based on the user's selection.

  **📚 Complete Parameter Reference:**

  For detailed information on required parameters for each payment mode, refer to:

  **[Generate Request for Payment - Android Core SDK](https://docs.payu.in/docs/integration-steps-android-core-sdk#step-5-generate-request-for-payment)**

  This documentation provides:

  * Required parameters for each payment mode (Card, Net Banking, UPI, Wallet, EMI, etc.)
  * Payment Gateway (`pg`) codes for each mode
  * Bank codes (`bankcode`) for each payment method
  * Additional mode-specific parameters (e.g., card details for CC/DC, VPA for UPI)
  * Complete sample payloads for all payment modes

  <Callout icon="🚧" theme="warn">
    **Example Payment Modes:**

    * **Credit/Debit Card**: Requires `ccnum`, `ccname`, `ccvv`, `ccexpmon`, `ccexpyr`, `pg=CC/DC`, `bankcode=CC/DC`
    * **Net Banking**: Requires `pg=NB`, `bankcode=<BANK_CODE>` (e.g., SBIB, AXIB, HDFCB)
    * **UPI Intent**: Requires `pg=UPI`, specific UPI parameters
    * **UPI Collect**: Requires `pg=UPI`, `vpa=user@upi`, `bankcode=UPI`
    * **Wallets**: Requires `pg=WALLET`, `bankcode=<WALLET_CODE>` (e.g., PAYTM, PHONEPE)

    **Always refer to the official documentation for the complete and up-to-date parameter list.**
  </Callout>
</Accordion>

<Accordion title="5.4: Payment Gateway (pg) and Bank Codes Reference" icon="fa-book">
  **Payment Gateway (pg) Codes:**

  | Code     | Payment Method                 |
  | -------- | ------------------------------ |
  | `CC`     | Credit Card                    |
  | `DC`     | Debit Card                     |
  | `NB`     | Net Banking                    |
  | `UPI`    | UPI (Intent/Collect)           |
  | `CASH`   | Cash Card                      |
  | `EMI`    | EMI                            |
  | `WALLET` | Wallets (Paytm, PhonePe, etc.) |

  **Bank Code References:**

  For complete list of bank codes and payment method codes, refer to:

  * **[Bank and Card Codes for Integration](https://docs.payu.in/docs/bank-and-card-codes-for-integration)** - Complete reference for all bank codes, card codes, and wallet codes
  * **[Net Banking Codes](https://docs.payu.in/docs/net-banking-codes)** - Specific codes for net banking banks
  * **[Supported Payment Methods](https://docs.payu.in/docs/supported-payment-methods)** - All available payment methods and their codes

  <Callout icon="👍" theme="okay">
    **Quick Examples:**

    * State Bank of India: `bankcode=SBIB`, `pg=NB`
    * Credit Card: `bankcode=CC`, `pg=CC`
    * Paytm Wallet: `bankcode=PAYTM`, `pg=CASH`
  </Callout>
</Accordion>

<Accordion title="5.5: Using Core SDK to Generate Post Data (Recommended)" icon="fa-code">
  **Recommended Approach**: Use the PayU Core SDK library to generate payment post data. This ensures proper formatting and parameter handling.

  ```java Java
  // Using Core SDK to generate post data
  PayuConfig payuConfig = new PayuConfig();
  payuConfig.setData(paymentParams.getParams());

  // Get the formatted post data string
  String postData = payuConfig.getData();

  // Use this post data with CustomBrowser
  customBrowserConfig.setPayuPostData(postData);
  ```
  ```kotlin Kotlin
  // Using Core SDK to generate post data
  val payuConfig = PayuConfig()
  payuConfig.data = paymentParams.params

  // Get the formatted post data string
  val postData = payuConfig.data

  // Use this post data with CustomBrowser
  customBrowserConfig.payuPostData = postData
  ```

  <Callout icon="👍" theme="okay">
    **Benefits of using Core SDK:**

    * Automatic parameter formatting
    * URL encoding handled automatically
    * Reduces manual errors
    * Ensures compliance with PayU standards
  </Callout>
</Accordion>

<Accordion title="5.6: Sample Post Data Example (Card Payment)" icon="fa-code">
  Here's a sample for credit card payment to understand the structure:

  ```
  key=gtKFFx
  &txnid=TXN1705055037779
  &amount=100.0
  &productinfo=Macbook+Pro
  &firstname=John
  &email=user@example.com
  &phone=9999999999
  &surl=https://yourdomain.com/success
  &furl=https://yourdomain.com/failure
  &hash=a9c33e...
  &pg=CC
  &bankcode=CC
  &ccnum=5123456789012346
  &ccname=John+Doe
  &ccvv=123
  &ccexpmon=12
  &ccexpyr=2025
  &device_type=1
  ```

  <Callout icon="🚧" theme="warn">
    **Important**: This is a manual example for reference. It's recommended to use the Core SDK library (as shown in section 5.5) to generate post data instead of manually creating the string.
  </Callout>

  <Callout icon="📘" theme="info">
    **For other payment modes** (Net Banking, UPI, Wallets, etc.), refer to the complete documentation:

    **[Generate Request for Payment](https://docs.payu.in/docs/integration-steps-android-core-sdk#step-5-generate-request-for-payment)**
  </Callout>
</Accordion>

***

### Step 6: Implement Payment Callbacks

<Accordion title="6.1: PayUCustomBrowserCallback Interface Overview" icon="fa-info">
  Implement this interface to handle payment responses and events. All callback methods must be implemented for proper payment flow handling.

  #### Sample Code for PayUCustomBrowserCallback

  Below is the complete implementation of `PayUCustomBrowserCallback` interface. This callback handles all payment events including success, failure, errors, and WebView customization.

  ```java Java
  PayUCustomBrowserCallback payUCustomBrowserCallback = new PayUCustomBrowserCallback() {
      
      @Override
      public void onPaymentFailure(String payuResponse, String merchantResponse) {
          // Called when payment fails
          Intent intent = new Intent();
          intent.putExtra(getString(R.string.cb_result), merchantResponse);
          intent.putExtra(getString(R.string.cb_payu_response), payuResponse);
          setResult(Activity.RESULT_CANCELED, intent);
          finish();
      }
      
      @Override
      public void onPaymentTerminate() {
          // Called when payment is terminated by user or system
          // Handle cleanup or show appropriate message to user
      }
      
      @Override
      public void onPaymentSuccess(String payuResponse, String merchantResponse) {
          // Called when payment completes successfully
          Intent intent = new Intent();
          intent.putExtra(getString(R.string.cb_result), merchantResponse);
          intent.putExtra(getString(R.string.cb_payu_response), payuResponse);
          setResult(Activity.RESULT_OK, intent);
          finish();
      }
      
      @Override
      public void onCBErrorReceived(int code, String errormsg) {
          // Called when CustomBrowser encounters an error
          // Handle errors based on error code
          // Refer to error codes table in section 6.4 for details
      }
      
      @Override
      public void setCBProperties(WebView webview, Bank payUCustomBrowser) {
          // Customize WebView settings and behavior
          webview.setWebChromeClient(new PayUWebChromeClient(payUCustomBrowser));
          webview.setWebViewClient(new PayUWebViewClient(payUCustomBrowser, merchantKey));
          webview.postUrl(url, payuConfig.getData().getBytes());
          // Comment above line if you are using CustomBrowser v6.1 or above
      }
      
      @Override
      public void onBackApprove() {
          // Called when user confirms exit from payment screen
          PaymentsActivity.this.finish();
      }
  };
  ```
</Accordion>

**Callback Methods Explanation:**

* **onPaymentSuccess**: Called when payment completes successfully. Receives PayU response and merchant response from success URL (surl).
* **onPaymentFailure**: Called when payment fails. Receives PayU response and merchant response from failure URL (furl).
* **onPaymentTerminate**: Called when payment is terminated by user or system.
* **onCBErrorReceived**: Called when CustomBrowser encounters an error. Use error code to handle specific errors.
* **setCBProperties**: Customize WebView settings and behavior. Set WebChromeClient and WebViewClient for handling page navigation.
* **onBackApprove**: Called when user confirms exit from payment screen via back button.
* **onBackDismiss**: Called when user dismisses the exit confirmation dialog.
* **onBackButton**: Customize the back button alert dialog appearance and behavior.
* **isPaymentOptionAvailable** (v7.1.3+): Response callback for payment option availability check (e.g., Samsung Pay VPA).
* **onVpaEntered** (v7.3.0+): Called when user enters VPA for Generic Intent flow. Calculate and verify VPA hash using this callback.

<Callout icon="👍" theme="okay">
  **Best Practice**: Always verify payment status on your server using the Verify Payment API, regardless of the callback received. This ensures accurate transaction status even in cases of network issues or callback failures.
</Callout>

<Accordion title="6.2: onPaymentSuccess - Handle Successful Payment" icon="fa-code">
  Called when payment completes successfully.

  ```java
  @Override
  public void onPaymentSuccess(String payuResponse, String merchantResponse) {
      // Handle successful payment
      // payuResponse: Response from PayU
      // merchantResponse: Response from your server (surl)
      
      Intent intent = new Intent();
      intent.putExtra("result", merchantResponse);
      intent.putExtra("payu_response", payuResponse);
      setResult(Activity.RESULT_OK, intent);
      finish();
  }
  ```

  **Parameters**:

  * `payuResponse` (String): Complete response from PayU gateway
  * `merchantResponse` (String): Response from your success URL (surl)
</Accordion>

<Accordion title="6.3: onPaymentFailure - Handle Failed Payment" icon="fa-code">
  Called when payment fails.

  ```java
  @Override
  public void onPaymentFailure(String payuResponse, String merchantResponse) {
      // Handle failed payment
      
      Intent intent = new Intent();
      intent.putExtra("result", merchantResponse);
      intent.putExtra("payu_response", payuResponse);
      setResult(Activity.RESULT_CANCELED, intent);
      finish();
  }
  ```

  **Parameters**:

  * `payuResponse` (String): Complete response from PayU gateway
  * `merchantResponse` (String): Response from your failure URL (furl)

  ***
</Accordion>

<Accordion title="6.4: onCBErrorReceived - Handle CustomBrowser Errors" icon="fa-code">
  Called when CustomBrowser encounters an error.

  ```java
  @Override
  public void onCBErrorReceived(int errorCode, String errorMsg) {
      // Handle CustomBrowser errors
      Toast.makeText(this, "Error: " + errorMsg, Toast.LENGTH_LONG).show();
  }
  ```

  **Error Codes Reference:**

  | Code | Error Message                                   | Description                                    |
  | ---- | ----------------------------------------------- | ---------------------------------------------- |
  | 1    | VENDOR\_NOT\_SUPPORTED                          | Device vendor is not supported                 |
  | 2    | DEVICE\_NOT\_SUPPORTED                          | Device is not supported                        |
  | 3    | APP\_VERSION\_MISMATCH                          | Samsung Pay version doesn't meet requirements  |
  | 4    | COUNTRY\_NOT\_SUPPORTED                         | Device country not supported by Samsung Pay    |
  | 5    | MERCHANT\_KEY\_NOT\_REGISTER\_FOR\_SAMSUNG\_PAY | Merchant not registered for Samsung Pay        |
  | 6    | CONTEXT\_NULL                                   | Context is null                                |
  | 7    | PAYMENT\_ID\_NOT\_PRESENT                       | Check your post data                           |
  | 1001 | DEVICE\_NOT\_SUPPORTED                          | Tez app not present and enablewebflow is false |
  | 1002 | MERCHANT\_INFO\_NOT\_PRESENT                    | Check your post data and hash                  |
</Accordion>

<Accordion title="6.5: setCBProperties - Customize WebView Settings" icon="fa-code">
  Customize WebView settings and behavior.

  ```java
  @Override
  public void setCBProperties(WebView webview, Bank payUCustomBrowser) {
      webview.setWebChromeClient(new PayUWebChromeClient(payUCustomBrowser));
      webview.setWebViewClient(new PayUWebViewClient(payUCustomBrowser, merchantKey));
      // Note: For CustomBrowser v6.1+, comment the postUrl line if using setHtmlData
  }
  ```

  **Parameters**:

  * `webview` (WebView): The WebView instance used for payment
  * `payUCustomBrowser` (Bank): PayU CustomBrowser instance
</Accordion>

<Accordion title="6.6: onPaymentTerminate - Handle Payment Termination" icon="fa-code">
  Called when payment is terminated by user or system.

  ```java
  @Override
  public void onPaymentTerminate() {
      // Handle payment termination
      Toast.makeText(this, "Payment terminated", Toast.LENGTH_SHORT).show();
  }
  ```
</Accordion>

<Accordion title="6.7: onBackButton - Customize Exit Dialog (Optional)" icon="fa-code">
  Customize the back button alert dialog.

  ```java
  @Override
  public void onBackButton(AlertDialog.Builder alertDialogBuilder) {
      // Customize alert dialog
      alertDialogBuilder.setTitle("Exit Payment?");
      alertDialogBuilder.setMessage("Are you sure you want to cancel this payment?");
  }
  ```
</Accordion>

<Accordion title="6.8: onBackApprove - Handle Exit Confirmation (Optional)" icon="fa-code">
  Called when user confirms exit from alert dialog.

  ```java
  @Override
  public void onBackApprove() {
      // Handle user confirming exit
      finish();
  }
  ```
</Accordion>

<Accordion title="6.9: onBackDismiss - Handle Exit Cancellation (Optional)" icon="fa-code">
  Called when user cancels exit from alert dialog.

  ```java
  @Override
  public void onBackDismiss() {
      // Handle user canceling exit
      super.onBackDismiss();
  }
  ```
</Accordion>

<Accordion title="6.10: isPaymentOptionAvailable - Check Option Availability (v7.1.3+)" icon="fa-code">
  Response callback for payment option availability check.

  ```java
  @Override
  public void isPaymentOptionAvailable(CustomBrowserResultData resultData) {
      PaymentOption option = resultData.getPaymentOption();
      boolean isAvailable = resultData.isPaymentOptionAvailable();
      String samsungPayVpa = resultData.getSamsungPayVpa();
      String errorMessage = resultData.getErrorMessage();
      
      if (isAvailable) {
          // Show payment option to user
          Toast.makeText(this, option + " is available", Toast.LENGTH_SHORT).show();
      } else {
          // Hide or disable payment option
          Log.e("PayU", "Payment option unavailable: " + errorMessage);
      }
  }
  ```

  **CustomBrowserResultData Methods**:

  * `getPaymentOption()`: Returns PaymentOption type
  * `isPaymentOptionAvailable()`: Returns boolean indicating availability
  * `getSamsungPayVpa()`: Returns Samsung Pay VPA (if applicable)
  * `getErrorMessage()`: Returns error message if unavailable
</Accordion>

<Accordion title="6.11: onVpaEntered - Handle VPA Verification (v7.3.0+)" icon="fa-code">
  Handle UPI Collect flow VPA verification.

  ```java
  @Override
  public void onVpaEntered(String vpa, PackageListDialogFragment packageListDialogFragment) {
      // Generate VPA verification hash
      String verifyVpaHash = generateVerifyVpaHash(vpa);
      
      // Provide hash to verify VPA
      packageListDialogFragment.verifyVpa(verifyVpaHash);
  }

  private String generateVerifyVpaHash(String vpa) {
      // Hash format: sha512(key|command|var1|salt)
      // command = "validateVPA"
      // var1 = vpa
      return hash;
  }
  ```

  **Parameters**:

  * `vpa` (String): Virtual Payment Address entered by user
  * `packageListDialogFragment` (PackageListDialogFragment): Fragment to handle verification
</Accordion>

### Step 7: Initiate Payment

<Accordion title="7.1: Invoke CustomBrowser" icon="fa-code">
  Call the `addCustomBrowser()` method with your configuration and callback:

  ```java
  new CustomBrowser().addCustomBrowser(
      Activity activity,
      CustomBrowserConfig customBrowserConfig,
      PayUCustomBrowserCallback payUCustomBrowserCallback
  );
  ```

  **Parameters:**

  | Parameter                   | Type                      | Description                               |
  | --------------------------- | ------------------------- | ----------------------------------------- |
  | `activity`                  | Activity                  | Current activity instance                 |
  | `customBrowserConfig`       | CustomBrowserConfig       | Configuration object with payment details |
  | `payUCustomBrowserCallback` | PayUCustomBrowserCallback | Callback interface for handling responses |
</Accordion>

<Accordion title="7.2: Complete Implementation Example" icon="fa-code">
  ```java
  public class PaymentActivity extends AppCompatActivity {
      
      private String merchantKey = "YOUR_MERCHANT_KEY";
      private String txnId = "TXN" + System.currentTimeMillis();
      
      @Override
      protected void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          setContentView(R.layout.activity_payment);
          
          // Check payment option availability (optional)
          checkPaymentAvailability();
          
          // Initiate payment
          initiatePayment();
      }
      
      private void checkPaymentAvailability() {
          String paymentOptionHash = generatePaymentOptionHash();
          
          new CustomBrowser().checkForPaymentAvailability(
              this,
              PaymentOption.PHONEPE,
              payUCustomBrowserCallback,
              paymentOptionHash,
              merchantKey,
              "default"
          );
      }
      
      private void initiatePayment() {
          // Create configuration
          CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey, txnId);
          
          // Set mandatory parameters
          customBrowserConfig.setPayuPostData(getPostData());
          customBrowserConfig.setPostUrl("https://secure.payu.in/_payment");
          
          // Set optional parameters
          customBrowserConfig.setAutoApprove(true);
          customBrowserConfig.setAutoSelectOTP(true);
          customBrowserConfig.setMerchantResponseTimeout(30000);
          customBrowserConfig.setEnableSslDialog(true);
          
          // Invoke CustomBrowser
          new CustomBrowser().addCustomBrowser(
              this,
              customBrowserConfig,
              payUCustomBrowserCallback
          );
      }
      
      // Callback implementation
      PayUCustomBrowserCallback payUCustomBrowserCallback = new PayUCustomBrowserCallback() {
          // ... (implement all callback methods as shown in Step 6)
      };
      
      private String getPostData() {
          // Build post data string with all required parameters
          return postDataString;
      }
      
      private String generatePaymentOptionHash() {
          // Generate hash: sha512(key|command|var1|salt)
          return hash;
      }
  }
  ```
</Accordion>

***

## Test the Integration

<Accordion title="Test Environment Setup" icon="fa-code">
  Use the following configuration for testing:

  * **Post URL**: `https://test.payu.in/_payment`
  * **Test Merchant Key**: Provided by PayU
  * **Test Salt**: Provided by PayU

  <Callout icon="🚧" theme="warn">
    **Important**: The UPI in-app and UPI intent flow is not available in Test mode.
  </Callout>
</Accordion>

<Accordion title="Test Credentials for Card" icon="fa-code">
  | Card Number      | Expiry | CVV | OTP    |
  | ---------------- | ------ | --- | ------ |
  | 5123456789012346 | 05/25  | 123 | 123456 |
</Accordion>

<Accordion title="Test Credentials for Net Banking" icon="fa-code">
  Use the following credentials to test the Net Banking integration:

  * **User name**: payu
  * **Password**: payu
  * **OTP**: 123456
</Accordion>

<Accordion title="Test VPA for UPI" icon="fa-code">
  You can use either of the following VPAs to test your UPI-related integration:

  * `anything@upi`
  * `9999999999@upi`

  **For Testing the UPI Collect flow, Please follow the below steps:**

  1. Once you enter the VPA click on the verify button and proceed to pay.
  2. In NPCI page timer will start, Don't "CLICK" on click text. Please wait on the NPCI page.
  3. The below link opens in the browser. Paste the transaction ID at the end of the URL then click on the success/failure simulator page. After that, your app will redirect to your app with the transaction response.

  ```
  https://pgsim01.payu.in/UPI-test-transaction/confirm/<Txn_id>
  ```

  Replace `<Txn_id>` with your actual transaction ID.

  <Callout icon="🚧" theme="warn">
    **Remove code from manifest**: Ensure to remove the debug metadata code from the manifest file before going live.
  </Callout>
</Accordion>

<Accordion title="Test Cards for EMI" icon="fa-code">
  You can use the following Debit and Credit cards to test EMI integration.

  Refer to [EMI Test Cards](https://docs.payu.in/docs/test-cards-for-emi) documentation for complete list of EMI testing cards.
</Accordion>

<Accordion title="Test Wallets" icon="fa-code">
  You can use the following wallets and their corresponding credentials to test wallet integration.

  Refer to [Test Wallets](https://docs.payu.in/docs/test-wallets) documentation for wallet testing credentials.
</Accordion>

***

## Go-Live Checklist

Ensure these steps before you deploy the integration in a live environment.

<Accordion title="Generate Production Key and Salt" icon="fa-code">
  <Callout icon="🚧" theme="warn">
    **Generate Production Key and Salt**: Ensure that you are using the production merchant key and salt generated in the live mode.
  </Callout>

  After testing the integration end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

  **Steps to get Production credentials:**

  1. Log in to the [PayU Dashboard](https://dashboard.payu.in)
  2. Navigate to **Settings** → **Account Details**
  3. Generate and save your **Production Key** and **Salt**
  4. Replace test credentials in your code with production credentials
</Accordion>

<Accordion title="Configure Production Post URL" icon="fa-code">
  Update the post URL to production:

  ```java
  customBrowserConfig.setPostUrl("https://secure.payu.in/_payment");
  ```
</Accordion>

<Accordion title="Set Your Own Success and Failure URLs" icon="fa-code">
  <Callout icon="🚧" theme="warn">
    **We do not recommend going live with PayU sample SURL and FURL.**
  </Callout>

  PayU recommends you to design your own SURL and FURL.

  Configure your own success and failure URLs:

  ```java
  String postData = "surl=https://yourdomain.com/payment/success" +
                    "&furl=https://yourdomain.com/payment/failure";
  ```

  Refer the link to [Handling SURL and FURL](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk) doc details.
</Accordion>

<Accordion title="Remove Debug Configuration from Manifest" icon="fa-code">
  You must be comment/remove the below metadata code from the manifest file to use the UPI Collect flow on Production env:

  Remove or comment the following metadata from your `AndroidManifest.xml`:

  ```xml
  <application>
  <!-- REMOVE THESE LINES BEFORE PRODUCTION -->
  <!--
  <meta-data android:name="payu_debug_mode_enabled" android:value="true" />
  <meta-data android:name="payu_web_service_url" android:value="https://test.payu.in" />
  <meta-data android:name="payu_post_url" android:value="https://test.payu.in"/>
  -->
  </application>
  ```
</Accordion>

<Accordion title="Configure Verify Payment Method" icon="fa-code">
  Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a back up method to handle scenarios where the payment callback is failed due to technical error.

  ```java
  // Implement verify payment API call
  // Refer to: https://docs.payu.in/docs/verify-payment-api
  ```

  We strongly recommend using this method to handle scenarios where payment callbacks fail due to technical errors.
</Accordion>

<Accordion title="Setup Webhook for Payment Notifications" icon="fa-code">
  We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).
</Accordion>

***

## Troubleshooting

<Accordion title="Issue 1: Interface Methods Error" icon="fa-code">
  **Error**: `Default interface methods are only supported starting with Android N`

  **Solution**: Add Java 1.8 compatibility in `build.gradle`:

  ```gradle
  android {
      compileOptions {
          sourceCompatibility 1.8
          targetCompatibility 1.8
      }
  }
  ```
</Accordion>

<Accordion title="Issue 2: UPI Payment Options Not Working" icon="fa-code">
  **Issue**: UPI options like PhonePe, Google Pay not appearing

  **Solution**:

  * Add UPI SDK dependency (mandatory from v7.4.0+)
  * Implement `checkForPaymentAvailability()` before showing options
  * Verify UPI apps are installed on device
</Accordion>

<Accordion title="Issue 3: Hash Mismatch Error" icon="fa-code">
  **Issue**: Payment fails with hash validation error

  **Solution**:

  * Verify hash generation formula matches PayU documentation
  * Ensure all parameters are in correct order
  * Check for extra spaces or special characters
  * Use UTF-8 encoding
  * Validate that salt is correct
</Accordion>

<Accordion title="Issue 4: OTP Not Auto-filled" icon="fa-code">
  **Issue**: OTP assist not working

  **Solution**:

  * Add `RECEIVE_SMS` permission in AndroidManifest.xml
  * Set `setAutoApprove(true)` or `setAutoSelectOTP(true)` in config
  * Check permission is granted at runtime (Android M+)
  * Verify SMS format is supported
</Accordion>

<Accordion title="Issue 5: Payment Option Not Available" icon="fa-code">
  **Issue**: `isPaymentOptionAvailable()` returns false

  **Solution**:

  * Check if payment app is installed on device
  * Verify merchant is registered for that payment option
  * Ensure device and country are supported
  * Check error message in `resultData.getErrorMessage()`
</Accordion>

<Accordion title="Issue 6: SSL Errors" icon="fa-code">
  **Issue**: Bank pages not loading due to SSL errors

  **Solution**:

  * Set `setEnableSslDialog(true)` to show user-friendly message
  * PayU will auto-redirect even with SSL errors
  * Contact bank if issue persists
</Accordion>

<Accordion title="Issue 7: WebView Not Loading" icon="fa-code">
  **Issue**: Payment page doesn't load in CustomBrowser

  **Solution**:

  * Verify post URL is correct (production vs staging)
  * Check post data format and encoding
  * Implement `setCBProperties()` callback correctly
  * Enable WebView debugging for troubleshooting:

  ```java
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT) {
      WebView.setWebContentsDebuggingEnabled(true);
  }
  ```
</Accordion>

***
