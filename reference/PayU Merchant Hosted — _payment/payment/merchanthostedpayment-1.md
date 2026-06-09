---
api:
  file: Merchant Hosted Checkout.postman_collection_9th_June.json
  operationId: merchantHostedPayment
hidden: true
---
To process payments with credit/debit card, UPI, wallet, etc. on your website using PayU, collect the payment details on your website and submit them to PayU via API. This eliminates the need for redirection to PayU’s payment page, resulting in a more secure and efficient transaction.

<Callout icon="📘" theme="info">
  **Reference**: For an example of how to submit a payment request on your website, refer to [Submitting Payment Request on your Website](doc:submitting-payment-request-on-your-website). To handle redirect URLs (surl and furl), refer to [Handling the Redirect URLs](doc:handling-the-redirect-urls).
</Callout>

|                            |                                                                         |
| :------------------------- | :---------------------------------------------------------------------- |
| **Test Environment**       | \<[https://test.payu.in/\_payment>](https://test.payu.in/_payment>)     |
| **Production Environment** | \<[https://secure.payu.in/\_payment>](https://secure.payu.in/_payment>) |

## Sample Request
<Tabs>
  <Tab title="Net banking">
```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=TESTPG&bankcode=TESTPGNB&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64"
```
```javascript
const url = 'https://test.payu.in/_payment';
const formData = new URLSearchParams();
formData.append('key', 'JP***g');
formData.append('txnid', 'bvRCCBO4YiGGHE');
formData.append('amount', '10.00');
formData.append('firstname', 'Ashish');
formData.append('email', 'test@gmail.com');
formData.append('phone', '9876543210');
formData.append('productinfo', 'iPhone');
formData.append('pg', 'TESTPG');
formData.append('bankcode', 'TESTPGNB');
formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
formData.append('hash', 'ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64');
const requestOptions = { method: 'POST',
  headers: { accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
  body: formData };
fetch(url, requestOptions).then(r => r.text()).then(console.log).catch(console.error);
```

```python
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"
payload = {
        "key": "JP***g",
        "txnid": "bvRCCBO4YiGGHE",
        "amount": "10.00",
        "firstname": "Ashish",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "productinfo": "iPhone",
        "pg": "TESTPG",
        "bankcode": "TESTPGNB",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "hash": "ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64",
}
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST", headers={
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
})
with urllib.request.urlopen(req) as resp:
    print(resp.status, resp.read().decode())
```
```php
<?php
$url = "https://test.payu.in/_payment";
$payload = [
        "key" => "JP***g",
        "txnid" => "bvRCCBO4YiGGHE",
        "amount" => "10.00",
        "firstname" => "Ashish",
        "email" => "test@gmail.com",
        "phone" => "9876543210",
        "productinfo" => "iPhone",
        "pg" => "TESTPG",
        "bankcode" => "TESTPGNB",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        "hash" => "ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64",
];
$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($payload),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded",
    ],
]);
$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo $code, "\n", $response;
```
```java
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.io.*;

String url = "https://test.payu.in/_payment";
byte[] post = "key=JP***g&txnid=bvRCCBO4YiGGHE&amount=10.00&firstname=Ashish&email=test%40gmail.com&phone=9876543210&productinfo=iPhone&pg=TESTPG&bankcode=TESTPGNB&surl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&furl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&hash=ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64".getBytes(StandardCharsets.UTF_8);
HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
c.setRequestMethod("POST");
c.setDoOutput(true);
c.setRequestProperty("accept", "application/json");
c.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
try (OutputStream os = c.getOutputStream()) { os.write(post); }
int code = c.getResponseCode();
try (BufferedReader br = new BufferedReader(new InputStreamReader(
        code >= 400 ? c.getErrorStream() : c.getInputStream(), StandardCharsets.UTF_8))) {
  String line, bodyOut = "";
  while ((line = br.readLine()) != null) bodyOut += line;
  System.out.println(code + " " + bodyOut);
}
```
```csharp
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

var url = "https://test.payu.in/_payment";
var form = new FormUrlEncodedContent(new Dictionary<string, string>
{
        { "key", "JP***g" },
        { "txnid", "bvRCCBO4YiGGHE" },
        { "amount", "10.00" },
        { "firstname", "Ashish" },
        { "email", "test@gmail.com" },
        { "phone", "9876543210" },
        { "productinfo", "iPhone" },
        { "pg", "TESTPG" },
        { "bankcode", "TESTPGNB" },
        { "surl", "https://apiplayground-response.herokuapp.com/" },
        { "furl", "https://apiplayground-response.herokuapp.com/" },
        { "hash", "ad36b3253313753088c662053b043fbe6d7a10112b31fbf20c4b0945b6a70c3a12239c5330ec2d0a0956bcd28a689f08c94fbb9cc2c5e06bb08dc81968672f64" },
});
using var http = new HttpClient();
http.DefaultRequestHeaders.Add("accept", "application/json");
var resp = await http.PostAsync(url, form);
var txt = await resp.Content.ReadAsStringAsync();
System.Console.WriteLine(((int)resp.StatusCode) + " " + txt);
```

  </Tab>
  <Tab title="Cards">
```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304"
```
```javascript
const url = 'https://test.payu.in/_payment';
const formData = new URLSearchParams();
formData.append('key', 'JP***g');
formData.append('txnid', 'EaE4ZO3vU4iPsp');
formData.append('amount', '10.00');
formData.append('firstname', 'Ashish');
formData.append('email', 'test@gmail.com');
formData.append('phone', '9876543210');
formData.append('productinfo', 'iPhone');
formData.append('pg', 'cc');
formData.append('bankcode', 'MAST');
formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
formData.append('ccnum', '5123456789012346');
formData.append('ccexpmon', '05');
formData.append('ccexpyr', '2022');
formData.append('ccvv', '123');
formData.append('ccname', 'undefined');
formData.append('hash', 'fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304');
const requestOptions = { method: 'POST',
  headers: { accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
  body: formData };
fetch(url, requestOptions).then(r => r.text()).then(console.log).catch(console.error);
```
```python
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"
payload = {
        "key": "JP***g",
        "txnid": "EaE4ZO3vU4iPsp",
        "amount": "10.00",
        "firstname": "Ashish",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "productinfo": "iPhone",
        "pg": "cc",
        "bankcode": "MAST",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "ccnum": "5123456789012346",
        "ccexpmon": "05",
        "ccexpyr": "2022",
        "ccvv": "123",
        "ccname": "undefined",
        "hash": "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304",
}
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST", headers={
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
})
with urllib.request.urlopen(req) as resp:
    print(resp.status, resp.read().decode())
```
```php
<?php
$url = "https://test.payu.in/_payment";
$payload = [
        "key" => "JP***g",
        "txnid" => "EaE4ZO3vU4iPsp",
        "amount" => "10.00",
        "firstname" => "Ashish",
        "email" => "test@gmail.com",
        "phone" => "9876543210",
        "productinfo" => "iPhone",
        "pg" => "cc",
        "bankcode" => "MAST",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        "ccnum" => "5123456789012346",
        "ccexpmon" => "05",
        "ccexpyr" => "2022",
        "ccvv" => "123",
        "ccname" => "undefined",
        "hash" => "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304",
];
$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($payload),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded",
    ],
]);
$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo $code, "\n", $response;
```
```java
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.io.*;

String url = "https://test.payu.in/_payment";
byte[] post = "key=JP***g&txnid=EaE4ZO3vU4iPsp&amount=10.00&firstname=Ashish&email=test%40gmail.com&phone=9876543210&productinfo=iPhone&pg=cc&bankcode=MAST&surl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&furl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=undefined&hash=fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304".getBytes(StandardCharsets.UTF_8);
HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
c.setRequestMethod("POST");
c.setDoOutput(true);
c.setRequestProperty("accept", "application/json");
c.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
try (OutputStream os = c.getOutputStream()) { os.write(post); }
int code = c.getResponseCode();
try (BufferedReader br = new BufferedReader(new InputStreamReader(
        code >= 400 ? c.getErrorStream() : c.getInputStream(), StandardCharsets.UTF_8))) {
  String line, bodyOut = "";
  while ((line = br.readLine()) != null) bodyOut += line;
  System.out.println(code + " " + bodyOut);
}
```
```csharp
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

var url = "https://test.payu.in/_payment";
var form = new FormUrlEncodedContent(new Dictionary<string, string>
{
        { "key", "JP***g" },
        { "txnid", "EaE4ZO3vU4iPsp" },
        { "amount", "10.00" },
        { "firstname", "Ashish" },
        { "email", "test@gmail.com" },
        { "phone", "9876543210" },
        { "productinfo", "iPhone" },
        { "pg", "cc" },
        { "bankcode", "MAST" },
        { "surl", "https://apiplayground-response.herokuapp.com/" },
        { "furl", "https://apiplayground-response.herokuapp.com/" },
        { "ccnum", "5123456789012346" },
        { "ccexpmon", "05" },
        { "ccexpyr", "2022" },
        { "ccvv", "123" },
        { "ccname", "undefined" },
        { "hash", "fc3206829a6b4f8e300aeefb8f91add568b83dc90d01383a8e16553cc9600a3aefd4be2e370d32f0315ef1b9f28740515a9556b55abfefa7b54b434f894c9304" },
});
using var http = new HttpClient();
http.DefaultRequestHeaders.Add("accept", "application/json");
var resp = await http.PostAsync(url, form);
var txt = await resp.Content.ReadAsStringAsync();
System.Console.WriteLine(((int)resp.StatusCode) + " " + txt);
```

  </Tab>
  <Tab title="UPI">
```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU+User&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=anything@payu&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=REPLACE_WITH_SERVER_GENERATED_HASH"
```
```javascript
const url = 'https://test.payu.in/_payment';
const formData = new URLSearchParams();
formData.append('key', 'JP***g');
formData.append('txnid', 'xdB9G7qYpfqszo');
formData.append('amount', '10');
formData.append('firstname', 'PayU User');
formData.append('email', 'test@gmail.com');
formData.append('phone', '9876543210');
formData.append('productinfo', 'iPhone');
formData.append('pg', 'UPI');
formData.append('bankcode', 'UPI');
formData.append('vpa', 'anything@payu');
formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
formData.append('hash', 'REPLACE_WITH_SERVER_GENERATED_HASH');
const requestOptions = { method: 'POST',
  headers: { accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
  body: formData };
fetch(url, requestOptions).then(r => r.text()).then(console.log).catch(console.error);
```
```python
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"
payload = {
        "key": "JP***g",
        "txnid": "xdB9G7qYpfqszo",
        "amount": "10",
        "firstname": "PayU User",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "productinfo": "iPhone",
        "pg": "UPI",
        "bankcode": "UPI",
        "vpa": "anything@payu",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "hash": "REPLACE_WITH_SERVER_GENERATED_HASH",
}
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST", headers={
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
})
with urllib.request.urlopen(req) as resp:
    print(resp.status, resp.read().decode())
```
```php
<?php
$url = "https://test.payu.in/_payment";
$payload = [
        "key" => "JP***g",
        "txnid" => "xdB9G7qYpfqszo",
        "amount" => "10",
        "firstname" => "PayU User",
        "email" => "test@gmail.com",
        "phone" => "9876543210",
        "productinfo" => "iPhone",
        "pg" => "UPI",
        "bankcode" => "UPI",
        "vpa" => "anything@payu",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        "hash" => "REPLACE_WITH_SERVER_GENERATED_HASH",
];
$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($payload),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded",
    ],
]);
$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo $code, "\n", $response;
```
```java
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.io.*;

String url = "https://test.payu.in/_payment";
byte[] post = "key=JP***g&txnid=xdB9G7qYpfqszo&amount=10&firstname=PayU+User&email=test%40gmail.com&phone=9876543210&productinfo=iPhone&pg=UPI&bankcode=UPI&vpa=anything%40payu&surl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&furl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&hash=REPLACE_WITH_SERVER_GENERATED_HASH".getBytes(StandardCharsets.UTF_8);
HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
c.setRequestMethod("POST");
c.setDoOutput(true);
c.setRequestProperty("accept", "application/json");
c.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
try (OutputStream os = c.getOutputStream()) { os.write(post); }
int code = c.getResponseCode();
try (BufferedReader br = new BufferedReader(new InputStreamReader(
        code >= 400 ? c.getErrorStream() : c.getInputStream(), StandardCharsets.UTF_8))) {
  String line, bodyOut = "";
  while ((line = br.readLine()) != null) bodyOut += line;
  System.out.println(code + " " + bodyOut);
}
```
```csharp
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

var url = "https://test.payu.in/_payment";
var form = new FormUrlEncodedContent(new Dictionary<string, string>
{
        { "key", "JP***g" },
        { "txnid", "xdB9G7qYpfqszo" },
        { "amount", "10" },
        { "firstname", "PayU User" },
        { "email", "test@gmail.com" },
        { "phone", "9876543210" },
        { "productinfo", "iPhone" },
        { "pg", "UPI" },
        { "bankcode", "UPI" },
        { "vpa", "anything@payu" },
        { "surl", "https://apiplayground-response.herokuapp.com/" },
        { "furl", "https://apiplayground-response.herokuapp.com/" },
        { "hash", "REPLACE_WITH_SERVER_GENERATED_HASH" },
});
using var http = new HttpClient();
http.DefaultRequestHeaders.Add("accept", "application/json");
var resp = await http.PostAsync(url, form);
var txt = await resp.Content.ReadAsStringAsync();
System.Console.WriteLine(((int)resp.StatusCode) + " " + txt);
```

  </Tab>
  <Tab title="Wallets">
```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&productinfo=iPhone&firstname=Ashish&email=test@gmail.com&phone=9876543210&pg=cash&bankcode=paytm&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```
```javascript
const url = 'https://test.payu.in/_payment';
const formData = new URLSearchParams();
formData.append('key', 'J****g');
formData.append('txnid', 'aI1UM19ONxLgPz');
formData.append('amount', '10.00');
formData.append('productinfo', 'iPhone');
formData.append('firstname', 'Ashish');
formData.append('email', 'test@gmail.com');
formData.append('phone', '9876543210');
formData.append('pg', 'cash');
formData.append('bankcode', 'paytm');
formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
formData.append('hash', '6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa');
const requestOptions = { method: 'POST',
  headers: { accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
  body: formData };
fetch(url, requestOptions).then(r => r.text()).then(console.log).catch(console.error);
```
```python
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"
payload = {
        "key": "J****g",
        "txnid": "aI1UM19ONxLgPz",
        "amount": "10.00",
        "productinfo": "iPhone",
        "firstname": "Ashish",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "pg": "cash",
        "bankcode": "paytm",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa",
}
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST", headers={
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
})
with urllib.request.urlopen(req) as resp:
    print(resp.status, resp.read().decode())
```
```php
<?php
$url = "https://test.payu.in/_payment";
$payload = [
        "key" => "J****g",
        "txnid" => "aI1UM19ONxLgPz",
        "amount" => "10.00",
        "productinfo" => "iPhone",
        "firstname" => "Ashish",
        "email" => "test@gmail.com",
        "phone" => "9876543210",
        "pg" => "cash",
        "bankcode" => "paytm",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        "hash" => "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa",
];
$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($payload),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded",
    ],
]);
$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo $code, "\n", $response;
```
```java
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.io.*;

String url = "https://test.payu.in/_payment";
byte[] post = "key=J****g&txnid=aI1UM19ONxLgPz&amount=10.00&productinfo=iPhone&firstname=Ashish&email=test%40gmail.com&phone=9876543210&pg=cash&bankcode=paytm&surl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&furl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa".getBytes(StandardCharsets.UTF_8);
HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
c.setRequestMethod("POST");
c.setDoOutput(true);
c.setRequestProperty("accept", "application/json");
c.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
try (OutputStream os = c.getOutputStream()) { os.write(post); }
int code = c.getResponseCode();
try (BufferedReader br = new BufferedReader(new InputStreamReader(
        code >= 400 ? c.getErrorStream() : c.getInputStream(), StandardCharsets.UTF_8))) {
  String line, bodyOut = "";
  while ((line = br.readLine()) != null) bodyOut += line;
  System.out.println(code + " " + bodyOut);
}
```
```csharp
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

var url = "https://test.payu.in/_payment";
var form = new FormUrlEncodedContent(new Dictionary<string, string>
{
        { "key", "J****g" },
        { "txnid", "aI1UM19ONxLgPz" },
        { "amount", "10.00" },
        { "productinfo", "iPhone" },
        { "firstname", "Ashish" },
        { "email", "test@gmail.com" },
        { "phone", "9876543210" },
        { "pg", "cash" },
        { "bankcode", "paytm" },
        { "surl", "https://apiplayground-response.herokuapp.com/" },
        { "furl", "https://apiplayground-response.herokuapp.com/" },
        { "hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" },
});
using var http = new HttpClient();
http.DefaultRequestHeaders.Add("accept", "application/json");
var resp = await http.PostAsync(url, form);
var txt = await resp.Content.ReadAsStringAsync();
System.Console.WriteLine(((int)resp.StatusCode) + " " + txt);
```

  </Tab>
  <Tab title="EMI">
```curl
curl -X POST "https://test.payu.in/_payment" -H "accept: application/json" -H "Content-Type: application/x-www-form-urlencoded" -d "key=JP***g&txnid=H6mUfE0ccAY94j&amount=20000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=EMI&bankcode=EMIA3&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&ccnum=5123456789012346&ccexpmon=05&ccexpyr=2022&ccvv=123&ccname=&hash=782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
```
```javascript
/**
 * PayU Credit Card EMI Payment Integration using Fetch API
 * 
 * IMPORTANT: This should only be executed server-side (e.g., in Node.js), never in the browser,
 * as it contains sensitive payment information.
 */

// Payment endpoint
const url = 'https://test.payu.in/_payment';

// Form data parameters
const formData = new URLSearchParams();
formData.append('key', 'JP***g');                // Your merchant key
formData.append('txnid', 'H6mUfE0ccAY94j');     // Unique transaction ID
formData.append('amount', '20000.00');          // Payment amount
formData.append('firstname', 'Ashish');         // Customer's name
formData.append('email', 'test@gmail.com');     // Customer's email
formData.append('phone', '9876543210');         // Customer's phone
formData.append('productinfo', 'iPhone');       // Product information
formData.append('pg', 'EMI');                   // Payment gateway (EMI)
formData.append('bankcode', 'EMIA3');           // Bank code (Axis Bank EMI)
formData.append('surl', 'https://apiplayground-response.herokuapp.com/'); // Success URL
formData.append('furl', 'https://apiplayground-response.herokuapp.com/'); // Failure URL
// Card details - SENSITIVE DATA
formData.append('ccnum', '5123456789012346');   // Card number
formData.append('ccexpmon', '05');              // Expiry month
formData.append('ccexpyr', '2022');             // Expiry year 
formData.append('ccvv', '123');                 // CVV
formData.append('ccname', '');                  // Cardholder name
// Security hash
formData.append('hash', '782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36');

// Request options
const requestOptions = {
  method: 'POST',
  headers: {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
  },
  body: formData
};

// Execute the request
fetch(url, requestOptions)
  .then(response => {
    console.log('Status Code:', response.status);
    return response.text(); // or response.json() if you're sure it returns JSON
  })
  .then(data => {
    console.log('Response:', data);
    // Process payment response here, which may include EMI options
  })
  .catch(error => {
    console.error('Error:', error);
  });

```
```python
import urllib.request
import urllib.parse
import json
from typing import Dict, Any

def process_credit_card_emi_payment() -> Dict[str, Any]:
    """
    Process credit card EMI payment using PayU's Merchant Hosted Checkout
    
    IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
    
    Returns:
        Dictionary with response from PayU API
    """
    # API endpoint
    url = "https://test.payu.in/_payment"
    
    # Prepare the form data
    payload = {
        "key": "JP***g",                   # Your merchant key
        "txnid": "H6mUfE0ccAY94j",         # Unique transaction ID
        "amount": "20000.00",              # Payment amount
        "firstname": "Ashish",             # Customer's name
        "email": "test@gmail.com",         # Customer's email
        "phone": "9876543210",             # Customer's phone
        "productinfo": "iPhone",           # Product information
        "pg": "EMI",                       # Payment gateway (EMI)
        "bankcode": "EMIA3",               # Bank code (Axis Bank EMI)
        "surl": "https://apiplayground-response.herokuapp.com/", # Success URL
        "furl": "https://apiplayground-response.herokuapp.com/", # Failure URL
        # Card details - SENSITIVE DATA
        "ccnum": "5123456789012346",       # Card number
        "ccexpmon": "05",                  # Expiry month
        "ccexpyr": "2022",                 # Expiry year
        "ccvv": "123",                     # CVV
        "ccname": "",                      # Cardholder name
        # Security hash
        "hash": "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
    }
    
    # Convert dictionary to URL-encoded form data
    data = urllib.parse.urlencode(payload).encode('utf-8')
    
    # Set headers
    headers = {
        "accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }
    
    # Create a request object
    req = urllib.request.Request(url, data=data, headers=headers, method="POST")
    
    try:
        # Send the request and get the response
        with urllib.request.urlopen(req) as response:
            response_data = response.read().decode('utf-8')
            
            # Process and return response
            return {
                "status_code": response.getcode(),
                "response": response_data
            }
            
    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        error_data = e.read().decode('utf-8')
        return {
            "status_code": e.code,
            "error": e.reason,
            "response": error_data
        }
        
    except Exception as e:
        # Handle other exceptions
        return {
            "status_code": 500,
            "error": str(e),
            "response": "An error occurred during payment processing"
        }

# Example usage
if __name__ == "__main__":
    result = process_credit_card_emi_payment()
    print(f"Status Code: {result['status_code']}")
    if 'error' in result:
        print(f"Error: {result['error']}")
    print(f"Response: {result['response']}")

```
```php
<?php
/**
 * Process credit card EMI payment using PayU's Merchant Hosted Checkout
 * 
 * IMPORTANT: This is a server-side function. Never expose payment details to client-side code.
 * 
 * @return array Response from PayU API
 */
function processCreditCardEmiPayment() {
    // API endpoint
    $url = "https://test.payu.in/_payment";
    
    // Prepare the form data
    $payload = [
        "key" => "JP***g",                    // Your merchant key
        "txnid" => "H6mUfE0ccAY94j",          // Unique transaction ID
        "amount" => "20000.00",               // Payment amount
        "firstname" => "Ashish",              // Customer's name
        "email" => "test@gmail.com",          // Customer's email
        "phone" => "9876543210",              // Customer's phone
        "productinfo" => "iPhone",            // Product information
        "pg" => "EMI",                        // Payment gateway (EMI)
        "bankcode" => "EMIA3",                // Bank code (Axis Bank EMI)
        "surl" => "https://apiplayground-response.herokuapp.com/", // Success URL
        "furl" => "https://apiplayground-response.herokuapp.com/", // Failure URL
        // Card details - SENSITIVE DATA
        "ccnum" => "5123456789012346",        // Card number
        "ccexpmon" => "05",                   // Expiry month
        "ccexpyr" => "2022",                  // Expiry year
        "ccvv" => "123",                      // CVV
        "ccname" => "",                       // Cardholder name
        // Security hash
        "hash" => "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36"
    ];
    
    // Initialize cURL session
    $ch = curl_init($url);
    
    // Set cURL options
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
    curl_setopt($ch, CURLOPT_HTTPHEADER, [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded"
    ]);
    
    // For additional security in production
    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, true);
    curl_setopt($ch, CURLOPT_SSL_VERIFYHOST, 2);
    
    // Execute the request
    $response = curl_exec($ch);
    $statusCode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
    $error = curl_error($ch);
    $errno = curl_errno($ch);
    
    // Close cURL session
    curl_close($ch);
    
    // Handle response
    if ($errno) {
        return [
            "status_code" => 500,
            "error" => $error,
            "response" => "cURL Error: " . $error
        ];
    }
    
    return [
        "status_code" => $statusCode,
        "response" => $response
    ];
}

// Example usage
$result = processCreditCardEmiPayment();
echo "Status Code: " . $result["status_code"] . "\n";
if (isset($result["error"])) {
    echo "Error: " . $result["error"] . "\n";
}
echo "Response: " . $result["response"] . "\n";
?>

```
```java
import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.StringJoiner;

/**
 * PayU Credit Card EMI Payment Processor for Merchant Hosted Checkout
 * 
 * IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
 */
public class PayUCreditCardEmiPaymentProcessor {
    
    // API endpoint
    private static final String PAYU_TEST_URL = "https://test.payu.in/_payment";
    
    /**
     * Process credit card EMI payment through PayU
     * @return PaymentResponse containing status and response data
     */
    public PaymentResponse processCreditCardEmiPayment() {
        try {
            // Initialize URL
            URL url = new URL(PAYU_TEST_URL);
            
            // Prepare form parameters
            Map<String, String> params = new HashMap<>();
            params.put("key", "JP***g");                    // Your merchant key
            params.put("txnid", "H6mUfE0ccAY94j");          // Unique transaction ID
            params.put("amount", "20000.00");               // Payment amount
            params.put("firstname", "Ashish");              // Customer's name
            params.put("email", "test@gmail.com");          // Customer's email
            params.put("phone", "9876543210");              // Customer's phone
            params.put("productinfo", "iPhone");            // Product information
            params.put("pg", "EMI");                        // Payment gateway (EMI)
            params.put("bankcode", "EMIA3");                // Bank code (Axis Bank EMI)
            params.put("surl", "https://apiplayground-response.herokuapp.com/"); // Success URL
            params.put("furl", "https://apiplayground-response.herokuapp.com/"); // Failure URL
            // Card details - SENSITIVE DATA
            params.put("ccnum", "5123456789012346");        // Card number
            params.put("ccexpmon", "05");                   // Expiry month
            params.put("ccexpyr", "2022");                  // Expiry year
            params.put("ccvv", "123");                      // CVV
            params.put("ccname", "");                       // Cardholder name
            // Security hash
            params.put("hash", "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36");
            
            // Convert parameters to URL-encoded form data
            StringJoiner formData = new StringJoiner("&");
            for (Map.Entry<String, String> entry : params.entrySet()) {
                formData.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "=" + 
                             URLEncoder.encode(entry.getValue(), "UTF-8"));
            }
            byte[] postData = formData.toString().getBytes(StandardCharsets.UTF_8);
            
            // Configure connection
            HttpURLConnection conn = (HttpURLConnection) url.openConnection();
            conn.setRequestMethod("POST");
            conn.setRequestProperty("accept", "application/json");
            conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
            conn.setRequestProperty("Content-Length", String.valueOf(postData.length));
            conn.setDoOutput(true);
            conn.setConnectTimeout(5000);
            conn.setReadTimeout(15000);
            
            // Send request
            try (DataOutputStream dos = new DataOutputStream(conn.getOutputStream())) {
                dos.write(postData);
                dos.flush();
            }
            
            // Get response
            int responseCode = conn.getResponseCode();
            
            // Read response data
            StringBuilder response = new StringBuilder();
            try (BufferedReader reader = new BufferedReader(
                    new InputStreamReader(
                        responseCode >= 400 ? conn.getErrorStream() : conn.getInputStream(), 
                        StandardCharsets.UTF_8))) {
                        
                String line;
                while ((line = reader.readLine()) != null) {
                    response.append(line);
                }
            }
            
            return new PaymentResponse(responseCode, response.toString(), null);
            
        } catch (IOException e) {
            // Handle exception
            return new PaymentResponse(500, null, "Error: " + e.getMessage());
        }
    }
    
    /**
     * Payment response wrapper class
     */
    public static class PaymentResponse {
        private final int statusCode;
        private final String response;
        private final String error;
        
        public PaymentResponse(int statusCode, String response, String error) {
            this.statusCode = statusCode;
            this.response = response;
            this.error = error;
        }
        
        public int getStatusCode() {
            return statusCode;
        }
        
        public String getResponse() {
            return response;
        }
        
        public String getError() {
            return error;
        }
        
        public boolean isSuccess() {
            return statusCode >= 200 && statusCode < 300;
        }
    }
    
    // Example usage
    public static void main(String[] args) {
        PayUCreditCardEmiPaymentProcessor processor = new PayUCreditCardEmiPaymentProcessor();
        PaymentResponse result = processor.processCreditCardEmiPayment();
        
        System.out.println("Status Code: " + result.getStatusCode());
        if (result.isSuccess()) {
            System.out.println("Response: " + result.getResponse());
        } else {
            System.out.println("Error: " + result.getError());
        }
    }
}

```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;
using System.Text;

namespace PayUCreditCardEmiIntegration
{
    /// <summary>
    /// PayU Credit Card EMI Payment Processor for Merchant Hosted Checkout
    /// 
    /// IMPORTANT: This is a server-side implementation. Never expose payment details to client-side code.
    /// </summary>
    public class PayUCreditCardEmiPaymentProcessor
    {
        // API endpoint
        private const string PayuTestUrl = "https://test.payu.in/_payment";
        
        /// <summary>
        /// Process credit card EMI payment through PayU
        /// </summary>
        /// <returns>PaymentResponse containing status and response data</returns>
        public async Task<PaymentResponse> ProcessCreditCardEmiPaymentAsync()
        {
            try
            {
                // Prepare form parameters
                var formData = new Dictionary<string, string>
                {
                    { "key", "JP***g" },                     // Your merchant key
                    { "txnid", "H6mUfE0ccAY94j" },           // Unique transaction ID
                    { "amount", "20000.00" },                // Payment amount
                    { "firstname", "Ashish" },               // Customer's name
                    { "email", "test@gmail.com" },           // Customer's email
                    { "phone", "9876543210" },               // Customer's phone
                    { "productinfo", "iPhone" },             // Product information
                    { "pg", "EMI" },                         // Payment gateway (EMI)
                    { "bankcode", "EMIA3" },                 // Bank code (Axis Bank EMI)
                    { "surl", "https://apiplayground-response.herokuapp.com/" }, // Success URL
                    { "furl", "https://apiplayground-response.herokuapp.com/" }, // Failure URL
                    // Card details - SENSITIVE DATA
                    { "ccnum", "5123456789012346" },         // Card number
                    { "ccexpmon", "05" },                    // Expiry month
                    { "ccexpyr", "2022" },                   // Expiry year
                    { "ccvv", "123" },                       // CVV
                    { "ccname", "" },                        // Cardholder name
                    // Security hash
                    { "hash", "782057a8bb0288c858149b4805103befa22041bb3092bc45a813738b43742e31baeae92375be5286a98b44ed66c36121aba0fff6a3170339a4949bc880125d36" }
                };
                
                // Create HttpClient with timeout
                using (var httpClient = new HttpClient())
                {
                    httpClient.Timeout = TimeSpan.FromSeconds(30);
                    
                    // Convert form data to content
                    var content = new FormUrlEncodedContent(formData);
                    
                    // Add headers
                    content.Headers.ContentType = new System.Net.Http.Headers.MediaTypeHeaderValue("application/x-www-form-urlencoded");
                    httpClient.DefaultRequestHeaders.Add("accept", "application/json");
                    
                    // Send POST request
                    var response = await httpClient.PostAsync(PayuTestUrl, content);
                    
                    // Get response content
                    var responseContent = await response.Content.ReadAsStringAsync();
                    
                    return new PaymentResponse(
                        (int)response.StatusCode,
                        responseContent,
                        null
                    );
                }
            }
            catch (Exception ex)
            {
                // Handle exception
                return new PaymentResponse(
                    500,
                    null,
                    $"Error: {ex.Message}"
                );
            }
        }
        
        /// <summary>
        /// Payment response wrapper class
        /// </summary>
        public class PaymentResponse
        {
            public int StatusCode { get; }
            public string Response { get; }
            public string Error { get; }
            
            public PaymentResponse(int statusCode, string response, string error)
            {
                StatusCode = statusCode;
                Response = response;
                Error = error;
            }
            
            public bool IsSuccess => StatusCode >= 200 && StatusCode < 300;
        }
    }
    
    // Example usage
    class Program
    {
        static async Task Main(string[] args)
        {
            var processor = new PayUCreditCardEmiPaymentProcessor();
            var result = await processor.ProcessCreditCardEmiPaymentAsync();
            
            Console.WriteLine($"Status Code: {result.StatusCode}");
            if (result.IsSuccess)
            {
                Console.WriteLine($"Response: {result.Response}");
            }
            else
            {
                Console.WriteLine($"Error: {result.Error}");
            }
        }
    }
}

```

  </Tab>
  <Tab title="BNPL">
```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test@gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https://apiplayground-response.herokuapp.com/&furl=https://apiplayground-response.herokuapp.com/&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa"
```
```javascript
const url = 'https://test.payu.in/_payment';
const formData = new URLSearchParams();
formData.append('key', 'J****g');
formData.append('txnid', '5jJ9xYceXX1ydT');
formData.append('amount', '1000.00');
formData.append('firstname', 'Ashish');
formData.append('email', 'test@gmail.com');
formData.append('phone', '9876543210');
formData.append('productinfo', 'iPhone');
formData.append('pg', 'BNPL');
formData.append('bankcode', 'LAZYPAY');
formData.append('surl', 'https://apiplayground-response.herokuapp.com/');
formData.append('furl', 'https://apiplayground-response.herokuapp.com/');
formData.append('hash', '6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa');
const requestOptions = { method: 'POST',
  headers: { accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
  body: formData };
fetch(url, requestOptions).then(r => r.text()).then(console.log).catch(console.error);
```
```python
import urllib.request
import urllib.parse

url = "https://test.payu.in/_payment"
payload = {
        "key": "J****g",
        "txnid": "5jJ9xYceXX1ydT",
        "amount": "1000.00",
        "firstname": "Ashish",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "productinfo": "iPhone",
        "pg": "BNPL",
        "bankcode": "LAZYPAY",
        "surl": "https://apiplayground-response.herokuapp.com/",
        "furl": "https://apiplayground-response.herokuapp.com/",
        "hash": "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa",
}
data = urllib.parse.urlencode(payload).encode("utf-8")
req = urllib.request.Request(url, data=data, method="POST", headers={
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded",
})
with urllib.request.urlopen(req) as resp:
    print(resp.status, resp.read().decode())
```
```php
<?php
$url = "https://test.payu.in/_payment";
$payload = [
        "key" => "J****g",
        "txnid" => "5jJ9xYceXX1ydT",
        "amount" => "1000.00",
        "firstname" => "Ashish",
        "email" => "test@gmail.com",
        "phone" => "9876543210",
        "productinfo" => "iPhone",
        "pg" => "BNPL",
        "bankcode" => "LAZYPAY",
        "surl" => "https://apiplayground-response.herokuapp.com/",
        "furl" => "https://apiplayground-response.herokuapp.com/",
        "hash" => "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa",
];
$ch = curl_init($url);
curl_setopt_array($ch, [
    CURLOPT_POST => true,
    CURLOPT_POSTFIELDS => http_build_query($payload),
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_HTTPHEADER => [
        "accept: application/json",
        "Content-Type: application/x-www-form-urlencoded",
    ],
]);
$response = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);
echo $code, "\n", $response;
```
```java
import java.net.*;
import java.nio.charset.StandardCharsets;
import java.io.*;

String url = "https://test.payu.in/_payment";
byte[] post = "key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&firstname=Ashish&email=test%40gmail.com&phone=9876543210&productinfo=iPhone&pg=BNPL&bankcode=LAZYPAY&surl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&furl=https%3A%2F%2Fapiplayground-response.herokuapp.com%2F&hash=6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa".getBytes(StandardCharsets.UTF_8);
HttpURLConnection c = (HttpURLConnection) new URL(url).openConnection();
c.setRequestMethod("POST");
c.setDoOutput(true);
c.setRequestProperty("accept", "application/json");
c.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
try (OutputStream os = c.getOutputStream()) { os.write(post); }
int code = c.getResponseCode();
try (BufferedReader br = new BufferedReader(new InputStreamReader(
        code >= 400 ? c.getErrorStream() : c.getInputStream(), StandardCharsets.UTF_8))) {
  String line, bodyOut = "";
  while ((line = br.readLine()) != null) bodyOut += line;
  System.out.println(code + " " + bodyOut);
}
```
```csharp
using System.Net.Http;
using System.Collections.Generic;
using System.Threading.Tasks;

var url = "https://test.payu.in/_payment";
var form = new FormUrlEncodedContent(new Dictionary<string, string>
{
        { "key", "J****g" },
        { "txnid", "5jJ9xYceXX1ydT" },
        { "amount", "1000.00" },
        { "firstname", "Ashish" },
        { "email", "test@gmail.com" },
        { "phone", "9876543210" },
        { "productinfo", "iPhone" },
        { "pg", "BNPL" },
        { "bankcode", "LAZYPAY" },
        { "surl", "https://apiplayground-response.herokuapp.com/" },
        { "furl", "https://apiplayground-response.herokuapp.com/" },
        { "hash", "6840ba0d1a14554f7ee5d20966dfbac6b221718e72dd823f05b6da01420286315b4956c28325898b66520b111604020ea2c547608606674766eb7e4164dc0baa" },
});
using var http = new HttpClient();
http.DefaultRequestHeaders.Add("accept", "application/json");
var resp = await http.PostAsync(url, form);
var txt = await resp.Content.ReadAsStringAsync();
System.Console.WriteLine(((int)resp.StatusCode) + " " + txt);
```

  </Tab>
</Tabs>
## Sample responses

After payment, PayU usually **redirects** the browser to **`surl`** or **`furl`** with a **query-string** body (`key=value&…`). The tabs below all use that **single-line URL / query-string** format (same style as **Cards** and **UPI**). Some integrations receive a **plain/HTML** body instead—treat per your flow. **Always** verify the response **`hash`** using [PayU response hashing](https://docs.payu.in/docs/custom-checkout-merchant-hosted).

<Tabs>
## Sample Response
  <Tab title="Net banking">

Source: [`_payment_merchant_hosted_netbanking.md`](./_payment_merchant_hosted_netbanking.md) — “Sample response” (successful redirect URL / query string).

```plaintext
mihpayid=403993715524046125&mode=NB&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=bvRCCBO4YiGGHE&amount=10.00&discount=0.00&net_amount_debit=10&addedon=2021-09-06+13%3A59%3A39&productinfo=iPhone&firstname=Ashish&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=fa7bb889d25b2a60bcf32316d1c9346589ff3de012dd0c66aa47ec12f1349837163ef8a603bd8b357de610b768f08dc4fb3bb470d2d1ca6d9751300667fd763a6&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=NB-PG&bank_ref_num=ae67e632-f4eb-4121-b47b-2d35dce5ec2e&bankcode=TESTPGNB&error=E000&error_Message=No+Error
```

  </Tab>

  <Tab title="Cards">

Source: [`_payment_merchant_hosted_cards.md`](./_payment_merchant_hosted_cards.md) — “Sample response” → **Normal transaction** (query string). A **parsed JSON** example is on the same page.

```plaintext
mihpayid=403993715531077182&mode=CC&status=success&unmappedstatus=captured&key=JPM7Fg&txnid=ypl938459435dfdfdf&amount=1000.00&cardCategory=domestic&discount=0.00&net_amount_debit=1000&addedon=2024-02-27+15%3A11%3A37&productinfo=iPhone&firstname=Ashish+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=ashish%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=afeab9dcf4e43d47f8fbf5a6838d393c70694a58e30ada08e6cb86ac943236c05717c5f5e4872d671fe81d0d9b2d9facd44e9a061ba621aff6f20c4343ea5dfa&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CC-PG&bank_ref_num=7f0d5ada-59bb-41d7-9e41-20a6af2406c9&bankcode=CC&error=E000&error_Message=No+Error&name_on_card=test&cardnum=411111XXXXXX1111&cardhash=This+field+is+no+longer+supported+in+postback+params.
```

  </Tab>

  <Tab title="UPI">

[`_payment_merchant_hosted_upi.md`](./_payment_merchant_hosted_upi.md) does **not** include a sample response. Below is an **illustrative** success query string in the same shape as other `_payment` redirects (`mode=UPI`, `bankcode=UPI`, `PG_TYPE=UPI-PG`). Replace values with your live postback and **verify `hash`**.

```plaintext
mihpayid=403993715530000001&mode=UPI&status=success&unmappedstatus=captured&key=JP***g&txnid=xdB9G7qYpfqszo&amount=10.00&discount=0.00&net_amount_debit=10&addedon=2024-06-09+12%3A00%3A00&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=REPLACE_WITH_VERIFIED_RESPONSE_HASH&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=UPI-PG&bank_ref_num=00000000-0000-0000-0000-000000000000&bankcode=UPI&error=E000&error_Message=No+Error
```

  </Tab>

  <Tab title="Wallets">

Source: [`_payment_merchant_hosted_wallets.md`](./_payment_merchant_hosted_wallets.md) — “Sample response” accordion, expressed as the **redirect query string** (same field values as the doc’s PHP sample).

```plaintext
mihpayid=403993715527518775&mode=CASH&status=success&unmappedstatus=captured&key=J*****g&txnid=HC13glcAkssIkl&amount=10.00&discount=0.00&net_amount_debit=10&addedon=2022-10-21+17%3A45%3A24&productinfo=iPhone&firstname=Ashish&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=9876543210&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=007435a716982c7f5eec5cff95701f65eb1bdbff8f852e461224e3b5e17126ad26bb3a3ffdb95cded6a87d3515fe86fc58925cad024595a4a6825adfed2dc436&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=CASH-PG&bank_ref_num=540898ed-72e7-40a8-a96e-f17de621cbb4&bankcode=CASH&error=E000&error_Message=No+Error&splitInfo=%7B%22splitStatus%22%3A%22splitNotReceived%22%2C%22splitSegments%22%3A%5B%5D%7D
```

  </Tab>

  <Tab title="EMI">

Source: [`_payment_merchant_hosted_emi.md`](./_payment_merchant_hosted_emi.md) — “Sample response” accordion, expressed as the **redirect query string** (same field values as the doc’s PHP sample; **`mode=EMI`** added for consistency with other modes).

```plaintext
mihpayid=403993715523602563&mode=EMI&status=success&unmappedstatus=captured&key=JP***g&txnid=v2tWbbdUOuacK9&amount=20000.00&discount=0.00&net_amount_debit=20000.00&addedon=2021-07-27+11%3A14%3A44&productinfo=iPhone&firstname=Ashish&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=test%40gmail.com&phone=1234567890&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=10f8ead10cdf5f9b7bf9046987de046d63d62d6679dded9d5da8145f459066943570eec4aa184494ae77f99a8bcd55452af3c4eff0d7a7d3ba809c97b7c73045&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=EMI-PG&bank_ref_num=3d7cc4a4-00c8-4705-a0e7-5708d2c2bb75&bankcode=EMIA3&error=E000&error_Message=No+Error&name_on_card=payu&cardnum=512345XXXXXX2346
```

  </Tab>

  <Tab title="BNPL">

Source: [`_payment_merchant_hosted_bnpl.md`](./_payment_merchant_hosted_bnpl.md) — “Sample Response” accordion; the doc excerpt is short, so the line below completes the usual **redirect query-string** shape to match Cards/UPI (**`hash`** placeholder where the doc omits it).

```plaintext
mihpayid=403993715523409521&mode=BNPL&status=success&unmappedstatus=captured&key=J****g&txnid=5jJ9xYceXX1ydT&amount=1000.00&discount=0.00&net_amount_debit=1000&addedon=2021-07-02+15%3A03%3A50&productinfo=iPhone&firstname=PayU+User&lastname=&address1=&address2=&city=&state=&country=&zipcode=&email=&phone=&udf1=&udf2=&udf3=&udf4=&udf5=&udf6=&udf7=&udf8=&udf9=&udf10=&hash=REPLACE_WITH_VERIFIED_RESPONSE_HASH&field1=&field2=&field3=&field4=&field5=&field6=&field7=&field8=&field9=Transaction+Completed+Successfully&payment_source=payu&PG_TYPE=BNPL-PG&bank_ref_num=&bankcode=LAZYPAY&error=E000&error_Message=No+Error
```

  </Tab>
</Tabs>
