---
title: Dynamic Currency Conversion (DCC) Quick Start Guide
deprecated: false
hidden: true
metadata:
  robots: index
---
> **What is Dynamic Currency Conversion (DCC)?**
> DCC allows international cardholders to pay in their **home currency** at your checkout. PayU detects the card's issuing currency, presents both the merchant currency (INR) and the cardholder's currency with a live exchange rate, and lets the customer choose which to pay in. Your settlement to PayU remains in INR — the customer gets transparent pricing in a familiar currency.
>
> **Merchant Hosted DCC** means your checkout UI is fully built and hosted by you. You call PayU's APIs to detect the card, fetch conversion rates, present the DCC offer to the customer on your own page, and then post the payment — giving you complete control over the experience.

<Callout icon="📘" theme="info">
  ### **Other DCC Integration Options:**

  - **PayU Hosted Checkout with DCC:** PayU's checkout page handles the entire DCC UI, rate display, and currency selection. Minimal code for you — just redirect the customer. Lowest PCI scope.
  - **Merchant Hosted Checkout with DCC (this guide):** Your checkout page. You call the BIN check and DCC APIs, build the selection UI, and post the payment. Full UI control but higher PCI obligation.
</Callout>

***

## A. Prerequisites

| \# | Requirement                                                   | Details                                                                                                                                                                                                           |
| -- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1  | **PayU Merchant Account with International Payments enabled** | Contact your **PayU Key Account Manager (KAM)** to enable international payments and DCC on your account. This is mandatory before any international card transactions can be processed.                          |
| 2  | **Merchant Key & Salt**                                       | Obtain your `key` and `salt` from the [PayU Dashboard](https://onboarding.payu.in/app/account/api-credentials). Use **test** credentials for sandbox and **production** credentials for live.                     |
| 3  | **Multi-Currency Configuration**                              | If you are a Multi-Currency Commerce (MCC) merchant, confirm with your KAM which `transactionCurrency` values are enabled on your account.                                                                        |
| 4  | **KYC / Onboarding Documents**                                | Submit all required business and financial documents to PayU (bank statements, ITR, audited accounts, and any LOB-specific certificates such as IATA, FSSAI, import/export) for international payment enablement. |
| 5  | **PCI-DSS Compliance**                                        | Merchant Hosted Checkout collects raw card data (PAN, CVV) on your server. You **must** be PCI-DSS compliant or use PayU-recommended client-side encryption/tokenisation to reduce your scope.                    |
| 6  | **Server-side Hash Generation**                               | All hashes must be computed on your backend server. **Never expose your&#x20;**`salt`**&#x20;in client-side or front-end code.**                                                                                  |
| 7  | **Publicly Reachable Callback URLs**                          | Your `surl` (success) and `furl` (failure) URLs must be HTTPS and publicly accessible for PayU to post payment responses.                                                                                         |

<Callout icon="⚠️" theme="warn">
  ### **Important:** International payments and DCC are **not enabled by default**. You must contact your PayU KAM and complete onboarding before going live.
</Callout>

***

## B. Integration Steps Overview

The Merchant Hosted DCC flow has four distinct steps:

```
Step 1 ──► Check Card BIN          Detect whether card is domestic or international
              │
              ▼ (International card detected)
Step 2 ──► Post Payment to PayU    Submit card + customer details with optional transactionCurrency
              │
              ▼
Step 3 ──► Present DCC Offer       Show customer their home-currency amount, exchange rate & margin
              │                    Customer selects preferred currency
              ▼
Step 4 ──► Verify Payment          Validate response hash + confirm payment status server-to-server
```

| Step | Action                                      | API / Endpoint                                    |
| ---- | ------------------------------------------- | ------------------------------------------------- |
| 1    | Detect if card is international             | `check_isDomestic` API                            |
| 2    | Post payment request                        | `POST https://test.payu.in/_payment`              |
| 3    | Present DCC offer & collect customer choice | Merchant-built UI using PayU-returned DCC details |
| 4    | Verify final payment status                 | `verify_payment` API                              |

***

## C. Make Your Test Payment

### Step 1: Prepare Request Parameters

#### 1a. Check Card BIN (check_isDomestic)

Before attempting a payment, call this API with the first 6 digits of the customer's card to determine whether it is a domestic (Indian) or international card. This drives whether DCC is offered.

**Endpoints:**

| Environment        | URL                                                |
| ------------------ | -------------------------------------------------- |
| **Test (Sandbox)** | `https://test.payu.in/merchant/postservice?form=2` |
| **Production**     | `https://info.payu.in/merchant/postservice?form=2` |

**Request Parameters:**

| Parameter | Data Type | Mandatory | Description                                               | Example Value      |
| --------- | --------- | --------- | --------------------------------------------------------- | ------------------ |
| `key`     | String    | Yes       | Your merchant key provided by PayU.                       | `JP***g`           |
| `command` | String    | Yes       | Fixed value — always pass `check_isDomestic`.             | `check_isDomestic` |
| `var1`    | String    | Yes       | First **6 digits** of the customer's card number (BIN).   | `462273`           |
| `hash`    | String    | Yes       | SHA-512 hash. Formula: `sha512(key\|command\|var1\|salt)` | _(computed)_       |

**Sample cURL:**

```bash
curl --request POST 'https://test.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=check_isDomestic' \
  --data-urlencode 'var1=462273' \
  --data-urlencode 'hash=COMPUTED_SHA512_HASH'
```

**Sample Responses:**

```json
// Domestic card
{ "isDomestic": "Y", "issuingBank": "SCB", "cardType": "VISA", "cardCategory": "CC" }

// International card (DCC can be offered)
{ "isDomestic": "N", "issuingBank": "UNKNOWN", "cardType": "VISA", "cardCategory": "CC" }
```

<Callout icon="📘" theme="info">
  ### **Tip:** If `isDomestic` = `"Y"`, process as a normal domestic card payment. If `isDomestic` = `"N"`, proceed to offer DCC at Step 3.
</Callout>

***

#### 1b. Payment Request Parameters (\_payment)

Once BIN detection confirms an international card, post the full payment to PayU.

**Payment Endpoints:**

| Environment        | URL                               |
| ------------------ | --------------------------------- |
| **Test (Sandbox)** | `https://test.payu.in/_payment`   |
| **Production**     | `https://secure.payu.in/_payment` |

##### Mandatory Parameters

| Parameter     | Data Type | Description                                                                                       | Example Value                    |
| ------------- | --------- | ------------------------------------------------------------------------------------------------- | -------------------------------- |
| `key`         | String    | Your merchant key provided by PayU.                                                               | `JP***g`                         |
| `txnid`       | String    | Merchant-generated unique transaction ID. Must be unique per transaction — no duplicates allowed. | `dcc_txn_001`                    |
| `amount`      | String    | Transaction amount in your base currency (INR), up to 2 decimal places.                           | `1000.00`                        |
| `productinfo` | String    | Brief description of the product or service.                                                      | `International Order`            |
| `firstname`   | String    | Customer's first name.                                                                            | `John`                           |
| `email`       | String    | Customer's email address.                                                                         | `john@example.com`               |
| `phone`       | String    | Customer's 10-digit mobile number.                                                                | `9876543210`                     |
| `pg`          | String    | Payment category. For card payments, use `CC`.                                                    | `CC`                             |
| `bankcode`    | String    | Card network / payment option code.                                                               | `CC`                             |
| `ccnum`       | String    | Customer's full card number (13–19 digits; 15 for AMEX). Must pass Luhn check.                    | `4111111111111111`               |
| `ccname`      | String    | Name as it appears on the card.                                                                   | `John Smith`                     |
| `ccvv`        | String    | Card CVV (3 digits for most cards; 4 digits for AMEX).                                            | `123`                            |
| `ccexpmon`    | String    | Card expiry month (2 digits, MM format).                                                          | `10`                             |
| `ccexpyr`     | String    | Card expiry year (4 digits, YYYY format).                                                         | `2026`                           |
| `surl`        | String    | Success redirect URL — PayU posts the payment response here on success.                           | `https://yourdomain.com/success` |
| `furl`        | String    | Failure redirect URL — PayU redirects here when payment fails.                                    | `https://yourdomain.com/failure` |
| `hash`        | String    | SHA-512 hash computed on your server. See Step 2 below.                                           | _(computed)_                     |

##### Optional Parameters

| Parameter             | Data Type | Description                                                                                                        | Example Value       |
| --------------------- | --------- | ------------------------------------------------------------------------------------------------------------------ | ------------------- |
| `transactionCurrency` | String    | **Required for MCC merchants.** ISO 4217 currency code for multi-currency processing. If omitted, defaults to INR. | `USD`, `AED`, `GBP` |
| `udf1` – `udf5`       | String    | User-defined fields for merchant reference (up to 5). Include as empty strings in hash even if unused.             | `custom_value`      |
| `address1`            | String    | Billing address line 1 (aids fraud detection — recommended for international cards).                               | `123 Main Street`   |
| `address2`            | String    | Billing address line 2.                                                                                            | `Apt 4B`            |
| `city`                | String    | Billing city.                                                                                                      | `New York`          |
| `state`               | String    | Billing state.                                                                                                     | `NY`                |
| `country`             | String    | Billing country.                                                                                                   | `US`                |
| `zipcode`             | String    | Billing ZIP / postal code.                                                                                         | `10001`             |

<Callout icon="📘" theme="info">
  ### **Handy Tips:**

  - `txnid` must be **unique** for every transaction. Reusing a `txnid` causes duplicate errors.
  - Billing address fields (`address1`, `city`, `state`, `country`, `zipcode`) are **strongly recommended** for international card transactions to improve authorization rates and reduce fraud.
  - For international cards, pass `transactionCurrency` if your account supports multi-currency billing.
  - DCC supports **credit, debit, and prepaid cards** on major international schemes (Visa, Mastercard, AMEX).
  - PayU supports cards issued in **130+ currencies** and can display prices in **27 local currencies**.
</Callout>

***

### Step 2: Generate SHA-512 Hash _(Critical Step)_

All hashes must be computed on your server using your PayU `salt`. Never expose the `salt` in client-side code.

#### Payment Request Hash Formula

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|||||Salt)
```

**Rules:**

- Fields are separated by a **pipe character** (`|`).
- If `udf1`–`udf5` are not used, include them as **empty strings** — keep the pipes.
- There are **5 trailing empty pipe-separated placeholders** after `udf5` before `Salt`.
- `Salt` is your PayU-provided merchant salt — treat it as a secret credential.
- `transactionCurrency` is **not** included in the standard hash string. Confirm with your KAM if your specific account configuration requires it.

**Example hash input string:**

```
JP***g|dcc_txn_001|1000.00|International Order|John|john@example.com|||||||||||YOUR_SALT
```

#### BIN Check & Verify Payment Hash Formula

For `check_isDomestic` and `verify_payment` API calls, the hash is simpler:

```
sha512(key|command|var1|salt)
```

#### Hash Generation Code Samples

**Python:**

```python
import hashlib

# Payment request hash
key         = "JP***g"
txnid       = "dcc_txn_001"
amount      = "1000.00"
productinfo = "International Order"
firstname   = "John"
email       = "john@example.com"
udf1 = udf2 = udf3 = udf4 = udf5 = ""
salt        = "YOUR_SALT"

hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}|||||{salt}"
hash_value  = hashlib.sha512(hash_string.encode()).hexdigest()
print(hash_value)

# BIN check / verify_payment hash
def simple_hash(key, command, var1, salt):
    s = f"{key}|{command}|{var1}|{salt}"
    return hashlib.sha512(s.encode()).hexdigest()
```

**PHP:**

```php
<?php
// Payment request hash
$hash_string = "$key|$txnid|$amount|$productinfo|$firstname|$email|$udf1|$udf2|$udf3|$udf4|$udf5|||||$salt";
$hash        = hash('sha512', $hash_string);

// BIN check / verify_payment hash
$simple_hash = hash('sha512', "$key|$command|$var1|$salt");
?>
```

**Java:**

```java
// Payment request hash
String hashString = key + "|" + txnid + "|" + amount + "|" + productinfo + "|" + firstname
    + "|" + email + "|" + udf1 + "|" + udf2 + "|" + udf3 + "|" + udf4 + "|" + udf5
    + "|||||" + salt;
MessageDigest md = MessageDigest.getInstance("SHA-512");
byte[] bytes = md.digest(hashString.getBytes("UTF-8"));
StringBuilder sb = new StringBuilder();
for (byte b : bytes) sb.append(String.format("%02x", b));
String hash = sb.toString();

// BIN check / verify_payment hash
String simpleHash = sha512(key + "|" + command + "|" + var1 + "|" + salt);
```

#### Verify Response Hash (Reverse Hash)

After receiving PayU's response at your `surl`/`furl`, **always validate** the response hash before processing the order:

```
sha512(Salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Callout icon="⚠️" theme="warn">
  ### **Warning:** If the computed reverse hash does not match the `hash` in PayU's response, treat the transaction as tampered or invalid. Do **not** fulfil the order.
</Callout>

***

### Step 3: Post the Request

#### Sample cURL — Minimal Mandatory Parameters (Domestic Card / No DCC)

```bash
curl --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'txnid=dcc_txn_001' \
  --data-urlencode 'amount=1000.00' \
  --data-urlencode 'productinfo=International Order' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'ccnum=4111111111111111' \
  --data-urlencode 'ccname=John Smith' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccexpmon=10' \
  --data-urlencode 'ccexpyr=2026' \
  --data-urlencode 'surl=https://yourdomain.com/success' \
  --data-urlencode 'furl=https://yourdomain.com/failure' \
  --data-urlencode 'hash=REPLACE_WITH_YOUR_SHA512_HASH'
```

#### Sample cURL — With DCC / Multi-Currency (International Card)

```bash
curl --request POST 'https://test.payu.in/_payment' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'txnid=dcc_txn_001' \
  --data-urlencode 'amount=1000.00' \
  --data-urlencode 'productinfo=International Order' \
  --data-urlencode 'firstname=John' \
  --data-urlencode 'email=john@example.com' \
  --data-urlencode 'phone=9876543210' \
  --data-urlencode 'pg=CC' \
  --data-urlencode 'bankcode=CC' \
  --data-urlencode 'ccnum=4111111111111111' \
  --data-urlencode 'ccname=John Smith' \
  --data-urlencode 'ccvv=123' \
  --data-urlencode 'ccexpmon=10' \
  --data-urlencode 'ccexpyr=2026' \
  --data-urlencode 'transactionCurrency=USD' \
  --data-urlencode 'address1=123 Main Street' \
  --data-urlencode 'city=New York' \
  --data-urlencode 'state=NY' \
  --data-urlencode 'country=US' \
  --data-urlencode 'zipcode=10001' \
  --data-urlencode 'surl=https://yourdomain.com/success' \
  --data-urlencode 'furl=https://yourdomain.com/failure' \
  --data-urlencode 'hash=REPLACE_WITH_YOUR_SHA512_HASH'
```

#### Python (requests)

```python
import requests

url = "https://test.payu.in/_payment"
payload = {
    "key":                "JP***g",
    "txnid":              "dcc_txn_001",
    "amount":             "1000.00",
    "productinfo":        "International Order",
    "firstname":          "John",
    "email":              "john@example.com",
    "phone":              "9876543210",
    "pg":                 "CC",
    "bankcode":           "CC",
    "ccnum":              "4111111111111111",
    "ccname":             "John Smith",
    "ccvv":               "123",
    "ccexpmon":           "10",
    "ccexpyr":            "2026",
    "transactionCurrency":"USD",          # omit for domestic / non-MCC merchants
    "surl":               "https://yourdomain.com/success",
    "furl":               "https://yourdomain.com/failure",
    "hash":               "REPLACE_WITH_YOUR_SHA512_HASH"
}
response = requests.post(url, data=payload)
print(response.text)
```

#### JavaScript (Node.js — axios)

```javascript
const axios = require('axios');
const qs    = require('qs');

const payload = {
  key:                 'JP***g',
  txnid:               'dcc_txn_001',
  amount:              '1000.00',
  productinfo:         'International Order',
  firstname:           'John',
  email:               'john@example.com',
  phone:               '9876543210',
  pg:                  'CC',
  bankcode:            'CC',
  ccnum:               '4111111111111111',
  ccname:              'John Smith',
  ccvv:                '123',
  ccexpmon:            '10',
  ccexpyr:             '2026',
  transactionCurrency: 'USD',            // omit for domestic / non-MCC merchants
  surl:                'https://yourdomain.com/success',
  furl:                'https://yourdomain.com/failure',
  hash:                'REPLACE_WITH_YOUR_SHA512_HASH'
};

axios.post('https://test.payu.in/_payment', qs.stringify(payload), {
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
}).then(res => console.log(res.data)).catch(err => console.error(err));
```

#### PHP

```php
<?php
$data = http_build_query([
    "key" => "JP***g", "txnid" => "dcc_txn_001", "amount" => "1000.00",
    "productinfo" => "International Order", "firstname" => "John",
    "email" => "john@example.com", "phone" => "9876543210",
    "pg" => "CC", "bankcode" => "CC",
    "ccnum" => "4111111111111111", "ccname" => "John Smith",
    "ccvv" => "123", "ccexpmon" => "10", "ccexpyr" => "2026",
    "transactionCurrency" => "USD",   // omit for domestic / non-MCC merchants
    "surl" => "https://yourdomain.com/success",
    "furl" => "https://yourdomain.com/failure",
    "hash" => "REPLACE_WITH_YOUR_SHA512_HASH"
]);
$ch = curl_init("https://test.payu.in/_payment");
curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_POSTFIELDS => $data,
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => ["Content-Type: application/x-www-form-urlencoded"]]);
echo curl_exec($ch); curl_close($ch);
?>
```

#### Java

```java
import java.net.*; import java.net.http.*; import java.nio.charset.StandardCharsets;

String[][] params = {
    {"key","JP***g"}, {"txnid","dcc_txn_001"}, {"amount","1000.00"},
    {"productinfo","International Order"}, {"firstname","John"},
    {"email","john@example.com"}, {"phone","9876543210"},
    {"pg","CC"}, {"bankcode","CC"}, {"ccnum","4111111111111111"},
    {"ccname","John Smith"}, {"ccvv","123"}, {"ccexpmon","10"}, {"ccexpyr","2026"},
    {"transactionCurrency","USD"},   // omit for domestic / non-MCC merchants
    {"surl","https://yourdomain.com/success"}, {"furl","https://yourdomain.com/failure"},
    {"hash","REPLACE_WITH_YOUR_SHA512_HASH"}
};
StringBuilder body = new StringBuilder();
for (String[] p : params) {
    if (body.length() > 0) body.append("&");
    body.append(URLEncoder.encode(p[0], StandardCharsets.UTF_8))
        .append("=").append(URLEncoder.encode(p[1], StandardCharsets.UTF_8));
}
HttpRequest req = HttpRequest.newBuilder()
    .uri(URI.create("https://test.payu.in/_payment"))
    .header("Content-Type","application/x-www-form-urlencoded")
    .POST(HttpRequest.BodyPublishers.ofString(body.toString())).build();
System.out.println(HttpClient.newHttpClient().send(req, HttpResponse.BodyHandlers.ofString()).body());
```

#### C\#

```csharp
using System; using System.Collections.Generic; using System.Net.Http; using System.Threading.Tasks;
class PayUDCC {
    static async Task Main() {
        using var client = new HttpClient();
        var payload = new Dictionary<string, string> {
            ["key"]="JP***g", ["txnid"]="dcc_txn_001", ["amount"]="1000.00",
            ["productinfo"]="International Order", ["firstname"]="John",
            ["email"]="john@example.com", ["phone"]="9876543210",
            ["pg"]="CC", ["bankcode"]="CC", ["ccnum"]="4111111111111111",
            ["ccname"]="John Smith", ["ccvv"]="123", ["ccexpmon"]="10", ["ccexpyr"]="2026",
            ["transactionCurrency"]="USD",   // omit for domestic / non-MCC merchants
            ["surl"]="https://yourdomain.com/success",
            ["furl"]="https://yourdomain.com/failure",
            ["hash"]="REPLACE_WITH_YOUR_SHA512_HASH"
        };
        var res = await client.PostAsync("https://test.payu.in/_payment",
            new FormUrlEncodedContent(payload));
        Console.WriteLine(await res.Content.ReadAsStringAsync());
    }
}
```

#### Sample Success Response

```json
{
  "mihpayid":         "403993715524308315",
  "mode":             "CC",
  "status":           "success",
  "unmappedstatus":   "captured",
  "key":              "JP***g",
  "txnid":            "dcc_txn_001",
  "amount":           "1000.00",
  "discount":         "0.00",
  "net_amount_debit": "1000",
  "addedon":          "2024-06-01 14:30:00",
  "productinfo":      "International Order",
  "firstname":        "John",
  "email":            "john@example.com",
  "phone":            "9876543210",
  "hash":             "<response_hash_to_verify>",
  "bank_ref_num":     "ae67e632-f4eb-4121-b47b-2d35dce5ec2e",
  "bankcode":         "CC",
  "error":            "E000",
  "error_Message":    "No Error",
  "cardnum":          "XXXXXXXXXXXX1111"
}
```

***

### Step 4: Complete the Test Payment

#### 4a. Present the DCC Offer to the Customer

After the `check_isDomestic` API confirms the card is international (`isDomestic = "N"`), present the DCC offer to the customer **before** posting the payment. PayU returns the conversion details (exchange rate, converted amount, markup) that you must display:

| Element                      | What to Display                              | Source                 |
| ---------------------------- | -------------------------------------------- | ---------------------- |
| **Merchant currency amount** | Original amount in INR                       | Your order total       |
| **Customer currency amount** | Converted amount in home currency            | PayU DCC rate response |
| **Exchange rate**            | Live FX rate with markup                     | PayU DCC rate response |
| **Disclosure text**          | Mandatory regulatory text (provided by PayU) | PayU DCC rate response |
| **Currency choice**          | Two buttons: "Pay in USD" / "Pay in INR"     | Customer action        |

<Callout icon="⚠️" theme="warn">
  ### **Compliance requirement:** You must display the exchange rate, final amount, and mandatory disclosure text exactly as provided by PayU. Failure to do so may result in chargebacks or non-compliance penalties from card schemes.
</Callout>

#### 4b. Customer Selects Currency

- If the customer selects **their home currency (DCC)**: pass `transactionCurrency` as the ISO code (e.g., `USD`) in your `_payment` POST.
- If the customer selects **merchant currency (INR)**: omit `transactionCurrency` or pass `INR` — PayU processes in INR with no conversion.

#### 4c. Verify Payment (verify_payment)

After receiving PayU's response at your `surl`/`furl`, call the Verify Payment API server-to-server for authoritative status confirmation.

**Endpoint:**

| Environment    | URL                                                |
| -------------- | -------------------------------------------------- |
| **Test**       | `https://test.payu.in/merchant/postservice?form=2` |
| **Production** | `https://info.payu.in/merchant/postservice?form=2` |

**Request Parameters:**

| Parameter | Data Type | Mandatory | Description                                       | Example          |
| --------- | --------- | --------- | ------------------------------------------------- | ---------------- |
| `key`     | String    | Yes       | Your merchant key.                                | `JP***g`         |
| `command` | String    | Yes       | Fixed value — always pass `verify_payment`.       | `verify_payment` |
| `var1`    | String    | Yes       | The `txnid` used in the original payment request. | `dcc_txn_001`    |
| `hash`    | String    | Yes       | `sha512(key\|command\|var1\|salt)`                | _(computed)_     |

**Sample cURL:**

```bash
curl --request POST 'https://test.payu.in/merchant/postservice?form=2' \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --data-urlencode 'key=JP***g' \
  --data-urlencode 'command=verify_payment' \
  --data-urlencode 'var1=dcc_txn_001' \
  --data-urlencode 'hash=COMPUTED_SHA512_HASH'
```

**Sample Verify Response:**

```json
{
  "status":       "1",
  "txn_status":   "SUCCESS",
  "txnid":        "dcc_txn_001",
  "mihpayid":     "403993715524308315",
  "amount":       "1000.00",
  "bank_ref_num": "ae67e632-f4eb-4121-b47b-2d35dce5ec2e",
  "payment_mode": "CC",
  "card_type":    "VISA"
}
```

***

### Errors and Troubleshooting

| Error / Symptom                         | Likely Cause                                                                                  | Fix                                                                                                                                                                                       |
| --------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hash mismatch                           | Wrong field order, extra spaces, incorrect salt, or URL-encoded values used in hash           | Print the raw hash string for debugging. Ensure `udf1`–`udf5` are empty strings (not omitted). The formula is `key\|txnid\|amount\|productinfo\|firstname\|email\|udf1..5\|\|\|\|\|Salt`. |
| `E401` — Unauthorized / Invalid Key     | Wrong merchant `key` or `salt`; or international payments not enabled                         | Confirm credentials from the PayU Dashboard; contact KAM to enable international payments.                                                                                                |
| Card declined — international card      | International payments not enabled on account, or downstream PG does not support the currency | Contact your KAM to verify enablement; confirm the card currency is in the supported list.                                                                                                |
| `isDomestic` returns `"Y"` unexpectedly | BIN is being classified as domestic by PayU                                                   | Verify the first 6 digits are correct; some co-branded or domestic-issued international cards may still show `Y`.                                                                         |
| DCC not offered to customer             | `transactionCurrency` not passed, or card BIN is domestic                                     | Confirm BIN check returns `"N"`, then pass `transactionCurrency` in the payment request.                                                                                                  |
| Currency not supported                  | `transactionCurrency` value is not enabled on your account or not in the supported list       | Refer to the [Supported Currencies for International Payments](../supported_currencies_for_international_payments) list; confirm with your KAM.                                           |
| Exchange rate / amount mismatch         | DCC rate changed between quote and authorization (TTL expired)                                | Re-fetch the DCC rate before submission if the customer took too long to decide. Enforce rate validity time-to-live (TTL).                                                                |
| Response not received at `surl`/`furl`  | Callback URL is not publicly reachable                                                        | Ensure URLs are HTTPS and publicly accessible. Use tools like ngrok for local testing.                                                                                                    |
| Reverse hash mismatch on response       | Response fields used in wrong order                                                           | Follow exact reverse formula: `Salt\|status\|...\|udf5..1\|email\|firstname\|productinfo\|amount\|txnid\|key`.                                                                            |
| Settlement amount differs from expected | DCC conversion fees, cross-border fees, or PG markup applied                                  | Review the fee breakdown provided in the DCC rate response; reconcile with PayU settlement reports.                                                                                       |
| No response / timeout                   | Wrong environment URL or TLS issues                                                           | Confirm test vs. production endpoint; verify TLS 1.2+ is used.                                                                                                                            |

<Callout icon="📘" theme="info">
  ### **Still stuck?** Collect your full request payload (excluding raw card data), response body, `txnid`, and `mihpayid` and contact [PayU Support](https://support.payu.in) or your KAM.
</Callout>

***

## D. What is Next?

Once your test payment succeeds end-to-end, complete these before going live:

- ✅ **Test with multiple card BINs** — test domestic, international, and cards from different issuing countries and currencies to validate the full DCC flow.
- ✅ **Verify response hash** for every transaction before updating order status.
- ✅ **Call&#x20;**`verify_payment`**&#x20;API** server-to-server after every payment — do not rely solely on `surl`/`furl` redirect.
- ✅ **Implement idempotency** on callback handlers to prevent duplicate order fulfilment from repeated redirects.
- ✅ **Store DCC transaction data** — save `mihpayid`, `txnid`, `transactionCurrency`, exchange rate, and converted amount for reconciliation and potential chargebacks.
- ✅ **Build the DCC selection UI** — ensure the currency choice page displays the exchange rate, converted amount, and PayU-provided mandatory disclosure text.
- ✅ **Handle DCC quote TTL** — if the customer takes too long on the selection screen, re-fetch rates before submitting the payment.
- ✅ **Complete PCI-DSS compliance** — for Merchant Hosted Checkout collecting raw card data. Consult your compliance advisor.
- ✅ **Get KAM sign-off** — coordinate with your PayU KAM for production enablement and any certification steps.
- ✅ **Switch to production endpoints** — replace `https://test.payu.in/_payment` → `https://secure.payu.in/_payment` and BIN/verify → `https://info.payu.in/merchant/postservice?form=2`.

***

## E. Next Steps

Explore these resources to extend your DCC integration:

| Resource                                                                                              | Description                                                                     |
| ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| [DCC Overview & Index](../index)                                                                      | Introduction to DCC, how it works, and when to use it                           |
| [DCC Workflow](../dynamic_currency_conversion_workflow)                                               | Detailed end-to-end workflow with API call sequence for DCC                     |
| [PayU Hosted Checkout with DCC](../payu_hosted_checkout_integration_dynamic_currency_conversion)      | Simpler DCC integration with PayU managing the currency selection UI            |
| [Supported Currencies for International Payments](../supported_currencies_for_international_payments) | Full list of 130+ supported card currencies and 27 display currencies           |
| [MCC Currency Codes](../mcc_currency_codes)                                                           | ISO 4217 currency codes used for multi-currency commerce (MCC)                  |
| [APIs Used in International Payments](../apis_used_in_international_payments_integration)             | Complete API reference for `check_isDomestic`, `_payment`, and `verify_payment` |
| [FAQs — Dynamic Currency Conversion](../faqs_dynamic_currency_conversion)                             | Answers to common DCC questions on fees, settlement, FIRC, and onboarding       |

***

_This QuickStart Guide is a draft for review. All endpoint URLs, parameter names, hash formulas, and sample values should be validated against the latest PayU API documentation and confirmed with your PayU KAM before publication._
