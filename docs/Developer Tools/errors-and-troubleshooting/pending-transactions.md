---
title: Pending Transactions
excerpt: Debug pending, dropped, timeout, and uncertain PayU payment states.
deprecated: false
hidden: false
metadata:
  robots: index
---
Pending transactions occur when PayU has not received a final success or failure from the bank, PSP, wallet, or UPI app.

## Error Sample

<Accordion title="Sample Error Response" icon="fa-code">

```json
{
  "mihpayid": "403993715525036528",
  "txnid": "txn_10003",
  "amount": "100.00",
  "status": "pending",
  "unmappedstatus": "in progress",
  "error": "E227",
  "error_Message": "Transaction is Pending",
  "PG_TYPE": "UPI-PG",
  "field7": "TXNPENDING",
  "field8": "Awaiting response from bank",
  "field9": "TRANSACTION_PENDING",
  "hash": "response_hash"
}
```

</Accordion>

## Root cause

Below are the root causes of the above error

<Accordion title="Common Causes" icon="fa-list">
  * Bank callback is delayed.
  * UPI app did not send the final response yet.
  * Customer closed the browser after bank debit.
  * Corporate net banking checker has not approved the transaction.
  * Bank or wallet verification timed out.
  * PayU received a late response from the bank or PSP.
</Accordion>

## Troubleshooting Steps

Now that we know the root causes of the error, let's see how to troubleshoot the error.

<Accordion title="Troubleshooting Steps" icon="fa-steps">

1. Keep the order in `payment_pending`; do not mark it paid or failed immediately.
2. Store `mihpayid`, `txnid`, `amount`, `status`, `unmappedstatus`, `error`, `field7`, `field8`, and `bank_ref_num`.
3. Verify response hash if a response payload was received.
4. Listen for webhook updates.
5. Query Transaction Detail APIs using the original transaction identifiers.
6. Reconcile final status before allowing a second payment for the same order.
7. If the customer retries, create a new `txnid` and link both attempts to the same merchant order.

</Accordion>

<Callout icon="❗️">
  **Watch Out!**

  Treating pending as failed can create false failures. Treating pending as success can create revenue leakage. Keep a separate pending state.
</Callout>

## Error Codes

Below are the similar errors and their recommended fixes.

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
    headers={['Error code / type', 'What it means', 'Recommended fix']}
    rows={[
    ['`status=pending`', 'PayU has not confirmed final payment status.', 'Keep the order pending and wait for webhook/status reconciliation.'],
    ['`unmappedstatus=in progress`', 'The transaction is still being processed.', 'Do not fulfill or fail the order until final status is available.'],
    ['`error=E227`', 'Transaction is pending.', 'Poll Transaction Detail APIs and listen for webhooks.'],
    ['`field7=TXNPENDING` / `VERPENDING`', 'Bank/wallet or verification stage is pending.', 'Recheck on a controlled interval and avoid immediate retry.'],
    ['`field7=TXNERROR` / `VERERROR`', 'Callback or verification had a technical error.', 'Treat as uncertain and reconcile before changing order status.'],
    ['`Browser redirect failed`', 'Customer browser did not return final response.', 'Use webhook and Transaction Detail APIs as the source of truth.'],
    ['`Corporate net banking approval pending`', 'Checker approval is pending.', 'Keep pending until bank confirmation or timeout.'],
  ]}
    placeholder="Search errors..."
  />
</Accordion>

<br />

## Recommended Order States

<Accordion title="My Accordion Title" icon="fa-info-circle">
  <SearchableTable
  headers={['Merchant state', 'PayU status / error type', 'Recommended fix']}
  rows={[
    ['`payment_initiated`', 'Request created', 'Await redirect, webhook, or status API result before fulfillment.'],
    ['`payment_pending`', '`status=pending` or `E227`', 'Do not fulfill. Poll Transaction Detail APIs and wait for webhook/status reconciliation.'],
    ['`payment_success`', '`status=success` and hash valid', 'Fulfill only after matching `txnid`, `amount`, and response hash.'],
    ['`payment_failed`', '`status=failure` and final status verified', 'Show retry options and create a new `txnid` for a new attempt.'],
    ['`payment_dropped`', '`E231`, timeout, abandoned flow', 'Verify final status before retry; if not successful, create a new attempt.'],
    ['`payment_review`', 'Conflicting redirect/webhook/status', 'Hold fulfillment and reconcile manually using `mihpayid`, `txnid`, and latest verified status.'],
  ]}
  placeholder="Search..."
/>
</Accordion>

## Common Pending Indicators

<Accordion title="My Accordion Title" icon="fa-info-circle">
  <SearchableTable
  headers={['Error code / type', 'Error message or response indicator', 'Description', 'Possible cause', 'Recommended fix']}
  rows={[
    ['`E227`', '`Transaction is Pending`', 'Final transaction state is not yet available.', 'Bank/PSP callback is delayed or verification has not completed.', 'Keep order pending, listen for webhook, and poll Transaction Detail APIs.'],
    ['`TXNPENDING`', '`field7=TXNPENDING`', 'Bank/wallet transaction is awaiting final result.', 'Bank or wallet has not sent final callback.', 'Do not retry immediately; reconcile before allowing another attempt.'],
    ['`VERPENDING`', '`field7=VERPENDING`', 'Verification confirms the transaction is still pending.', 'Corporate banking checker approval or delayed verification.', 'Keep pending and recheck status on a controlled interval.'],
    ['`TXNERROR`', '`field7=TXNERROR`', 'PayU did not receive a valid bank/wallet callback.', 'Null response, callback failure, or technical issue.', 'Treat as uncertain; use webhook/status API before marking failed.'],
    ['`VERERROR`', '`field7=VERERROR`', 'Verification attempt had a technical error.', 'Bank verification API timeout or service issue.', 'Retry status check later and hold fulfillment.'],
    ['`E231`', '`Transaction was marked as dropped`', 'Flow was abandoned or dropped.', 'Browser close, redirect failure, or no bank response.', 'Verify final status before retry; create a new `txnid` only after reconciliation.'],
  ]}
  placeholder="Search errors..."
/>
</Accordion>
