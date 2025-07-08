---
title: Test the Split During Transaction Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
## Test Environment

Use the test environment for development and testing:

* **API URL**: `https://test.payu.in/_payment`
* **Test Cards**:
  * Visa: 4012001037141112
  * MasterCard: 5123456789012346
  * Test CVV: 123
  * Test Expiry: Any future date

### Test Child Merchants

In the test environment, you can use test merchant keys for child merchants:

* **Test Merchant Key 1**: `TEST_MERCHANT_KEY_1`
* **Test Merchant Key 2**: `TEST_MERCHANT_KEY_2`

## Going Live

### Production Environment

Switch to production when testing is complete:

* **API URL**: `https://secure.payu.in/_payment`\*\*\*\*