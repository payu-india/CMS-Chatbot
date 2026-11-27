---
title: Pre-Auth UPI Intent - Merchant Hosted
deprecated: false
hidden: true
metadata:
  robots: index
---
In Merchant Hosted UPI Intent integration, PayU returns a mandate URI (`intentURIData`), allowing your native mobile app or web app to launch installed UPI apps directly.

***

## Step 1: Post UPI Intent Pre-Auth Request

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
| `txnid`         | String         | Unique merchant order ID (Max 25 characters).                                                                            | `UPI_SEAM_INT_1`     |
| `amount`        | Float / String | Amount to block (2 decimal places).                                                                                      | `1000.00`            |
| `productinfo`   | String         | Product description (Max 100 characters).                                                                                | `Electronics_Hold`   |
| `firstname`     | String         | Customer first name.                                                                                                     | `Ashish`             |
| `email`         | String         | Customer email address.                                                                                                  | `ashish@example.com` |
| `phone`         | String         | Customer mobile number.                                                                                                  | `9876543210`         |
| `surl`          | String         | Success callback URL.                                                                                                    | `<redacted URL>`     |
| `furl`          | String         | Failure callback URL.                                                                                                    | `<redacted URL>`     |
| `pg`            | String         | Must be set to `UPI`.                                                                                                    | `UPI`                |
| `bankcode`      | String         | Must be set to `INTENT`.                                                                                                 | `INTENT`             |
| `txn_s2s_flow`  | String         | Must be set to `4`.                                                                                                      | `4`                  |
| `pre_authorize` | String         | Must be set to `1`.                                                                                                      | `1`                  |
| `hash`          | String         | SHA-512 hash: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)`. | `8e8de8...`          |

#### Optional Parameters

| Parameter       | Type          | Description                                                                                | Example                                                           |
| :-------------- | :------------ | :----------------------------------------------------------------------------------------- | :---------------------------------------------------------------- |
| `siDetails`     | String (JSON) | Mandate validity range: `{"paymentStartDate":"YYYY-MM-DD","paymentEndDate":"YYYY-MM-DD"}`. | `{"paymentStartDate":"2026-11-20","paymentEndDate":"2026-12-20"}` |
| `udf1` - `udf5` | String        | Custom metadata fields.                                                                    | `Ref_Intent_01`                                                   |

### Sample Request

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JPM7Fg" \
  -d "pg=UPI" \
  -d "bankcode=INTENT" \
  -d "txn_s2s_flow=4" \
  -d "pre_authorize=1" \
  -d "txnid=UPI_SEAM_INT_1" \
  -d "amount=1000.00" \
  -d "productinfo=Electronics_Hold" \
  -d "firstname=Ashish" \
  -d "email=ashish@example.com" \
  -d "phone=9876543210" \
  -d "siDetails={\"paymentStartDate\":\"2026-11-20\",\"paymentEndDate\":\"2026-12-20\"}" \
  -d "surl=<redacted URL>" \
  -d "furl=<redacted URL>" \
  -d "hash=CALCULATED_HASH"
```

***

## Step 2: Parse `intentURIData` and Trigger App Switch

PayU returns a JSON response containing `intentURIData`:

```json
{
  "metaData": {
    "referenceId": "test123",
    "txnId": "UPI_SEAM_INT_1",
    "txnStatus": "pending",
    "unmappedStatus": "pending"
  },
  "result": {
    "paymentId": "99999999",
    "amount": "1000.00",
    "intentURIData": "upi://mandate?pa=abc@upi&pn=Merchant&mn=ONETIME&tid=test123&validitystart=20112026&validityend=20122026&am=1000.00&amrule=MAX&recur=ONETIME&tr=UPI_SEAM_INT_1&cu=INR&mode=13&block=Y&txnType=CREATE"
  }
}
```

Open the `intentURIData` URI in your mobile application to invoke the customer's UPI app. Upon PIN entry, PayU sends the confirmation callback to your `surl` and webhook.

***

## Step 3 & 4: Capture or Cancel

Execute fund capture or mandate cancellation via `postservice.php`.