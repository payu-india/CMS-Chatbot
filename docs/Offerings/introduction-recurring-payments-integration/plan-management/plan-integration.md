---
title: Plan Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
Use Standing Instruction (SI) subscription plan integration when your business owns the billing schedule and wants to charge customers automatically after collecting their consent. In this flow, you define the plan details in your system, pass the same details to PayU during mandate registration, notify the customer before every debit, and trigger recurring charges as per the plan.

> 
>
> **Before you begin**: Enable Subscriptions for your PayU merchant account. Contact your PayU Key Account Manager or onboarding team before integrating SI plans.

## Integration flow

The SI subscription plan flow includes the following steps:

1. **Define the subscription plan** in your system with the amount, billing frequency, start date, end date, and customer details.
2. **Collect customer consent** by initiating the payment consent transaction with `si=1` and `si_details`.
3. **Store the mandate identifier** returned by PayU, such as `mihpayid` or `authpayuid`, against the customer subscription.
4. **Send the pre-debit notification** before the recurring debit as required by RBI guidelines.
5. **Collect the recurring payment** by calling the Recurring Payment Transaction API.
6. **Update the subscription state** in your system based on the recurring transaction response, webhook, or Verify Payment API.

<Cards columns={3}>
  <Card title="1. Consent" href="https://docs.payu.in/reference/payment-consent-transaction-merchant-hosted">
    Register the customer's SI mandate by passing plan details in `si_details`.
  </Card>

  <Card title="2. Pre-Debit" href="https://docs.payu.in/reference/pre_debit_notification_api">
    Notify the customer before initiating the recurring debit.
  </Card>

  <Card title="3. Recurring Debit" href="https://docs.payu.in/reference/recurring_payment_api">
    Charge the customer as per the registered plan and mandate.
  </Card>
</Cards>

## Define the subscription plan

Create and store the plan in your system before initiating the consent transaction. The plan information that the customer sees on your website or app must match the values sent to PayU in the `si_details` object.

| Plan field          | Description                                               | Example              |
| :------------------ | :-------------------------------------------------------- | :------------------- |
| Plan name           | Name shown to the customer for the selected subscription. | Premium monthly plan |
| Billing amount      | Amount to be charged for each billing cycle.              | 499.00               |
| Billing cycle       | Billing frequency for the plan.                           | MONTHLY              |
| Billing interval    | Interval between two billing cycles.                      | 1                    |
| Start date          | Date from which recurring debits can start.               | 2026-06-01           |
| End date            | Date on which the plan ends.                              | 2027-05-31           |
| Customer identifier | Your internal customer or subscription reference.         | CUST-10001           |

> 
>
> Keep your internal plan record immutable after consent is collected, except for changes explicitly approved through mandate modification flows. The plan values are used by PayU and banks to validate recurring charges.

## Pass plan details in `si_details`

During the consent transaction, pass `si=1` and include the plan details in the `si_details` JSON object. PayU forwards this mandate information to the issuer or payment ecosystem as applicable.

```json
{
  "billingCycle": "MONTHLY",
  "billingInterval": 1,
  "billingAmount": "499.00",
  "billingCurrency": "INR",
  "paymentStartDate": "2026-06-01",
  "paymentEndDate": "2027-05-31"
}
```

For the complete `si_details` field description, refer to [SI Parameter JSON Details](ref:si-parameter-json-details).

### Consent transaction checklist

Before calling the payment consent transaction API, ensure that:

- The customer has reviewed the amount, frequency, start date, end date, and cancellation terms.
- The payment request includes `si=1`.
- The payment request includes `si_details` with the same plan values shown to the customer.
- The hash is generated with `si_details` included in the hash sequence.
- Your success and failure URLs can update the subscription state after PayU redirects the customer.

The consent transaction can be initiated through either of the following integrations:

- [Payment Consent Transaction using PayU Hosted Checkout](ref:payment-consent-transaction-payu-hosted)
- [Payment Consent Transaction with Merchant Hosted Checkout](ref:payment-consent-transaction-merchant-hosted)

> 
>
> The first transaction must complete the required authentication flow. Subsequent recurring debits are processed against the registered mandate and do not require the customer to enter card credentials or complete 2FA again.

## Store consent response details

After the consent transaction succeeds, store the identifiers returned by PayU against your subscription record. These identifiers are required for later pre-debit notifications, recurring debits, mandate status checks, and reconciliation.

| Detail                      | Usage                                                                                |
| :-------------------------- | :----------------------------------------------------------------------------------- |
| `txnid`                     | Your transaction identifier for the consent transaction.                             |
| `mihpayid`                  | PayU transaction identifier returned for the consent transaction.                    |
| `authpayuid`                | Mandate or authorization identifier used in recurring payment APIs where applicable. |
| Subscription or customer ID | Your internal mapping between the customer, plan, and PayU mandate.                  |
| Mandate status              | Used to decide whether future recurring debits can be initiated.                     |

If the consent transaction fails or the mandate is rejected, ask the customer to retry the consent flow before scheduling recurring debits.

## Send pre-debit notification

Before charging the customer, call the [Pre-Debit Notification API](ref:pre_debit_notification_api) with the mandate identifier, debit amount, invoice number, and customer details. The notification amount must be within the limits approved during mandate registration.

Use a unique `invoiceDisplayNumber` for every debit attempt so you can reconcile the notification, recurring debit, and customer invoice.

## Initiate recurring payment

After the pre-debit notification succeeds, call the [Recurring Payment Transaction API](ref:recurring_payment_api) to debit the customer.

```json
{
  "authpayuid": "6611192557",
  "invoiceDisplayNumber": "INV-2026-0001",
  "amount": "499.00",
  "txnid": "REC-2026-0001",
  "phone": "9999999999",
  "email": "customer@example.com"
}
```

Treat the transaction status returned by PayU as the source of truth for that debit attempt. For pending or in-progress responses, update the final state using webhooks or the Verify Payment API.

## Manage plan changes

If the customer upgrades, downgrades, pauses, or cancels a plan, update your internal subscription state first and then use the appropriate mandate management APIs:

- [Check Mandate Status API](ref:check-mandate-status-api)
- [Modify the Recurring Payments for a Card](ref:modify-the-recurring-payments-for-a-card)
- [Cancel the Recurring Payment for Cards](ref:cancel-the-recurring-payment-for-cards)
- [Cancel the Recurring Payment for UPI](ref:cancel-the-recurring-payment-for-upi)

For fully managed subscription automation, you can also use [Zion Subscription Automation](doc:using-zion-subscription-automation-platform), where PayU manages plan billing, invoice generation, and recurring debits after consent.

## Go-live checklist

Before moving SI subscription plan integration to production:

- Confirm that Subscriptions are enabled on your PayU merchant account.
- Test successful and failed consent transactions for each supported payment mode.
- Validate the `si_details` payload for all plan frequencies that you offer.
- Store PayU mandate identifiers securely against your customer subscription records.
- Trigger pre-debit notifications before recurring debits.
- Implement webhooks or Verify Payment API polling to capture final payment status.
- Reconcile every recurring debit with the invoice and subscription record in your system.

<br />
