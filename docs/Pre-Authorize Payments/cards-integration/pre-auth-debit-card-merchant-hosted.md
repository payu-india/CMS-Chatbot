---
title: Pre-Auth Debit Card - Merchant Hosted
deprecated: false
hidden: true
metadata:
  robots: index
---
Debit Card Pre-Authorization enables temporary holds on customer bank account funds.

## Supported Debit Card Issuers

* HDFC Bank
* ICICI Bank
* State Bank of India
* Axis Bank
* Kotak Mahindra Bank

***

## Step 1: Post Debit Card Pre-Auth Request to `_payment`

### Endpoints

| Environment    | URL                                                                                             |
| :------------- | :---------------------------------------------------------------------------------------------- |
| **Test**       | [https://test.payu.in/\_payment](https://test.payu.in/_payment "https://test.payu.in/_payment") |
| **Production** | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment)                             |

### Request Parameters

#### Mandatory Parameters

| Parameter       | Type           | Description                                                                                                                         | Example              |
| :-------------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------- | :------------------- |
| `key`           | String         | Merchant Key provided by PayU.                                                                                                      | `JPM7Fg`             |
| `txnid`         | String         | Unique merchant transaction ID (Max 25 characters).                                                                                 | `DC_HOLD_0098`       |
| `amount`        | Float / String | Amount to block (format with 2 decimal places).                                                                                     | `1000.00`            |
| `productinfo`   | String         | Brief product description (Max 100 characters).                                                                                     | `Security_Deposit`   |
| `firstname`     | String         | Customer first name.                                                                                                                | `Ashish`             |
| `email`         | String         | Customer email address.                                                                                                             | `ashish@example.com` |
| `phone`         | String         | Customer mobile number.                                                                                                             | `9876543210`         |
| `surl`          | String         | Success callback URL.                                                                                                               | `<redacted URL>`     |
| `furl`          | String         | Failure callback URL.                                                                                                               | `<redacted URL>`     |
| `pg`            | String         | Payment category. Must be set to `DC`.                                                                                              | `DC`                 |
| `bankcode`      | String         | Card network/bank code: `VISA`, `MAST`, or supported issuer code.                                                                   | `VISA`               |
| `ccnum`         | String         | 16-digit debit card number. Validate with LUHN algorithm.                                                                           | `4506448888881881`   |
| `ccname`        | String         | Cardholder name.                                                                                                                    | `Ashish Kumar`       |
| `ccexpmon`      | String         | 2-digit expiry month (`01` to `12`).                                                                                                | `05`                 |
| `ccexpyr`       | String         | 4-digit expiry year (`YYYY`).                                                                                                       | `2028`               |
| `ccvv`          | String         | 3-digit CVV.                                                                                                                        | `123`                |
| `pre_authorize` | String         | Must be set to `1`.                                                                                                                 | `1`                  |
| `hash`          | String         | Calculated SHA-512 hash: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)`. | `d99f23...`          |

#### Optional Parameters

| Parameter       | Type   | Description                      | Example                 |
| :-------------- | :----- | :------------------------------- | :---------------------- |
| `address1`      | String | Customer billing address line 1. | `Flat 12B, Green Woods` |
| `address2`      | String | Customer billing address line 2. | `Indiranagar`           |
| `city`          | String | Billing city.                    | `Bengaluru`             |
| `state`         | String | Billing state.                   | `Karnataka`             |
| `country`       | String | Billing country.                 | `India`                 |
| `zipcode`       | String | Postal code.                     | `560038`                |
| `udf1` - `udf5` | String | Custom metadata strings.         | `Booking_Ref_01`        |

### Sample Request

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg" \
  -d "pg=DC" \
  -d "bankcode=VISA" \
  -d "pre_authorize=1" \
  -d "txnid=DC_HOLD_0098" \
  -d "amount=1000.00" \
  -d "productinfo=Security_Deposit" \
  -d "firstname=Ashish" \
  -d "email=ashish@example.com" \
  -d "phone=9876543210" \
  -d "ccnum=4506448888881881" \
  -d "ccname=Ashish Kumar" \
  -d "ccexpmon=05" \
  -d "ccexpyr=2028" \
  -d "ccvv=123" \
  -d "surl=<redacted URL>" \
  -d "furl=<redacted URL>" \
  -d "hash=CALCULATED_REQUEST_HASH"
```

***

## Step 2: Handle Response & Verification

Verify the reverse hash at `surl`:

```text
sha512(SALT|status|udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

Ensure `status == "success"` and `unmappedstatus == "auth"`.

***

## Step 3 & 4: Capture or Cancel

Use `capture_transaction` to settle held funds or `cancel_transaction` to release the debit card hold.