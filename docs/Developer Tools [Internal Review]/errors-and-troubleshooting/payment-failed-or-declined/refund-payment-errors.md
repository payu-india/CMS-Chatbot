---
title: Refund Payment Errors
excerpt: Go through these refund initiation and refund status errors.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are refund initiation and refund status errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="Errors and Fixes" icon="far fa-wrench-simple">
  <AdvancedTable
    data={[
      {
        'bank_code': '`Refund Successful`',
        'description': '100',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund Successful`',
        'description': '101',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Confirmation required`',
        'description': '104',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Invalid amount`',
        'description': '105',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Token already exists.`',
        'description': '106',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Upgraded to refund`',
        'description': '107',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '108',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Invalid transaction status`',
        'description': '111',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '112',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Invalid status to be updated`',
        'description': '115',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Transaction Not Found`',
        'description': '116',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Amount Does not Match`',
        'description': '117',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`No such Request Found`',
        'description': '119',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Transaction lock could not be obtained.`',
        'description': '120',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '122',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '126',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '127',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Partial refunds not allowed`',
        'description': '128',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refunds not allowed after`',
        'description': '130',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Overdraft has occurred. Kindly recheck the status tomorrow.`',
        'description': '225',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Capture has been initiated today. Please check for refund status tomorrow.`',
        'description': '226',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Transactions with same amount and same token not allowed`',
        'description': '227',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Purged Transaction. Refund request requires manual follow-up`',
        'description': '230',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund could not be initiated due to some internal error`',
        'description': '231',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund could not be initiated. Either refunds are not supported or need manual intervention`',
        'description': '232',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund/Cancel Blocked From Merchant Panel. Contact KM.`',
        'description': '233',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund/Cancel Blocked From Merchant Panel And API. Contact KM.`',
        'description': '234',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund/Cancel Blocked. Contact KM.`',
        'description': '235',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`API based alternate instant refunds not activated.`',
        'description': '239',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Store card failed`',
        'description': '240',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '241',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Bank Code Not Supported. Raise it to PayU support team`',
        'description': '242',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Virtual account setup to process instant refund is incomplete`',
        'description': '243',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Beneficiary Code for Virtual Account Not Set`',
        'description': '244',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`BBPS transaction is not successful`',
        'description': '245',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Value is Invalid for the Merchant SKU.`',
        'description': '246',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '248',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund Failed On Uploading Successful Chargeback`',
        'description': '250',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund Blocked for this PGMID by Bank`',
        'description': '251',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refunds are not allowed from panel for this MID`',
        'description': '252',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Instant refunds invalid mode`',
        'description': '253',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Remarks cannot contain special characters`',
        'description': '254',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Token Length Exceeded for Refund`',
        'description': '255',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Refund not supported on split transactions. Please initiate refund on the order transaction`',
        'description': '256',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '258',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`-`',
        'description': '259',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Invalid requested amount`',
        'description': '263',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Lock acquired on TransactionMetaData`',
        'description': '267',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Transaction not eligible for Instant Refund`',
        'description': '270',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Blocking refund initiation for Type A Merchant`',
        'description': '299',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Capture already successful for this transaction`',
        'description': '301',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Please try after some time`',
        'description': '302',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Amount greater than maximum capturable amount`',
        'description': '303',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Amount less than allowed`',
        'description': '304',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Amount more than allowed`',
        'description': '305',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Invalid amount tolerance configuration`',
        'description': '306',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Transaction upgraded to capture/refund.`',
        'description': '424',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`Successfully Updated`',
        'description': '501',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`SUCCESS`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`TECHNICAL_ERROR_AT_ACQUIRER_BANK`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`TECHNICAL_ERROR_AT_CUSTOMER_BANK`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`CREDIT_FAILED_IN_CUSTOMER_ACCOUNT`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`REFUND_NOT_PERMITTED_TO_ACCOUNT`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`TECHNICAL_ERROR`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`TECHNICAL_ERROR_AT_ISSUER_OR_ACQUIRER_END`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`REFUND_IN_DEEMED_STATE`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`ACCOUNT_DETAILS_NOT_FOUND_AT_CUSTOMER_BANK`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`COMPLIANCE_DECLINE_AT_CUSTOMER_BANK`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`CUSTOMER_ACCOUNT_BLOCKED`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`REFUND_NOT_ALLOWED_ON_VPA`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`ORIGINAL_REFUND_DETAILS_NOT_FOUND`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`CUSTOMER_ACCOUNT_INACTIVE`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`CUSTOMER_BANK_MAXIMUM_BALANCE_LIMIT_BREACHED`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`RISK_DECLINE`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`CUSTOMER_VPA_BLOCKED`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`REFUND_NOT_ALLOWED_ON_OVERDRAFT_ACCOUNT`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`MERCHANT_BLOCKED_BY_CUSTOMER`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`CUSTOMER_BANK_NOT_HONOURING_REFUND`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`IN_PROGRESS`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`INSUFFICIENT_BALANCE`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      },
      {
        'bank_code': '`FAILED`',
        'description': 'Refund status error',
        'recommended_fix': 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'
      }
    ]}
  />
</Accordion>
