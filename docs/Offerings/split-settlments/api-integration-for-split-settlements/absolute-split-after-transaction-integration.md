---
title: Absolute Split After Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Absolute Split After Transaction Integration
excerpt: >-
  Integrate `payment_split` API to split a completed transaction using absolute
  amounts.
deprecated: false
hidden: false
metadata:
  title: Absolute Split After Transaction Integration
  description: >-
    Learn how to call `payment_split` with absolute split values after payment
    completion and verify payment details.
  robots: index
next:
  description: ''
---

Use this integration to split a completed parent transaction into fixed amounts using the `payment_split` API.

In absolute split mode, each child merchant receives a fixed amount through `aggregatorSubAmt`.

## Prerequisites

Before integrating:

1. Split Settlements is enabled for your parent merchant account.
2. Child merchants are onboarded and active.
3. You have the merchant `key` and `salt`.
4. You have the `payuId` of the already completed parent transaction.

## Step 1: Verify the Payment

After completing the payment using **_payment** API, perform this step to verify the payment. Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

<Verify_Payment_Tabs />

## Step 2: Prepare var1 JSON payload

Set `type` as `absolute` and pass parent `payuId`:

```json
{
  "type": "absolute",
  "payuId": "403993715525003544",
  "splitInfo": {
    "merchantKey1": {
      "aggregatorSubTxnId": "subtxn-abs-after-001",
      "aggregatorSubAmt": "800.00",
      "aggregatorCharges": "100.00"
    },
    "merchantKey2": {
      "aggregatorSubTxnId": "subtxn-abs-after-002",
      "aggregatorSubAmt": "100.00"
    }
  }
}
```

> **Important:** Ensure all split amounts and charges map correctly to the original transaction amount.

## Step 3: Generate hash

Use:

```plaintext
sha512(key|command|var1|salt)
```

Where:

* `command` = `payment_split`
* `var1` = compact JSON string from Step 1

## Step 4: Call payment_split API

Environment endpoints:

* Test: `https://test.payu.in/merchant/postservice.php?form=2`
* Production: `https://info.payu.in/merchant/postservice.php?form=2`

Sample request:

```curl
curl -X POST "https://test.payu.in/merchant/postservice.php?form=2" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=vDy3i7" \
  -d "command=payment_split" \
  -d 'var1={"type":"absolute","payuId":"403993715525003544","splitInfo":{"merchantKey1":{"aggregatorSubTxnId":"subtxn-abs-after-001","aggregatorSubAmt":"800.00","aggregatorCharges":"100.00"},"merchantKey2":{"aggregatorSubTxnId":"subtxn-abs-after-002","aggregatorSubAmt":"100.00"}}}' \
  -d "hash=<generated_hash>"
```

Sample success response:

```json
{
  "status": 1,
  "message": "Splits creation successful.",
  "splitStatus": "success",
  "splitSegments": [
    {
      "merchantKey": "merchantKey1",
      "amount": 800,
      "subvention_amount": 0,
      "txnId": "subtxn-abs-after-001",
      "additional_charges": 0,
      "transaction_fee": 800
    },
    {
      "merchantKey": "merchantKey2",
      "amount": 100,
      "subvention_amount": 0,
      "txnId": "subtxn-abs-after-002",
      "additional_charges": 0,
      "transaction_fee": 100
    }
  ]
}
```

<br />
