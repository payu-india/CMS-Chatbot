---
title: CB LRS Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
The Liberalised Remittance Scheme (LRS) is a framework introduced by the Reserve Bank of India (RBI) that allows resident individuals in India, including minors, to freely remit up to USD 250,000 per financial year for permissible current and capital account transactions. This framework governs:

* **Current Account Transactions**: Travel, education, medical expenses, etc.
* **Capital Account Transactions**: Investments, property purchases abroad, etc.

LRS is strictly applicable to individual entities and not business transactions. The scheme operates under the Foreign Exchange Management Act (FEMA) 1999 and excludes specific countries like Nepal and Bhutan.

## Use Cases

The LRS framework enables several key business use cases with significant market potential:

**1. Travel Platforms**

* **Global Online Travel Agencies (OTAs)** like Expedia, Kiwi.com selling hotel or airline bookings to Indian consumers
  * Serviceable addressable market: USD 1.25 billion
* **Indian OTAs** offering foreign hotel/airline bookings to Indian consumers
  * Serviceable addressable market: USD 2.5 billion

**2. Education Merchants**

* **Educational Payment Platforms** accepting fees on behalf of foreign universities for Indian students (e.g., Flywire, education consultants, ERP systems)
  * Serviceable addressable market: USD 5 billion

**3. Medical and Gift Transactions**

* Platforms facilitating payments for medical treatments abroad
* Services enabling gifting or donations to foreign entities/relatives

## Benefits

Implementing LRS support offers significant benefits for cross-border merchants:

**1. Regulatory Compliance and Risk Mitigation**

* **Streamlined Compliance**: Automatic adherence to RBI guidelines
* **Reduced Regulatory Risk**: Built-in validations prevent non-compliant transactions

**2. Market Access and Revenue Growth**

* **Expanded Addressable Market**: Access to high-value segments like education, travel, and healthcare
* **Increased Transaction Volume**: Tap into India’s growing appetite for international services

**3. Enhanced Customer Experience**

* **Transparent Transaction Process**: Clear display of tax implications and regulatory requirements
* **Simplified Checkout Flow**: Integrated declarations and compliance checks
* **Reduced Friction**: Automated PAN validation and TCS calculation

**4. Operational Efficiency**

* **Automated Compliance**: Reduced manual intervention for regulatory checks
* **Simplified Settlement**: Streamlined processing of cross-border payments

**Technical Implementation Guide**

**API Parameters for LRS Implementation**

PayU’s payment API supports LRS implementation through the following parameters:

* buyer\_type\_business
* lrs\_mandatory\_limit\_declaration
* lrs\_tnc
* lrs\_tcs\_declaration\_under\_limit

## Integration Flow

* **Identify Transaction Type**:
  * Determine if the transaction falls under LRS (cross-border, individual buyer)
  * Set buyer\_type\_business appropriately
* **Collect Buyer PAN Information**:
  * For individual buyers, capture and validate PAN details
  * Ensure PAN is linked to Aadhaar for successful transaction processing
* **Present LRS Declarations**:
  * Display and capture acceptance of lrs\_mandatory\_limit\_declaration
  * Display and capture acceptance of lrs\_tnc
  * If applicable, capture lrs\_tcs\_declaration\_under\_limit
* **Proceed with Payment**:
  * Include all required LRS parameters in the payment API call
  * Process transaction through PayU gateway

**Compliance Requirements**

* PAN details must be collected for all LRS transactions
* PAN must be linked to Aadhaar for successful processing
* Transactions with inoperative PANs will be rejected

**Buyer Declarations**

* All buyers must acknowledge their understanding of LRS limits
* Buyers must confirm that their cumulative remittances are within USD 250,000 per financial year
* Additional declarations for transactions exceeding ₹10 lakhs