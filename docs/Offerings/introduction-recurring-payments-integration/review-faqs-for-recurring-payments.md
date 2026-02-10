---
title: '[Review] FAQs for Recurring Payments'
deprecated: false
hidden: false
metadata:
  robots: index
---
<br />

<br />

## Pre-Debit Notification API

* **What is the Pre-Debit Notification API and why is it mandatory?**

  The Pre-Debit Notification API is used to notify customers before a recurring transaction is debited from their account. It is mandatory for Cards and UPI recurring payments as per RBI guidelines. For Cards, you must send the pre-debit notification at least 24 hours before the recurring charge transaction. For UPI, the pre-debit notification must be sent at least 24 hours prior to the actual debit. If the pre-debit notification is not sent successfully, the recurring transaction will fail. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

* **How far in advance can I send a pre-debit notification?**

  For UPI Autopay, pre-debit notifications can be sent for a maximum of 30 days in advance. The debit date cannot exceed 30 days from the date of sending the pre-debit notification. For Cards, you must send the pre-debit notification at least 24 hours before the recurring charge transaction. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

* **What happens if I don't send a pre-debit notification before a recurring transaction?**

  If you don't send a pre-debit notification before a recurring transaction for Cards or UPI, the recurring transaction will fail. Pre-debit notification is mandatory for Cards and UPI recurring payments as per RBI guidelines. For Net Banking, pre-debit notification is not required. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

* **Can I send multiple pre-debit notifications for different sequence numbers simultaneously?**

  Yes, you can use Parallel Sequencing for UPI Autopay to send pre-debit notifications for different sequence numbers simultaneously. This allows you to run pre-debits and executions in parallel for different sequence numbers. To enable Parallel Sequencing, contact your PayU Account Manager (KAM). For more information, refer to [Integrate Parallel Sequencing for UPI AutoPay](doc:integrate-parallel-sequencing-for-upi-autopay).

* **What should I do if I receive an error that pre-debit notification was already sent for a sequence?**

  If you receive an error indicating that a pre-debit notification was already sent for a sequence number, you cannot send another pre-debit notification for the same sequence. You should proceed with the recurring payment transaction using the Recurring Payment Transaction API. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

***

### Recurring Payment Transaction API

* **How do I initiate a recurring payment transaction after registration?**

  After a successful registration (consent transaction), you can initiate recurring payment transactions using the **Recurring Payment Transaction API** (si_transaction). You need to pass the unique PayU ID (mihpayid) received in the response to the registration transaction. For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

* **What is the difference between registration transaction and recurring payment transaction?**

  * **Registration Transaction (Consent Transaction)**: This is the first transaction where the customer provides consent and payment details are stored. This transaction requires customer authentication (OTP/2FA) and establishes the mandate.

  * **Recurring Payment Transaction**: These are subsequent transactions that debit the customer's account based on the established mandate. These transactions do not require customer intervention or authentication.

  For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

* **Can I change the amount for recurring payment transactions?**

  The amount for recurring payment transactions should match the billing details (amount, frequency) that were presented to the customer during registration. For Cards, you can modify the mandate using the **Update SI API** to change the amount or other details. For UPI, you can use the **upi_mandate_modify** command to modify the mandate. For more information, refer to [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card) or [Modify the Recurring Payment for UPI](ref:modify-the-recurring-payment-for-upi).

* **What happens if a recurring payment transaction fails?**

  If a recurring payment transaction fails, you should:

  1. Check the transaction status using the Verify Payment API
  2. Review the error code and error message in the response
  3. For Cards: The transaction may fail due to insufficient funds, card expiry, or mandate cancellation
  4. For UPI: The transaction may fail due to insufficient funds, mandate cancellation, or bank issues
  5. You may need to notify the customer and request them to update their payment method or mandate

  For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

* **How do I know if a recurring payment transaction was successful?**

  You can check the transaction status using the Verify Payment API or by checking the response from the Recurring Payment Transaction API. For UPI recurring payments, the response is typically returned as "Pending" initially since payment processing is asynchronous. You should use webhooks or polling to get the final transaction status. For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

***

## Mandate Management

* **How do I check the status of a mandate?**

  You can check the mandate status using the following APIs:

  * **For Cards**: Use the [Check Mandate Status API](ref:check-mandate-status-api)
  * **For Net Banking**: Use the [Check the Net Banking Mandate Status API](ref:net_banking_mandate_status_api)
  * **For UPI**: Use the [Get Mandate Status API (for UPI only)](ref:get-mandate-status-api-for-upi-only) with the `upi_mandate_status` command

  For more information, refer to the respective API documentation.

* **Can I modify an existing mandate after it's been created?**

  Yes, you can modify existing mandates:

  * **For Cards**: Use the [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card) API (Update SI API)
  * **For UPI**: Use the [Modify the Recurring Payment for UPI](ref:modify-the-recurring-payment-for-upi) API with the `upi_mandate_modify` command
  * **For International Cards**: Modification is allowed and requires authentication

  Note that for International Cards, authentication is required for mandate modification. For more information, refer to the respective API documentation.

* **How do I cancel or revoke a mandate?**

  You can cancel or revoke mandates using the following APIs:

  * **For Cards**: Use the [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards) API with the `mandate_revoke` command
  * **For Net Banking**: Use the [Cancel the Recurring Payment for Net Banking](ref:cancel-the-recurring-payment-for-net-banking) API
  * **For UPI**: Use the [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi) API with the `upi_mandate_revoke` command

  **Important**: After a mandate is canceled, you cannot restore it. The customer must register a fresh mandate if they want to continue with recurring payments. For more information, refer to the respective API documentation.

* **What happens to recurring transactions if I cancel a mandate?**

  Once a mandate is canceled, no further recurring transactions can be processed using that mandate. Any pending or scheduled recurring transactions may fail. You should notify customers before canceling their mandate and provide them with options to update their payment method or register a new mandate. For more information, refer to [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards).

* **Can I reactivate a canceled mandate?**

  No, you cannot reactivate a canceled mandate. Once a mandate is canceled, it cannot be restored. The customer must register a fresh mandate if they want to continue with recurring payments. For more information, refer to [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards).

* **What is the difference between an active and inactive mandate?**

  * **Active Mandate**: An active mandate allows recurring payment transactions to be processed. The mandate is in a state where it can be used for debiting the customer's account.

  * **Inactive Mandate**: An inactive mandate cannot be used for recurring payment transactions. Recurring payments cannot be performed if the mandate is inactive. You may need to check the mandate status and take appropriate action to activate it or create a new mandate.

  For more information, refer to [Check Mandate Status API](ref:check-mandate-status-api).

***

### Zion Subscription Automation Platform

* **What is Zion Subscription Automation Platform and how is it different from regular Recurring Payments?**

  Zion is PayU's subscription automation platform that automates the entire recurring payment lifecycle. With Zion, you only need to call the Consent transaction, and PayU takes care of the rest (pre-debit notifications, recurring charges, invoice generation). In contrast, regular Recurring Payments require you to manually call Pre-Debit Notification API and Recurring Payment Transaction API for each recurring charge. Zion provides a complete billing automation solution with subscription management, invoice generation, and automated charging. For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform).

* **How do I activate Zion platform for my account?**

  To activate the Zion platform, contact your PayU Account Manager (KAM). They will enable Zion for your merchant account and provide you with the necessary credentials and documentation. For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform).

* **What are the building blocks of Zion?**

  Zion consists of three main building blocks:

  1. **Subscription**: Allows merchants to define tailored subscription experiences with billing plans and preferred payment instruments
  2. **Consent Flow**: The only way to generate `authRefId`, which represents the customer's preferred payment instrument
  3. **Invoices**: Automatically generated on scheduled billing cycles to charge customers without intervention

  For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform).

* **How does billing work with Zion?**

  After a consent transaction occurs where the customer signs up and the merchant gets one-time authentication, Standing Instructions allow recurring charges without further customer approval. The merchant defines subscriptions, and Zion automatically generates invoices per the subscription plans, notifying the merchant through webhooks. For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform).

* **What payment methods does Zion support?**

  Zion supports the following payment methods for subscriptions:

  * Credit Cards
  * Debit Cards
  * UPI Autopay
  * Net Banking (eNACH)

  For more information, refer to [Supported Payment Instruments by Zion](doc:supported-payment-instruments-by-zion).

* **Can I use Zion for free trials and one-time payments?**

  Yes, Zion's billing automation can handle complex cases including free trials, one-time payments, fixed payments, add-on charges, usage-based payments, and delayed payments. All of this can be managed with simple REST APIs. For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform).

* **How do subscriptions start and end with Zion?**

  The merchant initiates a subscription using the Zion APIs. Subscriptions automatically end after all invoices related to the included plans are processed. Merchants can also allow customers to actively end subscriptions via their website/portal. For more information, refer to [Using Zion Subscription Automation](doc:using-zion-subscription-automation-platform).

***

## Subscription Dashboard

* **What can I do with the Subscription Dashboard?**

  The Subscription Dashboard allows you to:

  * Create subscription payment links
  * Upload subscription registration transactions in bulk
  * Upload recurring transactions in bulk
  * Manage subscription payment links
  * Manage bulk upload transactions
  * Access subscription mandates

  For more information, refer to [Subscriptions Dashboard](doc:subscription-dashboard).

* **How do I create a subscription payment link using the Dashboard?**

  You can create a subscription payment link directly from the PayU Dashboard. Navigate to the Subscriptions section and follow the steps to create a payment link with subscription details. For more information, refer to [Create a Subscription Payment Link using Dashboard](doc:create-a-subscription-payment-link-using-dashboard).

* **Can I upload registration transactions in bulk?**

  Yes, you can upload registration transactions in bulk using an Excel file through the Subscription Dashboard. This allows you to register multiple customers for recurring payments at once. For more information, refer to [Upload Registration Transactions in Bulk](doc:upload-registration-transactions-in-bulk).

* **Can I upload recurring transactions in bulk?**

  Yes, you can upload recurring transactions in bulk using an Excel file through the Subscription Dashboard. For Cards and UPI, you can use the "Recurring + Pre-Debit" option to upload both pre-debit notifications and recurring transactions together. For more information, refer to [Upload Recurring Transactions in Bulk](doc:upload-recurring-transactions-in-bulk).

* **How do I manage subscription payment links created through the Dashboard?**

  You can manage subscription payment links by accessing them through the Subscription Dashboard. You can view, update, or delete payment links as needed. For more information, refer to [Manage Subscription Payment Links](doc:manage-subscription-payment-links).

* **How do I access subscription mandates through the Dashboard?**

  You can access subscription mandates through the Subscription Dashboard to view mandate details, status, and history. For more information, refer to [Access Subscription Mandates](doc:access-subscription-mandates).

***

### Payment Links with SI

* **Can I create payment links with Standing Instructions (SI)?**

  Yes, you can create payment links that include Standing Instructions for recurring payments. This allows customers to register for recurring payments through a payment link. For more information, refer to [Create a Payment Link with SI](doc:create-a-payment-link-with-si).

* **How do payment links with SI work?**

  When a customer clicks on a payment link with SI, they can complete the registration transaction (consent transaction) through the payment link. After successful registration, the mandate is established, and you can process recurring payments using the Recurring Payment Transaction API. For more information, refer to [Create a Payment Link with SI](doc:create-a-payment-link-with-si).

***

### Customer Experience and Workflow

* **What is the customer experience for Cards recurring payments?**

  For Cards recurring payments:

  1. Customer completes shopping and initiates a transaction with card credentials
  2. Customer enters CVV and proceeds with payment
  3. Customer goes through 2FA (OTP/3D Secure) authentication
  4. Customer provides consent for Standing Instructions
  5. Registration transaction is completed
  6. For subsequent transactions, customer receives pre-debit notification and payment is processed automatically

  For more information, refer to [Recurring Payments Experience for Cards](doc:recurring-payments-experience-for-cards).

* **What is the customer experience for UPI recurring payments?**

  For UPI recurring payments:

  1. Customer selects UPI as payment method
  2. Customer enters preferred VPA handle
  3. Customer approves the registration request by entering MPIN in their PSP app
  4. Registration transaction is completed
  5. For subsequent transactions, customer receives pre-debit notification and payment is processed automatically

  For more information, refer to [UPI Recurring Payment Experience for UPI](doc:upi-recurring-payment-experience-for-upi).

* **What is the customer experience for Net Banking recurring payments?**

  For Net Banking recurring payments:

  1. Customer selects Net Banking as payment method
  2. Customer completes Net Banking or Debit Card authentication
  3. Registration transaction is completed
  4. For subsequent transactions, payment is processed automatically (no pre-debit notification required)

  For more information, refer to [Net Banking Experience](doc:net-banking-experience).

* **What is the "Pay and Subscribe" mandate experience?**

  The "Pay and Subscribe" mandate experience allows customers to make an immediate payment while also registering for recurring payments in a single transaction. This provides a seamless experience where customers can pay for the first billing cycle and set up automatic payments for future cycles at the same time. For more information, refer to [Pay and Subscribe Mandate Experience](doc:pay-and-subscribe-mandate-experience).

***

### Parallel Sequencing for UPI Autopay

* **What is Parallel Sequencing for UPI Autopay?**

  Parallel Sequencing allows you to run pre-debits and executions simultaneously for different sequence numbers in UPI Autopay. This enables you to process multiple recurring transactions in parallel, improving efficiency and reducing processing time. For more information, refer to [Integrate Parallel Sequencing for UPI AutoPay](doc:integrate-parallel-sequencing-for-upi-autopay).

* **How do I enable Parallel Sequencing for UPI Autopay?**

  To enable Parallel Sequencing for UPI Autopay, contact your PayU Account Manager (KAM). They will enable this feature for your merchant account. For more information, refer to [Integrate Parallel Sequencing for UPI AutoPay](doc:integrate-parallel-sequencing-for-upi-autopay).

* **How does Parallel Sequencing work?**

  With Parallel Sequencing, you can:

  1. Send pre-debit notifications for different sequence numbers simultaneously
  2. Execute recurring transactions for different sequence numbers in parallel
  3. Use the `mandateSeqNo` parameter to specify the sequence number for each pre-debit and recurring transaction

  This allows you to process multiple recurring transactions more efficiently. For more information, refer to [Integrate Parallel Sequencing for UPI AutoPay](doc:integrate-parallel-sequencing-for-upi-autopay).

***

## API Integration

* **What APIs do I need to integrate for recurring payments?**

  The following APIs are mandatory for recurring payments integration:

  * **_payment API**: For Payment Consent Transaction (registration)
  * **pre_debit_SI API**: For Pre-Debit Notification (mandatory for Cards and UPI)
  * **si_transaction API**: For Recurring Payment Transaction
  * **mandate_revoke API**: For canceling mandates (optional)
  * **Update SI API**: For modifying mandates (optional)
  * **Check Mandate Status API**: For checking mandate status (optional)

  For more information, refer to [Using API Integration](doc:using-api-integration-recurring-payments).

* **Do I need separate APIs for Cards, Net Banking, and UPI?**

  No, you use the same set of APIs for different payment modes. The **_payment** API is used for all payment modes for registration. The Recurring Payment Transaction API (si_transaction) is used for all payment modes for subsequent transactions. However, some APIs are specific to certain payment modes:

  * Pre-Debit Notification is required only for Cards and UPI
  * UPI-specific commands: `upi_mandate_status`, `upi_mandate_modify`, `upi_mandate_revoke`

  For more information, refer to [Using API Integration](doc:using-api-integration-recurring-payments).

* **What is the difference between PayU Hosted Checkout and Merchant Hosted Checkout for recurring payments?**

  * **PayU Hosted Checkout**: The customer is redirected to PayU's payment page for registration. PayU handles the payment page and customer interaction.

  * **Merchant Hosted Checkout**: The customer enters payment details on your website, and you collect the details before sending them to PayU. This requires PCI-DSS compliance.

  Both methods use the same APIs for recurring payments. The difference is in how the registration transaction is initiated. For more information, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted) and [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted).

***

### Bulk Upload Operations

* **Can I upload registration transactions in bulk?**

  Yes, you can upload registration transactions in bulk using an Excel file through the Subscription Dashboard. This allows you to register multiple customers for recurring payments at once without making individual API calls. For more information, refer to [Upload Registration Transactions in Bulk](doc:upload-registration-transactions-in-bulk).

* **Can I upload recurring transactions in bulk?**

  Yes, you can upload recurring transactions in bulk using an Excel file through the Subscription Dashboard. For Cards and UPI, you can use the "Recurring + Pre-Debit" option to upload both pre-debit notifications and recurring transactions together in a single file. For more information, refer to [Upload Recurring Transactions in Bulk](doc:upload-recurring-transactions-in-bulk).

* **What is the format for bulk upload files?**

  The bulk upload files should be in Excel format (.xlsx). The file should contain specific columns with customer and transaction details. Refer to the bulk upload documentation for the exact format and required columns. For more information, refer to [Upload Registration Transactions in Bulk](doc:upload-registration-transactions-in-bulk) and [Upload Recurring Transactions in Bulk](doc:upload-recurring-transactions-in-bulk).

* **How do I manage bulk upload transactions?**

  You can manage bulk upload transactions through the Subscription Dashboard. You can view the status of bulk uploads, check for errors, and retry failed transactions. For more information, refer to [Manage Bulk Upload Transactions](doc:manage-subscription-bulk-upload-transactions).

***

## Error Handling and Troubleshooting

* **What should I do if a registration transaction fails?**

  If a registration transaction fails:

  1. Check the error code and error message in the response
  2. Common reasons for failure include:
     * Card not supported for recurring payments
     * Authentication failure (OTP/2FA)
     * Invalid payment details
     * Insufficient funds (for immediate charge)
  3. Display appropriate error messages to the customer
  4. Allow the customer to retry with different payment details

  For more information, refer to [Customer Experience and Workflow - Recurring Payments](doc:customer-experience-and-workflow-recurring-payments).

* **What should I do if a recurring payment transaction fails?**

  If a recurring payment transaction fails:

  1. Check the transaction status using Verify Payment API
  2. Common reasons for failure include:
     * Insufficient funds
     * Card expired or blocked
     * Mandate canceled or inactive
     * Bank issues
  3. Notify the customer about the failure
  4. Request customer to update payment method or register a new mandate
  5. Retry the transaction if appropriate

  For more information, refer to [Recurring Payment Transaction API](ref:recurring_payment_api).

* **What happens if I miss sending a pre-debit notification?**

  If you don't send a pre-debit notification before a recurring transaction for Cards or UPI, the recurring transaction will fail. Pre-debit notification is mandatory as per RBI guidelines. You should ensure that pre-debit notifications are sent at least 24 hours before the recurring charge transaction. For more information, refer to [Pre-Debit Notification API](ref:pre_debit_notification_api).

* **What should I do if a mandate becomes inactive?**

  If a mandate becomes inactive:

  1. Check the mandate status using the Check Mandate Status API
  2. Identify the reason for inactivity
  3. You may need to:
     * Modify the mandate if possible
     * Cancel the mandate and request customer to register a new one
     * Contact PayU support for assistance

  Recurring payments cannot be performed if the mandate is inactive. For more information, refer to [Check Mandate Status API](ref:check-mandate-status-api).

***

## SI with International Cards

* **What is the workflow for International Cards recurring payments?**

  The workflow for International Cards recurring payments:

  1. Customer provides card details and completes authentication (OTP verification is required)
  2. PayU performs authentication and creates subscription with SI hub
  3. PayU does authorization and updates SI hub with details
  4. Subscription is activated
  5. Merchant sends Pre-Debit Notification API
  6. Merchant processes recurring transactions using Recurring Payment Transaction API

  For more information, refer to [International Cards Integration - Recurring Payments](doc:international-cards-integration-recurring-payments).

* **Can I process recurring payments immediately after mandate setup for International Cards?**

  Yes, recurring payments can happen in real-time after the mandate is set up for International Cards. However, you must send the Pre-Debit Notification API before processing the recurring transaction. For more information, refer to [International Cards Integration - Recurring Payments](doc:international-cards-integration-recurring-payments).

* **What currencies are supported for International Cards recurring payments?**

  International Cards recurring payments support:

  * User issuing card currency
  * INR (Indian Rupees)

  For more information, refer to [International Cards Integration - Recurring Payments](doc:international-cards-integration-recurring-payments).

<br />
