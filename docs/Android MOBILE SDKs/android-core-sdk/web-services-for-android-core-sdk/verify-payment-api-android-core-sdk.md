---
title: 'Android SDK: Verify Payment Integration Guide'
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Verify Payment API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---

## Overview

The Android SDK provides a wrapper for the Verify Payment API that allows your mobile application to reconcile transactions with PayU's database securely. This integration is essential for Android developers implementing PayU payment functionality in their apps.

## Why Use Verify Payment in Your Android App

When implementing payments in your Android application, transaction responses may occasionally fail to reach your app due to network issues or user interactions (like app switching or device issues). The Verify Payment feature ensures your app can confirm transaction statuses directly with PayU's servers, preventing discrepancies in payment records.

> 📱 **Android Developer Note:**
>
> Implementing this verification step in your Android payment flow protects your application from potential payment status tampering and ensures a reliable payment experience for your users.

## Android Implementation

### Step 1: Configure the Verify Payment Request

In your Android payment handling class, implement the Verify Payment API using the MerchantWebService provided by the PayU Android SDK:

```java
// Import the required PayU Android SDK classes
import com.payu.india.Model.PayuResponse;
import com.payu.india.Payu.PayuConstants;
import com.payu.india.Payu.PayuMerchantWebService;

// In your payment verification method
private void verifyTransactionStatus(String transactionId) {
    MerchantWebService merchantWebService = new MerchantWebService();
    
    // Set your merchant credentials and API parameters
    merchantWebService.setKey(merchantKey);
    merchantWebService.setCommand(PayuConstants.VERIFY_PAYMENT);
    
    // Set the transaction ID to verify
    // For multiple transactions, use pipe symbol (|) as separator: "txnId1|txnId2|txnId3"
    merchantWebService.setVar1(transactionId);
    
    // Generate and set the hash for secure communication
    String hashString = merchantKey + "|" + PayuConstants.VERIFY_PAYMENT + "|" + transactionId + "|" + salt;
    String hash = calculateHash(hashString);
    merchantWebService.setHash(hash);
    
    // Execute the verification request
    merchantWebService.postWebServiceRequest(this);
}
```

### Step 2: Implement the Response Handler

Add the response handler in your Activity or Fragment that implements PayuResponseListener:

```java
@Override
public void onVerifyPaymentResponse(PayuResponse payuResponse) {
    if (payuResponse != null) {
        // Log the complete response for debugging
        Log.d(TAG, "Payment Verification Response: " + payuResponse.getRawResponse());
        
        // Process the verification result
        if (payuResponse.isResponseAvailable() && payuResponse.getResponseStatus().equals(PayuConstants.SUCCESS)) {
            // Transaction verified successfully
            // Update your app's UI or database based on the verified status
            String transactionStatus = payuResponse.getResult();
            updateTransactionStatus(transactionStatus);
        } else {
            // Verification failed - handle accordingly
            handleVerificationFailure(payuResponse.getErrorMessage());
        }
    }
}
```

## Best Practices for Android Implementation

1. **Always verify after receiving payment notifications** - Implement the verification call in your app's payment completion handler
2. **Handle timeouts appropriately** - Set reasonable timeouts for verification requests to avoid blocking your app's UI
3. **Implement proper error handling** - Create user-friendly error messages for different verification failure scenarios
4. **Store verification results** - Cache verification results locally to reduce unnecessary API calls
5. **Background processing** - Consider using WorkManager for verification to ensure it completes even if the app is closed

## Troubleshooting Android Integration

### Common Issues:

- **Hash calculation errors**: Ensure your hash generation uses the correct format and encoding
- **Network connectivity**: Implement proper retry logic for intermittent network failures
- **Transaction ID format**: Verify that transaction IDs are correctly formatted when sending multiple IDs

For additional support with Android SDK integration, refer to the complete PayU Android SDK documentation or contact PayU mobile developer support.