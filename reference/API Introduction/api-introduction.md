---
title: PayU API Ecosystem
excerpt: >-
  Start here to understand the PayU API ecosystem. How they are organized, how
  authentication works, and how to make your first request.
deprecated: false
hidden: true
metadata:
  title: PayU API Introduction | Developer Guide
  description: >-
    Canonical starting point for PayU APIs. Learn which PayU API to use, how
    authentication works, base URLs, common workflows, and how to make your
    first API request.
  keywords:
    - PayU API
    - PayU API introduction
    - PayU developer documentation
    - PayU payment API
    - PayU API reference
    - PayU REST API
  robots: index
---
PayU APIs let you collect payments, verify transactions, issue refunds, manage subscriptions, disburse payouts, and operate partner or marketplace flows. This **API Introduction** is the canonical starting point for developers working with PayU APIs before you dive into individual [API Reference](ref:introduction-api-reference) pages.

Find answers to these questions here:

- What APIs does PayU provide?
- Which API should I use for my use case?
- How are PayU APIs organized?
- What authentication model applies to my product?
- How do I make my first successful API request?

## Your First API Call

Follow this recommended path:

1. Go through the ecosystem by reading [Which API should I use?](doc:which-api-should-i-use) and [API Architecture](doc:api-architecture) pages.
2. After you understand the PayU's API ecosystem, you should now set up credentials by getting your merchant key and salt from the [PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard), then review [API Authentication and Security](doc:api-authentication-and-security).
3. Now that you have credentials ready, choose the right environment. Use [API Environments and Base URLs](doc:api-environments-and-base-urls) to pick Test vs Production endpoints.
4. You have everything handy now to make your first request. Go through the [Making Your First API Request](doc:making-your-first-api-request) page for steps.

## PayU API Ecosystem at a Glance

| API family                           | What it does                                                                  | Typical auth                            | Start here                                                                                              |
| :----------------------------------- | :---------------------------------------------------------------------------- | :-------------------------------------- | :------------------------------------------------------------------------------------------------------ |
| **Collect Payment (**`_payment`**)** | Create payment transactions for hosted, merchant-hosted, and S2S checkout     | Key + salt + hash                       | [Collect Payment APIs](ref:_payment_payu_hosted_checkout)                                               |
| **General APIs**                     | Verify payments, fetch transaction details, refund, BIN info, EMI eligibility | Key + salt + hash (`command` + `var1…`) | [Check Transaction APIs](ref:check-transaction-apis)                                                    |
| **Payment Links**                    | Create and manage shareable payment links                                     | Product-specific                        | [Create Payment Link API](ref:create-payment-links)                                                     |
| **Subscriptions / Recurring**        | Consent, recurring debit, and subscription management                         | Key + salt + hash (+ SI details)        | [Payment Consent Transaction](ref:payment-consent-transaction-payu-hosted)                              |
| **Zion**                             | Subscription automation and invoice APIs                                      | Product-specific                        | [Zion Subscription APIs](ref:associating-plan-in-defined-subscription-interface)                        |
| **Settlements**                      | Settlement details, ranges, release                                           | Key + salt / product auth               | [Settlement Transaction Details API](https://docs.payu.in/reference/settlement_transaction_details_api) |
| **Payouts**                          | Disburse funds to beneficiaries                                               | OAuth token                             | [Generate Token API](ref:generate-token-using-merchants-credentials-api)                                |
| **Partner / Onboarding**             | Onboard merchants, KYC, OAuth partner flows                                   | OAuth / partner credentials             | [Get Token API](ref:get_token_api)                                                                      |
| **Split Settlements**                | Marketplace split during or after transaction                                 | Key + salt + hash (+ split payload)     | [Split During Transaction](ref:split-during-transaction-using-_payment)                                 |
| **Tokenization / Save Cards**        | Vault and saved-card payments                                                 | Key + salt + hash                       | [Save Cards APIs](ref:model-2-zero-code-change-for-vault-integration)                                   |
| **Affordability**                    | Offers, EMI, BNPL                                                             | Key + salt + hash / product auth        | [Fetch Offers API](ref:fetch-offers-api)                                                                |
| **Cross-border**                     | Import payments, virtual accounts, PACB                                       | Product-specific                        | [Invoice Upload API](ref:invoice_upload_api)                                                            |
| **BBPS**                             | Billers, bills, complaints, recharge                                          | Product-specific                        | [BBPS Introduction](ref:introduction-bbps)                                                              |
| **Chargeback**                       | Dispute and chargeback operations                                             | Product-specific                        | [Chargeback](doc:chargeback)                                                                            |
| **In-person / POS**                  | POS terminal, UPI QR, Android POS                                             | Product-specific                        | [In-person payments](ref:pos-terminal-integration-apis)                                                 |

## What's Next?

Choose your API based on your requirement.

<br />