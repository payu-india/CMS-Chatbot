---
title: Partner QR Integration APIs
deprecated: false
hidden: true
metadata:
  robots: index
---
Partner QR Payment Integration APIs enable partners to collect payments using **Bharat QR (BQR)** on omni-channel soundbox devices. Unlike Hosted Checkout or UPI S2S partner APIs that use a Bearer token only, QR wrapper APIs require **dual authentication**: an OAuth access token (`partner_payments` scope) **and** an HMAC request signature on every call.

The following steps allow you to integrate Partner QR payments:

1. Get OAuth access token and sign requests: For more information, refer to [Authentication for Partner QR APIs.](https://docs.payu.in/reference/authentication-for-partner-qr-apis)
2. Initiate payment request: For more information, refer to [Initiate Payment.](https://docs.payu.in/reference/initiate-payment-partner-qr-integration)
3. Generate dynamic QR: For more information, refer to [Generate Dynamic QR.](https://docs.payu.in/reference/generate-dynamic-qr-partner-qr-integration)
4. Check BQR transaction status: For more information, refer to [Check BQR Transaction Status.](https://docs.payu.in/reference/check-bqr-transaction-status-partner-qr-integration)
