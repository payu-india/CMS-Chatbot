---
title: PACB - FAQs
deprecated: false
hidden: true
metadata:
  robots: index
---
## Getting Started

1. #### What is Cross-Border Payments — Import (PACB)?

<Accordion title="Answer" icon="fab fa-adn">
  [Cross-Border Payments — Import (PACB)](doc:workflow-for-cross-border-payments-import) is an RBI-compliant payment solution governed by the Online Payment Gateway Service Provider (OPGSP) framework. It enables overseas merchants to accept payments from Indian buyers in Indian Rupees (INR) across local payment methods:

  - Indian Credit Cards and Debit Cards
  - NetBanking
  - UPI Intent and UPI Collect
  - UPI Autopay (Recurring Subscriptions)
  - Virtual Account Bank Wires (NEFT / RTGS)

  PayU collects payments domestically in INR through Indian clearing rails, performs regulatory trade compliance, and coordinates with an Authorized Dealer Category-1 (AD-1) bank to disburse outward remittances directly into your overseas bank account.
</Accordion>

2. #### How does PACB (Import) differ from domestic payment processing?

<Accordion title="Answer" icon="fab fa-adn">
  While domestic checkout processes standard payments with minimal customer data, PACB operates under strict foreign exchange and trade import regulations:

  | Parameter / Feature     | Domestic Checkout                     | Cross-Border Payments — Import (PACB)                                                                              |
  | :---------------------- | :------------------------------------ | :----------------------------------------------------------------------------------------------------------------- |
  | **Buyer KYC**           | Basic details (name, email, phone)    | **Mandatory Buyer KYC**: Indian PAN (`udf1`), Date of Birth (`udf3`), and foreign seller name (`udf4`)             |
  | **Invoice Tracking**    | Internal merchant order reference     | **Mandatory Commercial Invoice**: Unique `udf5` invoice ID matching a physical PDF invoice uploaded within 10 days |
  | **Transaction Limits**  | Standard banking/UPI rails limit      | **₹2,50,000** max cap for online checkout; **₹25,00,000** for Virtual Account NEFT/RTGS                            |
  | **Settlement Clearing** | T+1 or T+2 domestic bank settlement   | Funds held in Nodal account and remitted overseas after trade document verification (T+2 / T+3)                    |
  | **Currency Rails**      | INR collection to INR bank settlement | INR domestic collection to Foreign Currency outward remittance                                                     |
</Accordion>

3. #### What are the minimum prerequisites to integrate PACB?

<Accordion title="Answer" icon="fab fa-adn">
  To accept import payments via PACB, you must have:

  - An active PayU merchant account enabled for Cross-Border Import (PACB / OPGSP)
  - Valid Merchant Key and Salt from your PayU Dashboard
  - An overseas commercial bank account eligible to receive international trade remittances
  - A backend checkout system capable of collecting buyer PAN and Date of Birth
  - An automated pipeline to generate and upload commercial invoices (and carrier Airway Bills for physical goods) within 10 calendar days
  - Publicly reachable HTTPS endpoints for callbacks (`surl`/`furl`) and webhooks
</Accordion>

4. #### Can B2B corporate buyers make payments through PACB?

<Accordion title="Answer" icon="fab fa-adn">
  B2B transactions (passing `buyer_type_business = 1`) are legally permitted **strictly for software, SaaS, digital services, and subscriptions**. Physical goods merchants cannot process B2B import transactions under PACB and must accept consumer (B2C) payments only.
</Accordion>

***

## Regulatory & Buyer KYC

1. #### Which buyer KYC fields are strictly mandatory for PACB transactions?

<Accordion title="Answer" icon="fab fa-adn">
  Under RBI regulations for trade inward collections and outward remittances, every cross-border payment must submit the following buyer KYC fields:

  | Field                     | Parameter | Requirement | Format & Validation                                                                     |
  | :------------------------ | :-------- | :---------- | :-------------------------------------------------------------------------------------- |
  | **Buyer PAN**             | `udf1`    | Mandatory   | 10-character alphanumeric Indian PAN matching regex: `^[A-Z]{5}[0-9]{4}[A-Z]{1}$`       |
  | **Custom Metadata**       | `udf2`    | Optional    | Merchant custom tracking metadata (max 255 characters)                                  |
  | **Buyer Date of Birth**   | `udf3`    | Mandatory   | Must use hyphens in `DD-MM-YYYY` format (e.g., `15-08-1988`). Do not use slashes (`/`). |
  | **Foreign Seller Entity** | `udf4`    | Mandatory   | Registered legal business name of the overseas entity. _(Leave empty for UPI Autopay)._ |
  | **Invoice Identifier**    | `udf5`    | Mandatory   | Unique commercial invoice number. Must match the invoice PDF uploaded later.            |

  <Callout icon="far fa-circle-check" theme="success">
    ### **Important:**

    Pre-validate the buyer PAN and Date of Birth on your frontend checkout form before submitting the payment request to prevent payment initiation rejections.
  </Callout>
</Accordion>

2. #### What format should I use for UPI Autopay mandate consent?

<Accordion title="Answer" icon="fab fa-adn">
  UPI Autopay combines mandate parameters and regulatory KYC using a pipe-delimited format:

  - `udf1`: `PAN||DOB` (e.g., `ABCDE1234F||15-08-1988`)
  - `udf3`: `InvoiceID||OverseasSellerName` (e.g., `INV-2026-1104||GlobalTechLtd`)
  - `udf4`: **Do not pass** (leave completely empty)
  - `udf5`: `InvoiceID` (must match the invoice prefix passed in `udf3`)

  <Callout icon="⚠️" theme="warn">
    ### **Warning!**

    Passing one-time UDF formatting (such as a plain PAN string without DOB delimiter) on a recurring consent request will cause mandate creation to fail at NPCI/PayU validation.
  </Callout>
</Accordion>

3. #### Are Indian buyer billing addresses and postal codes mandatory?

<Accordion title="Answer" icon="fab fa-adn">
  While PayU core checkout accepts payments without billing addresses, passing complete Indian billing information (`address1`, `city`, `state`, `country="IN"`, and 6-digit `zipcode`) is **strongly recommended**.

  International card schemes (Visa, Mastercard, Amex) and issuer fraud engines frequently decline cross-border card transactions (error `E1632`) if Address Verification System (AVS) checks fail.
</Accordion>

***

## Transaction Limits & Routing

1. #### What is the maximum transaction limit for PACB payments?

<Accordion title="Answer" icon="fab fa-adn">
  RBI regulatory caps dictate transaction routing based on the checkout channel:

  | Integration Channel               | Payment Methods                            | Maximum Allowed Transaction Limit         |
  | :-------------------------------- | :----------------------------------------- | :---------------------------------------- |
  | **Online Checkout**               | Cards, NetBanking, UPI Intent, UPI Collect | **₹2,50,000 (₹2.5 Lakh)** per transaction |
  | **Virtual Account Wire Transfer** | Local NEFT / RTGS Bank Transfer            | **₹25,00,000 (₹25 Lakh)** per transaction |

  Transactions exceeding ₹2,50,000 submitted through online checkout will fail with error code `E308` (Amount limit exceeded).
</Accordion>

2. #### How should high-value purchases exceeding ₹2.5 Lakh be handled?

<Accordion title="Answer" icon="fab fa-adn">
  Implement tiered checkout routing on your billing system:

  1. **Cart values up to ₹2,50,000:** Present standard checkout modes (Cards, NetBanking, or UPI).
  2. **Cart values between ₹2,50,001 and ₹25,00,000:** Automatically route the customer to [Virtual Account Local Wire Transfers](doc:virtual-account-based-local-wire-transfers). Issue a commercial invoice displaying custom virtual account details (unique Account Number + IFSC) for local NEFT/RTGS remittance.
  3. **Cart values above ₹25,00,000:** Must be settled via direct international wire transfer (A2 bank remittance) outside the OPGSP framework.
</Accordion>

***

## Trade Invoices & Settlement Compliance

1. #### Why are my settlements marked "On Hold" even after payment capture?

<Accordion title="Answer" icon="fab fa-adn">
  Under AD-1 Category Bank regulations, funds collected in the PayU Nodal account cannot be remitted overseas until trade documentation is verified:

  1. You have a **strict 10-calendar-day window** from transaction capture to submit the commercial invoice PDF.
  2. If the 10-day window expires without a matching invoice, the AD-1 bank automatically places all subsequent merchant settlements on hold.
  3. Once the matching invoice (and Airway Bill for physical goods) is uploaded and verified, the hold is cleared, and funds are disbursed in the next settlement cycle (T+2 / T+3).
</Accordion>

2. #### What documents are required for physical goods versus digital goods/services?

<Accordion title="Answer" icon="fab fa-adn">
  Documentation requirements depend on the nature of your trade:

  - **Digital Goods / SaaS / Cloud Subscriptions:** Single document: Commercial Invoice PDF matching the `udf5` invoice number and buyer PAN.
  - **Physical Goods / E-Commerce:** Dual documents:
    1. Commercial Invoice PDF (submitted at T+0 upon order confirmation).
    2. Carrier Airway Bill (AWB) or Bill of Entry (submitted once dispatch commences, within the 10-day window).
</Accordion>

3. #### How do I automate commercial invoice submission?

<Accordion title="Answer" icon="fab fa-adn">
  Automate invoice uploads by listening for PayU's payment capture webhook on your backend:

  1. When your webhook endpoint receives `status: "success"` and `unmappedstatus: "captured"`, generate the customer invoice PDF.
  2. Immediately invoke the PayU Invoice Upload API:
     - Endpoint: `POST <redacted URL>` (Production)
     - Parameters: `txnid`, `invoiceId` (matching `udf5`), and the PDF multipart binary.
  3. Store the API upload acknowledgment reference to maintain a verifiable audit trail.
</Accordion>

***

## Hash Generation & Security

1. #### What is the hash formula for PACB one-time checkout requests?

<Accordion title="Answer" icon="fab fa-adn">
  ```text Hash Formula
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  Example with values (`udf1`=PAN, `udf2`=empty, `udf3`=DOB, `udf4`=Seller, `udf5`=Invoice):

  ```text
  gtKFFx|TXN1001|1500.00|SaaS Plan|Aarav|aarav@example.com|ABCDE1234F||15-08-1988|GlobalTechLtd|INV-98765||||||eCwWELxi
  ```

  <Callout icon="far fa-circle-check" theme="success">
    ### **Important:**

    - [x] Ensure 6 empty pipes (`||||||`) separate `udf5` and `SALT`.
    - [x] When passing extended trade parameters (`udf_params`) or B2B flags (`buyer_type_business`), append them after `SALT`.
    - [x] Never compute or expose the hash client-side in the browser or mobile application.
  </Callout>
</Accordion>

2. #### What causes an "Invalid Hash" error on PACB transactions?

<Accordion title="Answer" icon="fab fa-adn">
  Work through this checklist:

  - [x] Verify exact parameter sequence: `key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT`.
  - [x] Ensure exactly 6 pipe delimiters exist between `udf5` and `SALT`.
  - [x] Confirm `udf1` through `udf5` in the hash match the exact values sent in the request body.
  - [x] Check for leading or trailing whitespace in PAN, DOB, or merchant key.
  - [x] Ensure the amount format uses two decimal places (e.g., `1500.00`).
  - [x] Ensure your server is using SHA-512 and generating lowercase hex output.
</Accordion>

***

## Webhook Handling & Reverse Hashing

1. #### What is the reverse hash formula for PACB callbacks and webhooks?

<Accordion title="Answer" icon="fab fa-adn">
  When receiving transaction callbacks or Server-to-Server (S2S) webhooks, verify authenticity using the reverse hash formula:

  **Standard Response:**

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  **When&#x20;**`additional_charges`**&#x20;are present:**

  ```text
  sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <Callout icon="⚠️" theme="warn">
    ### **Warning!**

    Notice the reverse UDF sequence: **udf5 → udf4 → udf3 → udf2 → udf1**. Mismatching the UDF order is the single most common cause of webhook validation failure.
  </Callout>
</Accordion>

2. #### Why do webhooks arrive in production but not in sandbox/test mode?

<Accordion title="Answer" icon="fab fa-adn">
  Common causes for missing sandbox webhooks:

  - Webhook URL was added only under the **Live** dashboard mode instead of the **Test** toggle.
  - Your staging endpoint requires a custom port or VPN access (PayU servers only post to standard public HTTPS ports `443`).
  - Your endpoint returned an HTTP status other than `200 OK` (such as `301/302` redirect or `500` internal error), causing PayU's retry engine to back off.
  - Webhooks are disabled on your test MID. Contact PayU Integration Support to enable test webhook dispatch.
</Accordion>

***

## Currency & Outward Remittance

1. #### Does PACB checkout display amounts in foreign currency (USD, EUR, GBP) to the Indian customer?

<Accordion title="Answer" icon="fab fa-adn">
  No. Under the PACB (Import) model, the Indian customer is always billed in **Indian Rupees (INR)**. The payment request `amount` and `currency` must be set to `INR`.

  PayU clears the transaction domestically in INR and disburses the foreign currency equivalent (USD, EUR, GBP, etc.) to your overseas bank account following AD-1 bank trade conversion.

  _(If you require pricing in foreign currencies directly on checkout, refer to [Multi-Currency Checkout (MCC)](doc:payu-hosted-checkout-integration-dynamic-currency-conversion) or [Dynamic Currency Conversion (DCC)](doc:dynamic-currency-conversion-workflow))._
</Accordion>

2. #### How are currency exchange rates and outward settlement fees applied?

<Accordion title="Answer" icon="fab fa-adn">
  When funds are cleared from the Nodal account for international outward remittance:

  - The AD-1 Category Bank applies the prevailing interbank foreign exchange rate on the date of trade filing and cross-border transfer.
  - PayU deducts the agreed processing commission (MDR) and statutory GST.
  - Funds are remitted to your overseas account via SWIFT wire transfer, typically arriving within T+2 or T+3 business days.
</Accordion>

***

## Testing & Sandbox Validation

1. #### How do I test PACB transactions in the sandbox environment?

<Accordion title="Answer" icon="fab fa-adn">
  Follow these testing rules in the sandbox (`<redacted URL>`):

  - **Endpoint:** Point payment POST requests to `<redacted URL>`.
  - **Credentials:** Use your Sandbox Merchant Key and Salt.
  - **Valid Test PAN:** Use a syntactically valid test PAN (e.g., `ABCDE1234F`).
  - **Date of Birth:** Use any valid adult birthdate in `DD-MM-YYYY` format (e.g., `15-08-1988`).
  - **Test Cards / UPI:** Use test cards or the test UPI VPA `anything@payu` from the [Test Integration](doc:test-integration) guide.
  - **Transaction Amount:** Test with amounts under ₹2,50,000 (e.g., `100.00`).
</Accordion>

2. #### How can I test the 10-day invoice compliance workflow in staging?

<Accordion title="Answer" icon="fab fa-adn">
  In the staging environment, use the sandbox Invoice Upload API:

  1. Complete a successful test checkout payment and save the returned `txnid`.
  2. Send a `POST` request to `<redacted URL>` with the matching `txnid`, `invoiceId` (`udf5`), and a sample PDF invoice file.
  3. Validate that the API returns `status: 1` and `message: "Invoice uploaded successfully"`.
</Accordion>
