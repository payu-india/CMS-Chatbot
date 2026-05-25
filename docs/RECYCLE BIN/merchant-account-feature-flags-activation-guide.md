---
title: '[Internal Review]Merchant Account Feature Flags — Activation Guide'
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU supports many non-default features that must be explicitly enabled on your merchant account by your PayU KAM or support. These are sometimes referred to as "flags" or "merchant config" settings.

This section lists all known configurable flags, what each one does, and how to request activation.

## How to Request Flag Activation

To enable any flag listed on this page:

1. Contact your PayU **Key Account Manager (KAM)** directly, or
2. Email **[integration@payu.in](mailto:integration@payu.in)** with:
   - Your Merchant ID (MID)
   - The name of the flag or feature you need
   - Whether you need it on UAT, Production, or both

Response times vary by feature and some are activated within hours, others require compliance review or partner onboarding and may take several business days.

## Feature Flags Reference Table

| Flag / Feature                   | What It Does                                                                                                                                                                      | How to Request                                                 | Available In          |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | --------------------- |
| `txn_s2s_flow=1`                 | Enables seamless server-to-server (S2S) flow for card and UPI payments. Required for orchestration platforms like Juspay. Bypasses PayU's hosted payment page.                    | Contact KAM with MID                                           | UAT + Prod (separate) |
| `txn_s2s_flow=4`                 | Enables UPI Intent and DBQR S2S flows. Required for UPI Intent deep-link integration and Dynamic QR (DBQR) payments.                                                              | Contact KAM with MID                                           | Production only       |
| `disable_all_retry=1`            | Disables PayU's automatic payment retry logic. Use when you need an immediate failure response without retry delays. Helpful for real-time retry management on your own platform. | Contact KAM with MID                                           | UAT + Prod (separate) |
| UPI Intent                       | Enables UPI Intent (deep-link) payment mode on checkout. Customers are deep-linked directly into their UPI app to authorise payment. Not enabled by default.                      | Contact KAM                                                    | Production only       |
| UPI Mandate / AutoPay            | Required for UPI-based recurring payments via NPCI's autopay infrastructure. Separate from card SI.                                                                               | Contact KAM                                                    | UAT + Prod (separate) |
| eNACH                            | Enables bank-mandate based recurring payments (NACH/ACH). Separate activation from Standing Instructions (SI).                                                                    | Contact KAM                                                    | UAT + Prod (separate) |
| BNPL (Buy Now Pay Later)         | Enables LazyPay and similar BNPL payment options at checkout. Requires separate BNPL partner onboarding in addition to PayU flag activation.                                      | Contact KAM                                                    | UAT + Prod            |
| Offers Engine                    | Required to create and apply discount or cashback offers. Once enabled, manage offers from Dashboard → Offers.                                                                    | Contact KAM                                                    | UAT + Prod (separate) |
| No Cost EMI                      | Enables No Cost EMI (interest subsidised by merchant) as a payment option. Requires Offers Engine to be enabled first. Create No Cost EMI offers from Dashboard → Offers.         | Contact KAM (enable Offers Engine first)                       | UAT + Prod            |
| Split Settlement                 | Enables splitting a single transaction's settlement across multiple sub-merchant accounts. Used by aggregators and marketplaces.                                                  | Contact KAM — provide aggregator MID and all sub-merchant MIDs | Production only       |
| DBQR (Dynamic QR)                | Enables `pg=DBQR` payment flow — generates per-transaction UPI QR codes via API. Not available in test environment.                                                               | Contact KAM                                                    | Production only       |
| Tokenization / TRID / Store Card | Enables saving customer card details (tokenized) for future payments. Requires PCI-DSS compliance verification.                                                                   | Contact KAM — compliance review required                       | UAT + Prod (separate) |
| Auth & Capture                   | Enables two-step payment flow: Authorization (reserve funds) followed by a separate Capture (charge card). Supported for cards only.                                              | Contact KAM                                                    | UAT + Prod (separate) |
| `callback_on_failure`            | Sends real-time webhook notifications for pending and failed payment states, not just successful payments. By default, webhooks are only sent on success.                         | Email [support@payu.in](mailto:support@payu.in) or contact KAM | UAT + Prod (separate) |
| Pluxee Card (Sodexo)             | Separate activation required to accept Pluxee (formerly Sodexo) meal and gift cards as a payment method.                                                                          | Contact KAM                                                    | Prod only             |
| Cross-Border / Multi-Currency    | Required for accepting non-INR payments from international customers. Additional compliance and currency conversion configuration needed.                                         | Contact KAM                                                    | Prod only             |

## How to Check What Is Enabled on Your Account

### Payment methods

Log in to the **PayU Dashboard** → **Settings** → **Payment Methods**. This shows which payment instruments (card, UPI, net banking, wallets, etc.) are enabled for your checkout. For more information, refer to [Customize PayU Payment Page.](doc:payu-payment-page-customization)

### S2S flags and merchant config

There is no self-serve view for S2S flags (`txn_s2s_flow`, `disable_all_retry`, etc.) or most merchant config settings. Contact your KAM to confirm which flags are currently active on your MID. For more information, refer to [Server-to-Server.](doc:server-to-server-integration)

### Offers

Dashboard → **Offers** — if the Offers Engine is enabled, you will see the option to create and manage offers. For more information, refer to [Offers Dashboard.](doc:offers-dashboard)

***

## UAT vs Production Flags

> ⚠️ **Note:** Flags must be enabled **separately** for UAT and Production environments. Enabling a flag in UAT does not automatically apply it to Production.

You need to follow these steps in this regard:

1. Request UAT activation to develop and test your integration. For more information, refer to [Register with PayU.](doc:register-with-payu)
2. Raise a **separate request** for Production activation before going live.
3. Test your complete flow in UAT with the flag enabled before requesting Production access.

Some flags (DBQR, UPI Intent, Split Settlement, Pluxee, Cross-Border) are **Production-only** — there is no UAT equivalent for these features. Test your integration using alternative flows in UAT and validate the feature-specific behaviour in Production with small transactions.

***

## Frequently Asked Questions

### Can I enable flags myself from the Dashboard?

Most flags cannot be self-activated. Payment method toggles (e.g. enabling/disabling specific banks) may be self-serve, but S2S flows, recurring payment modes, tokenization, and settlement features require PayU team intervention.

### How long does activation take?

- Standard flags (S2S flows, DBQR, UPI Intent): typically 1–3 business days
- eNACH, UPI Mandate: may require additional onboarding documentation
- Tokenization: requires compliance review — typically longer
- BNPL: requires partner onboarding with the BNPL provider — varies

### Will activating a flag affect existing transactions?

Most flags are additive — they enable new payment options without affecting existing flows. However, `disable_all_retry` and `callback_on_failure` change payment processing behaviour and should be tested in UAT before Production activation.

***

##

<br />
