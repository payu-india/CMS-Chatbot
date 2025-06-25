---
title: Test the Integration - Split After Transaction
deprecated: false
hidden: true
metadata:
  robots: index
---
> 📘 Note:
>
> Always test thoroughly in the sandbox environment with various split scenarios before implementing in production. Ensure proper error handling and validation for all edge cases.

## Step 1: Complete Base Transaction

* Process a regular transaction without split
* Note the PayU transaction ID (`payuId`)
* Ensure transaction is in completed/captured status

## Step 2: Prepare Post-Transaction Split Request

* **Test Endpoint**: `https://test.payu.in/merchant/postservice.php?form=2`
* **Method**: POST
* Create JSON for post-transaction split:

```json
{
  "type": "absolute",
  "payuId": "403993715525003544",
  "splitInfo": {
    "merchantKey1": {
      "aggregatorSubTxnId": "posttxn001",
      "aggregatorSubAmt": "600.00",
      "aggregatorCharges": "40.00"
    },
    "merchantKey2": {
      "aggregatorSubTxnId": "posttxn002",
      "aggregatorSubAmt": "360.00"
    }
  }
}
```

## Step 3: Generate Hash for Post-Transaction Split

* Hash format: `sha512(key|command|var1|salt)`
* **Sample Hash Generation**:

```bash
key="testMerchantKey"
command="payment_split"
var1='{"type":"absolute","payuId":"403993715525003544","splitInfo":{"merchantKey1":{"aggregatorSubTxnId":"posttxn001","aggregatorSubAmt":"600.00","aggregatorCharges":"40.00"},"merchantKey2":{"aggregatorSubTxnId":"posttxn002","aggregatorSubAmt":"360.00"}}}'
salt="testSalt"
```

## Step 4: Submit Split Request

* **Sample Request Payload**:

```json
{
  "key": "testMerchantKey",
  "command": "payment_split",
  "hash": "generated_hash_value",
  "var1": "{"type":"absolute","payuId":"403993715525003544","splitInfo":{"merchantKey1":{"aggregatorSubTxnId":"posttxn001","aggregatorSubAmt":"600.00","aggregatorCharges":"40.00"},"merchantKey2":{"aggregatorSubTxnId":"posttxn002","aggregatorSubAmt":"360.00"}}}"
}
```

## Step 5: Verify Post-Transaction Split Response

* **Expected Success Response**:

```json
{
  "status": 1,
  "message": "Splits creation successful.",
  "splitStatus": "success", 
  "splitSegments": [
    {
      "merchantKey": "merchantKey1",
      "amount": 600.00,
      "subvention_amount": 0,
      "txnId": "posttxn001",
      "additional_charges": 40.00,
      "transaction_fee": 600.00
    },
    {
      "merchantKey": "merchantKey2",
      "amount": 360.00,
      "txnId": "posttxn002",
      "subvention_amount": 0,
      "additional_charges": 0,
      "transaction_fee": 360.00
    }
  ]
}
```

***

## 🧪 Test Data and Credentials

### Authentication Test Data:

* **Merchant Key**: Use test merchant key from PayU dashboard
* **Salt**: Use test salt from PayU dashboard
* **Sub-Merchant Keys**: Test keys for participating merchants

### Transaction Test Data:

* **Transaction Amount**: ₹1000.00
* **Split 1**: ₹700.00 (Sub-merchant 1)
* **Split 2**: ₹250.00 (Sub-merchant 2)
* **Platform Fee**: ₹50.00 (optional)

### Card Test Data:

* **Card Number**: 5123456789012346
* **CVV**: 123
* **Expiry Month**: 12
* **Expiry Year**: 2025
* **Cardholder Name**: Test User

### Customer Test Data:

* **Name**: Test Customer
* **Email**: [testcustomer@payu.in](mailto:testcustomer@payu.in)
* **Phone**: 9876543210
* **Transaction ID**: txn\_test\_12345

***

<br />

* 🔐 SSL/TLS encryption validation

***

## 📊 Expected Results Verification

### During Transaction Split:

1. **Payment Status**: "success" with valid mihpayid
2. **Split Status**: "success" in splitInfo section
3. **Amount Distribution**: Correct amounts in splitSegments
4. **Transaction IDs**: Unique IDs for each split segment

### After Transaction Split:

1. **API Response**: Status = 1 with success message
2. **Split Segments**: Accurate amount distribution
3. **Charges**: Correct aggregator charges applied
4. **Settlement**: Funds distributed to respective accounts

***

## 🚨 Troubleshooting Common Issues

### Hash-Related Issues:

* **Problem**: Hash validation failed
* **Solution**: Verify hash generation sequence and special character encoding

### Split Amount Issues:

* **Problem**: "Split amounts do not match transaction amount"
* **Solution**: Ensure sum of all split amounts equals exact transaction amount

### Merchant Key Issues:

* **Problem**: Invalid merchant key in split request
* **Solution**: Verify all merchant keys are active and have split permissions

### Post-Transaction Split Issues:

* **Problem**: Cannot split after transaction
* **Solution**: Ensure original transaction is captured and not refunded

***

## Testing Checklist

### Pre-Testing Setup

* [ ] Test merchant accounts configured
* [ ] Sub-merchant accounts activated
* [ ] Hash generation logic implemented
* [ ] Test endpoints configured
* [ ] SSL certificates in place

### During Transaction Testing

* [ ] Split request properly formatted
* [ ] Hash generated correctly
* [ ] Payment flow completed
* [ ] Split response validated
* [ ] Settlement verification done

### After Transaction Testing

* [ ] Base transaction completed
* [ ] Post-split API called successfully
* [ ] Split response verified
* [ ] Settlement status checked
* [ ] Error scenarios tested

### Final Validation

* [ ] All split amounts reconciled
* [ ] Sub-merchant settlements confirmed
* [ ] Error handling validated
* [ ] Security measures tested
* [ ] Documentation updated

***