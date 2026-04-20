---
title: UPI Convenience Fee Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: UPI Convenience Fee Integration
excerpt: 'Learn how to integrate and handle convenience fees for UPI Credit Card, PPI, and Credit Line payments.'
deprecated: false
hidden: false
metadata:
  title: UPI Convenience Fee Integration
  description: >-
    Complete guide to implementing convenience fees for UPICC (UPI Credit Card),
    UPIPPI (UPI PPI), and UPICL (UPI Credit Line) payments with PayU.
  keywords:
    - UPI Convenience Fee
    - UPICC Convenience Fee
    - CCONFEE
    - PCONFEE
    - Split tag UPI
    - UPI Credit Card fees
  robots: index
next:
  description: ''
---

This section describes how to implement and handle convenience fees for UPI-based payment modes including UPICC (UPI Credit Card), UPIPPI (UPI Prepaid Payment Instrument), and UPICL (UPI Credit Line).

NPCI has built a solution to support convenience fees for UPI instruments where charges are applicable. This solution allows merchants to accept transactions via UPICC, PPI, and Credit Line where the customer's payment amount gets updated while authorizing, and the merchant receives the transaction with the updated amount.

### Supported Payment Modes

| Mode   | Description                    | Ibibo Code |
| ------ | ------------------------------ | ---------- |
| UPICC  | UPI Credit Card                | INTCC      |
| UPIPPI | UPI Prepaid Payment Instrument | INTPPI     |
| UPICL  | UPI Credit Line                | INTCL      |

## How It Works

<Image align="center" src="https://files.readme.io/ada489770af12f7d7df3c9fb363573c4e5feffed4944f243bc46304656df51fc-upi-conv-fee-swimlane-diagram.png" />

### Split Tag in Intent String

When convenience fee is configured, PayU adds a `split` tag to the intent string:

```text
upi://pay?pa=merchant@icici&pn=Merchant&tr=675879299&tid=PPPL675879299&am=100.00&cu=INR&split=CCONFEE:2.13|PCONFEE:1.77
```

#### Split Tag Components

| Tag       | Description                             | Applicable For        |
| --------- | --------------------------------------- | --------------------- |
| `CCONFEE` | Credit Card/Credit Line Convenience Fee | UPICC, UPICL payments |
| `PCONFEE` | PPI Convenience Fee                     | UPIPPI payments       |

## Convenience Fee Calculation

### Rate Structure

The convenience fee is calculated based on the transaction amount and configured rates:

| Mode   | Rate Structure   | Example Calculation (Amount: ₹100)           |
| ------ | ---------------- | -------------------------------------------- |
| UPICC  | 1.8% + GST (18%) | 100 × 1.8% = 1.80 + (1.80 × 18%) = **₹2.13** |
| UPIPPI | 1.5% + GST (18%) | 100 × 1.5% = 1.50 + (1.50 × 18%) = **₹1.77** |
| UPICL  | 1.8% + GST (18%) | 100 × 1.8% = 1.80 + (1.80 × 18%) = **₹2.13** |

<Callout icon="📘" theme="info">
  **Note**: The actual rates may vary based on your merchant agreement. Contact your PayU Key Account Manager for your specific rate structure.
</Callout>

### Calculation Formula

```text
Convenience Fee = (Transaction Amount × Rate%) + (Transaction Amount × Rate% × GST%)
```

Example:

```text
Transaction Amount = ₹100
UPICC Rate = 1.8%
GST = 18%

CCONFEE = (100 × 0.018) + (100 × 0.018 × 0.18)
        = 1.80 + 0.324
        = 2.124
        ≈ ₹2.13 (rounded to next decimal)
```

## Integration Steps

### Step 1: Configure Convenience Fee

Contact your PayU Key Account Manager to configure convenience fee for UPI modes:

* UPICC (Credit Card)
* UPIPPI (PPI)
* UPICL (Credit Line)

Configuration is done at the merchant level through the PayU admin panel.

### Step 2: Initiate UPI Intent Transaction

Make a standard UPI Intent API call. PayU automatically calculates and adds convenience fee to the intent string.

```curl
curl --location 'https://secure.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=JPM****f' \
--data-urlencode 'txnid=conv_fee_txn_123' \
--data-urlencode 'amount=100.00' \
--data-urlencode 'productinfo=Order #123' \
--data-urlencode 'firstname=John' \
--data-urlencode 'email=john@example.com' \
--data-urlencode 'phone=9876543210' \
--data-urlencode 'pg=UPI' \
--data-urlencode 'bankcode=INTENT' \
--data-urlencode 'surl=https://merchant.com/success' \
--data-urlencode 'furl=https://merchant.com/failure' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'hash=<calculated_hash>'
```

### Step 3: Parse Intent String with Split Tag

The response contains an intent string with the split tag:

```json
{
  "result": {
    "intentURIData": "pa=merchant@icici&pn=Merchant&tr=675879299&tid=PPPL675879299&am=100.00&cu=INR&split=CCONFEE:2.13|PCONFEE:1.77"
  }
}
```

### Step 4: Handle Customer Payment

When the customer opens the UPI app:

1. **Credit Card Selected**: Amount updates to ₹102.13 (100 + 2.13 CCONFEE)
2. **PPI Selected**: Amount updates to ₹101.77 (100 + 1.77 PCONFEE)
3. **Savings/Current Account**: Amount remains ₹100 (no convenience fee)

### Step 5: Process Callback/Webhook

When payment completes, PayU sends a callback with the final amount including convenience fee.

#### Sample Callback Response (UPICC Payment)

```json
{
  "status": "success",
  "txnid": "conv_fee_txn_123",
  "amount": "102.13",
  "transaction_fee": "100.00",
  "additional_charges": "2.13",
  "mode": "UPICC",
  "bankcode": "INTCC"
}
```

## Database Storage

### Transaction Info Keys

PayU stores convenience fee values in the `txn_info` table with the following keys:

| Key       | Description                    | Usage                                      |
| --------- | ------------------------------ | ------------------------------------------ |
| `CCONFEE` | Convenience fee for CC/CL mode | Stored when intent generated with conv fee |
| `PCONFEE` | Convenience fee for PPI mode   | Stored when intent generated with conv fee |

These values are used for validation when payment authorization is received from the bank.

## Validation at PayU

PayU validates the payment amount received from the bank:

```text
Expected Amount = Transaction Amount + Applicable Convenience Fee

If (Received Amount ≠ Expected Amount):
    Transaction fails with amount mismatch error
```

### Validation Logic

```text
For UPICC/UPICL payments:
  Expected = transaction.amount + txn_info.CCONFEE

For UPIPPI payments:
  Expected = transaction.amount + txn_info.PCONFEE

For UPI Savings payments:
  Expected = transaction.amount (no convenience fee)
```

## Calculating Convenience Fee (Server-Side)

PayU calculates convenience fee using the `getAllowedIbiboCodesByCategory` function:

### Calculation Steps

1. Call `getAllowedIbiboCodesByCategory` method to get convenience fees on all active ibibo codes grouped by category
2. Check if `upicc`, `upicl`, or `upippi` category exists in the result
3. Get `additional_charges` under `intcc` or `intcl` ibibo_code → This becomes `CCONFEE`
4. If `upippi` is not blank and `additional_charges` under `intppi` is non-zero → This becomes `PCONFEE`
5. Add to the intent string in the format: `split=CCONFEE:value|PCONFEE:value`

## Response Parameters

### Payment Response with Convenience Fee

| Parameter            | Description                                   | Example  |
| -------------------- | --------------------------------------------- | -------- |
| `amount`             | Total amount paid (including convenience fee) | `102.13` |
| `transaction_fee`    | Original transaction amount                   | `100.00` |
| `additional_charges` | Convenience fee charged                       | `2.13`   |
| `mode`               | Payment mode used                             | `UPICC`  |

### Verify Payment Response

```json
{
  "status": 1,
  "msg": "1 Transaction Fetched Successfully",
  "transaction_details": {
    "conv_fee_txn_123": {
      "status": "success",
      "txnid": "conv_fee_txn_123",
      "amount": "102.13",
      "transaction_fee": "100.00",
      "additional_charges": "2.13",
      "mode": "UPICC",
      "PG_TYPE": "UPICC-INTCC"
    }
  }
}
```

## Reverse Hash Calculation

When convenience fee is applied, include `additional_charges` in the reverse hash:

### Hash Formula with Additional Charges

```text
sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

### Hash Formula without Additional Charges

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Callout icon="⚠️" theme="warning">
  **Important**: Always check if `additional_charges` parameter is present in the response before calculating reverse hash.
</Callout>

## Error Handling

### Common Errors

| Error Code | Error Message                  | Cause                                 | Resolution                            |
| ---------- | ------------------------------ | ------------------------------------- | ------------------------------------- |
| E1657      | Surcharge amount not permitted | Convenience fee exceeds allowed limit | Contact PayU support                  |
| E9209      | Unacceptable Transaction Fee   | Fee mismatch                          | Verify convenience fee calculation    |
| -          | Amount mismatch                | Received amount differs from expected | Check if customer paid correct amount |

## Best Practices

1. **Display Convenience Fee**: Show customers the convenience fee breakup before payment to avoid surprises.

2. **Handle Mode Changes**: The final mode may differ from the initiated mode based on customer's payment source. Always read the `mode` parameter in the response.

3. **Validate Response**: Always validate the reverse hash including `additional_charges` when present.

4. **Reconciliation**: Use `transaction_fee` for the original amount and `additional_charges` for convenience fee during reconciliation.

5. **Refund Handling**: Note that convenience fee handling during refunds may vary. Contact PayU for specific refund policies.

## Sample Code

### Parsing Split Tag (JavaScript)

```javascript
function parseSplitTag(intentUri) {
  const splitMatch = intentUri.match(/split=([^&]+)/);
  if (!splitMatch) return null;
  
  const splitParts = splitMatch[1].split('|');
  const fees = {};
  
  splitParts.forEach(part => {
    const [key, value] = part.split(':');
    fees[key] = parseFloat(value);
  });
  
  return fees;
  // Returns: { CCONFEE: 2.13, PCONFEE: 1.77 }
}
```

### Calculating Expected Amount (Java)

```java
public BigDecimal calculateExpectedAmount(String mode, BigDecimal txnAmount, 
                                          BigDecimal cconfee, BigDecimal pconfee) {
    switch (mode) {
        case "UPICC":
        case "UPICL":
            return txnAmount.add(cconfee);
        case "UPIPPI":
            return txnAmount.add(pconfee);
        default:
            return txnAmount;
    }
}
```

<br />
