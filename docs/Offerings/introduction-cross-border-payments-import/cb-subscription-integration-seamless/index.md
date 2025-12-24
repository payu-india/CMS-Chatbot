---
title: Subscriptions with Merchant Hosted Integration - CB
deprecated: false
hidden: true
metadata:
  robots: index
---
CB (Cross-Border) Subscription integration enables you to set up automated recurring payment systems for international customers. This comprehensive solution supports multiple payment methods including Cards, UPI, and Net Banking, allowing businesses to streamline their subscription billing processes while maintaining compliance with cross-border payment regulations.

## Transaction Flow Components

The CB Subscription integration consists of three main components:

### 1. Registration Consent

**Purpose**: Establish customer consent and register payment mandates for recurring transactions.

**Key Features**:

* Secure mandate registration across multiple payment methods
* Compliance with cross-border payment regulations
* Customer consent validation and authentication
* Token generation for secure recurring payments

### 2. Recurring Payment Transaction

**Purpose**: Execute automated payments based on registered mandates.

**Key Features**:

* Automatic billing cycle execution
* Multiple billing frequencies (monthly, yearly, custom intervals)
* Intelligent retry mechanisms for failed payments
* Real-time payment status notifications

<Callout icon="👍">
  **Reference:** For recurring payments with CB, you must pass the UDF parameters with invoice ID and customer details. For more information, refer to [Recurring Payment Transaction API - PACB](ref:recurring-payment-transaction-api-pacb).
</Callout>

### 3. Pre-Debit Notification

**Purpose**: Notify customers and validate account status before executing recurring payments.

**Key Features**:

* Customer notification system
* Account balance verification
* Compliance with regulatory pre-debit requirements
* Risk assessment and fraud prevention

<Callout icon="👍">
  **Reference:** For pre-debit transaction, you must use the **Pre-Debit Notification** API. For more information, refer to [Pre-Debit SI API](ref:pre-debit-si-api-parallel-sequencing)
</Callout>

## Payment Method Support

### 💳 Cards (Credit/Debit)

* **Registration**: Secure card tokenization with consent
* **Compliance**: PAN validation, mandate limits
* **Benefits**: Wide acceptance, instant processing
* **Use Cases**: International subscriptions, premium services

**Key Parameters**:

* Card details (number, expiry, CVV, holder name)
* Standing Instruction (SI) details
* Cross-border compliance fields (PAN, DOB, merchant entity)

### 📱 UPI (Unified Payments Interface)

* **Registration**: UPI mandate with customer approval
* **Flows**: Collect and Intent workflows
* **Benefits**: Cost-effective, real-time processing
* **Use Cases**: Domestic subscriptions, micro-payments

**Key Parameters**:

* VPA (for Collect flow)
* SI mandate details
* Billing cycle configuration
* Customer authentication

### 🏦 Net Banking (eNACH)

* **Registration**: Electronic mandate registration
* **Compliance**: Bank-specific validation
* **Benefits**: Direct bank account access, lower processing fees
* **Use Cases**: Large-value subscriptions, enterprise billing

**Key Parameters**:

* Bank code selection
* Mandate details with billing schedule
* Customer bank account validation
* Secure hash authentication

## API Endpoints Summary

| Function             | Endpoint          |
| -------------------- | ----------------- |
| Registration Consent | `/payment`        |
| Recurring Payment    | `/payment`        |
| Transaction Status   | `/verify_payment` |
| Mandate Management   | `/manage_mandate` |

This part of the documentation includes the following sections on how to integrate Registration Consent Transaction with Cross-Border Payments:

* [Cards Consent Transaction](https://docs.payu.in/docs/registration-consent-cards-integration-cb)
* [UPI Consent Transaction](https://docs.payu.in/docs/upi-consent-transaction-cb)
* [Net Banking Consent Transaction](doc:netbanking-consent-or-enach-cb)

<br />
