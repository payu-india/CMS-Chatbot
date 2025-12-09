---
title: NBBL Overview with Merchant Hosted
deprecated: false
hidden: true
metadata:
  robots: index
---
**NBBL (NPCI Bharat Bill Pay)** has developed the **Net Banking Interoperable Platform (IBMB/Banking Connect)** to modernize and revitalize net banking in India. This platform addresses the long-standing challenges of traditional net banking by providing interoperability, standardized settlements, and enhanced user experience.

PayU has been selected as a key partner to pilot this new net banking platform, enabling merchants to offer a modern, seamless net banking payment experience to their customers.

### What is NBBL?

NBBL's Interoperable Platform is a centralized payment system that enables:

* **Single Integration** – Merchants integrate once with NBBL to accept payments from multiple banks
* **Mobile-First Experience** – Authentication and authorization handled within the issuer's mobile app
* **Near-Real-Time Settlement** – Faster fund transfers between banks
* **No Amount Limits** – Process transactions of any size
* **Standardized Operations** – Unified dispute management and settlement processes

<Accordion title="Challenges with Traditional Net Banking" icon="fa-info-circle">
Despite significant advancements in India's payments landscape, net banking has remained largely unchanged for over a decade. While UPI and cards have revolutionized transactions, net banking continues to struggle with:

### Key Challenges

| Challenge                   | Impact                                                                              |
| :-------------------------- | :---------------------------------------------------------------------------------- |
| **Multiple Integrations**   | Payment Aggregators need to integrate with 40-50 individual banks separately        |
| **Varying Commercials**     | Pricing varies widely by industry sector (flat rates, percentage, revenue-sharing)  |
| **Unpredictable Refunds**   | No defined TAT; process varies by bank (2-10 days)                                  |
| **Inconsistent Settlement** | Settlement times vary significantly between banks                                   |
| **Low Success Rates**       | Frequently below 50%, with significant variations between banks                     |
| **Poor User Experience**    | Mandatory Customer ID & Password, step-up authentication (OTP & Security Questions) |
| **Lack of Risk Checks**     | No defined risk checklist; up to bank discretion                                    |
| **Dispute Management**      | Difficult to resolve disputes without centralized authority                         |

### Why Net Banking Still Matters

Despite challenges, net banking offers unique advantages:

* **High Ticket Size** – Often used for large transactions
* **Flat Rate Commercials** – Attractive pricing model for businesses
* **TPV Features** – Supports various transaction processing functionalities
* **Bank Security** – Strong authentication credentials and risk mitigation
  
NBBL's platform addresses these challenges through a centralized, interoperable system that standardizes net banking transactions across all participating banks and payment aggregators.
</Accordion>

### Key Features

| Feature                       | Description                                                            |
| :---------------------------- | :--------------------------------------------------------------------- |
| **Interoperability**          | Single integration with NBBL enables access to all participating banks |
| **Mobile-First Approach**     | Authentication and authorization within bank's mobile app              |
| **Near-Real-Time Settlement** | Faster fund transfers between banks                                    |
| **No Amount Limit**           | Process transactions of any size                                       |
| **Configurability**           | Platform can be customized to meet specific business needs             |
| **Standardized Disputes**     | Unified dispute management system                                      |
| **Settlement Framework**      | Standardized settlement process similar to IMPS, BBPS, UPI             |

***

## How It Works

NBBL offers two payment flows to accommodate different use cases:

### Net Banking 1.0+ (Redirect Flow)

Enhanced version of traditional net banking that maintains the familiar bank website experience while adding interoperability:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Customer   │────▶│   Merchant  │────▶│     PayU     │────▶│    IBMB     │
│             │     │   / PA      │     │   Gateway    │     │  Platform   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │
       │  1. Select Bank   │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │  2. Txn Details   │                   │
       │                   │──────────────────▶│                   │
       │                   │                   │                   │
       │                   │                   │  3. reqTxnInit    │
       │                   │                   │──────────────────▶│
       │                   │                   │                   │
       │                   │                   │  4. Encrypted URL  │
       │                   │                   │◀──────────────────│
       │                   │                   │                   │
       │                   │  5. Redirect URL  │                   │
       │                   │◀──────────────────│                   │
       │                   │                   │                   │
       │  6. Redirect to    │                   │                   │
       │     Bank Website  │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │                   │  7. Bank decrypts │
       │                   │                   │     URL via API   │
       │                   │                   │──────────────────▶│
       │                   │                   │                   │
       │  8. Complete      │                   │                   │
       │     Transaction   │                   │                   │
       │     on Bank Site  │                   │                   │
       │                   │                   │                   │
```

**Key Steps:**

1. Customer selects bank and initiates payment
2. Merchant/PA sends transaction details to PayU
3. PayU sends transaction to IBMB platform via `reqTxnInit` API
4. IBMB generates bank-specific encrypted redirection URL
5. Customer is redirected to bank website
6. Bank decrypts URL via API call to IBMB
7. Customer completes transaction on bank website using existing login
8. Transaction status communicated back through the system

### Net Banking 2.0 (QR & Intent Flow)

Modern mobile-first approach using QR codes and app intents:

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Customer   │     │   Merchant  │     │     PayU     │     │    IBMB     │
│  (Desktop)  │     │   / PA      │     │   Gateway    │     │  Platform   │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │
       │  1. Select QR     │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │  2. Txn Details   │                   │
       │                   │──────────────────▶│                   │
       │                   │                   │                   │
       │                   │                   │  3. reqTxnInit    │
       │                   │                   │──────────────────▶│
       │                   │                   │                   │
       │                   │                   │  4. Encrypted URL │
       │                   │                   │◀──────────────────│
       │                   │                   │                   │
       │                   │  5. QR Code       │                   │
       │                   │◀──────────────────│                   │
       │                   │                   │                   │
       │  6. QR Displayed  │                   │                   │
       │◀──────────────────│                   │                   │
       │                   │                   │                   │
       │                   │                   │                   │
┌─────────────┐            │                   │                   │
│  Customer   │            │                   │                   │
│  (Mobile)   │            │                   │                   │
│  Bank App   │            │                   │                   │
└─────────────┘            │                   │                   │
       │                   │                   │                   │
       │  7. Scan QR       │                   │                   │
       │──────────────────▶│                   │                   │
       │                   │                   │                   │
       │                   │                   │  8. reqFetchTxn   │
       │                   │                   │     Details       │
       │                   │                   │◀──────────────────│
       │                   │                   │                   │
       │  9. Select Account│                   │                   │
       │     & Authorize   │                   │                   │
       │                   │                   │                   │
       │  10. Payment      │                   │                   │
       │      Success      │                   │                   │
       │                   │                   │                   │
```

**Key Steps:**

1. Customer selects QR code payment option
2. Merchant/PA sends transaction to PayU
3. PayU sends transaction to IBMB via `reqTxnInit` API
4. IBMB generates encrypted URL (format: `nb://nbpay?param=value`)
5. PayU converts URL to QR code and displays on merchant page
6. Customer scans QR code using bank mobile app
7. Bank app sends `reqFetchTxnDetails` to IBMB to decrypt URL
8. Customer selects account and authorizes payment in bank app
9. Transaction completes within bank app
10. Merchant page shows payment confirmation

## Prerequisites & Compliance Requirements

### Before You Begin

1. **PayU Account Setup**
   * PayU merchant account with NBBL enabled
   * PAID (Payment Aggregator ID) assigned by NBBL
   * Access to NBBL Bharat Connect portal

2. **Technical Requirements**
   * Network connectivity: Minimum 2 Mbps for up to 50 TPS
   * SSL/TLS certificates for secure communication
   * Ability to send/receive signed JSON messages
   * Batch file processing capability
   * NTP synchronization with global servers

3. **API Integration**
   * Implement NBBL APIs: `reqTxnInit`, `reqTxnStatus`, `reqChkTxn`, `reqFetchTxnDetails`
   * Health Check API integration for endpoint availability
   * Digital signature and encryption implementation
   * Certificate exchange with NBBL

### Network Requirements

| Requirement      | Specification                                                                          |
| :--------------- | :------------------------------------------------------------------------------------- |
| **Bandwidth**    | Minimum 2 Mbps for up to 50 TPS (SD-WAN recommended for high volume)                   |
| **IP/Port**      | Single bi-directional IP/Port per environment (mutually exclusive across environments) |
| **Connectivity** | Leased line or secure connection to NPCI (can utilize existing BBPS line)              |
| **Environments** | Separate IP/Port for Sandbox, Comfort, Certification, Production, DR                   |

### Software Requirements

| Requirement          | Description                                           |
| :------------------- | :---------------------------------------------------- |
| **Message Format**   | Ability to send/receive signed JSON messages          |
| **Batch Processing** | Capability to send/receive batch files                |
| **Data Storage**     | Secure, encrypted storage with 5-year archival policy |
| **Compliance**       | IT Act compliance and PCI DSS compliance for PII data |

### Certification Process

PayU must complete three levels of certification:

1. **UAT (User Acceptance Testing)** – Initial testing with dummy values
2. **Sandbox** – Testing with actual PAID and configuration
3. **Comfort** – Final certification before production

***

## Quick Start Guide

### Step 1: Merchant Onboarding

For existing merchants, upload merchant details via CSV file to NBBL portal:

1. Prepare merchant data in NBBL-specified format
2. Log in to NBBL Bharat Connect portal
3. Upload CSV file via Participant Management → Merchant Bulk
4. Checker approves the file
5. Merchant appears as onboarded in the system

For new merchants, use API-based onboarding:

* Call `reqMerchantOnboard` API with merchant details
* NBBL validates and responds with onboarding status

### Step 2: Enable NBBL on PayU Platform

1. Set `NBBL Onboarded = Yes` flag for merchant
2. Configure PG ID = NBBL (600) with appropriate IBIBO codes
3. Set merchant MDR rates matching existing net banking rates
4. Configure bank rates for NBBL PG
5. Enable `enableNbViaNbbl` flag in merchant parameters
6. Activate NBBL PG ID for the merchant

### Step 3: Initialize Transaction

**For QR/Intent Flow:**

```bash
# Step 1: Request transaction initialization
POST https://ibmb.npci.org.in/v1/nbc/reqTxnInit
{
  "txnId": "unique_transaction_id",
  "paId": "your_paid",
  "mid": "merchant_id",
  "amount": "1000.00",
  "currency": "INR",
  "merchantName": "Merchant Name",
  "bankId": "issuing_bank_id",
  "beneBankId": "beneficiary_bank_id",
  "journeyType": "QR" // or "INTENT" or "REDIRECT"
}

# Response: Encrypted URL for QR/Intent or Redirect URL
{
  "txnId": "unique_transaction_id",
  "encryptedUrl": "nb://nbpay?param=encrypted_value",
  "status": "SUCCESS"
}
```

**For Redirect Flow:**

```bash
# Similar API call with journeyType: "REDIRECT"
# Response contains bank-specific encrypted redirect URL
```

### Step 4: Handle Transaction Status

```bash
# IBMB sends transaction status via webhook
POST https://your-callback-url.com/nbbl/status
{
  "txnId": "unique_transaction_id",
  "status": "SUCCESS", // or "FAILURE"
  "result": "SUCCESS",
  "errCode": "",
  "errMsg": ""
}

# Or check status manually
POST https://ibmb.npci.org.in/v1/nbc/reqChkTxn
{
  "txnId": "unique_transaction_id",
  "paId": "your_paid"
}
```

### Step 5: Process Settlement

1. Download daily settlement files from NBBL portal
2. Raw transaction file: Detailed transaction data
3. Net settlement file: Summary of debits/credits
4. Upload to PayU's reconciliation platform
5. Settlement credited to HDFC sponsor bank account (T+1)

***

## Integration Options

### Payment Flow Selection

NBBL supports multiple payment flows that can be offered to customers:

| Flow Type    | Use Case              | Customer Experience           |
| :----------- | :-------------------- | :---------------------------- |
| **QR Code**  | Desktop or mobile web | Scan QR with banking app      |
| **Intent**   | Mobile web or app     | Redirect to banking app       |
| **Redirect** | Any device            | Traditional bank website flow |

### A/B Testing Framework

For redirect flow, PayU uses Pariksha A/B testing framework:

* **Control Group**: BAU Net Banking 1.0 flow
* **Test Group**: NBBL Net Banking 1.0+ flow
* **QR & Intent**: Always use NBBL 2.0 flow (no A/B testing)

***

## Settlement & Reconciliation

### Settlement Process

NBBL provides standardized settlement similar to IMPS, BBPS, and UPI:

| Aspect                 | Details                               |
| :--------------------- | :------------------------------------ |
| **Settlement Type**    | Batch settlement via RTGS             |
| **Current Cycle**      | T+1 (End of Day)                      |
| **Future Cycle**       | 6 cycles per day                      |
| **Sponsor Bank**       | HDFC Bank for PayU                    |
| **Settlement Account** | NBBL RTGS settlement account with RBI |

### Settlement Reports

Available daily from NBBL Bharat Connect portal:

| Report Type                      | Description                                    | Frequency         |
| :------------------------------- | :--------------------------------------------- | :---------------- |
| **Raw Transaction File**         | Detailed transaction data for all transactions | End of each cycle |
| **Net Settlement Report (NTSL)** | Summary of debit/credit transactions           | End of each cycle |
| **Adjustment Reports**           | Refunds and chargebacks processed              | End of each cycle |
| **GST Reports**                  | Monthly GST data                               | End of month      |

### Reconciliation Process

1. Download settlement files from NBBL portal (File Download section)
2. Upload files to PayU's Coherence platform
3. Verify transaction details against internal records
4. Process adjustments for refunds and chargebacks
5. Reconcile with HDFC sponsor bank statements

***

## Dispute Management

### Refunds

**Process:**

1. PA raises refund request via NBBL portal (File Upload section)
2. Maker uploads refund file in specified format
3. Checker approves the file
4. Issuing bank accepts/rejects refund
5. NBBL processes approved refunds in next settlement cycle
6. Refund adjustment reflected in settlement files

**Key Points:**

* Refunds can only be raised on successful transactions
* Cooling period must be completed before raising refund
* Interchange fees and switching fees are not refunded
* Current cycle: T+1, Future: 6 cycles per day

### Chargebacks

**Process:**

1. Bank raises chargeback via NBBL portal (single or bulk)
2. PA receives notification and reviews transaction
3. PA accepts/rejects chargeback with supporting documents
4. Checker approves/rejects the action
5. If accepted, amount debited in next settlement cycle

**Timelines:**

* Dispute and Pre-Arb: 4 calendar days
* Arbitration: 15 calendar days
* Chargeback window: T+45 days from transaction date

**Key Features:**

* No upfront debit (unlike card chargebacks)
* Maker-checker workflow
* Bulk file upload supported
* Portal accessible 24/7 including weekends

***

## API Reference

### Core APIs

| API                                          | Purpose                                      | Direction   |
| :------------------------------------------- | :------------------------------------------- | :---------- |
| **reqTxnInit / respTxnInit**                 | Initialize transaction and get encrypted URL | PA ↔ IBMB   |
| **reqTxnStatus / respTxnStatus**             | Receive transaction status updates           | IBMB → PA   |
| **reqChkTxn / respChkTxn**                   | Check transaction status                     | PA ↔ IBMB   |
| **reqFetchTxnDetails / respFetchTxnDetails** | Decrypt QR/Intent URL (Bank → IBMB)          | Bank ↔ IBMB |
| **Health Check API**                         | Check endpoint availability                  | PA → IBMB   |

### API Environments

| Environment    | URL                               | Purpose                 |
| :------------- | :-------------------------------- | :---------------------- |
| **UAT**        | `https://ibmbcert.npci.org.in`    | User acceptance testing |
| **Sandbox**    | `https://ibmbcert.npci.org.in`    | Integration testing     |
| **Comfort**    | `https://ibmbcert.npci.org.in`    | Pre-production testing  |
| **Production** | `https://ibmb.bharat-connect.com` | Live transactions       |

***

## Best Practices

### Do's ✅

* Test thoroughly in UAT, Sandbox, and Comfort environments before production
* Implement Health Check API to monitor endpoint availability (every 5 seconds)
* Handle all error codes and timeout scenarios gracefully
* Implement retry mechanisms for QR timeout and failed transactions
* Maintain proper logging and audit trails for all transactions
* Keep merchant data synchronized with NBBL master data
* Monitor settlement files daily and reconcile promptly
* Respond to chargebacks within specified timelines
* Use secure storage and encryption for all PII data
* Maintain 5-year archival policy for transaction data

### Don'ts ❌

* Don't skip certification levels (UAT → Sandbox → Comfort)
* Don't process transactions without proper error handling
* Don't ignore Health Check API responses
* Don't store sensitive data without encryption
* Don't miss settlement file downloads
* Don't delay chargeback responses beyond timelines
* Don't use production credentials in testing environments
* Don't skip transaction verification before order fulfillment

***

## Success Metrics

### Key Performance Indicators

| Metric                  | Description                                         | Target                |
| :---------------------- | :-------------------------------------------------- | :-------------------- |
| **Transaction Volume**  | Number of net banking transactions on NBBL platform | Track growth          |
| **Bank Onboarding**     | Number of banks onboarded on NBBL platform          | Maximize coverage     |
| **Merchant Onboarding** | Number of merchants onboarded on NBBL platform      | Scale adoption        |
| **Success Rate**        | NBBL platform success rate vs. old net banking      | Improve significantly |
| **GMV**                 | Gross Merchandise Value on NBBL vs. old net banking | Track growth          |
| **AOV**                 | Average Order Value on NBBL vs. old net banking     | Compare performance   |
| **SRT**                 | Success Rate Time for NBBL vs. old net banking      | Faster processing     |

***

## Next Steps

* [NBBL Integration Guide](doc:nbbl-integration) – Detailed integration guide with API specifications
* [NBBL API Reference](doc:nbbl-api-reference) – Complete API documentation
* [Merchant Onboarding Guide](doc:nbbl-merchant-onboarding) – Step-by-step onboarding process
* [Settlement & Reconciliation](doc:nbbl-settlement) – Settlement process and reconciliation
* [Dispute Management](doc:nbbl-disputes) – Refunds and chargeback handling

> 📘 **Need Help?**
>
> Contact PayU support or your Key Account Manager for:
>
> * NBBL platform enablement
> * Integration assistance
> * Merchant onboarding support
> * Technical queries

***

## Related Documentation

* [Net Banking Codes](doc:net-banking-codes) – Bank codes and IBIBO codes reference
* [Payment Integration Overview](doc:payment-integration-overview) – General payment integration guide
* [API Authentication](doc:api-authentication) – Authentication and security
* [Testing Guide](doc:testing-guide) – Testing best practices

***

## Reference Documents

* **NBBL Handbook**: Integration handbook for net banking interoperability
* **Technical Specification Document (TSD)**: Complete API specifications
* **Procedural Guidelines**: Guidelines for Payment Aggregators
* **Design Guidelines**: UI/UX design principles for NBBL flows

***

_Last updated: Based on NBBL Product Note v1.0_