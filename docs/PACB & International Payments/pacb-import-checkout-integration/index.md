---
title: PACB Import - Checkout Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<br />

##

Under Reserve Bank of India (RBI) guidelines for the Online Payment Gateway Service Provider (OPGSP / PACB) framework, every cross-border inward remittance for import of goods and software services requires mandatory buyer identification, overseas seller identification, and verifiable commercial invoice tracking.

<Callout icon="📘" theme="info">
  ### **Core Compliance Rule:**

  Unlike domestic payments where User Defined Fields (`udf1` to `udf5`) are optional metadata, **cross-border import payments mandate specific UDF values**. Failure to supply valid regulatory values will result in immediate API rejection or settlement holds by the authorized dealer (AD-1) bank.
</Callout>

***

## Master Parameter Matrix by Flow

The table below details all top-level request parameters and cross-border regulatory fields across each PACB integration channel:

<HTMLBlock>{`
<div style="overflow-x: auto;">
  <table>
    <thead>
      <tr>
        <th style="width: 14%;">Parameter</th>
        <th style="width: 8%;">Type</th>
        <th style="width: 16%;">One-Time Checkout (Cards / NB / UPI Intent)</th>
        <th style="width: 16%;">UPI Autopay Mandate (Consent)</th>
        <th style="width: 14%;">UPI Autopay Recurring Debit</th>
        <th style="width: 16%;">Virtual Account (NEFT / RTGS Wire)</th>
        <th style="width: 16%;">Format & Validation Rules</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><code>key</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td>PayU Merchant Key from Dashboard.</td>
      </tr>
      <tr>
        <td><code>txnid</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Auto-generated</em></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td>Unique alphanumeric ID per transaction (max 25 chars).</td>
      </tr>
      <tr>
        <td><code>amount</code></td>
        <td><code>Number</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong><br>(Max ₹2,50,000)</td>
        <td><strong style="color: #b91c1c;">Mandatory</strong><br>(e.g. ₹2.00)</td>
        <td><strong style="color: #b91c1c;">Mandatory</strong><br>(Per schedule)</td>
        <td><strong style="color: #b91c1c;">Mandatory</strong><br>(Max ₹25,00,000)</td>
        <td>INR currency with 2 decimal places (e.g. <code>1500.00</code>).</td>
      </tr>
      <tr>
        <td><code>productinfo</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Optional</em></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td>Description of goods or digital services (max 100 chars).</td>
      </tr>
      <tr>
        <td><code>firstname</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Optional</em></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td>Payer first name matching official PAN card record.</td>
      </tr>
      <tr>
        <td><code>email</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Optional</em></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td>Valid customer email address for invoice delivery.</td>
      </tr>
      <tr>
        <td><code>phone</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Optional</em></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td>10-digit Indian mobile number (without +91).</td>
      </tr>
      <tr>
        <td><code>surl</code> / <code>furl</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Optional</em></td>
        <td><em>Not Applicable</em></td>
        <td>Publicly accessible HTTPS callback endpoints.</td>
      </tr>
      <tr>
        <td><code>hash</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Not Applicable</em></td>
        <td>Server-generated SHA-512 hex signature string.</td>
      </tr>
      <tr>
        <td><code>udf1</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory (Buyer PAN)</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory (PAN||DOB)</strong></td>
        <td><em>Inherited</em></td>
        <td><strong style="color: #b91c1c;">Mandatory (Buyer PAN)</strong></td>
        <td>10-character Indian PAN regex: <code>^[A-Z]{5}[0-9]{4}[A-Z]{1}$</code>. In Autopay: pipe-delimited with DOB (e.g. <code>ABCDE1234F||15-08-1988</code>).</td>
      </tr>
      <tr>
        <td><code>udf2</code></td>
        <td><code>String</code></td>
        <td><em>Optional</em></td>
        <td><em>Optional</em></td>
        <td><em>Inherited</em></td>
        <td><em>Optional</em></td>
        <td>Custom merchant metadata string (max 255 chars).</td>
      </tr>
      <tr>
        <td><code>udf3</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory (Buyer DOB)</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory (Inv||Seller)</strong></td>
        <td><em>Inherited</em></td>
        <td><strong style="color: #b91c1c;">Mandatory (Buyer DOB)</strong></td>
        <td>One-time: <code>DD-MM-YYYY</code> format. Autopay: pipe-delimited with Seller Name (e.g. <code>INV-98765||GlobalTechLtd</code>).</td>
      </tr>
      <tr>
        <td><code>udf4</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory (Overseas Seller)</strong></td>
        <td><em>Do NOT Send</em></td>
        <td><em>Inherited</em></td>
        <td><strong style="color: #b91c1c;">Mandatory (Overseas Seller)</strong></td>
        <td>Legal entity name of the foreign seller / exporter. (Leave empty in UPI Autopay).</td>
      </tr>
      <tr>
        <td><code>udf5</code></td>
        <td><code>String</code></td>
        <td><strong style="color: #b91c1c;">Mandatory (Invoice ID)</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory (Invoice ID)</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory (Invoice ID)</strong></td>
        <td><strong style="color: #b91c1c;">Mandatory (Invoice ID)</strong></td>
        <td>Commercial invoice number. Must match the uploaded PDF commercial invoice.</td>
      </tr>
      <tr>
        <td><code>si</code></td>
        <td><code>String</code></td>
        <td><em>Not Applicable</em></td>
        <td><strong style="color: #b91c1c;">Mandatory (1)</strong></td>
        <td><em>Not Applicable</em></td>
        <td><em>Not Applicable</em></td>
        <td>Flags request as a standing instruction mandate.</td>
      </tr>
      <tr>
        <td><code>si_details</code></td>
        <td><code>JSON</code></td>
        <td><em>Not Applicable</em></td>
        <td><strong style="color: #b91c1c;">Mandatory</strong></td>
        <td><em>Not Applicable</em></td>
        <td><em>Not Applicable</em></td>
        <td>JSON object specifying billing cycle, intervals, and dates.</td>
      </tr>
      <tr>
        <td><code>api_version</code></td>
        <td><code>String</code></td>
        <td><em>Optional</em></td>
        <td><strong style="color: #b91c1c;">Mandatory (7)</strong></td>
        <td><em>Not Applicable</em></td>
        <td><em>Not Applicable</em></td>
        <td>Version string required for UPI Autopay consent hashing.</td>
      </tr>
      <tr>
        <td><code>authpayuid</code></td>
        <td><code>String</code></td>
        <td><em>Not Applicable</em></td>
        <td><em>Returned by PayU</em></td>
        <td><strong style="color: #b91c1c;">Mandatory (var1)</strong></td>
        <td><em>Not Applicable</em></td>
        <td>Original mandate identifier (<code>mihpayid</code> from consent response).</td>
      </tr>
      <tr>
        <td><code>buyer_type_business</code></td>
        <td><code>String</code></td>
        <td><em>Conditional</em></td>
        <td><em>Conditional</em></td>
        <td><em>Not Applicable</em></td>
        <td><em>Conditional</em></td>
        <td>Set to <code>1</code> strictly for B2B cross-border software / digital service imports.</td>
      </tr>
    </tbody>
  </table>
</div>
`}</HTMLBlock>

***

## Deep Dive: Critical Regulatory Fields

### 1. Buyer Permanent Account Number (PAN)

* **One-time flows (Cards / NB / UPI Intent)**: Passed in `udf1`.
* **UPI Autopay flows**: Passed as the first segment of `udf1`, delimited by double pipes `||`.
* **Validation**:
  * Must be exactly 10 alphanumeric characters.
  * Format: 5 uppercase letters, 4 digits, 1 uppercase letter (`^[A-Z]{5}[0-9]{4}[A-Z]{1}$`).
  * Fourth character indicates entity type (`P` for Individual, `C` for Company, `H` for HUF, `F` for Firm).

### 2. Buyer Date of Birth (DOB)

* **One-time flows**: Passed in `udf3`.
* **UPI Autopay flows**: Passed as the second segment of `udf1` (`PAN||DOB`).
* **Format**: Must follow `DD-MM-YYYY` (e.g., `15-08-1988`). Avoid slashes (`/`) or ISO 8601 timestamps.

### 3. Overseas Seller Name (End-Merchant)

* **One-time flows**: Passed in `udf4`. Represents the foreign seller or marketplace merchant receiving settlement.
* **UPI Autopay flows**: Passed as the second segment of `udf3` (`InvoiceID||SellerName`).
* **Crucial Rule for Autopay**: In UPI Autopay consent, `udf4`**&#x20;must NOT be passed** as a separate top-level field; doing so triggers parameter mismatch validation errors.

### 4. Commercial Invoice ID

* **All flows**: Passed in `udf5` (and also in the first segment of `udf3` for UPI Autopay).
* **Fulfillment Constraint**: Every invoice ID passed in `udf5` must be backed by a matching commercial invoice PDF uploaded to PayU within **10 calendar days**.

***

## Hash Calculation Rules by Flow

<Tabs>
  <Tab title="One-Time PACB Checkout">
    For standard Cards, NetBanking, and UPI Intent checkout payments:

    ```text
    sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
    ```

    <Callout icon="⚠️" theme="warning">
      ### **Notice on Empty Pipes:**

      Notice the six consecutive empty pipes `||||||` between `udf5` and `SALT`. These correspond to the unused domestic `udf6` through `udf10` slots and must be preserved exactly.
    </Callout>
  </Tab>

  <Tab title="UPI Autopay Mandate (Consent)">
    For UPI Autopay mandate consent registration (`si=1`, `api_version=7`):

    ```text
    sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||si_details|SALT)
    ```

    Where:

    * `udf1` = `PAN||DOB` (e.g., `ABCDE1234F||15-08-1988`)
    * `udf2` = Merchant custom tracking string or empty
    * `udf3` = `InvoiceID||SellerName` (e.g., `INV-10023||GlobalTechLtd`)
    * `udf4` = Empty string
    * `udf5` = `InvoiceID` (e.g., `INV-10023`)
    * `si_details` = Valid JSON string matching mandate terms
  </Tab>

  <Tab title="UPI Autopay Recurring Debit">
    For execution of scheduled recurring debits using `command=siTransaction`:

    ```text
    sha512(key|siTransaction|var1|SALT)
    ```

    Where:

    * `var1` = Original mandate registration ID (`authpayuid` / `mihpayid`)
  </Tab>
</Tabs>

***

## Next Steps

<Cards columns="3">
  <Card title="Workflow & Compliance" href="/docs/workflow-for-cross-border-payments-import">
    Review the 4-stage regulatory clearing cycle and 10-day invoice rules.
  </Card>

  <Card title="Webhooks & Verification" href="/docs/pacb-webhooks-and-signature-verification">
    Inspect canonical webhook payloads and signature verification code.
  </Card>

  <Card title="Errors & Troubleshooting" href="/docs/pacb-error-map-and-resolutions">
    Diagnose hash validation failures, KYC errors, and settlement holds.
  </Card>
</Cards>
