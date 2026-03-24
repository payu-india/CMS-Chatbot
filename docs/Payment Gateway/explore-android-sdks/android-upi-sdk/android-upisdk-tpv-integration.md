---
title: TPV with Android UPI SDK
excerpt: Implement TPV for UPI payment on Android apps
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
---
title: TPV with Android UPI SDK
excerpt: Implement TPV for UPI payment on Android apps
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
To pay using UPI, you need to pass a beneficiary account number parameter as described in the various implementation:

## Hash Generation

* For TPV transactions, hash calculation formula is different from the normal type of payment:
* For multiple account numbers, account numbers should be pipe-separated and max 4 account numbers are allowed.‌

<Accordion title="Hash Formula" icon="fa-code">
  <Callout icon="📘" theme="info">
    **Note**: It is recommended to pass ifscCode for UPI , UPI Intent and TEZ TPV transactions. The hash calculation will include ifscCode as shown below
  </Callout>

  ```
  // For single ifsc code
  beneficiarydetail = "{'beneficiaryAccountNumber':'917732227242','ifscCode':'SBIN000700'}"

  // For multiple ifsc number
  beneficiarydetail = "{'beneficiaryAccountNumber':'917732227242|72522762|283228235','ifscCode':'SBIN000700|KTKN2937492|ICIC0002522'}"    

  // Hash calculation
  Hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
  ```
</Accordion>

## Make Payment

<Accordion title="Set Beneficiary Parameters" icon="fa-code">
  ```Text JAVA
  // For single account number 
  mPaymentParams.setBeneficiaryAccountNumber("123456789");
  mPaymentParams.setIfscCode("SBIN000700");

  // For multiple account numbers
  mPaymentParams.setBeneficiaryAccountNumber("123456789|23456782|1234567"); 
  mPaymentParams.setIfscCode("SBIN000700|KTKN2937492|ICIC0002522");
  ```
  ```Text Kotlin
  // For single account number 
  mPaymentParams.beneficiaryAccountNumber = "123456789"
  mPaymentParams.ifscCode = "SBIN000700"

  // For multiple account numbers
  mPaymentParams.beneficiaryAccountNumber = "123456789|23456782|1234567"  
  mPaymentParams.ifscCode = "SBIN000700|KTKN2937492|ICIC0002522"
  ```
</Accordion>

### UPI Collect

After setting the above parameters for the UPI Collect transaction, you can get the payment post parameters using the following code block:

<Accordion title="UPI Collect Code Sample" icon="fa-code">
  ```Text JAVA
  // To provide customer VPA
  mPaymentParams.setVpa("valid VPA")‌;
  try {
      mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.UPITPV).getPaymentPostParams();
  } catch (Exception e) {
      e.printStackTrace();
  }
  ```
  ```Text Kotlin
  // To provide customer VPA
  mPaymentParams.vpa = "valid VPA";
  try {
      mPostData = PaymentPostParams(mPaymentParams, PayuConstants.UPI).paymentPostParams
  } catch (Exception e) {
      e.printStackTrace();
  }‌
  ```
</Accordion>

### UPI Intent (Generic Intent)

After setting the above parameters for the UPI INTENT transaction, you can get the payment post parameters using the following code snippet:

<Accordion title="Generic Intent Code Sample" icon="fa-code">
  ```Text JAVA
  try {
      mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.INTTPV).getPaymentPostParams();
  } catch (Exception e) {
      e.printStackTrace();
  }
  ```
  ```Text Kotlin
  try {
      mPostData = PaymentPostParams(mPaymentParams, PayuConstants.UPI_INTENT).paymentPostParams
  } catch (Exception e) {
      e.printStackTrace();
  }‌
  ```
</Accordion>

### UPI Intent (Specific App)

After setting the above parameters for the UPI INTENT transaction, you can get the payment post parameters using the following code snippet:

<Accordion title="Specific App Intent Code Sample" icon="fa-code">
  ```java Java
  // To pass the package name
  mPaymentParams.setPackageName("<Package Name>")‌;
  try {
      mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.INTTPV).getPaymentPostParams();
  } catch (Exception e) {
      e.printStackTrace();
  }
  ```
  ```kotlin Kotlin
  // To pass the package name
  mPaymentParams.setPackageName("<Package Name>")‌;
  try {
      mPostData = PaymentPostParams(mPaymentParams, PayuConstants.UPI_INTENT).paymentPostParams
  } catch (Exception e) {
      e.printStackTrace();
  }‌
  ```
</Accordion>

### Tez

For TEZ transaction, you can get the payment post params using the below:

<Accordion title="Tez (Google Pay) Code Sample" icon="fa-code">
  ```java Java
  try {
      mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.TEZTPV).getPaymentPostParams();
  } catch (Exception e) {
      e.printStackTrace();
  }
  ```
</Accordion>
