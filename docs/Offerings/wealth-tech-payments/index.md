---
title: Wealth Tech Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
This part of the document outlines the integration process for Wealth Tech merchants to implement mutual fund payment flows using PayU's payment infrastructure in compliance with SEBI regulations.

## Regulatory Requirements

**SEBI Requirements:** Payment aggregators must report investment transactions for:

* Stock brokers
* Mutual fund distributors
  • Certain fields are mandatory for regulatory compliance
  • Additional data capture required for exchange/regulatory reporting

## Use Case

#### Target Users:

* Stock brokers
* Mutual fund distributors

#### Payment Methods:

* Net Banking
* UPI

#### Transaction Type:

Lump-sum investment payments from investors

#### Compliance Assurance:

* Every transaction meets SEBI requirements
* Mandatory capture of investor bank details
* Fund information reporting (scheme code and folio)

## Payment Flow Benefits

The standardized WealthTech payment flow enables platforms to:

* **Secure Payment Collection**: Collect investor payments securely via PayU's APIs
* **Transaction Mapping**: Map payments to specific fund orders through `wt_params`
* **Reporting & Reconciliation**: This enables and ensures:
  * Enable downstream reporting with AMCs
  * Facilitate reconciliation with exchanges
  * Ensure regulatory compliance

## Next Steps

Integrate Wealth Tech with PayU Hosted Checkout or Merchant Hosted Checkout as mentioned in the following sections:

* [PayU Hosted Integration](doc:payu-hosted-integration-wealth-tech-payment)
* [Merchant Hosted Integration](doc:merchant-hosted-integration-wealth-tech-payment)
* [UPI Autopay Integration](doc:upi-autopay-integration-wealth-tech-payment)