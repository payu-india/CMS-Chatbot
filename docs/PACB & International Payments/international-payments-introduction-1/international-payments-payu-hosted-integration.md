---
title: International Payments - PayU Hosted Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Minimal technical setup required</Banner>

With <Glossary>PayU Hosted Checkout</Glossary>, the customer pays on PayU's checkout page. When they enter an international card, PayU handles the currency for you:

* **<Glossary>DCC</Glossary>:** PayU shows the amount in the card's currency and lets the customer choose. You don't need to change your integration.
* **<Glossary>MCC</Glossary>:** you send the payment currency in `transactionCurrency`, and the customer pays in that currency. Unlike <Glossary>Merchant Hosted Checkout</Glossary>, you do not need to call <Glossary>check_isDomestic</Glossary> yourself — PayU handles card detection automatically.

<Callout icon="📘" theme="info">
  ### **Before you begin**

  * Register for a [PayU merchant account](doc:register-for-a-merchant-account-on-dashboard).
  * Ask your PayU Key Account Manager to enable international payments, and say whether you need DCC, MCC or both.
  * Check the currencies you can use: [DCC](doc:supported-currencies-for-international-payments) or [MCC](doc:mcc-currency-codes).
  * Get international test cards from [Test Cards, UPI ID and Wallets](doc:test-cards-upi-id-and-wallets).
</Callout>

**Steps to integrate**

<Cards columns="3">
  <Card title="1. Build and send the request" href="#step-1-build-and-send-the-payment-request">
    Generate the hash and post the payment request to PayU
  </Card>

  <Card title="2. Check the response" href="#step-2-check-the-response-from-payu">
    Verify the response hash and read the payment status
  </Card>

  <Card title="3. Verify the payment" href="#step-3-verify-the-payment">
    Confirm the status from your server before you fulfil the order
  </Card>
</Cards>

**Environment**

| Environment | URL                               |
| :---------- | :-------------------------------- |
| Test        | `https://test.payu.in/_payment`   |
| Production  | `https://secure.payu.in/_payment` |

***

## Step 1: Build and Post the Payment Request

Post the payment request from the customer's browser to PayU. PayU shows its checkout page, the customer chooses to pay by card and enters an international card. For DCC, PayU then shows the currency choice.

**DCC — no extra parameters needed**

DCC needs no extra parameters. Send the standard request, priced in INR, and use the standard <Glossary>hash</Glossary>:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

**MCC — additional parameters required**

For MCC, send three things in addition to the standard request. The key addition is <Glossary>transactionCurrency</Glossary>, which tells PayU which currency to charge:

* `transactionCurrency`: the 3-letter ISO 4217 code of the currency you're charging, for example `USD`. See [Supported Currencies for MCC](doc:mcc-currency-codes).
* `api_version`: set to `22` whenever you send `transactionCurrency`.
* A hash that includes `transactionCurrency` just before the salt:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||transactionCurrency|SALT)
```

`amount` is in the currency you send in `transactionCurrency`.

<Callout icon="🚧" theme="warn">
  ### **Critical Rules**

  * Generate the hash on your server. Never put your <Glossary>salt</Glossary> in the browser or app.
  * For MCC, send `transactionCurrency` and `<Glossary>api_version</Glossary>=22` together. If you send `transactionCurrency` without the right `api_version`, or leave it out of the hash, PayU rejects the payment.
  * If your account uses one <Glossary>merchant key</Glossary> for several currencies, send `transactionCurrency` on every payment, including INR payments.
</Callout>

### Request Parameters

#### Mandatory Parameters

| Parameter     | Type & Description                                                                            | Example                           |
| :------------ | :-------------------------------------------------------------------------------------------- | :-------------------------------- |
| `key`         | `String` — Your merchant key provided by PayU.                                                | `JP***g`                          |
| `txnid`       | `String` — Unique transaction ID that you generate for the order.                             | `PQI6MqpYrjEefU`                  |
| `amount`      | `String` — Payment amount. For DCC, in INR. For MCC, in the `transactionCurrency` currency.   | `10.00`                           |
| `productinfo` | `String` — Short description of the product.                                                  | `iPhone`                          |
| `firstname`   | `String` — Customer's first name.                                                             | `Ashish`                          |
| `email`       | `String` — Customer's email address.                                                          | `test@example.com`                |
| `phone`       | `String` — Customer's phone number.                                                           | `9876543210`                      |
| `surl`        | `String` — <Glossary>surl</Glossary>. PayU posts the response here when the payment succeeds. | `https://yourwebsite.com/success` |
| `furl`        | `String` — <Glossary>furl</Glossary>. PayU posts the response here when the payment fails.    | `https://yourwebsite.com/failure` |
| `hash`        | `String` — <Glossary>SHA-512</Glossary> hash generated on your server, as shown above.        | `d3b4...e9f1`                     |

#### MCC-Specific Parameters

| Parameter             | Type & Description                                                                                                                        | Example |
| :-------------------- | :---------------------------------------------------------------------------------------------------------------------------------------- | :------ |
| `transactionCurrency` | `String` — 3-letter ISO 4217 code of the payment currency. Mandatory for MCC. See [Supported Currencies for MCC](doc:mcc-currency-codes). | `USD`   |
| `api_version`         | `String` — Set to `22` when you send `transactionCurrency`.                                                                               | `22`    |

#### Optional Parameters

| Parameter     | Type & Description                                                                     | Example           |
| :------------ | :------------------------------------------------------------------------------------- | :---------------- |
| `lastname`    | `String` — Customer's last name.                                                       | `Kumar`           |
| `address1`    | `String` — First line of the billing address. Helps with fraud checks and chargebacks. | `123 Main Street` |
| `address2`    | `String` — Second line of the billing address.                                         | `Apt 4B`          |
| `city`        | `String` — Billing city.                                                               | `London`          |
| `state`       | `String` — Billing state or region.                                                    | `Greater London`  |
| `country`     | `String` — Billing country.                                                            | `United Kingdom`  |
| `zipcode`     | `String` — Billing postal code. Up to 20 characters.                                   | `SW1A 1AA`        |
| `udf1`–`udf5` | `String` — User-defined fields for your own reference.                                 | `Order-7781`      |

<Callout icon="💡" theme="info">
  ### **Tips**

  Send the customer's full billing address, email and phone. PayU uses these details for fraud checks on international cards.
</Callout>

### Generate the Hash

#### Generate Hash for DCC

For DCC, do **not** include `transactionCurrency` in the hash string.

```bash
# Formula:
# sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
echo -n "YOUR_MERCHANT_KEY|PQI6MqpYrjEefU|1000.00|iPhone|Ashish|test@example.com|||||||||||YOUR_SALT" | sha512sum
```
```python
import hashlib, os

def generate_hash_dcc(p, salt):
    fields = [
        p['key'], p['txnid'], p['amount'], p['productinfo'],
        p['firstname'], p['email'],
        p.get('udf1', ''), p.get('udf2', ''), p.get('udf3', ''),
        p.get('udf4', ''), p.get('udf5', ''),
        '', '', '', '', '',
        salt
    ]
    return hashlib.sha512('|'.join(fields).encode('utf-8')).hexdigest()

hash_value = generate_hash_dcc(params, os.environ['PAYU_SALT'])
```
```csharp
using System.Security.Cryptography;
using System.Text;

public static string GenerateHashDcc(Dictionary<string, string> p, string salt)
{
    string G(string k) => p.TryGetValue(k, out var v) ? v : "";
    var f = new List<string> {
        G("key"), G("txnid"), G("amount"), G("productinfo"), G("firstname"), G("email"),
        G("udf1"), G("udf2"), G("udf3"), G("udf4"), G("udf5"),
        "", "", "", "", "",
        salt
    };
    using var sha = SHA512.Create();
    var bytes = sha.ComputeHash(Encoding.UTF8.GetBytes(string.Join("|", f)));
    return string.Concat(bytes.Select(b => b.ToString("x2")));
}
```
```javascript
const crypto = require('crypto');

function generateHashDcc(p, salt) {
  const fields = [
    p.key, p.txnid, p.amount, p.productinfo, p.firstname, p.email,
    p.udf1 || '', p.udf2 || '', p.udf3 || '', p.udf4 || '', p.udf5 || '',
    '', '', '', '', '',
    salt
  ];
  return crypto.createHash('sha512').update(fields.join('|')).digest('hex');
}

const hash = generateHashDcc(params, process.env.PAYU_SALT);
```
```java
import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;
import java.util.*;

public static String generateHashDcc(Map<String, String> p, String salt) throws Exception {
    List<String> f = new ArrayList<>(Arrays.asList(
        p.get("key"), p.get("txnid"), p.get("amount"), p.get("productinfo"),
        p.get("firstname"), p.get("email"),
        p.getOrDefault("udf1", ""), p.getOrDefault("udf2", ""),
        p.getOrDefault("udf3", ""), p.getOrDefault("udf4", ""),
        p.getOrDefault("udf5", ""), "", "", "", "", "",
        salt
    ));
    byte[] d = MessageDigest.getInstance("SHA-512")
        .digest(String.join("|", f).getBytes(StandardCharsets.UTF_8));
    StringBuilder sb = new StringBuilder();
    for (byte b : d) sb.append(String.format("%02x", b));
    return sb.toString();
}
```
```php
<?php
function generateHashDcc(array $p, string $salt): string {
    $fields = [
        $p['key'], $p['txnid'], $p['amount'], $p['productinfo'],
        $p['firstname'], $p['email'],
        $p['udf1'] ?? '', $p['udf2'] ?? '', $p['udf3'] ?? '',
        $p['udf4'] ?? '', $p['udf5'] ?? '',
        '', '', '', '', '',
        $salt
    ];
    return hash('sha512', implode('|', $fields));
}

$hash = generateHashDcc($params, getenv('PAYU_SALT'));
```

#### Generate Hash for MCC

For MCC, include `transactionCurrency` just before the salt.

```bash
# Formula:
# sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||transactionCurrency|SALT)
echo -n "YOUR_MERCHANT_KEY|PQI6MqpYrjEefV|12.00|iPhone|Ashish|test@example.com|||||||||||USD|YOUR_SALT" | sha512sum
```
```python
import hashlib, os

def generate_hash_mcc(p, salt):
    fields = [
        p['key'], p['txnid'], p['amount'], p['productinfo'],
        p['firstname'], p['email'],
        p.get('udf1', ''), p.get('udf2', ''), p.get('udf3', ''),
        p.get('udf4', ''), p.get('udf5', ''),
        '', '', '', '', '',
        p['transactionCurrency'],
        salt
    ]
    return hashlib.sha512('|'.join(fields).encode('utf-8')).hexdigest()

hash_value = generate_hash_mcc(params, os.environ['PAYU_SALT'])
```
```csharp
using System.Security.Cryptography;
using System.Text;

public static string GenerateHashMcc(Dictionary<string, string> p, string salt)
{
    string G(string k) => p.TryGetValue(k, out var v) ? v : "";
    var f = new List<string> {
        G("key"), G("txnid"), G("amount"), G("productinfo"), G("firstname"), G("email"),
        G("udf1"), G("udf2"), G("udf3"), G("udf4"), G("udf5"),
        "", "", "", "", "",
        G("transactionCurrency"),
        salt
    };
    using var sha = SHA512.Create();
    var bytes = sha.ComputeHash(Encoding.UTF8.GetBytes(string.Join("|", f)));
    return string.Concat(bytes.Select(b => b.ToString("x2")));
}
```
```javascript
const crypto = require('crypto');

function generateHashMcc(p, salt) {
  const fields = [
    p.key, p.txnid, p.amount, p.productinfo, p.firstname, p.email,
    p.udf1 || '', p.udf2 || '', p.udf3 || '', p.udf4 || '', p.udf5 || '',
    '', '', '', '', '',
    p.transactionCurrency,
    salt
  ];
  return crypto.createHash('sha512').update(fields.join('|')).digest('hex');
}

const hash = generateHashMcc(params, process.env.PAYU_SALT);
```
```java
import java.security.MessageDigest;
import java.nio.charset.StandardCharsets;
import java.util.*;

public static String generateHashMcc(Map<String, String> p, String salt) throws Exception {
    List<String> f = new ArrayList<>(Arrays.asList(
        p.get("key"), p.get("txnid"), p.get("amount"), p.get("productinfo"),
        p.get("firstname"), p.get("email"),
        p.getOrDefault("udf1", ""), p.getOrDefault("udf2", ""),
        p.getOrDefault("udf3", ""), p.getOrDefault("udf4", ""),
        p.getOrDefault("udf5", ""), "", "", "", "", "",
        p.get("transactionCurrency"),
        salt
    ));
    byte[] d = MessageDigest.getInstance("SHA-512")
        .digest(String.join("|", f).getBytes(StandardCharsets.UTF_8));
    StringBuilder sb = new StringBuilder();
    for (byte b : d) sb.append(String.format("%02x", b));
    return sb.toString();
}
```
```php
<?php
function generateHashMcc(array $p, string $salt): string {
    $fields = [
        $p['key'], $p['txnid'], $p['amount'], $p['productinfo'],
        $p['firstname'], $p['email'],
        $p['udf1'] ?? '', $p['udf2'] ?? '', $p['udf3'] ?? '',
        $p['udf4'] ?? '', $p['udf5'] ?? '',
        '', '', '', '', '',
        $p['transactionCurrency'],
        $salt
    ];
    return hash('sha512', implode('|', $fields));
}

$hash = generateHashMcc($params, getenv('PAYU_SALT'));
```

### Sample Request

The following examples show a complete payment request. For DCC, omit `transactionCurrency` and `api_version`; for MCC, include both and use the MCC hash.

**DCC — HTML Form**

```html
<form action="https://test.payu.in/_payment" method="post">
  <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
  <input type="hidden" name="txnid" value="PQI6MqpYrjEefU" />
  <input type="hidden" name="amount" value="1000.00" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="email" value="test@example.com" />
  <input type="hidden" name="phone" value="9876543210" />
  <input type="hidden" name="surl" value="https://yourwebsite.com/success" />
  <input type="hidden" name="furl" value="https://yourwebsite.com/failure" />
  <input type="hidden" name="hash" value="HASH_GENERATED_ON_YOUR_SERVER" />
  <input type="submit" value="Pay" />
</form>
```

**MCC — HTML Form**

```html
<form action="https://test.payu.in/_payment" method="post">
  <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
  <input type="hidden" name="txnid" value="PQI6MqpYrjEefV" />
  <input type="hidden" name="amount" value="12.00" />
  <input type="hidden" name="transactionCurrency" value="USD" />
  <input type="hidden" name="api_version" value="22" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="email" value="test@example.com" />
  <input type="hidden" name="phone" value="9876543210" />
  <input type="hidden" name="surl" value="https://yourwebsite.com/success" />
  <input type="hidden" name="furl" value="https://yourwebsite.com/failure" />
  <input type="hidden" name="hash" value="HASH_INCLUDING_TRANSACTION_CURRENCY" />
  <input type="submit" value="Pay" />
</form>
```

**MCC — cURL**

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "txnid=PQI6MqpYrjEefV" \
  -d "amount=12.00" \
  -d "transactionCurrency=USD" \
  -d "api_version=22" \
  -d "productinfo=iPhone" \
  -d "firstname=Ashish" \
  -d "email=test@example.com" \
  -d "phone=9876543210" \
  -d "surl=https://yourwebsite.com/success" \
  -d "furl=https://yourwebsite.com/failure" \
  -d "hash=HASH_INCLUDING_TRANSACTION_CURRENCY"
```
```python
import os, requests

payload = {
    "key": os.environ["PAYU_KEY"],
    "txnid": "PQI6MqpYrjEefV",
    "amount": "12.00",
    "transactionCurrency": "USD",
    "api_version": "22",
    "productinfo": "iPhone",
    "firstname": "Ashish",
    "email": "test@example.com",
    "phone": "9876543210",
    "surl": "https://yourwebsite.com/success",
    "furl": "https://yourwebsite.com/failure",
}
payload["hash"] = generate_hash_mcc(payload, os.environ["PAYU_SALT"])
response = requests.post("https://test.payu.in/_payment", data=payload, timeout=30)
```
```csharp
using System.Net.Http;
using System.Collections.Generic;

var payload = new Dictionary<string, string> {
    ["key"] = Environment.GetEnvironmentVariable("PAYU_KEY"),
    ["txnid"] = "PQI6MqpYrjEefV",
    ["amount"] = "12.00",
    ["transactionCurrency"] = "USD",
    ["api_version"] = "22",
    ["productinfo"] = "iPhone",
    ["firstname"] = "Ashish",
    ["email"] = "test@example.com",
    ["phone"] = "9876543210",
    ["surl"] = "https://yourwebsite.com/success",
    ["furl"] = "https://yourwebsite.com/failure",
};
payload["hash"] = GenerateHashMcc(payload, Environment.GetEnvironmentVariable("PAYU_SALT"));

using var client = new HttpClient();
var response = await client.PostAsync(
    "https://test.payu.in/_payment",
    new FormUrlEncodedContent(payload)
);
```
```javascript
const payload = {
  key: process.env.PAYU_KEY,
  txnid: 'PQI6MqpYrjEefV',
  amount: '12.00',
  transactionCurrency: 'USD',
  api_version: '22',
  productinfo: 'iPhone',
  firstname: 'Ashish',
  email: 'test@example.com',
  phone: '9876543210',
  surl: 'https://yourwebsite.com/success',
  furl: 'https://yourwebsite.com/failure',
};
payload.hash = generateHashMcc(payload, process.env.PAYU_SALT);

const response = await fetch('https://test.payu.in/_payment', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams(payload),
});
```
```java
import java.net.http.*;
import java.net.URI;
import java.util.*;
import java.util.stream.Collectors;

Map<String, String> payload = new LinkedHashMap<>();
payload.put("key", System.getenv("PAYU_KEY"));
payload.put("txnid", "PQI6MqpYrjEefV");
payload.put("amount", "12.00");
payload.put("transactionCurrency", "USD");
payload.put("api_version", "22");
payload.put("productinfo", "iPhone");
payload.put("firstname", "Ashish");
payload.put("email", "test@example.com");
payload.put("phone", "9876543210");
payload.put("surl", "https://yourwebsite.com/success");
payload.put("furl", "https://yourwebsite.com/failure");
payload.put("hash", generateHashMcc(payload, System.getenv("PAYU_SALT")));

String form = payload.entrySet().stream()
    .map(e -> e.getKey() + "=" + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
    .collect(Collectors.joining("&"));

HttpRequest request = HttpRequest.newBuilder()
    .uri(URI.create("https://test.payu.in/_payment"))
    .header("Content-Type", "application/x-www-form-urlencoded")
    .POST(HttpRequest.BodyPublishers.ofString(form))
    .build();
HttpResponse<String> response = HttpClient.newHttpClient().send(request, HttpResponse.BodyHandlers.ofString());
```
```php
<?php
$payload = [
    'key'                 => getenv('PAYU_KEY'),
    'txnid'               => 'PQI6MqpYrjEefV',
    'amount'              => '12.00',
    'transactionCurrency' => 'USD',
    'api_version'         => '22',
    'productinfo'         => 'iPhone',
    'firstname'           => 'Ashish',
    'email'               => 'test@example.com',
    'phone'               => '9876543210',
    'surl'                => 'https://yourwebsite.com/success',
    'furl'                => 'https://yourwebsite.com/failure',
];
$payload['hash'] = generateHashMcc($payload, getenv('PAYU_SALT'));

$ch = curl_init('https://test.payu.in/_payment');
curl_setopt_array($ch, [
    CURLOPT_POST           => true,
    CURLOPT_POSTFIELDS     => http_build_query($payload),
    CURLOPT_RETURNTRANSFER => true,
]);
$response = curl_exec($ch);
curl_close($ch);
```

**Expected output:** the customer sees PayU Hosted Checkout. With an international card, a DCC customer sees the currency choice, and an MCC customer sees the amount in the currency you sent.

***

## Step 2: Check the response from PayU

PayU posts the result to your `surl` or `furl` as form data. Before you update the order:

1. Calculate the reverse hash and compare it with the `hash` in the response:

   ```
   sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
   ```

   If the response includes `additional_charges`, add it at the start:

   ```
   sha512(additional_charges|SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
   ```

2. Check that `status` is `success` and `unmappedstatus` is `captured`.

{/* REVIEW: confirm the reverse hash for MCC payments, and whether it includes transactionCurrency. */}

<ReverseHashing />

**Success Response:**

```json
{
  "mihpayid": "403993715527769337",
  "mode": "CC",
  "status": "success",
  "unmappedstatus": "captured",
  "key": "YOUR_MERCHANT_KEY",
  "txnid": "PQI6MqpYrjEefU",
  "amount": "1000.00",
  "cardCategory": "international",
  "discount": "0.00",
  "net_amount_debit": "1000",
  "productinfo": "iPhone",
  "firstname": "Ashish",
  "email": "test@example.com",
  "phone": "9876543210",
  "field9": "Transaction Completed Successfully",
  "payment_source": "payu",
  "PG_TYPE": "CC-PG",
  "bank_ref_num": "<bank reference>",
  "bankcode": "MASTCC",
  "error": "E000",
  "error_Message": "No Error",
  "cardnum": "XXXXXXXXXXXX1287",
  "hash": "<response hash>"
}
```

**Failure Response:**

```json
{
  "mihpayid": "403993715527769338",
  "mode": "CC",
  "status": "failure",
  "unmappedstatus": "failed",
  "key": "YOUR_MERCHANT_KEY",
  "txnid": "PQI6MqpYrjEefW",
  "amount": "1000.00",
  "cardCategory": "international",
  "net_amount_debit": "0",
  "productinfo": "iPhone",
  "firstname": "Ashish",
  "email": "test@example.com",
  "field9": "<bank failure reason>",
  "bankcode": "MASTCC",
  "error": "<error code>",
  "error_Message": "<error message>",
  "hash": "<response hash>"
}
```

**Expected output:** the reverse hash matches and the status tells you whether to confirm or cancel the order.

***

## Step 3: Verify the payment

Browser redirects can be interrupted or spoofed. For DCC, the customer also completes <Glossary>3D Secure</Glossary> authentication before the final redirect. Confirm the status from your server with the <Glossary>Verify Payment API</Glossary> or a <Glossary>webhook</Glossary> before you fulfil the order.

<Verify_Payment_Tabs />

***

## Refunds

No change is needed in your <Glossary>refund</Glossary> integration. These rules apply to both PayU Hosted Checkout and Merchant Hosted Checkout.

* **DCC:** raise refunds in INR, for the original INR amount. PayU converts the amount to the currency the customer paid in.
* **MCC:** raise refunds in the original payment currency.

> **Note:** PayU applies an <Glossary>exchange rate</Glossary> and a <Glossary>markup</Glossary> to DCC transactions. The converted amount the customer pays is inclusive of the markup. <Glossary>Settlement</Glossary> to your account is processed in INR for DCC payments.

{/* REVIEW: confirm the exchange rate used for DCC refunds. */}

***

## Common first-time errors

| Problem                                              | Likely cause                                                                  | Fix                                                                           |
| :--------------------------------------------------- | :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Payment rejected for an MCC request                  | `transactionCurrency` missing from the hash, or `api_version` not set to `22` | Add the currency before the salt and send `api_version=22`                    |
| Payment fails on a single-key multi-currency account | `transactionCurrency` not sent                                                | Send `transactionCurrency` on every payment, including INR                    |
| No currency choice shown                             | Card is domestic, or international payments or DCC aren't enabled             | Use an international test card, or ask your Key Account Manager to enable DCC |
| Hash mismatch                                        | Salt or field order wrong                                                     | Check the formula and generate the hash on your server                        |

***

## Next steps

<Cards columns="3">
  <Card title="Merchant Hosted Checkout" href="doc:merchant-hosted-checkout-dynamic-currency-conversion" icon="fa-code">
    Accept international payments on your own checkout.
  </Card>

  <Card title="MCC currencies" href="doc:mcc-currency-codes" icon="fa-coins">
    Find the currency codes for transactionCurrency.
  </Card>

  <Card title="FAQs" href="doc:faqs-dynamic-currency-conversion" icon="fa-circle-question">
    Find answers on settlement, refunds and documents.
  </Card>
</Cards>
