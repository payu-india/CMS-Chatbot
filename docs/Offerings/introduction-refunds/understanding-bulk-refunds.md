---
title: Understanding Bulk Refunds
deprecated: false
hidden: true
icon: fab fa-cash-app
metadata:
  robots: index
---
---
title: Bulk Refund File Format
excerpt: 'Prepare the merchant-level file used to upload refunds in bulk.'
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---

ulk refunds let merchants initiate multiple refund requests at after uploading a file through the PayU Dashboard. PayU processes the uploaded file row by row: each row represents one refund request and can be accepted for processing or rejected if it does not meet the file requirements. A batch output file provides the processing result for each row, helping merchants review refund outcomes. 
Use this format to prepare the merchant-level file for a bulk refund upload. The file contains six columns: the first two columns are mandatory, followed by optional and Closed Loop Wallet-only conditional fields.

For the upload steps, see [Refunds Dashboard](doc:refunds-dashboard#upload-bulk-refunds-using-dashboard).

## Supported file types

Bulk refund uploads support `.xls`, `.xlsx`, and `.csv` files.

## File requirements

- The first two columns, `transactionid` and `amount`, are mandatory.
- Do not change the first two column headers.
- Include all six columns in the file, in the order shown below. Leave fields that do not apply blank.
- Use a unique filename for each upload.

## Merchant-level fields

The following fields are defined at the merchant level:

| Field name | Description | Requirement |
| --- | --- | --- |
| `transactionid` | Unique PayU Transaction ID (PayU ID) for which the refund is processed. | Mandatory |
| `amount` | Refund amount. | Mandatory |
| `remarks` | Additional information or notes for reference and future tracking. | Optional |
| `reference_id` | Merchant's unique refund reference ID for merchant-side tracking and reconciliation. | Optional |
| `refund_type` | Applicable only to Closed Loop Wallet merchants; other merchants may leave blank. Supported value: `wallet`. | Conditional: Closed Loop Wallet only |
| `customer_phone` | Customer's registered mobile number. Required only for Closed Loop Wallet refund processing; other merchants may leave blank. Supported value: a 10-digit phone number. | Conditional: Closed Loop Wallet only |

The first two fields, `transactionid` and `amount`, are mandatory for every merchant. The `remarks` and `reference_id` fields are optional. The `refund_type` and `customer_phone` fields are conditional: use them for Closed Loop Wallet refunds and leave them blank for other merchants. For Closed Loop Wallet refunds, set `refund_type` to `wallet` and provide the customer's registered 10-digit mobile number in `customer_phone`.

## Examples

The following examples show the six-column order. They are illustrative rows only.

### Standard refund row

For a non-Closed Loop Wallet refund, the two conditional fields are blank:

```csv
transactionid,amount,remarks,reference_id,refund_type,customer_phone
PayUTxn12345,500.00,Customer return,MER-REF-1001,,
```

### Closed Loop Wallet refund row

For a Closed Loop Wallet refund, provide `wallet` and the customer's registered 10-digit phone number:

```csv
transactionid,amount,remarks,reference_id,refund_type,customer_phone
PayUWallet67890,250.00,Wallet refund,MER-REF-1002,wallet,9876543210
```
