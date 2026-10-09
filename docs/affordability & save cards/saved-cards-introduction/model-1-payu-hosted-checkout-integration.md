---
title: 'Model 1: PayU Hosted Checkout Integration'
deprecated: false
hidden: false
metadata:
  robots: index
---
This guide describes how cards are tokenized, saved, and charged in PayU Vault using **PayU Hosted Checkout (Model 1)**.

<Callout icon="📘" theme="info">
  ### **Note**:

  If you are an existing PayU Vault merchant, no additional development is required. Tokenization will be handled automatically for your account.
</Callout>

<Callout icon="👍" theme="okay">
  ### **Zero UI Implementation**:

  When customers make a card payment using PayU Hosted Checkout, PayU displays the card saving consent checkbox automatically on the checkout page. You do not need to build or modify any checkout UI elements for customer consent.
</Callout>

## Onboarding & Setup

To use Card-on-File Tokenization with PayU Hosted Checkout:

1. **Enable Vault**: Contact your PayU Key Account Manager (KAM) to activate PayU Vault and ensure your Token Requestor ID (TRID) is provisioned with card networks.
2. **Customer Identifier**: When initiating payment, pass the customer identifier in `user_credentials` (`<merchantKey>:<customerId>`). This identifier links saved card tokens to the user profile across sessions.

***

## First-Time Transaction Workflow

1. **Checkout Initiation**: Your customer lands on the PayU hosted checkout page.
2. **Card Entry**: The customer enters card details (Card Number, Name, Expiry, CVV).
3. **Explicit Consent**: The customer opts in by checking the **"Save this card as per RBI guidelines"** checkbox displayed by PayU.
4. **Authorization & Tokenization**: PayU initiates the payment with Additional Factor of Authentication (AFA/OTP). Upon successful authorization, PayU provisions the network and issuer tokens and stores them securely in PayU Vault.

***

## Repeat Transaction Workflow

When a returning customer performs a repeat transaction:

1. **Initiate Payment Request**: You initiate the payment request via `_payment` passing `user_credentials` set to `<merchantKey>:<customerId>`.
2. **Saved Cards Displayed**: PayU automatically renders the customer's saved cards with masked numbers (last 4 digits), expiry month/year, and card brand icon.
3. **Fast Payment**: The customer selects their preferred card and completes the payment via OTP. (CVV is prompted only if required by the card-issuing bank).
