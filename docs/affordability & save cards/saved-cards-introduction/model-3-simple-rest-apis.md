---
title: 'Model 3: Simple REST APIs'
deprecated: false
hidden: true
metadata:
  robots: index
---
Model 3 provides programmatic REST and Postservice APIs to manage the tokenization lifecycle independently of payment processing.

<Callout icon="📘" theme="info">
  ### **Note**:

  To tokenize cards and process transactions, complete Token Requestor ID (TRID) onboarding through your PayU Key Account Manager (KAM).
</Callout>

***

## Model 3 Capabilities

- **Direct Token Creation**: Generate network/issuer tokens after validating cardholder consent and completing AFA.
- **Decoupled Architecture**: Separate card storage from transaction processing.
- **Dynamic Cryptogram Retrieval**: Fetch transaction cryptograms (TAVV) to process payments across any acquiring partner or gateway.
- **Consent & Lifecycle Management**: Update card metadata or delete tokens on demand to maintain compliance.
- **Multi-Merchant / Sub-Merchant Support**: Aggregators and marketplaces can pass `subMerchantId` to segregate token vaults across seller accounts.

***

## Integration Workflow

### 1. First-Time Transaction & Tokenization

1. **Obtain Consent**: Capture explicit cardholder consent to save the card on your checkout page.
2. **Authorize Payment**: Process the first transaction via `_payment` to establish the Additional Factor of Authentication (AFA/OTP).
3. **Invoke Save Card API**: After receiving a successful payment response, call `save_payment_instrument` (or `POST /v4/carddetail`) to generate and store tokens:
   - Returns the PayU `cardToken`.
   - If the merchant is certified PCI-DSS Level 1 (SAQ D), the response includes the network token and issuer token details.

### 2. Repeat Transactions

#### Scenario A: Processing via PayU Gateway

Submit the saved `cardToken` (or `networkToken`) with `user_credentials` to the `_payment` API. Refer to [Collect Payments using a Tokenized Card](doc:collect-payments-using-a-saved-card).

#### Scenario B: Decoupled Processing (Outside PayU)

If routing transactions through another payment processor:

1. Call `get_payment_details` passing the `cardToken` or `networkToken` to generate a dynamic cryptogram (TAVV) and transaction reference.
2. Submit the resulting token and cryptogram to your preferred payment processor.

***

## Token Lifecycle Management

Merchants must provide customers with tools to manage their vaulted cards in compliance with RBI guidelines:

| Action                 | API Command / Endpoint                                       | Description                                                                      |
| :--------------------- | :----------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **Retrieve Cards**     | `get_payment_instrument`<br />`GET /storecard/card/v1`       | Fetch all active saved cards for a customer using `userCredentials`.             |
| **Edit Card Metadata** | `edit_payment_instrument`                                    | Update cardholder name or card nickname associated with a token.                 |
| **Delete Saved Card**  | `delete_payment_instrument`<br />`DELETE /storecard/card/v1` | Delete a vaulted card by `cardToken`, `networkToken`, or `issuerToken`.          |
| **Fetch Cryptogram**   | `get_payment_details`<br />`GET /storecard/v3/token-data`    | Retrieve dynamic TAVV cryptogram, PAR, and TRID for decoupled payment execution. |
