---
title: Pre-Auth UPI Reserve Pay Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
**UPI Reserve Pay** allows merchants to securely reserve funds in a customer's bank account for up to **90 days**. The customer authorizes the block once using their UPI PIN, and the merchant can execute **multiple partial debits** until the reserved sum is exhausted.

***

## Key Differences: Cards vs. UPI Reserve Pay

| Capability                  | Card Pre-Authorization                                | UPI Reserve Pay                                             |
| :-------------------------- | :---------------------------------------------------- | :---------------------------------------------------------- |
| **Maximum Hold Time**       | 7 Days                                                | **Up to 90 Days**                                           |
| **Debit Flexibility**       | Single partial capture only (remainder auto-released) | **Multiple partial debits** supported against the same hold |
| **Customer Authentication** | 3DS OTP per authorization                             | Customer enters UPI PIN once during block creation          |
| **Hold Expiration**         | Auto-captured on Day 7 (or auto-cancelled by config)  | Automatically released upon mandate end date                |

***

## Use Cases

* **E-Commerce & Pre-Orders**: Block ₹10,000 during product reservations. As items ship in split consignments (e.g. ₹4,000, then ₹5,200), execute multiple debits. Release any remaining balance upon final shipment.
* **Tourism & Long-Stay Bookings**: Reserve ₹25,000 during booking; debit installments as itinerary milestones are confirmed.
* **Healthcare & Extended Treatments**: Block estimated treatment charges; debit itemized daily or department bills against the block.

***

## Step 1: Initiate UPI Reserve Pay Mandate

UPI Reserve Pay uses the standard UPI One-Time Mandate request parameters with an extended `siDetails` validity window (up to 90 days).

### Endpoints

| Environment    | URL              |
| :------------- | :--------------- |
| **Test**       | `<redacted URL>` |
| **Production** | `<redacted URL>` |

### Request Parameters

#### Mandatory Parameters

| Parameter       | Type           | Description                                                                                                              | Example                   |
| :-------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------- | :------------------------ |
| `key`           | String         | Merchant Key provided by PayU.                                                                                           | `JPM7Fg`                  |
| `txnid`         | String         | Unique merchant transaction ID (Max 25 characters).                                                                      | `RES_PAY_90D_01`          |
| `amount`        | Float / String | Total amount to reserve (2 decimal places).                                                                              | `10000.00`                |
| `productinfo`   | String         | Product description (Max 100 characters).                                                                                | `PreOrder_Flagship_Phone` |
| `firstname`     | String         | Customer first name.                                                                                                     | `Ashish`                  |
| `email`         | String         | Customer email address.                                                                                                  | `ashish@example.com`      |
| `phone`         | String         | Customer mobile number.                                                                                                  | `9876543210`              |
| `surl`          | String         | Success callback URL.                                                                                                    | `<redacted URL>`          |
| `furl`          | String         | Failure callback URL.                                                                                                    | `<redacted URL>`          |
| `pg`            | String         | Must be set to `UPI`.                                                                                                    | `UPI`                     |
| `bankcode`      | String         | Set to `INTENT` (App Switch) or `UPI` (VPA Collect).                                                                     | `INTENT`                  |
| `pre_authorize` | String         | Must be set to `1`.                                                                                                      | `1`                       |
| `hash`          | String         | SHA-512 hash: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)`. | `8e8de8...`               |

#### Optional Parameters

| Parameter       | Type          | Description                                                                                                | Example                                                           |
| :-------------- | :------------ | :--------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| `siDetails`     | String (JSON) | Mandate validity range (up to 90 days): `{"paymentStartDate":"YYYY-MM-DD","paymentEndDate":"YYYY-MM-DD"}`. | `{"paymentStartDate":"2026-11-20","paymentEndDate":"2027-02-18"}` |
| `vpa`           | String        | Customer VPA handle (required when `bankcode="UPI"`).                                                      | `customer@okaxis`                                                 |
| `udf1` - `udf5` | String        | Custom metadata fields.                                                                                    | `PreOrder_Batch_A`                                                |

***

## Step 2: Customer Authorization

Customer approves the block mandate in their UPI app with their UPI PIN. PayU posts confirmation to `surl`. Store `mihpayid`.

***

## Step 3: Executing Multiple Partial Debits

To debit from the reserved amount, invoke `capture_transaction` with the specific debit amount in `var3`. You can repeat this call for subsequent debits until the cumulative total reaches the original reserved amount.

```bash
curl -X POST "<redacted URL>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg" \
  -d "command=capture_transaction" \
  -d "var1=403993715523409521" \
  -d "var2=DEBIT_INSTALLMENT_01" \
  -d "var3=4000.00" \
  -d "hash=CALCULATED_CAPTURE_HASH"
```
