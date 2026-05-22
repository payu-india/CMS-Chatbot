---
title: Plan Management
deprecated: false
hidden: true
metadata:
  robots: index
---
A plan defines the subscription terms that the customer accepts before a Standing Instruction (SI) mandate is registered. In API-based SI integrations, the plan is managed by your system and shared with PayU during the consent transaction through `si_details`.

PayU does not require you to create a separate plan object before registering an SI mandate. Your frontend should maintain the plan configuration, show it to the customer, pass the approved values to PayU during consent, and use the returned mandate identifiers for future pre-debit notifications, recurring debits, and mandate management.

> ✅ **Before you Begin**&#x20;
>
> Enable Subscriptions for your PayU merchant account. Contact your PayU Key Account Manager or onboarding team before integrating SI plans.

## What is a plan?

A plan is the billing schedule and amount that the customer agrees to for recurring payments. It should include enough information for your system, PayU, and the customer to identify what will be charged and when.

| Plan field         | Description                                                       | PayU mapping                                                        |
| :----------------- | :---------------------------------------------------------------- | :------------------------------------------------------------------ |
| Plan name          | Merchant-defined name shown to the customer.                      | Store in your system or pass through UDF/custom fields if required. |
| Billing amount     | Amount charged for each billing cycle or maximum approved amount. | `si_details.billingAmount`                                          |
| Billing currency   | Currency for the recurring amount.                                | `si_details.billingCurrency`                                        |
| Billing cycle      | Frequency such as DAILY, WEEKLY, MONTHLY, YEARLY, ONCE, or ADHOC. | `si_details.billingCycle`                                           |
| Billing interval   | Interval for the selected billing cycle.                          | `si_details.billingInterval`                                        |
| Start date         | Date from which recurring payments can start.                     | `si_details.paymentStartDate`                                       |
| End date           | Date on which recurring payments should end.                      | `si_details.paymentEndDate`                                         |
| Customer details   | Customer name, email, phone, and identifier.                      | `_payment` request parameters and merchant records.                 |
| Mandate identifier | PayU identifier returned after successful consent.                | `mihpayid`, `authpayuid`, or relevant response identifier.          |
| Plan status        | State used by your frontend to control actions.                   | Merchant-managed state, updated using PayU responses and webhooks.  |

For the complete SI field descriptions, refer to [SI Parameter JSON Details](ref:si-parameter-json-details).

## Plan lifecycle

Use a lifecycle in your frontend so merchants can understand which actions are available at each stage.

| Status          | Meaning                                                             | Typical frontend actions                                            |
| :-------------- | :------------------------------------------------------------------ | :------------------------------------------------------------------ |
| Draft           | Plan details are being configured and consent is not yet requested. | Edit, preview, duplicate, delete draft.                             |
| Consent pending | Customer checkout or mandate registration has started.              | View, resend link if applicable, mark failed after timeout.         |
| Active          | Consent succeeded and future debits can be scheduled.               | View, schedule pre-debit, trigger recurring debit, cancel mandate.  |
| Debit scheduled | A pre-debit notification has been sent for an upcoming charge.      | View notification, track debit window, trigger debit when eligible. |
| Paused          | Merchant has stopped scheduling debits temporarily in their system. | Resume, cancel.                                                     |
| Completed       | Plan end date or planned billing count has been reached.            | View, export, duplicate.                                            |
| Cancelled       | Mandate or merchant plan has been cancelled.                        | View, export, create a new plan.                                    |
| Failed          | Consent or recurring debit failed.                                  | View failure reason, retry consent, retry debit where applicable.   |

## Frontend actions for plan management

The following actions can be exposed on a merchant dashboard or internal frontend. The API column shows the PayU reference page that supports each backend step.

| Frontend action             | What the merchant can do                                                                                                            | PayU API reference                                                                                                                                                                                                  |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Create plan                 | Enter plan name, amount, billing cycle, interval, start date, end date, and customer details.                                       | [SI Parameter JSON Details](ref:si-parameter-json-details)                                                                                                                                                          |
| Preview customer consent    | Review the exact subscription terms before sending the customer to checkout.                                                        | [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted), [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted) |
| Register mandate            | Start consent with `si=1` and `si_details`.                                                                                         | [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted), [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted) |
| View plans                  | List plans from your system with mandate status, customer details, next debit date, and last payment status.                        | [Check Mandate Status API](ref:check-mandate-status-api), [Verify Payment API](ref:verify_payment_api)                                                                                                              |
| Search and filter           | Filter by status, customer, date range, payment mode, plan name, mandate ID, or transaction ID.                                     | [Check Mandate Status API](ref:check-mandate-status-api), [Verify Payment API](ref:verify_payment_api)                                                                                                              |
| View plan details           | Show plan configuration, consent transaction, mandate identifier, pre-debit history, recurring debit history, and customer details. | [SI Parameter JSON Details](ref:si-parameter-json-details), [Verify Payment API](ref:verify_payment_api)                                                                                                            |
| Edit draft plan             | Change plan values before consent is requested.                                                                                     | No PayU API call is required until consent starts.                                                                                                                                                                  |
| Modify active mandate       | Change supported mandate details after registration where the payment mode supports modification.                                   | [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card), [Modify the Recurring Payment for UPI](ref:modify-the-recurring-payment-for-upi)                                          |
| Pause plan in frontend      | Stop scheduling pre-debit and debit attempts in your system without cancelling the mandate.                                         | Merchant-managed action.                                                                                                                                                                                            |
| Resume plan                 | Resume scheduling future pre-debit and debit attempts from your system.                                                             | [Pre-Debit Notification API](ref:pre_debit_notification_api), [Recurring Payment Transaction API](ref:recurring_payment_api)                                                                                        |
| Send pre-debit notification | Notify the customer before charging them.                                                                                           | [Pre-Debit Notification API](ref:pre_debit_notification_api)                                                                                                                                                        |
| Trigger recurring debit     | Charge the customer against the registered mandate.                                                                                 | [Recurring Payment Transaction API](ref:recurring_payment_api)                                                                                                                                                      |
| Cancel plan or mandate      | Stop future recurring charges by cancelling the mandate where supported.                                                            | [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards), [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi)                                              |
| Duplicate plan              | Copy plan configuration to create a new draft for another customer.                                                                 | No PayU API call is required until consent starts.                                                                                                                                                                  |
| Export plans                | Download plan, mandate, and debit history for reconciliation.                                                                       | Use your merchant records with [Verify Payment API](ref:verify_payment_api) where status refresh is needed.                                                                                                         |

> 
>
> Keep draft edits separate from active mandate changes. Once the customer has approved a mandate, use only the supported modification or cancellation flows for that payment mode.

## Recommended frontend sections

### Plan list

The plan list helps merchants monitor all subscriptions at a glance.

Recommended columns:

- Plan name
- Customer name, email, and phone
- Payment mode
- Billing amount and currency
- Billing cycle and interval
- Start date and end date
- Plan status
- Mandate identifier
- Next debit date
- Last debit status

Use your system as the source for plan configuration. Use [Check Mandate Status API](ref:check-mandate-status-api), [Verify Payment API](ref:verify_payment_api), and webhooks to refresh payment and mandate status.

### Plan creation form

Capture the values that will be shown to the customer and sent to PayU.

| Form field       | Validation guidance                                                                 |
| :--------------- | :---------------------------------------------------------------------------------- |
| Plan name        | Use a merchant-readable name for support and reconciliation.                        |
| Amount           | Match the amount format required by the payment request and `si_details`.           |
| Currency         | Use INR where applicable.                                                           |
| Billing cycle    | Use values supported for the selected payment mode.                                 |
| Billing interval | Keep the value consistent with the billing cycle.                                   |
| Start date       | Use the date from which recurring debits can start.                                 |
| End date         | Use the final date allowed for recurring debits.                                    |
| Customer details | Capture email and phone because they are used for payment and notifications.        |
| Payment mode     | Show only modes enabled for your account, such as Cards, UPI, or Net Banking/eNACH. |

For field-level mapping, refer to [SI Parameter JSON Details](ref:si-parameter-json-details).

### Consent review

Before initiating the consent transaction, show the customer:

- Plan name or subscription purpose
- Amount or maximum amount
- Billing frequency
- Start date and end date
- Payment mode
- Cancellation terms

Use these same values in the `_payment` request with `si=1` and `si_details`. For consent integration, refer to [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted) or [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted).

### Plan detail page

The plan detail page should combine plan configuration with transaction history.

Recommended sections:

- Plan summary
- Customer details
- Consent transaction details
- Mandate details
- Pre-debit notification history
- Recurring debit history
- Available actions based on plan and mandate status
- Audit log of merchant actions

### Audit log

Maintain an audit log for frontend plan actions. Include:

- Merchant user
- Action performed
- Previous values and new values
- Timestamp
- Plan ID or merchant reference ID
- PayU transaction or mandate identifier, where applicable

## API reference matrix

| Use case                                          | Reference                                                                                                    |
| :------------------------------------------------ | :----------------------------------------------------------------------------------------------------------- |
| Understand plan fields sent during consent        | [SI Parameter JSON Details](ref:si-parameter-json-details)                                                   |
| Register consent through PayU Hosted Checkout     | [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)        |
| Register consent through Merchant Hosted Checkout | [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted) |
| Check mandate status for card mandates            | [Check Mandate Status API](ref:check-mandate-status-api)                                                     |
| Send pre-debit notification                       | [Pre-Debit Notification API](ref:pre_debit_notification_api)                                                 |
| Trigger recurring debit                           | [Recurring Payment Transaction API](ref:recurring_payment_api)                                               |
| Modify a card mandate                             | [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card)                     |
| Modify a UPI mandate                              | [Modify the Recurring Payment for UPI](ref:modify-the-recurring-payment-for-upi)                             |
| Cancel a card mandate                             | [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards)                         |
| Cancel a UPI mandate                              | [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi)                             |
| Verify payment status                             | [Verify Payment API](ref:verify_payment_api)                                                                 |

## Implementation checklist

Before publishing plan management actions:

- Keep the merchant plan record as the source of truth for plan configuration.
- Pass the same plan terms to the customer UI and `si_details`.
- Store `txnid`, `mihpayid`, `authpayuid`, customer identifiers, and mandate status after consent.
- Show only actions that are valid for the current plan and mandate status.
- Trigger pre-debit notifications before recurring debits where required.
- Use webhooks or Verify Payment API to update final payment status.
- Confirm cancellation or destructive actions before calling the relevant API.
- Maintain an audit trail for every frontend action.

<br />
