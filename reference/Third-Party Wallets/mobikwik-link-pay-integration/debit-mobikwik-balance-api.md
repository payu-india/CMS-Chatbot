---
title: Debit Mobikwik Balance API
deprecated: false
hidden: true
metadata:
  robots: index
---

This API allows merchants to debit a specified amount from a user's Mobikwik wallet for transaction processing.

## Environment

| Environment | URL |
|-------------|-----|
| **Test** | `https://test.mobikwik.com/debitwallet` |
| **Production** | `https://walletapi.mobikwik.com/debitwallet` |

**Method:** `GET`  

## Request parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| mid<br/><code>mandatory</code> | <code>String</code> Unique parent merchant ID | `MBK9006` |
| cell<br/><code>mandatory</code> | <code>String</code> Mobile number of the user | `9311032820` |
| amount<br/><code>mandatory</code> | <code>Decimal</code> Amount to be debited from wallet | `150.50` |
| orderid<br/><code>mandatory</code> | <code>String</code> Unique order identifier | `ORDER_123456` |
| token<br/><code>mandatory</code> | <code>String</code> Valid wallet token for the user | `MBK_TOKEN_123456789` |
| merchantname<br/><code>mandatory</code> | <code>String</code> Alias for the merchant | `TestMerchant` |
| msgcode<br/><code>mandatory</code> | <code>String</code> Message code | `504` |
| comment<br/><code>optional</code> | <code>String</code> Transaction description/comment | `Payment for order` |
| txntype<br/><code>mandatory</code> | <code>String</code> Transaction type | `DEBIT` |
| checksum<br/><code>mandatory</code> | <code>String</code> Calculated checksum for validation | `calculated_hash` |
| aggregatedMerchantId<br/><code>optional</code> | <code>String</code> Unique ID for aggregated merchants (For Aggregators Only) | `AGG123` |
| couponcode<br/><code>optional</code> | <code>String</code> Coupon code for cashback | `SAVE20` |

📘 **Important:** Ensure the token is valid and the user has sufficient balance before initiating the debit request.

## Checksum Generation

### For Aggregators
**Format:** `'amount''cell''comment''merchantname''mid''msgcode''orderid''token''txntype''aggregatedMerchantId'`

### For Direct Merchants  
**Format:** `'amount''cell''comment''merchantname''mid''msgcode''orderid''token''txntype'`

**Algorithm:** HMAC SHA256  
**Secret Key:** Provided by Mobikwik during merchant onboarding

📘 **Note:** For merchant `MBK9006`, the secret key is `ju6tygh7u7tdg554k098ujd5468o`. Each merchant will receive their unique secret key.

## Sample Request

```bash
GET https://test.mobikwik.com/debitwallet?mid=MBK9006&cell=9311032820&amount=150.50&orderid=ORDER_123456&token=MBK_TOKEN_123456789&merchantname=TestMerchant&msgcode=504&comment=Payment%20for%20order&txntype=DEBIT&checksum=calculated_hash_value
```

### With Coupon Code
```bash
GET https://test.mobikwik.com/debitwallet?mid=MBK9006&cell=9311032820&amount=150.50&orderid=ORDER_123456&token=MBK_TOKEN_123456789&merchantname=TestMerchant&msgcode=504&comment=Payment%20for%20order&txntype=DEBIT&couponcode=SAVE20&checksum=calculated_hash_value
```

## Response Parameters

| Field | Description | Example |
|-------|-------------|---------|
| messagecode | <code>String</code> Message code from request | `504` |
| status | <code>String</code> Transaction status | `SUCCESS` |
| statuscode | <code>String</code> Numeric status code | `0` |
| statusdescription | <code>String</code> Description of the status | `Transaction completed successfully` |
| orderid | <code>String</code> Order identifier from request | `ORDER_123456` |
| txnid | <code>String</code> Mobikwik transaction ID | `MBK_TXN_789012345` |
| amount | <code>String</code> Transaction amount | `150.50` |
| cashback | <code>String</code> Cashback amount applied | `5.00` |
| checksum | <code>String</code> Response checksum for validation | `8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47` |

### Response Attributes

The response checksum that will be returned to the users will have the following format:



📘 **Note:** Always validate the response checksum to ensure data integrity and security.

## Sample Responses
📘 **Notes:**
- Always validate the response checksum for security
- Use unique order IDs to prevent duplicate transactions
- Implement proper error handling and retry mechanisms
- Store transaction details for reconciliation purposes
- Consider using webhooks for real-time transaction status updates
### Success Response
```json
{
  "messagecode": "504",
  "status": "SUCCESS",
  "statuscode": "0",
  "statusdescription": "Transaction completed successfully",
  "orderid": "ORDER_123456",
  "txnid": "MBK_TXN_789012345",
  "amount": "150.50",
  "cashback": "5.00",
  "checksum": "8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47"
}
```
### Failure Scenarios 
- Insufficient Balance
```json
{
  "messagecode": "504",
  "status": "FAILURE",
  "statuscode": "301",
  "statusdescription": "Insufficient wallet balance",
  "orderid": "ORDER_123456",
  "checksum": "f25ac916fe4806591e16269fc912771456437b784fa144a77fa9842d154920cc"
}
```

- Invalid Token
```json
{
  "messagecode": "504",
  "status": "FAILURE",
  "statuscode": "302",
  "statusdescription": "Invalid or expired token",
  "orderid": "ORDER_123456",
  "checksum": "e35bc916fe4806591e16269fc912771456437b784fa144a77fa9842d154920dd"
}
```

## Status Codes

| Status | Status Code | Description |
|--------|-------------|-------------|
| SUCCESS | 0 | Transaction completed successfully |
| FAILURE | 301 | Insufficient wallet balance |
| FAILURE | 302 | Invalid or expired token |
| FAILURE | 303 | Transaction limit exceeded |
| FAILURE | 304 | Duplicate order ID |
| FAILURE | 305 | Wallet temporarily blocked |
| FAILURE | Various | Other validation errors |

## Coupon Integration

### Cashback Processing
- Include `couponcode` parameter for real-time cashback calculation
- Cashback amount is applied during transaction processing
- Final debit amount = Original amount - Cashback amount
- Response includes both original amount and cashback details

### Example with Coupon
```bash
# Request with 20% cashback coupon
amount=100.00&couponcode=SAVE20

# Response shows:
"amount": "100.00",
"cashback": "20.00",
"net_debit": "80.00"
```