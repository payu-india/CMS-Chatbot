---
title: UPI SDK Integration - TPV
deprecated: false
hidden: false
metadata:
  robots: index
---
For UPI integration, you need to post transaction details to PayU with beneficiary details for validation, similar to Net-Banking integration.

The request parameters for UPI integration are the same as Net-Banking integration. The `beneficiarydetail` parameter should include the UPI beneficiary details.

## Steps for Integration Changes

### SDK for Android

To integrate TPV in an Android app:

1. **Include the SDK**:\
   Add the following line to your `build.gradle` file under dependencies:
   ```groovy
   implementation 'in.payu:payu-checkout-pro:2.4.8-alpha1'
   ```

2. **Include Maven Repository (only for alpha version)**:\
   Add the following in the root-level `build.gradle`:
   ```groovy
   allprojects {
       repositories {
           maven { url "https://oss.sonatype.org/content/groups/staging/" }
       }
   }
   ```

3. **Merchant Changes for Beneficiary Details**:\
   Use the following code to pass the `beneficiarydetails` list:
   ```kotlin
   val beneficiaryDetailsList = ArrayList<PayUBeneficiaryDetail>()
   val beneficiaryDetails = PayUBeneficiaryDetail.Builder()
       .setBeneficiaryIfsc(<String>)
       .setBeneficiaryAccountNumber(<String>)
       .build()

   beneficiaryDetailsList.add(beneficiaryDetails)

   PayUPaymentParams.Builder()
       .setBeneficiaryDetailsList(beneficiaryDetailsList)
       .build()
   ```

### SDK for iOS

To integrate TPV in an iOS app:

1. **Create Beneficiary Details**:\
   Use the following Swift code for passing beneficiary details:
   ```swift
   var payuBeneficieryDetailsList = [PayUBeneficiaryParams]()
   let beneficiaryDetails1 = PayUBeneficiaryParams(beneficiaryAccountNumber: <String>, beneficiaryIFSC: <String>)
   let beneficiaryDetails2 = PayUBeneficiaryParams(beneficiaryAccountNumber: <String>, beneficiaryIFSC: <String>)
   payuBeneficieryDetailsList.append(beneficiaryDetails1)
   payuBeneficieryDetailsList.append(beneficiaryDetails2)

   let paymentParam = PayUPaymentParam(
       key: <String>,
       transactionId: <String>,
       amount: <String>,
       productInfo: <String>,
       firstName: <String>,
       email: <String>,
       phone: <String>,
       surl: <String>, // Success URL
       furl: <String>, // Failure URL
       environment: <Environment> /* .production or .test */
   )
   paymentParam.payuBeneficieryDetails = payuBeneficieryDetailsList
   ```

2. **Set Beneficiary Details Priority**:\
   If `beneficiaryDetails` are passed in both `PayUPaymentParams` and `SiParams`, priority is given to `PayUPaymentParams`.

## Hash Calculation

The hash is calculated using the following formula:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||beneficiarydetail|SALT)
```

Replace `SALT` with the salt value provided during onboarding.