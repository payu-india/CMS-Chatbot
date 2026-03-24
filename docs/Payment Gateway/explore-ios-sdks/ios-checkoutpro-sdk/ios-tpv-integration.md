---
title: TPV Integration - iOS
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
title: TPV Integration - iOS
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

**Steps to Integrate**

<Cards columns={4}>
  <Card title="1. Include SDK" href="#step-1-include-the-sdk-in-your-app-buildgradle">
    Add SDK dependency to app.build.gradle

    <br />
  </Card>

  <Card title="2. Update build.gradle" href="#step-2-update-root-level-buildgradleonly-for-alpha-version">
    Update root level build.gradle for alpha

    <br />
  </Card>

  <Card title="3. TPV Changes" href="#step-3-tpv-integration-changes">
    Set up beneficiary details and payment params

    <br />
  </Card>

  <Card title="4. Pod File" href="#step-4-changes-for-pod-file">
    Update pod file with SDK version
  </Card>

  <br />
</Cards>

<Accordion title="Payment Modes Supported" icon="fa-credit-card">
  * Net-banking
  * UPI
</Accordion>

## Step 1: Include the SDK in your app build.gradle

Add the following line in the app.build.grade:

<Accordion title="Gradle dependency" icon="fa-code">
  ```gradle
  implementation 'in.payu:payu-checkout-pro:2.4.8-alpha1
  ```
</Accordion>

## Step 2: Update root level build.gradle(only for alpha version)

Update root level in the build.gradle (for alpha version only):

<Accordion title="Root level build.gradle configuration" icon="fa-code">
  ```gradle
  allprojects {    repositories {        maven {url  "<https://oss.sonatype.org/content/groups/staging/"}>    } }\`
  ```
</Accordion>

## Step 3: TPV Integration changes

The step is to perform the following:

* **Beneficiary Details**: The code sets up the details of beneficiaries (such as their IFSC code and account number) who will receive payments.
* **Payment Parameters**: These details are then added to the payment parameters, which are used to configure the payment request.\
  This setup is essential for ensuring that the payment gateway knows where to direct the funds during a transaction.

<Accordion title="TPV integration code samples" icon="fa-code">
  To include TPV integration changes:

  1. Create a list to hold beneficiary details:
     ```swift
     var payuBeneficieryDetailsList = PayUBeneficiaryParams
     ```
  2. Create beneficiary detail objects with IFSC and account number:
     ```swift
     let beneficiaryDetails1 = PayUBeneficiaryParams(beneficiaryAccountNumber: <String>,
                                                     beneficiaryIFSC: <String>)
     let beneficiaryDetails2 = PayUBeneficiaryParams(beneficiaryAccountNumber: <String>,
                                                     beneficiaryIFSC: <String>)
     ```
  3. Add the beneficiary detail objects to the list:
     ```swift
     payuBeneficieryDetailsList.append(beneficiaryDetails1)
     payuBeneficieryDetailsList.append(beneficiaryDetails2)
     ```
  4. Set up the payment parameters with necessary details:
     ```swift
     let paymentParam = PayUPaymentParam(key: <String>,
                                         transactionId: <String>,
                                         amount: <String>,
                                         productInfo: <String>,
                                         firstName: <String>,
                                         email: <String>,
                                         phone: <String>,
                                         surl: <String>, // Pass your own surl
                                         furl: <String>, // Pass your own furl
                                         environment: <Environment> /* .production or .test */)
     ```
  5. Assign the list of beneficiary details to the payment parameters:
     ```swift
     paymentParam.payuBeneficieryDetails = payuBeneficieryDetailsList
     ```
</Accordion>

## Step 4: Changes for pod file

Include the following lines for iOS pod file to indicate PayU Checkout Pro SDK version dependency:

<Accordion title="Pod file configuration" icon="fa-code">
  ```ruby
  pod 'PayUIndia-CheckoutPro', '8.3.0-alpha.1'
  ```
</Accordion>
