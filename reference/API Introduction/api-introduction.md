---
title: Introduction
excerpt: >-
  Start here to understand the PayU API ecosystem. How they are organized, how
  authentication works, and how to make your first request.
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU APIs let you collect payments, verify transactions, issue refunds, manage subscriptions, disburse payouts, and operate partner or marketplace flows. This **API Introduction** is the canonical starting point for developers working with PayU APIs before you dive into individual [API Reference](ref:introduction-api-reference) pages.

Use this section to answer:

- What APIs does PayU provide?
- Which API should I use for my use case?
- How are PayU APIs organized?
- What authentication model applies to my product?
- How do I make my first successful API request?

## Who this section is for

- Backend developers integrating PayU for the first time
- Platform and marketplace engineers evaluating PayU APIs
- Partners building onboarding, payments, or payouts flows
- AI agents and Ask AI workflows that need a single, consistent entry point

## How to use this section

Follow this recommended path:

1. **Understand the ecosystem** — Read [Which API should I use?](doc:which-api-should-i-use) and [API Architecture](doc:api-architecture).
2. **Set up credentials** — Get your merchant key and salt from the [PayU Dashboard](doc:generate-merchant-key-and-salt-on-payu-dashboard), then review [API Authentication and Security](doc:api-authentication-and-security).
3. **Choose the right environment** — Use [API Environments and Base URLs](doc:api-environments-and-base-urls) to pick Test vs Production endpoints.
4. **Make your first request** — Follow [Making Your First API Request](doc:making-your-first-api-request).
5. **Build the workflow** — Use [Common API Workflows](doc:common-api-workflows) for payment, verification, callback, refund, and reconciliation paths.
6. **Open the reference** — Call the exact endpoint from [API Reference](ref:introduction-api-reference).

## PayU API ecosystem at a glance

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

<Callout icon="📘" theme="info">
  ### Integration vs API Reference

  - Use **Integration Guides** under [Getting Started](doc:introduction) and [Collect Payments](doc:introduction-web) for end-to-end product workflows.
  - Use **API Introduction** (this section) for shared API concepts that apply across products.
  - Use **[API Reference](ref:introduction-api-reference)** for endpoint schemas, parameters, and Try It playground calls.
</Callout>

## Developer journey

```
Get credentials → Authenticate → Call Test API → Create payment
→ Handle redirect/webhook → Verify payment → Refund / settle / reconcile
```

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Stage
      </th>

      <th>
        What you do
      </th>

      <th>
        Docs
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        1. Credentials
      </td>

      <td>
        Generate Test key and salt
      </td>

      <td>
        [Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)
      </td>
    </tr>

    <tr>
      <td>
        2. Authenticate
      </td>

      <td>
        Build the correct hash or OAuth token
      </td>

      <td>
        [Authentication](doc:api-authentication-and-security)
      </td>
    </tr>

    <tr>
      <td>
        3. First call
      </td>

      <td>
        Hit a Test endpoint
      </td>

      <td>
        [Making Your First API Request](doc:making-your-first-api-request)
      </td>
    </tr>

    <tr>
      <td>
        4. Collect
      </td>

      <td>
        Create a payment with `_payment`
      </td>

      <td>
        [Collect Payment](ref:_payment_payu_hosted_checkout)
      </td>
    </tr>

    <tr>
      <td>
        5. Confirm
      </td>

      <td>
        Verify status server-to-server
      </td>

      <td>
        [Verify Payment](ref:verify_payment_api)
      </td>
    </tr>

    <tr>
      <td>
        6. Notify
      </td>

      <td>
        Process surl/furl and webhooks
      </td>

      <td>
        [Webhooks and Callbacks](doc:webhooks-and-callbacks)
      </td>
    </tr>

    <tr>
      <td>
        7. Operate
      </td>

      <td>
        Refund, settle, reconcile
      </td>

      <td>
        [Common API Workflows](doc:common-api-workflows)
      </td>
    </tr>
  </tbody>
</Table>

## What to read next

- [Which API should I use?](doc:which-api-should-i-use) — Choose the right PayU API for your use case
- [API Architecture](doc:api-architecture) — How PayU APIs are organized
- [API Authentication and Security](doc:api-authentication-and-security) — Key, salt, hash, OAuth, and HMAC
- [Making Your First API Request](doc:making-your-first-api-request) — End-to-end first call
- [API Reference](ref:introduction-api-reference) — Endpoint catalog and Try It playground

## Related APIs

- [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
- [Verify Payment API](ref:verify_payment_api)
- [Create Payment Link API](ref:create-payment-links)
- [Generate Token using Merchant's Credentials API](ref:generate-token-using-merchants-credentials-api)

<br />