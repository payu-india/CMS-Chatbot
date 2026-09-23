---
title: Banking Connect - IBMB or NBBL
deprecated: false
hidden: true
metadata:
  robots: index
---
NBBL Banking Connect is PayU's implementation of NPCI Bharat BillPay Limited's standardized NetBanking framework. It modernizes NetBanking without changing a merchant's existing NetBanking integration.

Customers authenticate inside their own bank app instead of entering NetBanking credentials on a merchant or PayU page. On mobile, the customer can use a bank-app deep link. On desktop, the customer can scan a NetBanking QR code with a bank app. If the app-first path is unavailable, the journey can fall back to the familiar bank-website flow.

## Why merchants use Banking Connect

- **Mobile-first journey:** Customers complete payment in the bank app.
- **Password-free checkout:** Customers do not need to remember or enter NetBanking User IDs and passwords during checkout.
- **High-value payments:** NetBanking continues to support high-value, uncapped payments.
- **No integration change:** Existing merchant NetBanking integrations remain unchanged.
- **Phased rollout:** PayU can enable banks individually or use traffic splits before a broader rollout.
- **Existing operations:** The reconciliation and settlement processes do not change.

## Payment journeys

| Journey          | Customer device       | How the customer pays                                                                    |
| ---------------- | --------------------- | ---------------------------------------------------------------------------------------- |
| App intent       | Mobile browser or app | Selects a bank and opens the installed bank app through a deep link.                     |
| QR               | Desktop or web        | Scans a NetBanking QR code with the bank's mobile app.                                   |
| Website fallback | Any supported device  | Continues through the familiar bank website flow when the app-first path is unavailable. |

For the detailed customer journey, see [PayU Hosted Customer Journey - Banking Connect](./payu-hosted-customer-journey-banking-connect.md).

For Android and iOS WebView implementations, see [Handle NBBL Deep-Links in WebView](./handle-nbbl-deep-links-in-webview.md).

## Supported banks

The attached product brief lists these banks as currently live via NBBL:

- HDFC Bank
- ICICI Bank
- Axis Bank
- YES Bank

The brief lists these banks as coming soon:

- SBI
- IDBI Bank
- Bank of Baroda
- IDFC FIRST Bank
- Canara Bank
- Kotak Mahindra Bank
- CSB Bank
- Federal Bank
- AU Small Finance Bank
