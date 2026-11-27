---
title: Pre-Authorize Payments (Auth and Capture)
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Pre-Authorize Payments (Auth and Capture)
excerpt: Learn how to hold funds at checkout and settle or release them later using PayU Auth and Capture.
deprecated: false
hidden: false
metadata:
  title: Pre-Authorize Payments (Auth and Capture) - PayU Developer Guide
  description: Overview of PayU Auth and Capture (Pre-Authorization) for credit cards, debit cards, UPI One-Time Mandates, and UPI Reserve Pay.
  robots: index
---

## What is Auth & Capture?

**Auth & Capture** (also known as Pre-Authorization, Two-Step Payment, or Authorization Hold) is a payment workflow that separates fund reservation from actual settlement:

1. **Authorization (Hold)**: Verifies the customer's payment instrument and places a temporary hold on the specified funds without debiting them.
2. **Capture (Settlement)**: Debits the held funds (in full or partially) and transfers them to your merchant settlement account once the order, booking, or service is confirmed.
3. **Cancel (Release)**: Releases the held funds back to the customer immediately if the order is cancelled prior to capture.

PayU supports Auth and Capture across **Credit Cards**, **Debit Cards**, **UPI One-Time Mandates (OTM)**, and **UPI Reserve Pay**.

---

## Key Benefits for Merchants

* **Zero TDR on Cancellations**: No Transaction Discount Rate (TDR) or gateway processing fee is charged on authorizations cancelled before capture.
* **Instant Hold Release**: Because funds were never settled, cancelling an authorization releases the hold back to the customer's payment source immediately.
* **Zero Chargeback Risk During Hold**: Pre-authorized transactions carry no chargeback liability until funds are captured.
* **Fulfillment Flexibility**: Reserve funds at order creation, verify stock or calculate metered charges, and capture the exact final amount.

---

## Supported Payment Instruments & Hold Durations

| Payment Instrument | Supported Schemes / Issuers | Maximum Hold Window | Capture Flexibility |
| :--- | :--- | :--- | :--- |
| **Credit Cards** | Visa, Mastercard, American Express | **Up to 7 Days** (Default auto-capture on Day 7) | Full or Single Partial Capture |
| **Debit Cards** | HDFC Bank, ICICI Bank, State Bank of India, Axis Bank, Kotak Mahindra Bank | **Up to 7 Days** (Default auto-capture on Day 7) | Full or Single Partial Capture |
| **UPI One-Time Mandates (OTM)** | Major UPI Apps (Intent & Collect) | **Up to 60 Days** (Configured via validity window) | Full or Partial Capture |
| **UPI Reserve Pay** | Supported UPI handles (Intent & Collect) | **Up to 90 Days** (Customer-authorized block) | Multiple Partial Debits or Single Debit |

---

## Transaction Lifecycle & Rules

```mermaid
sequenceDiagram
    autonumber
    actor Customer
    participant Merchant as Merchant App / Server
    participant PayU as PayU Gateway
    participant Bank as Issuing Bank / UPI PSP

    Customer->>Merchant: 1. Place order (Checkout)
    Merchant->>PayU: 2. POST _payment (pre_authorize=1)
    PayU->>Customer: 3. Render 3DS / UPI PIN Authentication
    Customer->>Bank: 4. Authenticate transaction
    Bank-->>PayU: 5. Hold confirmed / Mandate created
    PayU-->>Merchant: 6. Callback (unmappedstatus=auth, status=success)
    Note over Merchant,PayU: Funds held for up to 7 days (Cards) or 90 days (UPI Reserve Pay)

    alt Order Fulfilled (Capture)
        Merchant->>PayU: 7a. POST capture_transaction (var1=payuid, var3=amount)
        PayU->>Bank: 8a. Settle captured amount; release excess hold
        PayU-->>Merchant: 9a. Capture confirmed (status=1, unmappedstatus=captured)
    else Order Cancelled (Release)
        Merchant->>PayU: 7b. POST cancel_transaction (var1=payuid)
        Bank-->>Customer: 8b. Hold released immediately
        PayU-->>Merchant: 9b. Cancel confirmed (status=1)
    end
```

### Important Processing Rules

1. **Auto-Capture vs. Auto-Cancel**:
   * For card payments, PayU executes **Auto-Capture on Day 7** by default if no capture or cancel call is made.
   * If your business model requires uncaptured authorizations to expire safely, contact your PayU Key Account Manager (KAM) to configure **Auto-Cancel**.
2. **Single Partial Capture Rule (Cards)**:
   * When capturing a partial amount on a card pre-authorization, the remaining held balance is **immediately and permanently released**. You cannot execute a second partial capture against the same card transaction ID.
   * If your business model requires multiple incremental debits against a single reserved hold, integrate **UPI Reserve Pay**.
3. **Cancel vs. Refund**:
   * Use **`cancel_transaction`** only while the transaction is in authorization status (`unmappedstatus=auth`). Reversal is instant with zero TDR.
   * Once a transaction is captured (`unmappedstatus=captured`), you must use the standard Refund API command (`cancel_refund_transaction`).

---

## Industry Use Cases

* **Hospitality & Rentals**: Pre-authorize room tariffs and security deposits during booking or check-in; capture the adjusted bill during checkout.
* **E-Commerce & Flash Sales**: Block funds during high-volume pre-orders or sales; capture once inventory is verified and dispatched.
* **On-Demand & Ride-Hailing**: Block estimated trip or meter charges; capture final fare upon ride completion.
* **Healthcare & Insurance**: Reserve estimated hospitalization charges; capture approved claim balances upon discharge.

---

## Documentation Index

Explore the dedicated implementation guides based on your checkout design:

* **PayU Hosted**:
  * [PayU Hosted Checkout – Pre-Authorize Payment](02-payu-hosted-pre-authorize-payment.md)
  * [UPI Intent OTM – PayU Hosted](06-upi-intent-otm-payu-hosted.md)
  * [UPI Collect OTM – PayU Hosted](08-upi-collect-otm-payu-hosted.md)
* **Merchant Hosted (Seamless)**:
  * [Credit Card – Merchant Hosted Integration](03-credit-card-merchant-hosted-integration.md)
  * [Debit Card – Merchant Hosted Integration](04-debit-card-merchant-hosted-integration.md)
  * [UPI Intent OTM – Merchant Hosted](07-upi-intent-otm-merchant-hosted.md)
  * [UPI Collect OTM – Merchant Hosted](09-upi-collect-otm-merchant-hosted.md)
* **Server-to-Server (Decoupled)**:
  * [S2S Pre-Authorize Payment](05-s2s-pre-authorize-payment.md)
* **Extended Hold (Up to 90 Days)**:
  * [UPI Reserve Pay](10-upi-reserve-pay.md)
* **Lifecycle & Operations**:
  * [Cancel a Pre-Authorized Payment](11-cancel-a-pre-authorized-payment.md)
  * [APIs Used in Auth and Capture Integration](12-apis-used-in-auth-and-capture.md)
  * [Test Integration, Go-Live Checklist, and Troubleshooting](13-test-integration-go-live-checklist-troubleshooting.md)
