---
title: 'Native OTP New '
deprecated: false
hidden: true
metadata:
  robots: index
---
# Native OTP Assist SDK Integration Guide

## Overview

The Native OTP Assist SDK provides automatic OTP reading and submission functionality for card payments, enhancing the payment experience by reducing manual OTP entry.

Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard > Settings > Payment methods**. For more information, refer to [Checkout Payment Modes](https://docs.payu.in/docs/payu-payment-page-customization#configure-checkout-payment-methods-and-settings).

***

## Prerequisites

### Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

***

## SDK Integration

### Step 2: Include the SDK in your application

<Accordion title="2.1: Add Gradle Dependency" icon="fa-code">
  Include the SDK in your application's `build.gradle`:

  ```gradle
  implementation 'in.payu:native-otp-assist:1.6.3'
  ```

  <Callout icon="❗️" theme="error">
    **Maven Central**: PayU has moved to Maven Central. Update your existing dependency with the above configuration.
  </Callout>
</Accordion>

<Accordion title="2.2: Configure Java 8 Compatibility" icon="fa-code">
  Add the following in your app's `build.gradle` inside the `android{}` block:

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

  <Callout icon="📘" theme="info">
    **Compatibility Requirements:**

    1. **Android SDK** — Version 21 and above
    2. **Compile SDK** — Version 31 and above
  </Callout>
</Accordion>

<Accordion title="2.3: Add Required Permissions" icon="fa-code">
  Add the following permission in your application's `AndroidManifest.xml`:

  ```xml
  <uses-permission android:name="android.permission.RECEIVE_SMS" />
  ```

  <Callout icon="👍" theme="okay">
    **Tip**: This permission is required for automatic OTP reading. The SDK will request this permission at runtime. Users must grant this permission for OTP auto-read functionality to work.
  </Callout>

  <Callout icon="🚧" theme="warn">
    **Remember**: This SDK will work only if the customer provides consent for the app to read SMS on their device.
  </Callout>
</Accordion>

***

### Step 3: Set up payment hash and post data

<Accordion title="3.1: Generate Payment Hash" icon="fa-key">
  For more information on the generation of Payment Hash, refer to [Generate Static Hash](https://docs.payu.in/docs/generate-static-hash-android-sdk-pro).

  <Callout icon="🚧" theme="warn">
    **Generate hash on your server**: Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.
  </Callout>

  **Hash Formula**: `sha512(<key>|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||<Add Salt Value>)`

  Every transaction (payment or non-payment) needs a hash set up by you before sending the transaction details to PayU. Hash is required for PayU to validate the authenticity of the transaction. This hashing should be done on your server.
</Accordion>

<Accordion title="3.2: Payment Post Data" icon="fa-code">
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

***

### Step 4: Initiate payment

<Accordion title="4.1: Create PayUOtpAssistConfig" icon="fa-code">
  Create the configuration object with payment post data:

  ```java Java
  PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig();
  payUOtpAssistConfig.setPostData("POST_DATA_FOR_TRANSACTION");
  ```
  ```kotlin Kotlin
  val payUOtpAssistConfig = PayUOtpAssistConfig()
  payUOtpAssistConfig.postData = "POST_DATA_FOR_TRANSACTION"
  ```

  **Configuration Parameters:**

  | Parameter  | Type   | Description                                  | Mandatory |
  | ---------- | ------ | -------------------------------------------- | --------- |
  | `postData` | String | Complete payment post data with card details | Yes       |
</Accordion>

<Accordion title="4.2: Initialize Native OTP SDK" icon="fa-play">
  Initialize the Native OTP Assist SDK by providing the configuration object and callback listener:

  ```java Java
  PayUOtpAssist.open(
      Context context, 
      PayUOtpAssistCallback payUOtpAssistCallback, 
      PayUOtpAssistConfig payUOtpAssistConfig
  );
  ```
  ```kotlin Kotlin
  PayUOtpAssist.open(
      context: Context, 
      payUOtpAssistCallback: PayUOtpAssistCallback,  
      payUOtpAssistConfig: PayUOtpAssistConfig
  )
  ```

  **Parameters:**

  | Parameter               | Type                  | Description                               |
  | ----------------------- | --------------------- | ----------------------------------------- |
  | `context`               | Context               | Current activity or application context   |
  | `payUOtpAssistCallback` | PayUOtpAssistCallback | Callback interface for handling responses |
  | `payUOtpAssistConfig`   | PayUOtpAssistConfig   | Configuration object with payment details |

  <Callout icon="📘" theme="info">
    **OTP Reading Method**: PayU fetches the OTP through RECEIVE\_SMS if the permission is granted. Otherwise, it fetches the OTP using the Google Consent API.
  </Callout>
</Accordion>

***

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

### Step 6: Handle Payment Flow

<Accordion title="6.1: Complete Implementation Example" icon="fa-code">
  ```java Java
  public class PaymentActivity extends AppCompatActivity {
      
      private String merchantKey = "YOUR_MERCHANT_KEY";
      private String merchantSalt = "YOUR_MERCHANT_SALT";
      private String txnId = "TXN" + System.currentTimeMillis();
      
      @Override
      protected void onCreate(Bundle savedInstanceState) {
          super.onCreate(savedInstanceState);
          setContentView(R.layout.activity_payment);
          
          // Initiate payment
          initiatePayment();
      }
      
      private void initiatePayment() {
          // Step 1: Generate payment post data
          String postData = generatePostData();
          
          // Step 2: Create configuration
          PayUOtpAssistConfig payUOtpAssistConfig = new PayUOtpAssistConfig();
          payUOtpAssistConfig.setPostData(postData);
          
          // Step 3: Open OTP Assist SDK
          PayUOtpAssist.open(
              this,
              payUOtpAssistCallback,
              payUOtpAssistConfig
          );
      }
      
      private String generatePostData() {
          // Build post data with all parameters
          StringBuilder postData = new StringBuilder();
          postData.append("key=").append(merchantKey);
          postData.append("&txnid=").append(txnId);
          postData.append("&amount=").append("100.0");
          postData.append("&productinfo=").append("Test Product");
          postData.append("&firstname=").append("John");
          postData.append("&email=").append("john@example.com");
          postData.append("&phone=").append("9999999999");
          postData.append("&surl=").append("https://yourdomain.com/success");
          postData.append("&furl=").append("https://yourdomain.com/failure");
          
          // Add card details
          postData.append("&ccnum=").append("5123456789012346");
          postData.append("&ccname=").append("John Doe");
          postData.append("&ccvv=").append("123");
          postData.append("&ccexpmon=").append("12");
          postData.append("&ccexpyr=").append("2025");
          postData.append("&bankcode=").append("CC");
          postData.append("&pg=").append("CC");
          
          // Generate and add hash
          String hash = generateHash();
          postData.append("&hash=").append(hash);
          
          return postData.toString();
      }
      
      // Callback implementation
      PayUOtpAssistCallback payUOtpAssistCallback = new PayUOtpAssistCallback() {
          
          @Override
          public void onPaymentSuccess(@Nullable String merchantResponse, 
                                        @Nullable String payUResponse) {
              Log.d("PayU", "Payment Success");
              
              Intent intent = new Intent();
              intent.putExtra("merchant_response", merchantResponse);
              intent.putExtra("payu_response", payUResponse);
              setResult(Activity.RESULT_OK, intent);
              finish();
          }

          @Override
          public void onPaymentFailure(@Nullable String merchantResponse, 
                                        @Nullable String payUResponse) {
              Log.e("PayU", "Payment Failed");
              
              Intent intent = new Intent();
              intent.putExtra("merchant_response", merchantResponse);
              intent.putExtra("payu_response", payUResponse);
              setResult(Activity.RESULT_CANCELED, intent);
              finish();
          }

          @Override
          public void onError(@Nullable String errorCode, 
                              @Nullable String errorMessage) {
              Log.e("PayU", "Error: " + errorMessage);
              Toast.makeText(PaymentActivity.this, 
                  "Error: " + errorMessage, Toast.LENGTH_LONG).show();
              finish();
          }

          @Override
          public boolean shouldHandleFallback(PayUAcsRequest payUAcsRequest) {
              // Let SDK handle fallback by default
              return true;
              
              // Or handle yourself:
              // return handleCustomBrowserFallback(payUAcsRequest);
          }
      };
  }
  ```
  ```kotlin Kotlin
  class PaymentActivity : AppCompatActivity() {
      
      private val merchantKey = "YOUR_MERCHANT_KEY"
      private val merchantSalt = "YOUR_MERCHANT_SALT"
      private val txnId = "TXN${System.currentTimeMillis()}"
      
      override fun onCreate(savedInstanceState: Bundle?) {
          super.onCreate(savedInstanceState)
          setContentView(R.layout.activity_payment)
          
          // Initiate payment
          initiatePayment()
      }
      
      private fun initiatePayment() {
          // Step 1: Generate payment post data
          val postData = generatePostData()
          
          // Step 2: Create configuration
          val payUOtpAssistConfig = PayUOtpAssistConfig()
          payUOtpAssistConfig.postData = postData
          
          // Step 3: Open OTP Assist SDK
          PayUOtpAssist.open(
              this,
              payUOtpAssistCallback,
              payUOtpAssistConfig
          )
      }
      
      private fun generatePostData(): String {
          // Build post data with all parameters
          val postData = StringBuilder()
          postData.append("key=$merchantKey")
          postData.append("&txnid=$txnId")
          postData.append("&amount=100.0")
          postData.append("&productinfo=Test Product")
          postData.append("&firstname=John")
          postData.append("&email=john@example.com")
          postData.append("&phone=9999999999")
          postData.append("&surl=https://yourdomain.com/success")
          postData.append("&furl=https://yourdomain.com/failure")
          
          // Add card details
          postData.append("&ccnum=5123456789012346")
          postData.append("&ccname=John Doe")
          postData.append("&ccvv=123")
          postData.append("&ccexpmon=12")
          postData.append("&ccexpyr=2025")
          postData.append("&bankcode=CC")
          postData.append("&pg=CC")
          
          // Generate and add hash
          val hash = generateHash()
          postData.append("&hash=$hash")
          
          return postData.toString()
      }
      
      // Callback implementation
      private val payUOtpAssistCallback = object : PayUOtpAssistCallback {
          
          override fun onPaymentSuccess(merchantResponse: String?, 
                                         payUResponse: String?) {
              Log.d("PayU", "Payment Success")
              
              val intent = Intent()
              intent.putExtra("merchant_response", merchantResponse)
              intent.putExtra("payu_response", payUResponse)
              setResult(Activity.RESULT_OK, intent)
              finish()
          }

          override fun onPaymentFailure(merchantResponse: String?, 
                                         payUResponse: String?) {
              Log.e("PayU", "Payment Failed")
              
              val intent = Intent()
              intent.putExtra("merchant_response", merchantResponse)
              intent.putExtra("payu_response", payUResponse)
              setResult(Activity.RESULT_CANCELED, intent)
              finish()
          }

          override fun onError(errorCode: String?, 
                               errorMessage: String?) {
              Log.e("PayU", "Error: $errorMessage")
              Toast.makeText(this@PaymentActivity, 
                  "Error: $errorMessage", Toast.LENGTH_LONG).show()
              finish()
          }

          override fun shouldHandleFallback(payUAcsRequest: PayUAcsRequest): Boolean {
              // Let SDK handle fallback by default
              return true
          }
      }
  }
  ```
</Accordion>

<Accordion title="6.2: Handling Fallback with CustomBrowser" icon="fa-code">
  If you want to handle the bank page redirection yourself, implement the fallback handler:

  ```java Java
  private boolean handleCustomBrowserFallback(PayUAcsRequest payUAcsRequest) {
      CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey, txnId);
      
      // Check what data is available in PayUAcsRequest
      if (payUAcsRequest.getIssuerUrl() != null && 
          payUAcsRequest.getIssuerPostData() != null) {
          // Case 1: Bank URL and POST data provided
          customBrowserConfig.setPostURL(payUAcsRequest.getIssuerUrl());
          customBrowserConfig.setPayuPostData(payUAcsRequest.getIssuerPostData());
          
      } else if (payUAcsRequest.getAcsTemplate() != null) {
          // Case 2: HTML template provided
          customBrowserConfig.setHtmlData(payUAcsRequest.getAcsTemplate());
          
      } else {
          // Case 3: Fallback to original payment URL
          customBrowserConfig.setPostURL("https://secure.payu.in/_payment");
          customBrowserConfig.setPayuPostData(originalPostData);
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
  private fun handleCustomBrowserFallback(payUAcsRequest: PayUAcsRequest): Boolean {
      val customBrowserConfig = CustomBrowserConfig(merchantKey, txnId)
      
      // Check what data is available in PayUAcsRequest
      when {
          // Case 1: Bank URL and POST data provided
          !payUAcsRequest.issuerUrl.isNullOrEmpty() && 
          !payUAcsRequest.issuerPostData.isNullOrEmpty() -> {
              customBrowserConfig.postURL = payUAcsRequest.issuerUrl
              customBrowserConfig.payuPostData = payUAcsRequest.issuerPostData
          }
          
          // Case 2: HTML template provided
          !payUAcsRequest.acsTemplate.isNullOrEmpty() -> {
              customBrowserConfig.htmlData = payUAcsRequest.acsTemplate
          }
          
          // Case 3: Fallback to original payment URL
          else -> {
              customBrowserConfig.postURL = "https://secure.payu.in/_payment"
              customBrowserConfig.payuPostData = originalPostData
          }
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

  **PayUAcsRequest Fields:**

  | Field            | Type    | Description                                                                                                   |
  | ---------------- | ------- | ------------------------------------------------------------------------------------------------------------- |
  | `issuerUrl`      | String? | Bank/ACS page URL for 3D Secure authentication                                                                |
  | `issuerPostData` | String? | POST data to send to issuer URL. Load as: `webView.postUrl(issuerUrl, issuerPostData.toByteArray())`          |
  | `acsTemplate`    | String? | HTML template to load if `issuerUrl` is empty. Load as: `webView.loadData(acsTemplate, "text/html", "UTF-8")` |

  <Callout icon="📘" theme="info">
    **Understanding Fallback:**

    Fallback occurs when:

    * Card requires 3D Secure authentication
    * Bank needs additional verification
    * ACS (Access Control Server) page needs to be displayed

    By default, the SDK handles this automatically. Override only if you need custom handling.
  </Callout>
</Accordion>

***

## Test the Integration

> 🚧 Callout
>
> The Native-OTP flow is not available in the Test mode.

***

## Go-Live Checklist

Ensure these steps before you deploy the integration in a live environment.

### Checklist 1: Collect Live Payments

<Accordion title="Generate Production Key and Salt" icon="fa-code">
  <Callout icon="🚧" theme="warn">
    **Generate Production Key and Salt**: Ensure that you are using the production merchant key and salt generated in the live mode.
  </Callout>

  After testing the integration end-to-end, once you are confident that the integration is working as expected, you can switch to live mode to start accepting payments from your customers.

  **Steps to get Production credentials:**

  1. Log in to the [PayU Dashboard](https://dashboard.payu.in)
  2. Switch to **Live** mode
  3. Navigate to **Settings** → **Account Details**
  4. Copy your **Production Key** and **Salt**
  5. Replace test credentials in your code with production credentials
</Accordion>

***

### Checklist 2: Configure SURL/FURL

<Accordion title="Set Your Own Success and Failure URLs" icon="fa-code">
  <Callout icon="🚧" theme="warn">
    **We do not recommend going live with PayU sample SURL and FURL.**
  </Callout>

  PayU recommends you to design your own SURL and FURL.

  Configure your own success and failure URLs in the post data:

  ```java
  String postData = "surl=https://yourdomain.com/payment/success" +
                    "&furl=https://yourdomain.com/payment/failure";
  ```

  Refer to [Handling SURL and FURL](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk) for detailed guidance.
</Accordion>

***

### Checklist 3: Verify Payment Implementation

<Accordion title="Configure Verify Payment Method" icon="fa-code">
  Configure the Verify payment method to fetch the payment status. We strongly recommend that you use this as a backup method to handle scenarios where the payment callback fails due to technical error.

  **Implementation:**

  ```java Java
  // After receiving payment response, verify the transaction
  public void verifyPayment(String txnId) {
      // Call verify payment API
      // Refer to: https://docs.payu.in/docs/verify-payment-api
  }
  ```
  ```kotlin Kotlin
  // After receiving payment response, verify the transaction
  fun verifyPayment(txnId: String) {
      // Call verify payment API
      // Refer to: https://docs.payu.in/docs/verify-payment-api
  }
  ```

  For more information, refer to [Verify Payment API](https://docs.payu.in/docs/verify-payment-api).
</Accordion>

***

### Checklist 4: Configure Webhook

<Accordion title="Setup Webhook for Payment Notifications" icon="fa-code">
  We recommend that you configure Webhook to receive payment responses on your server. For more information, refer to [Webhooks](https://docs.payu.in/docs/webhooks).

  **Benefits of Webhooks:**

  * Reliable payment notification
  * Server-to-server communication
  * Handles network failures
  * Real-time payment status updates
</Accordion>

***

### Checklist 5: Test in Production Environment

Before going live, test the following scenarios:

<Callout icon="👍" theme="okay">
  **Best Practice**: Test with small amounts first (₹1-10) before processing larger transactions.
</Callout>

***

## Troubleshooting

<Accordion title="Issue 1: OTP Not Auto-Reading" icon="fa-code">
  **Problem**: OTP is not automatically filled in the payment screen.

  **Possible Causes:**

  * SMS permission not granted
  * SMS format not recognized
  * Google Play Services not available

  **Solutions:**

  1. Check SMS permission is granted:
     ```java
     if (ContextCompat.checkSelfPermission(this, 
         Manifest.permission.RECEIVE_SMS) != PackageManager.PERMISSION_GRANTED) {
         // Request permission
         ActivityCompat.requestPermissions(this, 
             new String[]{Manifest.permission.RECEIVE_SMS}, 
             REQUEST_CODE_SMS);
     }
     ```
  2. Verify Google Play Services is available
  3. Check SMS format contains recognizable OTP pattern
  4. Enable logging to debug SMS reading
</Accordion>

<Accordion title="Issue 2: Payment Fails with Hash Error" icon="fa-code">
  **Problem**: Payment fails with "Hash mismatch" or "Invalid hash" error.

  **Solution:**

  1. Verify hash generation formula is correct:
     ```
     sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
     ```
  2. Ensure all parameters match exactly in hash and post data
  3. Check for extra spaces or special characters
  4. Verify salt is correct (production vs test)
  5. Use UTF-8 encoding for hash calculation
</Accordion>

<Accordion title="Issue 3: shouldHandleFallback Not Working" icon="fa-code">
  **Problem**: Bank page is not loading when 3D Secure is required.

  **Solution:**

  1. Verify CustomBrowser SDK is included in dependencies
  2. Check `shouldHandleFallback()` return value:
     * `true`: SDK handles (default)
     * `false`: You handle with CustomBrowser
  3. Implement CustomBrowser callback properly
  4. Verify `issuerUrl` and `issuerPostData` are not null
  5. Check WebView settings allow JavaScript and DOM storage
</Accordion>

<Accordion title="Issue 4: Permission Request Not Showing" icon="fa-code">
  **Problem**: SMS permission dialog not appearing.

  **Solution:**

  1. Add permission in `AndroidManifest.xml`:
     ```xml
     <uses-permission android:name="android.permission.RECEIVE_SMS" />
     ```
  2. Request permission at runtime (Android M+):
     ```java
     ActivityCompat.requestPermissions(this, 
         new String[]{Manifest.permission.RECEIVE_SMS}, 
         REQUEST_CODE_SMS);
     ```
  3. Handle permission result:
     ```java
     @Override
     public void onRequestPermissionsResult(int requestCode, 
                                            String[] permissions, 
                                            int[] grantResults) {
         if (requestCode == REQUEST_CODE_SMS) {
             if (grantResults.length > 0 && 
                 grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                 // Permission granted, proceed with payment
             } else {
                 // Permission denied, inform user
             }
         }
     }
     ```
</Accordion>

<Accordion title="Issue 5: Payment Stuck on Loading Screen" icon="fa-code">
  **Problem**: Payment screen shows loading indefinitely.

  **Possible Causes:**

  * Network timeout
  * Invalid post data
  * Server not responding

  **Solutions:**

  1. Check network connection
  2. Verify post data format is correct
  3. Check logs for error messages
  4. Verify payment gateway URL is correct
  5. Test with smaller timeout values
  6. Implement timeout handling:
     ```java
     // Set timeout in configuration (if available)
     payUOtpAssistConfig.setTimeout(30000); // 30 seconds
     ```
</Accordion>

<Accordion title="Issue 6: Java 8 Compilation Error" icon="fa-code">
  **Problem**: Build fails with error about Java 8 features.

  **Solution:**
  Add Java 8 compatibility in your app's `build.gradle`:

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
</Accordion>

<Accordion title="Issue 7: SMS Format Not Recognized" icon="fa-code">
  **Problem**: OTP is received but not detected by SDK.

  **Explanation**: The SDK uses pattern matching to extract OTP from SMS. If the SMS format is non-standard, it may not be detected.

  **Solution:**

  1. Check SMS contains numeric OTP (4-6 digits)
  2. Verify SMS sender is recognized
  3. Manual fallback is available if auto-read fails
  4. Contact PayU support for SMS format whitelist

  **Supported OTP Patterns:**

  * `OTP: 123456`
  * `Your OTP is 123456`
  * `123456 is your OTP`
  * `One time password: 123456`
</Accordion>

***

## Sample Response Format

<Accordion title="Success Response" icon="fa-code">
  ```json
  {
      "mihpayid": "403993715526100438",
      "mode": "CC",
      "status": "success",
      "unmappedstatus": "captured",
      "key": "gt***",
      "txnid": "1651831862726",
      "amount": "100.00",
      "cardCategory": "domestic",
      "discount": "0.00",
      "addedon": "2022-05-06 15:41:38",
      "productinfo": "Macbook Pro",
      "firstname": "John",
      "email": "john@example.com",
      "phone": "9999999999",
      "hash": "...",
      "bank_ref_no": "711633",
      "bankcode": "CC",
      "error": "E000",
      "error_Message": "No Error"
  }
  ```
</Accordion>

<Accordion title="Failure Response" icon="fa-code">
  ```json
  {
      "mihpayid": "15130876153",
      "mode": "CC",
      "status": "failure",
      "unmappedstatus": "failed",
      "key": "gt***",
      "txnid": "1651832033713",
      "amount": "100.00",
      "productinfo": "Macbook Pro",
      "firstname": "John",
      "email": "john@example.com",
      "phone": "9999999999",
      "error": "E1302",
      "error_Message": "Bank failed to authenticate the customer"
  }
  ```
</Accordion>

***
