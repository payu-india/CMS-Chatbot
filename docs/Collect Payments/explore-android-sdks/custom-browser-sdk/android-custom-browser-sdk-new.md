---
title: Android Custom Browser SDK (New)
deprecated: false
hidden: true
metadata:
  robots: index
---
# Custom Browser SDK Integration Guide

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Initial Setup](#initial-setup)
3. [Payment Option Availability Check](#payment-option-availability-check)
4. [CustomBrowser Implementation](#custombrowser-implementation)
5. [Configuration Reference](#configuration-reference)
6. [Callback Methods](#callback-methods)
7. [Sample Code](#sample-code)
8. [Troubleshooting](#troubleshooting)

***

## 🔴 CRITICAL NOTICE

> **Payment Mode-Specific Parameters Required**: When implementing PayU Custom Browser SDK, you **MUST** configure the `pg` (Payment Gateway) and `bankcode` parameters in your post data based on the payment method selected by the user. Incorrect values will cause payment failures.
>
> **📚 Essential References**:
>
> * **Implementation Guide**: [Android Core SDK - Generate Request for Payment](https://docs.payu.in/docs/integration-steps-android-core-sdk#step-5-generate-request-for-payment)
> * **Codes Reference**: [Bank and Card Codes for Integration](https://docs.payu.in/docs/bank-and-card-codes-for-integration)
>
> See [Payment Mode-Specific Configuration](#️-critical-payment-mode-specific-configuration)  section for detailed guidance.

<br />

## Prerequisites

### 1. Create PayU Account

* Register for a PayU Merchant Account at [PayU Dashboard](https://dashboard.payu.in)
* For detailed instructions, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account)

***

## Initial Setup

### Step 1: Add SDK Dependency

Add the following dependency in your application’s build.gradle:

```
implementation 'in.payu:payu-custom-browser:7.16.0'
```

<Callout icon="🚧" theme="warn">
  **Watch Out**: If you are getting the following error: `Default interface methods are only supported starting with Android N (--min-api 24): Landroidx/lifecycle/DefaultLifecycleObserver;onCreate(Landroidx/lifecycle/LifecycleOwner;)V`

  Add the following compileOptions on your app's build.gradle:

  ```Text build.gradle
  android {
   compileOptions {
          sourceCompatibility 1.8
          targetCompatibility 1.8
      }
  }
  ```
</Callout>

From version 7.4.0 onwards, it is mandatory to import UPI SDK dependency if you want to make payments through any of the following UPI options along with the changes mentioned in the Third-Party Payments Support section.

* UPI Intent
* Collect
* Google Pay
* PhonePe

```
<uses-permission android:name="android.permission.RECEIVE_SMS" />
```

<Callout icon="👍" theme="okay">
  **Tip**: Merchants are advised to add this permission in the application’s `AndroidManifest.xml` to support OTP assist. In case your application supports a minimum SDK of less than 20, do these changes in your surl/furl.
</Callout>

### Step 3: Add UPI SDK Dependency (Version 7.4.0+)

## Payment Option Availability Check (Optional)

### Overview

Before displaying payment options like Samsung Pay, PhonePe, or Google Pay, you must check if they are available on the user's device.

### Method Signature

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

### Parameters

| Parameter                   | Type                      | Description                                                                     |
| --------------------------- | ------------------------- | ------------------------------------------------------------------------------- |
| `activity`                  | Activity                  | Current activity instance                                                       |
| `paymentOption`             | PaymentOption             | Payment option type (e.g., `PaymentOption.SAMSUNGPAY`, `PaymentOption.PHONEPE`) |
| `payUCustomBrowserCallback` | PayUCustomBrowserCallback | Callback interface for handling responses                                       |
| `paymentOptionHash`         | String                    | SHA-512 hash for payment option verification                                    |
| `merchantKey`               | String                    | Your PayU merchant key                                                          |
| `user_credentials`          | String                    | User credentials or use "default"                                               |

### Generate PaymentOption Hash

**Formula**: `sha512(key|command|var1|salt)`

Where:

* `key` = Your merchant key
* `command` = `"payment_related_details_for_mobile_sdk"`
* `var1` = User credentials or "default"
* `salt` = Your merchant salt

For more information, refer to [Generate Static Hash](https://docs.payu.in/docs/generate-static-hash).

### Example

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

***

## CustomBrowser Implementation

### Step 1: Create CustomBrowserConfig

Create a basic configuration object with mandatory parameters:

```java
CustomBrowserConfig customBrowserConfig = new CustomBrowserConfig(merchantKey, txnId);
customBrowserConfig.setPayuPostData(postData);
customBrowserConfig.setPostUrl(postUrl);
```

#### Post URLs

| Environment    | URL                               |
| -------------- | --------------------------------- |
| **Production** | `https://secure.payu.in/_payment` |
| **Staging**    | `https://test.payu.in/_payment`   |

### Step 2: Create PayUCustomBrowserCallback

Implement the callback interface to handle payment responses. See [Callback Methods](#callback-methods) section for details.

### Step 3: Invoke CustomBrowser

Call the `addCustomBrowser()` method:

```java
new CustomBrowser().addCustomBrowser(
    Activity activity,
    CustomBrowserConfig customBrowserConfig,
    PayUCustomBrowserCallback payUCustomBrowserCallback
);
```

#### Parameters

| Parameter                   | Type                      | Description                               |
| --------------------------- | ------------------------- | ----------------------------------------- |
| `activity`                  | Activity                  | Current activity instance                 |
| `customBrowserConfig`       | CustomBrowserConfig       | Configuration object with payment details |
| `payUCustomBrowserCallback` | PayUCustomBrowserCallback | Callback interface for handling responses |

***

## Configuration Reference

### Mandatory Configuration

#### 1. Post Data

Set the payment post data to be sent to PayU payment gateway.

```java
customBrowserConfig.setPayuPostData(String postData);
```

**Description**: Contains all payment parameters including transaction details, user information, and hash.

#### 2. Post URL

Set the PayU payment gateway URL.

```java
customBrowserConfig.setPostUrl(String postUrl);
```

**Values**:

* Production: `https://secure.payu.in/_payment`
* Staging: `https://test.payu.in/_payment`

### Optional Configuration

#### 1. HTML Data (Available from v7.2.2+)

Set HTML string received from PayU web service using Server-to-Server call.

```java
customBrowserConfig.setHtmlData(String htmlData);
```

**Use Case**: When you receive pre-rendered HTML from PayU's server-side API.

#### 2. ViewPort Enable

Control viewport settings for the web view.

```java
customBrowserConfig.setViewPortWideEnable(boolean viewPortWide);
```

| Value   | Description                     |
| ------- | ------------------------------- |
| `true`  | Enable wide viewport            |
| `false` | Disable wide viewport (default) |

#### 3. Progress Dialog Custom View

Set a custom view for the progress dialog.

```java
customBrowserConfig.setProgressDialogCustomView(View progressDialogCustomView);
```

**Use Case**: Brand the loading experience with your custom UI.

#### 4. Auto Approve

Control OTP auto-fill and approval behavior.

```java
customBrowserConfig.setAutoApprove(boolean isAutoApprove);
```

| Value   | Description                                                |
| ------- | ---------------------------------------------------------- |
| `true`  | OTP will be fetched and approved automatically             |
| `false` | OTP will be fetched but requires manual approval (default) |

**Requirements**: Requires `RECEIVE_SMS` permission.

#### 5. Surl/Furl Response Timeout

Set timeout for success/failure URL response.

```java
customBrowserConfig.setMerchantResponseTimeout(int merchantResponseTimeout);
```

**Parameter**: Timeout in milliseconds
**Default**: System default timeout

#### 6. Auto Select OTP

Automatically select OTP option when available.

```java
customBrowserConfig.setAutoSelectOTP(boolean isAutoSelect);
```

| Value   | Description                                        |
| ------- | -------------------------------------------------- |
| `true`  | OTP option will be selected automatically          |
| `false` | User will choose between password or OTP (default) |

#### 7. Merchant SMS Permission

Control SMS permission dialog display (Android M only).

```java
customBrowserConfig.setMerchantSMSPermission(boolean showPermission);
```

| Value   | Description               |
| ------- | ------------------------- |
| `true`  | Shows permission dialog   |
| `false` | No dialog shown (default) |

#### 8. Package Name for Specific App

Specify a particular UPI app to invoke instead of showing generic intent chooser.

```java
customBrowserConfig.setPackageNameForSpecificApp(String packageName);
```

**Common Package Names**:

* PhonePe: `com.phonepe.app`
* Google Pay: `com.google.android.apps.nbu.paisa.user`
* Paytm: `net.one97.paytm`

**Requirements**: Must include UPI SDK dependency.

#### 9. Disable Intent Seamless Failure

Disable manual VPA fallback option from generic Intent tray.

```java
customBrowserConfig.setDisableIntentSeamlessFailure(CustomBrowserConfig.DISABLE);
```

**Values**:

* `CustomBrowserConfig.DISABLE` - Disable manual VPA fallback
* `CustomBrowserConfig.ENABLE` - Enable manual VPA fallback (default)

**Requirements**: Must include UPI SDK dependency.

#### 10. Domain URL List to Unclear

Specify URLs for which cookies should not be cleared.

```java
customBrowserConfig.setDomainUrlListToUnclear(ArrayList<String> urlList);
```

**Use Case**: Preserve session cookies for specific domains during payment flow.

**Example**:

```java
ArrayList<String> protectedUrls = new ArrayList<>();
protectedUrls.add("https://yourdomain.com");
customBrowserConfig.setDomainUrlListToUnclear(protectedUrls);
```

#### 11. Enable SSL Dialog

Show a popup message when SSL errors occur.

```java
customBrowserConfig.setEnableSslDialog(boolean enable);
```

| Value   | Description                          |
| ------- | ------------------------------------ |
| `true`  | Show SSL error dialog to user        |
| `false` | Handle SSL errors silently (default) |

**Note**: PayU automatically redirects users to bank pages even with SSL errors.

***

## Callback Methods

### PayUCustomBrowserCallback Interface

Implement this interface to handle payment responses and events.

### Required Callback Methods

#### 1. onPaymentSuccess

Called when payment completes successfully.

```java
@Override
public void onPaymentSuccess(String payuResponse, String merchantResponse) {
    // Handle successful payment
    // payuResponse: Response from PayU
    // merchantResponse: Response from your server (surl)
}
```

**Parameters**:

* `payuResponse` (String): Complete response from PayU gateway
* `merchantResponse` (String): Response from your success URL (surl)

#### 2. onPaymentFailure

Called when payment fails.

```java
@Override
public void onPaymentFailure(String payuResponse, String merchantResponse) {
    // Handle failed payment
    // payuResponse: Response from PayU
    // merchantResponse: Response from your server (furl)
}
```

**Parameters**:

* `payuResponse` (String): Complete response from PayU gateway
* `merchantResponse` (String): Response from your failure URL (furl)

#### 3. onCBErrorReceived

Called when CustomBrowser encounters an error.

```java
@Override
public void onCBErrorReceived(int errorCode, String errorMsg) {
    // Handle CustomBrowser errors
}
```

**Error Codes**:

| Code | Error Message                             | Description                                           |
| ---- | ----------------------------------------- | ----------------------------------------------------- |
| 1    | VENDOR_NOT_SUPPORTED                      | Device vendor is not supported                        |
| 2    | DEVICE_NOT_SUPPORTED                      | Device is not supported                               |
| 3    | APP_VERSION_MISMATCH                      | Samsung Pay version doesn't meet requirements         |
| 4    | COUNTRY_NOT_SUPPORTED                     | Device country of origin not supported by Samsung Pay |
| 5    | MERCHANT_KEY_NOT_REGISTER_FOR_SAMSUNG_PAY | Merchant not registered for Samsung Pay with PayU     |
| 6    | CONTEXT_NULL                              | Context is null                                       |
| 7    | PAYMENT_ID_NOT_PRESENT                    | Check your post data                                  |
| 1001 | DEVICE_NOT_SUPPORTED                      | Tez app not present and enablewebflow is false        |
| 1002 | MERCHANT_INFO_NOT_PRESENT                 | Check your post data and hash                         |

#### 4. setCBProperties

Customize WebView settings and behavior.

```java
@Override
public void setCBProperties(WebView webview, Bank payUCustomBrowser) {
    webview.setWebChromeClient(new PayUWebChromeClient(payUCustomBrowser));
    webview.setWebViewClient(new PayUWebViewClient(payUCustomBrowser, merchantKey));
    webview.postUrl(url, payuConfig.getData().getBytes());
    // Note: Comment above line if using CustomBrowser v6.1 or above
}
```

**Parameters**:

* `webview` (WebView): The WebView instance used for payment
* `payUCustomBrowser` (Bank): PayU CustomBrowser instance

#### 5. onPaymentTerminate

Called when payment is terminated by user or system.

```java
@Override
public void onPaymentTerminate() {
    // Handle payment termination
}
```

### Optional Callback Methods

#### 6. onBackButton

Customize the back button alert dialog.

```java
@Override
public void onBackButton(AlertDialog.Builder alertDialogBuilder) {
    // Customize alert dialog
    alertDialogBuilder.setTitle("Exit Payment?");
    alertDialogBuilder.setMessage("Are you sure you want to cancel this payment?");
}
```

**Parameter**:

* `alertDialogBuilder` (AlertDialog.Builder): Alert dialog builder for customization

#### 7. onBackApprove

Called when user confirms exit from alert dialog.

```java
@Override
public void onBackApprove() {
    // Handle user confirming exit
    finish();
}
```

#### 8. onBackDismiss

Called when user cancels exit from alert dialog.

```java
@Override
public void onBackDismiss() {
    // Handle user canceling exit
    super.onBackDismiss();
}
```

#### 9. isPaymentOptionAvailable (Available from v7.1.3+)

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
    } else {
        // Hide or disable payment option
        Log.e("PayU", "Payment option unavailable: " + errorMessage);
    }
}
```

**CustomBrowserResultData Methods**:

* `getPaymentOption()`: Returns PaymentOption (SamsungPay/PhonePe/Google Pay/UPI)
* `isPaymentOptionAvailable()`: Returns boolean indicating availability
* `getSamsungPayVpa()`: Returns Samsung Pay VPA associated with device (if applicable)
* `getErrorMessage()`: Returns error message if payment option is unavailable

#### 10. onVpaEntered (Available from v7.3.0+)

Handle UPI Collect flow VPA verification.

```java
@Override
public void onVpaEntered(String vpa, PackageListDialogFragment packageListDialogFragment) {
    // Generate VPA verification hash
    String verifyVpaHash = generateVerifyVpaHash(vpa);
    
    // Provide hash to verify VPA
    packageListDialogFragment.verifyVpa(verifyVpaHash);
}
```

**Parameters**:

* `vpa` (String): Virtual Payment Address entered by user
* `packageListDialogFragment` (PackageListDialogFragment): Fragment to handle VPA verification

**Hash Generation**:

* Use `validateVPA` command
* Use VPA address as `var1`
* Refer to [Hash Generation](https://docs.payu.in/docs/hash-generation) documentation

***

## Sample Code

### Complete Implementation Example

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
        
        @Override
        public void onPaymentSuccess(String payuResponse, String merchantResponse) {
            Intent intent = new Intent();
            intent.putExtra("result", merchantResponse);
            intent.putExtra("payu_response", payuResponse);
            setResult(Activity.RESULT_OK, intent);
            finish();
        }
        
        @Override
        public void onPaymentFailure(String payuResponse, String merchantResponse) {
            Intent intent = new Intent();
            intent.putExtra("result", merchantResponse);
            intent.putExtra("payu_response", payuResponse);
            setResult(Activity.RESULT_CANCELED, intent);
            finish();
        }
        
        @Override
        public void onCBErrorReceived(int errorCode, String errorMsg) {
            Toast.makeText(PaymentActivity.this, 
                "Error: " + errorMsg, 
                Toast.LENGTH_LONG).show();
        }
        
        @Override
        public void setCBProperties(WebView webview, Bank payUCustomBrowser) {
            webview.setWebChromeClient(new PayUWebChromeClient(payUCustomBrowser));
            webview.setWebViewClient(new PayUWebViewClient(payUCustomBrowser, merchantKey));
        }
        
        @Override
        public void onPaymentTerminate() {
            Toast.makeText(PaymentActivity.this, 
                "Payment terminated", 
                Toast.LENGTH_SHORT).show();
        }
        
        @Override
        public void onBackApprove() {
            finish();
        }
        
        @Override
        public void onBackDismiss() {
            super.onBackDismiss();
        }
        
        @Override
        public void onBackButton(AlertDialog.Builder alertDialogBuilder) {
            alertDialogBuilder.setTitle("Exit Payment");
            alertDialogBuilder.setMessage("Are you sure you want to cancel?");
        }
        
        @Override
        public void isPaymentOptionAvailable(CustomBrowserResultData resultData) {
            if (resultData.isPaymentOptionAvailable()) {
                // Enable payment option in UI
                Toast.makeText(PaymentActivity.this, 
                    resultData.getPaymentOption() + " is available", 
                    Toast.LENGTH_SHORT).show();
            } else {
                // Disable payment option in UI
                Toast.makeText(PaymentActivity.this, 
                    resultData.getErrorMessage(), 
                    Toast.LENGTH_SHORT).show();
            }
        }
        
        @Override
        public void onVpaEntered(String vpa, PackageListDialogFragment packageListDialogFragment) {
            String verifyVpaHash = generateVerifyVpaHash(vpa);
            packageListDialogFragment.verifyVpa(verifyVpaHash);
        }
    };
    
    private String getPostData() {
        // Build post data string with all required parameters
        // See "Post Data Parameters" section below
        return postDataString;
    }
    
    private String generatePaymentOptionHash() {
        // Generate hash: sha512(key|command|var1|salt)
        // command = "payment_related_details_for_mobile_sdk"
        // var1 = "default"
        return hash;
    }
    
    private String generateVerifyVpaHash(String vpa) {
        // Generate hash for VPA verification
        // command = "validateVPA"
        // var1 = vpa
        return hash;
    }
}
```

***

## Post Data Parameters

### Card Payment

```
firstname=John
&ccnum=5123456789012346
&device_type=1
&ccvv=123
&ccexpyr=2025
&ccexpmon=05
&ccname=PayuUser
&key=YOUR_MERCHANT_KEY
&email=user@example.com
&bankcode=CC
&txnid=1705055037779
&amount=1.0
&phone=9999999999
&pg=CC
&productinfo=Product+Name
&udf1=udf1
&udf2=udf2
&udf3=udf3
&udf4=udf4
&udf5=udf5
&surl=https://yourdomain.com/success
&furl=https://yourdomain.com/failure
&hash=GENERATED_HASH
&sdk_platform=[{"name":"PayUCheckoutPro","platform":"android","version":"2.0.27"}]
```

### Net Banking Payment

```
firstname=John
&device_type=1
&key=YOUR_MERCHANT_KEY
&email=user@example.com
&bankcode=SBIB
&txnid=1705055218155
&amount=1.0
&phone=9999999999
&pg=NB
&productinfo=Product+Name
&udf1=udf1
&udf2=udf2
&udf3=udf3
&udf4=udf4
&udf5=udf5
&surl=https://yourdomain.com/success
&furl=https://yourdomain.com/failure
&hash=GENERATED_HASH
&sdk_platform=[{"name":"PayUCheckoutPro","platform":"android","version":"2.0.27"}]
```

### Parameter Descriptions

| Parameter      | Mandatory | Description               | Example                                |
| -------------- | --------- | ------------------------- | -------------------------------------- |
| `key`          | Yes       | Your PayU merchant key    | `gt****`                               |
| `txnid`        | Yes       | Unique transaction ID     | `TXN1705055037779`                     |
| `amount`       | Yes       | Transaction amount        | `1.0`                                  |
| `productinfo`  | Yes       | Product description       | `Macbook Pro`                          |
| `firstname`    | Yes       | Customer first name       | `John`                                 |
| `email`        | Yes       | Customer email            | `user@example.com`                     |
| `phone`        | Yes       | Customer phone number     | `9999999999`                           |
| `surl`         | Yes       | Success callback URL      | `https://yourdomain.com/success`       |
| `furl`         | Yes       | Failure callback URL      | `https://yourdomain.com/failure`       |
| `hash`         | Yes       | SHA-512 hash for security | Generated hash string                  |
| `pg`           | Yes       | Payment gateway type      | `CC` (Card), `NB` (Net Banking), `UPI` |
| `bankcode`     | Yes       | Bank/payment method code  | `CC`, `SBIB`, etc.                     |
| `device_type`  | No        | Device type indicator     | `1` (Mobile)                           |
| `udf1-udf5`    | No        | User-defined fields       | Custom data                            |
| `sdk_platform` | No        | SDK platform information  | JSON array                             |

### Payment Gateway (pg) Codes

| Code     | Payment Method |
| -------- | -------------- |
| `CC`     | Credit Card    |
| `DC`     | Debit Card     |
| `NB`     | Net Banking    |
| `UPI`    | UPI            |
| `CASH`   | Cash Card      |
| `EMI`    | EMI            |
| `WALLET` | Wallet         |

### Bank Codes

For complete list of bank codes, refer to:

* [Net Banking Codes](https://docs.payu.in/docs/net-banking-codes)
* [Supported Payment Methods](https://docs.payu.in/docs/supported-payment-methods)

**Common Bank Codes**:

* `SBIB` - State Bank of India
* `AXIB` - Axis Bank
* `ICICIB` - ICICI Bank
* `HDFCB` - HDFC Bank

***

## Troubleshooting

### Common Issues and Solutions

#### 1. Interface Methods Error

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

#### 2. UPI Payment Options Not Working

**Issue**: UPI options like PhonePe, Google Pay not appearing

**Solution**:

* Add UPI SDK dependency (mandatory from v7.4.0+)
* Implement `checkForPaymentAvailability()` before showing options

#### 3. Hash Mismatch Error

**Issue**: Payment fails with hash validation error

**Solution**:

* Verify hash generation formula matches PayU documentation
* Ensure all parameters are in correct order
* Check for extra spaces or special characters
* Use UTF-8 encoding

#### 4. OTP Not Auto-filled

**Issue**: OTP assist not working

**Solution**:

* Add `RECEIVE_SMS` permission in AndroidManifest.xml
* Set `setAutoApprove(true)` or `setAutoSelectOTP(true)` in config
* Check permission is granted at runtime (Android M+)

#### 5. Payment Option Not Available

**Issue**: `isPaymentOptionAvailable()` returns false

**Solution**:

* Check if payment app is installed on device
* Verify merchant is registered for that payment option
* Ensure device and country are supported
* Check error message in `resultData.getErrorMessage()`

#### 6. SSL Errors

**Issue**: Bank pages not loading due to SSL errors

**Solution**:

* Set `setEnableSslDialog(true)` to show user-friendly message
* PayU will auto-redirect even with SSL errors
* Contact bank if issue persists

#### 7. WebView Not Loading

**Issue**: Payment page doesn't load in CustomBrowser

**Solution**:

* Verify post URL is correct (production vs staging)
* Check post data format and encoding
* Implement `setCBProperties()` callback correctly
* Enable WebView debugging for troubleshooting

***
