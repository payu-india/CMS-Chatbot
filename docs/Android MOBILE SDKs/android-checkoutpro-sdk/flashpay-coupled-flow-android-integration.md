---
title: FlashPay Coupled Flow Android Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
FlashPay SDK provides a comprehensive solution for Android payment processing with advanced 3DS protocols, end-to-end authentication, and biometric-based out-of-band (OOB) authentication. This guide will walk you through the complete integration process.

The FlashPay SDK enables secure payment processing on Android devices with:

* **3DS 2.0 Protocol Support**: Advanced authentication mechanisms
* **End-to-End Authentication**: Secure transaction processing
* **Biometric Authentication**: OOB authentication using device biometrics
* **Customizable UI**: Full control over the payment interface
* **Error Handling**: Comprehensive error management and reporting

## Prerequisites

Before you begin, ensure you have:

* Android Studio with Kotlin support
* Minimum Android API level 21 (Android 5.0)
* Valid PayU merchant credentials
* Basic understanding of Android development

## Step 1: Add Gradle Dependency

Add the FlashPay SDK dependency to your app-level `build.gradle` file:

```gradle
dependencies {
    implementation 'in.payu:threeds-sdk:X.X.X'
}
```

> **Note**: Replace `X.X.X` with the latest version of the FlashPay SDK.

## Step 2: Initialize Payment

Use the `initiatePayment` method to start the payment process:

```kotlin
fun initiatePayment(
    activity: AppCompatActivity,
    config: PayU3DS2Config,
    paymentParams: PaymentParams,
    callback: PayU3DS2PaymentCallback
)
```

### Basic Implementation

```kotlin
// Initialize payment configuration
val config = PayU3DS2Config().apply {
    isProduction = true
    autoRead = false
    autoSubmit = false
    setDefaultProgressLoader(true, "#FFFFFF")
}

// Create payment parameters
val paymentParams = PaymentParams().apply {
    key = "<Your Merchant Key>"
    amount = "<Transaction Amount>"
    cardNumber = "<Card Number>"
    expiryMonth = "12"
    expiryYear = "2025"
    cvv = "123"
    // Add other required parameters
}

// Initiate payment
initiatePayment(this, config, paymentParams, paymentCallback)
```

## Step 3: Configure PayU3DS2Config

The `PayU3DS2Config` object allows you to customize the payment flow behavior:

```kotlin
val config = PayU3DS2Config().apply {
    // Environment configuration
    isProduction = true  // Set to false for test environment
    
    // OTP handling
    autoRead = false     // Automatically read OTP from SMS
    autoSubmit = false   // Automatically submit OTP
    
    // UI configuration
    setDefaultProgressLoader(true, "#FFFFFF")
    
    // Timeout settings
    timeoutInMinutes = 5
    
    // Biometric authentication
    enableBiometric = true
}
```

### Configuration Properties

| Property         | Description                                                                 |
| ---------------- | --------------------------------------------------------------------------- |
| isProduction     | `Boolean` Set environment (true for production). By default, it is "false". |
| autoRead         | `Boolean`Enable automatic OTP reading. By default, it is "false".           |
| autoSubmit       | `Boolean`Enable automatic OTP submission. By default, it is "false".        |
| timeoutInMinutes | `Integer` Transaction timeout in minutes. By default, it is "5".            |
| enableBiometric  | `Boolean`Enable biometric authentication. By default, it is "false".        |

## Step 4: Customize UI Components

### Button Customization

```kotlin
val buttonCustomisation = ButtonCustomisation.Builder()
    .setBackgroundColor("#FF0000")
    .setCornerRadius(5)
    .setTextFontColor("#FFFFFF")
    .setTextFontSize(16)
    .build()

config.setButtonCustomisation(buttonCustomisation)
```

### Toolbar Customization

```kotlin
val toolbarCustomisation = ToolbarCustomisation.Builder()
    .setBackgroundColor("#000000")
    .setButtonText("Back")
    .setTextColor("#FFFFFF")
    .setHeaderText("Payment")
    .build()

config.setToolbarCustomisation(toolbarCustomisation)
```

### TextBox Customization

```kotlin
val textBoxCustomisation = TextBoxCustomisation.Builder()
    .setBorderColor("#CCCCCC")
    .setBorderWidth(1)
    .setCornerRadius(4)
    .setTextColor("#000000")
    .setTextFontSize(14)
    .build()

config.setTextBoxCustomisation(textBoxCustomisation)
```

### Label Customization

```kotlin
val labelCustomisation = LabelCustomisation.Builder()
    .setTextColor("#333333")
    .setTextFontSize(14)
    .setHeadingTextColor("#000000")
    .setHeadingTextFontSize(18)
    .build()

config.setLabelCustomisation(labelCustomisation)
```

## Step 5: Set Payment Parameters

Configure the `PaymentParams` object with transaction details:

```kotlin
val paymentParams = PaymentParams().apply {
    // Merchant details
    key = "<Your Merchant Key>"
    
    // Transaction details
    amount = "100.00"
    txnid = "TXN_${System.currentTimeMillis()}"
    productinfo = "Product Description"
    firstname = "Customer Name"
    email = "customer@example.com"
    phone = "9876543210"
    
    // Card details
    cardNumber = "4111111111111111"
    expiryMonth = "12"
    expiryYear = "2025"
    cvv = "123"
    nameOnCard = "CUSTOMER NAME"
    
    // URLs
    surl = "https://your-domain.com/success"
    furl = "https://your-domain.com/failure"
    
    // Optional parameters
    udf1 = "User Defined Field 1"
    udf2 = "User Defined Field 2"
    // ... add more UDF fields as needed
}
```

### Required Parameters

| Parameter   | Description                   | Example                                                    |
| ----------- | ----------------------------- | ---------------------------------------------------------- |
| key         | Merchant key provided by PayU | "your\_merchant\_key"                                      |
| amount      | Transaction amount            | "100.00"                                                   |
| txnid       | Unique transaction ID         | "TXN\_123456789"                                           |
| productinfo | Product description           | "Product Name"                                             |
| firstname   | Customer first name           | "John"                                                     |
| email       | Customer email                | "[john@example.com](mailto:john@example.com)"              |
| phone       | Customer phone number         | "9876543210"                                               |
| surl        | Success URL                   | "[https://domain.com/success](https://domain.com/success)" |
| furl        | Failure URL                   | "[https://domain.com/failure](https://domain.com/failure)" |

## Step 6: Implement Payment Callbacks

Create a callback handler to manage payment responses:

```kotlin
private val paymentCallback = object : PayU3DS2PaymentCallback {
    
    override fun onPaymentSuccess(response: Any?) {
        // Handle successful payment
        Log.d("FlashPay", "Payment successful: $response")
        // Process success response
    }
    
    override fun onPaymentFailure(response: Any?) {
        // Handle payment failure
        Log.e("FlashPay", "Payment failed: $response")
        // Show error message to user
    }
    
    override fun onPaymentCancel(isTxnInitiated: Boolean) {
        // Handle payment cancellation
        Log.d("FlashPay", "Payment cancelled. Transaction initiated: $isTxnInitiated")
        // Navigate back or show cancellation message
    }
    
    override fun onError(error: Any?) {
        // Handle errors
        Log.e("FlashPay", "Payment error: $error")
        // Show error dialog
    }
    
    override fun generateHash(
        data: HashMap<String, String>,
        hashGenerationListener: HashGenerationListener
    ) {
        // Generate hash for the transaction
        val hashString = data["hashString"] ?: ""
        val salt = "<Your Salt>"
        
        // Generate SHA-512 hash
        val hash = generateSHA512Hash(hashString + salt)
        
        val hashMap = HashMap<String, String>()
        hashMap["payment_hash"] = hash
        
        hashGenerationListener.onHashGenerated(hashMap)
    }
}
```

## Step 7: Generate Transaction Hash

Implement hash generation for secure transactions:

```kotlin
private fun generateSHA512Hash(input: String): String {
    return try {
        val digest = MessageDigest.getInstance("SHA-512")
        val hashBytes = digest.digest(input.toByteArray(StandardCharsets.UTF_8))
        hashBytes.joinToString("") { "%02x".format(it) }
    } catch (e: Exception) {
        Log.e("FlashPay", "Hash generation failed", e)
        ""
    }
}
```

### Hash Generation Process

1. **Concatenate Parameters**: Combine payment parameters in the specified order
2. **Add Salt**: Append your merchant salt to the string
3. **Generate Hash**: Create SHA-512 hash of the final string
4. **Return Hash**: Provide the hash through the callback

## Step 8: Handle ACS Content Configuration

Configure OTP and authentication content:

```kotlin
val acsContentConfig = ACSContentConfig().apply {
    // OTP configuration
    otpMessage = "Enter the OTP sent to your registered mobile number"
    resendButtonText = "Resend OTP"
    submitButtonText = "Submit"
    
    // Timer configuration
    showTimer = true
    timerFormat = "mm:ss"
    
    // Help text
    helpText = "Having trouble? Contact support"
}

config.setACSContentConfig(acsContentConfig)
```

## Error Handling

The SDK provides comprehensive error codes for debugging:

| Error Code | Description                | Solution                       |
| ---------- | -------------------------- | ------------------------------ |
| `E001`     | Invalid merchant key       | Verify merchant credentials    |
| `E002`     | Network connection failed  | Check internet connectivity    |
| `E003`     | Invalid card details       | Validate card information      |
| `E004`     | Transaction timeout        | Retry the transaction          |
| `E005`     | Authentication failed      | Check 3DS configuration        |
| `E006`     | User cancelled transaction | Handle cancellation gracefully |

### Error Handling Implementation

```kotlin
override fun onError(error: Any?) {
    when (error) {
        is PayUError -> {
            when (error.errorCode) {
                "E001" -> showError("Invalid merchant configuration")
                "E002" -> showError("Network error. Please try again")
                "E003" -> showError("Invalid card details")
                "E004" -> showError("Transaction timeout")
                else -> showError("Payment failed: ${error.errorMessage}")
            }
        }
        else -> showError("Unknown error occurred")
    }
}

private fun showError(message: String) {
    // Show error dialog or toast
    Toast.makeText(this, message, Toast.LENGTH_LONG).show()
}
```

## Testing and Validation

### Test Environment Setup

```kotlin
val testConfig = PayU3DS2Config().apply {
    isProduction = false  // Use test environment
    // ... other configurations
}
```

### Test Card Details

Use these test card numbers for integration testing:

| Card Type        | Card Number      | CVV  | Expiry |
| ---------------- | ---------------- | ---- | ------ |
| Visa             | 4111111111111111 | 123  | 12/25  |
| Mastercard       | 5555555555554444 | 123  | 12/25  |
| American Express | 378282246310005  | 1234 | 12/25  |

## Best Practices

1. **Security**
   * Always generate hash on server-side
   * Never store sensitive card data
   * Use HTTPS for all communications

2. **User Experience**
   * Implement proper loading states
   * Provide clear error messages
   * Handle network interruptions gracefully

3. **Performance**
   * Initialize SDK only when needed
   * Implement proper memory management
   * Use background threads for network calls

## Complete Integration Example

Here's a complete example of FlashPay integration:

```kotlin
class PaymentActivity : AppCompatActivity() {
    
    private lateinit var config: PayU3DS2Config
    private lateinit var paymentParams: PaymentParams
    
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_payment)
        
        setupFlashPayConfig()
        setupPaymentParams()
        
        // Trigger payment
        findViewById<Button>(R.id.btnPay).setOnClickListener {
            initiatePayment()
        }
    }
    
    private fun setupFlashPayConfig() {
        config = PayU3DS2Config().apply {
            isProduction = false
            autoRead = true
            autoSubmit = false
            setDefaultProgressLoader(true, "#FFFFFF")
        }
        
        // Customize UI
        val buttonCustomisation = ButtonCustomisation.Builder()
            .setBackgroundColor("#007BFF")
            .setCornerRadius(8)
            .setTextFontColor("#FFFFFF")
            .build()
        
        config.setButtonCustomisation(buttonCustomisation)
    }
    
    private fun setupPaymentParams() {
        paymentParams = PaymentParams().apply {
            key = "your_merchant_key"
            amount = "100.00"
            txnid = "TXN_${System.currentTimeMillis()}"
            productinfo = "Test Product"
            firstname = "Test User"
            email = "test@example.com"
            phone = "9876543210"
            cardNumber = "4111111111111111"
            expiryMonth = "12"
            expiryYear = "2025"
            cvv = "123"
            nameOnCard = "TEST USER"
            surl = "https://example.com/success"
            furl = "https://example.com/failure"
        }
    }
    
    private fun initiatePayment() {
        try {
            FlashPaySDK.initiatePayment(
                this,
                config,
                paymentParams,
                paymentCallback
            )
        } catch (e: Exception) {
            Log.e("FlashPay", "Payment initiation failed", e)
            showError("Failed to start payment")
        }
    }
    
    private val paymentCallback = object : PayU3DS2PaymentCallback {
        
        override fun onPaymentSuccess(response: Any?) {
            runOnUiThread {
                Toast.makeText(this@PaymentActivity, "Payment Successful!", Toast.LENGTH_LONG).show()
                finish()
            }
        }
        
        override fun onPaymentFailure(response: Any?) {
            runOnUiThread {
                showError("Payment failed. Please try again.")
            }
        }
        
        override fun onPaymentCancel(isTxnInitiated: Boolean) {
            runOnUiThread {
                showError("Payment cancelled by user")
            }
        }
        
        override fun onError(error: Any?) {
            runOnUiThread {
                showError("Error: $error")
            }
        }
        
        override fun generateHash(
            data: HashMap<String, String>,
            hashGenerationListener: HashGenerationListener
        ) {
            // In production, generate hash on server-side
            val hashString = data["hashString"] ?: ""
            val salt = "your_merchant_salt"
            val hash = generateSHA512Hash(hashString + salt)
            
            val hashMap = HashMap<String, String>()
            hashMap["payment_hash"] = hash
            hashGenerationListener.onHashGenerated(hashMap)
        }
    }
    
    private fun generateSHA512Hash(input: String): String {
        return try {
            val digest = MessageDigest.getInstance("SHA-512")
            val hashBytes = digest.digest(input.toByteArray(StandardCharsets.UTF_8))
            hashBytes.joinToString("") { "%02x".format(it) }
        } catch (e: Exception) {
            Log.e("FlashPay", "Hash generation failed", e)
            ""
        }
    }
    
    private fun showError(message: String) {
        Toast.makeText(this, message, Toast.LENGTH_LONG).show()
    }
}
```