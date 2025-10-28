---
title: EFTNET
deprecated: false
hidden: true
metadata:
  robots: index
---
NEFT (National Electronic Fund Transfer) or RTGS (Real-Time Gross Settlement) facilitates secure fund transfers from one bank account to another on a one-to-one basis. PayU EFTNET offers NEFT/RTGS as an payment mode through non-seamless (PayU Hosted) or seamless integration (Merchant Hosted or S2S). 

Allows customers who browse online but lack access to or are reluctant to use digital payment methods to complete transactions via bank branches. Specifically designed for high-value transactions and customers in Tier-2/Tier-3 cities where bank-based payments are preferred

## Advantages and Business Benefits 

**For Merchants:**

* **Expanded market reach**: Access to customers in Tier-2 and Tier-3 cities who prefer traditional banking methods
* **High-value transaction support**: Ideal for organizations requiring fast, seamless solutions for large transactions without online payment risks
* **Customizable challans**: Greater flexibility for transaction management
* **Real-time updates**: Transaction success notifications in real-time
* **Automated reconciliation**: Aggregated settlement reports with reconciliation and refunds across all payment modes including NEFT/RTGS, eliminating manual reconciliation needs
* **QR-enabled tracking**: Real-time monitoring of transactions INR 5 lakh and above, reducing customer service inquiries
* **Instant refunds**: Automated refund processing for erroneous entries

**For Customers:**

* **Dual payment options**: Visit bank branch OR add beneficiary details for net banking/mobile banking completion
* **One-time use challan**: Secure, transaction-specific payment instruments
* **Real-time status tracking**: QR code-based payment status monitoring for high-value transactions
* **Reduced anxiety**: Clear visibility into payment status for time-bound, high-value transactions

## Use Cases

**Ideal Scenarios:**

* Application fees and tender registrations (time-bound payments)
* Corporate payments where employees aren't authorized for digital payment initiation
* Educational institution fee payments
* Government payment collections
* B2B transactions with high-value amounts
* Customers comfortable with online browsing but hesitant about digital payments

## Compliance and Regulatory Information

* NEFT available 24/7 with near-real-time settlement
* Transaction limits: No minimum or maximum caps for NEFT transfers
* Penal interest provision for delays in credit or transaction returns
* Consumer rights under EFT regulations for timely transactions and grievance redressal

## Prerequisites

**Merchant Requirements:**

* PayU merchant account activation
* EFTNet payment mode enablement (contact PayU support)
* Integration capability for challan generation API
* System for receiving real-time transaction webhooks

**Technical Prerequisites:**

* API integration for challan generation
* Webhook endpoint for payment status updates
* Dashboard access for transaction monitoring

## How It Works - Process Flow

**Transaction Flow:**

1. Customer selects NEFT/RTGS option at merchant checkout
2. PayU generates one-time use challan with bank details
3. Customer downloads/prints challan with transaction reference and customer has the following options to make payment:
   1. Customer visits bank branch to complete payment
   2. Customer adds beneficiary details and completes via net banking/mobile banking
4. Bank processes NEFT/RTGS transfer
5. PayU receives payment confirmation
6. Merchant receives real-time transaction success update
7. For transactions, customer can scan QR code on the challan for real-time status tracking

## Next Steps

This part of the document provides the steps to integrate the EFTNET (NEFT/RTGS) and its other offerings:

* [PayU Hosted Checkout Integration - EFTNET](doc:payu-hosted-checkout-eftnet)
* [Merchant Hosted Checkout Integration - EFTNET](doc:collect-payments-with-eftnet-neftrtgs-seamless)
  * [Reusable VANs Integration - EFTNET](doc:reusable-van-integration-neft)

<Callout icon="📘" theme="info">
  **Note:** With PayU Hosted Checkout, EFTNET with or without reusable VANs integration does not require any changes. For reusable VANs integration, you need to enable it and pass the VAN identifier in any of the UDF fields (udf1-udf5) as agreed with PayU. For more information enabling reusable VANs, contact<Anchor label=" PayU Support." target="_blank" href="https://help.payu.in"> PayU Support.</Anchor>
</Callout>

<br />
