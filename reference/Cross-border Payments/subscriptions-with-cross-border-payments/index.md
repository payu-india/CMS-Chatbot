---
title: Subscriptions with Cross-Border Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
The Subscriptions with Cross-Border Payments involves various APIs and must be used as mentioned in the integration. For more 

### 1. Registration Consent

**Purpose**: Establish customer consent and register payment mandates for recurring transactions.

**Key Features**:

* Secure mandate registration across multiple payment methods
* Compliance with cross-border payment regulations
* Customer consent validation and authentication
* Token generation for secure recurring payments

Refer to the following sections on how to integrate Registration Consent Transaction with Cross-Border Payments:

* [PayU Hosted Integration](doc:cb-subscriptions-integration-non-seamless)
* S2S
  * [Cards Consent Transaction](https://docs.payu.in/docs/registration-consent-cards-integration-cb)
  * [UPI Consent Transaction](https://docs.payu.in/docs/upi-consent-transaction-cb)
  * [Net Banking Consent Transaction](doc:netbanking-consent-or-enach-cb)

### 2. Recurring Payment Transaction

**Purpose**: Execute automated payments based on registered mandates.

**Key Features**:

* Automatic billing cycle execution
* Multiple billing frequencies (monthly, yearly, custom intervals)
* Intelligent retry mechanisms for failed payments
* Real-time payment status notifications

<Callout icon="👍" theme="okay">
  **Reference:** For recurring payments with CB, you must pass the UDF parameters with invoice ID and customer details. For more information, refer to [Recurring Payment Transaction API - PACB](ref:recurring-payment-transaction-api-pacb).
</Callout>

### 3. Pre-Debit Notification

**Purpose**: Notify customers and validate account status before executing recurring payments.

**Key Features**:

* Customer notification system
* Account balance verification
* Compliance with regulatory pre-debit requirements
* Risk assessment and fraud prevention

<Callout icon="👍" theme="okay">
  **Reference:** For pre-debit transaction, you must use the **Pre-Debit Notification** API. For more information, refer to [Pre-Debit SI API](ref:pre-debit-si-api-parallel-sequencing)
</Callout>

##
