---
title: '[Internal Review]Get Checkout Details API '
deprecated: false
hidden: true
metadata:
  robots: index
---
---
title: Get Checkout Details API
deprecated: false
hidden: false
metadata:
  title: Get Checkout Details API
  description: >-
    The Get Checkout Details API returns payment options, extended EMI details,
    additional charges, tax configuration, downtime status, and customer
    eligibility for custom checkout pages.
  keywords:
    - Get Checkout Details API
    - get_checkout_details
    - checkout detail API
    - EMI eligibility API
    - payment options API
    - additional charges API
  robots: index
---

The Get Checkout Details API returns the information required to build custom checkout experiences — including payment options, extended EMI details, additional charges, tax configuration, downtime status, and customer eligibility.

Use this API when you need to render payment methods, show EMI breakups, validate customer eligibility, or surface downtime before the customer proceeds to pay.

| Capability | Description |
| :--------- | :---------- |
| Payment option details | Extended details for each enabled payment mode, including titles, limits, tenure breakup, and PG routing. |
| Additional charges | Convenience or surcharge amounts configured per payment option. |
| Eligibility details | EMI, BNPL, and cardless eligibility based on customer mobile number. |
| Downtime details | Issuing-bank and payment-mode downtime status. |
| Merchant and SDK config | Merchant branding, tax specification, and SDK configuration. |

## Environment

|            |                                                                                                  |
| :--------- | :----------------------------------------------------------------------------------------------- |
| Production | [https://api.payu.in/fems/v1/checkout/detail](https://api.payu.in/fems/v1/checkout/detail)       |
| Test       | [https://apitest.payu.in/fems/v1/checkout/detail](https://apitest.payu.in/fems/v1/checkout/detail) |

HTTP Method: **POST**

## Request header

All Get Checkout Details API requests require **HMAC-SHA512** header authentication. Every request must include a `Date` header and a signed `Authorization` header.

### Required request headers

| Header | Description |
| :----- | :---------- |
| Content-Type | `application/json` |
| accept | `application/json` |
| Date | Current UTC timestamp in RFC 1123 format (for example, `Fri, 24 Jul 2026 05:51:20 GMT`). Use the same value when computing the Authorization header. |
| Authorization | HMAC-SHA512 signature. Format: `hmac username="<merchant_key>", algorithm="sha512", headers="date", signature="<computed_signature>"`. |

<Accordion title="Authorization fields and hashing algorithm" icon="fa-code">
#### Authorization fields description

| Parameter | Description |
| --------- | ----------- |
| username | Merchant key provided by PayU during onboarding. |
| algorithm | Hashing algorithm used for the signature. Use `sha512`. |
| headers | Headers included in the signature. Use `date`. |
| signature | SHA-512 hash of the signing string, in lowercase hexadecimal. |

#### Hashing algorithm

Build the signing string using the **exact raw JSON request body** sent with the request:

```
sha512(<raw_request_body>|<Date>|<merchant_secret>)
```

Where:

* `<raw_request_body>` is the exact JSON body string posted with the request.
* `<Date>` is the same value sent in the `Date` header.
* `<merchant_secret>` is the merchant Salt provided by PayU during onboarding.

Convert the SHA-512 output to **lowercase hexadecimal** (zero-pad to 128 characters if required) and pass it as `signature` in the `Authorization` header:

```
hmac username="<merchant_key>", algorithm="sha512", headers="date", signature="<signature>"
```

#### Signing rules

* Use the exact raw JSON request body. The JSON string used for hashing must exactly match the request body sent in the POST call.
* The `Date` value in the signature must exactly match the `Date` header.
* Regenerate `Date` and `Authorization` for every request.
</Accordion>

<br />

## Request parameters
<HTMLBlock>{`
<style>
/* Target only the second column in the table */
.markdown-body table td:nth-child(2) {
  word-break: break-word !important;
}

/* Keep the first column from breaking unnecessarily */
.markdown-body table td:nth-child(1) {
  word-break: normal;
  white-space: nowrap;
}
</style>
<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Parameter
      </th>
      <th style={{ textAlign: "left" }}>
        Description
      </th>
      <th style={{ textAlign: "left" }}>
        Example
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        requestId <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>String</code> Unique request identifier. Allowed characters: a–z, A–Z, 0–9, _.
      </td>
      <td style={{ textAlign: "left" }}>
        9920371372_38
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        transactionDetails <br/>
        <code>mandatory</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Object</code> Transaction context. Must include <code>amount</code>. Optional fields: <code>txnId</code>, <code>additional_charges</code>, <code>pre_authorize</code>, <code>source</code>.
      </td>
      <td style={{ textAlign: "left" }}>
        {"amount": 8000}
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        useCase <br/>
        <code>recommended</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Object</code> Flags that control which data is returned. Set at least one flag to <code>true</code>. You can combine multiple flags in a single request.
      </td>
      <td style={{ textAlign: "left" }}>
        {"getExtendedPaymentDetails": true}
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        customerDetails <br/>
        <code>conditional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Object</code> Required when <code>checkCustomerEligibility</code> is true. If included, <code>mobile</code> must be a valid 10-digit mobile number. Optional: <code>ifscCodes</code> for bank-name mapping.
      </td>
      <td style={{ textAlign: "left" }}>
        {"mobile": "9368252248"}
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        filters <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Object</code> Limits which payment modes and options are returned under <code>paymentOptions</code>.
      </td>
      <td style={{ textAlign: "left" }}>
        {"paymentOptions": {"emi": {"dc": "SBIN,KKBK,ICIC"}}}
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        apiTimeout <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Integer</code> Timeout in milliseconds for downstream eligibility calls.
      </td>
      <td style={{ textAlign: "left" }}>
        5000
      </td>
    </tr>
    <tr>
      <td style={{ textAlign: "left" }}>
        isSITxn <br/>
        <code>optional</code>
      </td>
      <td style={{ textAlign: "left" }}>
        <code>Boolean</code> Set to <code>true</code> for Standing Instruction transactions.
      </td>
      <td style={{ textAlign: "left" }}>
        false
      </td>
    </tr>
  </tbody>
</Table>
`}</HTMLBlock>
<Accordion title="transactionDetails JSON Fields description" icon="fa-table">
### transactionDetails fields

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| amount `mandatory` | `Number` Transaction amount. | `8000` |
| txnId `optional` | `String` Transaction ID. When provided, the API validates it has not already been captured. | `TXN_12345` |
| additional_charges `optional` | `String` Pre-configured charges in `MODE:amount` format. | `"UPI:10,CC:5"` |
| pre_authorize `optional` | `Integer` Set to `1` for UPI OTM / pre-authorize options. | `1` |
| source `optional` | `String` Transaction source. | `"Android_SDK"`, `"IOS_SDK"` |
</Accordion>
<Accordion title="customerDetails JSON Fields description" icon="fa-table">
### customerDetails fields

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| mobile `conditional` | `String` Customer mobile number. Required when `checkCustomerEligibility` is true. | `9368252248` |
| ifscCodes `optional` | `String[]` IFSC codes for bank-name mapping. | `["SBIN", "HDFC"]` |
</Accordion>
<Accordion title="filters.paymentOptions JSON Fields description" icon="fa-table">
### filters.paymentOptions fields

| Filter key | Description | Example |
| ---------- | ----------- | ------- |
| emi.dc | Debit-card EMI banks | `"SBIN,KKBK,ICIC"` or `"all"` |
| emi.cc | Credit-card EMI banks | `"all"` |
| emi.cardless | Cardless EMI lenders | `"all"` |
| emi.other | Other EMI options | `"all"` |
| emi.payInParts | Pay-in-Parts lenders | `"LENDER_CODE"` |
| bnpl | BNPL options | `"all"` |
| cc | Credit card types | `"CC,RUPAYCC"` |
| dc | Debit card types | `"MAST,RUPAY"` |
| nb | Net banking options | `"SBIB,AXIB"` |
| upi | UPI options | `"all"` |
| cash | Wallet and cash options. Includes wallet-style methods (PhonePe, Amazon Pay, Paytm) in addition to cash-collection options. | `"PAYTM"` |
| enach | eNACH options | `"all"` |
| standinginstruction / si | Standing Instruction options | `"all"` |
</Accordion>
<Accordion title="useCase JSON Fields description" icon="fa-="fa-table">
### useCase fields

| Field | Description |
| ----- | ----------- |
| getExtendedPaymentDetails | `Boolean` Returns EMI tenure breakup — interest rate, monthly EMI, interest charged, payback amount, bank charge. |
| getAdditionalCharges | `Boolean` Returns `additionalCharge` for each payment option. |
| getTaxSpecification | `Boolean` Returns `configData.taxSpecification`. |
| checkDownStatus | `Boolean` Returns `downInfo` with downtime lists. |
| checkCustomerEligibility | `Boolean` Evaluates EMI and BNPL eligibility. Requires `customerDetails.mobile`. |
| checkNTBCustomerEligibility | `Boolean` Includes NTB EMI eligibility in `paymentOption.emi.ntb`. |
| returnUserLimit | `Boolean` Returns `maximumEligibleLimit` on eligible tenure options. |
| getMerchantDetails | `Boolean` Returns merchant branding in `merchant`. |
| getActivePaymentDetails | `Boolean` Returns only active payment options with full detail. |
| getPgIdForEachOption | `Boolean` Includes `pgId` for each payment option. |
| emiTopBanks | `Boolean` Returns prioritized top bank list within EMI subcategories. |
</Accordion>
<Accordion title="Example JSON" icon="fa-="fa-table">
### Example request body

```json
{
  "requestId": "9920371372_38",
  "transactionDetails": {
    "amount": 8000,
    "txnId": "TXN_12345",
    "additional_charges": "UPI:10",
    "pre_authorize": 1,
    "source": "Android_SDK"
  },
  "customerDetails": {
    "mobile": "9368252248",
    "ifscCodes": [
      "SBIN",
      "HDFC"
    ]
  },
  "useCase": {
    "getExtendedPaymentDetails": true,
    "getAdditionalCharges": true,
    "checkCustomerEligibility": true,
    "getMerchantDetails": true
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "dc": "SBIN,KKBK,ICIC",
        "cc": "all",
        "cardless": "all",
        "other": "all"
      },
      "bnpl": "all",
      "nb": "all",
      "cc": "all",
      "dc": "all",
      "upi": "all",
      "cash": "all",
      "enach": "all"
    }
  },
  "apiTimeout": 5000,
  "isSITxn": false
}
```
</Accordion>
## Sample request

All samples below include HMAC-SHA512 authentication headers. Replace `YOUR_MERCHANT_KEY`, `YOUR_MERCHANT_SALT`, and `GENERATED_SIGNATURE` with your PayU credentials. See [Request header](#request-header) for the signing algorithm.

<Accordion title="Get extended payment details" icon="fa-code">
Use `getExtendedPaymentDetails` to retrieve EMI tenure breakup and extended payment option details.

```curl
curl -X POST "https://api.payu.in/fems/v1/checkout/detail" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Date: Fri, 24 Jul 2026 05:51:20 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}'
```
```python
import hashlib
import json
import requests
from datetime import datetime, timezone

def get_sha512_hash(hash_string):
    return hashlib.sha512(hash_string.encode("utf-8")).hexdigest().zfill(128)

key = "YOUR_MERCHANT_KEY"
secret = "YOUR_MERCHANT_SALT"
url = "https://api.payu.in/fems/v1/checkout/detail"

payload = {'requestId': '9920371372_38',
 'transactionDetails': {'amount': 8000},
 'useCase': {'getExtendedPaymentDetails': True}}

date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
body = json.dumps(payload, separators=(",", ":"))
signature = get_sha512_hash(f"{body}|{date}|{secret}")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Date": date,
    "Authorization": (
        f'hmac username="{key}", algorithm="sha512", '
        f'headers="date", signature="{signature}"'
    ),
}

response = requests.post(url, data=body, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```javascript
const crypto = require("crypto");

function getSha512Hash(hashString) {
  return crypto.createHash("sha512").update(hashString).digest("hex").padStart(128, "0");
}

const key = "YOUR_MERCHANT_KEY";
const secret = "YOUR_MERCHANT_SALT";
const url = "https://api.payu.in/fems/v1/checkout/detail";

const payload = {
  "requestId": "9920371372_38",
  "transactionDetails": {
    "amount": 8000
  },
  "useCase": {
    "getExtendedPaymentDetails": true
  }
};

const date = new Date().toUTCString();
const body = JSON.stringify(payload);
const signature = getSha512Hash(`${body}|${date}|${secret}`);

async function makeRequest() {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Date": date,
        "Authorization": `hmac username="${key}", algorithm="sha512", headers="date", signature="${signature}"`
      },
      body: body
    });
    const data = await response.text();
    console.log("Status Code:", response.status);
    console.log("Response:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

makeRequest();
```
```java
import java.math.BigInteger;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class CheckoutDetailRequest {
    public static String getSha512Hash(String hashString) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        String hashtext = new BigInteger(1, digest).toString(16);
        return String.format("%128s", hashtext).replace(' ', '0');
    }

    public static void main(String[] args) throws Exception {
        String key = "YOUR_MERCHANT_KEY";
        String secret = "YOUR_MERCHANT_SALT";
        String url = "https://api.payu.in/fems/v1/checkout/detail";

        String requestBodyJson = "{\"requestId\":\"9920371372_38\",\"transactionDetails\":{\"amount\":8000},\"useCase\":{\"getExtendedPaymentDetails\":true}}";
        String date = DateTimeFormatter
                .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
                .format(ZonedDateTime.now(ZoneOffset.UTC));
        String hash = getSha512Hash(requestBodyJson + "|" + date + "|" + secret);
        String authorization = "hmac username=\"" + key
                + "\", algorithm=\"sha512\", headers=\"date\", signature=\""
                + hash + "\"";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/json")
                .header("Date", date)
                .header("Authorization", authorization)
                .POST(HttpRequest.BodyPublishers.ofString(requestBodyJson))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var key = "YOUR_MERCHANT_KEY";
        var secret = "YOUR_MERCHANT_SALT";
        var url = "https://api.payu.in/fems/v1/checkout/detail";

        var body = @"{""requestId"":""9920371372_38"",""transactionDetails"":{""amount"":8000},""useCase"":{""getExtendedPaymentDetails"":true}}";
        var date = DateTime.UtcNow.ToString("r");
        var hashString = $"{body}|{date}|{secret}";
        var signature = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(hashString)))
            .ToLower()
            .PadLeft(128, '0');

        var client = new HttpClient();
        var request = new HttpRequestMessage(HttpMethod.Post, url);
        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("Date", date);
        request.Headers.TryAddWithoutValidation(
            "Authorization",
            $"hmac username=\"{key}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        request.Content = new StringContent(body, Encoding.UTF8, "application/json");

        var response = await client.SendAsync(request);
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
    }
}
```
```php
<?php
$key = "YOUR_MERCHANT_KEY";
$secret = "YOUR_MERCHANT_SALT";
$url = "https://api.payu.in/fems/v1/checkout/detail";

$payload = json_decode('{"requestId":"9920371372_38","transactionDetails":{"amount":8000},"useCase":{"getExtendedPaymentDetails":true}}', true);

$date = gmdate("D, d M Y H:i:s") . " GMT";
$body = json_encode($payload, JSON_UNESCAPED_SLASHES);
$signature = str_pad(hash("sha512", $body . "|" . $date . "|" . $secret), 128, "0", STR_PAD_LEFT);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "accept: application/json",
  "Content-Type: application/json",
  "Date: $date",
  "Authorization: hmac username=\"$key\", algorithm=\"sha512\", headers=\"date\", signature=\"$signature\""
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
</Accordion>
<Accordion title="Get additional charges" icon="fa-code">
Use `getAdditionalCharges` to return the `additionalCharge` configured for each payment option.

> **Note**: Use `getTaxSpecification` if you want to calculate the tax split of additional charges on your end.

```curl
curl -X POST "https://api.payu.in/fems/v1/checkout/detail" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Date: Fri, 24 Jul 2026 05:51:20 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{"requestId":"12345678","transactionDetails":{"amount":12345.12},"useCase":{"getAdditionalCharges":true}}'
```
```python
import hashlib
import json
import requests
from datetime import datetime, timezone

def get_sha512_hash(hash_string):
    return hashlib.sha512(hash_string.encode("utf-8")).hexdigest().zfill(128)

key = "YOUR_MERCHANT_KEY"
secret = "YOUR_MERCHANT_SALT"
url = "https://api.payu.in/fems/v1/checkout/detail"

payload = {'requestId': '12345678',
 'transactionDetails': {'amount': 12345.12},
 'useCase': {'getAdditionalCharges': True}}

date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
body = json.dumps(payload, separators=(",", ":"))
signature = get_sha512_hash(f"{body}|{date}|{secret}")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Date": date,
    "Authorization": (
        f'hmac username="{key}", algorithm="sha512", '
        f'headers="date", signature="{signature}"'
    ),
}

response = requests.post(url, data=body, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```javascript
const crypto = require("crypto");

function getSha512Hash(hashString) {
  return crypto.createHash("sha512").update(hashString).digest("hex").padStart(128, "0");
}

const key = "YOUR_MERCHANT_KEY";
const secret = "YOUR_MERCHANT_SALT";
const url = "https://api.payu.in/fems/v1/checkout/detail";

const payload = {
  "requestId": "12345678",
  "transactionDetails": {
    "amount": 12345.12
  },
  "useCase": {
    "getAdditionalCharges": true
  }
};

const date = new Date().toUTCString();
const body = JSON.stringify(payload);
const signature = getSha512Hash(`${body}|${date}|${secret}`);

async function makeRequest() {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Date": date,
        "Authorization": `hmac username="${key}", algorithm="sha512", headers="date", signature="${signature}"`
      },
      body: body
    });
    const data = await response.text();
    console.log("Status Code:", response.status);
    console.log("Response:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

makeRequest();
```
```java
import java.math.BigInteger;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class CheckoutDetailRequest {
    public static String getSha512Hash(String hashString) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        String hashtext = new BigInteger(1, digest).toString(16);
        return String.format("%128s", hashtext).replace(' ', '0');
    }

    public static void main(String[] args) throws Exception {
        String key = "YOUR_MERCHANT_KEY";
        String secret = "YOUR_MERCHANT_SALT";
        String url = "https://api.payu.in/fems/v1/checkout/detail";

        String requestBodyJson = "{\"requestId\":\"12345678\",\"transactionDetails\":{\"amount\":12345.12},\"useCase\":{\"getAdditionalCharges\":true}}";
        String date = DateTimeFormatter
                .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
                .format(ZonedDateTime.now(ZoneOffset.UTC));
        String hash = getSha512Hash(requestBodyJson + "|" + date + "|" + secret);
        String authorization = "hmac username=\"" + key
                + "\", algorithm=\"sha512\", headers=\"date\", signature=\""
                + hash + "\"";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/json")
                .header("Date", date)
                .header("Authorization", authorization)
                .POST(HttpRequest.BodyPublishers.ofString(requestBodyJson))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var key = "YOUR_MERCHANT_KEY";
        var secret = "YOUR_MERCHANT_SALT";
        var url = "https://api.payu.in/fems/v1/checkout/detail";

        var body = @"{""requestId"":""12345678"",""transactionDetails"":{""amount"":12345.12},""useCase"":{""getAdditionalCharges"":true}}";
        var date = DateTime.UtcNow.ToString("r");
        var hashString = $"{body}|{date}|{secret}";
        var signature = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(hashString)))
            .ToLower()
            .PadLeft(128, '0');

        var client = new HttpClient();
        var request = new HttpRequestMessage(HttpMethod.Post, url);
        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("Date", date);
        request.Headers.TryAddWithoutValidation(
            "Authorization",
            $"hmac username=\"{key}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        request.Content = new StringContent(body, Encoding.UTF8, "application/json");

        var response = await client.SendAsync(request);
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
    }
}
```
```php
<?php
$key = "YOUR_MERCHANT_KEY";
$secret = "YOUR_MERCHANT_SALT";
$url = "https://api.payu.in/fems/v1/checkout/detail";

$payload = json_decode('{"requestId":"12345678","transactionDetails":{"amount":12345.12},"useCase":{"getAdditionalCharges":true}}', true);

$date = gmdate("D, d M Y H:i:s") . " GMT";
$body = json_encode($payload, JSON_UNESCAPED_SLASHES);
$signature = str_pad(hash("sha512", $body . "|" . $date . "|" . $secret), 128, "0", STR_PAD_LEFT);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "accept: application/json",
  "Content-Type: application/json",
  "Date: $date",
  "Authorization: hmac username=\"$key\", algorithm=\"sha512\", headers=\"date\", signature=\"$signature\""
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
</Accordion>
<Accordion title="Get tax specification" icon="fa-code">
Use `getTaxSpecification` to return `configData.taxSpecification`.

```curl
curl -X POST "https://api.payu.in/fems/v1/checkout/detail" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Date: Fri, 24 Jul 2026 05:51:20 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{"requestId":"12345678","transactionDetails":{"amount":12345.12},"useCase":{"getTaxSpecification":true}}'
```
```python
import hashlib
import json
import requests
from datetime import datetime, timezone

def get_sha512_hash(hash_string):
    return hashlib.sha512(hash_string.encode("utf-8")).hexdigest().zfill(128)

key = "YOUR_MERCHANT_KEY"
secret = "YOUR_MERCHANT_SALT"
url = "https://api.payu.in/fems/v1/checkout/detail"

payload = {'requestId': '12345678',
 'transactionDetails': {'amount': 12345.12},
 'useCase': {'getTaxSpecification': True}}

date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
body = json.dumps(payload, separators=(",", ":"))
signature = get_sha512_hash(f"{body}|{date}|{secret}")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Date": date,
    "Authorization": (
        f'hmac username="{key}", algorithm="sha512", '
        f'headers="date", signature="{signature}"'
    ),
}

response = requests.post(url, data=body, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```javascript
const crypto = require("crypto");

function getSha512Hash(hashString) {
  return crypto.createHash("sha512").update(hashString).digest("hex").padStart(128, "0");
}

const key = "YOUR_MERCHANT_KEY";
const secret = "YOUR_MERCHANT_SALT";
const url = "https://api.payu.in/fems/v1/checkout/detail";

const payload = {
  "requestId": "12345678",
  "transactionDetails": {
    "amount": 12345.12
  },
  "useCase": {
    "getTaxSpecification": true
  }
};

const date = new Date().toUTCString();
const body = JSON.stringify(payload);
const signature = getSha512Hash(`${body}|${date}|${secret}`);

async function makeRequest() {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Date": date,
        "Authorization": `hmac username="${key}", algorithm="sha512", headers="date", signature="${signature}"`
      },
      body: body
    });
    const data = await response.text();
    console.log("Status Code:", response.status);
    console.log("Response:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

makeRequest();
```
```java
import java.math.BigInteger;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class CheckoutDetailRequest {
    public static String getSha512Hash(String hashString) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        String hashtext = new BigInteger(1, digest).toString(16);
        return String.format("%128s", hashtext).replace(' ', '0');
    }

    public static void main(String[] args) throws Exception {
        String key = "YOUR_MERCHANT_KEY";
        String secret = "YOUR_MERCHANT_SALT";
        String url = "https://api.payu.in/fems/v1/checkout/detail";

        String requestBodyJson = "{\"requestId\":\"12345678\",\"transactionDetails\":{\"amount\":12345.12},\"useCase\":{\"getTaxSpecification\":true}}";
        String date = DateTimeFormatter
                .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
                .format(ZonedDateTime.now(ZoneOffset.UTC));
        String hash = getSha512Hash(requestBodyJson + "|" + date + "|" + secret);
        String authorization = "hmac username=\"" + key
                + "\", algorithm=\"sha512\", headers=\"date\", signature=\""
                + hash + "\"";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/json")
                .header("Date", date)
                .header("Authorization", authorization)
                .POST(HttpRequest.BodyPublishers.ofString(requestBodyJson))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var key = "YOUR_MERCHANT_KEY";
        var secret = "YOUR_MERCHANT_SALT";
        var url = "https://api.payu.in/fems/v1/checkout/detail";

        var body = @"{""requestId"":""12345678"",""transactionDetails"":{""amount"":12345.12},""useCase"":{""getTaxSpecification"":true}}";
        var date = DateTime.UtcNow.ToString("r");
        var hashString = $"{body}|{date}|{secret}";
        var signature = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(hashString)))
            .ToLower()
            .PadLeft(128, '0');

        var client = new HttpClient();
        var request = new HttpRequestMessage(HttpMethod.Post, url);
        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("Date", date);
        request.Headers.TryAddWithoutValidation(
            "Authorization",
            $"hmac username=\"{key}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        request.Content = new StringContent(body, Encoding.UTF8, "application/json");

        var response = await client.SendAsync(request);
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
    }
}
```
```php
<?php
$key = "YOUR_MERCHANT_KEY";
$secret = "YOUR_MERCHANT_SALT";
$url = "https://api.payu.in/fems/v1/checkout/detail";

$payload = json_decode('{"requestId":"12345678","transactionDetails":{"amount":12345.12},"useCase":{"getTaxSpecification":true}}', true);

$date = gmdate("D, d M Y H:i:s") . " GMT";
$body = json_encode($payload, JSON_UNESCAPED_SLASHES);
$signature = str_pad(hash("sha512", $body . "|" . $date . "|" . $secret), 128, "0", STR_PAD_LEFT);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "accept: application/json",
  "Content-Type: application/json",
  "Date: $date",
  "Authorization: hmac username=\"$key\", algorithm=\"sha512\", headers=\"date\", signature=\"$signature\""
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
</Accordion>
<Accordion title="Check down status" icon="fa-code">
Use `checkDownStatus` to return `downInfo` with issuing-bank and payment-mode downtime lists. Keys in `downInfo` use payment mode category names (for example, `netbanking`), not filter short codes (`nb`).

```curl
curl -X POST "https://api.payu.in/fems/v1/checkout/detail" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Date: Fri, 24 Jul 2026 05:51:20 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{"requestId":"12345678","transactionDetails":{"amount":12345.12},"useCase":{"checkDownStatus":true}}'
```
```python
import hashlib
import json
import requests
from datetime import datetime, timezone

def get_sha512_hash(hash_string):
    return hashlib.sha512(hash_string.encode("utf-8")).hexdigest().zfill(128)

key = "YOUR_MERCHANT_KEY"
secret = "YOUR_MERCHANT_SALT"
url = "https://api.payu.in/fems/v1/checkout/detail"

payload = {'requestId': '12345678',
 'transactionDetails': {'amount': 12345.12},
 'useCase': {'checkDownStatus': True}}

date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
body = json.dumps(payload, separators=(",", ":"))
signature = get_sha512_hash(f"{body}|{date}|{secret}")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Date": date,
    "Authorization": (
        f'hmac username="{key}", algorithm="sha512", '
        f'headers="date", signature="{signature}"'
    ),
}

response = requests.post(url, data=body, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```javascript
const crypto = require("crypto");

function getSha512Hash(hashString) {
  return crypto.createHash("sha512").update(hashString).digest("hex").padStart(128, "0");
}

const key = "YOUR_MERCHANT_KEY";
const secret = "YOUR_MERCHANT_SALT";
const url = "https://api.payu.in/fems/v1/checkout/detail";

const payload = {
  "requestId": "12345678",
  "transactionDetails": {
    "amount": 12345.12
  },
  "useCase": {
    "checkDownStatus": true
  }
};

const date = new Date().toUTCString();
const body = JSON.stringify(payload);
const signature = getSha512Hash(`${body}|${date}|${secret}`);

async function makeRequest() {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Date": date,
        "Authorization": `hmac username="${key}", algorithm="sha512", headers="date", signature="${signature}"`
      },
      body: body
    });
    const data = await response.text();
    console.log("Status Code:", response.status);
    console.log("Response:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

makeRequest();
```
```java
import java.math.BigInteger;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class CheckoutDetailRequest {
    public static String getSha512Hash(String hashString) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        String hashtext = new BigInteger(1, digest).toString(16);
        return String.format("%128s", hashtext).replace(' ', '0');
    }

    public static void main(String[] args) throws Exception {
        String key = "YOUR_MERCHANT_KEY";
        String secret = "YOUR_MERCHANT_SALT";
        String url = "https://api.payu.in/fems/v1/checkout/detail";

        String requestBodyJson = "{\"requestId\":\"12345678\",\"transactionDetails\":{\"amount\":12345.12},\"useCase\":{\"checkDownStatus\":true}}";
        String date = DateTimeFormatter
                .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
                .format(ZonedDateTime.now(ZoneOffset.UTC));
        String hash = getSha512Hash(requestBodyJson + "|" + date + "|" + secret);
        String authorization = "hmac username=\"" + key
                + "\", algorithm=\"sha512\", headers=\"date\", signature=\""
                + hash + "\"";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/json")
                .header("Date", date)
                .header("Authorization", authorization)
                .POST(HttpRequest.BodyPublishers.ofString(requestBodyJson))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var key = "YOUR_MERCHANT_KEY";
        var secret = "YOUR_MERCHANT_SALT";
        var url = "https://api.payu.in/fems/v1/checkout/detail";

        var body = @"{""requestId"":""12345678"",""transactionDetails"":{""amount"":12345.12},""useCase"":{""checkDownStatus"":true}}";
        var date = DateTime.UtcNow.ToString("r");
        var hashString = $"{body}|{date}|{secret}";
        var signature = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(hashString)))
            .ToLower()
            .PadLeft(128, '0');

        var client = new HttpClient();
        var request = new HttpRequestMessage(HttpMethod.Post, url);
        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("Date", date);
        request.Headers.TryAddWithoutValidation(
            "Authorization",
            $"hmac username=\"{key}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        request.Content = new StringContent(body, Encoding.UTF8, "application/json");

        var response = await client.SendAsync(request);
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
    }
}
```
```php
<?php
$key = "YOUR_MERCHANT_KEY";
$secret = "YOUR_MERCHANT_SALT";
$url = "https://api.payu.in/fems/v1/checkout/detail";

$payload = json_decode('{"requestId":"12345678","transactionDetails":{"amount":12345.12},"useCase":{"checkDownStatus":true}}', true);

$date = gmdate("D, d M Y H:i:s") . " GMT";
$body = json_encode($payload, JSON_UNESCAPED_SLASHES);
$signature = str_pad(hash("sha512", $body . "|" . $date . "|" . $secret), 128, "0", STR_PAD_LEFT);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "accept: application/json",
  "Content-Type: application/json",
  "Date: $date",
  "Authorization: hmac username=\"$key\", algorithm=\"sha512\", headers=\"date\", signature=\"$signature\""
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
</Accordion>
<Accordion title="Check customer eligibility" icon="fa-code">
Use `checkCustomerEligibility` to evaluate customer eligibility for EMI and BNPL payment options. `customerDetails.mobile` is required when `checkCustomerEligibility` is true.

```curl
curl -X POST "https://api.payu.in/fems/v1/checkout/detail" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Date: Fri, 24 Jul 2026 05:51:20 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{"requestId":"Test212345","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9368252248"},"useCase":{"checkCustomerEligibility":true,"returnUserLimit":true},"filters":{"paymentOptions":{"emi":{"dc":"all","cc":"all","cardless":"all"},"bnpl":"all"}}}'
```
```python
import hashlib
import json
import requests
from datetime import datetime, timezone

def get_sha512_hash(hash_string):
    return hashlib.sha512(hash_string.encode("utf-8")).hexdigest().zfill(128)

key = "YOUR_MERCHANT_KEY"
secret = "YOUR_MERCHANT_SALT"
url = "https://api.payu.in/fems/v1/checkout/detail"

payload = {'requestId': 'Test212345',
 'transactionDetails': {'amount': 10000},
 'customerDetails': {'mobile': '9368252248'},
 'useCase': {'checkCustomerEligibility': True, 'returnUserLimit': True},
 'filters': {'paymentOptions': {'emi': {'dc': 'all', 'cc': 'all', 'cardless': 'all'},
                                'bnpl': 'all'}}}

date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
body = json.dumps(payload, separators=(",", ":"))
signature = get_sha512_hash(f"{body}|{date}|{secret}")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Date": date,
    "Authorization": (
        f'hmac username="{key}", algorithm="sha512", '
        f'headers="date", signature="{signature}"'
    ),
}

response = requests.post(url, data=body, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```javascript
const crypto = require("crypto");

function getSha512Hash(hashString) {
  return crypto.createHash("sha512").update(hashString).digest("hex").padStart(128, "0");
}

const key = "YOUR_MERCHANT_KEY";
const secret = "YOUR_MERCHANT_SALT";
const url = "https://api.payu.in/fems/v1/checkout/detail";

const payload = {
  "requestId": "Test212345",
  "transactionDetails": {
    "amount": 10000
  },
  "customerDetails": {
    "mobile": "9368252248"
  },
  "useCase": {
    "checkCustomerEligibility": true,
    "returnUserLimit": true
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "dc": "all",
        "cc": "all",
        "cardless": "all"
      },
      "bnpl": "all"
    }
  }
};

const date = new Date().toUTCString();
const body = JSON.stringify(payload);
const signature = getSha512Hash(`${body}|${date}|${secret}`);

async function makeRequest() {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Date": date,
        "Authorization": `hmac username="${key}", algorithm="sha512", headers="date", signature="${signature}"`
      },
      body: body
    });
    const data = await response.text();
    console.log("Status Code:", response.status);
    console.log("Response:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

makeRequest();
```
```java
import java.math.BigInteger;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class CheckoutDetailRequest {
    public static String getSha512Hash(String hashString) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        String hashtext = new BigInteger(1, digest).toString(16);
        return String.format("%128s", hashtext).replace(' ', '0');
    }

    public static void main(String[] args) throws Exception {
        String key = "YOUR_MERCHANT_KEY";
        String secret = "YOUR_MERCHANT_SALT";
        String url = "https://api.payu.in/fems/v1/checkout/detail";

        String requestBodyJson = "{\"requestId\":\"Test212345\",\"transactionDetails\":{\"amount\":10000},\"customerDetails\":{\"mobile\":\"9368252248\"},\"useCase\":{\"checkCustomerEligibility\":true,\"returnUserLimit\":true},\"filters\":{\"paymentOptions\":{\"emi\":{\"dc\":\"all\",\"cc\":\"all\",\"cardless\":\"all\"},\"bnpl\":\"all\"}}}";
        String date = DateTimeFormatter
                .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
                .format(ZonedDateTime.now(ZoneOffset.UTC));
        String hash = getSha512Hash(requestBodyJson + "|" + date + "|" + secret);
        String authorization = "hmac username=\"" + key
                + "\", algorithm=\"sha512\", headers=\"date\", signature=\""
                + hash + "\"";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/json")
                .header("Date", date)
                .header("Authorization", authorization)
                .POST(HttpRequest.BodyPublishers.ofString(requestBodyJson))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var key = "YOUR_MERCHANT_KEY";
        var secret = "YOUR_MERCHANT_SALT";
        var url = "https://api.payu.in/fems/v1/checkout/detail";

        var body = @"{""requestId"":""Test212345"",""transactionDetails"":{""amount"":10000},""customerDetails"":{""mobile"":""9368252248""},""useCase"":{""checkCustomerEligibility"":true,""returnUserLimit"":true},""filters"":{""paymentOptions"":{""emi"":{""dc"":""all"",""cc"":""all"",""cardless"":""all""},""bnpl"":""all""}}}";
        var date = DateTime.UtcNow.ToString("r");
        var hashString = $"{body}|{date}|{secret}";
        var signature = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(hashString)))
            .ToLower()
            .PadLeft(128, '0');

        var client = new HttpClient();
        var request = new HttpRequestMessage(HttpMethod.Post, url);
        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("Date", date);
        request.Headers.TryAddWithoutValidation(
            "Authorization",
            $"hmac username=\"{key}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        request.Content = new StringContent(body, Encoding.UTF8, "application/json");

        var response = await client.SendAsync(request);
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
    }
}
```
```php
<?php
$key = "YOUR_MERCHANT_KEY";
$secret = "YOUR_MERCHANT_SALT";
$url = "https://api.payu.in/fems/v1/checkout/detail";

$payload = json_decode('{"requestId":"Test212345","transactionDetails":{"amount":10000},"customerDetails":{"mobile":"9368252248"},"useCase":{"checkCustomerEligibility":true,"returnUserLimit":true},"filters":{"paymentOptions":{"emi":{"dc":"all","cc":"all","cardless":"all"},"bnpl":"all"}}}', true);

$date = gmdate("D, d M Y H:i:s") . " GMT";
$body = json_encode($payload, JSON_UNESCAPED_SLASHES);
$signature = str_pad(hash("sha512", $body . "|" . $date . "|" . $secret), 128, "0", STR_PAD_LEFT);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "accept: application/json",
  "Content-Type: application/json",
  "Date: $date",
  "Authorization: hmac username=\"$key\", algorithm=\"sha512\", headers=\"date\", signature=\"$signature\""
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
</Accordion>
<Accordion title="Filter EMI options" icon="fa-code">
Use `filters.paymentOptions.emi` to limit EMI banks returned in the response. Use `"all"` (case-insensitive) to include every option in a category. For the full list of EMI bank codes, refer to [EMI Options for Get Checkout Details API](ref:emi-options-for-get-checkout-details-api).

```curl
curl -X POST "https://api.payu.in/fems/v1/checkout/detail" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Date: Fri, 24 Jul 2026 05:51:20 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{"requestId":"4NQD7jcrGCt2LAxB","transactionDetails":{"amount":12386.0},"customerDetails":{"mobile":"9871732405"},"useCase":{"checkCustomerEligibility":true},"filters":{"paymentOptions":{"emi":{"dc":"SBIN,KKBK,ICIC"}}}}'
```
```python
import hashlib
import json
import requests
from datetime import datetime, timezone

def get_sha512_hash(hash_string):
    return hashlib.sha512(hash_string.encode("utf-8")).hexdigest().zfill(128)

key = "YOUR_MERCHANT_KEY"
secret = "YOUR_MERCHANT_SALT"
url = "https://api.payu.in/fems/v1/checkout/detail"

payload = {'requestId': '4NQD7jcrGCt2LAxB',
 'transactionDetails': {'amount': 12386.0},
 'customerDetails': {'mobile': '9871732405'},
 'useCase': {'checkCustomerEligibility': True},
 'filters': {'paymentOptions': {'emi': {'dc': 'SBIN,KKBK,ICIC'}}}}

date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
body = json.dumps(payload, separators=(",", ":"))
signature = get_sha512_hash(f"{body}|{date}|{secret}")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Date": date,
    "Authorization": (
        f'hmac username="{key}", algorithm="sha512", '
        f'headers="date", signature="{signature}"'
    ),
}

response = requests.post(url, data=body, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```javascript
const crypto = require("crypto");

function getSha512Hash(hashString) {
  return crypto.createHash("sha512").update(hashString).digest("hex").padStart(128, "0");
}

const key = "YOUR_MERCHANT_KEY";
const secret = "YOUR_MERCHANT_SALT";
const url = "https://api.payu.in/fems/v1/checkout/detail";

const payload = {
  "requestId": "4NQD7jcrGCt2LAxB",
  "transactionDetails": {
    "amount": 12386.0
  },
  "customerDetails": {
    "mobile": "9871732405"
  },
  "useCase": {
    "checkCustomerEligibility": true
  },
  "filters": {
    "paymentOptions": {
      "emi": {
        "dc": "SBIN,KKBK,ICIC"
      }
    }
  }
};

const date = new Date().toUTCString();
const body = JSON.stringify(payload);
const signature = getSha512Hash(`${body}|${date}|${secret}`);

async function makeRequest() {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Date": date,
        "Authorization": `hmac username="${key}", algorithm="sha512", headers="date", signature="${signature}"`
      },
      body: body
    });
    const data = await response.text();
    console.log("Status Code:", response.status);
    console.log("Response:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

makeRequest();
```
```java
import java.math.BigInteger;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class CheckoutDetailRequest {
    public static String getSha512Hash(String hashString) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        String hashtext = new BigInteger(1, digest).toString(16);
        return String.format("%128s", hashtext).replace(' ', '0');
    }

    public static void main(String[] args) throws Exception {
        String key = "YOUR_MERCHANT_KEY";
        String secret = "YOUR_MERCHANT_SALT";
        String url = "https://api.payu.in/fems/v1/checkout/detail";

        String requestBodyJson = "{\"requestId\":\"4NQD7jcrGCt2LAxB\",\"transactionDetails\":{\"amount\":12386.0},\"customerDetails\":{\"mobile\":\"9871732405\"},\"useCase\":{\"checkCustomerEligibility\":true},\"filters\":{\"paymentOptions\":{\"emi\":{\"dc\":\"SBIN,KKBK,ICIC\"}}}}";
        String date = DateTimeFormatter
                .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
                .format(ZonedDateTime.now(ZoneOffset.UTC));
        String hash = getSha512Hash(requestBodyJson + "|" + date + "|" + secret);
        String authorization = "hmac username=\"" + key
                + "\", algorithm=\"sha512\", headers=\"date\", signature=\""
                + hash + "\"";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/json")
                .header("Date", date)
                .header("Authorization", authorization)
                .POST(HttpRequest.BodyPublishers.ofString(requestBodyJson))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var key = "YOUR_MERCHANT_KEY";
        var secret = "YOUR_MERCHANT_SALT";
        var url = "https://api.payu.in/fems/v1/checkout/detail";

        var body = @"{""requestId"":""4NQD7jcrGCt2LAxB"",""transactionDetails"":{""amount"":12386.0},""customerDetails"":{""mobile"":""9871732405""},""useCase"":{""checkCustomerEligibility"":true},""filters"":{""paymentOptions"":{""emi"":{""dc"":""SBIN,KKBK,ICIC""}}}}";
        var date = DateTime.UtcNow.ToString("r");
        var hashString = $"{body}|{date}|{secret}";
        var signature = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(hashString)))
            .ToLower()
            .PadLeft(128, '0');

        var client = new HttpClient();
        var request = new HttpRequestMessage(HttpMethod.Post, url);
        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("Date", date);
        request.Headers.TryAddWithoutValidation(
            "Authorization",
            $"hmac username=\"{key}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        request.Content = new StringContent(body, Encoding.UTF8, "application/json");

        var response = await client.SendAsync(request);
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
    }
}
```
```php
<?php
$key = "YOUR_MERCHANT_KEY";
$secret = "YOUR_MERCHANT_SALT";
$url = "https://api.payu.in/fems/v1/checkout/detail";

$payload = json_decode('{"requestId":"4NQD7jcrGCt2LAxB","transactionDetails":{"amount":12386.0},"customerDetails":{"mobile":"9871732405"},"useCase":{"checkCustomerEligibility":true},"filters":{"paymentOptions":{"emi":{"dc":"SBIN,KKBK,ICIC"}}}}', true);

$date = gmdate("D, d M Y H:i:s") . " GMT";
$body = json_encode($payload, JSON_UNESCAPED_SLASHES);
$signature = str_pad(hash("sha512", $body . "|" . $date . "|" . $secret), 128, "0", STR_PAD_LEFT);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "accept: application/json",
  "Content-Type: application/json",
  "Date: $date",
  "Authorization: hmac username=\"$key\", algorithm=\"sha512\", headers=\"date\", signature=\"$signature\""
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
</Accordion>
<Accordion title="Get merchant details" icon="fa-code">
Use `getMerchantDetails` to return merchant branding and checkout settings.

```curl
curl -X POST "https://api.payu.in/fems/v1/checkout/detail" \
  -H "accept: application/json" \
  -H "Content-Type: application/json" \
  -H "Date: Fri, 24 Jul 2026 05:51:20 GMT" \
  -H "Authorization: hmac username=\"YOUR_MERCHANT_KEY\", algorithm=\"sha512\", headers=\"date\", signature=\"GENERATED_SIGNATURE\"" \
  -d '{"requestId":"12345678","transactionDetails":{"amount":5000},"useCase":{"getMerchantDetails":true}}'
```
```python
import hashlib
import json
import requests
from datetime import datetime, timezone

def get_sha512_hash(hash_string):
    return hashlib.sha512(hash_string.encode("utf-8")).hexdigest().zfill(128)

key = "YOUR_MERCHANT_KEY"
secret = "YOUR_MERCHANT_SALT"
url = "https://api.payu.in/fems/v1/checkout/detail"

payload = {'requestId': '12345678',
 'transactionDetails': {'amount': 5000},
 'useCase': {'getMerchantDetails': True}}

date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")
body = json.dumps(payload, separators=(",", ":"))
signature = get_sha512_hash(f"{body}|{date}|{secret}")

headers = {
    "accept": "application/json",
    "Content-Type": "application/json",
    "Date": date,
    "Authorization": (
        f'hmac username="{key}", algorithm="sha512", '
        f'headers="date", signature="{signature}"'
    ),
}

response = requests.post(url, data=body, headers=headers)
print("Status Code:", response.status_code)
print("Response:", response.text)
```
```javascript
const crypto = require("crypto");

function getSha512Hash(hashString) {
  return crypto.createHash("sha512").update(hashString).digest("hex").padStart(128, "0");
}

const key = "YOUR_MERCHANT_KEY";
const secret = "YOUR_MERCHANT_SALT";
const url = "https://api.payu.in/fems/v1/checkout/detail";

const payload = {
  "requestId": "12345678",
  "transactionDetails": {
    "amount": 5000
  },
  "useCase": {
    "getMerchantDetails": true
  }
};

const date = new Date().toUTCString();
const body = JSON.stringify(payload);
const signature = getSha512Hash(`${body}|${date}|${secret}`);

async function makeRequest() {
  try {
    const response = await fetch(url, {
      method: "POST",
      headers: {
        "accept": "application/json",
        "Content-Type": "application/json",
        "Date": date,
        "Authorization": `hmac username="${key}", algorithm="sha512", headers="date", signature="${signature}"`
      },
      body: body
    });
    const data = await response.text();
    console.log("Status Code:", response.status);
    console.log("Response:", data);
  } catch (error) {
    console.error("Error:", error);
  }
}

makeRequest();
```
```java
import java.math.BigInteger;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.time.ZoneOffset;
import java.time.ZonedDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Locale;

public class CheckoutDetailRequest {
    public static String getSha512Hash(String hashString) throws Exception {
        MessageDigest md = MessageDigest.getInstance("SHA-512");
        byte[] digest = md.digest(hashString.getBytes(StandardCharsets.UTF_8));
        String hashtext = new BigInteger(1, digest).toString(16);
        return String.format("%128s", hashtext).replace(' ', '0');
    }

    public static void main(String[] args) throws Exception {
        String key = "YOUR_MERCHANT_KEY";
        String secret = "YOUR_MERCHANT_SALT";
        String url = "https://api.payu.in/fems/v1/checkout/detail";

        String requestBodyJson = "{\"requestId\":\"12345678\",\"transactionDetails\":{\"amount\":5000},\"useCase\":{\"getMerchantDetails\":true}}";
        String date = DateTimeFormatter
                .ofPattern("EEE, dd MMM yyyy HH:mm:ss 'GMT'", Locale.ENGLISH)
                .format(ZonedDateTime.now(ZoneOffset.UTC));
        String hash = getSha512Hash(requestBodyJson + "|" + date + "|" + secret);
        String authorization = "hmac username=\"" + key
                + "\", algorithm=\"sha512\", headers=\"date\", signature=\""
                + hash + "\"";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(url))
                .header("accept", "application/json")
                .header("Content-Type", "application/json")
                .header("Date", date)
                .header("Authorization", authorization)
                .POST(HttpRequest.BodyPublishers.ofString(requestBodyJson))
                .build();

        HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println("Status Code: " + response.statusCode());
        System.out.println("Response: " + response.body());
    }
}
```
```csharp
using System;
using System.Net.Http;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        var key = "YOUR_MERCHANT_KEY";
        var secret = "YOUR_MERCHANT_SALT";
        var url = "https://api.payu.in/fems/v1/checkout/detail";

        var body = @"{""requestId"":""12345678"",""transactionDetails"":{""amount"":5000},""useCase"":{""getMerchantDetails"":true}}";
        var date = DateTime.UtcNow.ToString("r");
        var hashString = $"{body}|{date}|{secret}";
        var signature = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(hashString)))
            .ToLower()
            .PadLeft(128, '0');

        var client = new HttpClient();
        var request = new HttpRequestMessage(HttpMethod.Post, url);
        request.Headers.TryAddWithoutValidation("accept", "application/json");
        request.Headers.TryAddWithoutValidation("Date", date);
        request.Headers.TryAddWithoutValidation(
            "Authorization",
            $"hmac username=\"{key}\", algorithm=\"sha512\", headers=\"date\", signature=\"{signature}\"");
        request.Content = new StringContent(body, Encoding.UTF8, "application/json");

        var response = await client.SendAsync(request);
        Console.WriteLine($"Status Code: {(int)response.StatusCode}");
        Console.WriteLine($"Response: {await response.Content.ReadAsStringAsync()}");
    }
}
```
```php
<?php
$key = "YOUR_MERCHANT_KEY";
$secret = "YOUR_MERCHANT_SALT";
$url = "https://api.payu.in/fems/v1/checkout/detail";

$payload = json_decode('{"requestId":"12345678","transactionDetails":{"amount":5000},"useCase":{"getMerchantDetails":true}}', true);

$date = gmdate("D, d M Y H:i:s") . " GMT";
$body = json_encode($payload, JSON_UNESCAPED_SLASHES);
$signature = str_pad(hash("sha512", $body . "|" . $date . "|" . $secret), 128, "0", STR_PAD_LEFT);

$ch = curl_init($url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $body);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
  "accept: application/json",
  "Content-Type: application/json",
  "Date: $date",
  "Authorization: hmac username=\"$key\", algorithm=\"sha512\", headers=\"date\", signature=\"$signature\""
]);

$response = curl_exec($ch);
$httpCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

echo "Status Code: " . $httpCode . "\n";
echo "Response: " . $response . "\n";
?>
```
</Accordion>

## Response parameters

All responses follow a standard envelope:

```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "paymentOption": {},
      "merchant": {},
      "configData": {},
      "downInfo": {},
      "merchantAdditionalInfo": {}
    }
  }
}
```

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| status | `Integer` `1` indicates success. `0` indicates failure. | `1` |
| httpCode | `String` HTTP status code. | `"200"` |
| message | `String` Human-readable message. Empty on success. | `""` |
| data.details | `Object` Checkout details payload. | See sample responses |

### data.details fields

Successful responses return checkout data under `data.details`.

| Parameter | Description |
| --------- | ----------- |
| paymentOption | `Object` Payment modes requested via filters / enabled for the merchant: `emi`, `nb`, `cc`, `dc`, `upi`, `cash`, `bnpl`, `enach`, `si`, `qr`, `sbqr`, etc. |
| merchant | `Object` Merchant branding and checkout settings. Returned when `getMerchantDetails` is true. Omitted when the flag is false. |
| configData | `Object` Tax and SDK configuration. Returned when `getTaxSpecification` is true and/or config data exists. Omitted when neither applies or no data exists. |
| downInfo | `Object` Downtime by payment mode. Returned when `checkDownStatus` is true. Omitted when the flag is false or no downtime exists. |
| merchantAdditionalInfo | `Object` Dynamic Express Checkout merchant parameters. Sibling of `merchant` under `details` (not nested inside `merchant`). Often omitted when no parameters are configured. |
| registeredAmtConvFee | `Object` Convenience fee for registered payment methods (SI flows). |
| recurringAmtConvFee | `Object` Convenience fee for recurring payments (SI flows). |
| si_details | `Object` Standing Instruction configuration. |

### data.details.merchant

Returned when `useCase.getMerchantDetails` is `true`.

| Field | Type | Description |
| ----- | ---- | ----------- |
| logo | `String` / `null` | Merchant logo URL. `null` if not configured. |
| displayName | `String` | Merchant name shown on checkout. |
| retryAllowed | `Integer` | Max payment retry attempts (`0` = no retries). |
| isClevertapActive | `Number` | CleverTap analytics flag (`0` = off, `1` = on). |
| walletIdentifier | `String` / `null` | Wallet identifier for wallet flows. `null` if not configured. |
| enableNewOffersEngine | `Boolean` | Whether the new offers engine is enabled. |
| accentColor | `String` | Checkout theme color (hex). Optional branding field when returned. |
| featureEnforcedOffers | `Boolean` | Offer enforcement enabled. Optional branding field when returned. |
| enableMapMyIndia | `Boolean` | MapMyIndia address lookup enabled. Optional branding field when returned. |
| saveMerchantProvidedAddress | `Boolean` | Save merchant-provided address. Optional branding field when returned. |
| ifscBankNameMapping | `Object` | IFSC-to-bank mapping. Returned when `customerDetails.ifscCodes` is provided. |

#### ifscBankNameMapping value (per IFSC prefix)

| Field | Type | Description |
| ----- | ---- | ----------- |
| name | `String` | Bank display name. |
| ibiboCode | `String` | Net banking `ibiboCode`. |
| imageURL | `String` / `null` | Bank logo URL. |

Example:

```json
{
  "merchant": {
    "logo": null,
    "displayName": "English.bmrc",
    "retryAllowed": 0,
    "isClevertapActive": 0,
    "walletIdentifier": null,
    "enableNewOffersEngine": true
  }
}
```

### data.details.configData

Returned when `getTaxSpecification` is true and/or config data exists.

| Field | Type | Description |
| ----- | ---- | ----------- |
| taxSpecification | `Object` | GST configuration. Returned when `getTaxSpecification` is true. |
| taxSpecification.default | `Integer` | Default GST % on convenience fees (for example, `18`). |
| sdkConfig | `Object` | SDK checkout configuration when present in the response. |

#### sdkConfig fields

| Field | Type | Description |
| ----- | ---- | ----------- |
| isQuickPayEnabled | `Boolean` | Quick Pay (saved instruments) enabled. |
| enable3dsSDK | `Boolean` | 3DS SDK flow enabled. |
| customerRevenueEnabled | `Boolean` | Customer revenue tracking enabled. |
| checkout_timer_duration | `Integer` | Checkout session timer in seconds (`0` = disabled). |
| internationalOn3DSS | `Boolean` | 3D Secure for international cards. |
| isQuickPayBottomSheetEnabled | `Boolean` | Quick Pay bottom sheet UI enabled. |
| pricingShadowMode | `String` | Pricing shadow mode (may be empty). |
| pricingLiveMode | `String` | Pricing live mode (may be empty). |
| preferredUpiApps | `String` / `null` | Preferred UPI apps override. |
| upiSiApps | `String` | Comma-separated UPI apps for standing instruction. |
| enableInternal3DSS | `Boolean` | Internal 3D Secure processing. |
| nfcEnabled | `Boolean` | NFC tap-to-pay enabled. |
| isOfferEnabled | `Boolean` | Offers on SDK checkout. |
| deviceFP | `Boolean` | Device fingerprinting for fraud detection. |
| disabledLoadAndPay | `Integer` | Load & Pay control (`0` = enabled, `1` = disabled). |
| upiApps | `Array` | Supported UPI apps for SDK intent flow. |
| (other keys) | Varies | Additional merchant-specific SDK flags (for example, `3DSSupportedBankList`, `isInsuranceMerchant`, `checkout_timer`, `opgsp_merchant`). |

#### sdkConfig.upiApps[] item

| Field | Type | Description |
| ----- | ---- | ----------- |
| appName | `String` | UPI app identifier (for example, `googlepay`, `phonepe`). |
| handlers | `String` | Comma-separated UPI handles. |
| androidBundleIdentifier | `String` | Android package name for intent launch. |
| iOSSchemaIdentifier | `String` | iOS URI scheme (optional). |

### data.details.downInfo

Returned when `checkDownStatus` is `true` and downtime exists.

Map of downtime categories to affected `ibiboCode` values. Keys use payment mode category names (for example, `netbanking`), not filter short codes (`nb`).

| Key | Type | Description |
| --- | ---- | ----------- |
| issuingBanks | `Array` of `String` | Issuing bank codes with card downtime (for example, `["HSBC", "HDFC"]`). |
| netbanking | `Array` of `String` | Down net banking `ibiboCode` values. |
| emi | `Array` of `String` | Down EMI `ibiboCode` values. |
| creditcard | `Array` of `String` | Down credit card options. |
| debitcard | `Array` of `String` | Down debit card options. |
| upi | `Array` of `String` | Down UPI options. |
| (other modes) | `Array` of `String` | Other payment mode categories with downtime (for example, `cash`, `wallet`). |

Example:

```json
{
  "downInfo": {
    "netbanking": ["BOINB", "JSBNB", "CRPB"]
  }
}
```

### data.details.merchantAdditionalInfo

Dynamic key-value map for Express Checkout merchant parameters. Keys and types vary by merchant — do not hardcode in client integrations.

`merchantAdditionalInfo` is a sibling of `merchant` under `details`, not nested inside `merchant`. Often omitted when no parameters are configured.

| Field | Type | Description |
| ----- | ---- | ----------- |
| (dynamic keys) | `String` / `Boolean` / `Integer` | Merchant-specific Express Checkout parameters (for example, `tags`, `payuVerifiedBadge`, `dynamic_cod_fee`). |

### Non-EMI payment option structure

```json
{
  "nb": {
    "all": {
      "SBIB": {
        "title": "State Bank of India",
        "priority": "1",
        "additionalCharge": 0,
        "pgId": "266",
        "eligibility": { "status": true }
      }
    }
  }
}
```

### EMI payment option structure

```json
{
  "emi": {
    "all": {
      "dc": {
        "hasEligible": true,
        "minimumAmount": 1000,
        "maximumAmount": null,
        "top": ["UTIB", "HDFC"],
        "all": {
          "UTIB": {
            "title": "Axis Bank",
            "shortTitle": "Axis",
            "priority": "100",
            "tenureOptions": {
              "AXISD03": {
                "tenure": 3,
                "interestRate": 13,
                "monthlyEmi": 400.5,
                "interestCharged": 200.45,
                "paybackAmount": 0.0,
                "bankCharge": 0.0,
                "additionalCharge": 13.37,
                "maximumEligibleLimit": 50000,
                "eligibility": { "status": true }
              }
            }
          }
        }
      }
    }
  }
}
```

### eligibility object

| Parameter | Description | Example |
| --------- | ----------- | ------- |
| status | `Boolean` `true` if eligible. | `true` |
| reason | `String` Reason when `status` is `false`. | `"Customer not eligible for EMI"` |

## Sample response

<Accordion title="Get extended payment details" icon="fa-reply">
```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "paymentOption": {
        "emi": {
          "all": {
            "dc": {
              "hasEligible": true,
              "minimumAmount": 1000,
              "maximumAmount": null,
              "all": {
                "UTIB": {
                  "title": "Axis Bank",
                  "shortTitle": "Axis",
                  "priority": "100",
                  "minimumAmount": 1000,
                  "maximumAmount": null,
                  "eligibility": {
                    "status": true
                  },
                  "tenureOptions": {
                    "AXISD03": {
                      "tenure": 3,
                      "interestRate": 13,
                      "interestCharged": 200.45,
                      "monthlyEmi": 400.5,
                      "paybackAmount": 0.0,
                      "bankCharge": 0.0,
                      "minimumAmount": 1000,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  }
                }
              }
            },
            "cc": {
              "...": "..."
            },
            "cardless": {
              "hasEligible": true,
              "all": {
                "ZESTMON": {
                  "title": "Zest Money",
                  "shortTitle": "ZestMoney",
                  "minimumAmount": 1000,
                  "maximumAmount": null,
                  "tenureOptions": {
                    "ZESTMON": {
                      "tenure": null,
                      "minimumAmount": 1000,
                      "maximumAmount": null,
                      "eligibility": {
                        "status": true
                      }
                    }
                  }
                }
              }
            }
          }
        },
        "nb": {
          "all": {
            "SBIB": {
              "title": "State Bank of India",
              "priority": "1"
            }
          }
        },
        "dc": {
          "all": {
            "MAST": {
              "title": "MasterCard Debit Cards",
              "priority": "100"
            }
          }
        },
        "cc": {
          "all": {
            "CC": {
              "title": "Credit Card",
              "priority": "100"
            }
          }
        },
        "cash": {
          "all": {
            "PAYTM": {
              "title": "Paytm",
              "priority": "100"
            }
          }
        }
      }
    }
  }
}
```
</Accordion>
<Accordion title="Get additional charges" icon="fa-reply">
```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "paymentOption": {
        "emi": {
          "all": {
            "dc": {
              "all": {
                "UTIB": {
                  "tenureOptions": {
                    "AXISD03": {
                      "additionalCharge": 13.37
                    }
                  }
                }
              }
            }
          }
        },
        "nb": {
          "all": {
            "SBIB": {
              "additionalCharge": 0
            }
          }
        },
        "dc": {
          "all": {
            "MAST": {
              "additionalCharge": 5.0
            }
          }
        },
        "cc": {
          "all": {
            "CC": {
              "additionalCharge": 5.0
            }
          }
        },
        "cash": {
          "all": {
            "PAYTM": {
              "additionalCharge": 10.5
            }
          }
        }
      }
    }
  }
}
```
</Accordion>
<Accordion title="Get tax specification" icon="fa-reply">
```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "paymentOption": {
        "cc": {
          "...": "..."
        },
        "dc": {
          "...": "..."
        }
      },
      "configData": {
        "taxSpecification": {
          "default": 18
        }
      }
    }
  }
}
```
</Accordion>
<Accordion title="Check down status" icon="fa-reply">
```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "paymentOption": {
        "cc": {
          "...": "..."
        },
        "dc": {
          "...": "..."
        },
        "nb": {
          "...": "..."
        },
        "emi": {
          "...": "..."
        },
        "upi": {
          "...": "..."
        },
        "cash": {
          "...": "..."
        }
      },
      "downInfo": {
        "issuingBanks": [
          "HDFC",
          "AXIS",
          "ICICI"
        ],
        "netbanking": [
          "SBIB",
          "ANDB"
        ],
        "cash": [
          "PAYTM",
          "YESW"
        ]
      }
    }
  }
}
```
</Accordion>
<Accordion title="Check customer eligibility" icon="fa-reply">
```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "paymentOption": {
        "emi": {
          "all": {
            "dc": {
              "all": {
                "KKBK": {
                  "tenureOptions": {
                    "KOTAKD03": {
                      "tenure": 3,
                      "eligibility": {
                        "status": true
                      },
                      "maximumEligibleLimit": 50000
                    }
                  },
                  "eligibility": {
                    "status": true
                  }
                },
                "ICIC": {
                  "tenureOptions": {
                    "ICICID03": {
                      "tenure": 3,
                      "eligibility": {
                        "status": false,
                        "reason": "This mobile number is not eligible. Please change the mobile number."
                      }
                    }
                  },
                  "eligibility": {
                    "status": false,
                    "reason": "Customer not eligible for EMI"
                  }
                }
              },
              "hasEligible": true
            }
          },
          "ntb": {
            "cardless": {
              "...": "..."
            }
          }
        },
        "bnpl": {
          "all": {
            "LAZYPAY": {
              "eligibility": {
                "status": false,
                "reason": "Maximum allowed amount is 5000"
              }
            }
          }
        }
      }
    }
  }
}
```
</Accordion>
<Accordion title="Filter EMI options" icon="fa-reply">
```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "paymentOption": {
        "emi": {
          "all": {
            "dc": {
              "all": {
                "SBIN": {
                  "tenureOptions": {
                    "SBID03": {
                      "tenure": 3,
                      "eligibility": {
                        "status": true
                      }
                    },
                    "SBID18": {
                      "tenure": 18,
                      "eligibility": {
                        "status": false,
                        "reason": "Minimum required amount is 25000"
                      }
                    }
                  },
                  "eligibility": {
                    "status": true
                  }
                }
              },
              "hasEligible": true
            }
          }
        }
      }
    }
  }
}
```
</Accordion>
<Accordion title="Get merchant details" icon="fa-reply">
```json
{
  "status": 1,
  "httpCode": "200",
  "message": "",
  "data": {
    "details": {
      "merchant": {
        "logo": "https://...",
        "displayName": "Merchant Name",
        "retryAllowed": 3,
        "isClevertapActive": 0,
        "walletIdentifier": "WALLET_ID",
        "enableNewOffersEngine": true,
        "accentColor": "#1A73E8",
        "featureEnforcedOffers": false,
        "enableMapMyIndia": true,
        "saveMerchantProvidedAddress": false
      },
      "merchantAdditionalInfo": {
        "tags": "...",
        "payuVerifiedBadge": true
      }
    }
  }
}
```
</Accordion>

## Error responses

Error response example:

```json
{
  "status": 0,
  "httpCode": "400",
  "message": "transactionDetails.amount is mandatory",
  "data": null
}
```

| HTTP Code | Message | Cause |
| --------- | ------- | ----- |
| 401 | Invalid or missing signature | Authorization header is missing, malformed, or signature does not match. |
| 401 | Merchant not allowed to use this API | Merchant is inactive or not permitted. |
| 400 | Bad Request. requestId is mandatory | `requestId` is missing. |
| 400 | Bad Request. requestId cannot be empty | `requestId` is an empty string. |
| 400 | requestId must be alpha-numeric | `requestId` contains invalid characters. |
| 400 | transactionDetails must be an object | `transactionDetails` is null or not an object. |
| 400 | transactionDetails.amount is mandatory | Transaction amount is missing. |
| 400 | customerDetails.mobile must be a valid 10 digit mobile number | Invalid mobile number format. |
| 400 | useCase.checkCustomerEligibility requires customerDetails.mobile field | Eligibility requested without a mobile number. |
| 400 | txnid is already captured for the merchant | Duplicate `transactionDetails.txnId`. |
| 429 | Requests limit reached | Rate limit exceeded. Retry after a short delay. |
| 500 | FAILURE | Internal server error. |