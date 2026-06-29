---
title: Mobikwik Link & Pay Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
---
title: Mobikwik Link & Pay Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
This section describes step-by-step integration procedure for Mobikwik Link & Pay, designed to offer a seamless, one-click payment experience for users and merchants.

It provides a **seamless, one-click payment experience** for Mobikwik wallet users on PayU’s S2S integration. This streamlined flow aims to simplify the checkout process and enhance the overall payment experience for all parties. By introducing Link & Pay, Mobikwik seeks to offer merchants an efficient and scalable solution that improves conversion rates and customer satisfaction, reinforcing PayU's leadership in payment innovation.

This integration is expected to deliver **measurable value** to merchants by reducing friction at checkout, increasing transaction success, and improving customer retention. For users, it promises a faster, more convenient, and secure payment process, making digital wallet payments more appealing.

## Integration guides

- [Steps to Integrate – Mobikwik Link & Pay](doc:steps-to-integrate-mobikwik-link-pay)
- [Testing Checklist – Mobikwik Link & Pay](doc:testing-checklist-mobikwik-link-pay)


## Advantages

<Accordion title="Advantages for Merchants" icon="fa-store">
  1. **Increased Conversion Rates**: The frictionless one-click payment process minimizes cart abandonment, leading to more completed transactions.
  2. **Enhanced Customer Retention**: A smoother payment experience boosts customer satisfaction, encouraging repeat purchases and fostering long-term loyalty.
  3. **Simplified Integration**: Merchants can implement Link & Pay with minimal changes, simplifying payment workflows and reducing operational complexity.
</Accordion>

<Accordion title="Advantages for Users" icon="fa-user">
  1. **Faster, Simplified Payments**: Users can complete transactions with a single click, eliminating the need to log into their wallet, resulting in a quicker and more convenient checkout.
  2. **Greater Flexibility**: Link & Pay allows secure storage of payment information, enabling instant and seamless payments across various platforms.
  3. **Enhanced Security**: Users benefit from Mobikwik’s encryption and authentication processes, ensuring their payment information is protected.
</Accordion>

This solution aims to drive higher user engagement, improved conversion rates, and reinforce PayU's position at the forefront of payment innovation, ultimately leading to increased transaction success, better customer retention, and stronger merchant relationships.

## Prerequisites

The development of the Link & Pay wallet feature spans multiple key areas, from Checkout to Core Payments. The entire ecosystem is designed for flexibility and scalability, serving the needs of both **S2S** (where the checkout and Wallet link/OTP page are managed by the merchant or PayU) and **PayU Hosted** checkout integration.

The integration utilizes the existing BNPL Link & Pay Generic API Stack, with customisation for S2S and PayU hosted Checkout merchants.

## Workflow

<Image align="center" src="https://files.readme.io/2e908af4b1340e292d310830a7d84b277916ddf80a49d05c1def1e171f1b427e-mobikwik_workflow_diagram_2.png" />

<Image align="center" src="https://files.readme.io/dfcb2bf925cd3a7dcc62d337dd3b8c9a27a489ac8f460361516999956c2da34b-mobikwik_workflow_diagram_3_1.png" />

## APIs used in Mobikwik Link & Pay integration

| API name | Purpose |
| --- | --- |
| [Check User Balance and Link Status API](doc:steps-to-integrate-mobikwik-link-pay#step-1-check-user-balance-and-link-status) (`/userbalance`) | Check whether the customer's Mobikwik wallet is linked and retrieve the available balance before initiating payment. |
| [Payment Initiation API](doc:steps-to-integrate-mobikwik-link-pay#step-2-payment-initiation-api) (`/v2/payments`) | Initiate a Mobikwik Link & Pay transaction on PayU; automatically routes linked users to auto-debit and unlinked users to the wallet-linking flow.|
| [Token Generate API – Mobikwik](ref:token-generate-api-mobikwik) (`/tokengenerate`) | Submit the OTP and generate a wallet token for linked repeat transactions.  |
| [Add Money to Wallet And Debit API – Mobikwik](ref:add-money-to-wallet-and-debit-api-mobikwik) | Load money into the wallet and debit in a single flow when the wallet balance is insufficient. |
| [Check Status API – Mobikwik](ref:check-status-api-mobikwik) | Verify whether the payment is complete|
| [Verify Payment API](ref:verify_payment_api) | Server-side reconciliation of transaction status after payment. |