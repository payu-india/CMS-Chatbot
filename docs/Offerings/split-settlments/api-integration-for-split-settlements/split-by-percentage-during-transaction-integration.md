---
title: Split by Percentage During Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Split by Percentage During Transaction Integration
excerpt: >-
  Integrate split settlements using percentage distribution with the `_payment`
  API and confirm payment status through webhooks.
deprecated: false
hidden: false
metadata:
  title: Split by Percentage During Transaction Integration
  description: >-
    Learn how to pass splitRequest with percentage splits in `_payment`, generate
    hash, and verify the payment outcome using webhooks.
  robots: index
next:
  description: ''
---
Use this integration when you want to distribute a payment by percentage among multiple merchants at transaction time.

In this mode, set `type` as `percentage` and ensure that the total percentage across all split entries is exactly 100.

## Prerequisites

Before implementing:

1. Parent merchant account is enabled for Split Settlements.
2. Child merchants are onboarded and mapped.
3. Merchant `key` and `salt` are available.
4. Your backend can generate hash and process webhook events.

## Step 1: Build splitRequest for percentage split

Use `type: "percentage"` and assign percentage values in `aggregatorSubAmt`.

```json
{
  "type": "percentage",
  "splitInfo": {
    "P41sCY": {
      "aggregatorSubTxnId": "subtxn-per-001",
      "aggregatorSubAmt": "55.00",
      "aggregatorCharges": "5.00"
    },
    "P41sCK": {
      "aggregatorSubTxnId": "subtxn-per-002",
      "aggregatorSubAmt": "40.00"
    }
  }
}
```

> **Important:** Ensure the total split percentage equals `100.00`.

## Step 2: Generate request hash

Hash pattern with split request:

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

Example hash input string:

```plaintext
Ax4j7J|txn-per-1001|1000.00|Order #2001|Aman|aman@example.com|||||||||||t5atu4TyCvrJDPxAYrmfJfzd90kbXMfL|{"type":"percentage","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"subtxn-per-001","aggregatorSubAmt":"55.00","aggregatorCharges":"5.00"},"P41sCK":{"aggregatorSubTxnId":"subtxn-per-002","aggregatorSubAmt":"40.00"}}}
```

## Step 3: Submit payment request to `_payment`

Use:

- Test: `https://test.payu.in/_payment`
- Production: `https://secure.payu.in/_payment`

Sample request:

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=Ax4j7J" \
  -d "txnid=txn-per-1001" \
  -d "amount=1000.00" \
  -d "productinfo=Order #2001" \
  -d "firstname=Aman" \
  -d "email=aman@example.com" \
  -d "phone=9999999999" \
  -d "api_version=7" \
  -d "surl=https://merchant.example.com/payu/success" \
  -d "furl=https://merchant.example.com/payu/failure" \
  -d 'splitRequest={"type":"percentage","splitInfo":{"P41sCY":{"aggregatorSubTxnId":"subtxn-per-001","aggregatorSubAmt":"55.00","aggregatorCharges":"5.00"},"P41sCK":{"aggregatorSubTxnId":"subtxn-per-002","aggregatorSubAmt":"40.00"}}}' \
  -d "hash=<generated_hash>"
```

## Step 4: Validate redirect response using reverse hash

When PayU posts data to your `surl` or `furl`, validate reverse hash before finalizing state:

```plaintext
sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

## Step 5: Confirm payment via webhooks

Use webhook notifications as your final payment confirmation mechanism.

1. Configure webhook URL in PayU Dashboard.
2. Subscribe to relevant payment events.
3. Verify webhook signature and ignore duplicate deliveries using idempotency checks.
4. Mark order paid only after a successful webhook event.
5. Store split metadata from webhook payload for reconciliation and settlement tracking.

### Sample webhook payload (illustrative)

```json
{
  "event": "payment.success",
  "txnid": "txn-per-1001",
  "mihpayid": "403993715519672951",
  "status": "success",
  "amount": "1000.00",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "P41sCY",
        "amount": 550,
        "txnId": "subtxn-per-001"
      },
      {
        "merchantKey": "P41sCK",
        "amount": 400,
        "txnId": "subtxn-per-002"
      }
    ]
  }
}
```

## Go-live checklist

- Ensure split percentages sum to `100.00`.
- Use unique `txnid` and `aggregatorSubTxnId` values per attempt.
- Validate reverse hash in redirect handler.
- Validate webhook signature and implement idempotent webhook processing.
- Move from test endpoint to production endpoint only after complete UAT.
