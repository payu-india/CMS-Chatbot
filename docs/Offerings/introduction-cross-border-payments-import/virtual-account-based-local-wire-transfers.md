---
title: Virtual-Account Based Local Wire Transfers
deprecated: false
hidden: true
metadata:
  robots: index
---
Collect cross-border payments through Virtual Accounts (VA). Payers in India transfer INR via NEFT, RTGS, or IMPS. PayU confirms the credit, holds it until required trade data is submitted and approved, then settles to your offshore account in currency of choice.

Suited for: Global **Payment Service Providers&#x20;**(PSPs) integrating via API.

**Illustrative payment journey for PACB Virtual Account Collections.**

![](https://files.readme.io/363270ff925b38a549c84cdfddf9b4bd346b7180f3a944581c9b680b6a889635-image.png)

<br />

1. **Sub-merchant onboarding** — Create sub-merchant and retrieve API credentials.
2. **Create & manage VA&#x20;**— Provision and manage Virtual Account via API.
3. **Receive credit&#x20;**— Payer transfers to VA; PayU confirms and notifies PSP.
4. **On-hold handling** — PSP submits invoice and trade metadata; PayU runs checks.
5. **Settle&#x20;**— Approved payments settle to PSP via AD Bank with UTR.

PayU partners with an AD-1 category bank for outward settlement. Funds move to the Outward Collection Account (OCA) before settlement to the PSP, similar to the [import collections workflow.](https://docs.payu.in/docs/workflow-for-cross-border-payments-import)

## Integration Guide

| Section                             | Activity                                  | API Document(s)                                                                                           |
| ----------------------------------- | ----------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| **Sub-merchant onboarding**         | Create sub-merchant                       | [Create Merchant API (International)](https://docs.payu.in/reference/create-merchant-api-pacb)            |
|                                     | Update sub-merchant profile               | [Update Merchant API (International)](https://docs.payu.in/reference/update-merchant-details-api-pacb)    |
| **Virtual Account (VA) Management** | Create Virtual Account                    | [Create Virtual Account](https://docs.payu.in/reference/create-virtual-account-api-pacb)                  |
|                                     | Disable Virtual Account                   | [Deactivate Virtual Account](https://docs.payu.in/reference/deactivate-virtual-account-api-pacb)          |
|                                     | Get List of VA per merchant               | [Get Virtual Accounts per MID](https://docs.payu.in/reference/get-virtual-accounts-api-pacb)              |
| **Payments**                        | Payment webhooks &                        | [Payment Webhooks](https://docs.payu.in/docs/webhook-events-and-sample-payloads)                          |
|                                     | Transaction Status Check API              | [Verify Payment API](https://docs.payu.in/reference/verify_payment_api)                                   |
|                                     | Get all transactions (per MID)            | [Get Transactions API](https://docs.payu.in/reference/get_transaction_details_api)                        |
| **On hold transactions**            | Get & Update On-Hold transactions         | [Get & Update On-hold API](https://docs.payu.in/docs/on-hold-settlements-cross-border-payments)           |
| **Settlement**                      | Get Settlement Status                     | [Get Settlement Details API](https://docs.payu.in/reference/settlement-detail-range-api-for-cross-border) |
| **Refunds**                         | Initiate refund by merchant txn ID / PayU | [Refund APIs (Initiate, Check Status)](https://docs.payu.in/docs/refund-apis-doc)                         |
|                                     | Get Refund Status API                     | [Refund APIs (Initiate, Check Status)](https://docs.payu.in/docs/refund-apis-doc)                         |

## Key Behaviours

- After credit, payment is on hold until metadata is complete and checks pass
- Transaction limit at INR 25,00,000, any transaction on the virtual account higher than this amount will be **rejected**.
- Onboarding uses PSP's credentials; payments use **sub-merchant credentials**

<br />

## Getting Started

- Obtain parent PA credentials from PayU.
- Integrate Create Merchant and Get Credentials for a test sub-merchant.
- Register webhook URLs.
- Test: create sub-merchant → receive credit → submit metadata → fetch settlement details.

For issues, share merchant ID, transaction ID, and webhook eventId with your PayU integration contact or [international.integration@payu.in](mailto:international.integration@payu.in)
