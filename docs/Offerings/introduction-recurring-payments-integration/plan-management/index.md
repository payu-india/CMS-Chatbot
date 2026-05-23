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

## Benefits of a Plan

Using a plan gives merchants a structured way to manage SI subscriptions.

<Accordion title="Plan Benefits" icon="fa-list-check">
<ul><li><strong>Clear customer consent:</strong> The customer sees the amount, frequency, start date, and end date before approving the mandate.</li>
<li><strong>Consistent billing schedule:</strong> Your system can calculate upcoming debit dates from the plan instead of relying on manual inputs for every cycle.</li>
<li><strong>Easier pre-debit management:</strong> The plan provides the amount and due date needed to trigger pre-debit notifications on time.</li>
<li><strong>Faster recurring payment operations:</strong> Merchants can trigger debits from a saved plan and mandate mapping instead of recreating payment details.</li>
<li><strong>Better dashboard controls:</strong> The frontend can show plan status, next debit date, last debit status, and allowed actions in one place.</li>
<li><strong>Improved reconciliation:</strong> Plan ID or merchant reference, mandate ID, invoice number, and transaction IDs can be mapped together for reports.</li>
<li><strong>Safer modifications and cancellations:</strong> Merchants can separate draft edits from active mandate changes and use the correct PayU APIs for supported updates.</li>
<li><strong>Reusable subscription setup:</strong> Common plan templates can reduce errors when merchants create similar subscriptions for multiple customers.</li>
<li><strong>Better customer support:</strong> Support teams can quickly see what the customer approved, when the next charge is due, and why a debit succeeded or failed.</li></ul>

</Accordion>

## Plan Status

Every plan goes through the following statuses:

<Cards>
  <Card title="Draft" icon="fa-file-pen" iconColor="#0c6150">
    Plans are saved in the system but not active. You cannot use draft plans for subscriptions until they are activated.
  </Card>

  <Card title="Active" icon="fa-circle-check" iconColor="#0c6150">
    A plan becomes active once it is created and immediately available for creating subscriptions.
  </Card>
</Cards>

## Access Plans

You can access **Plans** under **Subscriptions&#x20;**&#x66;rom the left navigation as shown below.


<Image src="https://files.readme.io/ceab99a98c18eb24f14d434f5159d4a6ae066d810e940e9f32828515fee74cc7-plan-management.gif" alt="Access Plans" align="center" caption="_Access Plans_" border={true} />


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
