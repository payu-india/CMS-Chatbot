---
title: Subscriptions Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Subscriptions
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU Subscriptions Overview
  description: >-
    Learn how to integrate PayU Subscriptions to charge customers automatically on a recurring basis. 
    Set up various billing models, manage subscription lifecycles, and ensure RBI compliance.
  keywords:
    - PayU Subscriptions
    - Recurring Payments
    - Standing Instructions
    - Mandate Management
    - Pre-Debit Notification
  robots: index
---

## Overview

PayU Subscriptions allow you to charge your customers automatically on a recurring basis. With PayU Subscriptions, you can set up various billing models, manage subscription lifecycles, and ensure regulatory compliance for automated recurring payments.

## Key Features

* **Automated Recurring Billing**: Charge customers automatically based on predefined schedules
* **RBI Compliance**: Fully compliant with RBI guidelines for recurring payments
* **Smart Retry Logic**: Automatically retry failed payments with configurable schedules
* **Flexible Billing Models**: Support for fixed, variable, and usage-based billing
* **Comprehensive Webhooks**: Real-time notifications for all subscription events
* **Customer Management**: Complete customer lifecycle management with payment method tokenization

## Workflow

PayU Subscriptions offers two primary integration approaches to accommodate different business requirements and technical implementations:

### Step 1: Create a Subscription

There are two ways to create a Subscription:

#### 1.1 Non-Seamless Integration (PayU Hosted Checkout)

Customers redirect to PayU's hosted payment page for subscription setup with built-in compliance features, requiring minimal frontend development while PayU handles regulatory requirements.

For more information, refer to [PayU Hosted Integration](doc:payu-hosted-integration-subscriptions).

#### 1.2 Seamless Integration (Merchant Hosted Checkout)

Seamless integration provides greater control by embedding payment collection directly into merchant applications, supporting multiple payment instruments with specific integration patterns for enhanced customer experience.

**Different modes to integrate:**

* **UPI Integration**: Customers are redirected to their UPI app for mandate approval through intent-based flows, providing a familiar mobile-first experience. For more information, refer to [UPI Subscriptions Integration](doc:upi-subscriptions-integration-merchant-hosted-checkout).

* **Cards Integration**: Card-based subscriptions utilize redirect flows to PayU's secure tokenization interface, ensuring PCI DSS compliance and RBI tokenization requirements. For more information, refer to [Cards Subscription Integration](doc:cards-subscription-integration-merchant-hosted-checkout).

* **ENACH Integration**: Direct integration with NPCI's ENACH infrastructure enables automated mandate creation for net banking customers, supporting both physical and digital mandate workflows. For more information, refer to [Net Banking Integration](doc:net-banking-subscriptions-integration-merchant-hosted).

<Callout icon="📘" theme="info">
  **Note**: Once the authorization transaction is successful, PayU returns the `mihpayid`, `txnid`, and `hash`.
</Callout>

### Step 2: Mandate Management APIs

Before proceeding to hit pre-debit/recurring payments, check the mandate status using the following APIs:

| Payment Mode          | API Reference                                                                                                                                                                      |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Cards**             | The Check Mandate Status API enables you to understand the current state of the mandate with cards at any time. Refer to [Check Mandate Status API](ref:check-mandate-status-api). |
| **UPI Autopay**       | Used to understand the current state of the UPI mandate at any time. Refer to [Get Mandate Status API (for UPI only)](ref:get-mandate-status-api-for-upi-only).                    |
| **ENACH/Net Banking** | Check the Net Banking Mandate Status API. Refer to [Net Banking Mandate Status API](ref:net_banking_mandate_status_api).                                                           |

### Step 3: Recurring Payment Processing

After subscription creation and mandate approval, PayU provides comprehensive APIs for recurring payment lifecycle management, covering pre-debit notifications, payment processing, and mandate management across all payment methods.

<Callout icon="📘">
  **Note**: This step is common for both seamless and non-seamless integration.
</Callout>

#### Step 3.1: Pre-Debit Notification API (Card and UPI Autopay Only)

The Pre-Debit Notification API is **mandatory for RBI compliance** and must be called 24-72 hours before processing any recurring payment. This API sends notifications to customers about upcoming charges via SMS and email.

For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

#### Step 3.2: Recurring Payment Processing

This API processes the actual recurring payment after the pre-debit notification period has elapsed.

For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

#### Step 3.3: Modify or Cancel Recurring Payments

**For Cards (VISA/Mastercard):**

* [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card)
* [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards)

**For Cards (AMEX):**

* [Modify Recurring Payments for AMEX Card](ref:modify-recurring-payments-for-amex-card)
* [Cancel Recurring Payment for AMEX Card](ref:cancel-recurring-payment-for-a-amex-card)

**For ENACH/Net Banking:**

PayU's ENACH APIs enable net banking mandate status monitoring, cancellation management, and UMRN tracking for seamless recurring payment administration across participating banks.

* [Cancel the Recurring Payment for Net Banking](ref:cancel-the-recurring-payment-for-net-banking)

**For UPI:**

* [Modify the Recurring Payment for UPI](ref:modify-the-recurring-payment-for-upi)
* [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi)

## Manage Mandates

### Check Mandate Status

Before proceeding to hit pre-debit/recurring payments, check the mandate status:

| Payment Mode | API                                                                              |
| ------------ | -------------------------------------------------------------------------------- |
| Cards        | [Check Mandate Status API](ref:check-mandate-status-api)                         |
| UPI Autopay  | [Get Mandate Status API (for UPI only)](ref:get-mandate-status-api-for-upi-only) |
| ENACH        | [Net Banking Mandate Status API](ref:net_banking_mandate_status_api)             |

### Additional Mandate Management APIs

* **Validate VPA API**: Use this API to validate if a VPA supports recurring payments before initiating a UPI mandate. Refer to [Validate VPA API](ref:validate_vpa_api).

## Customization and Advanced Features

### Pay and Subscribe Flow (SI=4)

The Pay and Subscribe flow allows merchants to collect an initial payment along with subscription setup in a single transaction. By setting the `si` parameter to `4`, customers can make an immediate purchase while simultaneously authorizing future recurring payments, streamlining the onboarding process for subscription services.

For more information, refer to [Pay and Subscribe Consent Transaction](ref:pay-and-subscribe-consent-transaction).

### Third Party Validation (TPV) Flow

TPV flow enables additional validation layers for high-value subscriptions or regulated industries. This feature allows merchants to implement custom validation rules, fraud checks, or compliance requirements before finalizing subscription creation, ensuring adherence to specific business or regulatory standards.

For more information, refer to [Introduction to PayU TPV](doc:introduction-to-payu-tpv).

### Direct ENACH Integration

For enterprises requiring deeper control over the mandate lifecycle, direct ENACH integration bypasses standard redirect flows. This approach enables merchants to handle mandate creation, modification, and cancellation through direct API calls to NPCI infrastructure, providing complete control over the customer journey while maintaining regulatory compliance.

For more information, refer to [Net Banking Recurring Payment Consent Transaction](ref:netbanking-recurring-payment-consent-transaction).
