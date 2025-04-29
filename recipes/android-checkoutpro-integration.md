---
title: Android CheckoutPro Integration
description: >-
  After you include the SDK in app.build.gradle, you need to follow the steps
  described in this recipe to implement PayU Checkout Pro for Android SDK to
  implement basic integration.
hidden: false
recipe:
  color: '#018FF4'
  icon: 🦉
---
```java Java
val payUPaymentParams = PayUPaymentParams.Builder() 
    .setAmount()      
    .setIsProduction()  
    .setKey()       
    .setProductInfo()   
    .setPhone()  
    .setTransactionId() 
    .setFirstName() 
    .setEmail() 
    .setSurl() 
    .setFurl() 
    .setUserCredential()
    .setUserToken()
    .setAdditionalParams(<HashMap>) //Optional, can contain any additional PG params 
    .build() 
   
HashMap additionalParams = new HashMap(); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF1, "udf1"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF2, "udf2"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF3, "udf3"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF4, "udf4"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF5, "udf5"); 
// to show saved sodexo card
additionalParams.put(PayUCheckoutProConstants.SODEXO_SOURCE_ID, "srcid123"); 
 additionalParamsMap[PayUCheckoutProConstants.WALLET_URN] = "<Wallet URN>"
PayUPaymentParams.Builder builder = new PayUPaymentParams.Builder(); 
builder.setAmount("1.0") 
        .setIsProduction(true) 
        .setProductInfo("Macbook Pro") 
        .setKey(key) 
        .setPhone(phone) 
        .setTransactionId(String.valueOf(System.currentTimeMillis())) 
        .setFirstName("John") 
        .setEmail("john@yopmail.com") 
        .setSurl("https://payuresponse.firebaseapp.com/success") 
        .setFurl("https://payuresponse.firebaseapp.com/failure") 
        .setUserCredential(key+":john@yopmail.com") 
        .setAdditionalParams(additionalParams); 
PayUPaymentParams payUPaymentParams = builder.build();  

PayUSIParams siDetails  = new PayUSIParams.Builder()
                .setIsFreeTrial(true) //set it to true for free trial. Default value is false 
                .setBillingAmount("1.0")
                .setBillingCycle(PayUBillingCycle.ONCE)     
                .setBillingCurrency("INR")
                .setBillingInterval(1)
                .setPaymentStartDate("2021-12-24")
                .setPaymentEndDate("2021-12-31")
                .setBillingRule(PayuBillingRule.MAX)
                .setBillingLimit(PayuBillingLimit.ON)
                .setRemarks("SI Txn")
                .build();

paymentParam.splitPaymentDetails = "{
      "type":"absolute",
        "splitInfo":{
           "P****Y":{
             "aggregatorSubTxnId":"9a70ea0155268101001ba",
             "aggregatorSubAmt":"50",
             "aggregatorCharges":"20"
           },
           "P***K":{
             "aggregatorSubTxnId":"9a70ea0155268101001bb",
             "aggregatorSubAmt":"30"
          }
       }
    }";

HashMap<String, Object> additionalParams = new HashMap<>();  
additionalParams.put(PayUCheckoutProConstants.CP_VAS_FOR_MOBILE_SDK], <String>); 
additionalParams.put(PayUCheckoutProConstants.CP_PAYMENT_RELATED_DETAILS_FOR_MOBILE_SD K], <String>); 

void generateHash(HashMap<String,String> map, PayUHashGenerationListener hashGenerationListener) 

@Override 
public void generateHash(@NotNull HashMap map, @NotNull PayUHashGenerationListener hashGenerationListener) { 
    String hashName = map.get(CP_HASH_NAME); 
    String hashData = map.get(CP_HASH_STRING); 
    if (!TextUtils.isEmpty(hashName) && !TextUtils.isEmpty(hashData)) { 

//Do not generate hash from local, it needs to be calculated from server side only. Here, hashString contains hash created from your server side.
        String hash = hashString 
        if (!TextUtils.isEmpty(hash)) { 
            HashMap hashMap = new HashMap(); 
            hashMap.put(hashName, hash); 
            hashGenerationListener.onHashGenerated(hashMap); 
        } 
    } 
}

PayUCheckoutPro.open(
    Activity activity, 
    PayUPaymentParams payUPaymentParams, 
    PayUCheckoutProListener payUCheckoutProListener)
```

# Build the Payment Parameters

<!-- java@1-15 -->

To initiate a payment, your app must send transactional information to the Checkout Pro SDK.To pass this information, build a payment parameter object similar to the code snippet.

# Include the Additional Parameters

<!-- java@17-39 -->

Additional parameters are optional parameters such as UDF (User Defined Fields), static hashes, etc. More details on static hash generation and passing are mentioned in the hash generation section. The following is a list of other parameters that can be passed in additional parameters.

# For Recurring Payments(SI) [Optional]

<!-- java@41-52 -->

If you are integrating SI, generate the following payment parameters additionally.

# For Split Settlements [Optional]

<!-- java@54 -->

To integrate Split Settlements, create an object of the paymentParam class and set the splitPaymentDetails property of the object to a JSON string containing the details of the split transactions, and then pass it as a request parameter as shown in the code snippet.

# Pass Static Hashes

<!-- java@56-58 -->

This is for passing static hashes during integration.

# Pass Dynamic Hashes

<!-- java@60 -->

For generating and passing dynamic hashes, the merchant will receive a call from the generateHash method of PayUCheckoutProListener.

# Pass Generated Hash to SDK

<!-- java@62-76 -->

Prepare a map, where the key should be the hash name in "Step 1: Build the Payment Parameters" and value should be generated hash value and pass this map in onHashGenerated() method described above.

# Initiate the Payment

<!-- java@78-81 -->

Initialize the PayUCheckoutPro SDK by submitting the payment parameters prepared in the previous step and a reference to the transaction listener.