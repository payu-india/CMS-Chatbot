---
title: PayU Omni
deprecated: false
hidden: true
icon: far fa-arrow-left-from-dotted-line
metadata:
  robots: index
---
# PayU Omni — Integrated Flow

PayU Omni — Integrated Flow is a seamless payment solution that allows merchants to integrate their billing or ordering systems directly with PayU-enabled payment devices. This integration enables order-level payment linking, ensuring every transaction on your POS device or Dynamic QR display is mapped to a specific order in your system.

With support for **Card payments** (RuPay, Visa, Mastercard) and **Dynamic DBQR (UPI)**, PayU Omni Integrated Flow brings together the convenience of modern payment acceptance with the control of real-time reconciliation.

---

## How it works?

PayU Omni Integrated Flow creates a direct link between your billing system and PayU payment devices. Here's the end-to-end process:

1. **Order Creation** — Your billing/ordering system generates a new order (invoice, bill, booking, etc.)
2. **Payment Initiation** — Your server calls the PayU Initiate Payment API with order details and the target device ID
3. **Device Activation** — The specified PayU device (POS terminal or DBQR display) receives the payment request and activates for that specific order
4. **Customer Payment** — The customer pays using their card (swipe/tap/chip) or scans the Dynamic DBQR with their UPI app
5. **Payment Processing** — The payment network (card network or NPCI UPI) authorizes and processes the transaction
6. **Real-Time Notification** — PayU sends a webhook to your server with the transaction result (success/failure)
7. **Status Verification** — Your server calls the Check Transaction Status API to retrieve complete transaction details
8. **Reconciliation** — Your billing system updates the order status and prints/displays the receipt
9. **Settlement** — Funds are settled to your bank account as per your agreement with PayU

<!-- diagram: Sequence diagram showing Billing System → PayU API → Payment Device → Payment Network → Webhook → Status API flow -->

---

## Customer Journey

From a customer's perspective, PayU Omni Integrated Flow delivers a fast, frictionless payment experience:

**Step 1:** Customer places order at merchant location (store, restaurant, clinic, etc.)

**Step 2:** Merchant generates bill in their billing system

**Step 3:** Billing system automatically pushes payment request to the linked POS device or displays a Dynamic QR code

**Step 4:** Customer sees the exact order amount on the device screen or QR display

**Step 5:** Customer pays using:
   - **Card:** Tap, swipe, or insert card into the POS terminal
   - **UPI:** Scan the Dynamic DBQR with any UPI app (Google Pay, PhonePe, Paytm, etc.)

**Step 6:** Customer receives instant payment confirmation on the device/app

**Step 7:** Customer receives printed or digital receipt with transaction details

**Step 8:** Merchant's billing system updates order status automatically

**Step 9:** Customer leaves with confirmed payment and receipt

<!-- diagram: Customer journey flowchart showing customer actions, device interactions, and merchant system updates -->

---

## Features of PayU Omni — Integrated Flow

**1. Order-Linked Payments**  
Every payment request is tied to a specific order ID (`txnId`) from your billing system, eliminating manual reconciliation errors.

**2. Multi-Device Support**  
Works with three device types:
   - **Android POS** — Accepts cards + DBQR, with receipt printing
   - **All-in-One Device with Soundbox** — Accepts cards + DBQR, with audio payment confirmation
   - **DBQR Display** — Displays Dynamic QR codes for UPI payments only

**3. Card Payment Acceptance**  
Accept all major card types: RuPay, Visa, and Mastercard via EMV chip, contactless tap, or magnetic stripe.

**4. Dynamic DBQR (UPI) Payments**  
Generate order-specific QR codes that customers scan with any UPI app. Each QR is valid only for that order amount.

**5. Forced Payment Routing**  
Control which payment method appears on the device using `posPaymentMethod` parameter (`"sale"` for card only, `"qr"` for DBQR only).

**6. Automated Receipt Printing**  
Include custom receipt fields via the `printInfo` parameter. Devices with printers automatically generate receipts post-payment.

**7. Soundbox Audio Confirmation**  
All-in-One devices announce payment success audibly, useful in noisy environments or for visually impaired merchants.

**8. Real-Time Webhooks**  
Receive instant server-to-server notifications when payment succeeds or fails, enabling immediate order fulfillment.

**9. GST-Ready Invoicing**  
Pass GST parameters (`gstIn`, `gst`, `cgst`, `sgst`, `igst`, `cess`) in the payment request for automatic GST-compliant receipts.

**10. Custom Fields (UDFs)**  
Use `field1` through `field9` to pass custom data (table number, customer name, salesperson ID, etc.) that appears in reports and webhooks.

**11. Transaction Status API**  
Query any transaction anytime using the Check Transaction Status API to retrieve complete payment metadata, refund status, and settlement details.

---

## Benefits of PayU Omni — Integrated Flow

**✅ Faster Checkout**  
Eliminate manual entry of payment amounts on devices. Amount auto-populates from your billing system, reducing checkout time by 40-60%.

**✅ Higher Conversion Rates**  
Customers trust order-linked payments. The displayed amount matches their bill exactly, increasing payment completion rates.

**✅ Accurate Reconciliation**  
Every payment is tagged with your order ID. End-of-day reconciliation becomes a simple database query, not manual matching.

**✅ Flexible Payment Acceptance**  
One integration, multiple payment methods. Accept cards and UPI without separate integrations or terminals.

**✅ Real-Time Visibility**  
Know instantly when a payment succeeds or fails. No waiting for settlement reports to update order status.

**✅ Branded Receipts**  
Customize receipt fields with your branding, customer details, and compliance information via the `printInfo` parameter.

**✅ GST Compliance Built-In**  
Automatically generate GST-compliant receipts when you pass GST parameters. No manual invoice generation needed.

**✅ Developer-Friendly APIs**  
RESTful APIs with JSON payloads, HMAC authentication, and comprehensive webhooks. Build once, scale effortlessly.

---

## Next Steps

To integrate PayU Omni Integrated Flow with your billing system, refer to:

**Integration Guides:**
- [Integrate PayU Omni — Initiate Payment](#integrate-payu-omni-initiate-payment) — Learn how to push payment requests to your devices
- [Integrate PayU Omni — Check Transaction Status](#integrate-payu-omni-check-transaction-status) — Learn how to verify and reconcile transactions

**API References:**
- [Initiate Payment API Reference](#initiate-payment-api) — Complete API specification for payment initiation
- [Check Transaction Status API Reference](#check-transaction-status-api) — Complete API specification for status checks

> 📮 **Postman Collection**  
> Download the PayU Omni Postman Collection from: [Collection URL placeholder — contact PayU support]
