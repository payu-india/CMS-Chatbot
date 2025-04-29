---
title: TPV Integration - Android
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
This section describes the integration of third-party validation (TPV) on PayUCheckoutPro SDK. TPV is essential for businesses in the BFSI sector to ensure transactions are made from registered bank accounts, complying with SEBI guidelines.

#### Payment Modes Supported

- Net-banking
- UPI

## Step 1: Include the SDK in your app build.gradle

Add the following line in the app.build.grade:

```
implementation 'in.payu:payu-checkout-pro:2.4.8-alpha1
```

## Step 2: Update root level build.gradle(only for alpha version)

Update root level in the build.gradle (for alpha version only):

```
allprojects {    repositories {        maven {url  "<https://oss.sonatype.org/content/groups/staging/"}>    } }\`
```

## Step 3: TPV Integration changes

The step is to perform the following:

- **Beneficiary Details**: The code sets up the details of beneficiaries (such as their IFSC code and account number) who will receive payments.
- **Payment Parameters**: These details are then added to the payment parameters, which are used to configure the payment request.  
  This setup is essential for ensuring that the payment gateway knows where to direct the funds during a transaction.

To include TPV integration changes:

1. Create a list to hold beneficiary details:

```kotlin
   val beneficiaryDetailsList = ArrayList<PayUBeneficiaryDetail>()
```

2. Create a beneficiary detail object with IFSC and account number:
   ```kotlin
   val beneficiaryDetails = PayUBeneficiaryDetail.Builder()
       .setBeneficiaryIfsc(<String>)
       .setBeneficiaryAccountNumber(<String>)
       .build()
   ```

3. Add the beneficiary detail object to the list:
   ```kotlin
   beneficiaryDetailsList.add(beneficiaryDetails)
   ```
   <br />

4. Repeat steps 2 and 3 for another beneficiary:
   ```kotlin
   val beneficiaryDetails1 = PayUBeneficiaryDetail.Builder()
       .setBeneficiaryIfsc(<String>)
       .setBeneficiaryAccountNumber(<String>)
       .build()
   beneficiaryDetailsList.add(beneficiaryDetails1)
   ```
   <br />

5. Set the list of beneficiary details in the payment parameters:
   ```kotlin
   PayUPaymentParams.Builder()
       .setBeneficiaryDetailsList(beneficiaryDetailsList)
       .build()
   ```