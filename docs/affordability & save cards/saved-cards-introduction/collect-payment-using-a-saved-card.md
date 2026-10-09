---
title: Collect Payment using a Saved Card
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
PayU allows merchants to charge saved cards securely using card tokens across several transaction flows:

1. **Zero Code Change (Model 2)**: Using PayU Vault token hub reference IDs.
2. **Network Tokens**: Using tokens issued directly by Visa, Mastercard, RuPay, etc.
3. **Issuer Tokens**: Using bank-issued tokens for optimized on-us routing.
4. **Decoupled Flow**: Using PayU for authentication or authorization with external partner tokens.

***

## End-to-End Repeat Payment Lifecycle

For all scenarios described below, follow this 3-step sequence:

1. **Retrieve Saved Cards**: Call `get_user_cards` or `get_payment_instrument` with your `key` and customer `user_credentials` (`<merchantKey>:<customerId>`).
2. **Submit Payment Request**: Send the payment details along with the token identifier to the `_payment` endpoint.
3. **Verify Payment Status**: Verify the payment status using server-to-server reconciliation via the `verify_payment` API.

***

## Scenario 1: Using Zero Code Change Approach (Model 2)

**Applicability**: The card was tokenized through PayU Vault Model 2, and PayU manages token creation and storage.

- **Mandatory Parameters in&#x20;**`_payment`:
  - `user_credentials`: `<merchantKey>:<customerId>`
  - `store_card_token`: PayU `cardToken` returned when the card was vaulted
  - `storecard_token_type`: `0`
  - Standard payment parameters (`key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `surl`, `furl`, `hash`, `pg=CC`, `bankcode`)
  - `ccvv`: Customer CVV (prompted only if required by the issuing bank)

***

## Scenario 2: Using Network Tokens

**Applicability**: The merchant has obtained a network token and cryptogram (TAVV) from a card scheme or partner TSP and submits the transaction for processing.

### Additional Parameters Required

| Parameter              | Type      | Required? | Description                                            | Example                                                                                   |
| :--------------------- | :-------- | :-------- | :----------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| `store_card_token`     | `string`  | Mandatory | The 16-digit Network Token value.                      | `1234456724563566`                                                                        |
| `storecard_token_type` | `integer` | Mandatory | Set to `1` for network tokens.                         | `1`                                                                                       |
| `ccexpmon`             | `integer` | Mandatory | Token expiry month (`MM`).                             | `10`                                                                                      |
| `ccexpyr`              | `integer` | Mandatory | Token expiry year (`YYYY`).                            | `2026`                                                                                    |
| `additional_info`      | `string`  | Mandatory | JSON-encoded string containing network token metadata. | `{"last4Digits":"1234","tavv":"ABCDEFGH","trid":"1234567890","tokenRefNo":"abcde123456"}` |

***

## Scenario 3: Using Issuer Tokens

**Applicability**: The merchant holds an issuer token generated directly by the card-issuing bank for on-us processing.

### Additional Parameters Required

| Parameter              | Type      | Required? | Description                                           | Example                                                                                                                                   |
| :--------------------- | :-------- | :-------- | :---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- |
| `store_card_token`     | `string`  | Mandatory | The Issuer Token value.                               | `1234456724563566`                                                                                                                        |
| `storecard_token_type` | `integer` | Mandatory | Set to `1`.                                           | `1`                                                                                                                                       |
| `ccexpmon`             | `integer` | Mandatory | Token expiry month (`MM`).                            | `10`                                                                                                                                      |
| `ccexpyr`              | `integer` | Mandatory | Token expiry year (`YYYY`).                           | `2026`                                                                                                                                    |
| `additional_info`      | `string`  | Mandatory | JSON-encoded string containing issuer token metadata. | `{"trMerchantId":"INBANPAYUWIBPAY011","tokenReferenceId":"02ac786d-0081-4b1a-a2a6-b0755a83964c","tokenBank":"HDFC","last4Digits":"8179"}` |

***

## Scenario 4: Decoupled Payment Flows

In decoupled processing, token generation/authentication and payment authorization occur through separate platforms:

- **Authentication via PayU, Authorization Outside**: Generate tokens via PayU, retrieve the dynamic cryptogram (TAVV) via `get_payment_details`, and submit the transaction to an external processor.
- **External Authentication, Authorization via PayU**: Pass the external network token, TAVV cryptogram, and TRID in `additional_info` to PayU's `_payment` endpoint for payment clearing.