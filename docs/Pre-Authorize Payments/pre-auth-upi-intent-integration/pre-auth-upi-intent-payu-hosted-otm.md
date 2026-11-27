---
title: Pre-Auth PayU Hosted UPI Intent OTM
deprecated: false
hidden: true
metadata:
  robots: index
---
With **UPI Intent One-Time Mandates (OTM)** on PayU Hosted Checkout, customers select UPI on the PayU payment page and switch directly to their installed UPI app (Google Pay, PhonePe, Paytm, BHIM) to approve an authorization hold using their UPI PIN.

***

## Step 1: Post Pre-Auth Request to `_payment`

### Environment

| Environment        | URL                                                                                                   |
| :----------------- | :---------------------------------------------------------------------------------------------------- |
| **Test (Sandbox)** | [https://test.payu.in/\_payment](https://test.payu.in/_payment)                                       |
| **Production**     | [https://secure.payu.in/\_payment](https://secure.payu.in/_payment "https://secure.payu.in/_payment") |

### Request Parameters

#### Mandatory Parameters

| Parameter       | Type           | Description                                                                                                              | Example              |
| :-------------- | :------------- | :----------------------------------------------------------------------------------------------------------------------- | :------------------- |
| `key`           | String         | Merchant Key provided by PayU.                                                                                           | `JPM7Fg`             |
| `txnid`         | String         | Unique merchant order ID (Max 25 characters).                                                                            | `UPI_INT_001`        |
| `amount`        | Float / String | Amount to block (2 decimal places).                                                                                      | `1000.00`            |
| `productinfo`   | String         | Product description (Max 100 characters).                                                                                | `Pre_Order_Phone`    |
| `firstname`     | String         | Customer first name.                                                                                                     | `Ashish`             |
| `email`         | String         | Customer email address.                                                                                                  | `ashish@example.com` |
| `phone`         | String         | Customer mobile number.                                                                                                  | `9876543210`         |
| `surl`          | String         | Success callback URL.                                                                                                    | `<redacted URL>`     |
| `furl`          | String         | Failure callback URL.                                                                                                    | `<redacted URL>`     |
| `pg`            | String         | Must be set to `UPI`.                                                                                                    | `UPI`                |
| `bankcode`      | String         | Set to `INTENT` for UPI Intent.                                                                                          | `INTENT`             |
| `pre_authorize` | String         | Must be set to `1`.                                                                                                      | `1`                  |
| `hash`          | String         | SHA-512 hash: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)`. | `8e8de8...`          |

#### Optional Parameters

| Parameter       | Type          | Description                                                                                | Example                                                           |
| :-------------- | :------------ | :----------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| `siDetails`     | String (JSON) | Mandate validity range: `{"paymentStartDate":"YYYY-MM-DD","paymentEndDate":"YYYY-MM-DD"}`. | `{"paymentStartDate":"2026-11-20","paymentEndDate":"2026-12-20"}` |
| `udf1` - `udf5` | String        | Custom metadata fields.                                                                    | `Batch_1`                                                         |

### Sample Request

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg" \
  -d "txnid=UPI_INT_001" \
  -d "amount=1000.00" \
  -d "productinfo=Pre_Order_Phone" \
  -d "firstname=Ashish" \
  -d "email=ashish@example.com" \
  -d "phone=9876543210" \
  -d "pg=UPI" \
  -d "bankcode=INTENT" \
  -d "pre_authorize=1" \
  -d "siDetails={\"paymentStartDate\":\"2026-11-20\",\"paymentEndDate\":\"2026-12-20\"}" \
  -d "surl=<redacted URL>" \
  -d "furl=<redacted URL>" \
  -d "hash=CALCULATED_REQUEST_HASH"
```

***

## Step 2: Handle Response & Verification

* Customer authorizes the hold in their UPI app using their UPI PIN.
* PayU posts the callback to `surl`. Verify that `status == "success"` and `unmappedstatus == "auth"`.
* Store `mihpayid` for subsequent capture.

***

## Step 3 & 4: Capture or Cancel

* To settle funds, call `capture_transaction` via `postservice.php`.
* To cancel the mandate hold, call `cancel_transaction`.