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
Use [SI - Subscription Plan Integration](doc:si-subscription-plan-integration) to define the billing schedule in your system, capture customer consent, and trigger recurring debits through PayU APIs.

The following APIs are used to integrate subscription for Net Banking, Cards, and UPI. These APIs are mandatory for any merchant to go live and comply with all the standing instruction guidelines:

* **_payment** API: The Payment Consent Transaction using _payment API  is used. For integrating using various integrations, refer to:
  * [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)
  * [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)
  * [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction)

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

* **pre_debit_SI** API: The [Pre-Debit Notification API](ref:pre_debit_notification_api) section describes how to use this API to notify the customers before a recurring transaction.
* **si_transaction** API: The [Recurring Payment Transaction API](ref:recurring_payment_api) section describes how to use this API to initiate a recurring transaction for a customer.
* **mandate_revoke** API : The [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards) API allows the merchants to cancel the card mandate at bank's end. After the registration is canceled for a customer, the merchant cannot restore it, and the customer must register a fresh mandate with the merchant. For cancelling or revoking UPI mandates, refer to [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi).

## Manage Recurring Payment for Cards

The following sections describe how to cancel or modify the recurring payment for cards:

* [Check Mandate Status API](ref:check-mandate-status-api)
* [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card)
* [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards)

## Manage Recurring Payment for Net Banking

The following sections describe how to check or cancel the recurring payment for Net Banking:

* [Cancel the Recurring Payment for Net Banking](https://docs.payu.in/reference/cancel-the-recurring-payment-for-net-banking)
* [Check the Net Banking Mandate Status API](https://docs.payu.in/reference/net_banking_mandate_status_api)

## Manage Recurring Payment for UPI

The following API commands are applicable only for UPI:

* **upi_mandate_status**: Used to understand the current state of the UPI mandate at any time. For more information, refer to [Get Mandate Status API (for UPI only)](ref:get-mandate-status-api-for-upi-only).
* **upi_mandate_modify**: Used to modify an existing UPI Recurring Payment Registration. For more information, [Modify the Recurring Payment for UPI](ref:modify-the-recurring-payment-for-upi).
* **upi_mandate_revoke**: Used to cancel a UPI Recurring Payment Registration. For more information, refer to  [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi).

<Callout icon="📘" theme="info">
  **Handle Guest Checkout Transaction**: You can handle Guest Checkout transactions for EMI integration. For more information, refer to[ Cards Integration > Handling Guest Checkout Transactions](doc:collect-payments-with-cards-seamless#handling-guest-checkout-transactions).
</Callout>
