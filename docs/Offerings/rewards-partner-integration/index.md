---
title: Rewards Partner Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
Rewards is a loyalty points integration solution that leverages India's largest reward points network and integrates seamlessly with the PayU payment platform. It connects merchants to over 300 million users and allows them to earn and redeem reward points from over 20 leading issuers in a unified, frictionless checkout experience.

<Callout icon="👍" theme="okay">
  ### Before you begin:

  Register for a account with PayU before you start integration. Contact your PayU Key Account Manager to enable Rewards (RewardX) and obtain your merchant ID (`mid`) for loyalty APIs. For more information, refer to [Register for a Merchant Account](doc:register-for-a-merchant-account-on-dashboard).
</Callout>

## Product overview

<Accordion title="Product ecosystem" icon="fa-network-wired">
  * **Network and scale** — Over 300 million active users; 20+ issuer partners (for example, Flipkart SuperCoins, Zillion)
  * **Key features** — Unified loyalty experience combining multiple programs; hybrid payments (rewards + Card/UPI) using PayU's existing infrastructure
  * **Primary use cases** — eCommerce, digital marketplaces, quick commerce, and travel/entertainment
</Accordion>

<Accordion title="Benefits for merchants" icon="fa-store">
  * **Incremental GMV** — Increases revenue through alternative payment options
  * **Conversion optimization** — Reduces checkout drop-offs with flexible payment methods
  * **Cost savings** — Merchants can save approximately 8–10% on orders using reward point strategies
  * **Customer retention** — Improves customer lifetime value through loyalty engagement
  * **Unified integration** — Access the loyalty ecosystem without separate issuer integrations
</Accordion>

<Accordion title="Benefits for customers" icon="fa-user">
  * **Enhanced value** — Better utility for reward points across multiple brands
  * **Simplified experience** — Consolidated interface for various loyalty programs
  * **Flexible payments** — Combine reward points, promotional offers, and balance payments in one checkout
</Accordion>

<Accordion title="Benefits for developers" icon="fa-code">
  * Minimal implementation by leveraging PayU's existing payment framework
  * Detailed documentation and developer support from PayU
  * Reliable scalability for high transaction volumes
  * Proven across 35,000+ active merchant integrations
</Accordion>

<Accordion title="Use cases and applications" icon="fa-bullseye">
  * **E-commerce platforms** — Seamless reward point redemption during online checkout
  * **Digital marketplaces** — Cross-brand point utilisation across product categories
  * **Quick commerce** — Instant reward point validation for time-sensitive transactions
  * **Entertainment and travel** — Point redemption for bookings, tickets, and experiential purchases
</Accordion>

<Accordion title="Integration workflow summary" icon="fa-diagram-project">
  **Burn (redemption) or earn**

  1. **Fetch balance** — Call [Fetch Balance All API](ref:rewards-fetch-balance-all-api) with customer mobile and loyalty providers (`TWID`, `ZILLION`).
  2. **Initiate payment** — POST to [Collect Payment with Rewards API](ref:_payment-merchant-hosted-rewards) with `pg=SPLITPAY`, provider `bankcode`, and `splitInfo` for Card/UPI and reward legs.
  3. **Validate postback** — Verify reverse hash on the PayU response.
  4. **Verify payment** — Reconcile status with [Verify Payment API](ref:verify_payment_api) or webhooks.

  **Refunds**

  For partial refunds, the primary instrument (UPI or Card) is refunded first, then the reward partner leg. See [Rewards Refund Integration](doc:rewards-refund-integration).
</Accordion>

## Integration guides

The following sections describe how to integrate Rewards (RewardX) with PayU:

- [Rewards Pay Redemption Integration](doc:rewards-pay-redemption-integration) — Burn TWID or Zillion points at checkout with Card or UPI
- [Earn Rewards Integration](doc:earn-rewards-integration) — Accrue loyalty points on Card/UPI transactions
- [RewardX Decoupled Flow Integration](doc:rewardx-decoupled-flow-integration) — Server-to-server decoupled card flow for RewardX payments
- [Rewards Refund Integration](doc:rewards-refund-integration) — Refund split-payment transactions across payment legs

## APIs used in Rewards Partner integration

| API                                                                              | Purpose                                                                                                                         |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| [Fetch Balance All API](ref:rewards-fetch-balance-all-api)                       | Retrieve usable TWID and Zillion reward balances for a customer before checkout.                                                |
| [Collect Payment with Rewards API](ref:_payment-merchant-hosted-rewards)         | Initiate a SPLITPAY `_payment` request with `pg=SPLITPAY` and `splitInfo` to burn or earn reward points along with Card or UPI. |
| [Verify Payment API](ref:verify_payment_api)                                     | Server-side reconciliation of transaction status after payment.                                                                 |
| [Cards Decoupled Flow API](ref:_payment_s2s_decoupled_flow)                      | Initiate a server-to-server decoupled card payment for RewardX transactions.                                                    |
| [Submit OTP API](ref:submit-otp-to-payu)                                         | Submit OTP during decoupled card authentication on the merchant page.                                                           |
| [Refund Transaction API](ref:refund_transaction_api)                             | Initiate refunds for split-payment transactions; both child transactions (Card/UPI and rewards) are refunded.                   |
| [Refund Status API for Split Payments](ref:refund-status-api-for-split-payments) | Check refund status for split-payment child transactions.                                                                       |

<br />
