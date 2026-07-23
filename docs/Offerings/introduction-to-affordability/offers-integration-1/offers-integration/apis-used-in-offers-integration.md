---
title: APIs used in Offers Integration
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used in Offers Integration
  robots: index
---
---
title: Using API Integration
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Recurring Payments Using API Integration
  description: >-
    Learn how to use various PayU’s API to create and manage recurring payments
    for your online business. Find out how to set up subscription plans, capture
    customer consent, and handle notifications.
  keywords:
    - APIs for Recurring Payments Integration
    - APIs for Subscriptions Integration
    - APIs for Autopay Integration
    - APIs for Scheduled Payment Integration Integration
  robots: index
next:
  description: ''
---
The following APIs support recurring-payment consent, charging, and mandate management for Cards, Net Banking, and UPI.

### Consent and recurring payment lifecycle

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted) | `POST /_payment` | Register a customer's recurring-payment consent through PayU Hosted Checkout. |
| [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted) | `POST /_payment` | Register a customer's recurring-payment consent through a merchant-hosted Cards, Net Banking, or UPI checkout. |
| [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction) | `POST /_payment` | Register a UPI recurring-payment mandate through Merchant Hosted Checkout. |
| [Pre-Debit Notification API](ref:pre_debit_notification_api) | `pre_debit_SI` | Notify the customer at least 48 hours before an upcoming recurring debit. |
| [Recurring Payment Transaction API](ref:recurring_payment_api) | `si_transaction` | Charge a successfully registered Cards, Net Banking, or UPI mandate through the recurring interface. |
| [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards) | `mandate_revoke` | Revoke a card mandate so that it can no longer be used for recurring payments. |
| [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi) | `upi_mandate_revoke` | Revoke a UPI mandate so that it can no longer be used for recurring payments. |

<Callout icon="👍" theme="okay">
  Experience the end-to-end **PayU Hosted > Subscriptions** flow and instantly generate the complete code for seamless, zero-coding integration into your website.

  <HTMLBlock>{`
                    <style>
                    .tooltip-btn {
                        position: relative;
                        background-color: #4CAF50;
                        color: white;
                        padding: 10px 20px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        font-weight: bold; /* Added this line */
                    }
                    .tooltip-btn:hover::after {
                        content: attr(data-tooltip);
                        position: absolute;
                        bottom: 125%;
                        left: 50%;
                        transform: translateX(-50%);
                        background-color: #333;
                        color: white;
                        padding: 5px 10px;
                        border-radius: 4px;
                        white-space: nowrap;
                        font-size: 12px;
                        z-index: 1;
                    }
                    </style>

                    <button onclick="window.open('https://payu.in/integrationlab/subscription', '_blank')" 
                            class="tooltip-btn" 
                            data-tooltip="Automatically generate code including hashing for your eCommerce website to integrate Subscriptions - PayU Hosted Checkout with zero coding knowledge.">
                        Experience the flow and get the code
                    </button>
  `}</HTMLBlock>
</Callout>

After a registration is canceled for a customer, the merchant cannot restore it, and the customer must register a fresh mandate with the merchant.

### Manage Recurring Payment for Cards

The following sections describe how to cancel or modify the recurring payment for cards:

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [Check Mandate Status API](ref:check-mandate-status-api) | `check_mandate_status` | Retrieve the current state of a card mandate. |
| [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card) | `POST /_payment` | Update the billing details for an existing Visa or Mastercard recurring-payment mandate after customer authentication. |
| [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards) | `mandate_revoke` | Revoke a card mandate so that the customer must register a new mandate to resume recurring payments. |

### Manage Recurring Payment for Net Banking

The following sections describe how to check or cancel the recurring payment for Net Banking:

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [Cancel the Recurring Payment for Net Banking](https://docs.payu.in/reference/cancel-the-recurring-payment-for-net-banking) | `mandate_revoke` | Revoke a Net Banking mandate so that it can no longer be used for recurring payments. |
| [Check the Net Banking Mandate Status API](https://docs.payu.in/reference/net_banking_mandate_status_api) | `NB_mandate_status` | Retrieve the current state of an e-NACH mandate. |

### Manage Recurring Payment for UPI

The following API commands are applicable only for UPI:

| Use case → Reference | `command` / primary value | Description |
| --- | --- | --- |
| [Get Mandate Status API (for UPI only)](ref:get-mandate-status-api-for-upi-only) | `upi_mandate_status` | Retrieve the current state of a UPI mandate, including mandates paused outside the merchant's system. |
| [Modify the Recurring Payment for UPI](ref:modify-the-recurring-payment-for-upi) | `upi_mandate_modify` | Modify an existing UPI recurring-payment registration. |
| [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi) | `upi_mandate_revoke` | Revoke an existing UPI recurring-payment registration. |

<Callout icon="📘" theme="info">
  **Handle Guest Checkout Transaction**: You can handle Guest Checkout transactions for EMI integration. For more information, refer to[ Cards Integration > Handling Guest Checkout Transactions](doc:collect-payments-with-cards-seamless#handling-guest-checkout-transactions).
</Callout>
