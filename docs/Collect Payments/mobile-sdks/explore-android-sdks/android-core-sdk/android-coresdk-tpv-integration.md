---
title: TPV with Android Core SDK
excerpt: ''
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
title: TPV with Android Core SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: >-
    Third Party Verification (TPV) with PayU Android Core SDK: beneficiary validation, UPI TPV flow, and server-side hash setup.
  keywords:
    - payu android core sdk tpv integration guide india
    - tpv third party verification upi sdk android integration
    - android payment gateway tpv beneficiary validation payu
    - payu coresdk android tpv uPI collect intent flow
    - integrate tpv payment android native sdk payu gateway
    - android seamless payment tpv verification integration payu
    - mobile payment sdk android tpv bank account validation
    - payu android core sdk third party verification steps
    - payment gateway android tpv integration developer guide
    - upi tpv android sdk integration payu india
    - android native payment tpv flow payu coresdk
    - server side hash tpv android sdk integration payu
  robots: index
next:
  description: ''
---
This section describes <Glossary>TPV</Glossary> integration with Android SDK platform.

> 📘 Note:
>
> For TPV transactions, you need to have a different Merchant ID. Contact your Key Account Manager at PayU for the same.

## Step 1: Hash calculation
<Accordion title="Hash logic" icon="fa-code">
For TPV transactions, the hash calculation formula is different from the typical type of payment:

The account numbers should be separated by a pipe (|) character for multiple account numbers, and a maximum of four are allowed.‌

```
// For single account number
beneficiarydetail = “{‘beneficiaryAccountNumber’:’123456789′}”
// For multiple account number
beneficiarydetail = “{‘beneficiaryAccountNumber’:’123456789|54321234|98765673|34767988′}”
// Hash calculation
Hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```
</Accordion>
It is recommended to pass ifscCode for Net Banking, UPI, and TEZ TPV transactions. Hash calculation will include ifscCode similar to the following code block:

```
// For single ifsc code
beneficiarydetail = “{‘beneficiaryAccountNumber’:’917732227242′,’ifscCode’:’SBIN000700′}”
// For multiple ifsc number
beneficiarydetail = “{‘beneficiaryAccountNumber’:’917732227242|72522762|283228235′,’ifscCode’:’SBIN000700|KTKN2937492|ICIC0002522′}” 
// Hash calculation
Hash = sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```

## Step 2: Make Payment

<Accordion title="Net Banking" icon="fa-code">
  To pay using Net Banking, you need to pass payment params along with the following additional parameters:

  ```Text Java
  mPaymentParams.setBeneficiaryAccountNumber("123456789");
  mPaymentParams.setIfscCode("SBIN000700");
  mPaymentParams.setBankCode("AXNBTPV");
  ```
  ```Text Kotlin
  mPaymentParams.beneficiaryAccountNumber = "123456789"
  mPaymentParams.ifscCode = "SBIN000700"
  mPaymentParams.bankCode = "AXNBTPV"
  ```

  After setting the above parameters, you can get the payment post parameters using the following code snippet:

  ```Text Node

  BeneficiaryDetails beneficiaryDetails = new BeneficiaryDetails();
  beneficiaryDetails.setBeneficiaryName("John Doe");
  beneficiaryDetails.setBeneficiaryAccountNumber("51234567890");
  beneficiaryDetails.setBeneficiaryAccountType(BeneficiaryAccountType.SAVINGS);
  beneficiaryDetails.setBeneficiaryIfsc("ICIC0006621")
  SIParams siParams = new SIParams();
  siParams.setBeneficiarydetail(beneficiaryDetails);
  ```
</Accordion>

<Accordion title="UPI" icon="fa-code">
  ‌To pay using UPI, you need to pass beneficiary account number parameters similar to the following code snippet:

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

<Accordion title="UPI collect" icon="fa-code">
  After setting the above parameters for a UPI Collect transaction, you can get the payment post parameters using the following code snippet:

  ```Text JAVA
  ‌     try {
              mPostData = new PaymentPostParams(mPaymentParams, PayuConstants.UPITPV).getPaymentPostParams();
          } catch (Exception e) {
              e.printStackTrace();
          }‌
  ```
  ```Text Kotlin
       try {
              mPostData = PaymentPostParams(mPaymentParams, PayuConstants.UPI).paymentPostParams
          } catch (Exception e) {
              e.printStackTrace();
          }‌
  ```
</Accordion>

<Accordion title="TEZ" icon="fa-code">
  ```Text JAVA
  ‌     try {
              mPostData = new PaymentPostParams(mPaymentParams,  PayuConstants.TEZTPV).getPaymentPostParams();
          } catch (Exception e) {
              e.printStackTrace();
          }
  ```
  ```Text Kotlin
       try {
              mPostData = PaymentPostParams(mPaymentParams, PayuConstants.TEZ).paymentPostParams  
          } catch (Exception e) {
              e.printStackTrace();
          }
  ```
</Accordion>