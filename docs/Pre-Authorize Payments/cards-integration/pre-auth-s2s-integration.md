---
title: Pre-Auth S2S Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
In the Server-to-Server (S2S) Decoupled Pre-Authorization flow, your backend interacts directly with PayU's `_payment` API. PayU returns the bank Access Control Server (ACS) HTML template, enabling you to embed or render the bank's 3DS challenge within your own application.

***

## Step 1: Post S2S Pre-Auth Request to `_payment`

### Environment

| Environment        | URL                                                                                                   |
| :----------------- | :---------------------------------------------------------------------------------------------------- |
| **Test (Sandbox)** | [https://test.payu.in/\_payment](https://test.payu.in/_payment)                                       |
| **Production**     | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment "https://secure.payu.in/_payment") |

### Request Parameters

#### Mandatory Parameters

| Parameter         | Type           | Description                                                                                                              | Example              |
| :---------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------- | :------------------- |
| `key`             | String         | Merchant Key.                                                                                                            | `JPM7Fg`             |
| `txnid`           | String         | Merchant Transaction ID (Max 25 characters).                                                                             | `S2S_ORD_1001`       |
| `amount`          | Float / String | Amount to pre-authorize (2 decimal places).                                                                              | `1000.00`            |
| `productinfo`     | String         | Product description.                                                                                                     | `Flight_Reservation` |
| `firstname`       | String         | Customer first name.                                                                                                     | `Ashish`             |
| `email`           | String         | Customer email address.                                                                                                  | `ashish@example.com` |
| `phone`           | String         | Customer mobile number.                                                                                                  | `9876543210`         |
| `pg`              | String         | Payment category (`CC` or `DC`).                                                                                         | `CC`                 |
| `bankcode`        | String         | Scheme/bank code (`CC`, `VISA`, `MAST`, etc.).                                                                           | `CC`                 |
| `ccnum`           | String         | 13–19 digit card number.                                                                                                 | `4012888888881881`   |
| `ccname`          | String         | Cardholder name.                                                                                                         | `Ashish Kumar`       |
| `ccexpmon`        | String         | Card expiry month (`01`–`12`).                                                                                           | `11`                 |
| `ccexpyr`         | String         | Card expiry year (`YYYY`).                                                                                               | `2027`               |
| `ccvv`            | String         | 3-digit CVV or 4-digit CID.                                                                                              | `123`                |
| `surl`            | String         | Success URL.                                                                                                             | `<redacted URL>`     |
| `furl`            | String         | Failure URL.                                                                                                             | `<redacted URL>`     |
| `pre_authorize`   | String         | Must be set to `1`.                                                                                                      | `1`                  |
| `txn_s2s_flow`    | String         | Must be set to `4` for decoupled flow.                                                                                   | `4`                  |
| `auth_only`       | String         | Must be set to `2` for authentication-only decoupled flow.                                                               | `2`                  |
| `termUrl`         | String         | Merchant endpoint configured to receive 3DS response from bank ACS.                                                      | `<redacted URL>`     |
| `s2s_client_ip`   | String         | Customer's client IP address.                                                                                            | `203.0.113.195`      |
| `s2s_device_info` | String         | Customer's browser user-agent string.                                                                                    | `Mozilla/5.0...`     |
| `hash`            | String         | SHA-512 hash: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)`. | `d99f23...`          |

#### Optional Parameters

| Parameter       | Type   | Description                                | Example              |
| :-------------- | :----- | :----------------------------------------- | :------------------- |
| `notifyurl`     | String | Webhook endpoint for server notifications. | `<redacted URL>`     |
| `address1`      | String | Customer billing address line 1.           | `Plot 23, Sector 18` |
| `address2`      | String | Customer billing address line 2.           | `Udyog Vihar`        |
| `city`          | String | Billing city.                              | `Gurugram`           |
| `state`         | String | Billing state.                             | `Haryana`            |
| `country`       | String | Billing country.                           | `India`              |
| `zipcode`       | String | Billing postal code.                       | `122015`             |
| `udf1` - `udf5` | String | Custom metadata strings.                   | `Flight_SG123`       |

### Sample S2S Request

```bash
curl -X POST "<redacted URL>" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg" \
  -d "txnid=S2S_ORD_1001" \
  -d "amount=1000.00" \
  -d "productinfo=Flight_Reservation" \
  -d "firstname=Ashish" \
  -d "email=ashish@example.com" \
  -d "phone=9876543210" \
  -d "pg=CC" \
  -d "bankcode=CC" \
  -d "ccnum=4012888888881881" \
  -d "ccname=Ashish Kumar" \
  -d "ccexpmon=11" \
  -d "ccexpyr=2027" \
  -d "ccvv=123" \
  -d "pre_authorize=1" \
  -d "txn_s2s_flow=4" \
  -d "auth_only=2" \
  -d "termUrl=<redacted URL>" \
  -d "s2s_client_ip=203.0.113.195" \
  -d "s2s_device_info=Mozilla/5.0" \
  -d "surl=<redacted URL>" \
  -d "furl=<redacted URL>" \
  -d "hash=CALCULATED_HASH"
```

***

## Step 2: Handle ACS Challenge & Verify Response

### Decode ACS Template

The API response returns a JSON payload containing base64-encoded `acsTemplate`:

```json
{
  "metaData": {
    "referenceId": "00c44a4c8306f9cbe5ecf6133afe08a7",
    "txnId": "S2S_ORD_1001",
    "txnStatus": "Enrolled",
    "unmappedStatus": "pending"
  },
  "result": {
    "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0Ii...",
    "otpPostUrl": ""
  }
}
```

Decode the `acsTemplate` string and render it in the customer's browser. The customer enters the bank OTP, and the ACS posts the result back to your `termUrl`.

### Callback Verification

Once authentication completes, verify that:

* `status == "success"`
* `unmappedstatus == "auth"`
* Store `mihpayid` for settlement.

***

## Step 3 & 4: Capture or Cancel

Execute fund capture using `capture_transaction` or cancel hold using `cancel_transaction` at `<redacted URL>`.