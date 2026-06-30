---
title: APIs for UPI QR Integration
excerpt: ''
deprecated: false
hidden: true
link:
  url: https://docs.payu.in/docs/integrate-upi-qr
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The following APIs used for UPI QR integration:

- [Dynamic QR Generation API](ref:dynamic-qr-generation-api)
- [Insta Static QR Generation API](https://docs.payu.in/reference/insta-static-qr-generation-api)
- [Insta Deactivate VPA API](https://docs.payu.in/reference/insta-deactivate-vpa-api)
- [Insta Static QR Regeneration API](https://docs.payu.in/reference/insta-static-qr-regeneration-api)
- [Integrated Static Bharat QR Generation API](https://docs.payu.in/reference/integrated-static-bharat-qr-generation-api)
- [Payment Initiation API – Integrated Bharat QR](https://docs.payu.in/reference/payment-initiation-api-integrated-bharat-qr)
- [Offline Intent Link Generation API](https://docs.payu.in/reference/offline-intent-link-generation-api)
- [Expire Intent Link API](https://docs.payu.in/reference/expire-intent-link-api)
- [Print Invoice QR API](https://docs.payu.in/reference/print-invoice-qr-api)
- [Send Invoice QR to SMS API](https://docs.payu.in/reference/send-invoice-qr-to-sms-api)
- [Transaction Callback API](https://docs.payu.in/reference/transaction-callback-api)
- [Transaction Status Check API](https://docs.payu.in/reference/transaction-status-check-api-2)
- [Cancel QR Transaction API](https://docs.payu.in/reference/cancel-qr-transaction-api-1)

<Callout icon="📘" theme="info">
  ### Reference

  - To imitate refund for a transaction, refer to [Refund Transaction API](ref:refund_transaction_api).
  - For error codes, refer to [Error codes for QR APIs](https://docs.payu.in/reference/error-codes-for-qr-apis-1).
</Callout>

## Testing UPI QR

<Callout icon="⚠️" theme="warn">
  ### **UPI QR test limitations:**

  - UPI QR transactions require the `DBQR` flag to be activated on your merchant account. If you receive an error when posting with `pg=DBQR` and `bankcode=UPIDBQR`, contact your KAM to enable this feature.
  - UPI QR in the test environment may show failures that do not replicate in production. If UPI QR transactions fail consistently in UAT with no clear error, contact [integration@payu.in](mailto:integration@payu.in) with your MID and a sample transaction ID for investigation.
  - Ensure `txn_s2s_flow=4` is included in your QR payment request. Without this flag, the DBQR flow will not initiate correctly.
</Callout>

<br />