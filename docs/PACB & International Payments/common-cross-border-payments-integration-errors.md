---
title: Common Cross-Border Payments Integration Errors
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">
  Diagnose and resolve common Cross-Border Payments - Import (PACB) integration errors: invalid hash, missing buyer KYC, 10-day invoice upload holds, transaction limits, and callback reconciliation.
</Banner>

Diagnose and resolve common issues with your PayU Cross-Border Payments - Import (PACB) integration. Cross-border outward remittance transactions carry specific regulatory checks (RBI PACB/OPGSP guidelines) alongside standard payment validations. Use this guide to identify the root cause of errors and apply the recommended fixes.

***

## Common PACB Integration Errors

<Accordion title="1. Invalid Hash / Hash Validation Failed" icon="fa-shield-halved">
  ### What Happened

  PayU rejects the transaction immediately or displays an **"Invalid Hash"** error on the checkout page. The transaction does not proceed to the payment network or bank.

  ### Common Causes

  - **Missing or Misplaced PACB UDFs in Hash**: For PACB, `udf1` (PAN), `udf2`, `udf3` (DOB), `udf4` (Seller Name), and `udf5` (Invoice ID) must be positioned in exact sequential order.
  - **Pipe Delimiter Errors**: Missing pipe (`|`) separators, especially when optional UDFs or empty fields are skipped.
  - **Optional Extended Parameters (**`udf_params`**,&#x20;**`buyer_type_business`**)**: If your account passes extended parameters like `udf_params` (e.g. IEC code) or `buyer_type_business`, they must be hashed **after** the salt in the exact documented sequence.
  - **Whitespace & Encoding**: Leading or trailing whitespace in the PAN (`udf1`), Date of Birth (`udf3`), or Invoice ID (`udf5`).
  - **Incorrect Hashing Algorithm**: Using SHA-256 or MD5 instead of SHA-512.
  - **Client-Side Hash Generation**: Calculating the hash in the browser or mobile app using exposed credentials.

  ### Recommended Fix

  1. Generate the hash exclusively on your secure backend server using **SHA-512**.
  2. For standard PACB one-time transactions, follow the standard PayU hash sequence:
     ```text
     sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
     ```
  3. When passing extended PACB parameters, append them after the salt:
     ```text
     sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|udf_params|buyer_type_business)
     ```
  4. Ensure all empty UDF placeholders (`udf6` through `udf10`) are preserved with exact pipes (`||||||`).
  5. Sanitize and trim all parameter values before hashing.
</Accordion>

<Accordion title="2. Missing or Invalid Buyer KYC Parameters (PAN / DOB)" icon="fa-id-card">
  ### What Happened

  The payment request is rejected by PayU during initiation with an error indicating missing or invalid buyer KYC parameters (such as `Invalid UDF1`, `Invalid PAN`, or `Invalid Date of Birth`).

  ### Common Causes

  - **Missing&#x20;**`udf1`**&#x20;(PAN)**: Under RBI import guidelines, an Indian resident buyer's 10-digit Permanent Account Number (PAN) is mandatory for outward remittance reconciliation.
  - **Malformed PAN Format**: PAN does not follow the standard Indian Income Tax format (`[A-Z]{5}[0-9]{4}[A-Z]{1}`) or contains spaces/lowercase letters.
  - **Invalid&#x20;**`udf3`**&#x20;Date of Birth Format**: The buyer's date of birth is passed in an unrecognised format (e.g. `YYYY-MM-DD` or `DD/MM/YYYY`) instead of the required `DD-MM-YYYY`.
  - **Missing Seller Name (**`udf4`**)**: For payment aggregator models, the actual overseas beneficiary / seller name is omitted in `udf4`.
  - **Missing Invoice ID (**`udf5`**)**: An invoice identifier is not supplied at transaction initiation.

  ### Recommended Fix

  - Validate the buyer's PAN client-side and server-side before initiating payment:
    ```javascript
    const panRegex = /^[A-Z]{5}[0-9]{4}[A-Z]{1}$/;
    if (!panRegex.test(buyerPan.trim().toUpperCase())) {
      throw new Error("Invalid PAN format. Must be 10 uppercase alphanumeric characters.");
    }
    ```
  - Format the buyer's Date of Birth strictly as `DD-MM-YYYY` (e.g. `15-08-1985`).
  - Always populate `udf4` with the registered overseas seller/merchant entity name.
  - Ensure `udf5` contains the exact commercial invoice number issued for this purchase.
</Accordion>

<Accordion title="3. Transaction Limit Exceeded (Regulatory Cap)" icon="fa-scale-unbalanced">
  ### What Happened

  The transaction is rejected with an error indicating amount limit exceeded, or the payment method is disabled for the requested transaction amount.

  ### Common Causes

  - **Per-Transaction Cap Exceeded on Checkout**: Under RBI PACB/OPGSP outward remittance regulations, retail checkout payment methods (Cards, NetBanking, and UPI) are capped at **₹2,50,000 (INR 2.5 Lakh)** per transaction.
  - **Attempting > ₹2.5 Lakh on Cards or UPI**: Passing an order amount exceeding ₹2,50,000 through the standard `_payment` checkout API causes immediate rejection.
  - **Virtual Account Wire Limit Exceeded**: For local wire transfers via Virtual Account (NEFT/RTGS), the statutory cap is **₹25,00,000 (INR 25 Lakh)**. Attempts above this limit fail.

  ### Recommended Fix

  - Implement cart/checkout amount gating in your order management system:
    - **Orders up to ₹2,50,000**: Route to standard checkout (Cards, NetBanking, UPI).
    - **Orders from ₹2,50,001 up to ₹25,00,000**: Route exclusively to **Virtual Account Local Wire Transfers** (NEFT/RTGS).
    - **Orders above ₹25,00,000**: Cannot be processed through PACB. Advise the buyer to use standard direct bank wire remittance (A2 form flow).
  - Clearly display transaction limits to buyers before initiating checkout to prevent checkout abandonment.
</Accordion>

<Accordion title="4. Settlements On Hold (10-Day Invoice Compliance Failure)" icon="fa-clock-rotate-left">
  ### What Happened

  Transactions process successfully and payments are captured, but your merchant dashboard shows settlement status as **"On Hold"** or subsequent payout disbursements are halted by the Authorised Dealer (AD-1) bank.

  ### Common Causes

  - **10-Day Invoice Deadline Expired**: Under RBI PACB regulations, commercial invoices must be submitted to PayU's AD-1 partner bank within **10 calendar days** of transaction capture.
  - **Missing Airway Bill (AWB) for Physical Goods**: For physical goods imports, both the commercial invoice **and** the carrier Airway Bill / Bill of Lading must be provided. Uploading only the invoice causes regulatory rejection.
  - **Mismatched Invoice ID**: The invoice number uploaded does not match the `udf5` invoice identifier submitted during payment initiation.
  - **Unreadable or Incomplete PDF**: Uploaded invoice documents are corrupt, unreadable, or missing mandatory details (buyer name, seller name, itemized description, currency, and amount).

  ### Recommended Fix

  1. Automate invoice upload via PayU's **Upload Invoice API** as soon as the payment webhook confirms `status=success`.
  2. For physical shipments, trigger the AWB upload call immediately once the logistics carrier generates the consignment tracking note.
  3. Verify that the invoice ID passed in the API matches the `udf5` value passed during checkout initiation.
  4. Implement an automated alert within your system at **T+5 days** for any transaction lacking verified invoice documentation, well before the 10-day AD bank hard stop.
</Accordion>

<Accordion title="5. Reverse Hash Mismatch on Payment Callback" icon="fa-arrows-rotate">
  ### What Happened

  The customer completes payment, but your backend rejects the callback notification at `surl` or `furl` because your calculated reverse hash does not match the `hash` field returned in PayU's response.

  ### Common Causes

  - **Forward Hash Formula Used Instead of Reverse**: Attempting to verify the response using the request hash formula.
  - **Incorrect UDF Sequence in Reverse Hash**: The reverse hash requires UDF fields in reverse order: `udf5` down to `udf1`.
  - **Missing&#x20;**`additional_charges`: When surcharges or payment method fees apply, PayU includes `additional_charges` in the reverse hash formula. Omitting it causes verification failure.
  - **Status Value Case Sensitivity**: Using uppercase or modified status strings instead of the verbatim response `status` (e.g. `success`, `failure`, `pending`).
  - **Incorrect Environment Salt**: Verifying production responses with sandbox credentials or vice versa.

  ### Recommended Fix

  1. Standard reverse hash formula:
     ```text
     sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
     ```
  2. When `additional_charges` is present in the callback payload:
     ```text
     sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
     ```
  3. Maintain exact field values without trimming or URL-decoding modifications during hash verification.
  4. Always respond with HTTP `200 OK` once the reverse hash is verified.
</Accordion>

<Accordion title="6. UPI Autopay PACB Formatting Errors" icon="fa-repeat">
  ### What Happened

  UPI Autopay mandate registration (consent) or recurring debit transactions fail with validation errors or unmapped exceptions.

  ### Common Causes

  - **Incorrect UDF Delimiter in Autopay**: Unlike one-time payments where UDFs are distinct strings, PACB UPI Autopay requires pipe-concatenated values:
    - `udf1`: `PAN||DOB` (e.g. `ABCDE1234F||22-08-1972`)
    - `udf3`: `InvoiceID||MerchantName` (e.g. `INV-9021||GlobalSaaS`)
    - `udf4`: Must **not** be passed for UPI Autopay.
  - **Pre-Debit Notification Gap \< 24 Hours**: NPCI mandates that a pre-debit notification (PDN) must be triggered at least **24 hours** prior to executing the recurring debit.
  - **Amount Exceeding Mandate Cap**: Attempting to execute a recurring transaction for an amount higher than the approved mandate `maxAmount`.
  - **Mismatched Pre-Debit and Debit Amount**: The amount executed during recurring debit does not match the exact amount specified in the pre-debit notification.

  ### Recommended Fix

  - Verify Autopay UDF formats before initiating mandate registration.
  - Schedule pre-debit notifications between 24 and 48 hours prior to debit execution.
  - Ensure the recurring debit amount strictly equals the pre-notified amount and is within the mandate limit.
</Accordion>

<Accordion title="7. Virtual Account Wire Transfer Reconciliation Delays" icon="fa-building-columns">
  ### What Happened

  Buyer transfers funds via NEFT or RTGS, but the order remains in `pending` state and no payment success webhook is received.

  ### Common Causes

  - **Amount Mismatch**: Buyer transferred an amount different from the exact invoice amount (e.g. deducting bank wire transfer charges or rounding off).
  - **Remittance to Inactive/Expired Virtual Account**: The virtual account was closed or the validity window elapsed before the bank wire completed.
  - **NEFT/RTGS Batch Clearing Latency**: NEFT operates in half-hourly batches; RTGS settles during banking hours. Transactions outside clearing windows take longer to confirm.
  - **Payer Name Discrepancy**: Remittance originated from an unverified third-party account rather than the registered buyer.

  ### Recommended Fix

  - Explicitly instruct buyers to transfer the **exact invoice amount without deduction**.
  - Set a generous validity window (e.g. 48–72 hours) on dynamically generated Virtual Accounts.
  - Listen for the asynchronous Virtual Account collection webhook (`status=success`) rather than polling prematurely.
  - If a wire is pending beyond 24 banking hours, initiate an inquiry with the Unique Transaction Reference (UTR) number provided by the buyer.
</Accordion>

***

## Still Having Issues?

If your PACB integration issue persists after verifying the fixes above, contact PayU Merchant Support with the following diagnostic information:

<HTMLBlock>{`
<div style="overflow-x: auto;">
  <table style="width: 100%; border-collapse: collapse; margin-top: 1rem;">
    <thead>
      <tr style="background-color: #f3f4f6;">
        <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Field</th>
        <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Description</th>
        <th style="border: 1px solid #d1d5db; padding: 8px 12px; text-align: left;">Example Value</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>txnid</code></td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Your unique merchant transaction ID.</td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>PACB_TXN_987654321</code></td>
      </tr>
      <tr>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>mihpayid</code></td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;">PayU payment identifier (if transaction initiated).</td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>403993715523123456</code></td>
      </tr>
      <tr>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>Timestamp</code></td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Exact date and time of the attempt (IST / UTC).</td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>2026-11-03 14:35:10 IST</code></td>
      </tr>
      <tr>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>Hash String</code></td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Pre-hash string with salt masked (<strong>Never send your raw salt</strong>).</td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>key|txnid|amount|...|udf5||||||&lt;SALT_MASKED&gt;</code></td>
      </tr>
      <tr>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>Invoice ID (udf5)</code></td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Commercial invoice number associated with the attempt.</td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>INV-2026-8812</code></td>
      </tr>
      <tr>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>Error Message / Code</code></td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;">Exact error response, status code, or screenshot.</td>
        <td style="border: 1px solid #d1d5db; padding: 8px 12px;"><code>E308: Transaction limit exceeded</code></td>
      </tr>
    </tbody>
  </table>
</div>
`}</HTMLBlock>

<Callout icon="🔒" theme="warn">
  ### **Confidentiality Notice:**

  Never include your merchant **Salt**, API secret keys, full credit card numbers, or unmasked buyer PAN in support tickets, emails, or public issue trackers.
</Callout>

***

## What's Next?

<Cards columns="3">
  <Card title="PACB Best Practices" href="cross-border-payments-import-best-practices">
    Implement compliance, UX, and settlement best practices
  </Card>

  <Card title="PACB Workflow" href="workflow-for-cross-border-payments-import">
    Understand the end-to-end import payment and settlement lifecycle
  </Card>

  <Card title="PACB FAQs" href="faqs-for-cross-border-payments">
    Browse answers to frequently asked integration questions
  </Card>
</Cards>
