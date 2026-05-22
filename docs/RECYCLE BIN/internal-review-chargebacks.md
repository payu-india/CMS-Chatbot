---
title: '[Internal Review] Chargebacks'
deprecated: false
hidden: true
link:
  new_tab: false
metadata:
  robots: index
---
A chargeback is a transaction reversal that occurs when a customer successfully disputes a charge on their debit or credit card. It results in the payment amount being returned to the customer's account. Buyers typically request chargebacks from their credit card issuing bank when they want to dispute a charge from their credit card statement.

Understanding chargebacks and how to manage them effectively is critical for maintaining a healthy merchant account and minimizing financial losses.

***

## How Chargebacks Differ from Refunds

| Aspect                 | Chargeback                         | Refund                    |
| ---------------------- | ---------------------------------- | ------------------------- |
| **Initiated by**       | Customer (via their bank)          | Merchant                  |
| **Process**            | Bank-mediated dispute              | Direct merchant action    |
| **Timeline**           | Can occur months after transaction | Usually within days/weeks |
| **Fees**               | Chargeback fee applies             | No additional fees        |
| **Impact on Merchant** | Affects chargeback ratio           | No ratio impact           |
| **Reversible**         | Can be contested                   | Final once processed      |

<Callout icon="💡" theme="default">
  **Tip**:** Proactively issuing refunds when customers have legitimate complaints can help you avoid chargebacks and their associated fees.
</Callout>

***

## Chargeback Support by Payment Method

Chargebacks are supported for the following payment methods:

### Cards

* Credit Cards (Visa, Mastercard, Rupay, Amex, Diners)
* Debit Cards
* Card-Not-Present (CNP) transactions
* International Cards

### EMI

* Card EMI
* Debit Card EMI
* UPI EMI
* Cardless EMI

### Digital Payments

* UPI
* Net Banking

### Wallets

| Wallet       | Supported |
| ------------ | --------- |
| PayTM        | ✅         |
| PhonePe      | ✅         |
| Amazon Pay   | ✅         |
| Freecharge   | ✅         |
| Airtel Money | ✅         |
| Ola Money    | ✅         |
| MobiKwik     | ✅         |
| HDFC PayZapp | ✅         |
| Yes Bank     | ✅         |
| Jio Money    | ✅         |
| ItzCash      | ✅         |
| Oxigen       | ✅         |

### International

* Cross-Border Payments (OPGSP)
* Apple Pay

***

## PayU Chargeback Process

The chargeback process involves four key steps:

```
┌─────────────────────────────────────────────────────────────────────┐
│                     PayU Chargeback Process                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  Step 1: CHARGEBACK RECEIVED                                        │
│  └── PayU receives chargeback notification from acquiring bank       │
│                          │                                           │
│                          ▼                                           │
│  Step 2: MERCHANT NOTIFIED                                          │
│  └── PayU notifies merchant with case details and Reply Date         │
│      └── Via email, dashboard, and webhook (if configured)          │
│                          │                                           │
│                          ▼                                           │
│  Step 3: MERCHANT RESPONSE                                          │
│  └── Merchant must respond before Reply Date                        │
│      ├── Option A: Accept the chargeback                            │
│      └── Option B: Contest with supporting documents                │
│                          │                                           │
│                          ▼                                           │
│  Step 4: RESOLUTION                                                 │
│  └── PayU shares documents with acquiring bank                      │
│      └── Bank makes final decision                                  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

> ⚠️ **Critical:** If you do not respond before the **Reply Date**, the acquiring bank will automatically close the case in favor of the customer.

***

## Chargeback Lifecycle States

Understanding chargeback states helps you track and manage cases effectively:

| State                | Description                          | Actions Available                 |
| -------------------- | ------------------------------------ | --------------------------------- |
| **NEW**              | Chargeback just received             | View details                      |
| **PENDING_RESPONSE** | Awaiting merchant response           | Accept, Contest                   |
| **UNDER_REVIEW**     | PayU reviewing submitted documents   | View status                       |
| **CONTESTED**        | Documents sent to bank               | View status                       |
| **ACCEPTED**         | Merchant accepted the chargeback     | None                              |
| **WON**              | Dispute resolved in merchant's favor | None                              |
| **LOST**             | Dispute resolved in customer's favor | Request arbitration (if eligible) |
| **PRE_ARBITRATION**  | Bank requested additional review     | Submit additional documents       |
| **ARBITRATION**      | Final dispute resolution stage       | Submit final documents            |
| **CLOSED**           | Case finalized                       | None                              |

### State Flow Diagram

```
NEW
 │
 ▼
PENDING_RESPONSE ────────────────┐
 │                               │
 ├──▶ ACCEPTED ──▶ CLOSED       │
 │                               │
 └──▶ CONTESTED                  │
      │                          │
      ▼                          │
 UNDER_REVIEW                    │
      │                          │
      ├──▶ WON ──▶ CLOSED       │
      │                          │
      ├──▶ LOST ──┬──▶ CLOSED   │
      │           │              │
      │           └──▶ PRE_ARBITRATION
      │                    │
      │                    ▼
      │              ARBITRATION
      │                    │
      │                    ├──▶ WON ──▶ CLOSED
      │                    │
      │                    └──▶ LOST ──▶ CLOSED
      │
      └──▶ AUTO_CLOSED (No response by Reply Date)
```

***

## Response Timelines

### Standard Response Windows

| Payment Method  | Response Window | Notes                     |
| --------------- | --------------- | ------------------------- |
| **Visa**        | 7-14 days       | From notification date    |
| **Mastercard**  | 7-14 days       | From notification date    |
| **Rupay**       | 7-10 days       | From notification date    |
| **Amex**        | 10-20 days      | Varies by reason code     |
| **Debit Cards** | 7-14 days       | Depends on issuing bank   |
| **UPI**         | 5-7 days        | Shorter window            |
| **Net Banking** | 7-10 days       | Depends on bank           |
| **Wallets**     | 5-10 days       | Varies by wallet provider |

<Callout icon="📘" theme="info">
  **Note:** The exact reply date is always specified in the chargeback notification. Always refer to this date rather than general guidelines.
</Callout>

### Timeline for Chargeback Filing

Customers can file chargebacks within these windows from the transaction date:

| Card Network | Filing Window  |
| ------------ | -------------- |
| Visa         | Up to 120 days |
| Mastercard   | Up to 120 days |
| Rupay        | Up to 90 days  |
| Amex         | Up to 120 days |

***

## Managing Chargebacks

You can manage chargebacks through two methods:

### 1. PayU Dashboard

Best for: Low volume, manual review needed

* Navigate to **Dashboard → Chargebacks**
* View all chargeback cases
* Accept or contest chargebacks
* Upload supporting documents
* Track case status

For detailed instructions, refer to [Chargeback Dashboard](/docs/chargeback-dashboard).

### 2. Chargeback APIs

Best for: High volume, automated systems

| API                                                            | Purpose                          |
| -------------------------------------------------------------- | -------------------------------- |
| [Read Chargeback API](/reference/read-chargeback-api)          | Fetch chargeback details         |
| [Read Reasons API](/reference/read-reasons-api)                | Get chargeback reason codes      |
| [Accept Chargeback API](/reference/accept-chargeback-api)      | Accept a chargeback              |
| [Contest Chargeback API](/reference/contest-chargeback-api)    | Contest with documents           |
| [Accept/Contest API](/reference/accept-contest-chargeback-api) | Combined accept/contest endpoint |

For API integration details, refer to [Chargeback APIs](/docs/chargeback-apis).

### 3. Webhooks

Get real-time notifications for chargeback events. Configure webhooks to receive:

* New chargeback notifications
* Status updates
* Resolution notifications

For webhook setup, refer to [Webhooks for Chargeback](/docs/webhooks-for-chargeback).

***

## Financial Impact of Chargebacks

### Direct Costs

| Cost Type              | Description                   | Typical Amount      |
| ---------------------- | ----------------------------- | ------------------- |
| **Transaction Amount** | Full disputed amount          | 100% of transaction |
| **Chargeback Fee**     | Processing fee per chargeback | ₹200 - ₹500         |
| **Arbitration Fee**    | If case goes to arbitration   | ₹2,000 - ₹5,000     |

### Settlement Impact

When a chargeback is received:

1. **Immediate Hold:** The disputed amount is held from your next settlement
2. **If Won:** Amount is released back to your settlement
3. **If Lost:** Amount is permanently deducted

### Chargeback Ratio

Your chargeback ratio is calculated as:

```
Chargeback Ratio = (Number of Chargebacks / Total Transactions) × 100
```

| Ratio     | Status    | Consequence             |
| --------- | --------- | ----------------------- |
| \< 0.5%   | Healthy   | No action needed        |
| 0.5% - 1% | Warning   | Review fraud prevention |
| 1% - 2%   | High Risk | May face restrictions   |
| > 2%      | Critical  | Account suspension risk |

<Callout icon="⚠️" theme="warn">
  **Warning:** Consistently high chargeback ratios can result in:

  * Higher transaction fees
  * Reserve requirements
  * Account suspension
  * Placement on card network monitoring programs
</Callout>

***

## Next Steps

| Topic                                                    | Description                         |
| -------------------------------------------------------- | ----------------------------------- |
| [Chargeback Reason Codes](/docs/chargeback-reason-codes) | Understand why chargebacks occur    |
| [Contesting Chargebacks](/docs/contesting-chargebacks)   | How to effectively contest disputes |
| [Chargeback Prevention](/docs/chargeback-prevention)     | Strategies to reduce chargebacks    |
| [Chargeback APIs](/docs/chargeback-apis)                 | API integration guide               |
| [Chargeback Dashboard](/docs/chargeback-dashboard)       | Dashboard user guide                |

***

## FAQs

### How quickly should I respond to a chargeback?

Respond as soon as possible, but always before the Reply Date. We recommend responding within 3-5 days to allow time for any issues with document submission.

### Can I contest a chargeback after accepting it?

No, once you accept a chargeback, the decision is final and cannot be reversed.

### What happens if I miss the Reply Date?

The case is automatically closed in favor of the customer, and the chargeback amount is deducted from your settlement.

### How long does resolution take?

Typically 30-90 days from the contest date, depending on the card network and complexity of the case.

### Can a customer file multiple chargebacks for the same transaction?

No, only one chargeback can be filed per transaction. However, if the initial chargeback is resolved in your favor, the customer may escalate to pre-arbitration.

***

_Last updated: December 2024_
