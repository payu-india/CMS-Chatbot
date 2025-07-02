---
title: UPI SDK Integration - TPV
deprecated: false
hidden: true
metadata:
  robots: index
---
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