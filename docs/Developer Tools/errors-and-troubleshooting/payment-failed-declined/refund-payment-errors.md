---
title: Refund payment errors
excerpt: Go through these refund initiation and refund status errors.
deprecated: false
hidden: true
metadata:
  robots: index
---
These are refund initiation and refund status errors, along with their descriptions, and recommended fix.

Refer to the [Payment Failed or Declined](doc:payment-failed-declined) page for debugging guidance and retry handling.

<Accordion title="My Accordion Title" icon="fa-info-circle">

<SearchableTable
  headers={['Bank Code', 'Description', 'Recommended Fix']}
  columnWidths={['18%', '32%', '50%']}
  rows={[
    ['`Refund Successful`', '100', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund Successful`', '101', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Confirmation required`', '104', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Invalid amount`', '105', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Token already exists.`', '106', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Upgraded to refund`', '107', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '108', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Invalid transaction status`', '111', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '112', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Invalid status to be updated`', '115', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Transaction Not Found`', '116', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Amount Does not Match`', '117', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`No such Request Found`', '119', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Transaction lock could not be obtained.`', '120', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '122', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '126', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '127', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Partial refunds not allowed`', '128', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refunds not allowed after`', '130', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Overdraft has occurred. Kindly recheck the status tomorrow.`', '225', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Capture has been initiated today. Please check for refund status tomorrow.`', '226', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Transactions with same amount and same token not allowed`', '227', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Purged Transaction. Refund request requires manual follow-up`', '230', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund could not be initiated due to some internal error`', '231', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund could not be initiated. Either refunds are not supported or need manual intervention`', '232', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund/Cancel Blocked From Merchant Panel. Contact KM.`', '233', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund/Cancel Blocked From Merchant Panel And API. Contact KM.`', '234', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund/Cancel Blocked. Contact KM.`', '235', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`API based alternate instant refunds not activated.`', '239', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Store card failed`', '240', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '241', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Bank Code Not Supported. Raise it to PayU support team`', '242', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Virtual account setup to process instant refund is incomplete`', '243', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Beneficiary Code for Virtual Account Not Set`', '244', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`BBPS transaction is not successful`', '245', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Value is Invalid for the Merchant SKU.`', '246', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '248', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund Failed On Uploading Successful Chargeback`', '250', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund Blocked for this PGMID by Bank`', '251', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refunds are not allowed from panel for this MID`', '252', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Instant refunds invalid mode`', '253', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Remarks cannot contain special characters`', '254', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Token Length Exceeded for Refund`', '255', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Refund not supported on split transactions. Please initiate refund on the order transaction`', '256', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '258', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`-`', '259', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Invalid requested amount`', '263', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Lock acquired on TransactionMetaData`', '267', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Transaction not eligible for Instant Refund`', '270', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Blocking refund initiation for Type A Merchant`', '299', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Capture already successful for this transaction`', '301', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Please try after some time`', '302', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Amount greater than maximum capturable amount`', '303', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Amount less than allowed`', '304', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Amount more than allowed`', '305', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Invalid amount tolerance configuration`', '306', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Transaction upgraded to capture/refund.`', '424', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`Successfully Updated`', '501', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`SUCCESS`', 'Refund status error', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`TECHNICAL_ERROR_AT_ACQUIRER_BANK`', 'Refund status error', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`TECHNICAL_ERROR_AT_CUSTOMER_BANK`', 'Refund status error', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`TECHNICAL_ERROR`', 'Refund status error', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
    ['`FAILED`', 'Refund status error', 'Check the original transaction, refund amount, refund status, and eligibility; retry only when the source status permits it.'],
  ]}
  placeholder="Search errors..."
  maxHeight="500px"
/>
</Accordion>

<br />

<br />
