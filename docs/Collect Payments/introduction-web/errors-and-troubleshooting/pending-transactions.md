---
title: Pending Transactions
excerpt: Debug pending, dropped, timeout, and uncertain PayU payment states.
deprecated: false
hidden: false
metadata:
  title: Pending Transactions
  description: Debug pending, dropped, timeout, and uncertain PayU payment states.
  robots: index
next:
  description: ''
---

Pending transactions occur when PayU has not received a final success or failure from the bank, PSP, wallet, or UPI app.
## Category alignment

Primary category: Pending, timeout, and uncertain-status errors within Payment failures.

## When it occurs

| Error code / type | What it means | Recommended fix |
| --- | --- | --- |
| `status=pending` | PayU has not confirmed final payment status. | Keep the order pending and wait for webhook/status reconciliation. |
| `unmappedstatus=in progress` | The transaction is still being processed. | Do not fulfill or fail the order until final status is available. |
| `error=E227` | Transaction is pending. | Poll Transaction Detail APIs and listen for webhooks. |
| `field7=TXNPENDING` / `VERPENDING` | Bank/wallet or verification stage is pending. | Recheck on a controlled interval and avoid immediate retry. |
| `field7=TXNERROR` / `VERERROR` | Callback or verification had a technical error. | Treat as uncertain and reconcile before changing order status. |
| Browser redirect failed | Customer browser did not return final response. | Use webhook and Transaction Detail APIs as the source of truth. |
| Corporate net banking approval pending | Checker approval is pending. | Keep pending until bank confirmation or timeout. |

## Sample response

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

## Root cause

The final state is not yet known.

Common causes:

* Bank callback is delayed.
* UPI app did not send the final response yet.
* Customer closed the browser after bank debit.
* Corporate net banking checker has not approved the transaction.
* Bank or wallet verification timed out.
* PayU received a late response from the bank or PSP.

## Step-by-step debugging guide

1. Keep the order in `payment_pending`; do not mark it paid or failed immediately.
2. Store `mihpayid`, `txnid`, `amount`, `status`, `unmappedstatus`, `error`, `field7`, `field8`, and `bank_ref_num`.
3. Verify response hash if a response payload was received.
4. Listen for webhook updates.
5. Query Transaction Detail APIs using the original transaction identifiers.
6. Reconcile final status before allowing a second payment for the same order.
7. If the customer retries, create a new `txnid` and link both attempts to the same merchant order.

> **Common Mistake**
>
> Treating pending as failed can create false failures. Treating pending as success can create revenue leakage. Keep a separate pending state.

## Recommended order states

| Merchant state | PayU status / error type | Recommended fix |
| --- | --- | --- |
| `payment_initiated` | Request created | Await redirect, webhook, or status API result before fulfillment. |
| `payment_pending` | `status=pending` or `E227` | Do not fulfill. Poll Transaction Detail APIs and wait for webhook/status reconciliation. |
| `payment_success` | `status=success` and hash valid | Fulfill only after matching `txnid`, `amount`, and response hash. |
| `payment_failed` | `status=failure` and final status verified | Show retry options and create a new `txnid` for a new attempt. |
| `payment_dropped` | `E231`, timeout, abandoned flow | Verify final status before retry; if not successful, create a new attempt. |
| `payment_review` | Conflicting redirect/webhook/status | Hold fulfillment and reconcile manually using `mihpayid`, `txnid`, and latest verified status. |

## Common pending indicators

| Error code / type | Error message or response indicator | Description | Possible cause | Recommended fix |
| --- | --- | --- | --- | --- |
| `E227` | `Transaction is Pending` | Final transaction state is not yet available. | Bank/PSP callback is delayed or verification has not completed. | Keep order pending, listen for webhook, and poll Transaction Detail APIs. |
| `TXNPENDING` | `field7=TXNPENDING` | Bank/wallet transaction is awaiting final result. | Bank or wallet has not sent final callback. | Do not retry immediately; reconcile before allowing another attempt. |
| `VERPENDING` | `field7=VERPENDING` | Verification confirms the transaction is still pending. | Corporate banking checker approval or delayed verification. | Keep pending and recheck status on a controlled interval. |
| `TXNERROR` | `field7=TXNERROR` | PayU did not receive a valid bank/wallet callback. | Null response, callback failure, or technical issue. | Treat as uncertain; use webhook/status API before marking failed. |
| `VERERROR` | `field7=VERERROR` | Verification attempt had a technical error. | Bank verification API timeout or service issue. | Retry status check later and hold fulfillment. |
| `E231` | `Transaction was marked as dropped` | Flow was abandoned or dropped. | Browser close, redirect failure, or no bank response. | Verify final status before retry; create a new `txnid` only after reconciliation. |

<!-- PAYU_REPO_ERRORS_PENDING_TRANSACTIONS_BEGIN -->

## Repo-backed pending, timeout, and uncertain-status errors

These rows are categorized from existing PayU repository error-code and troubleshooting documentation. Existing guidance on this page remains unchanged.

| Source doc | Error code / type | Error message / response indicator | Description | Recommended fix |
| --- | --- | --- | --- | --- |
| Alt ID Error Page | EA05 | Failure | Card network seems to be down. Please retry after some time | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Alt ID Error Page | EA082 | Failure | Mastercard DPA creation in progress. Please retry after 15 mins | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Alt ID Error Page | EA11 | Failure | Alt ID timeout at StoreCard. Please raise this to PayU support team | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | 25 | E9211 | UNABLE_TO_LOCATE_ RECORD_ON_FILE | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | 54 | E311 | EXPIRED_CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | 68 | E9220 | RESPONSE_RECEIVED_ TOO_LATE | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | AUTHERROR | Authorization error | Indicates a technical failure during the authorization process, such as network issues, timeout, or gateway errors. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E000 | ACS_REDIRECT | Marking transaction as dropped - CSW | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E000 | AUTHNEGATIVE | T1 \| Payment Gateway timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E000 | AUTHNEGATIVE | 8 \| Transaction Timed Out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | 3DS_CHALLENGE_NEGATIVE | 914 \| Transaction timed out at the ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | 3DS_VERIFICATION_NEGATIVE | Transaction timed out at the ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | ACS_REDIRECT | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | ACS_REDIRECT | Marking transaction as dropped - CSW | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | AUCNEGATIVE | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | AUCNEGATIVE | T5 \| Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | AUTHNEGATIVE | 51 \| Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1206 | REDIRECT | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1602 | Transaction failed. Page expired due to no user input. | ATM_PIN_PAGE_EXPIRED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1610 | Transaction failed. Page expired due to no user input. | PAGE_EXPIRED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1617 | EVNEGATIVE | 10004 \| Timed out at NPCI | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1633 | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Cardholder did not complete authentication \| Transaction timed out at ACS—other timeouts | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1633 | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Cardholder did not complete authentication \| Transaction Timed out at ACS - First CReq not received by ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1633 | 3DS_VERIFICATION_NEGATIVE | Transaction timed out at the ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1633 | AUCNEGATIVE | 05 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1636 | AUTHNEGATIVE | 8 \| Transaction Timed Out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1636 | Transaction time out | TRANSACTION_TIMEOUT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1650 | AUTHNEGATIVE | 12002 \| Acquirer Timeout | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | - | Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | - | Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | - | Transaction timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | - | EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | - | Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | ACS_REDIRECT | EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | AUCNEGATIVE | EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | AUTHNEGATIVE | 54 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | AUTHNEGATIVE | Blc\|204 \| Exception occured durinf retry with Enquiry API | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | AUTHNEGATIVE | Blc\|204 \| Retrying due to IO Error at server | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | REDIRECT | Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | REDIRECT | Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | REDIRECT | Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | REDIRECT | Suspected Fraud. Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | REDIRECT | Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | REDIRECT | EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1703 | REDIRECT | Transaction timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | GW02016 \| PaymentId Expired | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | DECLINED \| EXPIRED_CARD \| Decline - Expired card. You might also receive this if the expiration date you provided does not match the date the issuing bank has on file. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | O6 \| Suspected Fraud. Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 12009 \| Acquirer Switch Timeout | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | 12009 \| ACQUIRER_TIMEOUT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | O8 \| Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | T1 \| Payment Gateway timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | GW00854 \| Card expired | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | rupay response Timeout | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | Authorise Failure : 54 : EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E1903 | AUTHNEGATIVE | VerifyOTP Failure - 451 : EXPIRED OTP | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E199 | Rreq not received from the Network Scheme | RREQ_NOT_RECEIVED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E202 | 3DS_CHALLENGE_NEGATIVE | 914 \| Transaction timed out at the ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E202 | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Cardholder did not complete authentication \| Transaction timed out at ACS—other timeouts | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E202 | 3DS_CHALLENGE_NEGATIVE | 402 \| CReq message with this ACS Transaction ID has already been received and processed. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E202 | 3DS_CHALLENGE_NEGATIVE | AUTHENTICATION_FAILED \| Cardholder did not complete authentication \| Transaction Timed out at ACS - First CReq not received by ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E202 | 3DS_CHALLENGE_NEGATIVE | 983 \| Declined by DS - DS dropped reason code received from ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E202 | ACS_REDIRECT | Marking transaction as dropped - CSW | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E204 | 3DS_METHOD_NEGATIVE | Blc\|204 \| Blc\|Retrying due to IO Error at server | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 305 \| Transaction ID has already been received and processed. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 30054 \| Transaction timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | O8 \| Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | O6 \| Suspected Fraud. Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E207 | AUCNEGATIVE | 402 \| For example, Read-Timeout expiry reached for the transaction as defined in Section 5.5. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E208 | AUTHNEGATIVE | Error - The request was received but there was a server timeout. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E208 | EVNEGATIVE | ERROR \| Error - The request was received but there was a server timeout. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E208 | Error at the Bank Server end | Error - The request was received but there was a server timeout. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E221 | Bank reference number is not received in transaction response | NO_BANK_REFERENCE * NUMBER | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E225 | Transaction in Progress | Destination cannot be found for routing / Unable to route transa | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E227 | Transaction is Pending | TRANSACTION_PENDING | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | - | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | - | N:54:EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | 3DS_CHALLENGE_NEGATIVE | 914 \| Transaction timed out at the ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | 3DS_CHALLENGE_NEGATIVE | 402 \| CReq message with this ACS Transaction ID has already been received and processed. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | 3DS_VERIFICATION_NEGATIVE | Transaction timed out at the ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | ACS_REDIRECT | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | ACS_REDIRECT | Marking transaction as dropped - CSW | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 14 \| Transaction timed out at the ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 305 \| Transaction ID has already been received and processed. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 54 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 51 \| Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 408 \| pArq Request timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUCNEGATIVE | 30054 \| Transaction timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | 12009 \| Acquirer Switch Timeout | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | DUE \| 3DS timeout | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | 51 \| Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | T5 \| Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | 14 \| 3DS timeout | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | O8 \| Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | AUTHNEGATIVE | O6 \| Suspected Fraud. Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | EVNEGATIVE | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | REDIRECT | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | REDIRECT | N:54:EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | REDIRECT | 54 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E231 | Transaction was marked as dropped | TRANSACTION_DROPPED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E303 | AUCERROR | 12002 \| Rupay Redirect Response Timeout | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E303 | AUCNEGATIVE | O8 \| Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E303 | AUCNEGATIVE | 51 \| Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E303 | AUCNEGATIVE | T5 \| Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E303 | AUCNEGATIVE | O6 \| Suspected Fraud. Do not retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E308 | ALT_ID_PROV_ERROR | \|DpaId on-boarding in progress | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E308 | AUTHNEGATIVE | HOST TIMEOUT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | 3DS_VERIFICATION_NEGATIVE | Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | AUCNEGATIVE | 05 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | AUCNEGATIVE | 54 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | AUTHNEGATIVE | 15054 \| expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | AUTHNEGATIVE | 15054 \| card expired | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | AUTHNEGATIVE | 54 \| Expired card \| Decline - Expired card. You might also receive this if the expiration date you provided does not match the date the issuing bank has on file. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | AUTHNEGATIVE | 54 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | AUTHNEGATIVE | 54 \| EXPIRED CARD | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | REDIRECT | 54 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E311 | Transaction declined due to invalid expiry details or the card is expired | Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E317 | 3DS_CHALLENGE_NEGATIVE | Blc\|204 \| Blc\|No Response from PG. Please Contact support | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E317 | AUCNEGATIVE | Blc\|204 \| Blc\|No Response from PG. Please Contact support | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E335 | 3DS_CHALLENGE_NEGATIVE | 51 \| Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E335 | 3DS_CHALLENGE_NEGATIVE | T5 \| Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 905 \| Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 305 \| Transaction ID has already been received and processed. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | 983 \| Declined by DS - DS dropped reason code received from ACS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | Blc\|202 \| Blc\|No Response from PG. Please Contact support | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E335 | AUCNEGATIVE | Blc\|202 \| Blc\|Retrying due to IO Error at server | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E408 | Transaction failed. Page expired due to no user input. | TRANSACTION_BOUNCED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4103 | Payment validity expired | Payment validity expired | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4167 | Transaction failed as authorisation acknowledgement not received | REQUEST AUTHORISATION ACKNOWLEDGEMENT IS NOT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4172 | CM REQUEST TIMEOUT | CM REQUEST TIMEOUT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4173 | CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED | CM REQUEST ACKNOWLEDGEMENT IS NOT RECEIVED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4175 | PSP REQUEST CREDIT PAY ACKNOWLEDGEMENT IS NOT RECEIVED | PSP REQUEST CREDIT PAY ACKNOWLEDGEMENT IS NOT RECEIVED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4176 | Transaction failed as no response received from merchant/customer | NO RESPONSE FROM PSP | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4184 | RESPONSE IS ALREADY BEEN RECEIVED | RESPONSE IS ALREADY BEEN RECEIVED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4185 | REQUEST IS ALREADY BEEN SENT | REQUEST IS ALREADY BEEN SENT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4187 | RESPONSE IS ALREADY BEEN SENT | RESPONSE IS ALREADY BEEN SENT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4218 | Transaction failed due to collect request expired | COLLECT EXPIRED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4219 | RECEIVED LATE RESPONSE | RECEIVED LATE RESPONSE | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4267 | Response Activation TimeOut | Response Activation TimeOut | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4268 | Response ValQR TimeOut | Response ValQR TimeOut | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4292 | Transaction declined due to timeout at Issuer's end | PSP TIME-OUT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4294 | Transaction declined due to timeout at Issuer/Customer's end | REMITTER/ISSUER UNAVAILABLE (TIMEOUT) | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4381 | RECEIVED LATE RESPONSE | RECEIVED LATE RESPONSE | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4387 | OTP EXPIRED | OTP EXPIRED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4522 | Refund failed due to no response from Customer's bank | No response from Beneficiary Bank | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E4608 | Request has been timed out | Request has been timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E501 | ACS_REDIRECT | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E501 | AUCNEGATIVE | \|Decline - Expired card. You might also receive this if the expiration date you provided does not match the date the issuing bank has on file. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E501 | REDIRECT | Marking transaction as dropped - CS | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E507 | Transaction Expired | TRANSACTION_EXPIRED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E706 | AUCNEGATIVE | 51 \| Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E706 | AUTHNEGATIVE | 51 \| Retry the transaction later | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E712 | AUCNEGATIVE | 408 \| pArq Request timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E803 | - | There is no eligible pg and retry are not allowed or is disabled. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E9211 | Unable to Locate Record on File | Unable to Locate Record on File | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E9220 | Response Received Too Late | Response Received Too Late | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E9248 | AUCNEGATIVE | T5 \| Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E9248 | AUTHNEGATIVE | T5 \| Check for New information before retry | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E9252 | PSP REQUEST META ACKNOWLEDGEMENT NOT RECEIVED | ADDRESS_RESOLUTION_IS_FAILED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | E9254 | ACQUIRER/BENEFICIARY UNAVAILABLE(TIMEOUT) | ACQUIRER_BENEFICIARY_UNAVAILABLE_TIMEOUT | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EA05 | Failure | Card network seems to be down. Please retry after some time | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EA082 | Failure | Mastercard DPA creation in progress. Please retry after 15 mins | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EA085 | ALT_ID_PROV_ERROR | EA085\|Issuer did not respond in time. Retry the request. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EA11 | ALT_ID_PROV_ERROR | EA11 \| Timeout reached from StoreCard | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EA11 | ALT_ID_PROV_ERROR | EA11\|Service unavailable. Typically the server not able to serve the request temporarily. Retry after sometime. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EA11 | ALT_ID_PROV_ERROR | EA11\|The network token service was unavailable or timed out | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EA11 | Failure | Alt ID timeout at StoreCard. Please raise this to PayU support team | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX063 | Invalid Transaction State: Transaction in IN PROGRESS state in cancel.php | INVALID_TRANSACTION_STATE | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX084 | Return URI not received | URI_NOT_RECEIVED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX085 | Verifier payu Id not received | VERIFIER_PAYUID_NOT_RECEIVED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX116 | Expired transaction. | PAYMENTFLOW_EXPIRED_TRANSACTION | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX125 | Transaction Expired, payuid: ? base txn Id: ? uniqueness: ? , ? | PAYMENT_FLOW_EXCEP_TRANSACTION_EXPIRED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX149 | Maximum retry attempts for this \ txnid\ has been exceeded. | RETRY_EXHAUSTED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX210 | This link has expired | INTENT_LINK_EXPIRED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | EX214 | Retry limit exhausted. Please ask your merchant to send you a new link. | INTENT_LINK_USE_EXHAUSTED | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | INTERROR | No response from bank | Occurs when PayU initiates a payment request to the bank or processor but does not receive any response within the expected timeframe. This usually indicates network issues, bank downtime, or timeout in communication. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E317 | Transaction Expired | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E4167 | Transaction failed as authorisation acknowledgement not received | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E4218 | Transaction failed due to collect request expired | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E4272 | Transaction declined due to timeout at Issuer/Acquirer end | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E4279 | Transaction declined due to timeout at customer's bank | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E4292 | Transaction declined due to timeout at Issuer's end | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E4294 | Transaction declined due to timeout at Issuer/Customer's end | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E4295 | Transaction failed as vpa is not valid/expired | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPI | E708 | Transaction failed. Page expired due to no user input. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPICC | E4294 | Transaction declined due to timeout at Issuer/Customer's end | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | UPICC | E708 | Transaction failed. Page expired due to no user input. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Collect Payment Error Codes | VERPENDING | Verification pending approval | Indicates that during verification, the transaction is still awaiting approval in corporate flows where a checker action is pending. | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Issuer Decline Error Codes | E225 / response 92 | Transaction in Progress | Destination cannot be found for routing / Unable to route transa | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Issuer Decline Error Codes | E311 / response 54 | Transaction declined due to invalid expiry details or the card is expired | Expired card | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Issuer Decline Error Codes | E9211 / response 25 | Unable to Locate Record on File | Unable to Locate Record on File | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Issuer Decline Error Codes | E9220 / response 68 | Response Received Too Late | Response Received Too Late | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Partner Integration Errors | Token expired | Auth | Refresh / contact KAM | Refresh / contact KAM |
| Refund Initiation Error Codes | 102 | Refund Queued | 102 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 103 | Request rejected on reconfirmation | 103 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 109 | Request is already logged | 109 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 121 | Incorrect/Empty value passed in retry | 121 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 123 | Request set as pending - requires manual follow-up | 123 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 125 | Merchant Failed the pending refund | 125 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 129 | Remark is mandatory for retry 0 | 129 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 249 | Retry the transaction | 249 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Initiation Error Codes | 266 | Chargeback is pending against this transaction | 266 | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Status Error Codes | R0003 | INVALID_OR_EXPIRED_VPA | Refund status error | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Status Error Codes | R0008 | TIMEOUT_AT_ACQUIRER_END | Refund status error | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Refund Status Error Codes | R0021 | TIMEOUT_AT_CUSTOMER_END | Refund status error | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Smart Send Error Codes | 1111 | LINK_EXPIRED | Smart Send Error Codes | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Smart Send Error Codes | 1127 | APPROVAL_PENDING | Smart Send Error Codes | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Transaction Stages Field7/Field8 | 3DS_METHOD_NEGATIVE | When 3DS Method is Shared but No Response on Notification | Indicates that while the 3DS method data was successfully sent to the ACS, PayU did not receive any response back at the notification URL within the expected timeframe. This could be due to network issues, ACS timeout... | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Transaction Stages Field7/Field8 | INTERROR | When no response received from the bank | Occurs when PayU initiates a payment request to the bank or payment processor, but does not receive any response within the expected timeframe. This typically indicates network connectivity issues, bank system downtim... | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Transaction Stages Field7/Field8 | TXNPENDING | For corp transaction Maker has made the transaction. Checker yet to approve | Specific to corporate banking transactions with dual authorization flows. This status indicates that the transaction initiator (Maker) has created the payment, but it is awaiting approval from an authorized approver (... | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |
| Transaction Stages Field7/Field8 | VERPENDING | For corp transaction Maker has made the transaction. Checker yet to approve | This status appears during verification calls for corporate transactions where the initiator (Maker) has created the payment, but the transaction is still awaiting approval from the authorized approver (Checker). The... | Keep the merchant order pending and reconcile with webhook or Transaction Detail APIs before retrying or fulfilling. |

<!-- PAYU_REPO_ERRORS_PENDING_TRANSACTIONS_END -->
