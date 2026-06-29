---
title: Customize PayU Hosted Checkout
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Customize PayU Payment Page or Checkout Page
  description: ''
  robots: index
next:
  description: ''
---
Customize the PayU Hosted Checkout experience by controlling:

- Which payment methods customers can see
- Which payment methods should be hidden
- Which checkout language should be displayed
- Which payment methods should be enabled for your business

Use this guide to reduce payment friction, improve conversion, and tailor checkout to your business needs.

***

# Quickstart

| Goal                                                   | Use This                     |
| ------------------------------------------------------ | ---------------------------- |
| Show only specific payment methods (example: UPI only) | `enforce_paymethod`          |
| Hide specific payment methods (example: wallets)       | `drop_category`              |
| Change checkout language                               | Language parameter           |
| Enable BNPL or other methods                           | PayU Dashboard configuration |

***

# Use Cases

<Accordion title="Common Use Cases" icon="fa-layer-group">
You can use this guide to:

- Show only UPI and cards
- Hide credit cards
- Hide wallets
- Display checkout in other languages
- Enable BNPL for eligible merchants
- Restrict checkout based on business rules
</Accordion>

<br />

***

# Prerequisites

<Accordion title="Checklist" icon="fa-list-check">
Before customizing checkout, ensure you have:

- Active PayU merchant account (test or production)
- API Key and Salt
- Hosted Checkout integration completed
- Merchant eligibility for payment methods you want to use
- Dashboard permissions (for enabling methods)
</Accordion>

<Callout icon="✅" theme="okay">
  ### **Enable Payment Methods**

  Some payment methods (such as BNPL) require PayU approval or merchant eligibility before they appear in checkout. Get in touch with your key account manager to enable them in the dashboard.
</Callout>

***

# Configuration Decision Matrix

Use this decision matrix to choose the correct approach.

| If You Want To                      | Use                      |
| ----------------------------------- | ------------------------ |
| Allow only selected payment methods | Restrict Payment Methods |
| Hide selected payment methods       | Drop Payment Methods     |
| Change language                     | Set Checkout Language    |
| Enable new payment category         | Dashboard Configuration  |

***

# Restrict Checkout to Specific Payment Methods (`enforce_paymethod`)

You can append the parameter names in your transaction request to restrict checkout to some of the payment modes.

Examples:

- Show only UPI
- Show only cards
- Show only UPI + NetBanking

The `enforce_paymethod` parameter allows you to customize payment methods in the checkout. You can restrict specific payment modes, cards scheme, and specific banks under NetBanking using this parameter.

These are the categories, sub-categories and their values you can pass in the `enforce_paymethod` parameter.

| **Category** | **Sub-category**                          | **Value**    |
| ------------ | ----------------------------------------- | ------------ |
| Credit Card  | MasterCard, Amex, Diners, etc.            | `creditcard` |
| Debit Card   | Visa, MasterCard, Maestro, etc.           | `debitcard`  |
| Net Banking  | SBI Net Banking, HDFC Net Banking, etc    | `netbanking` |
| EMI          | CITI 3 Months EMI, HFC 6 Months EMI, etc. | `emi`        |
| Wallet       | Airtel Money, YPay, ITZ, Cash Card, etc.  | `cashcard`   |
| UPI          | GooglePay, PhonePe, UPI, etc.             | `upi`        |
| Sodexo       | N/A                                       | `SODEXO`     |
| BNPL         | N/A                                       | `bnpl`       |
| QR           | N/A                                       | `qr`         |

### How it Works

PayU will show only the payment methods in the checkout you explicitly pass in the request.

### Sample Request

<Tabs>
  <Tab title="With Single Category">

To add a single category, pass the `enforce_paymethod` parameter value with a category mentioned in the table.<br/>
  ```curl
# PayU Hosted Checkout - enforce payment method customization
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=ENFCC001" \
  -d "amount=10.00" \
  -d "firstname=PayU%20User" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "enforce_paymethod=creditcard" \
  -d "hash=REPLACE_WITH_GENERATED_HASH"
# Parameters include key, txnid, amount, surl, furl, hash; enforce_paymethod=creditcard
```
```python
import requests

# PayU Hosted Checkout - enforce payment method customization
# PayU Hosted Checkout Collect Payment API endpoint (test environment)
url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "key": "JP***g",  # Merchant key provided by PayU
    "txnid": "ENFCC001",  # Unique transaction ID generated by merchant
    "amount": "10.00",  # Transaction amount
    "firstname": "PayU User",  # Customer first name
    "email": "test@gmail.com",  # Customer email address
    "phone": "9876543210",  # Customer phone number
    "productinfo": "iPhone",  # Product or order description
    "surl": "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    "furl": "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    "enforce_paymethod": "creditcard",  # Enforce payment method(s): creditcard
    "hash": "REPLACE_WITH_GENERATED_HASH",  # SHA-512 hash generated on server
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // PayU Hosted Checkout - enforce payment method customization
        using var client = new HttpClient();

        var url = "https://test.payu.in/_payment";

        client.DefaultRequestHeaders.Add("accept", "application/json");

        var payload = new Dictionary<string, string>
        {
            { "key", "JP***g" },  // Merchant key provided by PayU
            { "txnid", "ENFCC001" },  // Unique transaction ID generated by merchant
            { "amount", "10.00" },  // Transaction amount
            { "firstname", "PayU User" },  // Customer first name
            { "email", "test@gmail.com" },  // Customer email address
            { "phone", "9876543210" },  // Customer phone number
            { "productinfo", "iPhone" },  // Product or order description
            { "surl", "https://apiplayground-response.herokuapp.com/" },  // Success callback URL
            { "furl", "https://apiplayground-response.herokuapp.com/" },  // Failure callback URL
            { "enforce_paymethod", "creditcard" },  // Enforce payment method(s): creditcard
            { "hash", "REPLACE_WITH_GENERATED_HASH" },  // SHA-512 hash generated on server
        };

        var content = new FormUrlEncodedContent(payload);

        var response = await client.PostAsync(url, content);
        var result = await response.Content.ReadAsStringAsync();

        Console.WriteLine(result);
    }
}
```
```javascript
const axios = require('axios');
const qs = require('querystring');

// PayU Hosted Checkout - enforce payment method customization
// PayU Hosted Checkout Collect Payment API endpoint (test environment)
const url = 'https://test.payu.in/_payment';

const headers = {
  accept: 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
};

const payload = {
  key: 'JP***g',  // Merchant key provided by PayU
  txnid: 'ENFCC001',  // Unique transaction ID generated by merchant
  amount: '10.00',  // Transaction amount
  firstname: 'PayU User',  // Customer first name
  email: 'test@gmail.com',  // Customer email address
  phone: '9876543210',  // Customer phone number
  productinfo: 'iPhone',  // Product or order description
  surl: 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
  furl: 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
  enforce_paymethod: 'creditcard',  // Enforce payment method(s): creditcard
  hash: 'REPLACE_WITH_GENERATED_HASH'  // SHA-512 hash generated on server
};

axios.post(url, qs.stringify(payload), { headers })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayUPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        // PayU Hosted Checkout - enforce payment method customization
        HttpClient client = HttpClient.newHttpClient();

        // Request body: key, txnid, amount, surl, furl, hash; enforce_paymethod=creditcard
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("txnid", "ENFCC001");
        params.put("amount", "10.00");
        params.put("firstname", "PayU User");
        params.put("email", "test@gmail.com");
        params.put("phone", "9876543210");
        params.put("productinfo", "iPhone");
        params.put("surl", "https://apiplayground-response.herokuapp.com/");
        params.put("furl", "https://apiplayground-response.herokuapp.com/");
        params.put("enforce_paymethod", "creditcard");
        params.put("hash", "REPLACE_WITH_GENERATED_HASH");

        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
```
```php
<?php

// PayU Hosted Checkout - enforce payment method customization
$url = "https://test.payu.in/_payment";

$headers = array(
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
);

$payload = array(
    "key" => "JP***g",  // Merchant key provided by PayU
    "txnid" => "ENFCC001",  // Unique transaction ID generated by merchant
    "amount" => "10.00",  // Transaction amount
    "firstname" => "PayU User",  // Customer first name
    "email" => "test@gmail.com",  // Customer email address
    "phone" => "9876543210",  // Customer phone number
    "productinfo" => "iPhone",  // Product or order description
    "surl" => "https://apiplayground-response.herokuapp.com/",  // Success callback URL
    "furl" => "https://apiplayground-response.herokuapp.com/",  // Failure callback URL
    "enforce_paymethod" => "creditcard",  // Enforce payment method(s): creditcard
    "hash" => "REPLACE_WITH_GENERATED_HASH"  // SHA-512 hash generated on server
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

# PayU Hosted Checkout - enforce payment method customization
my $url = "https://test.payu.in/_payment";

my $ua = LWP::UserAgent->new;

my %payload = (
    key               => "JP***g",  # Merchant key provided by PayU
    txnid             => "ENFCC001",  # Unique transaction ID generated by merchant
    amount            => "10.00",  # Transaction amount
    firstname         => "PayU User",  # Customer first name
    email             => "test@gmail.com",  # Customer email address
    phone             => "9876543210",  # Customer phone number
    productinfo       => "iPhone",  # Product or order description
    surl              => "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    furl              => "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    enforce_paymethod => "creditcard",  # Enforce payment method(s): creditcard
    hash              => "REPLACE_WITH_GENERATED_HASH"  # SHA-512 hash generated on server
);

my $response = $ua->post(
    $url,
    accept       => "application/json",
    Content_Type => "application/x-www-form-urlencoded",
    Content      => \%payload
);

print $response->content;
```

  </Tab>

  <Tab title="With Multiple Categories">

To add multiple categories, pass the `enforce_paymethod` parameter value with categories separated by `|` as given in the sample below.<br/>
  ```curl With Multiple Categories
# PayU Hosted Checkout - enforce payment method customization
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=ENFCCDC001" \
  -d "amount=10.00" \
  -d "firstname=PayU%20User" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "enforce_paymethod=creditcard|debitcard" \
  -d "hash=REPLACE_WITH_GENERATED_HASH"
# Parameters include key, txnid, amount, surl, furl, hash; enforce_paymethod=creditcard|debitcard
```
```python
import requests

# PayU Hosted Checkout - enforce payment method customization
# PayU Hosted Checkout Collect Payment API endpoint (test environment)
url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "key": "JP***g",  # Merchant key provided by PayU
    "txnid": "ENFCCDC001",  # Unique transaction ID generated by merchant
    "amount": "10.00",  # Transaction amount
    "firstname": "PayU User",  # Customer first name
    "email": "test@gmail.com",  # Customer email address
    "phone": "9876543210",  # Customer phone number
    "productinfo": "iPhone",  # Product or order description
    "surl": "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    "furl": "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    "enforce_paymethod": "creditcard|debitcard",  # Enforce payment method(s): creditcard|debitcard
    "hash": "REPLACE_WITH_GENERATED_HASH",  # SHA-512 hash generated on server
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // PayU Hosted Checkout - enforce payment method customization
        using var client = new HttpClient();

        var url = "https://test.payu.in/_payment";

        client.DefaultRequestHeaders.Add("accept", "application/json");

        var payload = new Dictionary<string, string>
        {
            { "key", "JP***g" },  // Merchant key provided by PayU
            { "txnid", "ENFCCDC001" },  // Unique transaction ID generated by merchant
            { "amount", "10.00" },  // Transaction amount
            { "firstname", "PayU User" },  // Customer first name
            { "email", "test@gmail.com" },  // Customer email address
            { "phone", "9876543210" },  // Customer phone number
            { "productinfo", "iPhone" },  // Product or order description
            { "surl", "https://apiplayground-response.herokuapp.com/" },  // Success callback URL
            { "furl", "https://apiplayground-response.herokuapp.com/" },  // Failure callback URL
            { "enforce_paymethod", "creditcard|debitcard" },  // Enforce payment method(s): creditcard|debitcard
            { "hash", "REPLACE_WITH_GENERATED_HASH" },  // SHA-512 hash generated on server
        };

        var content = new FormUrlEncodedContent(payload);

        var response = await client.PostAsync(url, content);
        var result = await response.Content.ReadAsStringAsync();

        Console.WriteLine(result);
    }
}
```
```javascript
const axios = require('axios');
const qs = require('querystring');

// PayU Hosted Checkout - enforce payment method customization
// PayU Hosted Checkout Collect Payment API endpoint (test environment)
const url = 'https://test.payu.in/_payment';

const headers = {
  accept: 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
};

const payload = {
  key: 'JP***g',  // Merchant key provided by PayU
  txnid: 'ENFCCDC001',  // Unique transaction ID generated by merchant
  amount: '10.00',  // Transaction amount
  firstname: 'PayU User',  // Customer first name
  email: 'test@gmail.com',  // Customer email address
  phone: '9876543210',  // Customer phone number
  productinfo: 'iPhone',  // Product or order description
  surl: 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
  furl: 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
  enforce_paymethod: 'creditcard|debitcard',  // Enforce payment method(s): creditcard|debitcard
  hash: 'REPLACE_WITH_GENERATED_HASH'  // SHA-512 hash generated on server
};

axios.post(url, qs.stringify(payload), { headers })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayUPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        // PayU Hosted Checkout - enforce payment method customization
        HttpClient client = HttpClient.newHttpClient();

        // Request body: key, txnid, amount, surl, furl, hash; enforce_paymethod=creditcard|debitcard
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("txnid", "ENFCCDC001");
        params.put("amount", "10.00");
        params.put("firstname", "PayU User");
        params.put("email", "test@gmail.com");
        params.put("phone", "9876543210");
        params.put("productinfo", "iPhone");
        params.put("surl", "https://apiplayground-response.herokuapp.com/");
        params.put("furl", "https://apiplayground-response.herokuapp.com/");
        params.put("enforce_paymethod", "creditcard|debitcard");
        params.put("hash", "REPLACE_WITH_GENERATED_HASH");

        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
```
```php
<?php

// PayU Hosted Checkout - enforce payment method customization
$url = "https://test.payu.in/_payment";

$headers = array(
    "accept: application/json",
    "Content-Type: application/x-www-form-urlencoded"
);

$payload = array(
    "key" => "JP***g",  // Merchant key provided by PayU
    "txnid" => "ENFCCDC001",  // Unique transaction ID generated by merchant
    "amount" => "10.00",  // Transaction amount
    "firstname" => "PayU User",  // Customer first name
    "email" => "test@gmail.com",  // Customer email address
    "phone" => "9876543210",  // Customer phone number
    "productinfo" => "iPhone",  // Product or order description
    "surl" => "https://apiplayground-response.herokuapp.com/",  // Success callback URL
    "furl" => "https://apiplayground-response.herokuapp.com/",  // Failure callback URL
    "enforce_paymethod" => "creditcard|debitcard",  // Enforce payment method(s): creditcard|debitcard
    "hash" => "REPLACE_WITH_GENERATED_HASH"  // SHA-512 hash generated on server
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

# PayU Hosted Checkout - enforce payment method customization
my $url = "https://test.payu.in/_payment";

my $ua = LWP::UserAgent->new;

my %payload = (
    key               => "JP***g",  # Merchant key provided by PayU
    txnid             => "ENFCCDC001",  # Unique transaction ID generated by merchant
    amount            => "10.00",  # Transaction amount
    firstname         => "PayU User",  # Customer first name
    email             => "test@gmail.com",  # Customer email address
    phone             => "9876543210",  # Customer phone number
    productinfo       => "iPhone",  # Product or order description
    surl              => "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    furl              => "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    enforce_paymethod => "creditcard|debitcard",  # Enforce payment method(s): creditcard|debitcard
    hash              => "REPLACE_WITH_GENERATED_HASH"  # SHA-512 hash generated on server
);

my $response = $ua->post(
    $url,
    accept       => "application/json",
    Content_Type => "application/x-www-form-urlencoded",
    Content      => \%payload
);

print $response->content;
```
  </Tab>
</Tabs>

Refer to the <Anchor target="_blank" href="https://docs.payu.in/v3.0_pg-web-checkout-restcng-new/docs/integration-guide#step-11-prepare-payment-request-parameters">Step 1.1 Prepare Payment Request Parameters</Anchor> in the **Accept Payments using PayU Hosted Checkout** page for request parameter description.

### Expected Outcome

The categories passed in the `enforce_paymethod` parameter are displayed in the checkout.

### Errors and Troubleshooting

<Accordion title="Payment method not showing" icon="fa-info-circle">
**Possible causes:**
- Invalid method value

- Method not enabled for merchant

- Bank code invalid

- Hash not regenerated
</Accordion>

***

# Hide Specific Payment Methods (`drop_category`)

The `drop_category` parameter allows you to customize payment methods in the checkout. You can hide specific payment methods using this parameter.

These are the categories, sub-categories and their values you can pass in the `drop_category` parameter.

| **Category** | **Sub-category**                          | **Value**    |
| ------------ | ----------------------------------------- | ------------ |
| Credit Card  | MasterCard, Amex, Diners, etc.            | `creditcard` |
| Debit Card   | Visa, MasterCard, Maestro, etc.           | `debitcard`  |
| Net Banking  | SBI Net Banking, HDFC Net Banking, etc    | `netbanking` |
| NEFT/RTGS    | N/A                                       | `NEFTRTGS`   |
| EMI          | CITI 3 Months EMI, HFC 6 Months EMI, etc. | `emi`        |
| Wallet       | Airtel Money, YPay, ITZ, Cash Card, etc.  | `cashcard`   |
| Sodexo       | N/A                                       | `SODEXO`     |
| BNPL         | N/A                                       | `bnpl`       |

### How it Works

PayU will hide the payment methods you passed in the `drop_category` parameter in the checkout.

### Sample Payload

<Tabs>
  <Tab title="Single Payment Method Dropped">
  To drop a single payment, pass the `drop_category` parameter value with a category mentioned in the table.<br/>
```curl
# PayU Hosted Checkout - drop payment category customization
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=DROPCC001" \
  -d "amount=10.00" \
  -d "firstname=PayU%20User" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "drop_category=CC" \
  -d "hash=REPLACE_WITH_GENERATED_HASH"
# Parameters include key, txnid, amount, surl, furl, hash; drop_category=CC
```
```python
import requests

# PayU Hosted Checkout - drop payment category customization
# PayU Hosted Checkout Collect Payment API endpoint (test environment)
url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "key": "JP***g",  # Merchant key provided by PayU
    "txnid": "DROPCC001",  # Unique transaction ID generated by merchant
    "amount": "10.00",  # Transaction amount
    "firstname": "PayU User",  # Customer first name
    "email": "test@gmail.com",  # Customer email address
    "phone": "9876543210",  # Customer phone number
    "productinfo": "iPhone",  # Product or order description
    "surl": "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    "furl": "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    "drop_category": "CC",  # Hide payment category or sub-category: CC
    "hash": "REPLACE_WITH_GENERATED_HASH",  # SHA-512 hash generated on server
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // PayU Hosted Checkout - drop payment category customization
        using var client = new HttpClient();

        var url = "https://test.payu.in/_payment";

        client.DefaultRequestHeaders.Add("accept", "application/json");

        var payload = new Dictionary<string, string>
        {
            { "key", "JP***g" },  // Merchant key provided by PayU
            { "txnid", "DROPCC001" },  // Unique transaction ID generated by merchant
            { "amount", "10.00" },  // Transaction amount
            { "firstname", "PayU User" },  // Customer first name
            { "email", "test@gmail.com" },  // Customer email address
            { "phone", "9876543210" },  // Customer phone number
            { "productinfo", "iPhone" },  // Product or order description
            { "surl", "https://apiplayground-response.herokuapp.com/" },  // Success callback URL
            { "furl", "https://apiplayground-response.herokuapp.com/" },  // Failure callback URL
            { "drop_category", "CC" },  // Hide payment category or sub-category: CC
            { "hash", "REPLACE_WITH_GENERATED_HASH" },  // SHA-512 hash generated on server
        };

        var content = new FormUrlEncodedContent(payload);

        var response = await client.PostAsync(url, content);
        var result = await response.Content.ReadAsStringAsync();

        Console.WriteLine(result);
    }
}
```
```javascript
const axios = require('axios');
const qs = require('querystring');

// PayU Hosted Checkout - drop payment category customization
// PayU Hosted Checkout Collect Payment API endpoint (test environment)
const url = 'https://test.payu.in/_payment';

const headers = {
  accept: 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
};

const payload = {
  key: 'JP***g',  // Merchant key provided by PayU
  txnid: 'DROPCC001',  // Unique transaction ID generated by merchant
  amount: '10.00',  // Transaction amount
  firstname: 'PayU User',  // Customer first name
  email: 'test@gmail.com',  // Customer email address
  phone: '9876543210',  // Customer phone number
  productinfo: 'iPhone',  // Product or order description
  surl: 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
  furl: 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
  drop_category: 'CC',  // Hide payment category or sub-category: CC
  hash: 'REPLACE_WITH_GENERATED_HASH'  // SHA-512 hash generated on server
};

axios.post(url, qs.stringify(payload), { headers })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayUPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        // PayU Hosted Checkout - drop payment category customization
        HttpClient client = HttpClient.newHttpClient();

        // Request body: key, txnid, amount, surl, furl, hash; drop_category=CC
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("txnid", "DROPCC001");
        params.put("amount", "10.00");
        params.put("firstname", "PayU User");
        params.put("email", "test@gmail.com");
        params.put("phone", "9876543210");
        params.put("productinfo", "iPhone");
        params.put("surl", "https://apiplayground-response.herokuapp.com/");
        params.put("furl", "https://apiplayground-response.herokuapp.com/");
        params.put("drop_category", "CC");
        params.put("hash", "REPLACE_WITH_GENERATED_HASH");

        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
```
```php
<?php

// PayU Hosted Checkout - drop payment category customization
$url = 'https://test.payu.in/_payment';

$headers = array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
);

$payload = array(
    'key' => 'JP***g',  // Merchant key provided by PayU
    'txnid' => 'DROPCC001',  // Unique transaction ID generated by merchant
    'amount' => '10.00',  // Transaction amount
    'firstname' => 'PayU User',  // Customer first name
    'email' => 'test@gmail.com',  // Customer email address
    'phone' => '9876543210',  // Customer phone number
    'productinfo' => 'iPhone',  // Product or order description
    'surl' => 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
    'furl' => 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
    'drop_category' => 'CC',  // Hide payment category or sub-category: CC
    'hash' => 'REPLACE_WITH_GENERATED_HASH'  // SHA-512 hash generated on server
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

# PayU Hosted Checkout - drop payment category customization
my $url = 'https://test.payu.in/_payment';

my $ua = LWP::UserAgent->new;

my %payload = (
    key           => 'JP***g',  # Merchant key provided by PayU
    txnid         => 'DROPCC001',  # Unique transaction ID generated by merchant
    amount        => '10.00',  # Transaction amount
    firstname     => 'PayU User',  # Customer first name
    email         => 'test@gmail.com',  # Customer email address
    phone         => '9876543210',  # Customer phone number
    productinfo   => 'iPhone',  # Product or order description
    surl          => 'https://apiplayground-response.herokuapp.com/',  # Success callback URL
    furl          => 'https://apiplayground-response.herokuapp.com/',  # Failure callback URL
    drop_category => 'CC',  # Hide payment category or sub-category: CC
    hash          => 'REPLACE_WITH_GENERATED_HASH'  # SHA-512 hash generated on server
);

my $response = $ua->post(
    $url,
    accept       => 'application/json',
    Content_Type => 'application/x-www-form-urlencoded',
    Content      => \%payload
);

print $response->content;
```
  </Tab>

  <Tab title="Multiple Payment Method Dropped">
To drop multiple payment methods, pass the `drop_category` parameter value with categories separated by `|` as given in the sample below.<br/>
  ```curl
# PayU Hosted Checkout - drop payment category customization
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=DROP2CAT001" \
  -d "amount=10.00" \
  -d "firstname=PayU%20User" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "drop_category=CC|NB" \
  -d "hash=REPLACE_WITH_GENERATED_HASH"
# Parameters include key, txnid, amount, surl, furl, hash; drop_category=CC|NB
```
```python
import requests

# PayU Hosted Checkout - drop payment category customization
# PayU Hosted Checkout Collect Payment API endpoint (test environment)
url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "key": "JP***g",  # Merchant key provided by PayU
    "txnid": "DROP2CAT001",  # Unique transaction ID generated by merchant
    "amount": "10.00",  # Transaction amount
    "firstname": "PayU User",  # Customer first name
    "email": "test@gmail.com",  # Customer email address
    "phone": "9876543210",  # Customer phone number
    "productinfo": "iPhone",  # Product or order description
    "surl": "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    "furl": "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    "drop_category": "CC|NB",  # Hide payment category or sub-category: CC|NB
    "hash": "REPLACE_WITH_GENERATED_HASH",  # SHA-512 hash generated on server
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // PayU Hosted Checkout - drop payment category customization
        using var client = new HttpClient();

        var url = "https://test.payu.in/_payment";

        client.DefaultRequestHeaders.Add("accept", "application/json");

        var payload = new Dictionary<string, string>
        {
            { "key", "JP***g" },  // Merchant key provided by PayU
            { "txnid", "DROP2CAT001" },  // Unique transaction ID generated by merchant
            { "amount", "10.00" },  // Transaction amount
            { "firstname", "PayU User" },  // Customer first name
            { "email", "test@gmail.com" },  // Customer email address
            { "phone", "9876543210" },  // Customer phone number
            { "productinfo", "iPhone" },  // Product or order description
            { "surl", "https://apiplayground-response.herokuapp.com/" },  // Success callback URL
            { "furl", "https://apiplayground-response.herokuapp.com/" },  // Failure callback URL
            { "drop_category", "CC|NB" },  // Hide payment category or sub-category: CC|NB
            { "hash", "REPLACE_WITH_GENERATED_HASH" },  // SHA-512 hash generated on server
        };

        var content = new FormUrlEncodedContent(payload);

        var response = await client.PostAsync(url, content);
        var result = await response.Content.ReadAsStringAsync();

        Console.WriteLine(result);
    }
}
```
```javascript
const axios = require('axios');
const qs = require('querystring');

// PayU Hosted Checkout - drop payment category customization
// PayU Hosted Checkout Collect Payment API endpoint (test environment)
const url = 'https://test.payu.in/_payment';

const headers = {
  accept: 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
};

const payload = {
  key: 'JP***g',  // Merchant key provided by PayU
  txnid: 'DROP2CAT001',  // Unique transaction ID generated by merchant
  amount: '10.00',  // Transaction amount
  firstname: 'PayU User',  // Customer first name
  email: 'test@gmail.com',  // Customer email address
  phone: '9876543210',  // Customer phone number
  productinfo: 'iPhone',  // Product or order description
  surl: 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
  furl: 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
  drop_category: 'CC|NB',  // Hide payment category or sub-category: CC|NB
  hash: 'REPLACE_WITH_GENERATED_HASH'  // SHA-512 hash generated on server
};

axios.post(url, qs.stringify(payload), { headers })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayUPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        // PayU Hosted Checkout - drop payment category customization
        HttpClient client = HttpClient.newHttpClient();

        // Request body: key, txnid, amount, surl, furl, hash; drop_category=CC|NB
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("txnid", "DROP2CAT001");
        params.put("amount", "10.00");
        params.put("firstname", "PayU User");
        params.put("email", "test@gmail.com");
        params.put("phone", "9876543210");
        params.put("productinfo", "iPhone");
        params.put("surl", "https://apiplayground-response.herokuapp.com/");
        params.put("furl", "https://apiplayground-response.herokuapp.com/");
        params.put("drop_category", "CC|NB");
        params.put("hash", "REPLACE_WITH_GENERATED_HASH");

        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
```
```php
<?php

// PayU Hosted Checkout - drop payment category customization
$url = 'https://test.payu.in/_payment';

$headers = array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
);

$payload = array(
    'key' => 'JP***g',  // Merchant key provided by PayU
    'txnid' => 'DROP2CAT001',  // Unique transaction ID generated by merchant
    'amount' => '10.00',  // Transaction amount
    'firstname' => 'PayU User',  // Customer first name
    'email' => 'test@gmail.com',  // Customer email address
    'phone' => '9876543210',  // Customer phone number
    'productinfo' => 'iPhone',  // Product or order description
    'surl' => 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
    'furl' => 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
    'drop_category' => 'CC|NB',  // Hide payment category or sub-category: CC|NB
    'hash' => 'REPLACE_WITH_GENERATED_HASH'  // SHA-512 hash generated on server
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

# PayU Hosted Checkout - drop payment category customization
my $url = 'https://test.payu.in/_payment';

my $ua = LWP::UserAgent->new;

my %payload = (
    key           => 'JP***g',  # Merchant key provided by PayU
    txnid         => 'DROP2CAT001',  # Unique transaction ID generated by merchant
    amount        => '10.00',  # Transaction amount
    firstname     => 'PayU User',  # Customer first name
    email         => 'test@gmail.com',  # Customer email address
    phone         => '9876543210',  # Customer phone number
    productinfo   => 'iPhone',  # Product or order description
    surl          => 'https://apiplayground-response.herokuapp.com/',  # Success callback URL
    furl          => 'https://apiplayground-response.herokuapp.com/',  # Failure callback URL
    drop_category => 'CC|NB',  # Hide payment category or sub-category: CC|NB
    hash          => 'REPLACE_WITH_GENERATED_HASH'  # SHA-512 hash generated on server
);

my $response = $ua->post(
    $url,
    accept       => 'application/json',
    Content_Type => 'application/x-www-form-urlencoded',
    Content      => \%payload
);

print $response->content;
```
  </Tab>
</Tabs>

Refer to the <Anchor target="_blank" href="https://docs.payu.in/v3.0_pg-web-checkout-restcng-new/docs/integration-guide#step-11-prepare-payment-request-parameters">Step 1.1 Prepare Payment Request Parameters</Anchor> in the **Accept Payments using PayU Hosted Checkout** page for request parameter description.

### Expected Outcome

The categories passed in the `drop_category` parameter are hidden or not displayed in the checkout.

### Errors and Troubleshooting

<Accordion title="Method still visible" icon="fa-info-circle">
**Possible causes:**
- Invalid category

- Drop parameter not passed

- Conflicting rules

- Merchant-level override
</Accordion>

***

# Set Checkout Display Language

The `display_lang` parameter allows you to change the display language of the PayU Hosted Checkout. These are the supported language values:

- `English`
- `Hindi`
- `Kannada`
- `Telugu`
- `Tamil`
- `Gujarati`
- `Marathi`&#x20;

### Video Tutorial

Go through this video to know how vernacular support can improve your business:

<Embed title="" typeOfEmbed="youtube" url="https://www.youtube.com/watch?v=7UCT0jFbB90" href="https://www.youtube.com/watch?v=7UCT0jFbB90" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252F7UCT0jFbB90%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253D7UCT0jFbB90%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252F7UCT0jFbB90%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%3B%20encrypted-media%3B%20picture-in-picture%3B%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />

### How it Works

The PayU hosted checkout is displayed in the language specified in the request as shown below in the screenshot.


<Image src="https://files.readme.io/3aae0ef-hindipage.png" align="center" caption="_PayU Hosted Checkout in Hindi_" framed={true} />


### Sample Payload

<Tabs>
  <Tab title="Sample Request">
  ```curl
# PayU Hosted Checkout - set checkout display language
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=PQI6MqpYrjEefU" \
  -d "amount=10.00" \
  -d "firstname=PayU User" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "display_lang=Hindi" \
  -d "hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
# Parameters include key, txnid, amount, surl, furl, hash; display_lang=Hindi
```
```python
import requests

# PayU Hosted Checkout - set checkout display language
# PayU Hosted Checkout Collect Payment API endpoint (test environment)
url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "key": "JP***g",  # Merchant key provided by PayU
    "txnid": "PQI6MqpYrjEefU",  # Unique transaction ID generated by merchant
    "amount": "10.00",  # Transaction amount
    "firstname": "PayU User",  # Customer first name
    "email": "test@gmail.com",  # Customer email address
    "phone": "9876543210",  # Customer phone number
    "productinfo": "iPhone",  # Product or order description
    "surl": "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    "furl": "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    "display_lang": "Hindi",  # Display checkout page in Hindi
    "hash": "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072",  # SHA-512 hash generated on server
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // PayU Hosted Checkout - set checkout display language
        using var client = new HttpClient();

        var url = "https://test.payu.in/_payment";

        client.DefaultRequestHeaders.Add("accept", "application/json");

        var payload = new Dictionary<string, string>
        {
            { "key", "JP***g" },  // Merchant key provided by PayU
            { "txnid", "PQI6MqpYrjEefU" },  // Unique transaction ID generated by merchant
            { "amount", "10.00" },  // Transaction amount
            { "firstname", "PayU User" },  // Customer first name
            { "email", "test@gmail.com" },  // Customer email address
            { "phone", "9876543210" },  // Customer phone number
            { "productinfo", "iPhone" },  // Product or order description
            { "surl", "https://apiplayground-response.herokuapp.com/" },  // Success callback URL
            { "furl", "https://apiplayground-response.herokuapp.com/" },  // Failure callback URL
            { "display_lang", "Hindi" },  // Display checkout page in Hindi
            { "hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072" },  // SHA-512 hash generated on server
        };

        var content = new FormUrlEncodedContent(payload);

        var response = await client.PostAsync(url, content);
        var result = await response.Content.ReadAsStringAsync();

        Console.WriteLine(result);
    }
}
```
```javascript
const axios = require('axios');
const qs = require('querystring');

// PayU Hosted Checkout - set checkout display language
// PayU Hosted Checkout Collect Payment API endpoint (test environment)
const url = 'https://test.payu.in/_payment';

const headers = {
  accept: 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
};

const payload = {
  key: 'JP***g',  // Merchant key provided by PayU
  txnid: 'PQI6MqpYrjEefU',  // Unique transaction ID generated by merchant
  amount: '10.00',  // Transaction amount
  firstname: 'PayU User',  // Customer first name
  email: 'test@gmail.com',  // Customer email address
  phone: '9876543210',  // Customer phone number
  productinfo: 'iPhone',  // Product or order description
  surl: 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
  furl: 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
  display_lang: 'Hindi',  // Display checkout page in Hindi
  hash: '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'  // SHA-512 hash generated on server
};

axios.post(url, qs.stringify(payload), { headers })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayUPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        // PayU Hosted Checkout - set checkout display language
        HttpClient client = HttpClient.newHttpClient();

        // Request body: key, txnid, amount, surl, furl, hash; display_lang=Hindi
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("txnid", "PQI6MqpYrjEefU");
        params.put("amount", "10.00");
        params.put("firstname", "PayU User");
        params.put("email", "test@gmail.com");
        params.put("phone", "9876543210");
        params.put("productinfo", "iPhone");
        params.put("surl", "https://apiplayground-response.herokuapp.com/");
        params.put("furl", "https://apiplayground-response.herokuapp.com/");
        params.put("display_lang", "Hindi");
        params.put("hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072");

        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
```
```php
<?php

// PayU Hosted Checkout - set checkout display language
$url = 'https://test.payu.in/_payment';

$headers = array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
);

$payload = array(
    'key' => 'JP***g',  // Merchant key provided by PayU
    'txnid' => 'PQI6MqpYrjEefU',  // Unique transaction ID generated by merchant
    'amount' => '10.00',  // Transaction amount
    'firstname' => 'PayU User',  // Customer first name
    'email' => 'test@gmail.com',  // Customer email address
    'phone' => '9876543210',  // Customer phone number
    'productinfo' => 'iPhone',  // Product or order description
    'surl' => 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
    'furl' => 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
    'display_lang' => 'Hindi',  // Display checkout page in Hindi
    'hash' => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'  // SHA-512 hash generated on server
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

# PayU Hosted Checkout - set checkout display language
my $url = 'https://test.payu.in/_payment';

my $ua = LWP::UserAgent->new;

my %payload = (
    key          => 'JP***g',  # Merchant key provided by PayU
    txnid        => 'PQI6MqpYrjEefU',  # Unique transaction ID generated by merchant
    amount       => '10.00',  # Transaction amount
    firstname    => 'PayU User',  # Customer first name
    email        => 'test@gmail.com',  # Customer email address
    phone        => '9876543210',  # Customer phone number
    productinfo  => 'iPhone',  # Product or order description
    surl         => 'https://apiplayground-response.herokuapp.com/',  # Success callback URL
    furl         => 'https://apiplayground-response.herokuapp.com/',  # Failure callback URL
    display_lang => 'Hindi',  # Display checkout page in Hindi
    hash         => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'  # SHA-512 hash generated on server
);

my $response = $ua->post(
    $url,
    accept       => 'application/json',
    Content_Type => 'application/x-www-form-urlencoded',
    Content      => \%payload
);

print $response->content;
```
  </Tab>
</Tabs>

***

```curl
# PayU Hosted Checkout - set checkout display language
curl -X POST "https://test.payu.in/_payment" \
  -H "accept: application/json" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=JP***g" \
  -d "txnid=PQI6MqpYrjEefU" \
  -d "amount=10.00" \
  -d "firstname=PayU User" \
  -d "email=test@gmail.com" \
  -d "phone=9876543210" \
  -d "productinfo=iPhone" \
  -d "surl=https://apiplayground-response.herokuapp.com/" \
  -d "furl=https://apiplayground-response.herokuapp.com/" \
  -d "display_lang=Hindi" \
  -d "hash=05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072"
# Parameters include key, txnid, amount, surl, furl, hash; display_lang=Hindi
```
```python
import requests

# PayU Hosted Checkout - set checkout display language
# PayU Hosted Checkout Collect Payment API endpoint (test environment)
url = "https://test.payu.in/_payment"

headers = {
    "accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded"
}

payload = {
    "key": "JP***g",  # Merchant key provided by PayU
    "txnid": "PQI6MqpYrjEefU",  # Unique transaction ID generated by merchant
    "amount": "10.00",  # Transaction amount
    "firstname": "PayU User",  # Customer first name
    "email": "test@gmail.com",  # Customer email address
    "phone": "9876543210",  # Customer phone number
    "productinfo": "iPhone",  # Product or order description
    "surl": "https://apiplayground-response.herokuapp.com/",  # Success callback URL
    "furl": "https://apiplayground-response.herokuapp.com/",  # Failure callback URL
    "display_lang": "Hindi",  # Display checkout page in Hindi
    "hash": "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072",  # SHA-512 hash generated on server
}

response = requests.post(url, headers=headers, data=payload)
print(response.text)
```
```csharp
using System;
using System.Collections.Generic;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        // PayU Hosted Checkout - set checkout display language
        using var client = new HttpClient();

        var url = "https://test.payu.in/_payment";

        client.DefaultRequestHeaders.Add("accept", "application/json");

        var payload = new Dictionary<string, string>
        {
            { "key", "JP***g" },  // Merchant key provided by PayU
            { "txnid", "PQI6MqpYrjEefU" },  // Unique transaction ID generated by merchant
            { "amount", "10.00" },  // Transaction amount
            { "firstname", "PayU User" },  // Customer first name
            { "email", "test@gmail.com" },  // Customer email address
            { "phone", "9876543210" },  // Customer phone number
            { "productinfo", "iPhone" },  // Product or order description
            { "surl", "https://apiplayground-response.herokuapp.com/" },  // Success callback URL
            { "furl", "https://apiplayground-response.herokuapp.com/" },  // Failure callback URL
            { "display_lang", "Hindi" },  // Display checkout page in Hindi
            { "hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072" },  // SHA-512 hash generated on server
        };

        var content = new FormUrlEncodedContent(payload);

        var response = await client.PostAsync(url, content);
        var result = await response.Content.ReadAsStringAsync();

        Console.WriteLine(result);
    }
}
```
```javascript
const axios = require('axios');
const qs = require('querystring');

// PayU Hosted Checkout - set checkout display language
// PayU Hosted Checkout Collect Payment API endpoint (test environment)
const url = 'https://test.payu.in/_payment';

const headers = {
  accept: 'application/json',
  'Content-Type': 'application/x-www-form-urlencoded'
};

const payload = {
  key: 'JP***g',  // Merchant key provided by PayU
  txnid: 'PQI6MqpYrjEefU',  // Unique transaction ID generated by merchant
  amount: '10.00',  // Transaction amount
  firstname: 'PayU User',  // Customer first name
  email: 'test@gmail.com',  // Customer email address
  phone: '9876543210',  // Customer phone number
  productinfo: 'iPhone',  // Product or order description
  surl: 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
  furl: 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
  display_lang: 'Hindi',  // Display checkout page in Hindi
  hash: '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'  // SHA-512 hash generated on server
};

axios.post(url, qs.stringify(payload), { headers })
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    console.error(error);
  });
```
```java
import java.io.IOException;
import java.net.URI;
import java.net.URLEncoder;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;

public class PayUPayment {
    public static void main(String[] args) throws IOException, InterruptedException {
        // PayU Hosted Checkout - set checkout display language
        HttpClient client = HttpClient.newHttpClient();

        // Request body: key, txnid, amount, surl, furl, hash; display_lang=Hindi
        Map<String, String> params = new HashMap<>();
        params.put("key", "JP***g");
        params.put("txnid", "PQI6MqpYrjEefU");
        params.put("amount", "10.00");
        params.put("firstname", "PayU User");
        params.put("email", "test@gmail.com");
        params.put("phone", "9876543210");
        params.put("productinfo", "iPhone");
        params.put("surl", "https://apiplayground-response.herokuapp.com/");
        params.put("furl", "https://apiplayground-response.herokuapp.com/");
        params.put("display_lang", "Hindi");
        params.put("hash", "05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072");

        String formData = params.entrySet().stream()
            .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "="
                    + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
            .collect(Collectors.joining("&"));

        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("https://test.payu.in/_payment"))
            .header("accept", "application/json")
            .header("Content-Type", "application/x-www-form-urlencoded")
            .POST(HttpRequest.BodyPublishers.ofString(formData))
            .build();

        HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

        System.out.println(response.body());
    }
}
```
```php
<?php

// PayU Hosted Checkout - set checkout display language
$url = 'https://test.payu.in/_payment';

$headers = array(
    'accept: application/json',
    'Content-Type: application/x-www-form-urlencoded'
);

$payload = array(
    'key' => 'JP***g',  // Merchant key provided by PayU
    'txnid' => 'PQI6MqpYrjEefU',  // Unique transaction ID generated by merchant
    'amount' => '10.00',  // Transaction amount
    'firstname' => 'PayU User',  // Customer first name
    'email' => 'test@gmail.com',  // Customer email address
    'phone' => '9876543210',  // Customer phone number
    'productinfo' => 'iPhone',  // Product or order description
    'surl' => 'https://apiplayground-response.herokuapp.com/',  // Success callback URL
    'furl' => 'https://apiplayground-response.herokuapp.com/',  // Failure callback URL
    'display_lang' => 'Hindi',  // Display checkout page in Hindi
    'hash' => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'  // SHA-512 hash generated on server
);

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_POST, 1);
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

$response = curl_exec($ch);
curl_close($ch);

echo $response;
?>
```
```perl
#!/usr/bin/perl
use strict;
use warnings;
use LWP::UserAgent;
use HTTP::Request::Common;

# PayU Hosted Checkout - set checkout display language
my $url = 'https://test.payu.in/_payment';

my $ua = LWP::UserAgent->new;

my %payload = (
    key          => 'JP***g',  # Merchant key provided by PayU
    txnid        => 'PQI6MqpYrjEefU',  # Unique transaction ID generated by merchant
    amount       => '10.00',  # Transaction amount
    firstname    => 'PayU User',  # Customer first name
    email        => 'test@gmail.com',  # Customer email address
    phone        => '9876543210',  # Customer phone number
    productinfo  => 'iPhone',  # Product or order description
    surl         => 'https://apiplayground-response.herokuapp.com/',  # Success callback URL
    furl         => 'https://apiplayground-response.herokuapp.com/',  # Failure callback URL
    display_lang => 'Hindi',  # Display checkout page in Hindi
    hash         => '05a397501918ec5c36ae52daa3b3e49b43e986b86940e109d060076e467c3ea7536617df7420e0e6863dced8c5b45f9fff15c13bdf0335512c05f0210b31b072'  # SHA-512 hash generated on server
);

my $response = $ua->post(
    $url,
    accept       => 'application/json',
    Content_Type => 'application/x-www-form-urlencoded',
    Content      => \%payload
);

print $response->content;
```

## Example: Hindi Checkout

```json
{
  "language": "hi"
}
```

***

## Common Failures for Language Configuration

### Language not changing

Possible causes:

- Unsupported language
- Invalid parameter
- Language fallback to default

***

# Supported Parameter Reference

## Payment Method Values

Common supported values:

| Value    | Meaning            |
| -------- | ------------------ |
| `upi`    | UPI                |
| `cards`  | Credit/Debit Cards |
| `nb`     | Net Banking        |
| `wallet` | Wallets            |
| `emi`    | EMI                |

Refer to full PayU reference for all supported values.

***

## Bank Codes

Use bank codes when restricting specific banking methods.

Examples:

- HDFC
- ICICI
- SBI

***

## Scheme Codes

Use scheme codes for scheme-specific routing where applicable.

***

# Conflict & Precedence Rules

Understanding precedence prevents unexpected behavior.

***

## What Happens if You Use Both `enforce_paymethod` and `drop_category`?

Avoid using both unless explicitly supported.

This can create conflicting rules.

Example:

- enforce = cards
- drop = cards

Result may be:

- empty checkout
- fallback behavior
- invalid configuration

***

## Dashboard vs API Request Priority

General precedence:

1. Merchant eligibility
2. Dashboard enablement
3. Runtime request parameters

If a payment method is not enabled for your merchant, runtime parameters cannot force it to appear.

***

## Invalid Parameter Behavior

Depending on implementation, PayU may:

- ignore invalid values
- fallback to defaults
- reject request

Validate parameter values before production rollout.

***

# Validate Checkout After Customization

Validation should happen in four stages.

***

## 1. Request Validation

Verify:

- parameter exists in request
- value is correct
- delimiters are correct

***

## 2. Hash Validation

After adding customization parameters:

- regenerate hash
- verify parameter order
- confirm request signature

> **Warning**
> Invalid hash is one of the most common integration failures after adding customization parameters.

Common causes:

- wrong parameter order
- missing parameter in hash generation
- stale hash

***

## 3. Checkout Validation

Verify:

- expected methods appear
- hidden methods are absent
- language changed correctly

Test:

- desktop
- mobile
- multiple browsers

***

## 4. Production Validation

Before go-live:

- test with real merchant configuration
- validate dashboard enablement
- verify analytics and logs

***

# Common Errors & Troubleshooting

## Payment Method Not Showing

Possible causes:

- method not enabled
- invalid value
- merchant ineligible
- incorrect bank code

Fix:

- validate reference values
- verify dashboard setup
- check request payload

***

## Payment Method Still Visible After Drop

Possible causes:

- wrong category
- conflicting rules
- parameter ignored

Fix:

- verify category values
- check precedence rules

***

## Invalid Hash Error

Possible causes:

- parameter order issue
- stale hash
- missing parameter during signature generation

Fix:

- regenerate hash after every payload change
- verify hash logic

***

## Checkout Language Not Changing

Possible causes:

- unsupported language
- invalid language code
- fallback behavior

***

# Best Practices

Follow these recommendations:

- Prefer `enforce_paymethod` when you need strict control
- Use drop configuration sparingly
- Always test in sandbox before production
- Recalculate hash after request changes
- Validate on desktop and mobile
- Monitor conversion impact after customization

***

# FAQs

## Can I show only UPI?

Yes. Use `enforce_paymethod = upi`.

***

## Can I hide only credit cards?

Yes, if cards are exposed as a supported drop category.

***

## Can I use both enforce and drop together?

Avoid unless explicitly supported.

***

## Can I customize checkout per transaction?

Yes, using request-level parameters.

***

## Why is BNPL not available?

Possible reasons:

- merchant not eligible
- dashboard not enabled
- feature unavailable in environment

<br />
