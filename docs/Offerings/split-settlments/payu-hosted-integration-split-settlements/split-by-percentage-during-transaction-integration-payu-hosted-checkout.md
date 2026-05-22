---
title: '[INTERNAL REVIEW]Split by Percentage During Transaction Integration'
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Split by Percentage During Transaction Integration - PayU Hosted Checkout
excerpt: >-
  Integrate percentage-based split settlements with PayU Hosted Checkout using
  the `_payment` API, then confirm payment on redirect and webhooks.
deprecated: false
hidden: false
metadata:
  title: Split by Percentage During Transaction Integration - PayU Hosted Checkout
  description: >-
    Step-by-step guide to split a payment by percentage at transaction time using
    PayU Hosted Checkout, splitRequest, request hash, and webhook verification.
  robots: index
next:
  description: ''
---

Use this integration to distribute a payment by percentage among child merchants at transaction time with **PayU Hosted Checkout**. Set `type` to `percentage` and ensure the total across all splits equals **100**.

<Callout icon="👍">
  **Reference**: For the full API contract, refer to [Split by Percentage During Transaction - PayU Hosted Checkout](ref:split-by-percentage-during-transaction-payu-hosted-checkout).
</Callout>

## Prerequisites

Before implementing:

1. Parent merchant account is enabled for Split Settlements.
2. Child merchants are onboarded and mapped.
3. Merchant `key` and `salt` are available.
4. Your backend can generate hash and process redirect callbacks and webhooks.

## Step 1: Build splitRequest for percentage split

Use `type: "percentage"` and assign percentage values in `aggregatorSubAmt`.

```json
{
  "type": "percentage",
  "splitInfo": {
    "gYoEaY": {
      "aggregatorSubTxnId": "child_1779180636589_7309",
      "aggregatorSubAmt": "50",
      "aggregatorCharges": "0.00"
    },
    "5rgA73": {
      "aggregatorSubTxnId": "child_1779180636590_5791",
      "aggregatorSubAmt": "50",
      "aggregatorCharges": "0.00"
    }
  }
}
```

> **Important:** Ensure the total split percentage equals **100.00**. Use two decimal places for each split.

## Step 2: Generate request hash

Hash pattern with split request. The JSON string in the hash must match exactly what you post in the request.

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

Example hash input string:

```plaintext
a4vGC2|TXN_SPL_1779178418_441|2000|iPhone|John|pragram@gmail.com|||||||||||YOUR_SALT|{"type":"percentage","splitInfo":{"gYoEaY":{"aggregatorSubTxnId":"child_1779180636589_7309","aggregatorSubAmt":"50","aggregatorCharges":"0.00"},"5rgA73":{"aggregatorSubTxnId":"child_1779180636590_5791","aggregatorSubAmt":"50","aggregatorCharges":"0.00"}}}
```

For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

## Step 3: Submit payment request to `_payment`

Use:

* Test: `https://test.payu.in/_payment`
* Production: `https://secure.payu.in/_payment`

PayU Hosted Checkout does not require card parameters (`pg`, `bankcode`, `ccnum`, and so on). The customer selects the payment method on PayU's page.

Sample request:

```curl
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=a4vGC2" \
  -d "txnid=TXN_SPL_1779178418_441" \
  -d "amount=2000" \
  -d "productinfo=iPhone" \
  -d "firstname=John" \
  -d "lastname=Doe" \
  -d "email=pragram@gmail.com" \
  -d "phone=9876543210" \
  --data-urlencode 'splitRequest={"type":"percentage","splitInfo":{"gYoEaY":{"aggregatorSubTxnId":"child_1779180636589_7309","aggregatorSubAmt":"50","aggregatorCharges":"0.00"},"5rgA73":{"aggregatorSubTxnId":"child_1779180636590_5791","aggregatorSubAmt":"50","aggregatorCharges":"0.00"}}}' \
  -d "surl=https://payu.in/integrationlab/callback.php" \
  -d "furl=https://payu.in/integrationlab/callback.php" \
  -d "hash=<generated_hash>"
```

You can also submit the same parameters from an HTML form with `method="post"` and `action="https://test.payu.in/_payment"` to redirect the browser to PayU Hosted Checkout.

On success, PayU returns the hosted payment page (HTML). The customer completes payment on PayU.

## Step 4: Validate redirect response using reverse hash

When PayU posts data to your `surl` or `furl`, validate reverse hash before finalizing state:

```plaintext
sha512(SALT|status|splitInfo||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

**Response parameters**:

| Parameter   | Description                                        |
| ----------- | -------------------------------------------------- |
| `status`    | Payment status (`success`, `failure`, `pending`)   |
| `txnid`     | Transaction ID sent in the request                 |
| `amount`    | Transaction amount                                 |
| `mihpayid`  | PayU payment ID                                    |
| `splitInfo` | JSON string with `splitStatus` and `splitSegments` |

**Example response** (parsed `splitInfo`):

```json
{
  "status": "success",
  "txnid": "TXN_SPL_1779178418_441",
  "amount": "2000.00",
  "mihpayid": "403993715519672950",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "gYoEaY",
        "amount": 1000,
        "txnId": "child_1779180636589_7309"
      },
      {
        "merchantKey": "5rgA73",
        "amount": 1000,
        "txnId": "child_1779180636590_5791"
      }
    ]
  }
}
```

## Step 5: Confirm payment via webhooks

Use webhook notifications as your final payment confirmation mechanism.

1. Configure webhook URL in PayU Dashboard.
2. Subscribe to relevant payment events.
3. Verify webhook signature and ignore duplicate deliveries using idempotency checks.
4. Mark the order paid only after a successful webhook event.
5. Store split metadata from the webhook payload for reconciliation and settlement tracking.

### Sample webhook payload (illustrative)

```json
{
  "event": "payment.success",
  "txnid": "TXN_SPL_1779178418_441",
  "mihpayid": "403993715519672951",
  "status": "success",
  "amount": "2000.00",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "gYoEaY",
        "amount": 1000,
        "txnId": "child_1779180636589_7309"
      },
      {
        "merchantKey": "5rgA73",
        "amount": 1000,
        "txnId": "child_1779180636590_5791"
      }
    ]
  }
}
```

## [Optional] Check the transaction info

Verify split allocation using the [Get Aggregator/Parent Transaction Info API](ref:get_aggregator_parent_transaction_info_api).

```curl
curl -X POST "https://info.payu.in/merchant/postservice?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=a4vGC2" \
  -d "command=get_aggregator_transactions" \
  -d "var1=2024-01-15 10:00" \
  -d "var2=2024-01-15 23:59" \
  -d "var3=1" \
  -d "var4=100" \
  -d "var5=1" \
  -d "hash=<generated_hash>"
```

For server-to-server reconciliation samples in multiple languages, refer to [Split by Percentage During Transaction Integration](doc:split-by-percentage-during-transaction-integration).

## Go-live checklist

* Ensure split percentages sum to **100.00**.
* Use unique `txnid` and `aggregatorSubTxnId` values per attempt.
* URL-encode `splitRequest` when posting as form data.
* Keep `splitRequest` JSON compact and deterministic before hashing.
* Validate reverse hash in redirect handler.
* Validate webhook signature and implement idempotent webhook processing.
* Move from test endpoint to production endpoint only after complete UAT.

## Related documentation

* [Split by Percentage During Transaction - PayU Hosted Checkout](ref:split-by-percentage-during-transaction-payu-hosted-checkout) — API reference
* [Absolute Split During Transaction Integration - PayU Hosted Checkout](doc:absolute-split-during-transaction-payu-hosted-checkout-integration)
* [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)