---
title: API Integration
deprecated: false
hidden: true
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
---
This part of the document includes the sections for each payment mode that provides detailed explanation to integrate Subscriptions.

* [Net Banking Integration](https://docs.payu.in/docs/net-banking-subscriptions-integration-merchant-hosted)
* [Cards Integration](https://docs.payu.in/docs/cards-subscription-integration-merchant-hosted-checkout)
* [UPI Integration](https://docs.payu.in/docs/upi-subscriptions-integration-merchant-hosted-checkout)
* [Pay and Subscribe Integration](https://docs.payu.in/docs/pay-and-subscribe-integration)

## Subscription APIs

The following APIs are used to integrate subscription for Net Banking, Cards, and UPI. These APIs are mandatory for any merchant to go live and comply with all the standing instruction guidelines:

* **_payment** API: The Payment Consent Transaction using _payment API  is used. For integrating using various integrations, refer to:
  * [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)
  * [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)
  * [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction)
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
