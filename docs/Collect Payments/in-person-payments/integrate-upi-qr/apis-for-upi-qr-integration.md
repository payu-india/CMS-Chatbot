---
title: APIs used for Integration
excerpt: ''
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs for UPI QR Integration
  description: ''
  robots: index
next:
  description: ''
---
| API                                                                                              | Purpose                                                                |
| ------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------- |
| [Dynamic QR Generation API](ref:dynamic-qr-generation-api)                                       | Generate a dynamic UPI QR for offline payment collection               |
| [Insta Static QR Generation API](ref:insta-static-qr-generation-api)                             | Generate a static UPI or Bharat QR for repeat collections              |
| [Insta Deactivate VPA API](ref:insta-deactivate-vpa-api)                                         | Permanently deactivate the VPA embedded in an Insta static QR          |
| [Insta Static QR Regeneration API](ref:insta-static-qr-regeneration-api)                         | Regenerate a previously created Insta static UPI or Bharat QR          |
| [Integrated Static Bharat QR Generation API](ref:integrated-static-bharat-qr-generation-api)     | Generate an integrated static UPI or Bharat QR                         |
| [Payment Initiation API – Integrated Bharat QR](ref:payment-initiation-api-integrated-bharat-qr) | Initiate payment towards an integrated static QR                       |
| [Offline Intent Link Generation API](ref:offline-intent-link-generation-api)                     | Generate a UPI Intent link for customer payment                        |
| [Expire Intent Link API](ref:expire-intent-link-api)                                             | Expire one or more UPI Intent links                                    |
| [Print Invoice QR API](ref:print-invoice-qr-api)                                                 | Generate a printable dynamic UPI QR for invoices                       |
| [Send Invoice QR to SMS API](ref:send-invoice-qr-to-sms-api)                                     | Send payment confirmation SMS after a transaction                      |
| [Transaction Callback API](ref:transaction-callback-api)                                         | Receive transaction status on your webhook after QR payment processing |
| [Transaction Status Check API](ref:transaction-status-check-api-2)                               | Check the status of a QR transaction                                   |
| [Cancel QR Transaction API](ref:cancel-qr-transaction-api-1)                                     | Cancel an initiated QR transaction                                     |

<br />

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