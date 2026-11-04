---
title: Troubleshooting & Error Remediation Guide
deprecated: false
hidden: true
metadata:
  robots: index
---
This section maps common integration failures, API validation errors, and operational settlement holds encountered in PayU Cross-Border Payments – Import (PACB) directly to specific, actionable technical fixes.

***

## Diagnostic Decision Tree

Use the flowchart below to identify the failure point across the cross-border transaction lifecycle:

```mermaid
flowchart TD
    Start([Integration Issue Occurs]) --> Phase{At what stage did the failure occur?}

    Phase -->|Checkout Initiation| InitIssue{Error Type / Code}
    InitIssue -->|Invalid Hash / E000 Hash Fail| H1[1. Fix Hash Delimiters & Empty Pipes]
    InitIssue -->|Invalid PAN or DOB Format| H2[2. Validate 10-char PAN & DD-MM-YYYY DOB]
    InitIssue -->|Regulatory Limit Exceeded / E308| H3[3. Route: <= ₹2.5L Checkout vs <= ₹25L VA]
    InitIssue -->|B2B Purchase Flag Rejected| H4[4. Remove buyer_type_business for non-SaaS]

    Phase -->|Callback or Webhook| CallIssue{Callback Issue}
    CallIssue -->|Reverse Hash Signature Mismatch| H5[5. Factor in additional_charges & Inverted UDFs]
    CallIssue -->|UPI Autopay Validation Failure| H6[6. Format udf1 as PAN||DOB & udf3 as Inv||Seller]
    CallIssue -->|Card Declined / E1632| H7[7. Ensure Complete Indian Billing Address]

    Phase -->|Post-Payment & Payout| PostIssue{Settlement Issue}
    PostIssue -->|Settlements On Hold| H8[8. Verify 10-Day Commercial Invoice & AWB Filing]
    PostIssue -->|Virtual Account Wire Delayed| H9[9. Reconcile Exact Remittance Amount & Bank Window]
```

***

## Master PACB Error Map

<HTMLBlock>{`
<div style="overflow-x: auto;">
  <table>
    <thead>
      <tr>
        <th style="width: 18%;">Error Symptom / Code</th>
        <th style="width: 20%;">Root Cause</th>
        <th style="width: 24%;">Exact Parameter Check</th>
        <th style="width: 38%;">Actionable Resolution</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><strong>Invalid Hash / Hash Validation Failed</strong></td>
        <td>Parameter ordering mismatch, missing empty pipes, or inclusion of secret salt in request body.</td>
        <td>Check that 6 empty pipes (<code>||||||</code>) sit between <code>udf5</code> and <code>SALT</code>.</td>
        <td>
          Reconstruct the hash using the exact sequence:<br>
          <code>sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)</code><br>
          • Ensure <code>SALT</code> is kept strictly on your server backend.<br>
          • Trim leading/trailing whitespace from all parameter strings.<br>
          • Ensure <code>amount</code> matches exactly to two decimal places (e.g. <code>1500.00</code>).
        </td>
      </tr>
      <tr>
        <td><strong>Missing or Invalid Buyer KYC</strong></td>
        <td>Buyer PAN or Date of Birth missing, malformed, or failing regex validation.</td>
        <td>
          • <code>udf1</code> != 10-char PAN<br>
          • <code>udf3</code> != <code>DD-MM-YYYY</code>
        </td>
        <td>
          • Validate <code>udf1</code> on your frontend checkout form using regex: <code>^[A-Z]{5}[0-9]{4}[A-Z]{1}$</code>.<br>
          • Ensure <code>udf3</code> uses hyphens in <code>DD-MM-YYYY</code> format (e.g. <code>15-08-1988</code>). Do not pass slashes (<code>/</code>) or timestamps.<br>
          • Ensure <code>firstname</code> matches the legal entity name registered on the Indian PAN record.
        </td>
      </tr>
      <tr>
        <td><strong>UPI Autopay Delimiter Error</strong></td>
        <td>Passing single-string values in <code>udf1</code> or sending <code>udf4</code> in mandate consent requests.</td>
        <td>
          • <code>udf1</code> missing double pipe delimiter (<code>||</code>)<br>
          • <code>udf4</code> passed in request body
        </td>
        <td>
          In UPI Autopay consent:<br>
          • Format <code>udf1 = PAN||DOB</code> (e.g. <code>ABCDE1234F||15-08-1988</code>).<br>
          • Format <code>udf3 = InvoiceID||MerchantName</code> (e.g. <code>INV-98765||GlobalTechLtd</code>).<br>
          • <strong>Do NOT send <code>udf4</code></strong>; keep it empty to prevent field collision.<br>
          • Ensure <code>api_version=7</code> is passed.
        </td>
      </tr>
      <tr>
        <td><strong>Transaction Limit Exceeded (<code>E308</code>)</strong></td>
        <td>Checkout cart amount exceeds the RBI PACB regulatory ceiling of ₹2,50,000 per transaction.</td>
        <td><code>amount &gt; 250000.00</code> on Cards, NetBanking, or UPI Intent.</td>
        <td>
          Implement tiered routing logic on your server:<br>
          • Orders up to ₹2,50,000: Route to standard checkout (Cards / NetBanking / UPI).<br>
          • Orders from ₹2,50,001 to ₹25,00,000: Route customer to <strong>Virtual Account Local Wire Transfers (NEFT / RTGS)</strong>.<br>
          • Orders exceeding ₹25,00,000: Must be settled via direct commercial bank inward remittance (A2).
        </td>
      </tr>
      <tr>
        <td><strong>Settlement On Hold (10-Day Hold)</strong></td>
        <td>Commercial invoice PDF not submitted within the mandatory 10-day post-payment window.</td>
        <td>Invoice ID in trade ledger does not match <code>udf5</code>.</td>
        <td>
          • Call <code>POST /merchant/invoice/upload</code> supplying <code>txnid</code>, <code>invoiceId</code> (matching <code>udf5</code>), and the commercial invoice PDF.<br>
          • For physical goods, make two uploads: commercial invoice at T+0 and carrier Airway Bill (AWB) upon dispatch.<br>
          • Once verified by the AD-1 Category Bank, the settlement hold is automatically released.
        </td>
      </tr>
      <tr>
        <td><strong>B2B Flag Rejected</strong></td>
        <td>Passing <code>buyer_type_business=1</code> on an account not registered for software / digital services.</td>
        <td><code>buyer_type_business=1</code> on physical goods trade.</td>
        <td>
          Under RBI regulations, cross-border import B2B trade is strictly restricted to software, digital downloads, and consulting services. If importing physical goods, remove <code>buyer_type_business</code> from the request.
        </td>
      </tr>
      <tr>
        <td><strong>Reverse Hash Mismatch on Webhook</strong></td>
        <td>Verification logic omitted <code>additional_charges</code> or inverted UDF ordering.</td>
        <td>Webhook contains <code>additional_charges</code> field.</td>
        <td>
          When <code>additional_charges</code> is present in the webhook payload, prepend it to the reverse hash sequence:<br>
          <code>sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)</code><br>
          Confirm that UDFs run in descending order from <code>udf5</code> down to <code>udf1</code>.
        </td>
      </tr>
      <tr>
        <td><strong>Card Declined (<code>E1632</code>)</strong></td>
        <td>Indian issuing bank declined cross-border transaction due to risk or missing billing address.</td>
        <td>Missing Indian address fields (<code>country</code>, <code>zipcode</code>).</td>
        <td>
          Pass complete Indian billing address parameters in the payment request:<br>
          • <code>address1</code>: Physical street address.<br>
          • <code>city</code> & <code>state</code>: Corresponding Indian state.<br>
          • <code>country</code>: Set strictly to <code>"IN"</code>.<br>
          • <code>zipcode</code>: Valid 6-digit Indian PIN code.
        </td>
      </tr>
      <tr>
        <td><strong>Bank / Issuer Gateway Down (<code>E214</code>, <code>E803</code>)</strong></td>
        <td>Downstream banking switch, NPCI switch, or issuer 3DS ACS server is unreachable.</td>
        <td>Response returns <code>error: "E214"</code> or <code>"E803"</code>.</td>
        <td>
          • Do not retry the exact same <code>txnid</code>. Generate a fresh <code>txnid</code> and re-computed hash.<br>
          • Present customer with alternate payment method (e.g., switch from NetBanking to UPI).<br>
          • Check PayU Status Dashboard for banking partner downtimes.
        </td>
      </tr>
    </tbody>
  </table>
</div>
`}</HTMLBlock>

***

## Support Escalation

If an integration error persists after reviewing the table above, collect the following sanitized diagnostic packet before contacting PayU Merchant Support.

<Callout icon="🛡️" theme="warning">
  ### **Confidentiality Warning:**

  **NEVER** share your raw `SALT`, complete unmasked customer PAN numbers, or full card credentials in support emails or tickets.
</Callout>

### Diagnostic Information to Provide:

```text
1. Transaction Identifiers:
   - Merchant Account Key: [Your 6-character Key, e.g., Fa2IFz]
   - Transaction ID (txnid): [e.g., PACB_TXN_1730708400]
   - PayU Payment ID (mihpayid): [If returned, e.g., 403993715530123456]
   - Timestamp (UTC / IST): [e.g., 2026-11-04 13:45:02 IST]

2. Request Metadata:
   - Integration Channel: [e.g., Cards Seamless / PayU Hosted / UPI Autopay / VA Wire]
   - Environment: [Sandbox / Test OR Production]
   - Amount & Currency: [e.g., 1500.00 INR]
   - Product Info: [e.g., Digital Software License]

3. Cross-Border Compliance Parameters:
   - udf1 (PAN): [Masked, e.g., ABCDE****F]
   - udf3 (DOB): [e.g., 15-08-1988]
   - udf4 (Seller Entity): [e.g., Global Tech Services Ltd]
   - udf5 (Invoice Number): [e.g., INV-2026-1104]

4. Cryptographic Diagnostics:
   - Raw Hash String (Masked Salt): 
     key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||<MASKED_SALT>
   - Generated SHA-512 Hash: [Hex string generated on your server]

5. Error Details:
   - API Error Code: [e.g., E000 / E308 / E1632]
   - Exact Error Message: [e.g., Hash validation failed]
   - Full HTTP Status Code & Raw Response Payload
```

***

## Next Steps

<Cards columns="3">
  <Card title="Mandatory Parameters" href="/docs/pacb-mandatory-cross-border-parameters">
    Verify the master parameter matrix across all PACB flows.
  </Card>

  <Card title="Webhooks & Signatures" href="/docs/pacb-webhooks-and-signature-verification">
    Review canonical webhook payloads and reverse hash validation code.
  </Card>

  <Card title="PACB Best Practices" href="/docs/cross-border-payments-import-best-practices">
    Explore 10-day invoice compliance automation and retry logic.
  </Card>
</Cards>
