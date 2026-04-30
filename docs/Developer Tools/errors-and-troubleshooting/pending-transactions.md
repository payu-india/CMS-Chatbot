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

<Callout icon="❗️" theme="error">
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

## Recommended Order States

<Accordion title="Errors and Fixes" icon="fa-wrench">
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

<Accordion title="Errors and Fixes" icon="fa-wrench">
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

## Pending, Timeout, and Uncertain-status Errors

<Accordion title="Errors and Fixes" icon="fa-wrench">
  <SearchableTable
  headers={['Source doc', 'Error code / type', 'Error message / response indicator', 'Description', 'Recommended fix']}
  rows={[
    ['Alt ID Error Page', '`EA05`', '`Failure`', 'Card network seems to be down. Please retry after some time', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Alt ID Error Page', '`EA082`', '`Failure`', 'Mastercard DPA creation in progress. Please retry after 15 mins', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Alt ID Error Page', '`EA11`', '`Failure`', 'Alt ID timeout at StoreCard. Please raise this to PayU support team', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`25`', '`E9211`', 'UNABLE_TO_LOCATE_ RECORD_ON_FILE', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Collect Payment Error Codes', '`54`', '`E311`', 'EXPIRED_CARD', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Collect Payment Error Codes', '`68`', '`E9220`', 'RESPONSE_RECEIVED_ TOO_LATE', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`AUTHERROR`', 'Authorization error', 'Indicates a technical failure during the authorization process, such as network issues, timeout, or gateway errors.', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E000`', '`ACS_REDIRECT`', 'Marking transaction as dropped - CSW', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Collect Payment Error Codes', '`E000`', '`AUTHNEGATIVE`', 'T1 | Payment Gateway timed out', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Collect Payment Error Codes', '`E000`', '`AUTHNEGATIVE`', '8 | Transaction Timed Out', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E1206`', '`3DS_CHALLENGE_NEGATIVE`', '914 | Transaction timed out at the ACS', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Collect Payment Error Codes', '`E1206`', '`3DS_VERIFICATION_NEGATIVE`', 'Transaction timed out at the ACS', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E1602`', 'Transaction failed. Page expired due to no user input.', '`ATM_PIN_PAGE_EXPIRED`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Collect Payment Error Codes', '`E1610`', 'Transaction failed. Page expired due to no user input.', '`PAGE_EXPIRED`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E1633`', '`3DS_CHALLENGE_NEGATIVE`', 'AUTHENTICATION_FAILED | Cardholder did not complete authentication | Transaction timed out at ACS—other timeouts', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E1703`', '`AUTHNEGATIVE`', '54 | Expired card', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E1903`', '`AUTHNEGATIVE`', 'DECLINED | EXPIRED_CARD | Decline - Expired card.', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E202`', '`3DS_CHALLENGE_NEGATIVE`', '914 | Transaction timed out at the ACS', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E207`', '`AUCNEGATIVE`', '305 | Transaction ID has already been received and processed.', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E208`', '`AUTHNEGATIVE`', 'Error - The request was received but there was a server timeout.', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E221`', 'Bank reference number is not received in transaction response', '`NO_BANK_REFERENCE_NUMBER`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E225`', 'Transaction in Progress', 'Destination cannot be found for routing', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E227`', 'Transaction is Pending', '`TRANSACTION_PENDING`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E231`', 'Transaction was marked as dropped', '`TRANSACTION_DROPPED`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E303`', '`AUCERROR`', '12002 | Rupay Redirect Response Timeout', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E311`', '`AUTHNEGATIVE`', '54 | Expired card', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E408`', 'Transaction failed. Page expired due to no user input.', '`TRANSACTION_BOUNCED`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`E4103`', 'Payment validity expired', 'Payment validity expired', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Collect Payment Error Codes', '`INTERROR`', 'No response from bank', 'Occurs when PayU initiates a payment request to the bank but does not receive any response.', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Partner Integration Errors', 'Token expired', 'Auth', 'Refresh / contact KAM', 'Refresh / contact KAM'],

    ['Refund Initiation Error Codes', '`102`', 'Refund Queued', '`102`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
    ['Refund Initiation Error Codes', '`103`', 'Request rejected on reconfirmation', '`103`', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Refund Status Error Codes', '`R0003`', '`INVALID_OR_EXPIRED_VPA`', 'Refund status error', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Smart Send Error Codes', '`1111`', '`LINK_EXPIRED`', 'Smart Send Error Codes', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Transaction Stages Field7/Field8', '`TXNPENDING`', 'Maker has initiated but checker approval pending', 'Corporate transaction awaiting approval', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],

    ['Issuer Decline Error Codes', '`E311 / response 54`', 'Expired card', 'Transaction declined due to invalid expiry details or expired card', 'Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling.'],
  ]}
  placeholder="Search errors..."
/>
</Accordion>
