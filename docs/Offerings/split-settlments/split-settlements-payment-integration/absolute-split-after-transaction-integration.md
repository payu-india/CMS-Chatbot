---
title: Absolute Split After Transaction Integration
deprecated: false
hidden: false
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

<Split_Settlments_Prerequiisites />

**Steps to integrate:**

<Cards columns={2}>
  <Card title="1. Verify the Payment" href="#step-1-verify-the-payment">
    Verify the payment status to confirm the transaction is successful before initiating the split

    <br />
  </Card>

  <Card title="2. Prepare var1 JSON Payload" href="#step-2-prepare-var1-json-payload">
    Prepare the var1 JSON payload with the required split details and partner-specific parameters

    <br />
  </Card>

  <Card title="3. Generate Hash" href="#step-3-generate-hash">
    Generate a secure hash for the API request to ensure data integrity and authentication

    <br />
  </Card>

  <Card title="4. Call payment_split API" href="#step-4-call-payment_split-api">
    Make the API call to the payment\_split endpoint to execute the split on the verified transaction
  </Card>

  <br />
</Cards>

## Step 1: Verify the Payment

After completing the payment using the Collect Payment (**_payment**) API, perform this step to verify the payment.

<Callout icon="👍" theme="okay">
  **Reference:** Refer to any of the following API Reference pages for the sample request/response for collecting payments using the Collection (**_payment**)  API:

  * [Collect Payment API using PayU Hosted Checkout](https://docs.payu.in/reference/_payment_payu_hosted_checkout)
  * [Collect Payment API using Merchant Hosted Checkout](https://docs.payu.in/reference/_payment_merchant_hosted)
  * [Collect Payment API using S2S](https://docs.payu.in/reference/_payment_server_to_server)
</Callout>

Upon receiving the response, PayU recommends performing a reconciliation step to validate all transaction details. You can verify your payments using either of the following methods:

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
