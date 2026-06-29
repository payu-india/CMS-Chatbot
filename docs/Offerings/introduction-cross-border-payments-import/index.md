---
title: Cross-Border Payments
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: PayU Cross-Border Payments Introduction
  description: >-
    The PayU Cross-Border Payments Introduction page provides an overview of
    PayU's Cross-Border Payments - Import Integration, which allows overseas
    sellers to collect payments from buyers in India and facilitate the transfer
    of funds to the sellers' accounts in their native currency with reduced
    settlement times.


    The page emphasizes that Indian consumers can purchase products from
    international merchants without the need for these merchants to have a
    physical presence or establishment in India. PayU acts as the intermediary,
    handling the settlement process through Authorized Dealer (AD) banks in the
    merchant's native currency.
  keywords:
    - Cross-Border Payments intro
    - Cross-Border Payments Introduction
  robots: index
next:
  description: ''
---
Merchants outside India, who are willing to serve Indian consumers without establishment entities in India can collect payments from Indian customers. The settlement will be done to an offshore account directly by PayU through AD banks in the merchant’s native currency. The payment methods supported for cross-border payments are Cards (Debit & Credit), Net Banking, UPI and NEFT/RTGS.

PayU **Cross-Border Payments – Import** Integration facilitates overseas sellers to collect payments from buyers in India and transfer the funds to the overseas seller:

* In their desired currency (100+ options)
* With T+2/T+3 settlement time

This is as per the [RBI guidelines for Payment Aggregators - Cross Border](https://rbi.org.in/Scripts/NotificationUser.aspx?Id=12896\&Mode=0) - RBI/DPSS/2025-26/141
CO.DPSS.POLC.No.S-633/02-14-008/2025-26

<Callout icon="📘" theme="info">
  **Note**: RBI monitors cross-border payments with the support of AD banks. Hence, there are guidelines to be followed by AD Bank and PayU.
</Callout>

## Advantages

The advantages for the overseas merchant include: 

* International merchants are looking at simplified market entry into India. They want partners who can eliminate operational complexities by operating through local merchants of record with knowledge of the Indian market. 
* Merchants are looking to tap the Indian eCommerce market by offering them the majority of the local payment methods like Net Banking, Rupay cards, and local card processing with higher transaction success rates. 

Merchants cannot sell products / services for more than Rs. 25,00,000 (approx ~USD 27,000) per transaction.

* Every transaction must be accompanied with buyer's details - First Name, Last Name & Billing Zipcode
* Every transaction must be accompanied by an "invoice ID"
* Every transaction must be accompanied by a copy of the AWB once the product(s) has been shipped (applicable in case of physical goods)

The customers or end-users will be able to pay using their Indian debit cards and Net Banking on merchant’s websites, which was till now accepted only foreign transactions enabled credit cards.

## Benefits

* The amount can be settled early to merchants, that is, within T+2 / T+3 days.
* Reconciliation and settlement queries can be directly raised to PayU.
* Overseas merchants can easily offer services to Indian consumers.

To get started with integration, refer to: [Integrate Import for PayUBiz](doc:integrate-cross-border-payments-for-payubiz). For Subscriptions with various payment methods, refer to [Subscriptions with Cross-Border Payments](doc:cb-subscription-integration-seamless).

## APIs used in Cross-Border Payments – Import integration

| API name | Purpose |
| --- | --- |
| [PayU Hosted Checkout – CB](ref:_payment_cross-border_payu_hosted_checkout) | Initiate cross-border payments on PayU Hosted Checkout with `buyer_type_business` and mandatory UDF fields.  |
| [Collect Payment API – Cards (Cross-Border)](ref:_payment_cross-border_merchant_hosted_cards) | Submit merchant-hosted card payment requests for cross-border one-time transactions.|
| [Collect Payment API – NetBanking (Cross-Border)](ref:_payment_cross-border_merchant_hosted_netbanking) | Initiate NetBanking payments for cross-border transactions. **Used in:** [NetBanking Integration](doc:netbanking-integration-merchant-hosted-integration-cb). |
| [Collect Payment API – UPI (Cross-Border)](ref:_payment_cross-border_merchant_hosted_upi) | Initiate UPI Intent payments for cross-border transactions.|
| [UDF Update API](ref:udf_update_api) | Update UDF1–UDF5 values (including invoice ID) on a completed transaction. **Used in:** [Integrate Cross-Border Payments with PayU](doc:integrate-cross-border-payments-for-payubiz), [Import Plugin Integration](doc:cross-border-payments-import-plugin-integration-1). |
| [Invoice Upload API](ref:invoice_upload_api) | Upload invoice documents and AWB files required for bank processing and settlement. |
| [Payment Consent Transaction – PayU Hosted](ref:payment-consent-transaction-payu-hosted) | Register a subscription mandate on PayU Hosted Checkout for cross-border recurring payments. |
| [Registration Mandate for Cards – PACB](ref:registration-mandate-for-cards-pacb) | Register a card mandate for cross-border subscription consent transactions.|
| [UPI Consent Transaction – CB](ref:upi-consent-transaction-cross-border) | Register a UPI mandate for cross-border subscription consent transactions. |
| [Pre-Debit Notification API](ref:pre_debit_notification_api) | Notify the customer before executing a recurring debit (required at least 48 hours in advance).|
| [Recurring Payment Transaction API – PACB](ref:recurring-payment-transaction-api-pacb) | Execute recurring debits against a registered cross-border mandate.|
| [Get On-Hold Transactions API – CB](ref:get-on-hold-transactions-api) | Retrieve transactions held pending additional invoice or trade metadata. . |
| [Update On-Hold Transactions API – CB](ref:update-on-hold-transactions-api) | Submit additional customer or trade information to release on-hold settlements.  |
| [Settlement Detail Range API – CB](ref:settlement-detail-range-api-for-cross-border) | Retrieve paginated transaction-level settlement data for a date range or UTR.|
| [Get Settlement Detail API – CB](ref:get-settlement-detail-api-cross-border-payments) | Retrieve settlement details for cross-border transactions. |
| [Verify Payment API](ref:verify_payment_api) | Server-side reconciliation of transaction status after payment. |
<Accordion title="LRS-specific APIs" icon="fa-globe">
  Cross-border transactions under the Liberalised Remittance Scheme (LRS) use additional `_payment` parameters for PAN validation, TCS declarations, and `lrs_service_type`. For the full LRS API list and integration guides, refer to [Liberalised Remittance Scheme (LRS) for Travel & Education](doc:cb-lrs-integration).
</Accordion>
