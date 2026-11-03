---
title: Cross-Border Payments - Best Practices
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">
  Compliance, reliability, conversion, and operational best practices for PayU Cross-Border Payments - Import (PACB): buyer KYC validation, 10-day invoice automation, smart transaction routing, and resilient callbacks.
</Banner>

Cross-border import payments under RBI's Online Payment-Gateway Service Provider (OPGSP) and Payment Aggregator Cross-Border (PACB) guidelines require both frictionless merchant checkout and strict regulatory compliance. These best practices guide you through building a high-converting, resilient, and fully compliant PACB integration.

To apply these practices, your basic PACB payment integration should already be configured and verified in Sandbox.

***

## 1. Regulatory KYC & Conversion UX

<Accordion title="1.1 Pre-Validate Buyer PAN & Date of Birth at Checkout" icon="fa-id-card">
  For outward remittances from India, the Reserve Bank of India mandates collection of the Indian resident buyer's **Permanent Account Number (PAN)** and **Date of Birth (DOB)**. If invalid details reach PayU's payment gateway, the transaction is rejected immediately.

  ### Recommended Practice

  - Validate PAN format on your frontend checkout form before allowing the customer to proceed:
    ```javascript
    // Standard 10-character Indian PAN format
    const isValidPAN = (pan) => /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/.test(pan.trim().toUpperCase());
    ```
  - Format Date of Birth strictly as `DD-MM-YYYY` (e.g. `24-07-1988`). Provide a date-picker UI rather than freeform text input to eliminate formatting errors.
  - Pre-fill PAN and DOB from your saved customer profile for returning buyers to minimize checkout friction.

  <Callout icon="💡" theme="info">
    ### **Tips:**

    Always sanitize input by converting PAN to uppercase and stripping leading/trailing whitespace before including it in `udf1` and your request hash string.
  </Callout>
</Accordion>

<Accordion title="1.2 Collect Complete Indian Billing Addresses for Fraud Detection" icon="fa-map-location-dot">
  Passing complete billing address information significantly reduces transaction decline rates and assists in chargeback defense for cross-border card transactions.

  ### Recommended Parameters to Populate

  <HTMLBlock>{`
  <div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
      <thead>
        <tr style="background-color: #f3f4f6;">
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Parameter</th>
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Recommended Value</th>
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Regulatory & Risk Impact</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>country</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>"IN"</code> (ISO 3166-1 alpha-2)</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Validates outward remittance jurisdiction.</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>zipcode</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">6-digit Indian Postal PIN Code (e.g. <code>"560001"</code>)</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Matched against card issuer AVS and GST jurisdiction.</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>state</code> & <code>city</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">State name and City (e.g. <code>"Karnataka"</code>, <code>"Bengaluru"</code>)</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Required for commercial invoice reconciliation.</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>address1</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Street name, building, or premise</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Ensures full KYC alignment with the physical shipping bill.</td>
        </tr>
      </tbody>
    </table>
  </div>
  `}</HTMLBlock>
</Accordion>

<Accordion title="1.3 Prevent Duplicate Submissions With Visual Loading State" icon="fa-spinner">
  Cross-border redirection forms must prevent repeated submissions caused by impatient taps on slow mobile networks.

  ```html
  <!doctype html>
  <html>
  <head>
    <style>
      #loading-overlay {
        display: none;
        position: fixed;
        inset: 0;
        background: rgba(255, 255, 255, 0.9);
        text-align: center;
        padding-top: 20%;
        font-family: sans-serif;
      }
    </style>
  </head>
  <body onload="submitPaymentForm()">
    <form id="pacb-payment-form" name="payu" method="post" action="https://secure.payu.in/_payment">
      <input type="hidden" name="key" value="YOUR_MERCHANT_KEY">
      <input type="hidden" name="txnid" value="PACB-78245-a3f9">
      <input type="hidden" name="amount" value="12500.00">
      <input type="hidden" name="productinfo" value="Overseas Software License">
      <input type="hidden" name="firstname" value="Rahul">
      <input type="hidden" name="email" value="rahul.verma@example.com">
      <input type="hidden" name="phone" value="9876543210">
      <input type="hidden" name="udf1" value="ABCDE1234F">
      <input type="hidden" name="udf3" value="15-08-1985">
      <input type="hidden" name="udf4" value="GlobalTech LLC">
      <input type="hidden" name="udf5" value="INV-2026-9012">
      <input type="hidden" name="surl" value="<redacted URL>">
      <input type="hidden" name="furl" value="<redacted URL>">
      <input type="hidden" name="hash" value="YOUR_CALCULATED_HASH">
    </form>

    <div id="loading-overlay">
      <h3>Securing your cross-border payment…</h3>
      <p>Redirecting to PayU. Please do not refresh or press Back.</p>
    </div>

    <script>
      function submitPaymentForm() {
        document.getElementById('loading-overlay').style.display = 'block';
        document.forms['payu'].submit();
      }
    </script>
  </body>
  </html>
  ```
</Accordion>

***

## 2. Regulatory 10-Day Invoice Automation

<Accordion title="2.1 Automate Invoice Upload via API Immediately Upon Payment Capture" icon="fa-file-invoice-dollar">
  Under RBI guidelines, the Authorised Dealer (AD-1) partner bank requires proof of cross-border commercial transactions within **10 calendar days**. If invoices are not received within this window, the bank is legally required to place subsequent merchant payout settlements on hold.

  ### Automated Architecture

  ```text
  Customer Completes Payment
             │
             ▼
  PayU Webhook (status=success) ───────────► Your Server
                                                   │
  Generate PDF Invoice ◄───────────────────────────┘
             │
             ▼
  PayU Upload Invoice API (POST /invoice/upload)
             │
             ▼
  AD-1 Bank Clearance Verified (Status: Settled on Schedule)
  ```

  ### Best Practice Guidelines:

  - **Never rely on manual portal uploads** for high-volume transactions. Integrate PayU's **Invoice Upload API** directly into your post-payment processing pipeline.
  - Match the uploaded invoice number verbatim with the `udf5` parameter passed during initial checkout.
  - For digital goods or SaaS subscriptions, generate and push the digital tax invoice within minutes of receiving the payment success webhook.
</Accordion>

<Accordion title="2.2 Dual-Document Compliance for Physical Goods (Invoice + AWB)" icon="fa-truck-plane">
  If your store exports physical merchandise into India, the AD bank requires two distinct regulatory documents:

  1. **Commercial Invoice**: Detailing seller, buyer, itemized products, and total INR/foreign currency value.
  2. **Airway Bill (AWB) or Bill of Lading**: Demonstrating proof of international shipment and customs entry.

  ### Recommended Flow:

  - Upload the commercial invoice immediately at payment confirmation (`T+0`).
  - Listen for the logistics courier shipment creation event (`T+1` to `T+3`) and immediately push the corresponding Airway Bill PDF to PayU.
  - Implement a **T+5 day automated escalation alert**: If any physical order has not uploaded an AWB by Day 5, trigger an alert to your operations team to resolve before the 10-day settlement hold penalty.
</Accordion>

***

## 3. Smart Transaction Routing & Limit Management

<Accordion title="3.1 Enforce Per-Transaction Limits at the Checkout Tier" icon="fa-traffic-light">
  RBI guidelines impose strict per-transaction caps on cross-border outward remittances depending on the payment instrument used.

  <HTMLBlock>{`
  <div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
      <thead>
        <tr style="background-color: #f3f4f6;">
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Cart Amount Range</th>
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Recommended Channel</th>
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Payment Methods Presented</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><strong>Up to ₹2,50,000</strong></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Standard PACB Checkout</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Credit Cards, Debit Cards, NetBanking, UPI Intent</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><strong>₹2,50,001 to ₹25,00,000</strong></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Virtual Account Wire Transfer</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">NEFT / RTGS Local Bank Transfer (Unique Virtual IBAN/IFSC)</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><strong>Above ₹25,00,000</strong></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Direct Bank Wire (Form A2)</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Direct TT wire transfer through commercial bank channels</td>
        </tr>
      </tbody>
    </table>
  </div>
  `}</HTMLBlock>

  <Callout icon="🛡️" theme="warn">
    ### **Business-to-Business (B2B) Purchases:**

    Under PACB regulations, B2B payments using `buyer_type_business` are permitted **exclusively for software, SaaS, and digital services**. Physical goods merchants must not accept B2B transactions through PACB.
  </Callout>
</Accordion>

***

## 4. Transaction ID Strategy & Safe Retries

<Accordion title="4.1 Generate Collision-Proof, Traceable Transaction IDs" icon="fa-fingerprint">
  Every cross-border payment attempt requires a strictly unique `txnid`. Reusing a `txnid` causes immediate rejection or returns stale status data.

  ### Recommended Pattern

  Combine an application prefix, internal order reference, and a short unique random suffix:

  - **Format**: `{prefix}-{order_id}-{attempt_suffix}`
  - **Example**: `PACB-ORD9812-a1b2`
  - **Rules**:
    - Maximum 25 characters
    - Alphanumeric and hyphens only; no spaces, slashes, or special characters
    - Never include PII (e.g. buyer email or PAN) in the `txnid`
</Accordion>

<Accordion title="4.2 Design a Safe Payment Retry Flow" icon="fa-arrows-rotate">
  When an international payment attempt fails (e.g. 3DS authentication failure or bank decline):

  1. Record the failed attempt under `PaymentAttempt` linked to your internal order record.
  2. When the customer clicks **Try Again**, generate a brand-new `txnid` (e.g. `PACB-ORD9812-c3d4`).
  3. Recompute the SHA-512 request hash using the new `txnid`.
  4. Submit a fresh request to PayU.
  5. Mark the order as paid only when one payment attempt receives `status=success` verified by reverse hash.
</Accordion>

***

## 5. Callback Resilience & Verification

<Accordion title="5.1 Use Server-to-Server Webhooks as the Single Source of Truth" icon="fa-bell">
  Browser redirects to `surl` and `furl` depend on the customer's device staying connected through 3DS authentication. On mobile networks, drops and app switches frequently disrupt browser callbacks.

  ### Architecture:

  - Treat the asynchronous server-to-server **Webhook** as your primary fulfillment trigger.
  - Treat the `surl` browser redirect purely as a UX routing mechanism to show the "Order Confirmed" screen.
  - Implement idempotency: ensure processing the same webhook or callback twice does not result in duplicate order fulfillment or double provisioning.
  - Always respond to PayU webhooks immediately with HTTP `200 OK`.
</Accordion>

<Accordion title="5.2 Proactive Reconciliation with Verify Payment API" icon="fa-magnifying-glass-chart">
  If neither a browser callback nor a webhook arrives within **5 to 10 minutes** of redirecting the customer:

  - Run an automated server-side query to PayU's **Verify Payment API** (`verify_payment`).
  - If the status is `success`, update order status to confirmed and trigger the invoice upload.
  - If the status is `failure`, update the order and allow the buyer to retry.
  - If the status is `pending`, maintain pending state and re-poll at 15-minute intervals.
</Accordion>

***

## 6. Error Recovery UX

<Accordion title="6.1 Provide Specific Guidance for Cross-Border Failure Types" icon="fa-circle-exclamation">
  Map the response `unmappedstatus` and error codes to helpful, reassuring customer messages rather than generic error banners:

  <HTMLBlock>{`
  <div style="overflow-x: auto;">
    <table style="width: 100%; border-collapse: collapse; margin-top: 0.5rem;">
      <thead>
        <tr style="background-color: #f3f4f6;">
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Status / Error Code</th>
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Underlying Cause</th>
          <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Customer-Facing Recommended Message</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>failed / E1632</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Card issuer declined transaction.</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">"Your card issuer declined the international transaction. Please enable international/online usage on your card or try another payment method."</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>failed / E308</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Amount exceeds regulatory cap (₹2.5 Lakh).</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">"This order exceeds the online checkout limit of ₹2,50,000. Please select Local Bank Transfer (NEFT/RTGS) to complete your purchase."</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>userCancelled</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Customer cancelled 3DS or closed window.</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">"Your payment was cancelled. Your items are still reserved in your cart if you would like to try again."</td>
        </tr>
        <tr>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>pending</code></td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">NEFT/RTGS wire transfer in progress.</td>
          <td style="border: 1px solid #d1d5db; padding: 8px 12px;">"Your bank transfer has been initiated. We will confirm your order as soon as your funds are cleared by the bank."</td>
        </tr>
      </tbody>
    </table>
  </div>
  `}</HTMLBlock>
</Accordion>

***

## What's Next?

<Cards columns="3">
  <Card title="Errors & Troubleshooting" href="cross-border-payments-import-errors-and-troubleshooting">
    Browse common integration errors, root causes, and fixes
  </Card>

  <Card title="PACB Quick Start" href="cross-border-payments-import-quick-start">
    Run your first PACB test payment in 5 simple steps
  </Card>

  <Card title="Virtual Account Wires" href="virtual-account-based-local-wire-transfers">
    Integrate local NEFT/RTGS wire transfers for high-value orders
  </Card>
</Cards>
