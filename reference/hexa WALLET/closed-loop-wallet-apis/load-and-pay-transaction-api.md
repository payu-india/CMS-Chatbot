---
title: Load and Pay Transaction API
deprecated: false
hidden: false
metadata:
  robots: index
---
The Load and Pay Transaction API is designed to handle wallet transactions where the wallet balance is insufficient. It enables users to first load money into their wallet and then directly proceed with the payment (debiting the wallet) in a single streamlined transaction.

## Environment

| Environment | URL                               |
| ----------- | --------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

**HTTP Method**: POST

## Authentication

This API uses hash-based authentication. The hash is calculated using SHA512 algorithm with specific parameters.

## How It Works

1. **Wallet Balance Check**: The API checks the current wallet balance
2. **Load Money**: If the wallet has insufficient funds, it initiates the load process via payment gateway
3. **Debit Transaction**: Once sufficient funds are loaded, the API performs the debit transaction
4. **Single Flow**: Both loading and payment happen in a single unified API call

## Request Headers

| Parameter                                | Description                                           |
| ---------------------------------------- | ----------------------------------------------------- |
| Content-Type<br /><code>mandatory</code> | <code>String</code> application/x-www-form-urlencoded |

## Request Parameters

### Body Parameters

| Parameter                                  | Description                                                                                                                       | Example                                                      |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| key<br /><code>mandatory</code>            | <code>String</code> Merchant key provided by PayU during onboarding                                                               | KOEfPI                                                       |
| txnid<br /><code>mandatory</code>          | <code>Alphanumeric</code> Unique transaction ID generated for each load and pay transaction                                       | ram1234                                                      |
| amount<br /><code>mandatory</code>         | <code>Numeric</code> Transaction amount in implied decimals (₹41.00 → 4100)                                                       | 4100                                                         |
| productinfo<br /><code>mandatory</code>    | <code>String</code> Description and details about the product being purchased                                                     | eCommerce                                                    |
| firstname<br /><code>mandatory</code>      | <code>String</code> Customer's first name                                                                                         | John                                                         |
| lastname<br /><code>optional</code>        | <code>String</code> Customer's last name                                                                                          | Doe                                                          |
| email<br /><code>mandatory</code>          | <code>String</code> Email ID associated with the customer wallet/account                                                          | [john.doe@gmail.com](mailto:john.doe@gmail.com)              |
| phone<br /><code>mandatory</code>          | <code>Numeric</code> Customer's phone number with country code                                                                    | 919988776655                                                 |
| surl<br /><code>mandatory</code>           | <code>String</code> Success URL where customer will be redirected upon successful transaction                                     | [https://merchant.com/success](https://merchant.com/success) |
| furl<br /><code>mandatory</code>           | <code>String</code> Failure URL where customer will be redirected upon failed transaction                                         | [https://merchant.com/failure](https://merchant.com/failure) |
| pg<br /><code>mandatory</code>             | <code>String</code> Constant parameter indicating the payment gateway (CLW)                                                       | CLW                                                          |
| bankcode<br /><code>mandatory</code>       | <code>String</code> Bank code indicating the payment option used for the transaction                                              | PAY                                                          |
| customer\_id<br /><code>conditional</code> | <code>Numeric</code> Unique wallet/customer ID for wallet integration                                                             | 70000000008                                                  |
| walleturn<br /><code>conditional</code>    | <code>Numeric</code> URN (Unique Reference Number) for wallet transactions                                                        | 123456789                                                    |
| loadmoney<br /><code>mandatory</code>      | <code>Numeric</code> Amount to be loaded into the wallet if existing balance is insufficient                                      | 1000                                                         |
| txn\_s2s\_flow<br /><code>mandatory</code> | <code>Numeric</code> Identifies the merchant-hosted transaction flow (constant value 4)                                           | 4                                                            |
| hash<br /><code>mandatory</code>           | <code>String</code> SHA512 hash for securing the API request. For more information, refer to [Hash Calculation](#hash-calcuation) | 84bbbf...f5c9                                                |

> Note: Either `customer_id` or `walleturn` must be provided to identify the wallet.

### Hash calculation

The hash is calculated using SHA512 with the following string:

```
key|txnid|amount|productinfo|firstname|email|||||||||||||{salt}
```

## Response Parameters

| Parameter          | Description                                          | Example                                         |
| ------------------ | ---------------------------------------------------- | ----------------------------------------------- |
| mihpayid           | Unique PayU-generated transaction reference number   | 1735903830180094                                |
| status             | Transaction final status (success, failure, pending) | success                                         |
| key                | Merchant key (echoed back)                           | KOEfPI                                          |
| txnid              | Transaction ID (echoed back)                         | ram1234                                         |
| amount             | Transaction amount debited from the wallet           | 41.00                                           |
| addedon            | Time and date when the transaction was completed     | 2025-01-13 18:24:06                             |
| net\_amount\_debit | Final successfully paid amount after processing fees | 40.00                                           |
| hash               | Response hash generated by PayU for verification     | 6e640b16...2b2a                                 |
| bank\_ref\_num     | Unique reference number generated by the bank        | 1099                                            |
| PG\_TYPE           | Payment gateway used for the transaction             | CLW-PG                                          |
| error              | Error code if the transaction fails                  | E000                                            |
| error\_message     | Detailed error description                           | No Error                                        |
| firstname          | Customer's first name                                | John                                            |
| lastname           | Customer's last name                                 | Doe                                             |
| email              | Customer's email                                     | [john.doe@gmail.com](mailto:john.doe@gmail.com) |
| phone              | Customer's phone number                              | 919988776655                                    |

## Sample Request

```bash
curl --location --request POST 'https://test.payu.in/_payment' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'key=KOEfPI' \
--data-urlencode 'txnid=ram1234' \
--data-urlencode 'amount=41.00' \
--data-urlencode 'productinfo=eCommerce' \
--data-urlencode 'firstname=John' \
--data-urlencode 'lastname=Doe' \
--data-urlencode 'email=john.doe@gmail.com' \
--data-urlencode 'phone=919988776655' \
--data-urlencode 'surl=https://merchant.com/success' \
--data-urlencode 'furl=https://merchant.com/failure' \
--data-urlencode 'pg=CLW' \
--data-urlencode 'bankcode=PAY' \
--data-urlencode 'walleturn=123456789' \
--data-urlencode 'loadmoney=1000' \
--data-urlencode 'txn_s2s_flow=4' \
--data-urlencode 'hash=84bbbf...f5c9'
```

## Sample Response

### Successful Transaction

```json
{
  "mihpayid": "1735903830180094",
  "status": "success",
  "key": "KOEfPI",
  "txnid": "ram1234",
  "amount": "41.00",
  "addedon": "2025-01-13 18:24:06",
  "net_amount_debit": "40.00",
  "hash": "6e640b16...2b2a",
  "bank_ref_num": "1099",
  "PG_TYPE": "CLW-PG",
  "error": "E000",
  "error_message": "No Error",
  "firstname": "John",
  "lastname": "Doe",
  "email": "john.doe@gmail.com",
  "phone": "919988776655"
}
```

### Failed Transaction

```json
{
  "mihpayid": "1735903830180095",
  "status": "failure",
  "key": "KOEfPI",
  "txnid": "ram1235",
  "amount": "41.00",
  "error": "E001",
  "error_message": "Payment gateway error",
  "hash": "xyz789abc123..."
}
```

## HTTP Status Codes

| Status Code | Description                              |
| ----------- | ---------------------------------------- |
| 200         | OK - Request processed successfully      |
| 400         | Bad Request - Invalid request parameters |
| 401         | Unauthorized - Authentication failed     |
| 500         | Internal Server Error                    |

## Error Scenarios

| Error                      | Description                         | Solution                            |
| -------------------------- | ----------------------------------- | ----------------------------------- |
| Payment gateway failure    | PG load transaction failed          | Retry with different payment method |
| Insufficient load amount   | `loadmoney` less than required      | Increase load amount                |
| Invalid wallet             | Customer ID or wallet URN not found | Verify wallet details               |
| Transaction limit exceeded | Amount exceeds allowed limits       | Check transaction limits            |
| Hash mismatch              | Invalid hash in request             | Verify hash calculation             |