---
title: Cards SI Decoupled Integration
excerpt: >-
  Set up card-based Standing Instructions (SI) on PayU using a decoupled
  authentication and authorization flow for Visa, Mastercard, and AMEX. Covers
  mandate creation, pre-debit notifications, recurring payments, and mandate
  management.
hidden: true
link:
  new_tab: false
metadata:
  title: Cards SI Integration — Decoupled Authentication and Authorization Flow
  description: >-
    Set up card-based Standing Instructions (SI) on PayU using a decoupled
    authentication and authorization flow for Visa, Mastercard, and AMEX. Covers
    mandate creation, pre-debit notifications, recurring payments, and mandate
    management.
  keywords:
    - Cards SI Integration Decoupled
    - Card Mandate Registration PayU
    - Recurring Payments Cards Decoupled
    - Standing Instruction Cards API
    - 3DS Authentication Authorization Flow
    - AuthorizeTransaction PayU
    - Cards SI Pre-Debit Recurring
---
PayU's Cards SI (Standing Instruction) Integration with decoupled authentication lets merchants register card mandates for Visa, Mastercard, and AMEX through a two-step flow where **authentication and authorization are handled as separate steps**. This gives merchants greater control over the mandate registration process, supports stored network tokens (saved cards), and enables merchants who perform 3DS authentication externally to pass results directly into PayU.

## Supported Networks

| Network    | Supported Card Types    |
| :--------- | :---------------------- |
| Visa       | Credit Card, Debit Card |
| Mastercard | Credit Card, Debit Card |
| AMEX       | Credit Card             |

## Before You Begin

Ensure the following are in place before starting integration:

- Active PayU merchant account. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).

- SI feature enabled on your MID. Contact your PayU Key Account Manager (KAM) to activate Standing Instructions for cards.

- Test credentials (key and salt) for the test environment. For more information, refer to [Check your API Key and Salt](doc:check-api-key-and-salt).

- Mandate cancellations for **Visa and Mastercard** are processed **without AFA** in accordance with card network guidelines.

***

## Integration Steps

The integration is split into two steps **Mandate Creation** and **Recurring Payments**.

### Step 1: Mandate Creation

Authentication and authorization happen in two separate API calls.

#### Authentication Flows Supported

| Flow                                    | When to Use                                                                                                                                                                                                                                            |
| :-------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Authentication via PayU: New Card**   | Send plain card details (`ccnum`, `ccname`, etc.). PayU handles 3DS and returns a Base64-encoded OTP page template (`acsTemplate`).                                                                                                                    |
| **Authentication via PayU: Saved Card** | Send a stored network token (`store_card_token`) with `storecard_token_type=1`. PayU handles 3DS. `siTokenDetails` in the subsequent `AuthorizeTransaction` call is optional for this flow.                                                            |
| **Authentication not via PayU**         | The merchant performs 3DS externally and passes the authentication result (`authentication_info` with `cavv`, `eci`, etc.) directly in the `_payment` call. The mandate is registered in this single call — no separate `AuthorizeTransaction` needed. |

<Cards>
  <Card title="Step 1.1: Payment and Authentication Initiation" href="doc:cards-si-step1-payment-authentication">
    Send the `_payment` request with card details. PayU performs normal card authentication and returns an `acsTemplate` (Base64-encoded HTML). Decode and render it to redirect the customer to the OTP page. After OTP submission, you receive `bankData` in the response.
  </Card>

  <Card title="Step 1.2: Authorization and Mandate Registration" href="doc:cards-si-step2-authorize-transaction">
    Pass `bankData` (augmented with `siTokenDetails`) as `authentication_info` to the `AuthorizeTransaction` API. On success, the response contains `IsStandingInstructionSet: "1"` confirming the mandate is registered. Save the `mihpayid` — this is the `authPayuId` for all future pre-debit and recurring calls.
  </Card>
</Cards>

***

### Step 2: Recurring Payments

Once the mandate is registered, use these APIs to schedule and execute recurring debits against it.

There are two approaches to scheduling pre-debit notifications and recurring debits. Choose the one that fits your integration model.

<Cards>
  <Card title="Unified Pre-Debit and Recurring API" href="ref:subscriptions-pdn-rp">
    Make a **single API call** using `command=si_transaction` with `debitType=PREDEBIT_AND_RECURRING`. PayU handles scheduling the pre-debit notification and executing the recurring debit automatically.
  </Card>

  <Card title="Separate Pre-Debit and Recurring APIs" href="ref:subscriptions-pdn-rp">
    Make **two separate API calls** using `command=si_transaction` — first with `debitType=PREDEBIT` to send the pre-debit notification, then with `debitType=RECURRING` to execute the recurring debit. Use this when your workflow requires explicit control over each step.
  </Card>
</Cards>

After a pre-debit or recurring debit is processed, verify the transaction outcome using the Verify SI Payment Status API.

<Cards>
  <Card title="Verify SI Payment Status" href="doc:cards-si-verify-si-payment">
    Check the status of a pre-debit or recurring payment using the `verify_si_payment` command. Pass the `rc_` prefixed transaction ID returned by the PDN/RP API as `var1`. Use this when a webhook is not received or to independently confirm the transaction outcome.
  </Card>
</Cards>

***

## Complete Flow Summary

The following steps describe the end-to-end Cards SI decoupled integration flow for the PayU-authenticated case:

1. **Payment request**: The merchant sends a `_payment` POST request to PayU with card details, `si=1`, and `si_details`.
2. **Acquirer selection**: PayU identifies the acquiring bank using the PG Selector Service.
3. **Authentication initiation:** PayU submits an authentication initiation request to the acquirer.
4. **Authentication initiation response**: The acquirer acknowledges and prepares the authentication session.
5. **ACS template redirection**: Base64-decode the `acsTemplate` value from the response to generate the HTML OTP page, then redirect the customer to it.
6. **Authentication status response**: PayU returns the authentication status after the customer enters the OTP. This response includes `bankData`.
7. **Prepare AuthorizeTransaction payload**: Add `siTokenDetails` (network token details) to the `bankData` JSON and use the combined object as `authentication_info`.
8. **AuthorizeTransaction**: The merchant calls the `AuthorizeTransaction` API to complete authorization and register the mandate.
9. **Authorization response**: PayU returns the final transaction result. Verify `IsStandingInstructionSet: "1"` and store the `mihpayid` as your `authPayuId`.
10. **Callback**: If configured, PayU triggers a merchant callback with the final transaction response.

<Callout icon="📘" theme="info">
  ### **Tips:**

  For the **Authentication not via PayU** flow (`txn_s2s_flow=3`), steps 5–8 are replaced by a single `_payment` call that includes the merchant's 3DS result directly. The mandate is registered in that single call.
</Callout>

***

## Hash Calculation Logic

Each API requires a SHA-512 hash computed from pipe-separated parameters using your merchant salt.

| API                                                 | Hash Formula                                                                                              |
| :-------------------------------------------------- | :-------------------------------------------------------------------------------------------------------- |
| `_payment`                                          | `SHA512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)` |
| `AuthorizeTransaction`                              | `SHA512(key\|txnid\|amount\|authentication_info\|SALT)`                                                   |
| `si_transaction` (Pre-Debit / Recurring / Retrieve) | `SHA512(key\|command\|var1\|SALT)`                                                                        |

<Callout icon="📘" theme="info">
  ### **Tips:**

  For the `_payment` hash, include the **serialised&#x20;**`si_details`**&#x20;JSON string** at position 16, after six trailing pipe characters. Use empty strings for any `udf` fields you are not sending.

  For `AuthorizeTransaction` and `si_transaction`, use the **exact serialised JSON string** posted as the field value — not the parsed object — when computing the hash.
</Callout>

***

## `si_details` Parameters

The `si_details` JSON object is passed in the `AuthorizeTransaction` request to register the mandate billing parameters. Use identical values in both calls. All these parameters are mandatory.

| Parameter          | Type    | Description                                                            |
| :----------------- | :------ | :--------------------------------------------------------------------- |
| `billingAmount`    | String  | Maximum mandate billing amount per cycle.                              |
| `billingCurrency`  | String  | Billing currency. Default: `INR`.                                      |
| `billingCycle`     | String  | Billing frequency: `ADHOC`, `DAILY`, `WEEKLY`, `MONTHLY`, or `YEARLY`. |
| `billingInterval`  | Integer | Number of billing cycle units between debits.                          |
| `paymentStartDate` | String  | Mandate start date in `YYYY-MM-DD` format.                             |
| `paymentEndDate`   | String  | Mandate end date in `YYYY-MM-DD` format.                               |

***

## Webhook Notifications

PayU sends webhook callbacks to your configured URL for all mandate and recurring payment lifecycle events. Callbacks are delivered in URL-encoded format.

<Callout icon="📘" theme="info">
  ### **Tips:**

  The sample payloads shown in this section have been converted to JSON format for readability only. The actual webhook data from PayU arrives in URL-encoded format.
</Callout>

### Mandate Registration Webhooks

| Event                   | `status`  | `unmappedstatus` | Meaning                                              |
| :---------------------- | :-------- | :--------------- | :--------------------------------------------------- |
| Successful registration | `success` | `captured`       | Mandate registered and initial transaction captured. |
| Failed registration     | `failure` | `failed`         | Mandate registration failed.                         |

<Callout icon="📘" theme="info">
  ### **Tips:**

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
  ### **Tips:**

  Mandate cancellation requests for **Visa and Mastercard** are processed without Additional Factor of Authentication (AFA) in accordance with card network guidelines for mandate management.
</Callout>

***

## What to Do Next

Start the integration with **Step 1 — Payment and Authentication Initiation**. Choose the flow that matches your use case:

| Flow                        | When to Use                                               | Start Here                                                                                                                                                               |
| :-------------------------- | :-------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New card via PayU           | Customer is paying with a new card for the first time     | <Anchor target="_blank" href="https://docs.payu.in/reference/post_payment#flow-1-new-card-authentication-via-payu">Flow 1: New Card Authentication via PayU</Anchor>     |
| Saved card via PayU         | Customer has a previously tokenised card stored with PayU | <Anchor target="_blank" href="https://docs.payu.in/reference/post_payment#flow-2-saved-card-authentication-via-payu">Flow 2: Saved Card Authentication via PayU</Anchor> |
| Authentication not via PayU | Merchant performs 3DS authentication independently        | <Anchor target="_blank" href="https://docs.payu.in/reference/post_payment#flow-3-authentication-not-via-payu">Flow 3: Authentication Not via PayU</Anchor>               |
