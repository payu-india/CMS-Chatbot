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

**Integration Steps**

<Cards columns={3}>
  <Card title="1. Include SDK" href="#step-1-include-the-sdk-in-your-app-buildgradle">
    Add PayUCheckoutPro SDK dependency
  </Card>

  <Card title="2. Update Build Gradle" href="#step-2-update-root-level-buildgradleonly-for-alpha-version">
    Configure root level build.gradle for alpha version
  </Card>

  <Card title="3. TPV Integration" href="#step-3-tpv-integration-changes">
    Set up beneficiary details and payment parameters
  </Card>
</Cards>

<Accordion title="Payment Modes Supported" icon="fa-list">
  * Net-banking
  * UPI
</Accordion>

## Step 1: Include the SDK in your app build.gradle

<Accordion title="Gradle Dependency" icon="fa-cog">
  Add the following line in the app.build.grade:

  ```gradle
  implementation 'in.payu:payu-checkout-pro:2.4.8-alpha1'
  ```
</Accordion>

## Step 2: Update root level build.gradle(only for alpha version)

<Accordion title="Root Level Configuration" icon="fa-cog">
  Update root level in the build.gradle (for alpha version only):

  ```gradle
  allprojects {
      repositories {
          maven {
              url "https://oss.sonatype.org/content/groups/staging/"
          }
      }
  }
  ```
</Accordion>

## Step 3: TPV Integration changes

The step is to perform the following:

* **Beneficiary Details**: The code sets up the details of beneficiaries (such as their IFSC code and account number) who will receive payments.
* **Payment Parameters**: These details are then added to the payment parameters, which are used to configure the payment request.
  This setup is essential for ensuring that the payment gateway knows where to direct the funds during a transaction.

<Accordion title="TPV Integration Code Sample" icon="fa-code">
  To include TPV integration changes:

  **1. Create a list to hold beneficiary details:**

  ```kotlin
  val beneficiaryDetailsList = ArrayList<PayUBeneficiaryDetail>()
  ```

  **2. Create a beneficiary detail object with IFSC and account number:**

  ```kotlin
  val beneficiaryDetails = PayUBeneficiaryDetail.Builder()
      .setBeneficiaryIfsc(<String>)
      .setBeneficiaryAccountNumber(<String>)
      .build()
  ```

  **3. Add the beneficiary detail object to the list:**

  ```kotlin
  beneficiaryDetailsList.add(beneficiaryDetails)
  ```

  **4. Repeat steps 2 and 3 for another beneficiary:**

  ```kotlin
  val beneficiaryDetails1 = PayUBeneficiaryDetail.Builder()
      .setBeneficiaryIfsc(<String>)
      .setBeneficiaryAccountNumber(<String>)
      .build()
  beneficiaryDetailsList.add(beneficiaryDetails1)
  ```

  **5. Set the list of beneficiary details in the payment parameters:**

  ```kotlin
  PayUPaymentParams.Builder()
      .setBeneficiaryDetailsList(beneficiaryDetailsList)
      .build()
  ```
</Accordion>
