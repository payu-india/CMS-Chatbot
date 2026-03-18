---
title: Mututal Funds Payments
deprecated: false
hidden: true
metadata:
  robots: index
---
This part of the document outlines the integration process for Wealth Tech merchants to implement mutual fund payment flows using PayU's payment infrastructure in compliance with SEBI regulations.

## Regulatory Requirements

**SEBI Requirements:** Payment aggregators must report investment transactions for Mutual fund distributors and must comply to the following:

* Certain fields are mandatory for regulatory compliance
* Additional data capture required for exchange/regulatory reporting

## Use Case

#### Target Users:

* Stock brokers

#### Payment Methods:

* Non-seamless
* Seamless
  * Net Banking
  * UPI

#### Subscriptions 

* ENACH
* UPI Autopay

## Next Steps

Integrate Wealth Tech with PayU Hosted Checkout or Merchant Hosted Checkout as mentioned in the following sections:

* [PayU Hosted Integration](doc:payu-hosted-integration-wealth-tech-payment)
* [Merchant Hosted Integration](doc:merchant-hosted-integration-wealth-tech-payment)
* [UPI Autopay Integration](doc:upi-autopay-integration-wealth-tech-payment)