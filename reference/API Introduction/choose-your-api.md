---
title: Choose Your API
deprecated: false
hidden: true
metadata:
  robots: index
---
Choosing the right PayU API depends on what you want to achieve. Use this decision guide to map your developer workflow to the correct API family, then open the matching Integration Guide and API Reference.

## Start with your goal

| If you want to…                               | Use this API family                                      | Primary docs                                                                                                     |
| :-------------------------------------------- | :------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------- |
| Accept a one-time online payment on a website | Collect Payment (`_payment`) — Hosted or Merchant Hosted | [Web integrations](doc:introduction-web), [Collect Payment APIs](ref:_payment_payu_hosted_checkout)              |
| Accept payments with full backend control     | Collect Payment (`_payment`) — Server-to-Server          | [S2S integration](doc:server-to-server-integration)                                                              |
| Accept payments in a mobile app               | Mobile SDKs (backed by payment APIs)                     | [Mobile SDKs](doc:explore-android-sdks)                                                                          |
| Collect payment without building checkout UI  | Payment Links / Invoices                                 | [No-code payments](doc:introduction-no-code-payments-integration), [Payment Links API](ref:create-payment-links) |
| Check if a payment succeeded                  | General APIs — Verify Payment / transaction details      | [Verify Payment](ref:verify_payment_api)                                                                         |
| Refund a payment                              | General APIs — Refund                                    | [Refunds](doc:introduction-refunds), [Refund APIs](doc:apis-used-in-refunds-integration)                         |
| Charge customers on a schedule                | Subscriptions / Recurring / Zion                         | [Recurring payments](doc:introduction-recurring-payments-integration)                                            |
| Save cards for faster checkout                | Tokenization / Save Cards                                | [Save Cards](doc:introduction-save-cards)                                                                        |
| Split one payment across sellers              | Split Settlements                                        | [Split Settlements](doc:split-settlments)                                                                        |
| Send money to bank accounts or UPI            | Payouts                                                  | [Payouts](doc:introduction-to-payouts), [Payouts APIs](ref:generate-token-using-merchants-credentials-api)       |
| Onboard sub-merchants programmatically        | Partner / Merchant Onboarding APIs                       | [Partner integration](ref:partner-integration-api-introduction)                                                  |
| Offer EMI, BNPL, or offers at checkout        | Affordability APIs                                       | [Affordability](doc:introduction-to-affordability)                                                               |
| Accept cross-border / import payments         | Cross-border Payments                                    | [Cross-border import](doc:introduction-cross-border-payments-import)                                             |
| Integrate BBPS bill payments                  | BBPS APIs                                                | [BBPS](doc:recharge-api-integration)                                                                             |
| Handle disputes                               | Chargeback APIs                                          | [Chargeback](doc:chargeback)                                                                                     |
| Accept in-store / POS payments                | In-person payment APIs                                   | [In-person payments](doc:in-person-payments)                                                                     |

## Decision flow for collecting payments

```
Do you need a checkout UI from PayU?
├─ Yes, minimal code → Payment Links / No-code
├─ Yes, hosted page → PayU Hosted Checkout (_payment)
├─ Yes, but my UI → Merchant Hosted Checkout (_payment)
└─ No, pure API orchestration → Server-to-Server (_payment)
```

### Website and app collection options

| Integration              | Dev effort | PCI scope                         | Best for                                         |
| :----------------------- | :--------- | :-------------------------------- | :----------------------------------------------- |
| Payment Links / Invoices | Very low   | PayU-managed                      | Instant collection without a full checkout build |
| PayU Hosted Checkout     | Low        | PayU-managed                      | Fast go-live with PayU-hosted payment page       |
| Merchant Hosted Checkout | Medium     | Higher (card fields on your page) | Custom UI with more control                      |
| Server-to-Server         | High       | Highest                           | Large merchants needing full orchestration       |
| Mobile SDKs              | Low–medium | Depends on SDK mode               | Native Android, iOS, React Native, Flutter       |

For a deeper comparison of checkout products, see [Getting Started — Introduction](doc:introduction).

## Decision flow after a payment is created

| Next job                              | API to call                                                    | Why                                                   |
| :------------------------------------ | :------------------------------------------------------------- | :---------------------------------------------------- |
| Confirm final status from your server | [Verify Payment](ref:verify_payment_api) / transaction details | Never trust browser redirects alone                   |
| React in real time                    | [Webhooks and Callbacks](doc:webhooks-and-callbacks)           | Async status updates for success, failure, refund     |
| Return money to customer              | Refund APIs                                                    | Full or partial refunds against `mihpayid` / `txnid`  |
| Understand settlement timing          | Settlement APIs                                                | Know when funds are settled to your account           |
| Split with child merchants            | Split Settlements APIs                                         | Marketplace and aggregator payouts of collected funds |

## Auth model by API family

Not every PayU product uses the same authentication. Pick APIs and auth together:

| Auth model                         | Used by                                                        | Learn more                                                                                                      |
| :--------------------------------- | :------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| Merchant key + salt + request hash | Collect Payment, General APIs, many PG features                | [API Authentication and Security](doc:api-authentication-and-security)                                          |
| OAuth 2.0 access token             | Payouts, Partner flows                                         | [Payouts token API](ref:generate-token-using-merchants-credentials-api), [Partner Get Token](ref:get_token_api) |
| HMAC header authentication         | Selected product APIs (for example, some wallet/rewards flows) | [Headers and Content Types](doc:headers-and-content-types)                                                      |

## Recommended starting paths

### Path A — First online payment

1. [Making Your First API Request](doc:making-your-first-api-request)
2. [Collect Payment — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
3. [Verify Payment](ref:verify_payment_api)
4. [Webhooks and Callbacks](doc:webhooks-and-callbacks)

### Path B — Marketplace / aggregator

1. [Split Settlements overview](doc:split-settlments)
2. [Split During Transaction API](ref:split-during-transaction-using-_payment)
3. Child merchant onboarding APIs under Split Settlements

### Path C — Disbursements

1. [Introduction to Payouts](doc:introduction-to-payouts)
2. [Generate Token using Merchant's Credentials](ref:generate-token-using-merchants-credentials-api)
3. Beneficiary and payout initiation APIs

### Path D — Recurring revenue

1. [Recurring payments integration](doc:introduction-recurring-payments-integration)
2. Consent transaction APIs
3. Recurring debit / Zion management APIs

## What to read next

- [API Architecture](doc:api-architecture)
- [API Environments and Base URLs](doc:api-environments-and-base-urls)
- [Common API Workflows](doc:common-api-workflows)
- [API Reference catalog](ref:introduction-api-reference)

## Related APIs

- [Collect Payment API — PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
- [Collect Payment API — Merchant Hosted Checkout](ref:_payment_merchant_hosted)
- [Collect Payment API — S2S](ref:_payment_server_to_server)
- [Verify Payment API](ref:verify_payment_api)
- [Create Payment Link API](ref:create-payment-links)

<br />
