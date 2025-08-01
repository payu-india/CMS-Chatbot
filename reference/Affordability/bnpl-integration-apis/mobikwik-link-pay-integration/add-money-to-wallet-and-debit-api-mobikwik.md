---
title: Add Money to Wallet And Debit API - Mobikwik
deprecated: false
hidden: true
metadata:
  robots: index
---
This API allows merchants to add insufficient funds to a user's wallet and debit the total transaction amount in a single seamless operation.

## Environment

| Environment | URL |
|-------------|-----|
| **Test** | `https://test.mobikwik.com/walletapis/addmoneytowalletanddebit` |
| **Production** | `https://walletapi.mobikwik.com/walletapis/addmoneytowalletanddebit` |


**Method:** `POST`  

## Request parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| mid<br/><code>mandatory</code> | <code>String</code> Unique parent merchant ID | `MBK9006` |
| cell<br/><code>mandatory</code> | <code>String</code> Mobile number of the user | `9311032820` |
| amount<br/><code>mandatory</code> | <code>Decimal</code> Total transaction amount | `250.00` |
| orderid<br/><code>mandatory</code> | <code>String</code> Unique order identifier | `ORDER_123456` |
| token<br/><code>mandatory</code> | <code>String</code> Valid wallet token for the user | `MBK_TOKEN_123456789` |
| merchantname<br/><code>mandatory</code> | <code>String</code> Alias for the merchant | `TestMerchant` |
| redirecturl<br/><code>mandatory</code> | <code>String</code> URL for transaction completion notifications | `https://merchant.com/callback` |
| checksum<br/><code>mandatory</code> | <code>String</code> Calculated checksum for validation | `calculated_hash` |
| aggregatedMerchantId<br/><code>optional</code> | <code>String</code> Unique ID for aggregated merchants (For Aggregators Only) | `AGG123` |

## Response parameters

| Field | Description | Example |
|-------|-------------|---------|
| messagecode | <code>String</code> Message code from request | `504` |
| status | <code>String</code> Transaction status | `SUCCESS` |
| statuscode | <code>String</code> Numeric status code | `0` |
| statusdescription | <code>String</code> Description of the status | `Add money flow initiated successfully` |
| orderid | <code>String</code> Order identifier from request | `ORDER_123456` |
| txnid | <code>String</code> Mobikwik transaction ID | `MBK_TXN_789012345` |
| amount | <code>String</code> Transaction amount | `250.00` |
| wallet_balance | <code>String</code> Current wallet balance | `100.00` |
| added_amount | <code>String</code> Amount to be added to wallet | `150.00` |
| redirect_url | <code>String</code> URL for payment processing | `https://mobikwik.com/payment/process?token=xyz123` |
| checksum | <code>String</code> Response checksum for validation | `8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47` |

### Response attributes

The response checksum that will be returned to the users will have the following format:

📘 **Note:** Always validate the response checksum to ensure data integrity and security.

## Sample response

```json
{
  "messagecode": "504",
  "status": "SUCCESS",
  "statuscode": "0",
  "statusdescription": "Add money flow initiated successfully",
  "orderid": "ORDER_123456",
  "txnid": "MBK_TXN_789012345",
  "amount": "250.00",
  "wallet_balance": "100.00",
  "added_amount": "150.00",
  "redirect_url": "https://mobikwik.com/payment/process?token=xyz123",
  "checksum": "8feac7700a4efd1ef08ea0ec5bf5921c3f1fc3398944421978794b9ada1c2c47"
}
```