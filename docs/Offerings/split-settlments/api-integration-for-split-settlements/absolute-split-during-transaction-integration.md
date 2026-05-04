---
title: Absolute Split During Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Absolute Split During Transaction Integration
excerpt: >-
  Integrate split settlements using absolute amounts with the `_payment` API and
  confirm transaction outcome using webhooks.
deprecated: false
hidden: false
metadata:
  title: Absolute Split During Transaction Integration
  description: >-
    Learn how to integrate the `_payment` API for absolute split settlements,
    generate request hash, send splitRequest, and verify successful payment using
    webhook events.
  robots: index
next:
  description: ''
---
Use this integration to split a parent transaction into fixed amounts at payment time using the `_payment` API.

In an absolute split, each child merchant receives an exact amount (`aggregatorSubAmt`) that you define in advance.

## Prerequisites

Before you start, ensure the following:

1. Your parent merchant account is enabled for Split Settlements.
2. Child merchants are onboarded and available for split mapping.
3. You have your merchant `key` and `salt`.
4. You have server-side logic to generate hash and process webhooks.

## Step 1: Build splitRequest for absolute split

Create the `splitRequest` JSON with `type` as `absolute`.

```json
{
  "type": "absolute",
  "splitInfo": {
    "P41sCY": {
      "aggregatorSubTxnId": "subtxn-abs-001",
      "aggregatorSubAmt": "600.00",
      "aggregatorCharges": "50.00"
    },
    "P41sCK": {
      "aggregatorSubTxnId": "subtxn-abs-002",
      "aggregatorSubAmt": "350.00"
    }
  }
}
```

> **Important:** The total of all child split amounts plus parent charges must equal the transaction amount.

## Step 2: Generate request hash

Include `splitRequest` at the end of the hash sequence:

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

Example hash input string:

```plaintext
Ax4j7J|txn-abs-1001|1000.00|Order #1001|Aman|aman@example.com|||||||||||t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL|{"type":"absolute","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"subtxn-abs-001","aggregatorSubAmt":"600.00","aggregatorCharges":"50.00"},"P41sCK":{"aggregatorSubTxnId":"subtxn-abs-002","aggregatorSubAmt":"350.00"}}}
```

## Step 3: Submit payment request to `_payment`

Use the environment endpoint:

- Test: `https://test.payu.in/_payment`
- Production: `https://secure.payu.in/_payment`

Sample request:

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=Ax4j7J" \
  -d "txnid=txn-abs-1001" \
  -d "amount=1000.00" \
  -d "productinfo=Order #1001" \
  -d "firstname=Aman" \
  -d "email=aman@example.com" \
  -d "phone=9999999999" \
  -d "api_version=7" \
  -d "surl=https://merchant.example.com/payu/success" \
  -d "furl=https://merchant.example.com/payu/failure" \
  -d 'splitRequest={"type":"absolute","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"subtxn-abs-001","aggregatorSubAmt":"600.00","aggregatorCharges":"50.00"},"P41sCK":{"aggregatorSubTxnId":"subtxn-abs-002","aggregatorSubAmt":"350.00"}}}' \
  -d "hash=<generated_hash>"
```

## Step 4: Handle checkout response on success/failure URL

PayU posts response parameters to your `surl` or `furl`. Always validate reverse hash before updating order state.

Reverse hash format for split response:

```plaintext
sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

## Step 5: Verify final payment state using webhooks

Do not rely only on browser redirects. Use webhooks as the source of truth for final payment outcome.

1. Configure a webhook URL on PayU Dashboard.
2. Subscribe to payment status events relevant to your flow.
3. Validate webhook authenticity using your webhook signature validation logic.
4. Mark order as paid only when webhook confirms a successful captured transaction.
5. Persist `txnid`, `mihpayid`, status, and `splitInfo` for reconciliation.

### Sample webhook payload (illustrative)

```json
{
  "event": "payment.success",
  "txnid": "txn-abs-1001",
  "mihpayid": "403993715519672950",
  "status": "success",
  "amount": "1000.00",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "P41sCY",
        "amount": 600,
        "txnId": "subtxn-abs-001"
      },
      {
        "merchantKey": "P41sCK",
        "amount": 350,
        "txnId": "subtxn-abs-002"
      }
    ]
  }
}
```

## Go-live checklist

- Use unique `txnid` and unique `aggregatorSubTxnId` values.
- Keep `splitRequest` JSON compact and deterministic before hashing.
- Confirm reverse-hash validation on redirect response.
- Confirm webhook delivery, signature verification, and idempotent processing.
- Switch endpoint from test to production only after successful end-to-end tests.