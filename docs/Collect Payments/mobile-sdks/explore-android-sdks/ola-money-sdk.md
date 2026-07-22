---
title: Android Ola Money SDK
excerpt: A lightweight SDK which supports payments via OlaMoney (Postpaid + Wallet)
deprecated: false
hidden: false
metadata:
  title: Android Ola Money SDK
  description: >-
    This document provides instructions on setting up the PayU OlaMoney SDK in
    an Android application, including adding dependencies, using callback
    functions, checking OlaMoney eligibility, generating hashes, creating
    payment post data, and setting up for test/sandbox merchants.
  keywords:
    - PayU Ola Money SDK integration steps
    - PayU India Ola Money SDK for Android Integration Steps
    - Android Ola Money SDK integration Steps
    - Ola Money SDK integration steps
    - PayU Ola Money integration guide
    - >-
      How to integrate PayU Ola Money SDK in Android.Step-by-step PayU Ola Money
      SDK integration
    - PayU Ola Money SDK integration for Android apps
    - Detailed guide for PayU Ola Money SDK integration steps
    - PayU OlaMoney SDK integration steps
    - PayU India OlaMoney SDK steps
    - Android OlaMoney SDK integration
    - OlaMoney SDK integration steps
    - PayU OlaMoney integration guide
  robots: index
next:
  description: ''
---
## Set up build.gradle

Add the below dependency in the application’s build.gradle:

```Text build.gradle
implementation 'in.payu:olamoney:1.3.14'
```

## SDK Callbacks

PayU OlaMoney provides the following callback functions:

<br />

* `onPaymentInitialisationSuccess()`: Callback invoked if the customer is eligible for OlaMoney(Postpaid/Wallet).
* `onPaymentInitialisationFailure(int errorCode, String description)`: Callback invoked when there is some error in Customer eligibility.
* The following error messages are displayed when using onPaymentInitialisationFailure.

> ❗️ Error
>
> Following errors can occur if the `onPaymentInitialisationFailure` callback is failed:
>
> `100: Mandatory params are missing. Please check again!`
>
> `101 Something Went Wrong!`

Create an instance of OlaMoneyCallback similar to the following code block:

<Accordion title="Create an instance of `OlaMoneyCallback" icon="fa-code">
  ```java Java
      OlaMoneyCallback olaMoneyCallback = new OlaMoneyCallback() {
            @Override
            public void onPaymentInitialisationSuccess() {

            }

            @Override
            public void onPaymentInitialisationFailure(int i, String s) {

            }
        };
  ```
</Accordion>

## Checking OlaMoney Eligibility

Before proceeding with payment via OlaMoney payment mode merchant must check whether the customer is eligible for OlaMoney or not by using the following code block:

```Text JAVA
new OlaMoney().checkForPaymentAvailability(Activity activity, OlaMoneyCallback callback, PayUOlaMoneyParams olaMoneyParams);
```

Where `PayUOlaMoneyParams` object can be created as mentioned in the next section.

> 📘 Remember
>
> Values set in the `PayUOlaMoneyParams` must be the same that needs to be sent to PayU’s backend in payment post-data.

### Create PayUOlaMoneyParams

```Text JAVA
PayUOlaMoneyParams payUOlaMoneyParams = new PayUOlaMoneyParams(); 
payUOlaMoneyParams.setMobile(&lt;Customer Mobile number&gt;); 
payUOlaMoneyParams.setFirstName(&lt;Customer Firstname&gt;); 
payUOlaMoneyParams.setTxnId(&lt;TransactionId&gt;); 
payUOlaMoneyParams.setMerchantKey(&lt;PayU Merchant key&gt;); 
payUOlaMoneyParams.setHash(&lt;Hash generated for OlaMoney Eligibility check&gt;); 
payUOlaMoneyParams.setAmount(&lt;Amount that customer needs to pay&gt;); 
```

Where OlaMoney eligibility hash can be created as described in the following section.

### OlaMoney Eligibility Hash Generation

To generate the OlaMoney eligibility hash, use the method similar to the following:

`sha512(key|command|var1|salt)`

**Where**:

* Key – Merchant Key
* Command – get_eligible_payment_options  
  var1 – `{\\”amount\\”:\\””,\\”txnid\\”:\\”\\”,\\”mobile_number\\”:\\””,\\”first_name\\”:\\”\\”,\\”bankCode\\”:\\”OLAM\\”,\\”email\\”:\\”\\”,\\”last_name\\”:\\”\\”}`
* Salt – Merchant’s Salt

> 🚧 Remember
>
> The fields in the hashing string and the parameters in the var1 field should be in the exact same order as shown above.

| ErrorCode | Error Message                                         | Description                                                |
| :-------- | :---------------------------------------------------- | :--------------------------------------------------------- |
| 100       | Mandatory parameters are missing. Please check again! | Mandatory parameters for checking eligibility are missing. |
| 101       | Something Went Wrong!                                 |                                                            |

## Payment Post Data

Payment post data can be created as follows:

```Text JAVA
PaymentParams paymentParams = new PaymentParams(); 
paymentParams.setKey(&lt;Merchant Key&gt;); 
paymentParams.setAmount(&lt;Transaction Amount&gt;); 
paymentParams.setProductInfo(&lt;Product_info&gt;); 
paymentParams.setFirstName(&lt;First Name of Customer&gt;); 
paymentParams.setEmail(&lt;Customer's email&gt;); 
paymentParams.setTxnId(&lt;Transaction Id&gt;); 
paymentParams.setSurl(&lt;Success Url&gt;); 
paymentParams.setFurl(&lt;Failure Url&gt;); 
paymentParams.setUdf1(“udf1”); 
paymentParams.setUdf2(“udf2”); 
paymentParams.setUdf3(“udf3”); 
paymentParams.setUdf4(“udf4”); 
paymentParams.setUdf5(“udf5”); 
paymentParams.setPhone(&lt;Customer's Phone Number&gt;); 
paymentParams.setHash(&lt;Payment Hash&gt;); 
PostData postData = new PayUOlaMoneyPaymentParams().getPaymentPostData(paymentParams);
if(postData.getCode() == PayuErrors.NO_ERROR){
String postDataValue = postData.getResult();
}else{
String errorValue = postData.getResult();
}
```

## Set up for Test/Sandbox Merchant

If you use the SDK with a test merchant, please provide this metadata value to the manifest file.

```Text XML
<application>
    <meta-data
        android:name="payu_web_service_url"
        android:value="https://test.payu.in" />
</application>
```
