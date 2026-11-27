---
title: Cancel a Pre-Auth Transaction
deprecated: false
hidden: true
metadata:
  robots: index
---
The `cancel_transaction` API command releases a pre-authorized hold back to the customer's account or credit line.

<Callout icon="far fa-circle-info" theme="info">
  ## Key Operational Rules

  * **Applies Only to Authorized Holds**: Use `cancel_transaction` only while `unmappedstatus` is `"auth"`.
  * **Zero Processing Fee**: No Transaction Discount Rate (TDR) is levied on cancelled authorizations.
  * **Instant Reversals**: Because funds were merely held and never settled, the hold is released immediately.
  * **Captured Transactions**: Once funds are captured (`unmappedstatus=captured`), you cannot cancel the hold. You must execute a refund using `cancel_refund_transaction`.


</Callout>

## Environment

| Environment    | URL              |
| :------------- | :--------------- |
| **Test**       | `<redacted URL>` |
| **Production** | `<redacted URL>` |

***

## Hash Calculation Formula

```text
sha512(key|command|var1|salt)
```

_(Where&#x20;_`var1`_&#x20;is the&#x20;_`mihpayid`_&#x20;/ PayU ID)._

***

## Request Parameters

### Mandatory Parameters

| Parameter | Type   | Description                                                     | Example              |
| :-------- | :----- | :-------------------------------------------------------------- | :------------------- |
| `key`     | String | Merchant Key provided by PayU.                                  | `JPM7Fg`             |
| `command` | String | Must be set to `cancel_transaction`.                            | `cancel_transaction` |
| `hash`    | String | Calculated SHA-512 hash: `sha512(key\|command\|var1\|salt)`.    | `67411736ab...`      |
| `var1`    | String | PayU Transaction ID (`mihpayid`) received during authorization. | `403993715523615328` |
| `var2`    | String | Merchant Transaction ID (`txnid`).                              | `ORD_20261120_001`   |
| `var3`    | String | Amount to release (full authorization amount).                  | `1000.00`            |

***

## Sample Request: Cancel Transaction

```bash
curl -X POST "<redacted URL>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg" \
  -d "command=cancel_transaction" \
  -d "var1=403993715523615328" \
  -d "var2=ORD_20261120_001" \
  -d "var3=1000.00" \
  -d "hash=CALCULATED_CANCEL_HASH"
```

### Sample Response: Card Authorization Cancel

```json
{
  "status": 1,
  "msg": "Transaction Cancelled Successfully",
  "request_id": "REQ_CAN_1234567",
  "bank_ref_num": "7f0d5ada-59bb-41d7-9e41-20a6af2406c9"
}
```

### Sample Response: UPI One-Time Mandate Revoke

```json
{
  "status": 1,
  "action": "MANDATE_REVOKE",
  "message": "Mandate Revoke request processed successfully"
}
```
