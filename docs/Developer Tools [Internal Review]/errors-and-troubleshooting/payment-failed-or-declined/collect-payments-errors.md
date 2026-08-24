---
title: Collect Payments Errors
excerpt: Collect payments failure and decline errors with recommended fix.
deprecated: false
hidden: true
metadata:
  robots: index
---
Below are the errors associated with Collect Payments, along with their descriptions, and recommended fix.

Use this page with [Payment Failed or Declined](doc:payment-failed-declined) for debugging guidance and retry handling.

## Category Alignment

Primary categories: Authentication and authorization errors and Payment failures. Includes Collect Payments auth-stage (`AUC*`, `AUTH*`, `3DS_*`) and bank/payment-method errors.

<Accordion title="Errors and Fixes" icon="far fa-screwdriver-wrench">
  \<AdvancedTable
  data=\{\[ {
    'bank_code': '`E000`',
    'description': 'NO_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'OTP Generated Successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E348`',
    'description': 'ISSUER_DECLINED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9202`',
    'description': 'PARTIAL_AMOUNT_ APPROVED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9203`',
    'description': 'APPROVED_VIP',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E207`',
    'description': 'INVALID_TRANSACTION',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E715`',
    'description': 'INVALID_AMOUNT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E305`',
    'description': 'CARD_NUMBER_ INVALID',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9204`',
    'description': 'APPROVED_TRACK',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9205`',
    'description': 'CUSTOMER_ CANCELLATION',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9206`',
    'description': 'CUSTOMER_DISPUTE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E345`',
    'description': 'TECHNICAL_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E308`',
    'description': 'TRANSACTION_FAILED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9207`',
    'description': 'NO_ACTION_TAKEN_',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9208`',
    'description': 'SUSPECTED_ MALFUNCTION',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9209`',
    'description': 'UNACCEPTABLE_ TRANSACTION_FEE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9210`',
    'description': 'FILE_UPDATE_NOT_ SUPPORTED_BY_RECEIVER',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9212`',
    'description': 'DUPLICATE_FILE_ UPDATE_RECORD',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9213`',
    'description': 'FILE_UPDATE_ FIELD_EDIT_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9214`',
    'description': 'FILE_UPDATE_ FILE_LOCKED_OUT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9215`',
    'description': 'FILE_UPDATE_ NOT_SUCCESSFUL',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E341`',
    'description': 'INVALID_MERCHANT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E2102`',
    'description': 'TXN_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9216`',
    'description': 'COMPLETED_ PARTIALLY',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E324`',
    'description': 'CARD_FRAUD_ SUSPECTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E325`',
    'description': 'RESTRICTED_ CARD',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9217`',
    'description': 'ALLOWABLE_PIN_ TRIES_EXCEEDED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E224`',
    'description': 'VIRTUAL_ACCOUNT_ NUMBER_MISMATCH',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Challenge failed`',
    'description': 'Indicates that the Access Control Server returned a negative response, typically due to incorrect input or customer cancellation.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E310`',
    'description': 'LOST_CARD',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9218`',
    'description': 'REQUESTED_FUNCTION_ NOT_SUPPORTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9252`',
    'description': 'NO_UNIVERSAL_ ACCOUNT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E717`',
    'description': 'INVALID_ACCOUNT_ NUMBER',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E307`',
    'description': 'DO_NOT_HONOUR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E706`',
    'description': 'INSUFFICIENT_ FUNDS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E707`',
    'description': 'INVALID_PAN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E710`',
    'description': 'INVALID_PIN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E4346`',
    'description': 'NO_CARD_ RECORD_REMITTER',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E1642`',
    'description': 'CARD_NOT_ PERMITTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E1903`',
    'description': 'AUTHORIZATION_FAILED_ BY_BANK',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E337`',
    'description': 'NOT_CAPTURED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E909`',
    'description': 'TRANSACTION_MAX_ LIMIT_EXCEEDED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E1626`',
    'description': 'RESTRICTED_CARD_TYPE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E312`',
    'description': 'BANK_DENIED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9253`',
    'description': 'AMOUNT_INCORRECT_ MISMATCH',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9219`',
    'description': 'CARD_ACCEPTOR_CALL_ ACQUIRER_SECURITY',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9221`',
    'description': 'MOBILE_NUMBER_ RECORD_NOT_FOUND',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E1629`',
    'description': 'BANK_TECHNICAL_ FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9222`',
    'description': 'APPROVED_ANZ_ ONLY',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E1625`',
    'description': 'CARD_NOT_ENABLED_ FOR_ECOMM_TXN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9223`',
    'description': 'CRYPTOGRAPHIC_ ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E4519`',
    'description': 'Insufficient_Amount',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9224`',
    'description': 'NO_ENVELOPE_ INSERTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9225`',
    'description': 'UNABLE_TO_ DISPENSE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9254`',
    'description': 'BANK_NOT_ SUPPORTED_BY_ SWITCH',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E225`',
    'description': 'TRANSACTION_ IN_PROGRESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E1656`',
    'description': 'RECONCILE_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9229`',
    'description': 'RECONCILIATION_ TOTALS_RESET',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9230`',
    'description': 'EXCEEDS_CASH_ LIMIT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`E9231`',
    'description': 'RESERVED_FOR_ NATIONAL_USE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Authentication failed`',
    'description': 'Occurs when authentication fails with status N or U. This may happen when the customer enters incorrect details or the issuer rejects the authentication attempt.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Authorization failed`',
    'description': 'Occurs when authentication succeeds but the authorization request is declined by the issuing bank due to reasons such as insufficient funds or limits.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Bank was unable to authenticate.`',
    'description': 'DEFAULT_VALUE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': '-',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Application error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Transaction Completed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Wrong transaction state',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:-BEPG-0000013:Rupay transaction error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': '?:waiting authentication',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:-BEPG-0000017:Issuer authentication failure',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'E303 | SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'RREQ_NOT_RECEIVED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'ACS_REDIRECT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Approved or completed successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Invalid Otp',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'No Error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'AUTHORIZED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'GW00201 | Transaction not found',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Function performed error-free',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Successful approval/completion or that V.I.P. PIN verification is valid',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'TRANSACTION_INVALID',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCINVALID`',
    'description': 'AUCINVALID',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCINVALID`',
    'description': 'Invalid Otp',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Approved or completed successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Invalid Otp',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Wrong transaction state',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'AUCNEGATIVE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'UNKNOWN_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'GW00201 | Transaction not found',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHERROR`',
    'description': 'AUTHERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHERROR`',
    'description': 'AUTHORIZATION_FAILED_BY_BANK',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'AUTHNEGATIVE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'INTERNAL_SERVER_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'IPAY0100357 | IPAY0100357-Transaction declined due to OTP Page refreshed.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction state is invalid',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Issuer unavailable or switch inoperative',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Restricted card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Blc| | Blc|',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'BANK_DENIED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Approved or completed successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Insufficient funds/over credit limit / Not sufficient funds',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'GV00013 | Invalid payment id',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Do not honor',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'UNKNOWN_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid Otp',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'AUTHORIZATION_FAILED_BY_BANK',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Issuer Insufficient Funds',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction Completed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'MRN passed in request is duplicate',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'duplicate request, another txn already SUCCESS with same details',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'DUE | Charge status: DUE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Issuer Declined',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'NPCI96 | NPCI96 - SYSTEM ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'T1 | Direct Authorize charge status check failed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`No Error`',
    'description': 'Successful transaction',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Approved or completed successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'REDIRECT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'UNKNOWN_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Transaction Completed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Application error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'GW00201 | Transaction not found',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'ACS response received',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': '?:waiting authentication',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'system unavailable',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Bank network is unavailable at the moment.`',
    'description': 'AUTHENTICATION_SERVICE_UNAVAILABLE_ASU',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'RTO | Network Read Time Out',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Authentication was attempted but was not available at banks end`',
    'description': 'AUTHENTICATION_ATTEMPTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'AUTHENTICATION_FAILED|Encountered a Payer Authentication problem. Payer could not be authenticated. | CONSUMER_AUTHENTICATION_FAILED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Card not enabled for Ecomm transactions, either the card is newly issued or has not been used for any online transaction during last 12 months`',
    'description': 'AUTHENTICATION_NOT_ATTEMPTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction ID you\'ve generated isn\'t valid`',
    'description': 'INVALID_TRANSACTION_ID',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid CardNumber/Token/AltId or ibibo_code',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'This Card type is not allowed !!',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Cryptogram should not be null or blank',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid Merchant Id',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'pgTransactionId must not be null',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'This Card type is not allowed !!',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Bad Expiry Date passed!',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction is in _3ds_start status, cannot authorize',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Merchant 27186005 is DISABLED, please contact PG admin',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Couldn\'t verify the card, card number seems to be invalid',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Merchant 33656046 is DISABLED, please contact PG admin',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Merchant 43211737 is DISABLED, please contact PG admin',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Not a token card txn but cryptogram is sent in request',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Bad Expiry Year passed!',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Merchant 81543186 is DISABLED, please contact PG admin',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid Pan',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'ALT ID PAN should not be blank or empty',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'Bad Expiry year passed!',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'Card Information not found',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'MRN passed in request is duplicate',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'Bad cvd2 passed!',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'Merchant is not active',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'This Card type is not allowed !!',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction failed due to invalid params shared by the merchant`',
    'description': 'TXN_DETAIL_INVALID * REDIRECTING_TO_MERCHANT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`You are not authorized to do this transaction.`',
    'description': 'SERVICE_AUTHORIZATION_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`You have exceeded your third party funds transfer limit for the day.You cannot transfer any more funds.`',
    'description': 'PER TRANSACTION LIMIT EXCEEDED AS SET BY REMITTING MEMBER',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction Failed at bank end.`',
    'description': 'NETBANKING_AUTHENTICATION * ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'OTP Generated Successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': '',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': '',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'OTP Generated Successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:51:NON SUFFICIENT FUNDS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:ACCU400:User was Inactive',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:93:Transaction cannot be completed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:05:Do not honour',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:57:DECLINED (cardholder not allowed)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'N:59:DECLINED (fraud)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_CHALLENGE_NEGATIVE`',
    'description': 'TRANSACTION_INVALID',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_CHALLENGE_NEGATIVE`',
    'description': 'Card authentication failed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': '102',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': '0',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Restricted card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'K | UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'H | UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Invalid transaction',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Exceeds withdrawal count limit / Withdrawal count limit exceeded',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'GW00555 | UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'N:-BEPG-0000017:Issuer authentication failure',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Blc|0 | Blc|SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Invalid card number',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': '?:waiting authentication',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'P9 | Enter lesser amount',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Issuer unavailable or switch inoperative',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'GW00462 | Invalid Tranportal Password.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Insufficient funds/over credit limit / Not sufficient funds',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'CA | Acquirer compliance',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Transaction not permitted to issuer/cardholder',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'J | UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': '|',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Do not honor',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'No Card Record',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': '102',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': '?:waiting authentication',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Restricted card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': '',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'TXN_PND | UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': '| INVALID_REQUEST',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Suspected fraud',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'RNF | Request Not Found',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'T8 | Invalid account',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'N/A | UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'GENERAL ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'TF | UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Unable to get payer authentication',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Referenced transaction not found',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'UNKNOWN_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Transaction not permitted to issuer/cardholder',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:ACCU400:User was Inactive',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:-BEPG-0000017:Issuer authentication failure',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'CA | Acquirer compliance',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Restricted card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:05:Do not honour',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'P9 | Enter lesser amount',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:ACCU600:Invalid data was posted to Issuer',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Insufficient funds/over credit limit / Not sufficient funds',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:-BEPG-0000006:Rupay check bin error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:93:Transaction cannot be completed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:ACCU800:General exception',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:59:DECLINED (fraud)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:57:DECLINED (cardholder not allowed)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Invalid transaction',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:51:NON SUFFICIENT FUNDS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:91:Issuer not available',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'N:61:DECLINED (Exceeds withdrawal amount limit)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Do not honor',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction failed because the customer does not have the necessary funds or he has given a wrong expiry date.`',
    'description': 'INSUFFICIENT_FUNDS * INCORRECT_EXPIRY',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EMI not applicable for this transactions.`',
    'description': 'EMI_NOT_APPLICABLE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_METHOD_ERROR`',
    'description': '3DS_METHOD_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_METHOD_ERROR`',
    'description': 'NOT_ENROLLED_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_METHOD_NEGATIVE`',
    'description': 'NOT_ENROLLED_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'Cardholder not enrolled in service',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'NOT_ENROLLED_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCERROR`',
    'description': 'AUCERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'transactionid',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'DO_NOT_PROCEED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Cardholder not enrolled in service',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'device.browserDetails.language',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'NOT_ENROLLED_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction declined due to technical failure`',
    'description': 'OBJECT_CREATION_FAILED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'REJECT | Declined - One or more fields in the request contains invalid da',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Invalid data received from bank.`',
    'description': 'Decline - card verification number (CVN) did not match',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`You don\'t have sufficient credit limit to complete this transaction.`',
    'description': 'LOAN_AMOUNT_GREATER * THAN_ELIGIBLITY',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCINVALID`',
    'description': '',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCINVALID`',
    'description': 'Authentication Request Successful',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCINVALID`',
    'description': 'OTP Generated Successfully',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Authentication Request Successful',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid credentials.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Customer Authentication failed due to incorrect OTP.`',
    'description': 'OTP_MAX_LIMIT_EXCEEDED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Authentication Request Successful',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Blc|SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Blc|SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'Blc|SUCCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction failed. Mobile number not registered for the given card.`',
    'description': 'INVALID_PHONE_NO',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction failed due to incorrect user action.`',
    'description': 'OTP_MAX_RESEND_ATTEMPT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'No Error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Technical failure',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Unable to process the request.`',
    'description': 'UNABLE_TO_PROCESS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction declined due to the registered mobile number being international. It should be a domestic number to process the transaction.`',
    'description': 'NOT_DOMESTIC_NUMBER',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`ACS_REDIRECT`',
    'description': 'Authentication Request Successful',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`UserCancelled as the Transaction was left orphan during sure_pay`',
    'description': 'SURE_PAY_USER_CANCELLED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`SurePay usercancelled`',
    'description': 'SURE_PAY_PROCESSED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Non-seamless not allowed in S2S Flow`',
    'description': 'NONSEAMLESS_NOT * ALLOWED_S2SFLOW',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Invalid response from npci',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'INTERNAL_SERVER_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHERROR`',
    'description': 'Invalid Otp',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHERROR`',
    'description': 'Successful approval/completion or that V.I.P. PIN verification is valid',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Could not get the proper response from NPCI',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Internal Server Error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'The transaction is restricted for the card issued country Belgium byZOMATO. Please use another card issued in another country or contact ZOMATO',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'Internal server error in card info service',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'Unable to reach card information service',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'Could not get the proper response from NPCI',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'Something went wrong in checkbin request',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'Internal Server Error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVERROR`',
    'description': 'INTERNAL_SERVER_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'Unable to reach card information service',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'Invalid response from npci',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'Something went wrong in generate otp request',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'INTERNAL_SERVER_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'Could not get the proper response from NPCI',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Internal server Error [S2S FLow]`',
    'description': 'INTERNAL_SERVER * ERROR_S2SFLOW',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`No form post variables found [S2S Flow]`',
    'description': 'NO_FORM_POST * VARS_S2SFLOW',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Category or ibibo code not recieved`',
    'description': 'CATEGORY_IBIBO_NOT_RCVD_S2SFLOW',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Payment Method Enforced and wrong method selected`',
    'description': 'WRONG_PAYMENT_METHOD_SELECTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Merchant does not have access to S2S flow`',
    'description': 'S2S_NOT_ENABLED_MERCHANT',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`S2S flow not enabled on selected payment gateway`',
    'description': 'S2S_NOT_ENABLED_PAYMENTGATEWAY',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'no routing available',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`No Active Authentication Option Eligible`',
    'description': 'NO_ACTIVE_PAYMENT * ELIGIBLE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'E-Commerce is not enabled for this card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': ''Blocked, first used'—The transaction is from a new cardholder, and the card has not been properly unblocked.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Authorisation declined by bank',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid/nonexistent account specified (general)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'restricted card used',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Restricted Card—Pick Up',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Restricted card | Decline - Invalid Card Verification Number (CVN).',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Restricted Card, Retain Card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': '62',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'DECLINED (restricted card)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Restricted card`',
    'description': 'RESTRICTED CARD, DECLINE (REMITTER)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Daily limit for wrong ATM PIN attempts reached`',
    'description': 'DAILY_ATM_MAX_LIMIT_EXCEEDED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'exceeded frequency',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Daily limit exceeded`',
    'description': 'Decline - The card has reached the credit limit',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'PIN data required',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`REDIRECT`',
    'description': 'PIN data required',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Invalid Bank ME Code`',
    'description': 'Sorry! Transaction could not be processed as limit is exhausted',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Invalid card number (no such number)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'N7 | Customer selected negative file reason',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid card number (no such number)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid account number (no such number)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid card number',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Invalid card number | Decline - Invalid account number',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'N7',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'N7 | Authorisation declined by bank',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_CHALLENGE_ERROR`',
    'description': 'UNKNOWN_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_CHALLENGE_NEGATIVE`',
    'description': 'AUTHENTICATION_FAILED | Cardholder did not complete authentication',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_CHALLENGE_NEGATIVE`',
    'description': 'AUTHENTICATION_FAILED | Cardholder did not complete authentication | Cardholder selected Cancel',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_CHALLENGE_NEGATIVE`',
    'description': 'AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction Error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_ERROR`',
    'description': '3DS_VERIFICATION_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'Exceeds ACS maximum challenges',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'Invalid transaction',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'Card authentication failed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'Transaction not permitted to cardholder',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'Suspected fraud',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'System Error response from ACS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'Invalid card number',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_VERIFICATION_NEGATIVE`',
    'description': 'No Card Record',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'SERVER_FAILED::Please contact customer support quoting the support code.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Card authentication failed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'FAILURE::AUTHENTICATION_FAILED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Unknown Error. Transaction Failed. Please try again later.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Invalid card number',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Blc|Not Authenticated /Account Not Verified; Transaction denied',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Transaction not permitted to cardholder',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Blc|203 | Blc|result=FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'FAILURE::AUTHENTICATION_REJECTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'UNKNOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Policy (Mastercard use only)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': '|',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Stolen card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'No Card Record',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Blc|203 | Blc|response.gatewayRecommendation=DO_NOT_PROCEED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'FAILURE::DO_NOT_PROCEED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUCNEGATIVE`',
    'description': 'Message not recognised',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Separate Authentication Failed`',
    'description': 'SEPARATE_AUTHENTICATION_FAILED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Unique Constraint failure from the bank`',
    'description': 'UNIQUE_CONSTRAINT_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Broker failure received from bank`',
    'description': 'BROKER_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Merchant Type Not Supported`',
    'description': 'INVALID_MERCHANT_TYPE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Transaction Already Reversed`',
    'description': 'Decline - The transaction has already been settled or reversed.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_METHOD_NEGATIVE`',
    'description': 'CTO | Network Connect Time Out',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'CTO | Network Connect Time Out',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`EVNEGATIVE`',
    'description': 'CTO | Network Connect Time Out',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Host down`',
    'description': 'HOST_DOWN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_METHOD_NEGATIVE`',
    'description': '3DS212 |',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'CA | Acquirer compliance',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'CA | Compliance error code for acquirer',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction not permitted to acquirer/terminal | We encountered a problem with Rupay processor: DECLINED (terminal not allowed)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction not permitted to issuer/cardholder',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'CA | Acquirer compliance | We encountered a problem with Rupay processor: Acquirer compliance',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'DECLINED (cardholder not allowed)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction not allowed at terminal',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction not permitted to cardholder',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'M6 | Compliance error code for LMM',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Transaction not permitted to acquirer/terminal',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'SYSTEM UNAVALIABLE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Blc|399 | Blc|',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'M6 | Compliance error code for LMM | We encountered a problem with Rupay processor: Compliance error code for LMM',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'SYSTEM UNAVALIABLE | We encountered a problem with Rupay processor: SYSTEM UNAVALIABLE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Mecode Not Permitted`',
    'description': 'MECODE_NOT_PERMITTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`3DS_METHOD_ERROR`',
    'description': 'Blc| | Blc|',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'ITO | Late Authorization Request',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Invalid PayU ID`',
    'description': 'INVALID_PAYU_ID',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Invalid Merchant Key`',
    'description': 'INVALID_MERCHANT_KEY',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Partial Approval`',
    'description': 'Partial amount was approved',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`VIP Approval`',
    'description': 'VIP_APPROVAL',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`No action taken`',
    'description': 'NO_ACTION_TAKEN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Mismatch in retrieval reference number`',
    'description': 'MISMATCH_RETRIEVAL_REFERENCE_NUMBER',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Card blocked`',
    'description': 'CARD_BLOCKED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`AUTHNEGATIVE`',
    'description': 'Issuer or switch is inoperative',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Card Issuer Unavailable`',
    'description': 'Decline - Issuing bank unavailable',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Route to merchant unavailable`',
    'description': 'ROUTE_UNAVAILABLE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Reconcile Error`',
    'description': 'RECONCILE_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Surcharge amount not permitted`',
    'description': 'SURCHARGE_AMOUNT_NOT_PERMITTED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Service not available`',
    'description': 'SERVICE_NOT_AVAILABLE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Error while connecting with blaze net encryption utility`',
    'description': 'BLAZE_ENCRYPTION_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`MCP Lookup api failed after sending S2S response`',
    'description': 'BLAZE_MCP_LOOKUP_ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Failure received in send OTP API call`',
    'description': 'SEND_OTP_API_FAILURE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Card blocked by the issuer. Please contact the bank to get it enabled for online transactions.`',
    'description': 'SBI_DI_BLOCKED_CARD',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Incorrect request received for one click transaction`',
    'description': 'INVALID_ONE_CLICK * REQUEST_RECEIVED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Failing as One Click only option was used and transaction failed in authentication`',
    'description': 'ONE_CLICK_AUTHENTICATION * FAILED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Failing as no gateway found for One Click transaction`',
    'description': 'ONE_CLICK_PG * SELECTION_FAILED',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Card authentication failed at the bank due to invalid CVV (or CVC or Card Security Code)`',
    'description': 'Security violation',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Invalid Payment ID`',
    'description': 'Decline - The request ID is invalid.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Invalid Action`',
    'description': 'INVALID_ACTION',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'NON SUFFICIENT FUNDS',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid transaction',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'ECI 7',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Transaction not permitted to cardholder',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Authentication Failed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'ECI 1 and ECI6',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Issuer authentication failure',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Restricted card',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid card number (no such number)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'The order already exists in the database.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Unable to get payer authentication',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Rupay transaction error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  },
  \{
  'bank_code': '`-`',
  'description': 'Lost card',
  'recommended_fix': 'Verify final payment status, show a customer

  Thought for 6s

  'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  \}, {
    'bank_code': '`-`',
    'description': 'Rupay communication error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Bad Track Data',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid amount',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Pick-up',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'SYSTEM ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Transaction cannot be completed',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (cardholder not allowed)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (lost card)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Exceeds withdrawal frequency limit',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Unable to authorize',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (fraud)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (restricted card)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'No checking account',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Issuer not available',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Compliance error code for LMM',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Do not honour',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Rupay check bin error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (Exceeds withdrawal amount limit)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Rupay authentication error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (stolen)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (terminal not allowed)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid data was posted to Issuer',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid merchant',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'General exception',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid account',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Format error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Issuer Compliance',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Invalid BIN',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Incorrect personal identification number',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'No card record',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'GENERAL ERROR',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Suspected fraud',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'User was Inactive',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Communication Error',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Unable to verify card enrollment',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'NO ROUTING AVAILABLE',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'DECLINED (exceeds frequency)',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`-`',
    'description': 'Acquirer compliance',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }, {
    'bank_code': '`Verification failure`',
    'description': 'Indicates that a verification call confirms the transaction has failed or been declined.',
    'recommended_fix': 'Verify final payment status, show a customer-safe retry or alternate-payment message, and use a new txnid for any new payment attempt.'
  }
  ]\}
  placeholder="Search errors..."
  />
</Accordion>
