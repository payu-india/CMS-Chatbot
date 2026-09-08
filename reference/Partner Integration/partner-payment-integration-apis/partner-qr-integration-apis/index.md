---
title: Partner QR Integration APIs
deprecated: false
hidden: true
metadata:
  robots: index
---
# Partner QR Payment Integration APIs

Partner QR Payment Integration APIs enable partners to collect payments using **Bharat QR (BQR)** on omni-channel soundbox devices. Unlike Hosted Checkout or UPI S2S partner APIs that use a Bearer token only, QR wrapper APIs require **dual authentication**: an OAuth access token (`partner_payments` scope) **and** an HMAC request signature on every call.

The following steps allow you to integrate Partner QR payments:

1. Get OAuth access token and sign requests 
2. Initiate payment request →
3. Generate dynamic QR
4. Check BQR transaction status →

---

## Environment

| | |
| --- | --- |
| UAT Base URL | `https://apitest.payu.in/apilayer/partner` |
| PROD Base URL | `https://api.payu.in/apilayer/partner` |

All endpoints below are relative to the base URL above.

---

## APIs in this flow

| Step | Description | Endpoint |
| --- | --- | --- |
| 0 | Authentication (OAuth + HMAC) | See [Authentication for Partner QR APIs](authentication-partner-qr-apis) |
| 1 | Initiate payment and get `mihpayId` | `POST /initiatePayment` |
| 2 | Generate dynamic QR for soundbox | `POST /dbqr` |
| 3 | Check BQR transaction status | `POST /transaction/verifyStatus` |

---

## Prerequisites

PayU provides the following during partner onboarding:

| Credential | Used for |
| --- | --- |
| Client ID | OAuth token request; HMAC `username` in `Authorization` header |
| Client Secret | OAuth token request; HMAC signature computation |
| Reseller UUID | `X-PayU-Reseller-UUID` header on every API call |
| Merchant key | `accountId` in Initiate Payment body; `X-PayU-Merchant-Key` header on APIs 2 and 3 |

Before calling QR APIs:

- Obtain an access token with `scope=partner_payments`
- Ensure the merchant is **linked** to your partner account in the PayU reseller portal
- Sign each request body with HMAC before sending (see Authentication page)

---

## Merchant identification

Partners send the **merchant key** only (never numeric merchant ID):

| API | Where to send merchant key |
| --- | --- |
| Initiate Payment | `accountId` field in JSON **body** |
| Generate Dynamic QR | `X-PayU-Merchant-Key` **header** |
| Check BQR Transaction Status | `X-PayU-Merchant-Key` **header** |


