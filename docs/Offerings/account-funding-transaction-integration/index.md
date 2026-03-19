---
title: Account Funding Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
# Introduction to Account Funding Transaction (AFT)

Account Funding Transaction (AFT) is a payment method that enables merchants to fund customer accounts, wallets, or cards directly through the PayU platform. AFT is specifically designed for Visa MCC 6540 merchants and provides a secure, compliant way to transfer funds to customer accounts in real-time.

## Overview

AFT allows merchants to credit funds directly to customer debit cards, prepaid cards, or digital wallets. This payment method is ideal for businesses that need to disburse funds to their customers, such as:

- **Digital wallet top-ups** and account funding
- **Cashback and rewards** distribution  
- **Refunds and returns** processing
- **Marketplace payouts** to sellers
- **Gaming and entertainment** credit distribution
- **P2P money transfers** and remittances

## Advantages and Business Benefits

### **For Merchants**
- ✅ **Real-time fund transfers** - Instant account funding capabilities
- ✅ **Enhanced customer experience** - Quick and seamless fund disbursement  
- ✅ **Regulatory compliance** - Built-in compliance with Visa AFT standards
- ✅ **Reduced operational costs** - Automated fund transfer processes
- ✅ **Comprehensive reporting** - Detailed transaction tracking and reconciliation
- ✅ **High success rates** - Optimized routing for maximum transaction success
- ✅ **24/7 availability** - Round-the-clock fund transfer capabilities

### **For Customers**  
- ✅ **Instant fund availability** - Immediate access to transferred funds
- ✅ **Secure transactions** - Protected by industry-standard security protocols
- ✅ **Multiple funding options** - Support for various card types and wallets
- ✅ **Transaction transparency** - Clear visibility into fund transfer status
- ✅ **No additional registration** - Use existing payment credentials

## Use Cases

### **Digital Wallets and Fintech**
Perfect for digital wallet providers, fintech apps, and neobanks that need to enable instant account funding and top-ups for their customers.

### **Marketplace and Gig Economy**
Ideal for marketplace platforms, ride-sharing apps, and gig economy platforms that need to disburse earnings, commissions, or payments to sellers and service providers.

### **Gaming and Entertainment**
Essential for gaming platforms, entertainment apps, and loyalty programs that distribute rewards, cashback, winnings, or promotional credits to users.

### **E-commerce and Retail**
Valuable for e-commerce platforms processing refunds, returns, or cashback programs that require direct fund disbursement to customer accounts.

## Compliance and Regulatory Information

### **Visa MCC 6540 Requirement**
- AFT is available exclusively for merchants with **Visa MCC 6540** (Money Transfer)
- Ensures compliance with Visa's Account Funding Transaction guidelines
- Requires specific merchant category activation and approval

### **Security and Data Protection**
- **PCI DSS compliant** infrastructure for secure data handling
- **Tokenization support** for enhanced card data security  
- **Encryption** for all sensitive transaction data
- **Fraud monitoring** and risk management capabilities

### **Transaction Limits and Regulations**
- Adheres to applicable money transfer and remittance regulations
- Configurable transaction limits based on merchant requirements
- Real-time transaction monitoring for compliance reporting

## Prerequisites

### **Merchant Requirements**
- ✅ Active PayU merchant account with AFT enabled
- ✅ **Visa MCC 6540** (Money Transfer) merchant category assignment
- ✅ Completed merchant onboarding and KYC verification
- ✅ AFT feature activation through PayU merchant dashboard

### **Technical Requirements**
- ✅ Integration with PayU's `_payment` API endpoint
- ✅ Implementation of secure hash generation (SHA-512)
- ✅ Webhook endpoint for real-time transaction updates
- ✅ SSL/TLS enabled website for secure communication
- ✅ `additional_info` parameter implementation for AFT compliance

## How It Works - Process Flow

### **Step 1: Transaction Initiation**
Merchant initiates an AFT transaction through PayU's API with customer details, funding amount, and recipient information.

### **Step 2: Data Validation**
PayU validates the transaction request, including merchant credentials, recipient details, and AFT compliance parameters.

### **Step 3: Fund Processing**
The transaction is processed through Visa's AFT network to credit funds directly to the recipient's account or card.

### **Step 4: Real-time Confirmation**
PayU provides immediate transaction status updates through webhooks and API responses.

### **Step 5: Settlement and Reconciliation**
Completed transactions are included in merchant settlement reports with detailed transaction information.

## Integration Options

### **Server-to-Server (S2S) Integration**
Direct API integration for merchants who want full control over the user experience and transaction flow.

### **PayU Hosted Checkout**
Pre-built checkout interface that handles AFT transactions with minimal merchant development effort.

### **Merchant Hosted Checkout** 
Custom checkout implementation using PayU's payment processing APIs while maintaining merchant branding.

## Key API Parameters

### **Required Parameters**
- `key` - Merchant key provided by PayU
- `txnid` - Unique transaction identifier
- `amount` - Fund transfer amount
- `productinfo` - Transaction description
- `firstname`, `email`, `phone` - Customer information
- `pg=CC` and `bankcode` - Payment gateway configuration
- `additional_info` - AFT-specific recipient and sender information
- `hash` - SHA-512 security hash

### **AFT-Specific Requirements**
The `additional_info` parameter must contain:
- **Sender Information** - Details about the fund sender
- **Recipient Information** - Recipient account and personal details
- **KYC Information** - Required identification details for compliance

## Next Steps

### **Getting Started**
1. **Contact PayU Sales** - Request AFT enablement and MCC 6540 setup
2. **Review Integration Guide** - Follow detailed technical implementation steps  
3. **Test Implementation** - Use PayU's test environment for development
4. **Go Live** - Deploy to production after successful testing

### **Integration Resources**
- 📖 [Collection Payments with Account Funding Transaction](https://docs.payu.in/docs/collection-payments-with-account-funding-transaction) - Complete implementation guide
- 🔧 [API Reference](https://docs.payu.in/reference/merchant-hosted-checkout) - Technical API documentation
- 🧪 [Test Environment](https://docs.payu.in/docs/payment-testing) - Sandbox testing resources
- 📞 [Developer Support](https://docs.payu.in/docs/support) - Technical assistance and help

### **Support and Contact**
For AFT enablement, technical support, or implementation assistance:
- **Email**: [technical-support@payu.in](mailto:technical-support@payu.in)
- **Developer Portal**: [PayU Developer Documentation](https://docs.payu.in)
- **Merchant Dashboard**: [PayU Merchant Portal](https://merchant.payu.in)

---

> **Note**: Account Funding Transaction requires specific merchant category approval (Visa MCC 6540) and may not be available for all business types. Contact PayU sales team to verify eligibility and complete the enablement process.