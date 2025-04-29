---
title: Android UPI SDK
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Android UPI SDK
  description: >-
    This document provides information on UPI transactions, including Collect
    and Intent transactions, VPA verification, and compatibility requirements
    such as SDK versions and Kotlin version.
  keywords:
    - PayU India UPI SDK
    - PayU UPI SDK
    - UPI SDK integration Android
    - Android UPI payment SDK
    - PayU UPI payment gateway
    - How to integrate PayU UPI SDK in Android
    - PayU India UPI SDK for Android apps
    - Guide to PayU UPI Android SDK
    - PayU UPI payment gateway integration Android
    - Step-by-step PayU UPI SDK Android integration
  robots: index
next:
  description: ''
---
UPI SDK supports collect, intent and in app flows for accepting UPI payments through major acquirers. It seamlessly integrates into merchant apps providing various features for UPI.

## Features

* Collect, Intent and In App experience
* VPA verification
* Generic Intent(All UPI apps populated) or Smart Intent( Check if user is enrolled in UPI app)
* Addons ( GPay SDK and Phonepe In-App SDK)

This cluster aims to document all the knowledge base for UPI transactions. Implementation of most of the UPI flows is different when compared to normal transactions.

There are broadly two types of UPI transactions, **Collect and Intent(Pure Intent/In-App)**. 

For collect transactions, PayU informs the payment gateway to trigger a transaction to the app linked to the provided VPA, which asks the user for approval.

For intent transactions, we delegate the transaction process to an external app like BHIM, Google Pay, etc, which lets users transfer money to a VPA specified by us. After that, we use the PG (related to the specified VPA) for verification. PayU has a pre-configured VPA (distinct on the PG-Merchant level) on which the app makes the user to pay the amount.

Implementation details of the following are documented separately, and available at the same location as this document.​

* VPA validation
* Collect
* Payment Verification
* Generic Intent
* Google Pay
* PhonePe

## Compatibility

* Min SDK Version: 21
* Compile SDK Version: 31 and above
* Kotlin version: 1.6.10
