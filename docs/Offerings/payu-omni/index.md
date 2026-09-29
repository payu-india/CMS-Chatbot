---
title: PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
---
title: PayU Omni
excerpt: Accept in-person payments seamlessly with PayU's POS solution
category: 65ee4b13ba7bd6003d0c61b4
slug: payu-omni
---

PayU Omni is PayU's comprehensive Point of Sale (POS) solution that enables merchants to accept in-person payments through secure, reliable POS devices. Designed for retail stores, restaurants, and service providers, PayU Omni supports multiple payment methods including Cards, UPI DBQR, QR codes, Wallets, and EMI options.

---

## How it Works?

PayU Omni enables seamless in-person payment collection through an integrated flow between your billing system, PayU's API, and physical POS devices. Here's the complete flow:

1. **Customer Makes Purchase:** Customer selects products/services and is ready to pay at your physical location (store, restaurant, service center).

2. **Merchant Creates Order:** Your cashier creates an order in your **ERP/billing/ordering system** with the transaction amount and customer details.

3. **System Initiates Payment:** Your ERP/billing system calls the **PayU Omni Initiate Payment API** with the transaction details and the specific `posDeviceId` for the POS device at that counter.

4. **PayU Processes Request:** PayU validates the request, verifies the device is active and mapped to your merchant account, and processes the authentication.

5. **Device Receives Payment Push:** The PayU POS device at your location receives a notification to collect payment and displays the transaction amount to the customer.

6. **Customer Selects Payment Method:** Customer chooses their preferred payment method on the device (Card swipe/tap, UPI QR scan, Wallet, EMI).

7. **Payment is Processed:** Customer completes the payment (enters PIN, scans QR code, etc.). PayU processes the payment through the selected payment network.

8. **Transaction Confirmation:** The POS device displays the transaction result (success/failure) and prints a receipt for the customer.

9. **Webhook Notification:** PayU sends a webhook notification to your server with the complete transaction status and details, which updates your ERP/billing system in real-time.

<Warning>
**Critical Prerequisite:** Your POS device **MUST be activated and mapped to your merchant account** in the PayU Partner Dashboard before it can receive payment notifications. See [Device Activation Requirements](#prerequisites) below.
</Warning>

---

## Customer Journey

<!-- diagram: Customer journey flow showing ERP system → PayU API → POS Device → Customer → Webhook back to ERP -->

**Flow:**  
Customer at Counter → Cashier Creates Order in ERP → ERP Calls PayU API → Device Receives Payment Push → Customer Selects Payment Method → Payment Processed → Receipt Printed → Webhook Sent to ERP

---

## Features of PayU Omni

### Multi-Payment Method Support
Accept all major payment methods on a single device:
- **Cards:** Visa, Mastercard, RuPay (Debit & Credit) via swipe, chip, or contactless tap
- **UPI DBQR:** Dynamic Bharat QR for UPI payments
- **QR Codes:** Generate QR codes for customer scanning
- **Wallets:** Paytm, PhonePe, Amazon Pay, and more
- **EMI:** Convert high-value transactions to EMI at checkout

### Multiple Device Types
Choose from three device categories based on your business needs:
- **mPOS (mobile POS):** Portable, battery-powered devices for mobility
- **Android POS:** Full-featured Android devices with touchscreen
- **Static POS:** Counter-mounted devices for fixed checkout locations

### Real-Time Webhook Notifications
Receive instant payment status updates via secure webhooks to keep your billing system synchronized.

### Automated Receipt Printing
Built-in thermal printer generates customer receipts automatically after each transaction.

### Partner API Integration
Seamlessly integrate with your existing ERP, billing, or ordering system through RESTful APIs with comprehensive authentication and security.

### Secure Transactions
All transactions are encrypted and compliant with PCI-DSS standards, ensuring customer payment data security.

---

## Benefits of PayU Omni

### For Merchants
- **Faster Checkouts:** Reduce queue times with quick, reliable payment processing
- **Single Integration:** One API integration supports all payment methods and device types
- **Real-Time Reconciliation:** Instant webhook notifications enable automatic reconciliation
- **Lower MDR:** Competitive merchant discount rates across payment methods
- **Device Flexibility:** Choose devices that match your business environment

### For Customers
- **Payment Choice:** Multiple payment options at the point of sale
- **Contactless Payments:** Tap-and-pay for cards and UPI QR scanning for safety
- **Instant Confirmation:** Immediate receipt and payment confirmation
- **EMI Options:** Convert purchases to EMI on eligible transactions

### For Partners/Aggregators
- **Scalable Integration:** Single API endpoint to manage payments across multiple merchants
- **Device Management Dashboard:** Centralized view and control of all devices across merchants
- **Automated Token Management:** OAuth 2.0 token-based authentication for secure API access
- **Comprehensive Webhooks:** Real-time transaction updates for all merchants

---

## Prerequisites

Before integrating with PayU Omni, ensure you have completed the following:

<Warning>
### Device Must Be Activated

**Every POS device MUST be activated and mapped to a merchant account before it can process payments.**

If you attempt to initiate a payment with an inactive or unmapped device, you will receive error code **E342** or **E343** and the transaction will fail.
</Warning>

### Required Setup Steps

<Info>
**1. Partner Registration**

- Sign up for a Partner account at [partner.payu.in/app/account/signup](https://partner.payu.in/app/account/signup)
- You will receive: `client_id`, `client_secret`, and `uuid`
- Store these credentials securely (required for API authentication)
</Info>

<Info>
**2. Merchant Account Setup**

- Each merchant you serve must have an active PayU merchant account
- Obtain merchant's `key` and `salt` (unique per merchant)
- Verify merchant account has payment methods enabled (Card, UPI, etc.)
</Info>

<Info>
**3. Device Activation & Mapping**

- Log in to PayU Partner Dashboard
- Add each POS device using its serial number
- **Map each device to the specific merchant account** that will use it
- Enable required payment methods for each device
- Copy the `posDeviceId` value (required for API calls)
- Verify device status shows "Active"

**Important:** Each device can only be mapped to ONE merchant at a time. Payment methods must be enabled at BOTH merchant level AND device level.
</Info>

<Info>
**4. Required Configurations**

- Configure webhook URL in Partner Dashboard (HTTPS required)
- Whitelist PayU IP addresses in your firewall
- Ensure POS devices have stable internet connectivity
- Test all payment methods before going live
</Info>

---

## Next Steps

To integrate PayU Omni with your system, refer to:

- **[Collect Payment Using PayU Omni →](doc:collect-payment-using-payu-omni)**  
  Complete integration guide with device activation, API calls, testing, and troubleshooting

- **[Initiate Payment API Reference →](doc:initiate-payment-api-omni)**  
  Detailed API specification for initiating payments

- **[Check Transaction Status API Reference →](doc:check-transaction-status-api-omni)**  
  Query payment status for verification and reconciliation

---

> 📮 **Postman Collection**  
> Download the PayU Omni Postman Collection: [Coming Soon]

> 💬 **Need Help?**  
> Contact Integration Support: **integration-support@payu.in**
