---
title: Mutual Fund Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
This section outlines the integration process for Wealth Tech merchants to implement mutual fund payment flows using PayU's payment infrastructure in compliance with SEBI regulations.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. Contact your PayU Key Account Manager to enable Mutual Fund Payments (Wealth Tech) on your account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Overview

<Accordion title="Regulatory requirements" icon="fa-gavel">
  **SEBI requirements:** Payment aggregators must report investment transactions for mutual fund distributors and comply with the following:

  * Certain fields are mandatory for regulatory compliance
  * Additional data capture is required for exchange and regulatory reporting via the `products` (`wtParams`) object on each transaction
</Accordion>

<Accordion title="Supported payment methods" icon="fa-credit-card">
  **One-time payments**

  * Non-seamless — PayU Hosted Checkout
  * Seamless — Merchant Hosted
    * Net Banking
    * UPI

  **Subscriptions (SIP)**

  * ENACH (Net Banking mandate)
  * UPI Autopay
</Accordion>

<Accordion title="Benefits for Wealth Tech merchants" icon="fa-store">
  * **SEBI-compliant reporting** — Capture mandatory mutual fund fields through `wtParams` on every transaction
  * **Flexible checkout** — Offer PayU Hosted or Merchant Hosted flows for one-time investments
  * **Automated SIP** — Register mandates via ENACH or UPI Autopay and charge recurring debits without customer re-authentication
  * **Unified PayU stack** — Reuse standard `_payment`, subscription, and verification APIs with Wealth Tech extensions
</Accordion>

<Accordion title="Integration workflow summary" icon="fa-diagram-project">
  **One-time payment (PayU Hosted or Merchant Hosted)**

  1. Construct `_payment` request with `api_version=21`, `beneficiarydetail`, and `products` containing `wtParams`.
  2. Post to PayU and handle the customer payment flow (redirect or seamless).
  3. Validate postback reverse hash and verify payment status.

  **Subscription (ENACH or UPI Autopay)**

  1. Initiate consent transaction with `si=1`, `si_details`, `beneficiarydetail`, and `wtParams`.
  2. Verify successful mandate registration via Verify Payment API or webhooks.
  3. For UPI Autopay, call Pre-Debit Notification API before each debit.
  4. Execute recurring debits with Recurring Payment Transaction API (`si_transaction`) including `wtParams` in `var1`.
</Accordion>

## Integration guides

The following sections describe how to integrate mutual fund payments and subscriptions with PayU:

- **Payments**
  - [PayU Hosted Integration](doc:payu-hosted-integration-mutual-funds-payment) — Non-seamless checkout with `api_version=21`, `products` (`wtParams`), and `beneficiarydetail`
  - [Merchant Hosted Integration](doc:merchant-hosted-integration-mutual-fund-payments) — Seamless Net Banking and UPI with Wealth Tech reporting fields
- **Subscriptions**
  - [ENACH Integration – Mutual Funds](doc:enach-mutual-fund-payments-integration) — e-NACH mandate registration and recurring SIP debits
  - [UPI Autopay Integration – Mutual Funds](doc:upi-autopay-integration-mutual-fund-payments) — UPI mandate consent, pre-debit notification, and recurring debits

## APIs used in Mutual Fund Payments integration

<Table>
  <thead>
    <tr>
      <th>
        API
      </th>

      <th>
        Purpose
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ### \_payment APIs
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
      </td>

      <td>
        Initiate non-seamless mutual fund payments with `api_version=21`, `products` (`wtParams`), and `beneficiarydetail`.
      </td>
    </tr>

    <tr>
      <td>
        [Collect Payment API – Merchant Hosted Checkout](ref:_payment_merchant_hosted)
      </td>

      <td>
        Initiate seamless Net Banking (`pg=NB`) or UPI (`pg=UPI`) payments with Wealth Tech `products` and `beneficiarydetail`.
      </td>
    </tr>

    <tr>
      <td>
        ### Recurring Payment APIs
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Net Banking Recurring Payment Consent Transaction](ref:netbanking-recurring-payment-consent-transaction)
      </td>

      <td>
        Register an e-NACH mandate with `pg=ENACH`, `si=1`, and `si_details` for mutual fund SIP subscriptions.
      </td>
    </tr>

    <tr>
      <td>
        [UPI Recurring Payment Consent Transaction](ref:upi-recurring-payment-consent-transaction)
      </td>

      <td>
        Register a UPI Autopay mandate with `pg`/`bankcode` for INTTPV and `si=1`. .
      </td>
    </tr>

    <tr>
      <td>
        [Recurring Payment Transaction API](ref:recurring_payment_api)
      </td>

      <td>
        Execute subsequent SIP debits using `command=si_transaction` and `authpayuid` after mandate registration.
      </td>
    </tr>

    <tr>
      <td>
        [Pre-Debit Notification API](ref:pre_debit_notification_api)
      </td>

      <td>
        Send pre-debit notification before charging a UPI mandate (`command=pre_debit_si`).
      </td>
    </tr>

    <tr>
      <td>
        ### General
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        [Verify Payment API](ref:verify_payment_api)
      </td>

      <td>
        Server-side reconciliation of consent and payment transaction status.
      </td>
    </tr>
  </tbody>
</Table>

<br />
