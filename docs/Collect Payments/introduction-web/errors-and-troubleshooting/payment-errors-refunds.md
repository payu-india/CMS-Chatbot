---
title: Refund payment errors
excerpt: Refund initiation and refund status errors categorized from the PayU repo.
deprecated: false
hidden: false
metadata:
  title: Refund payment errors
  description: Refund initiation and refund status errors categorized from the PayU repo.
  robots: index
next:
  description: ''
---

These rows are categorized from existing PayU repository error-code and troubleshooting documentation for **Refund Initiation Error Codes, Refund Status Error Codes**.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_REFUNDS_BEGIN -->

## Error reference

Rows categorized: **85**.

| Source doc | Error code / type | Error message / response indicator | Description | Recommended fix |
| --- | --- | --- | --- | --- |
| Refund Initiation Error Codes | 100 | Refund Successful | 100 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 101 | Refund Successful | 101 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 104 | Confirmation required | 104 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 105 | Invalid amount | 105 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 106 | Token already exists. | 106 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 107 | Upgraded to refund | 107 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 108 | - | 108 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 111 | Invalid transaction status | 111 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 112 | - | 112 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 115 | Invalid status to be updated | 115 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 116 | Transaction Not Found | 116 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 117 | Amount Does not Match | 117 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 119 | No such Request Found | 119 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 120 | Transaction lock could not be obtained. | 120 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 122 | - | 122 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 126 | - | 126 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 127 | - | 127 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 128 | Partial refunds not allowed | 128 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 130 | Refunds not allowed after | 130 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 225 | Overdraft has occurred. Kindly recheck the status tomorrow. | 225 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 226 | Capture has been initiated today. Please check for refund status tomorrow. | 226 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 227 | Transactions with same amount and same token not allowed | 227 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 230 | Purged Transaction. Refund request requires manual follow-up | 230 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 231 | Refund could not be initiated due to some internal error | 231 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 232 | Refund could not be initiated. Either refunds are not supported or need manual intervention | 232 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 233 | Refund/Cancel Blocked From Merchant Panel. Contact KM. | 233 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 234 | Refund/Cancel Blocked From Merchant Panel And API. Contact KM. | 234 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 235 | Refund/Cancel Blocked. Contact KM. | 235 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 239 | API based alternate instant refunds not activated. | 239 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 240 | Store card failed | 240 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 241 | - | 241 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 242 | Bank Code Not Supported. Raise it to PayU support team | 242 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 243 | Virtual account setup to process instant refund is incomplete | 243 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 244 | Beneficiary Code for Virtual Account Not Set | 244 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 245 | BBPS transaction is not successful | 245 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 246 | Value is Invalid for the Merchant SKU. | 246 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 248 | - | 248 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 250 | Refund Failed On Uploading Successful Chargeback | 250 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 251 | Refund Blocked for this PGMID by Bank | 251 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 252 | Refunds are not allowed from panel for this MID | 252 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 253 | Instant refunds invalid mode | 253 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 254 | Remarks cannot contain special characters | 254 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 255 | Token Length Exceeded for Refund | 255 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 256 | Refund not supported on split transactions. Please initiate refund on the order transaction | 256 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 258 | - | 258 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 259 | - | 259 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 263 | Invalid requested amount | 263 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 267 | Lock acquired on TransactionMetaData | 267 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 270 | Transaction not eligible for Instant Refund | 270 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 299 | Blocking refund initiation for Type A Merchant | 299 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 301 | Capture already successful for this transaction | 301 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 302 | Please try after some time | 302 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 303 | Amount greater than maximum capturable amount | 303 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 304 | Amount less than allowed | 304 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 305 | Amount more than allowed | 305 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 306 | Invalid amount tolerance configuration | 306 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 424 | Transaction upgraded to capture/refund. | 424 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Initiation Error Codes | 501 | Successfully Updated | 501 | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R000 | SUCCESS | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0001 | TECHNICAL_ERROR_AT_ACQUIRER_BANK | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0002 | TECHNICAL_ERROR_AT_CUSTOMER_BANK | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0004 | CREDIT_FAILED_IN_CUSTOMER_ACCOUNT | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0005 | REFUND_NOT_PERMITTED_TO_ACCOUNT | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0006 | TECHNICAL_ERROR | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0007 | TECHNICAL_ERROR_AT_ISSUER_OR_ACQUIRER_END | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0009 | REFUND_IN_DEEMED_STATE | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0010 | ACCOUNT_DETAILS_NOT_FOUND_AT_CUSTOMER_BANK | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0011 | COMPLIANCE_DECLINE_AT_CUSTOMER_BANK | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0012 | CUSTOMER_ACCOUNT_BLOCKED | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0013 | REFUND_NOT_ALLOWED_ON_VPA | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0014 | ORIGINAL_REFUND_DETAILS_NOT_FOUND | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0015 | CUSTOMER_ACCOUNT_INACTIVE | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0016 | CUSTOMER_BANK_MAXIMUM_BALANCE_LIMIT_BREACHED | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0017 | RISK_DECLINE | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0018 | CUSTOMER_VPA_BLOCKED | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0019 | REFUND_NOT_ALLOWED_ON_OVERDRAFT_ACCOUNT | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0020 | MERCHANT_BLOCKED_BY_CUSTOMER | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0022 | CUSTOMER_BANK_NOT_HONOURING_REFUND | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0023 | TECHNICAL_ERROR_AT_ACQUIRER_BANK | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0024 | TECHNICAL_ERROR_AT_CUSTOMER_BANK | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0025 | TECHNICAL_ERROR | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R0026 | RISK_DECLINE | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R101 | IN_PROGRESS | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R102 | INSUFFICIENT_BALANCE | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |
| Refund Status Error Codes | R501 | FAILED | Refund status error | Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it. |

<!-- PAYU_REPO_PRODUCT_PAYMENT_ERRORS_PAYMENT_ERRORS_REFUNDS_END -->
