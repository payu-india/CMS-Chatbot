---
title: Cards SI APIs
hidden: true
link:
  new_tab: false
---
PayU's Cards SI (Standing Instruction) Integration with decoupled authentication lets merchants register card mandates for Visa, Mastercard, and AMEX through a two-step flow where **authentication and authorization are handled as separate steps**. This gives merchants greater control over the mandate registration process, supports stored network tokens (saved cards), and enables merchants who perform 3DS authentication externally to pass results directly into PayU.

## Supported Networks

| Network    | Supported Card Types    |
| :--------- | :---------------------- |
| Visa       | Credit Card, Debit Card |
| Mastercard | Credit Card, Debit Card |
| AMEX       | Credit Card             |

## Before You Begin

<Callout icon="👍" theme="okay">
  Ensure the following are in place before starting integration:

  - Active PayU merchant account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
  - SI feature enabled on your MID. Contact your PayU Key Account Manager (KAM) to activate Standing Instructions for cards.
  - Test credentials (key and salt) for the test environment. For more information, refer to [Check your API Key and Salt](doc:check-api-key-and-salt).
  - Mandate cancellations for **Visa and Mastercard** are processed **without AFA** in accordance with card network guidelines.
</Callout>

***

## Phase I — Mandate Creation Flow

The mandate creation flow uses a decoupled authentication and authorization model. Authentication and authorization happen in two separate API calls.

### Authentication Flows Supported

| Flow                                     | When to Use                                                                                                                                                                                                                                            |
| :--------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Authentication via PayU — New Card**   | Send plain card details (`ccnum`, `ccname`, etc.). PayU handles 3DS and returns a Base64-encoded OTP page template (`acsTemplate`).                                                                                                                    |
| **Authentication via PayU — Saved Card** | Send a stored network token (`store_card_token`) with `storecard_token_type=1`. PayU handles 3DS. `siTokenDetails` in the subsequent `AuthorizeTransaction` call is optional for this flow.                                                            |
| **Authentication not via PayU**          | The merchant performs 3DS externally and passes the authentication result (`authentication_info` with `cavv`, `eci`, etc.) directly in the `_payment` call. The mandate is registered in this single call — no separate `AuthorizeTransaction` needed. |

<Cards>
  <Card title="Step 1 — Payment and Authentication Initiation" href="ref:cards-si-payment-authentication-initiation">
    Send the `_payment` request with card details, `si=1`, and `si_details`. PayU returns an `acsTemplate` (Base64-encoded HTML). Decode and render it to redirect the customer to the OTP page. After OTP submission, you receive `bankData` in the response.
  </Card>

  <Card title="Step 2 — Authorization and Mandate Registration" href="ref:cards-si-authorize-transaction">
    Pass `bankData` (augmented with `siTokenDetails`) as `authentication_info` to the `AuthorizeTransaction` API. On success, the response contains `IsStandingInstructionSet: "1"` confirming the mandate is registered. Save the `mihpayid` — this is the `authPayuId` for all future pre-debit and recurring calls.
  </Card>
</Cards>

***

## Phase II — Recurring Payment Flow

Once the mandate is registered, use these APIs to schedule and execute recurring debits against it.

<Cards>
  <Card title="Merge Pre-Debit and Recurring API" href="ref:cards-si-pre-debit-recurring-api">
    Schedules the pre-debit notification and processes the recurring debit in a single call using `command=si_transaction`. Set `debitType` to `PREDEBIT_AND_RECURRING` (default), `PREDEBIT`, or `RECURRING` based on the operation needed.
  </Card>

  <Card title="Fetch Pre-Debit and Recurring Status" href="ref:cards-si-fetch-status-api">
    Retrieve the current invoice and payment lifecycle status for an existing debit. Pass `debitType: RETRIEVE` in the same `si_transaction` endpoint.
  </Card>
</Cards>

***

## Complete Flow Summary

The following steps describe the end-to-end Cards SI decoupled integration flow for the PayU-authenticated case:

1. **Payment request** — The merchant sends a `_payment` POST request to PayU with card details, `si=1`, and `si_details`.
2. **Acquirer selection** — PayU identifies the acquiring bank using the PG Selector Service.
3. **Authentication initiation** — PayU submits an authentication initiation request to the acquirer.
4. **Authentication initiation response** — The acquirer acknowledges and prepares the authentication session.
5. **ACS template redirection** — Base64-decode the `acsTemplate` value from the response to generate the HTML OTP page, then redirect the customer to it.
6. **Authentication status response** — PayU returns the authentication status after the customer enters the OTP. This response includes `bankData`.
7. **Prepare AuthorizeTransaction payload** — Add `siTokenDetails` (network token details) to the `bankData` JSON and use the combined object as `authentication_info`.
8. **AuthorizeTransaction** — The merchant calls the `AuthorizeTransaction` API to complete authorization and register the mandate.
9. **Authorization response** — PayU returns the final transaction result. Verify `IsStandingInstructionSet: "1"` and store the `mihpayid` as your `authPayuId`.
10. **Callback** — If configured, PayU triggers a merchant callback with the final transaction response.

<Callout icon="📘" theme="info">
  For the **Authentication not via PayU** flow (`txn_s2s_flow=3`), steps 5–8 are replaced by a single `_payment` call that includes the merchant's 3DS result directly. The mandate is registered in that single call.
</Callout>

***

## Hash Calculation Logic

Each API requires a SHA-512 hash computed from pipe-separated parameters using your merchant salt.

| API                                                 | Hash Formula                                                                                                          |
| :-------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------- |
| `_payment`                                          | `SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|si_details\|SALT)` |
| `AuthorizeTransaction`                              | `SHA512(key\|txnid\|amount\|authentication_info\|SALT)`                                                               |
| `si_transaction` (Pre-Debit / Recurring / Retrieve) | `SHA512(key\|command\|var1\|SALT)`                                                                                    |

<Callout icon="📘" theme="info">
  For the `_payment` hash, include the **serialised&#x20;**`si_details`**&#x20;JSON string** at position 16, after six trailing pipe characters. Use empty strings for any `udf` fields you are not sending.

  For `AuthorizeTransaction` and `si_transaction`, use the **exact serialised JSON string** posted as the field value — not the parsed object — when computing the hash.
</Callout>

***

## si_details Parameters

The `si_details` JSON object is required in both the `_payment` and `AuthorizeTransaction` requests. Use identical values in both calls.

| Parameter          | Type    | Required | Description                                                            |
| :----------------- | :------ | :------- | :--------------------------------------------------------------------- |
| `billingAmount`    | String  | Yes      | Maximum mandate billing amount per cycle.                              |
| `billingCurrency`  | String  | Yes      | Billing currency. Default: `INR`.                                      |
| `billingCycle`     | String  | Yes      | Billing frequency: `ADHOC`, `DAILY`, `WEEKLY`, `MONTHLY`, or `YEARLY`. |
| `billingInterval`  | Integer | Yes      | Number of billing cycle units between debits.                          |
| `paymentStartDate` | String  | Yes      | Mandate start date in `YYYY-MM-DD` format.                             |
| `paymentEndDate`   | String  | Yes      | Mandate end date in `YYYY-MM-DD` format.                               |

***

## Webhook Notifications

PayU sends webhook callbacks to your configured URL for all mandate and recurring payment lifecycle events. Callbacks are delivered in URL-encoded format.

<Callout icon="📘" theme="info">
  The sample payloads shown in this section have been converted to JSON format for readability only. The actual webhook data from PayU arrives in URL-encoded format.
</Callout>

### Mandate Registration Webhooks

| Event                   | `status`  | `unmappedstatus` | Meaning                                              |
| :---------------------- | :-------- | :--------------- | :--------------------------------------------------- |
| Successful registration | `success` | `captured`       | Mandate registered and initial transaction captured. |
| Failed registration     | `failure` | `failed`         | Mandate registration failed.                         |

### Recurring Payment Webhooks

| `notificationType`  | `invoice_status` | `paymentStatus` | Meaning                                                                                                 |
| :------------------ | :--------------- | :-------------- | :------------------------------------------------------------------------------------------------------ |
| `PREDEBIT_SUCCESS`  | `PD_SUCCESS`     | Due             | Pre-debit notification processed successfully. Recurring debit will be attempted on the scheduled date. |
| `PREDEBIT_FAILED`   | `PD_FAILED`      | Due             | Pre-debit notification failed. Payment still due.                                                       |
| `RECURRING_SUCCESS` | `RC_SUCCESS`     | Paid            | Recurring payment successfully processed and invoice paid.                                              |
| `RECURRING_FAILED`  | `RC_FAILED`      | Due             | Recurring payment failed. May be retried based on gateway configuration.                                |

<Callout icon="📘" theme="info">
  Webhook status can also be independently verified at any time using the **Fetch Pre-Debit and Recurring Status** API with `debitType: RETRIEVE`. For more information, refer to [Fetch Pre-Debit and Recurring Status](ref:cards-si-fetch-status-api).
</Callout>

***

## Mandate Management

After mandate creation, use the following APIs to manage the mandate lifecycle.

| Action                                                      | API Reference                                                                                 |
| :---------------------------------------------------------- | :-------------------------------------------------------------------------------------------- |
| Verify a payment transaction (if callback not received)     | [Verify Payment API](ref:verify-payment)                                                      |
| Check current mandate status at any time                    | [Check Mandate Status API](ref:check-mandate-status-api)                                      |
| Cancel mandate — Visa and Mastercard (existing integration) | [Cancel Recurring Payment for a VISA/MASTER Card](ref:cancel-the-recurring-payment-for-cards) |
| Cancel mandate — Visa, Mastercard, AMEX (new integration)   | Contact your PayU KAM for the updated cancellation API for the decoupled flow                 |

<Callout icon="📘" theme="info">
  Mandate cancellation requests for **Visa and Mastercard** are processed without Additional Factor of Authentication (AFA) in accordance with card network guidelines for mandate management.
</Callout>
