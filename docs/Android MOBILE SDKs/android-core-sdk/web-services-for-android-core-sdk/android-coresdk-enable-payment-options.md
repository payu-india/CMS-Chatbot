---
title: Enable Payment Options
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Enable Payment Options API - Android Core SDK
  description: ''
  robots: index
next:
  description: ''
---
This API is used enable multiple payment options on your checkout page. 

> 📘 Hash logic
> 
> The hash logic for this API is:
> 
> `<key>|payment_related_details_for_mobile_sdk|<userCredential>|<salt>`
> 
> For more information, refer to [Generate Static Hash](doc:generate-static-hash-android-sdk-pro).

## Step 1: Execute GetPaymentRelatedDetailsTask

This class is used to get payment-related details. It takes an instance of a class that implements the `PaymentRelatedDetailsListener` interface as input.

```Text Node
GetPaymentRelatedDetailsTask paymentRelatedDetailsForMobileSdkTask = new GetPaymentRelatedDetailsTask(this);
```

 The `PaymentRelatedDetailsListener` interface has an abstract method called `onPaymentRelatedDetailsResponse()`. This method is called when the payment-related details are received.

## Step 2: Get Response using onPaymentRelatedDetailsResponse()

Get response to determine the availability of various payment options (UPI, Google Pay, PhonePe, LazyPay, and Generic Intent) similar to the following code snippet:

```Text Node
@Override
public void onPaymentRelatedDetailsResponse(PayuResponse payuResponse) {
mPayuResponse = payuResponse;
// Check if UPI as payment option available.
if(payuResponse.isUpiAvailable()){
// To check if UPI as payment option is available
}
if(payuResponse.isGoogleTezAvailable()){
// To check if Google Pay as payment option is available
}
if(payuResponse.isPhonePeIntentAvailable()){
// To check if Phonepe as payment option is available
}
if(payuResponse.isLazyPayAvailable()){
// To check if LazyPay as payment option is available
}
if(payuResponse.isGenericIntentAvailable()){
// To check if Generic Intent as payment option is available
}
//For SI Payments
if(payuResponse.isNBAvailableFoSI){
//Fetch SI NB List from payuResponse.getSiBankList() method
}
}
```

This method is called when the payment-related details are received. This method takes a `PayuResponse` object as input. The `PayuResponse` object contains the payment-related details.

The `onPaymentRelatedDetailsResponse()` method can be used to check if the following payment options are available:

- UPI
- Google Pay
- PhonePe Intent
- LazyPay
- Generic Intent
- The `onPaymentRelatedDetailsResponse()` method can also be used to fetch the list of SI banks if SI payments are enabled.