---
title: APIs used for Integration
excerpt: ''
deprecated: false
hidden: false
icon: far fa-rectangle-api
metadata:
  title: APIs used for Cross-Border Import Integration
  description: ''
  robots: index
next:
  description: ''
---
Use these APIs to collect cross-border import payments, manage trade documents and subscriptions, and reconcile payments and settlements.

### Collect payment

| Use case → Reference                                                                      | `command` / primary value | Description                                                                                                                                                   |
| ----------------------------------------------------------------------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [PayU Hosted Checkout](ref:_payment_cross-border_payu_hosted_checkout)                    | `_payment`                | Initiate a cross-border payment on PayU Hosted Checkout with `buyer_type_business` and mandatory UDF fields.                                                  |
| [Collect Payment API – Cards ](ref:_payment_cross-border_merchant_hosted_cards)           | `_payment`                | Submit merchant-hosted card payment requests for cross-border one-time transactions.                                                                          |
| [Collect Payment API – NetBanking ](ref:_payment_cross-border_merchant_hosted_netbanking) | `_payment`                | Initiate NetBanking payments for cross-border transactions. **Used in:** [NetBanking Integration](doc:netbanking-integration-merchant-hosted-integration-cb). |
| [Collect Payment API – UPI ](ref:_payment_cross-border_merchant_hosted_upi)               | `_payment`                | Initiate UPI Intent payments for cross-border transactions.                                                                                                   |

### Update transaction data and upload invoices

| Use case → Reference                         | `command` / primary value  | Description                                                                                                                                                                                                                                                                  |
| -------------------------------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [UDF Update API](ref:udf_update_api)         | `udf_update`               | Update UDF1–UDF5 values, including invoice ID, on a completed transaction. **Used in:** [Integrate Cross-Border Payments with PayU](doc:integrate-cross-border-payments-for-payubiz) and [Import Plugin Integration](doc:cross-border-payments-import-plugin-integration-1). |
| [Invoice Upload API](ref:invoice_upload_api) | `opgsp_upload_invoice_awb` | Upload invoice documents and AWB files required for bank processing and settlement.                                                                                                                                                                                          |

### Manage PACB subscriptions

| Use case → Reference                                                                     | `command` / primary value | Description                                                                                  |
| ---------------------------------------------------------------------------------------- | ------------------------- | -------------------------------------------------------------------------------------------- |
| [Payment Consent Transaction – PayU Hosted](ref:payment-consent-transaction-payu-hosted) | `_payment`                | Register a subscription mandate on PayU Hosted Checkout for cross-border recurring payments. |
| [Registration Mandate for Cards](ref:registration-mandate-for-cards-pacb)                | `_payment`                | Register a card mandate for cross-border subscription consent transactions.                  |
| [UPI Consent Transaction](ref:upi-consent-transaction-cross-border)                      | `_payment`                | Register a UPI mandate for cross-border subscription consent transactions.                   |
| [Pre-Debit Notification API](ref:pre_debit_notification_api)                             | `pre_debit_SI`            | Notify the customer at least 48 hours before executing a recurring debit.                    |
| [Recurring Payment Transaction API](ref:recurring-payment-transaction-api-pacb)          | `si_transaction`          | Execute recurring debits against a registered cross-border mandate.                          |

### Manage PACB settlements

| Use case → Reference                                                             | `command` / primary value            | Description                                                                     |
| -------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------------------------------------- |
| [Get On-Hold Transactions API](ref:get-on-hold-transactions-api)                 | `GET /opgsp/getOnHoldTxnDetails`     | Retrieve transactions held pending additional invoice or trade metadata.        |
| [Update On-Hold Transactions API](ref:update-on-hold-transactions-api)           | `POST /opgsp/updateOnHoldTxnDetails` | Submit additional customer or trade information to release on-hold settlements. |
| [Settlement Detail Range API](ref:settlement-detail-range-api-for-cross-border)  | `GET /settlement/range/`             | Retrieve paginated transaction-level settlement data for a date range or UTR.   |
| [Get Settlement Detail API](ref:get-settlement-detail-api-cross-border-payments) | `get_settlement_details`             | Retrieve settlement details for cross-border transactions.                      |

### Verify the payment

| Use case → Reference                         | `command` / primary value | Description                                                      |
| -------------------------------------------- | ------------------------- | ---------------------------------------------------------------- |
| [Verify Payment API](ref:verify_payment_api) | `verify_payment`          | Reconcile the transaction status from your server after payment. |

<Accordion title="LRS-specific APIs" icon="fa-globe">
  Cross-border transactions under the Liberalised Remittance Scheme (LRS) use additional `_payment` parameters for PAN validation, TCS declarations, and `lrs_service_type`. For the full LRS API list and integration guides, refer to [Liberalised Remittance Scheme (LRS) for Travel & Education](doc:cb-lrs-integration).
</Accordion>

<br />
