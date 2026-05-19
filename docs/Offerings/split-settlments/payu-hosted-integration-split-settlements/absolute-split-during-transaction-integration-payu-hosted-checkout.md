---
title: Absolute Split During Transaction Integration - PayU Hosted Checkout
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Absolute Split During Transaction Integration - PayU Hosted Checkout
excerpt: >-
  Integrate absolute split settlements with PayU Hosted Checkout using the
  `_payment` API, then confirm payment on redirect and webhooks.
deprecated: false
hidden: false
metadata:
  title: Absolute Split During Transaction Integration - PayU Hosted Checkout
  description: >-
    Step-by-step guide to split a payment by fixed amount at transaction time
    using PayU Hosted Checkout, splitRequest, request hash, and webhook
    verification.
  robots: index
next:
  description: ''
---

Use this integration to split a parent transaction into fixed amounts at payment time with **PayU Hosted Checkout**. You post `_payment` with `splitRequest`; PayU redirects the customer to the hosted payment page, then returns transaction and split details to your `surl` or `furl`.

<Callout icon="📘" theme="info">
  **Reference**: For the full API contract, refer to [Absolute Split During Transaction - PayU Hosted Checkout](ref:absolute-split-during-transaction-payu-hosted-checkout).
</Callout>

## Prerequisites

Before you start, ensure the following:

1. Your parent merchant account is enabled for Split Settlements.
2. Child merchants are onboarded and available for split mapping.
3. You have your merchant `key` and `salt`.
4. You have server-side logic to generate hash and process redirect callbacks and webhooks.

## Step 1: Build splitRequest for absolute split

Create the `splitRequest` JSON with `type` as `absolute`. Each child receives a fixed amount in `aggregatorSubAmt`.

```json
{
  "type": "absolute",
  "splitInfo": {
    "gYoEaY": {
      "aggregatorSubTxnId": "child_1779181092078_285",
      "aggregatorSubAmt": "1000",
      "aggregatorCharges": "0.00"
    },
    "5rgA73": {
      "aggregatorSubTxnId": "child_1779181092078_6955",
      "aggregatorSubAmt": "1000",
      "aggregatorCharges": "0.00"
    }
  }
}
```

> **Important:** The sum of all child `aggregatorSubAmt` values (and any parent charges) must equal the transaction `amount`.

## Step 2: Generate request hash

Include `splitRequest` at the end of the hash sequence. The JSON string in the hash must match exactly what you post in the request.

```plaintext
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT|splitRequest)
```

Example hash input string:

```plaintext
a4vGC2|TXN_SPL_1779178418_441|2000|iPhone|John|pragram@gmail.com|||||||||||YOUR_SALT|{"type":"absolute","splitInfo":{"gYoEaY":{"aggregatorSubTxnId":"child_1779181092078_285","aggregatorSubAmt":"1000","aggregatorCharges":"0.00"},"5rgA73":{"aggregatorSubTxnId":"child_1779181092078_6955","aggregatorSubAmt":"1000","aggregatorCharges":"0.00"}}}
```

For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).

## Step 3: Submit payment request to `_payment`

Use the environment endpoint:

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
  --data-urlencode 'splitRequest={"type":"absolute","splitInfo":{"gYoEaY":{"aggregatorSubTxnId":"child_1779181092078_285","aggregatorSubAmt":"1000","aggregatorCharges":"0.00"},"5rgA73":{"aggregatorSubTxnId":"child_1779181092078_6955","aggregatorSubAmt":"1000","aggregatorCharges":"0.00"}}}' \
  -d "surl=https://payu.in/integrationlab/callback.php" \
  -d "furl=https://payu.in/integrationlab/callback.php" \
  -d "hash=<generated_hash>"
```

You can also submit the same parameters from an HTML form with `method="post"` and `action="https://test.payu.in/_payment"` to redirect the browser to PayU Hosted Checkout.

On success, PayU returns the hosted payment page (HTML). The customer completes payment on PayU.

## Step 4: Handle checkout response on success/failure URL

PayU posts response parameters to your `surl` or `furl`. Always validate reverse hash before updating order state.

Reverse hash format for split response:

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
        "txnId": "child_1779181092078_285"
      },
      {
        "merchantKey": "5rgA73",
        "amount": 1000,
        "txnId": "child_1779181092078_6955"
      }
    ]
  }
}
```

## Step 5: Verify final payment state using webhooks

Do not rely only on browser redirects. Use webhooks as the source of truth for final payment outcome.

1. Configure a webhook URL on PayU Dashboard.
2. Subscribe to payment status events relevant to your flow.
3. Validate webhook authenticity using your webhook signature validation logic.
4. Mark the order as paid only when the webhook confirms a successful captured transaction.
5. Persist `txnid`, `mihpayid`, `status`, and `splitInfo` for reconciliation.

### Sample webhook payload (illustrative)

```json
{
  "event": "payment.success",
  "txnid": "TXN_SPL_1779178418_441",
  "mihpayid": "403993715519672950",
  "status": "success",
  "amount": "2000.00",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "gYoEaY",
        "amount": 1000,
        "txnId": "child_1779181092078_285"
      },
      {
        "merchantKey": "5rgA73",
        "amount": 1000,
        "txnId": "child_1779181092078_6955"
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

For server-to-server reconciliation samples in multiple languages, refer to [Absolute Split During Transaction Integration](doc:absolute-split-during-transaction-integration).

## Go-live checklist

* Confirm split amounts sum to the transaction `amount`.
* Use unique `txnid` and unique `aggregatorSubTxnId` values per attempt.
* URL-encode `splitRequest` when posting as form data.
* Keep `splitRequest` JSON compact and deterministic before hashing.
* Confirm reverse-hash validation on redirect response.
* Confirm webhook delivery, signature verification, and idempotent processing.
* Switch endpoint from test to production only after successful end-to-end tests.

## Related documentation

* [Absolute Split During Transaction - PayU Hosted Checkout](ref:absolute-split-during-transaction-payu-hosted-checkout) — API reference
* [Split by Percentage During Transaction Integration - PayU Hosted Checkout](doc:split-by-percentage-during-transaction-payu-hosted-checkout-integration)
* [Collect Payment API - PayU Hosted Checkout](ref:_payment_payu_hosted_checkout)
