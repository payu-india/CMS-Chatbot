---
title: Split During Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
## API Integration

<br />

## Test the Integration

### Test Environment

Use the test environment for development and testing:

* **API URL**: `https://test.payu.in/_payment`
* **Test Cards**:
  * Visa: 4012001037141112
  * MasterCard: 5123456789012346
  * Test CVV: 123
  * Test Expiry: Any future date

#### Test Child Merchants

In the test environment, you can use test merchant keys for child merchants:

* **Test Merchant Key 1**: `TEST_MERCHANT_KEY_1`
* **Test Merchant Key 2**: `TEST_MERCHANT_KEY_2`

### Steps to test the integration

<Callout icon="📘" theme="info">
  **Note**: Always test thoroughly in the Test environment with various split scenarios before implementing in production. Ensure proper error handling and validation for all edge cases.
</Callout>

#### Step 1: Prepare Split Configuration

* Define absolute split amounts for each sub-merchant
* Ensure total split amounts equal the transaction amount
* **Sample Split Configuration**:

```json
{
  "type": "absolute",
  "splitInfo": {
    "merchantKey1": {
      "aggregatorSubTxnId": "subtxn001",
      "aggregatorSubAmt": "700.00",
      "aggregatorCharges": "50.00"
    },
    "merchantKey2": {
      "aggregatorSubTxnId": "subtxn002", 
      "aggregatorSubAmt": "250.00"
    }
  }
}
```

#### Step 2: Generate Security Hash

* Create SHA-512 hash using the format:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||||SALT|splitRequest)
```

* **Test Hash Example**:

```bash
key="testMerchantKey"
txnid="txn12345"
amount="1000.00"
productinfo="Test Product"
firstname="John"
email="john@test.com"
salt="testSalt"
splitRequest='{"type":"absolute","splitInfo":{"merchantKey1":{"aggregatorSubTxnId":"subtxn001","aggregatorSubAmt":"700.00","aggregatorCharges":"50.00"},"merchantKey2":{"aggregatorSubTxnId":"subtxn002","aggregatorSubAmt":"250.00"}}}'
```

#### Step 3: Submit Payment Request

* **Test Endpoint**: `https://test.payu.in/_payment`
* **Method**: POST
* **Sample Request Payload**:

```json
{
  "key": "testMerchantKey",
  "txnid": "txn12345", 
  "amount": "1000.00",
  "productinfo": "Test Product",
  "firstname": "John",
  "email": "john@test.com",
  "phone": "9876543210",
  "pg": "CC",
  "bankcode": "SBIN",
  "surl": "https://merchant.com/success",
  "furl": "https://merchant.com/failure",
  "splitRequest": {
    "type": "absolute",
    "splitInfo": {
      "merchantKey1": {
        "aggregatorSubTxnId": "subtxn001",
        "aggregatorSubAmt": "700.00",
        "aggregatorCharges": "50.00"
      },
      "merchantKey2": {
        "aggregatorSubTxnId": "subtxn002",
        "aggregatorSubAmt": "250.00"
      }
    }
  },
  "hash": "generated_hash_value"
}
```

#### Step 4: Process Test Payment

* Use **test card details**:
  * **Card Number**: 5123456789012346
  * **CVV**: 123
  * **Expiry**: Any future date (MM/YYYY format)
  * **Name**: Any name
* Complete payment flow and verify split processing

#### Step 5: Verify Split Response

* **Expected Success Response**:

```json
{
  "mihpayid": "41236782383977",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "testMerchantKey",
  "txnid": "txn12345",
  "amount": "1000.00",
  "splitInfo": {
    "splitStatus": "success",
    "splitSegments": [
      {
        "merchantKey": "merchantKey1",
        "amount": 700.00,
        "txnId": "subtxn001",
        "charges": 50.00
      },
      {
        "merchantKey": "merchantKey2", 
        "amount": 250.00,
        "txnId": "subtxn002"
      }
    ]
  }
}
```

***

### Going Live

#### Production Environment

Switch to production when testing is complete:

* **API URL**: `https://secure.payu.in/_payment`****
