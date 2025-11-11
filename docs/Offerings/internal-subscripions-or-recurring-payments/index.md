---
title: '[Review]Subscripions or Recurring Payments'
deprecated: false
hidden: true
metadata:
  title: Recurring Payments Introduction
  description: >-
    Learn how to integrate recurring payments with PayU, a leading online
    payment service provider in India. Find out how to create, manage, and
    cancel subscriptions using PayU’s hosted checkout and APIs1
  keywords:
    - Recurring Payments Integration Introduction
    - PayU Subscription Management Introduction
    - Monthly Payment Processing Integration Introduction
    - PayU Recurring Payment Platform Integration
  robots: index
---
The Subscriptions, Recurring Payments or Standing Instruction (SI) from PayU to set up and manage recurring payments. These recurring payments:

* Can be charged as per a cycle defined
* Do not require any customer intervention

The customer can instruct banks for regular funds transfers through standing instructions to automatically make payments. PayU Subscriptions enable you to collect **recurring payments** automatically through Standing Instructions (SI). This feature allows your business to:

* **Automate billing cycles** without customer intervention
* **Reduce administrative overhead** for periodic payments
* **Support multiple payment modes** (Cards, Net Banking, UPI)
* **Manage subscription lifecycles** with pre-debit notifications

PayU offers Recurring Payments integration using the APIs, Zion Subscription platforms, or PayU Dashboard.

The following video describes PayU’s Recurring Payment Suite offering:

<Embed typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=5AfrrFg6CEQ" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F5AfrrFg6CEQ%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D5AfrrFg6CEQ%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F5AfrrFg6CEQ%252Fhqdefault.jpg%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" href="https://www.youtube.com/watch?v=5AfrrFg6CEQ" providerUrl="https://www.youtube.com/" providerName="YouTube" />

## Key Benefits

* **Seamless Customer Experience**: One-time setup with automatic recurring charges
* **Flexible Integration**: Choose from API, platform-based, or zero-code solutions
* **Multi-Modal Support**: Cards, Net Banking, and UPI payment instruments
* **Automated Notifications**: Pre-debit alerts and transaction confirmations

## Use cases [Review and Update]

Standing Instructions allows your customers' banks to automatically debit predetermined amounts based on predefined billing cycles. Once set up, customers don't need to manually authorize each transaction, making it perfect for:

* Subscription services (streaming, software, etc.)
* Utility bill payments
* Insurance premiums
* Loan EMIs
* Membership fees

### Some Examples

* Ashish had subscribed for Magazine subscriptions for a specific magazine on the BeSpoke Online Magazine platform. Now, he wants to get a special edition, so he can ask the BeSpoke Online Magazine platform to debit the amount without a new payment consent, but a Pre-Debit Transaction. 
* \<Example 2>

## Prerequisites

Before implementing subscriptions, ensure you have:

1. **Active PayU Merchant Account**: [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard)
2. **Subscription Feature Enabled**: Contact your PayU Key Account Manager to activate subscriptions
3. **Integration Method Selected**: Review the three available approaches. For more information, refer to (Implementation Methods)[#implementation-methods]
4. **Technical Requirements**
   * API key and Salt  and webhook endpoints (for API integration)
   * Dashboard access (for zero-code implementation)

## Considerations (Require Info)

* Time and amount-related limitations which has to considered

## How to set up

1. **Register and Activate**: Set up your PayU merchant account
2. **Choose Integration Method**: Select API, Zion Platform, or Dashboard approach. Refer to [Implementation Methods](#implementation-methods)
3. **Configure Payment Modes**: Set up Cards, Net Banking, and/or UPI
4. **Test Integration**: Validate subscription flows in sandbox environment
5. **Go Live**: Deploy with production credentials

## Implementation methods

Choose the integration approach that best fits your technical requirements and business needs:

### Zero Code Dashboard Integration

This method suits your business if you have limitation with technical resources by using any of the following methods :

* **[Create a Payment Link](doc:create-a-payment-link-with-si)**
* **[Bulk Upload Payment Links](doc:bulk-upload-of-payment-links-with-si-registration)**
* **[Bulk Recurring Payments + Notifications](doc:bulk-upload-of-payment-links-for-recurring-payments-pre-debit-notication)**

**Key Features:**

* No coding required
* CSV-based bulk operations
* Dashboard-based subscription management
* Automated link generation and sharing

### API Integration

This methods suits if you have developers who need complete control over subscription workflows:

**Features:**

* **Seamless Integration** (Merchant Hosted Checkout)
* **Non-seamless Integration** (PayU Hosted Checkout)
* Full customization of user experience
* Direct API control over all subscription operations
* Custom billing logic implementation

**Technical Requirements:**

* Server-side integration capability
* Webhook handling for payment notifications
* Custom UI/UX development

### Zion Subscription Automation Platform

This method suits enterprises looking for minimal technical effort with maximum automation.

**Features:**

* Customizable and scalable platform
* Minimal coding required
* Automated pre-debit notifications
* Automated recurring transaction processing
* Enterprise-grade subscription management
* Built-in analytics and reporting

**Advantages:**

* Faster time to market
* Pre-built subscription management features
* Automated dunning management
* Comprehensive reporting dashboard

## Payment Modes

PayU Subscriptions supports three primary payment instruments with varying capabilities:

| Payment Mode     | Supported Cards/Banks | Consent Required | Pre-debit Notifications | Instant Setup     |
| ---------------- | --------------------- | ---------------- | ----------------------- | ----------------- |
| **Credit Cards** | All major issuers     | ✅ Yes            | ✅ Available             | ✅ Yes             |
| **Debit Cards**  | Select issuers only   | ✅ Yes            | ✅ Available             | ✅ Yes             |
| **Net Banking**  | Participating banks   | ✅ Yes            | ❌ Not available         | ⚠️ Varies by bank |
| **UPI**          | All UPI-enabled apps  | ✅ Yes            | ✅ Available             | ✅ Yes             |

### Payment Mode Specific Features

#### Credit Cards

* **Full Automation**: Complete recurring payment automation
* **Pre-debit Notifications**: 24-48 hours advance notice
* **Wide Acceptance**: All major card networks supported
* **Instant Setup**: Immediate consent and activation

#### Debit Cards

* **Selective Support**: Only participating issuing banks
* **Enhanced Security**: Additional authentication layers
* **Pre-debit Alerts**: SMS/email notifications available
* **Bank-specific Rules**: Varies by issuing institution

#### Net Banking

* **Bank Integration**: Direct integration with participating banks
* **Simplified Setup**: Streamlined consent process
* **No Pre-debit Notifications**: Direct debit processing
* **Bank-dependent**: Features vary by banking partner

#### UPI

* **Universal Support**: All UPI-enabled applications
* **Modern Digital**: Contemporary payment experience
* **Real-time Notifications**: Instant payment confirmations
* **Flexible Limits**: Configurable transaction amounts

## Integration Workflows

### Cards Recurring Workflow

**Phase 1: Consent Collection**

1. **[Cards Recurring Payment Consent Transaction →](ref:credit-card-recurring-payment-consent-transaction)**
   * Initial customer consent and card tokenization
   * Subscription terms acknowledgment
   * Payment authorization setup

**Phase 2: Pre-transaction Notification**

2. **[Pre-Debit Notification API →](ref:pre_debit_notification_api)**

* 24-48 hours advance notification
* Customer can view upcoming charges
* Option to pause/modify if needed

**Phase 3: Recurring Execution**

3. **[Recurring Payment Transaction API →](ref:recurring_payment_api)**

* Automated charge processing
* Real-time transaction status
* Success/failure notifications

### Net Banking Recurring Workflow

**Phase 1: Bank Authorization**

1. **[Net Banking Recurring Payment Consent Transaction →](ref:netbanking-recurring-payment-consent-transaction)**
   * Bank-specific consent collection
   * Standing instruction setup
   * Customer authentication

**Phase 2: Recurring Execution**

2. **[Recurring Payment Transaction API →](ref:recurring_payment_api)**

* Direct bank account debit
* Transaction confirmation
* Settlement processing

### UPI Recurring Workflow

**Phase 1: UPI Mandate Setup**

1. **[UPI Recurring Payment Consent Transaction →](ref:upi-recurring-payment-consent-transaction)**
   * UPI app-based consent
   * Mandate configuration
   * Customer approval via UPI PIN

**Phase 2: Pre-transaction Notification**

2. **[Pre-Debit Notification API →](ref:pre_debit_notification_api)**

* UPI app notifications
* Transaction preview
* Modification options

**Phase 3: Recurring Execution**

3. **[Recurring Payment Transaction API →](ref:recurring_payment_api)**

* Automated UPI debit
* Real-time processing
* Instant confirmations

## 📱 Supported Platforms

| Platform                 | API Integration | Zion Platform  | Dashboard Integration | Notes                        |
| ------------------------ | --------------- | -------------- | --------------------- | ---------------------------- |
| **Web Applications**     | ✅ Full Support  | ✅ Full Support | ✅ Full Support        | Complete feature set         |
| **Mobile Apps**          | ✅ Full Support  | ✅ Full Support | ⚠️ Limited            | Dashboard via mobile browser |
| **Server-to-Server**     | ✅ Full Support  | ✅ Full Support | ❌ Not Available       | Backend integration only     |
| **E-commerce Platforms** | ✅ Full Support  | ✅ Full Support | ✅ Full Support        | Plugin/module support        |
| **Point of Sale**        | ⚠️ Limited      | ⚠️ Limited     | ❌ Not Available       | Contact support              |

### Platform-Specific Considerations

#### Web Applications

* Complete API access
* Full customization capabilities
* Responsive design support
* Cross-browser compatibility

#### Mobile Applications

* Native SDK integration
* In-app payment flows
* Platform-specific UI guidelines
* Deep linking support

#### Server-to-Server

* Backend-only processing
* Webhook-based notifications
* Automated subscription management
* No user interface components
