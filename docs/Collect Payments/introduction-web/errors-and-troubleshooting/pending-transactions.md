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

## When it occurs

Common signals:

* `status=pending`
* `unmappedstatus=in progress`
* `error=E227`
* `field7=TXNPENDING`, `VERPENDING`, `TXNERROR`, or `VERERROR`
* Browser redirect failed, but payment may still complete at bank end
* Corporate net banking transaction is waiting for checker approval

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

| Merchant state | PayU signal | Action |
| --- | --- | --- |
| `payment_initiated` | Request created | Await redirect/webhook/status. |
| `payment_pending` | `status=pending` or `E227` | Do not fulfill. Poll/reconcile. |
| `payment_success` | `status=success` and hash valid | Fulfill order. |
| `payment_failed` | `status=failure` and final status verified | Show retry options. |
| `payment_dropped` | `E231`, timeout, abandoned flow | Verify status before retry. |
| `payment_review` | Conflicting redirect/webhook/status | Hold fulfillment and reconcile. |

