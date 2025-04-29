---
title: 1. SDK Integration
excerpt: >-
  Explore a complete, working code sample of integration with Android checkout
  pro SDK.
deprecated: false
hidden: false
metadata:
  title: Android Checkout Pro Integration Steps
  description: >-
    Integrate PayU's Android Checkout Pro SDK into your mobile applications for
    a seamless and secure payment experience. This detailed guide covers setup,
    customization, and advanced features, enabling developers to implement
    efficient payment solutions within Android apps. Perfect for developers
    aiming to enhance their app's payment capabilities with PayU's robust and
    comprehensive SDK.




    split Payments details
  keywords:
    - Android Checkout Pro SDK Integration Steps
    - PayU Android SDK integration steps
    - Mobile payment integration with PayU Android SDK steps
    - PayU Android Checkout Pro set up for Mobile
    - Android CheckoutPro SDK integration steps
    - PayU Hosted Checkout SDK for Mobile steps
    - Mobile Android SDK Basic Integration with Checkout Pro
    - Mobile Android SDK Recurring Payments Integration with Checkout Pro
    - Mobile Android SDK Standing Instruction Integration with Checkout Pro
    - Mobile Android SDK Split Payments Integration with Checkout Pro
    - Mobile Android SDK Split Settlements Integration with Checkout Pro
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: android-checkoutpro-test-integration
      title: 2. Test the Integration
---
Before you start with the integration, enable the payment methods that you want to offer to your customers from **Dashboard > Settings > Payment methods**.  For more information, refer. to [Checkout Payment Modes](doc:checkout-payment-modes). By default, Cards, UPI, and other payment methods are enabled, and PayU recommends you to enable other payment methods that are relevant to you.

## Step 1: Create a PayU account

First, create a PayU account. For more information, refer to [Register for a Merchant Account](https://docs.payu.in/docs/register-for-a-merchant-account-on-dashboard).

***

## Step 2: Include the SDK in your app build.gradle

> ❗️ Maven Central
> 
> PayU has moved to Maven Central, update your existing dependency with the following configuration:
> 
> ```Text build.gradle
> implementation 'in.payu:payu-checkout-pro:2.7.1' 
> ```

To include the CheckoutPro SDK in your project, add the following code snippet to your app’s <<glossary:build.gradle>> file inside the `android{}` block:

```Text build.gradle
compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }
    kotlinOptions {
        jvmTarget = '1.8'
    }
```

> ❗️ Compatibility
> 
> 1. **Android SDK** — Version 21 and above.
> 2. **Compile SDK** — version 31 and above.

### 2.1 Import Runtime Issue

> 🚧 Import Runtime Issue
> 
> 1. Dependency '`androidx.activity:activity:1.8.0`' requires libraries and applications that  
>          depend on it to compile against version 34 or later of the Android APIs.
> 
>    ```
>      :app is currently compiled against android-33.
> 
>      Recommended action: Update this project to use a newer compileSdk
>      of at least 34, for example 34.
> 
>      Note that updating a library or application's compileSdk (which
>      allows newer APIs to be used) can be done separately from updating
>      targetSdk (which opts the app in to new runtime behavior) and
>      minSdk (which determines which devices the app can be installed
>      on).
>    ```
> 2. Error: `Attribute application@theme value=(@style/Theme.TestApp) from AndroidManifest.xml:13:9-45
>    is also present at [in.payu:payu-checkout-pro-ui:1.9.20] AndroidManifest.xml:29:9-44 value=(@style/OnePayuTheme).
>    Suggestion: add 'tools:replace="android:theme"' to <application> element at AndroidManifest.xml:5:5-24:19 to override`.
> 
> **Solution**: After adding PayUCheckoutPro SDK gradle dependency, if below build error is received, add the below code in `application` tag of your App's `AndroidManifest.xm`l file
> 
> ```
> tools:replace="android:theme"
> ```
> 
> 3. Manifest merger failed: `Attribute application@allowBackup value=(true) from AndroidManifest.xml:6:9-35
>    is also present at [com.minkasu:minkasu-2fa:3.0.0] AndroidManifest.xml:14:18-45 value=(false).
>    Suggestion: add 'tools:replace="android:allowBackup"' to <application> element at AndroidManifest.xml:5:5-25:19 to override`.
> 
> **Solution**: After adding PayUCheckoutPro SDK gradle dependency, if below build error is received, add the below code in `application` tag of your App's AndroidManifest.xml file
> 
> ```
> tools:replace="android:allowBackup"
> ```

## Step 3: Build the payment parameters (mandatory step)

To initiate a payment, your app must send transactional information to the CheckoutPro SDK. To pass this information, create the`payUPaymentParams`object with the payment parameters.

### Step 3.1: Basic Integration

```Text Java
PayUPaymentParams.Builder builder = new PayUPaymentParams.Builder(); 
builder.setAmount(<String>)  
        .setIsProduction(<Boolean>)  //set is to true for Production and false for UAT
        .setProductInfo(<String>)   
        .setKey(<String>)      
        .setPhone(<String>)      
        .setTransactionId(<String>)  
        .setFirstName(<String>) 
        .setEmail(<String>) 
        .setSurl(<String>) //Pass your own surl your
        .setFurl(<String>) //Pass your own furl your
        .setUserCredential(<String>
        .setAdditionalParams(<HashMap<String,Object>>); //Optional, can contain any additional PG params  
PayUPaymentParams payUPaymentParams = builder.build();
```
```Text Kotlin
val payUPaymentParams = PayUPaymentParams.Builder() 
    .setAmount(<String>)      
    .setIsProduction(<Boolean>)  //set is to true for Production and false for UAT
    .setKey(<String>)       
    .setProductInfo(<String>)   
    .setPhone(<String>)  
    .setTransactionId(<String>) 
    .setFirstName(<String>) 
    .setEmail(<String>) 
    .setSurl(<String>) //Pass your own surl your
    .setFurl(<String>) //Pass your own furl your
    .setUserCredential(<String>) 
    .setAdditionalParams(<HashMap<String,Any?>>) //Optional, can contain any additional PG params 
    .build()  
```

 See [Payment Params Definition](https://docs.payu.in/docs/android-checkoutpro-integration-steps#step-35-payment-param-definitions) for parameter descriptions and sample values. 

> 📘 Important:
> 
> - The URLs used in surl and furl are for temporary use. PayU recommends you to design or use your own surl and furl after testing is completed. See [Handling SURL and FURL](https://docs.payu.in/docs/handling-redirect-urls-surlfurl-with-android-sdk). 
> 
> - The **TransactionId** parameter must not include special characters and must not exceed 25 characters.

### Step 3.2: For Recurring Payments(SI) (Optional)

If you are integrating SI, then generate the below payment params additionally

```Text Java
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
```
```Text Kotlin
val siDetails  = PayUSIParams.Builder()
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
                .build()
```

For more information on the PayUSIParams parameters, refer to [PayU Standing Instructions Parameters](https://docs.payu.in/docs/android-standing-instruction-parameters). After creating the above `PayUSIParams` object, configure it in the `PayUPaymentParams` object. For Standing Instruction, complete `PayUPaymentParams` similar to the following code block:

### Step 3.3: For UPI One Time Mandate Payments (Optional)

If you are integrating UPI OTM, then generate the below payment params additionally

```Text Java
PayUSIParams siDetails  = new PayUSIParams.Builder()
								.setPaymentStartDate("2025-04-14")
                .setPaymentEndDate("2025-04-21")
                .setPreAuthTxn(true)
                .build();
```
```Text kotlin
val siDetails = PayUSIParams.Builder()
								.setPaymentStartDate("2025-04-14")
                .setPaymentEndDate("2025-04-21")
                .setPreAuthTxn(true)
                .build();
```

Also need to enable isPreAuthTxn.

```Text Java
paymentParam.setPayUSIParams(siDetails);
```
```Text Kotlin
paymentParam.setPayUSIParams(siDetails)
```

### Step 3.4: For Additional Charges

If you are integrating additional charges or percentage additional charges, then generate the below payment params additionally

```Text Java
paymentParam.setAdditionalCharges("CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55")
paymentParam.setPercentageAdditionalCharges("CC:50,AMEX:100,DINR:75,DC:25")
```
```Text Kotlin
paymentParam.setAdditionalCharges("CC:12,AMEX:19,SBIB:98,DINR:2,DC:25,NB:55").setPercentageAdditionalCharges("CC:50,SBIB:100,DINR:100,DC:25,NB:50");
```

For more information on the Additional Charges, refer to [Collect Additional Charges](https://docs.payu.in/docs/collect-additional-charges). 

### Step 3:5: For split Payments details (Optional)

For a split payment transaction, create a JSON string with the split payment parameters as shown below:

#### JSON Request Structure of splitInfo Field

Here is a sample JSON structure for the `splitPaymentDetails` field:

```Text Json
{
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
}
```

Then create an object of the `PayUPaymentParam` class and set the `splitPaymentDetails` property of the object to the JSON string you created in the earlier step.

```
paymentParam.splitPaymentDetails = "";
```

> 🚧 Remember
> 
> - For the **absolute** type split, you must ensure that the sum of amount of all splits is equal to the parent transaction amount.
> - For the **percentage** type split, you must ensure that the sum of percentage of all splits is equal to 100. You can use any number decimal places for each split, but ensure the sum of percentage of all splits is equal to 100.

The following fields are included in the `splitPaymentDetails` parameter in a JSON format to specify the split details. The fields in the JSON format are described in the following table:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "   type  \n`mandatory`",
    "0-1": "`string` Any of the following types of split is specified in this field.  \n  \n**- absolute:** The absolute amount is specified for each part of the split. The absolute amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator. For a sample request and response, refer to Absolute Split During Payment  \n  \n**- percentage**: The percentage of the amount is specified for each part of the split. The percentage of the amount is specified in the aggregatorSubAmt field of the JSON for each child or aggregator. For a sample request and response, refer to Split by Percentage During Payment",
    "0-2": "absolute",
    "1-0": "splitInfo  \n`mandatory`",
    "1-1": "`JSON` This parameter must include the list of aggregator sub-transaction IDs and sub-amounts as follows:  \n  \n**- aggregatorSubTxnId**: The transaction ID of the aggregator is posted in this parameter. This field is mandatory and applicable only for child merchants.  \n  \n**- aggregatorSubAmt**: The transaction amount split for the aggregator is posted in this parameter. This field is mandatory.  \n  \n**- aggregatorCharges**: The transaction amount split for aggregator charges is posted in this parameter. This field is optional.  \n  \n**Note**: Only the parent aggregators can have the aggregatorCharges field as part of their JSON to collect charges.  \nThe sample request structure JSON Request Structure of splitInfo Field.",
    "1-2": "{  \n\"merchantKey1\": {  \n\"aggregatorSubTxnId\": \"30nknyhkhib\",  \n\"aggregatorSubAmt\": \"8\",  \n}"
  },
  "cols": 3,
  "rows": 2,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


### Step 3:5 : SKU details (Optional)

```Text Kotlin
SkuDetails: It contains below properties
SkuDetails(val skus: List<SKU>)
skus: "<ArrayList of SKU>"

SKU(
    val quantity: Int,
    val skuAmount: String,
    val skuId: String,
    val skuName: String,
    var offerKeys:ArrayList<String>?=null
)

skuId: "<Product Id which you use when creating offer on dashboard >"
skuName: "<Name of product>"
skuAmount: "<Amount of product>"
quantity: "<total quantity of product>"
offerKeys: "<Optional - Provide offer keys only if want to restrict offer for mention products, else set null>"
```

For more information on the SkuDetails parameters, refer to [Create SKU Based Offers details](https://docs.payu.in/docs/create-sku-based-offers-for-android-checkout-pro). After creating the above `SkuDetails` object, configure it in the `PayUPaymentParams` object. For SKU Details, complete `PayUPaymentParams` similar to the following code block:

```Text Java
paymentParam.setSkuDetails = "";
```

> 🚧 Keep in mind
> 
> if we are adding details of SKU offers, the amount passed in PayUPaymentParam must be equal to the sum of quantities \* skuAmount of each item.

### Step 3.6: Additional parameters (Optional)

Additional parameters are optional parameters such as UDF (User Defined Fields), static hashes, etc. More details on static hash generation and passing are mentioned in the hash generation section. The following is a list of other parameters that can be passed in additional parameters.

| Parameter                                              | Description                                                                                            | Example      |
| :----------------------------------------------------- | :----------------------------------------------------------------------------------------------------- | :----------- |
| PayUCheckoutProConstants.CP_UDF1        `optional`     | `String` User-defined field, Merchant can store their customer ID, etc.                                | udf1         |
| PayUCheckoutProConstants.CP_UDF2            `optional` | `String`User-defined field, Merchant can store their customer ID, etc.                                 | udf2         |
| PayUCheckoutProConstants.CP_UDF3        `optional`     | `String`User-defined field, Merchant can store their customer ID, etc                                  | udf3         |
| PayUCheckoutProConstants.CP_UDF4        `optional`     | `String`User-defined field, Merchant can store their customer ID, etc.                                 | udf4         |
| PayUCheckoutProConstants.CP_UDF5        `optional`     | `String`User-defined field, Merchant can store their customer ID, etc.                                 | udf5         |
| PayUCheckoutProConstants.SODEXO_SOURCE_ID `mandatory`  | `String`When we use SODEXO Card payment then it's a mandatory parameter otherwise not required.        | 456788765678 |
| PayUCheckoutProConstants.WALLET_URN `mandatory`        | `String`When we use ClossedLoop Wallet payment then it's a mandatory parameter otherwise not required. | 67890987     |

***

```Text JAVA
HashMap additionalParams = new HashMap(); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF1, "udf1"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF2, "udf2"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF3, "udf3"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF4, "udf4"); 
additionalParams.put(PayUCheckoutProConstants.CP_UDF5, "udf5"); 
// to show saved sodexo card
additionalParams.put(PayUCheckoutProConstants.SODEXO_SOURCE_ID, "srcid123"); 
// to show ClooseLoop Wallet 
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
        .setSurl("https://cbjs.payu.in/sdk/success") // This URL is used for Test Only. Don't go live
        .setFurl("https://cbjs.payu.in/sdk/failure") // This URL is used for Test Only. Don't go live
        .setUserCredential(key+":john@yopmail.com") 
        .setUserToken("")  //Optional, Only use for Offers
        .setSkuDetails(<SkuDetails>) //optional, create SKU Details as mention above
        .setAdditionalParams(<HashMap>); //Optional, can contain any additional PG params  
        .setPayUSIParams(siDetails) //Only for SI parameter
        .setSplitPaymentDetails(splitPaymentDetails); //Only for Split parameter
PayUPaymentParams payUPaymentParams = builder.build();  
```
```Text Kotlin
val additionalParamsMap: HashMap = HashMap() 
  additionalParamsMap[PayUCheckoutProConstants.CP_UDF1] = "udf1" 
  additionalParamsMap[PayUCheckoutProConstants.CP_UDF2] = "udf2" 
  additionalParamsMap[PayUCheckoutProConstants.CP_UDF3] = "udf3" 
  additionalParamsMap[PayUCheckoutProConstants.CP_UDF4] = "udf4" 
  additionalParamsMap[PayUCheckoutProConstants.CP_UDF5] = "udf5" 
  //to show saved sodexo card
  additionalParamsMap[PayUCheckoutProConstants.SODEXO_SOURCE_ID] = "srcid123" 
  //to show ClossedLoop Wallet
  additionalParamsMap[PayUCheckoutProConstants.WALLET_URN] = "<Wallet URN>"

  val payUPaymentParams = PayUPaymentParams.Builder() 
                          .setAmount("1.0") 
                          .setIsProduction(true) 
                          .setKey(key) 
                          .setProductInfo("Macbook Pro") 
                          .setPhone(phone) 
                          .setTransactionId(System.currentTimeMillis().toString()) 
                          .setFirstName("John") 
                          .setEmail("john@yopmail.com") 
                          .setSurl(“https://cbjs.payu.in/sdk/success”) // This URL is used for Test Only
                          .setFurl("https://cbjs.payu.in/sdk/failure ") // This URL is used for Test Only
                          .setUserCredential("$key:john@yopmail.com”) 
                          .setAdditionalParams(additionalParamsMap) 
                          .build() 
```

### Step 3.7: Payment Param Definitions

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "Key  \n`mandatory`",
    "0-1": "`String` This parameter must contain your merchant key received from PayU.",
    "0-2": "\"sms\\*\\*\\*\"",
    "1-0": "transactionId  \n`mandatory`",
    "1-1": "`String` It should be unique for each transaction.  \nCannot be null or empty and should be unique for each transaction. The maximum allowed length is 25 characters. It cannot contain special characters like: - \"\\_,$,%,&, etc\"",
    "1-2": "4567890",
    "2-0": "Amount  \n`mandatory`",
    "2-1": "`String` Total transaction amount.",
    "2-2": "100.0",
    "3-0": "productInfo  \n`mandatory`",
    "3-1": "`String` Information about the product.",
    "3-2": "\"ProductInfo\"",
    "4-0": "firstName  \n`mandatory`",
    "4-1": "`String` Customer’s first name.",
    "4-2": "\"Firstname\"",
    "5-0": "Email  \n`mandatory`",
    "5-1": "`String` Customer’s email id.",
    "5-2": "\"[test@payu.in](mailto:test@payu.in)\"",
    "6-0": "Phone  \n`mandatory`",
    "6-1": "`String` Customer’s phone number.",
    "6-2": "\"9999999999\"",
    "7-0": "Surl  \n`mandatory`",
    "7-1": "`String` When the transaction is successful, PayU will load this URL and pass the transaction response.  \n  \n**Sample SURL for testing**: <https://cbjs.payu.in/sdk/success>  \n  \n**Note**:- This URL is used for only Testing Purposes. Going live with this sample URL may result in transaction error.",
    "7-2": "The Surl that you have configured",
    "8-0": "Furl  \n`mandatory`",
    "8-1": "`String` When the transaction fails, PayU will load this URL and pass the transaction response.  \n  \n**Sample FURL for testing**: <https://cbjs.payu.in/sdk/failure>  \n  \n**Note**:- This URL is used for only Testing Purposes. Going live with this sample URL may result in transaction error. ",
    "8-2": "The Furl that you have configured",
    "9-0": "User Credential  \n`mandatory `",
    "9-1": "`String` This is used for the store card feature. PayU will store cards corresponding to passed user credentials and similarly, user credentials will be used to access previously saved cards. Format:  \n`<merchantKey>:<userId>  `  \nHere, the `UserId` is any ID/email/phone number to uniquely identify the user. \\*\\*",
    "9-2": "\"merchantKey:userId\"",
    "10-0": "isProduction `mandatory`",
    "10-1": "`String` Set the value of this parameter as `true`When you deploy the integration in production. To test the integration set the value as `false`. ",
    "10-2": "true",
    "11-0": "user_token  \n`mandatory`",
    "11-1": "`String` The use for this param is to allow the offer engine to apply velocity rules at a user level.  \n  \n-**Card Based Offers (CC, DC, EMI):** For card payment mode offers, if this parameter is passed then the velocity rules would be applied on this token, if not passed the same would be applied to the card number.  \n  \n\\-**UPI, NB, Wallet:** It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.  \n                                                                                                                           **Note:- **When we use Offer features then it's a mandatory parameter otherwise it's not required.",
    "11-2": "\"ABC456789\"",
    "12-0": "SkuDetails  \n`'madatory'`",
    "12-1": "Create list of SKU as per products added in cart and add this list in SKU details. and set sku detials to PayUPaymentParams.  \n**Note:- **When we use SKU features then it's a mandatory parameter otherwise it's not required.",
    "12-2": "",
    "13-0": "additionalCharges",
    "13-1": "String  \nThis parameter is required if merchant want to take additional charge from user",
    "13-2": "should be string with PG:Amount or IBIBOCode:Amount  \nSample : CC:10,NB:20,SBIB:15",
    "14-0": "percentageAdditionalCharges",
    "14-1": "String  \nThis parameter is required if merchant want to take percentage of TDR as additional charge from user for this feature dynamicConvFeeMerchant flag must be enable",
    "14-2": "should be string with PG:Amount or IBIBOCode:Amount  \nSample : CC:100,NB:50,SBIB:25"
  },
  "cols": 3,
  "rows": 15,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]


***

## Step 4: Secure the payment request using Hash

This step is to generate a hash that secures your payment request to PayU.

> 🚧 Remember
> 
> Always generate the hashes on your server. Do not generate the hashes locally in your app, as it will compromise the security of the transactions.

The CheckoutPro SDK uses hashes to ensure the security of the transaction and prevent any unauthorized intrusion or modification. The CheckoutPro SDK requires two types of hashes. For more information on the two types of hashes, refer to [Generate Hash](https://docs.payu.in/docs/hash-generation-for-checkoutpro-sdk) CheckoutPro SDK.

### Step 4.1: Set Up Payment Hashes

**Passing static hashes**

For passing static hashes during integration, use the following code snippet:

```Text JAVA
HashMap<String, Object> additionalParams = new HashMap<>();  
additionalParams.put(PayUCheckoutProConstants.CP_VAS_FOR_MOBILE_SDK], <String>); 
additionalParams.put(PayUCheckoutProConstants.CP_PAYMENT_RELATED_DETAILS_FOR_MOBILE_SD K], <String>); 
```
```Text Kotlin
val additionalParamsMap: HashMap<String, Any?> = HashMap() 
additionalParamsMap[PayUCheckoutProConstants.CP_VAS_FOR_MOBILE_SDK] = <String> 
additionalParamsMap[PayUCheckoutProConstants.CP_PAYMENT_RELATED_DETAILS_FOR_MOBILE_SDK] = <String> 
```

### Step 4.2: Passing dynamic hashes

For generating and passing dynamic hashes, the merchant will receive a call from the generateHash method of PayUCheckoutProListener.

```Text JAVA
public void generateHash(@NotNull HashMap map, @NotNull PayUHashGenerationListener hashGenerationListener) { 
}
```
```Text Kotlin
 fun generateHash(map:HashMap<String,String>,hashGenerationListener: PayUHashGenerationListener) 
```

Here:

`map` -> a hash map that contains hash string and hash name  
`hashGenerationListener` -> After the hash is generated on the merchant side. Pass the generated hash in the onHashGenerated() method of the hashGenerationListener.

```Text JAVA
interface PayUHashGenerationListener { 
    void onHashGenerated(HashMap<String,String> map) 
} 
```
```Text Kotlin
interface PayUHashGenerationListener { 
    fun onHashGenerated(map: HashMap<String,String?>) 
} 
```

The generateHash() method is called by the SDK each time it needs an individual hash. The CP_HASH_NAME will contain the name of the specific hash requested in that call, and the CP_HASH_STRING will contain the data/string that needs to be hashed.

### Step 4.3: Getting Hash data to calculate hash

Checkout Pro SDK will give a callback in the `generateHash()` method whenever any hash is needed by it. The merchant needs to calculate that hash and pass it back to the SDK.

To extract the hash string and hash name from the map received in `generateHash()` method, use the following keys:

`CP_HASH_STRING` -> This will contain a complete hash string excluding salt. For eg, for vas for mobile SDK hash, the hash string will contain “<key>\|<command>\|<var1>|”. Merchant can append their salt at the end of the hash string to calculate the hash.  
`CP_HASH_NAME `-> This will contain the hash name.

### Step 4.4: Pass generated hash to SDK

Prepare a map, where the key should be the hash name in Step 2: Build the Payment Parameters and value should be generated hash value and pass this map in `onHashGenerated()` method described above.

```Text JAVA
@Override 
public void generateHash(@NotNull HashMap map, @NotNull PayUHashGenerationListener hashGenerationListener) { 
    String hashName = map.get(CP_HASH_NAME); 
    String hashString = map.get(CP_HASH_STRING); 
    String postSalt = map.get(CP_POST_SALT); // compulsory for Additional Charges and Split Payment
    if (!TextUtils.isEmpty(hashName) && !TextUtils.isEmpty(hashString)) { 

//Do not generate hash from local, it needs to be calculated from server side only. Here, hashString contains hash created from your server side.
        String hash = "<create SHA -512 hash of 'hashString+salt+postSalt'>"  
        if (!TextUtils.isEmpty(hash)) { 
            HashMap hashMap = new HashMap(); 
            hashMap.put(hashName, hash); 
            hashGenerationListener.onHashGenerated(hashMap); 
        } 
    } 
}
```
```Text Kotlin
override fun generateHash( 
    map: HashMap, 
    hashGenerationListener: PayUHashGenerationListener 
) { 
    if (map.containsKey(CP_HASH_STRING) 
        && map.containsKey(CP_HASH_STRING) != null 
        && map.containsKey(CP_HASH_NAME) 
        && map.containsKey(CP_HASH_NAME) != null 
    ) { 
 
        val hashData = map[CP_HASH_STRING]  
        val hashName = map[CP_HASH_NAME]  
 
 //Do not generate hash from local, it needs to be calculated from server side only. Here, hashString contains hash created from your server side.
        val hash: String? = hashString;

        if (!TextUtils.isEmpty(hash)) { 
            val hashMap: HashMap = HashMap() 
            hashMap[hashName!!] = hash!! 
            hashGenerationListener.onHashGenerated(hashMap) 
        } 
    } 
} 
```

***

## Step 5: Initiate the Payment

Initialize the PayUCheckoutPro SDK by submitting the payment parameters prepared in the previous step and a reference to the transaction listener.

```Text JAVA
PayUCheckoutPro.open(
    Activity activity, 
    PayUPaymentParams payUPaymentParams, 
    PayUCheckoutProListener payUCheckoutProListener)
```
```Text Kotlin
PayUCheckoutPro.open(
    activity: Activity, 
    payUPaymentParams: PayUPaymentParams,  
    payUCheckoutProListener: PayUCheckoutProListener) 
```

## Step 6: Handle the Payment Callback

Confirm to PayUCheckoutProListener and use these functions to get appropriate callbacks from the SDK:

```Text JAVA
    PayUCheckoutPro.open(
            this,
            payUPaymentParams,
            new PayUCheckoutProListener() {
           
/// This function is called when we successfully process the payment
/// - Parameter response: success response           
                @Override
                public void onPaymentSuccess(Object response) {
                    //Cast response object to HashMap
                    HashMap result = (HashMap) response;
                    String payuResponse = (String)result.get(PayUCheckoutProConstants.CP_PAYU_RESPONSE);
                    String merchantResponse = (String) result.get(PayUCheckoutProConstants.CP_MERCHANT_RESPONSE);
                }

/// This function is called when we get failure while processing the payment
/// - Parameter response: failure response
                @Override
                public void onPaymentFailure(Object response) {
                    //Cast response object to HashMap
                    HashMap result = (HashMap) response;
                    String payuResponse = (String)result.get(PayUCheckoutProConstants.CP_PAYU_RESPONSE);
                    String merchantResponse = (String) result.get(PayUCheckoutProConstants.CP_MERCHANT_RESPONSE);
                }

/// This function is called when the user cancel’s the transaction
/// - Parameter isTxnInitiated: tells whether payment cancelled after reaching bankPage
                @Override
                public void onPaymentCancel(boolean isTxnInitiated) {
                  if(isTxnInitiated){
                     // call Verify API
                  }else {
                    // Show message
                  }
                }

/// This function is called when we encounter some error while fetching payment options or there is some validation error
/// - Parameter error: This contains error information
                @Override
                public void onError(ErrorResponse errorResponse) {
                    String errorMessage = errorResponse.getErrorMessage();
                }

                @Override
                public void setWebViewProperties(@Nullable WebView webView, @Nullable Object o) {
                    //For setting webview properties, if any. Check Customized Integration section for more details on this
                }

/// Use this function to provide hashes
/// - Parameters:
///   - param: Dictionary that contains key as PayUCheckoutProConstants.hashName & PayUCheckoutProConstants.hashString
///   - onCompletion: Once you fetch the hash from server, pass that hash with key as param[HashConstant.hashName]
                @Override
                public void generateHash(HashMap valueMap, PayUHashGenerationListener hashGenerationListener) {
                    String hashName = valueMap.get(PayUCheckoutProConstants.CP_HASH_NAME);
                    String hashData = valueMap.get(PayUCheckoutProConstants.CP_HASH_STRING);
                    if (!TextUtils.isEmpty(hashName) && !TextUtils.isEmpty(hashData)) {
                        //Do not generate hash from local, it needs to be calculated from server side only. Here, hashString contains hash created from your server side.
                        String hash = hashString;
                        HashMap dataMap = new HashMap();
                        dataMap.put(hashName, hash);
                        hashGenerationListener.onHashGenerated(dataMap);
                    }
                }
            }
);
```
```Text Kotlin
 PayUCheckoutPro.open( 
        this, payUPaymentParams, 
        object : PayUCheckoutProListener { 

 
            override fun onPaymentSuccess(response: Any) { 
                response as HashMap 
                val payUResponse = response[PayUCheckoutProConstants.CP_PAYU_RESPONSE]
                val merchantResponse = response[PayUCheckoutProConstants.CP_MERCHANT_RESPONSE]  
            } 

 
            override fun onPaymentFailure(response: Any) { 
                response as HashMap 
                val payUResponse = response[PayUCheckoutProConstants.CP_PAYU_RESPONSE]
                val merchantResponse = response[PayUCheckoutProConstants.CP_MERCHANT_RESPONSE]  
            } 

 
            override fun onPaymentCancel(isTxnInitiated:Boolean) { 
            } 

 
            override fun onError(errorResponse: ErrorResponse) { 
                val errorMessage: String 
                if (errorResponse != null && errorResponse.errorMessage != null && errorResponse.errorMessage!!.isNotEmpty()) 
                    errorMessage = errorResponse.errorMessage!! 
                else 
                    errorMessage = resources.getString(R.string.some_error_occurred) 
            } 
            
            override fun setWebViewProperties(webView: WebView?, bank: Any?) {
                //For setting webview properties, if any. Check Customized Integration section for more details on this
            }
                     
            override fun generateHash( 
                valueMap: HashMap, 
                hashGenerationListener: PayUHashGenerationListener 
            ) { 
                if ( valueMap.containsKey(CP_HASH_STRING) 
                    && valueMap.containsKey(CP_HASH_STRING) != null 
                    && valueMap.containsKey(CP_HASH_NAME) 
                    && valueMap.containsKey(CP_HASH_NAME) != null) { 
 
                    val hashData = valueMap[CP_HASH_STRING] 
                    val hashName = valueMap[CP_HASH_NAME] 
 
                    //Do not generate hash from local, it needs to be calculated from server side only. Here, hashString contains hash created from your server side.
                    val hash: String? = hashString
                    if (!TextUtils.isEmpty(hash)) { 
                        val dataMap: HashMap = HashMap() 
                        dataMap[hashName!!] = hash!! 
                        hashGenerationListener.onHashGenerated(dataMap) 
                    } 
                } 
            } 
        })
```

## Sample Responses

> 🚧 Watch Out
> 
> - In case of `UPI intent/InApp flow`,  you will not receive a callback response in surl or furl. In this case, the format of PayU response received will be different from other payment options that you need to handle at your end.                                                    
> - Consider the **mihpayid** in the PayU response as **PayU ID/ID**

### Card/NB/Wallet and other transactions

```Text Success
{
  "id": 403993715526100438,
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "gt***",
  "txnid": "1651831862726",
  "transaction_fee": "1.00",
  "amount": "1.00",
  "cardCategory": "domestic",
  "discount": "0.00",
  "addedon": "2022-05-06 15:41:38",
  "productinfo": "Macbook Pro",
  "firstname": "John",
  "email": "xyz@gmail.com",
  "phone": "7879*******",
  "udf1": "udf1",
  "udf2": "udf2",
  "udf3": "udf3",
  "udf4": "udf4",
  "udf5": "udf5",
  "hash": "62928c2f7490480951d25ae01bd0e748bb0b777ae27ef72eb93b7c1cc29eb2d84c4836faabe5ab1e1205a6f4a3f0876c5aece2ae96464c0cc9f1628693b074b1",
  "field1": "711633",
  "field2": "393337",
  "field3": "20220506",
  "field4": "0",
  "field5": "341867702575",
  "field6": "00",
  "field7": "AUTHPOSITIVE",
  "field8": "Approved or completed successfully",
  "field9": "No Error",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_no": "711633",
  "ibibo_code": "MASTCC",
  "error_code": "E000",
  "Error_Message": "No Error",
  "offer_key": "OfferKey@9227",
  "offer_failure_reason": "Invalid Offer Key.",
  "name_on_card": "PayuUser",
  "card_no": "512345XXXXXX2346",
  "issuing_bank": "HDFC",
  "card_type": "MAST",
  "is_seamless": 1,
  "surl": "https://payu.herokuapp.com/success",
  "furl": "https://payu.herokuapp.com/failure"
}
```
```Text Failure
{
  "id": "15130876153",
  "mode": "CC",
  "status": "failure",
  "unmappedstatus": "failed",
  "key": "sm*****",
  "txnid": "1651832033713",
  "transaction_fee": "1.00",
  "amount": "1.00",
  "cardCategory": "domestic",
  "offer_type": "instant",
  "addedon": "2022-05-06 15:44:09",
  "productinfo": "Macbook Pro",
  "firstname": "John",
  "email": "xyz@gmail.com",
  "phone": "7879*******",
  "udf1": "udf1",
  "udf2": "udf2",
  "udf3": "udf3",
  "udf4": "udf4",
  "udf5": "udf5",
  "hash": "c9c2d09d3387e7da70bc4ad6241f4ad3f610b3fcb0f9e481f5954a0d89d57791a5d027c303b239c1e8d6e0cad9c2d0b7ad87ba4911a60318675b15826c265929",
  "field5": "sl/mvXcXQLCWm49B/EAYjXMUh1o=",
  "field7": "EVNEGATIVE",
  "field9": "PROCEED",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "ibibo_code": "CC",
  "error_code": "E1302",
  "Error_Message": "Bank failed to authenticate the customer due to 3D Secure Enrollment decline",
  "offer_key": "OfferKey@9227",
  "offer_failure_reason": "Invalid Offer for merchant. ",
  "name_on_card": "PayuUser",
  "card_no": "512345XXXXXX2346",
  "issuing_bank": "HDFC",
  "card_type": "MAST",
  "is_seamless": 1,
  "surl": "https://payu.herokuapp.com/success",
  "furl": "https://payu.herokuapp.com/failure"
}
```

### UPI Intent /InApp payments

```Text Success
{
  "status": "success",
  "result": {
    "mihpayid": 15130530926,
    "mode": "UPI",
    "status": "success",
    "key": "sm*****",
    "txnid": "1651828235258",
    "amount": "1.00",
    "addedon": "2022-05-06 14:40:48",
    "productinfo": "Macbook Pro",
    "firstname": "John",
    "lastname": "",
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": "",
    "zipcode": "",
    "email": "xyz@gmail.com",
    "phone": "7879*******",
    "udf1": "udf1",
    "udf2": "udf2",
    "udf3": "udf3",
    "udf4": "udf4",
    "udf5": "udf5",
    "udf6": "",
    "udf7": "",
    "udf8": "",
    "udf9": "",
    "udf10": "",
    "card_token": "",
    "card_no": "",
    "field0": "",
    "field1": "",
    "field2": "",
    "field3": "andy**********@okhdfcbank",
    "field4": "",
    "field5": "",
    "field6": "ANAND*************|0000000000",
    "field7": "APPROVED OR COMPLETED SUCCESSFULLY|00",
    "field8": "",
    "field9": "Success|Completed Using Callback",
    "payment_source": "payuPureS2S",
    "PG_TYPE": "UPI-PG",
    "error": "E000",
    "error_Message": "No Error",
    "net_amount_debit": 1,
    "unmappedstatus": "captured",
    "hash": "8710a26e6f9da96e2de8648b7122b2ee243ba12e92059b69c66c831ec08cc69eaabff07bfea65de781a6a1c7605271164bf6075ab6e459687baa4888f4d97f2e",
    "bank_ref_no": "212631548690",
    "bank_ref_num": "212631548690",
    "bankcode": "INTENT",
    "surl": "https://payu.herokuapp.com/success",
    "furl": "https://payu.herokuapp.com/failure"
  }
}
```
```Text Failure
{
  "status": "success",
  "result": {
    "mihpayid": "15130540072",
    "mode": "UPI",
    "status": "failure",
    "key": "sm*****",
    "txnid": "1651828340011",
    "amount": "1.00",
    "addedon": "2022-05-06 14:42:25",
    "productinfo": "Macbook Pro",
    "firstname": "John",
    "lastname": "",
    "address1": "",
    "address2": "",
    "city": "",
    "state": "",
    "country": "",
    "zipcode": "",
    "email": "xyz@gmail.com",
    "phone": "7879******",
    "udf1": "udf1",
    "udf2": "udf2",
    "udf3": "udf3",
    "udf4": "udf4",
    "udf5": "udf5",
    "udf6": "",
    "udf7": "",
    "udf8": "",
    "udf9": "",
    "udf10": "",
    "card_token": "",
    "card_no": "",
    "field0": "",
    "field1": "",
    "field2": "",
    "field3": "",
    "field4": "",
    "field5": "",
    "field6": "",
    "field7": "",
    "field8": "",
    "field9": "response_from_psp",
    "payment_source": "payuPureS2S",
    "PG_TYPE": "UPI-PG",
    "error": "E308",
    "error_Message": "Transaction Failed at bank end.",
    "net_amount_debit": "0",
    "unmappedstatus": "failed",
    "hash": "5c4d80992f88a3cdd1b5b2a1452d69fe27fece37bc33838e2fb31a70e5636e857fc66952a750b638876bceace31fb8435307a9e2b3bda0e4b29f3478e4bb595a",
    "bank_ref_no": "",
    "bank_ref_num": "",
    "bankcode": "INTENT",
    "surl": "https://payu.herokuapp.com/success",
    "furl": "https://payu.herokuapp.com/failure"
  }
}
```

***

Placeholder for CheckoutPro Recipes

***

## Additional Integrations

The following are the additional Android SDK offerings:

- Offer Integration
- MCP Integration
- Custom Note Integration
- Add-on SDKs

## Offers Integration

Kindly add the `setUserToken` parameter in paymentParam.

```
paymentParam.setUserToken = "";
```

[block:parameters]
{
  "data": {
    "h-0": "parameter",
    "h-1": "Description",
    "0-0": "user_token  \n`mandatory` ",
    "0-1": "The use for this param is to allow the offer engine to apply velocity rules at a user level.  \n  \n-**Card Based Offers (CC, DC, EMI):** In the case of card payment mode offers, if this parameter is passed the velocity rules would be applied on this token, if not passed the same would be applied to the card number.  \n  \n\\-**UPI, NB, Wallet:** It is mandatory for UPI, NB, and Wallet payment modes. If not passed the validation rules would not apply.                                                                                                                                 **Note:- **When we use Offer features then it's a mandatory parameter otherwise it's not required."
  },
  "cols": 2,
  "rows": 1,
  "align": [
    "left",
    "left"
  ]
}
[/block]


Kindly refer to the below [link](https://docs.payu.in/docs/payu-hosted-checkout-integration-with-offers) for more details about Offer Integration. 

## MCP Integration

> 📘 Note
> 
> MCP is inbulit in CheckoutPro SDK. Get in touch with your KAMs to enable this feature for your MID.

## Custom Note Integration

This section describes how to integrate custom notes in PayUCheckoutPro SDK.

### Step 1: Create a Custom Note List

Create a list of custom notes that you want to pass to the CheckoutPro SDK. For each custom note, custom_note and `custom_note_category` need to be passed.

```Text Java
// for specific custom_note_category

      ArrayList<CustomNote> customNote = new ArrayList<>();
      ArrayList<PaymentType> noteCategory1 = new ArrayList<>();
      noteCategory1.add(PaymentType.CARD);
      CustomNote customNote1 = new CustomNote("Please welcome note", noteCategory1);
      customNote1.setCustom_note("Please welcome note");
      customNote1.setCustom_note_category(noteCategory1);

      ArrayList<PaymentType> noteCategory2 = new ArrayList<>();
      noteCategory2.add(PaymentType.CARD);
      CustomNote customNote2 = new CustomNote("Please welcome note", noteCategory1);
      customNote2.setCustom_note("Please welcome note");
      customNote2.setCustom_note_category(noteCategory2);
      customNote.add( customNote1);
      customNote.add( customNote2); 
        
// when want to pass same custom note for multiple custom_note_category

        ArrayList<CustomNote> customNote = new ArrayList<>();
        ArrayList<PaymentType> noteCategory1 = new ArrayList<>();
        noteCategory1.add(PaymentType.CARD);
        noteCategory1.add(PaymentType.NB);
        noteCategory1.add(PaymentType.UPI);
        CustomNote customNote1 = new CustomNote("Please welcome note", noteCategory1);
        customNote1.setCustom_note("Please welcome note");
        customNote1.setCustom_note_category(noteCategory1);
        customNote.add( customNote1);
        
        // if do not want to pass any custom_note_category
        ArrayList<CustomNote> customNote = new ArrayList<>();
        CustomNote customNote1 = new CustomNote("Please welcome note", null);
        customNote1.setCustom_note("Please welcome note");
        customNote1.setCustom_note_category(null);
        
```
```Text Kotlin
     // for specific custom_note_category
        val customNote = ArrayList<CustomNote>()
        customNote.add(CustomNote().also{
        it.custom_note = "Please welcome in Cards"
        it.custom_note_category = ArrayList<PaymentType>().also {
                it.add(PaymentType.CARD)
            }
        }
        // when want to pass same custom note for multiple custom_note_category
       
        val customNote = ArrayList<CustomNote>()
        customNote.add(CustomNote().also{
        it.custom_note = "Please welcome in Cards"
        it.custom_note_category = ArrayList<PaymentType>().also {
                it.add(PaymentType.NB)
                it.add(PaymentType.CARD)
            }
        } 
        // if do not want to pass any custom_note_category
        
        val customNote = ArrayList<CustomNote>()
        customNote.add(CustomNote().also{
        it.custom_note = "Please welcome in Cards"
        it.custom_note_category = null
        } 
```

### Step 2: Pass Custom Note List to SDK

To pass the custom note list created in the above section to the SDK. Create a `PayUCheckoutProConfig` object and set the `CustomNoteDetails` similar to the following code block:

```Text Java
PayUCheckoutProConfig payUCheckoutProConfig = new PayUCheckoutProConfig();
payUCheckoutProConfig.setCustomNoteDetails("");
```
```Text Kotlin
val checkoutProConfig = PayUCheckoutProConfig()  
checkoutProConfig.customNoteDetails = customNote
```

## Additional SDK Offerings

 If you want to add features like **Native OTP**, **Gpay InApp**, **PhonePe Inapp**, and **Ola Money** in our PayUCheckoutPro SDK, then please refer to the below [Add-on SDKs](https://dash.readme.com/project/payu-hosted-checkout/v1/docs/android-checkoutpro-addonsdks)