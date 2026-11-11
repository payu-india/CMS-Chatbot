---
title: How Merchant Hosted Checkout Works?
deprecated: false
hidden: true
metadata:
  robots: index
---
This section details the architectural transaction lifecycle and sequence workflow of PayU's Merchant Hosted Checkout.

***

## Environment Endpoints

| Environment           | Purpose                             | Payment Initiation URL (`_payment`) | Post-Service & Verification URL                        |
| :-------------------- | :---------------------------------- | :---------------------------------- | :----------------------------------------------------- |
| **Test (Sandbox)**    | Integration testing & mock payments | `<redacted URL>`                    | `<redacted URL>`                                       |
| **Production (Live)** | Real customer payments              | `https://secure.payu.in/_payment`   | `https://info.payu.in/merchant/postservice.php?form=2` |

***

## Architecture & Sequence Flow

```
Customer Browser / App            Merchant Server                      PayU Gateway                       Bank ACS / UPI App
       │                                │                                   │                                     │
       │─── 1. Selects Payment Method ─▶│                                   │                                     │
       │    (Enters Payment Data)       │                                   │                                     │
       │                                │─── 2. Compute SHA-512 Hash ──────▶│                                     │
       │                                │    (key|txnid|amount|...|salt)    │                                     │
       │◀── 3. Return Hash & Params ────│                                   │                                     │
       │                                                                    │                                     │
       │─── 4. Auto-submit Form POST to PayU _payment ─────────────────────▶│                                     │
       │    (Target: <redacted URL>)                         │                                     │
       │                                                                    │─── 5. Route to Bank/ACS ───────────▶│
       │◀── 6. Redirect to Bank OTP / ACS Authentication Screen ───────────┴─────────────────────────────────────┤
       │                                                                   │                                      │
       │─── 7. Customer submits OTP / Approves UPI Intent ─────────────────┼─────────────────────────────────────▶│
       │                                                                   │◀── 8. Bank Auth Success/Fail ────────│
       │                                                                    │                                     │
       │◀── 9. Browser POST redirect to Merchant surl/furl ─────────────────│                                     │
       │                                                                    │─── 10. Server-to-Server Webhook ───▶│ (Merchant Server)
       │─── 11. Customer redirected to Order Confirmation Page ────────────▶│                                     │
       │                                │                                   │                                     │
       │                                │─── 12. Double Verification: POST verify_payment ───────────────────────▶│
       │                                │    (Target: <redacted URL>)       │
       │                                │◀── 13. Confirm Captured Status ───│                                     │
```

***

## The 6-Stage Transaction Lifecycle

1. **Step 1: Customer Initiates Payment on Merchant UI**<br />The customer selects an instrument (Card, UPI, Net Banking, Wallet) on your custom checkout page and provides required payment details.

2. **Step 2: Server-Side Request Hash Generation**<br />Your frontend calls your backend server with the transaction parameters. Your backend server generates a cryptographic SHA-512 request hash using your private Merchant Salt.

3. **Step 3: Browser Submits Form POST to PayU (**`_payment`**)**<br />The customer's browser auto-submits a standard HTML form POST to:
   * **Test Environment:** `<redacted URL>`
   * **Production Environment:** `https://secure.payu.in/_payment`

4. **Step 4: Two-Factor Authentication (Bank ACS / UPI App)**<br />PayU routes the transaction to the issuing bank's Access Control Server (ACS) for OTP authentication or launches the user's UPI mobile application for intent authorization.

5. **Step 5: Browser Callback Redirect (**`surl`**/**`furl`**) & Reverse Hash Check**<br />Upon completion, PayU posts the transaction status back to the customer's browser, redirecting them to your `surl` (Success URL) or `furl` (Failure URL). Your backend recalculates the reverse hash to ensure data authenticity.

6. **Step 6: Server-to-Server Verification (**`verify_payment`**)**<br />Regardless of whether the browser reached `surl`, your backend executes an independent S2S query via the `verify_payment` API to verify the captured transaction state directly against PayU's payment database:
   * **Test Endpoint:** `POST <redacted URL>`
   * **Production Endpoint:** `POST https://info.payu.in/merchant/postservice.php?form=2`
