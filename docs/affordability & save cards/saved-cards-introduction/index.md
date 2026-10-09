---
title: Saved Cards Introduction
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU Vault APIs allow customers to store multiple credit or debit card details securely in PayU's PCI-DSS Level 1 certified vault. PayU Vault stores the card tokens and allows you (the merchant) to retrieve and charge saved cards when your customer provides their user credentials.

Customers save time during checkout by selecting a saved card rather than re-entering 16-digit card numbers and expiry dates.

Customers can update or delete their saved cards at any time to maintain full control over their stored payment credentials.

## Lifecycle of a Saved Card

1. **Card Entry & Consent**: The customer visits your website or app, selects card payment, enters card details, and provides explicit consent to save the card.
2. **Tokenization**: PayU provisions a secure card token (Network Token and/or Issuer Token) via the card network or issuer.
3. **Repeat Checkout**: On subsequent visits, the customer provides their user credentials, and the merchant retrieves the saved card list (masked card numbers and card brand).
4. **Fast Checkout**: The customer selects their preferred card and completes the payment via Additional Factor of Authentication (AFA/OTP).
5. **Card Lifecycle Management**: The customer or merchant can update card metadata or delete tokens at any time in compliance with RBI guidelines.

<Callout icon="📘" theme="info">
  ### **Note on CVV**:

  While CVV is not mandatory from a card network perspective for tokenized transactions, certain issuing banks may still require CVV verification. If the issuing bank does not mandate CVV, merchants should not prompt the customer for it.
</Callout>

## Onboarding Prerequisites

Before enabling Card-on-File Tokenization (CoFT):

- **Token Requestor ID (TRID)**: Tokenization requires merchant TRID provisioning across schemes (Visa, Mastercard, RuPay, etc.). Contact your PayU Key Account Manager (KAM) to initiate TRID onboarding. Typical provisioning turnaround is 2–3 business days for Visa/Mastercard and 1–2 hours for domestic networks.
- **PCI-DSS Scope**:
  - **PayU Hosted Checkout (Model 1)**: PayU manages card entry and tokenization end-to-end on PayU servers. Merchants have zero cardholder data storage obligations.
  - **Merchant Hosted Checkout (Model 2 / Model 3)**: If you handle plain card data on your servers prior to tokenization or store tokens locally, ensure you maintain compliance with the relevant PCI Self-Assessment Questionnaire (e.g., SAQ A-EP or SAQ D).

## What is Tokenization?

Tokenization protects sensitive cardholder data by replacing the primary account number (PAN) with a unique, cryptographically secure surrogate identifier called a **Token**. A token has no intrinsic value outside the specific merchant and network relationship for which it was created.

### RBI Guidelines & Card-on-File Tokenization (CoFT)

Under Reserve Bank of India (RBI) guidelines for Card-on-File Tokenization:

- **No Entity in the Transaction Chain** (except card networks and issuing banks) may store actual card numbers (PAN), expiry dates, or CVVs.
- **Permitted Data**: Non-payment entities and merchants may store only limited, non-sensitive card metadata: the last 4 digits of the card, card brand/scheme, card type (credit/debit), and issuing bank name for transaction display and reconciliation.
- **Explicit Customer Consent & AFA**: Card saving requires explicit customer consent accompanied by Additional Factor of Authentication (AFA/OTP).
- **Customer Control**: Customers must be empowered to view, update, and revoke/delete their saved card tokens across merchant applications and issuer platforms.
- **Token Scope**: Every token is uniquely scoped to a specific combination of customer, card, merchant (TRID), and device/platform.

### Key Participants in the Tokenization Ecosystem

| Participant                 | Role                                               | Responsibilities                                                                                        |
| :-------------------------- | :------------------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Cardholder**              | Customer                                           | Initiates payment, provides explicit consent to save card, and completes AFA (OTP).                     |
| **Merchant**                | Token Requestor                                    | Collects customer consent, passes credentials to PayU, and initiates payments using tokens.             |
| **PayU**                    | Token Requestor & Technical Service Provider (TSP) | Manages merchant TRID onboarding, interfaces with card schemes and issuers, and securely vaults tokens. |
| **Card Networks & Issuers** | Token Service Providers (TSPs)                     | Authoritative generators of tokens, cryptograms (TAVV), and PAN-to-token mappings.                      |

### Network Tokens vs. Issuer Tokens

PayU supports both network and issuer tokenization to maximize transaction success and reliability:

* **Network Tokens**:
  - Virtual payment credentials issued directly by payment card schemes (Visa, Mastercard, RuPay, Diners, American Express).
  - Can be processed across any payment aggregator or acquiring bank connected to that scheme.
* **Issuer Tokens**:
  - Virtual credentials generated directly by the card-issuing bank (e.g., HDFC, ICICI, SBI).
  - Designed for direct, on-us processing between the merchant's acquiring bank and the issuer.
  - **Merchant Advantage**: Issuer tokens bypass intermediary card schemes when routed through compatible acquiring channels, offering **higher transaction success rates** and **optimized processing costs/MDR**.

### Alternative ID (Alt ID) for Guest Checkout

For one-time or guest checkout transactions where customers do not give consent to save their cards, RBI mandates that card details cannot be retained post-transaction.

PayU automatically supports RBI-compliant **Alternative Identifier (Alt ID)** processing for guest checkouts:

- During payment processing, PayU generates a dynamic Alt ID and transaction cryptogram in real-time.
- Card details are purged immediately following payment authorization, fulfilling compliance without degrading checkout speed.

## Which Model you Should Choose for Tokenization?

### Comparison Matrix

| Feature / Criteria | Model 1: PayU Hosted Checkout | Model 2: Zero Code Change | Model 3: Simple REST APIs |
| :--- | :--- | :--- | :--- |
| **Checkout UI Hosting** | Hosted entirely on PayU | Hosted on Merchant site (Seamless) | Hosted on Merchant site (Custom) |
| **Merchant Dev Effort** | Minimal / None (Configuration only) | Low (1 additional parameter in `_payment`) | Moderate (Direct API calls for CRUD) |
| **PCI-DSS Scope** | None (PayU handles card data) | Low (Merchant does not store card data) | SAQ A-EP or SAQ D (if storing tokens locally) |
| **Token Storage** | Stored on PayU Vault | Stored on PayU Vault | Stored on PayU Vault and/or Merchant servers |
| **Token Portability / Decoupled** | PayU checkout only | PayU payment gateway | Supported via Cryptogram API |
| **Customer Consent UI** | Managed by PayU Checkout UI | Collected on Merchant UI | Collected on Merchant UI |

### Model 1: PayU Hosted Checkout Integration

If you use PayU Hosted Checkout, PayU manages the tokenization lifecycle end-to-end on PayU's hosted payment page.
- **Workflow**: Customer selects card payment on PayU Checkout → enters card details → checks consent box → PayU tokenizes the card upon successful payment → repeat visits automatically display saved cards.
- **Best For**: Businesses seeking zero integration complexity, minimal PCI compliance obligations, and a fully managed checkout experience.
- [Read Model 1 Guide](doc:payu-hosted-checkout-integration-with-vault-model-1)

### Model 2: Zero Code Change (Merchant Hosted Checkout)

If you use Server-to-Server / Merchant Hosted Checkout (Seamless) and want PayU to handle token lifecycle management:
- **Workflow**: Merchant captures customer card details and consent on their own checkout page → passes card details + `store_card=1` and `user_credentials` in the `_payment` API → PayU processes payment and tokenizes card. On subsequent visits, merchant retrieves saved cards via `get_user_cards` and submits `store_card_token`.
- **Best For**: Merchants who maintain their own checkout experience and want PayU to handle tokenization storage and scheme lifecycle operations with minimal code modifications.
- [Read Model 2 Guide](doc:zero-code-change-for-vault-integration-model-2)

### Model 3: Simple REST APIs

Model 3 provides programmatic control over token creation, retrieval, updates, and deletion using direct REST / Postservice APIs.
- **Workflow**:
  1. Capture card details and consent on merchant checkout.
  2. Process payment via PayU or payment gateway.
  3. Call `save_payment_instrument` (or `/v4/carddetail`) to generate tokens.
  4. Store the resulting tokens on merchant servers (requires PCI SAQ A-EP/D) or reference them on PayU Vault.
  5. Fetch dynamic cryptograms via `get_payment_details` to execute repeat payments across any acquiring partner.
- **Best For**: Enterprise merchants, marketplaces, and platforms requiring decoupled token storage, multi-gateway routing, and custom token lifecycle management.
- [Read Model 3 Guide](doc:simple-rest-apis-for-vault-integration-model-3)

---

## Processing Transactions with Tokens Created Outside PayU

If you already possess network tokens generated through another Token Service Provider or aggregator, you can process repeat transactions through PayU by passing the token, expiry, and TAVV (Cryptogram) in the `_payment` API. For details, refer to [Collect Payments using a Tokenized Card](doc:collect-payments-using-a-saved-card).
