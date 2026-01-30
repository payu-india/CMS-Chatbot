---
title: Capacitor UPI Bolt Mobile SDKs
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
**PayU UPI Bolt SDK** aims to streamline and enhance the merchants' payment process by:

1. Providing a seamless in-app payment experience without any third-party redirection.
2. Achieving a higher success rate, reducing customer drop-offs during payments.
3. Offering features for profile management, including managing user accounts and balances.
4. Improving the overall customer experience and supporting merchants in retaining their customers.

This part of the document includes the following SDK integrations:

* [UPI Bolt UI SDK Integration - Ionic](doc:upi-bolt-ui-sdk-integration-ionic)
* [UPI Bolt Capacitor-Ionic-Angular SDK Integration](doc:upi-bolt-capacitor-ionic-angular-sdk-integration)

## Advantages

The PayU UPI Bolt SDK offers the following benefits:

1. **One-click checkout**: Customers can avoid the hassle of redirection to third-party UPI apps.
2. **Faster transactions**: With direct bank integrations, transaction speeds improve.
3. **Improved user experience**: The entire process occurs within the merchant's app.
4. **Ease of integration**: Quick setup, leveraging existing customer profiles maintained by banks.
5. **Higher success rate**: A **5-6%** improvement in transaction success fosters better conversion rates.
6. **Behavior analytics**: Merchants gain insights into customer behavior and a complete user funnel.

# User Journeys in PayU UPI Bolt

### Registration and Pay

1. Merchants can perform user registration for new customers during checkout or as a separate flow.
2. Customers need to provide SMS permissions for SIM card verification (e.g., selecting a SIM on dual-SIM phones).
3. Following SIM/device verification:
   * A UPI ID is created.
   * The user completes a **bank account selection** and addition process with accounts linked to their verified mobile number.
   * If using an account for the first time, the customer sets an **MPIN**.
4. Transactions can be initiated once the bank account setup is complete.

<Image align="center" src="https://files.readme.io/c740dd57eb78f4c21a5ef065ec08a5a2575ad41b150e121416283965d3fef62b-ionic_react_sdk_integration_mobile_workflow1.jpeg" />

### Payment

1. Already registered users can make **one-click payments**.
2. Customers select a pre-added bank account, input their MPIN, and complete their transaction.
3. Optionally, customers can check their account balance before proceeding, avoiding potential low-balance failures.

<Image align="center" src="https://files.readme.io/da1e82d9ee03c1cd3da73c90abb0c399f2282b228a45d22a0a73353259be2803-ionic_react_sdk_integration_mobile_workflow2.jpeg" />

## Profile Management Journey

1. Customers can:
   * Add or remove bank accounts.
   * Manage MPINs (set, change, reset).
   * Check balances for linked accounts.
2. View transaction history and raise/query disputes.
3. Access a **dispute history** for tracking raised disputes.
4. De-register all their linked accounts from the PayU UPI Bolt SDK.

<Image align="center" src="https://files.readme.io/e635461aee9e9ee406ad9d9a48877a73c4aea51255cab4047e114e5c3081fd1c-ionic_react_sdk_integration_mobile_workflow3.jpeg" />

##