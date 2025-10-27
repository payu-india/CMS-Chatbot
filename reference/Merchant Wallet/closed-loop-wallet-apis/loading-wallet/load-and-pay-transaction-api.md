---
title: Load and Pay Transaction API
deprecated: false
hidden: true
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

## Request Headers

| Parameter                                | Description                                           |
| ---------------------------------------- | ----------------------------------------------------- |
| Content-Type<br /><code>mandatory</code> | <code>String</code> application/x-www-form-urlencoded |

## Request Parameters

<HTMLBlock>{`
<table>
    <thead>
        <tr>
            <th>Parameter</th>
            <th>Description</th>
            <th>Example</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>key<br><code>mandatory</code></td>
            <td><code>String</code> Merchant key provided by PayU during onboarding</td>
            <td>KOEfPI</td>
        </tr>
        <tr>
            <td>txnid<br><code>mandatory</code></td>
            <td><code>Alphanumeric</code> Unique transaction ID generated for each load and pay transaction</td>
            <td>ram1234</td>
        </tr>
        <tr>
            <td>amount<br><code>mandatory</code></td>
            <td><code>Numeric</code> Transaction amount in implied decimals (₹41.00 → 4100)</td>
            <td>4100</td>
        </tr>
        <tr>
            <td>productinfo<br><code>mandatory</code></td>
            <td><code>String</code> Description and details about the product being purchased</td>
            <td>eCommerce</td>
        </tr>
        <tr>
            <td>firstname<br><code>mandatory</code></td>
            <td><code>String</code> Customer's first name</td>
            <td>John</td>
        </tr>
        <tr>
            <td>lastname<br><code>optional</code></td>
            <td><code>String</code> Customer's last name</td>
            <td>Doe</td>
        </tr>
        <tr>
            <td>email<br><code>mandatory</code></td>
            <td><code>String</code> Email ID associated with the customer wallet/account</td>
            <td><a href="mailto:john.doe@gmail.com">john.doe@gmail.com</a></td>
        </tr>
        <tr>
            <td>phone<br><code>mandatory</code></td>
            <td><code>Numeric</code> Customer's phone number with country code</td>
            <td>919988776655</td>
        </tr>
        <tr>
            <td>surl<br><code>mandatory</code></td>
            <td><code>String</code> Success URL where customer will be redirected upon successful transaction</td>
            <td><a href="https://merchant.com/success">https://merchant.com/success</a></td>
        </tr>
        <tr>
            <td>furl<br><code>mandatory</code></td>
            <td><code>String</code> Failure URL where customer will be redirected upon failed transaction</td>
            <td><a href="https://merchant.com/failure">https://merchant.com/failure</a></td>
        </tr>
        <tr>
            <td>pg<br><code>mandatory</code></td>
            <td><code>String</code> Constant parameter indicating the payment gateway (CLW)</td>
            <td>CLW</td>
        </tr>
        <tr>
            <td>bankcode<br><code>mandatory</code></td>
            <td><code>String</code> Bank code indicating the payment option used for the transaction</td>
            <td>PAY</td>
        </tr>
        <tr>
            <td>customer_id<br><code>conditional</code></td>
            <td><code>Numeric</code> Unique wallet/customer ID for wallet integration</td>
            <td>70000000008</td>
        </tr>
        <tr>
            <td>walleturn<br><code>conditional</code></td>
            <td><code>Numeric</code> URN (Unique Reference Number) for wallet transactions</td>
            <td>123456789</td>
        </tr>
        <tr>
            <td>loadmoney<br><code>mandatory</code></td>
            <td><code>Numeric</code> Amount to be loaded into the wallet if existing balance is insufficient</td>
            <td>1000</td>
        </tr>
        <tr>
            <td>txn_s2s_flow<br><code>mandatory</code></td>
            <td><code>Numeric</code> Identifies the merchant-hosted transaction flow (constant value 4)</td>
            <td>4</td>
        </tr>
        <tr>
            <td>hash<br><code>mandatory</code></td>
            <td><code>String</code> SHA512 hash for securing the API request. For more information, refer to <a href="#hash-calcuation">Hash Calculation</a></td>
            <td>84bbbf...f5c9</td>
        </tr>
    </tbody>
</table>
`}</HTMLBlock>

<br />

> <Callout icon="📘" theme="info">
>   **Note**: Either `customer_id` or `walleturn` must be provided to identify the wallet.
> </Callout>

### Hash calculation

The hash is calculated using SHA512 with the following string:

```
key|txnid|amount|productinfo|firstname|email|||||||||||||{salt}
```

## Sample request

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

## Response Parameters

| Parameter        | Description                                          | Example                                         |
| ---------------- | ---------------------------------------------------- | ----------------------------------------------- |
| mihpayid         | Unique PayU-generated transaction reference number   | 1735903830180094                                |
| status           | Transaction final status (success, failure, pending) | success                                         |
| key              | Merchant key (echoed back)                           | KOEfPI                                          |
| txnid            | Transaction ID (echoed back)                         | ram1234                                         |
| amount           | Transaction amount debited from the wallet           | 41.00                                           |
| addedon          | Time and date when the transaction was completed     | 2025-01-13 18:24:06                             |
| net_amount_debit | Final successfully paid amount after processing fees | 40.00                                           |
| hash             | Response hash generated by PayU for verification     | 6e640b16...2b2a                                 |
| bank_ref_num     | Unique reference number generated by the bank        | 1099                                            |
| PG_TYPE          | Payment gateway used for the transaction             | CLW-PG                                          |
| error            | Error code if the transaction fails                  | E000                                            |
| error_message    | Detailed error description                           | No Error                                        |
| firstname        | Customer's first name                                | John                                            |
| lastname         | Customer's last name                                 | Doe                                             |
| email            | Customer's email                                     | [john.doe@gmail.com](mailto:john.doe@gmail.com) |
| phone            | Customer's phone number                              | 919988776655                                    |

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