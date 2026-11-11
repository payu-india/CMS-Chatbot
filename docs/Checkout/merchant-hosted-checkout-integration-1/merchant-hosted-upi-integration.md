---
title: Merchant Hosted - UPI Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Minimal technical setup required</Banner>

Collect UPI payments on your own checkout page. Your customer enters their <Glossary>UPI</Glossary> ID (<Glossary>VPA</Glossary>) on your page, PayU sends a collect request to their UPI app, and the customer approves it with their UPI PIN.

<NPCI_Mandate />

{/* REVIEW: check that the <NPCI_Mandate /> component doesn't repeat the callout below. If it does, keep only one. */}

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

NPCI sunset the UPI Collect flow on **28 February 2026**. Customers can no longer pay or register mandates by typing a UPI ID, UPI number or mobile number, except in these cases:

\- **MCC 6012 and 6211:** IPO and secondary market transactions.
\- **iOS mobile apps and mobile web:** payments started from an iOS app or a mobile browser on iOS.
\- **UPI mandates:** executing, modifying or revoking an existing mandate.
\- **Cross-border payments (PACB):** cross-border and international payments.

If your business isn't covered by these exemptions, use [UPI Intent Integration](doc:upi-intent-server-to-server) or a UPI QR code instead:

\- **Android apps:** use [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow).
\- **Web:** generate a QR code from the deeplink returned by [UPI Intent Integration](doc:upi-intent-server-to-server).
\- **Seamless form post:** move to the server-to-server UPI Intent flow.

{/* REVIEW: an internal playbook also lists desktop web as an exempt case, but the published notice in CTP-273 doesn't. Confirm before adding desktop to the list. */}

</Callout>

<Callout icon="👍" theme="success">
  ### **Tips**

  Try the end-to-end **Merchant Hosted Checkout > UPI** flow and get ready-made code in the Integration Lab.

  <HTMLBlock>{`
    <button onclick="window.open('https://payu.in/integrationlab/seamless/sm-upiflow', '_blank')" class="tooltip-btn">

      Experience the flow and get the code
    </button>
  `}</HTMLBlock>
</Callout>

**Steps to integrate**

<Cards columns="4">
  <Card title="1. Validate the UPI ID" href="#step-1-validate-the-upi-id">
    Check the customer's VPA with the Validate VPA API
  </Card>

  <Card title="2. Send the payment" href="#step-2-send-the-payment-request">
    Post the request with pg=UPI and bankcode=UPI
  </Card>

  <Card title="3. Check the response" href="#step-3-check-the-response">
    Verify the response hash and status
  </Card>

  <Card title="4. Verify the payment" href="#step-4-verify-the-payment">
    Confirm with Verify Payment or webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="📮" theme="info">
  ### **For Developers**

  **Postman collection:** [Merchant Hosted Checkout > UPI](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/394lrbp/upi-integration)
</Callout>

***

## Step 1: Validate the UPI ID

Before you send the payment, check that the customer's UPI ID exists with the [Validate VPA API](ref:validate_vpa_api). This catches typing mistakes before the collect request is sent, which is the most common reason collect payments fail.

| Environment    | URL                                                    |
| :------------- | :----------------------------------------------------- |
| **Test**       | `<redacted URL>`                                       |
| **Production** | `https://info.payu.in/merchant/postservice.php?form=2` |

<Accordion title="Request parameters" icon="fa-table">
  #### Mandatory Parameters

  | Parameter | Type & Description                                                                                                               | Example          |
  | :-------- | :------------------------------------------------------------------------------------------------------------------------------- | :--------------- |
  | `key`     | `String` — Your <Glossary>merchant key</Glossary> provided by PayU.                                                              | `JP***g`         |
  | `command` | `String` — Must be `validateVPA`.                                                                                                | `validateVPA`    |
  | `var1`    | `String` — The customer's UPI ID (VPA).                                                                                          | `9999999999@upi` |
  | `hash`    | `String` — <Glossary>SHA-512</Glossary> <Glossary>hash</Glossary>: `sha512(key\|command\|var1\|SALT)`, generated on your server. | `d6a8...f3c2`    |

  {/* REVIEW: the sample response includes isAutoPayVPAValid. Confirm which request parameter returns it, and add it here if merchants should use it. */}
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "<redacted URL>" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=YOUR_MERCHANT_KEY" \
    -d "command=validateVPA" \
    -d "var1=9999999999@upi" \
    -d "hash=YOUR_GENERATED_HASH"
  ```
  ```python
  import hashlib, os, requests

  key, salt = os.environ["PAYU_KEY"], os.environ["PAYU_SALT"]
  vpa = "9999999999@upi"
  hash_value = hashlib.sha512(f"{key}|validateVPA|{vpa}|{salt}".encode()).hexdigest()

  r = requests.post("<redacted URL>",
                    data={"key": key, "command": "validateVPA", "var1": vpa, "hash": hash_value})
  print(r.text)
  ```
  ```csharp
  using System;
  using System.Collections.Generic;
  using System.Net.Http;
  using System.Security.Cryptography;
  using System.Text;

  var key  = Environment.GetEnvironmentVariable("PAYU_KEY");
  var salt = Environment.GetEnvironmentVariable("PAYU_SALT");
  var vpa  = "9999999999@upi";

  var raw  = $"{key}|validateVPA|{vpa}|{salt}";
  var hash = Convert.ToHexString(SHA512.HashData(Encoding.UTF8.GetBytes(raw))).ToLower();

  var form = new FormUrlEncodedContent(new Dictionary<string, string> {
      ["key"] = key, ["command"] = "validateVPA", ["var1"] = vpa, ["hash"] = hash
  });
  var res = await new HttpClient().PostAsync("<redacted URL>", form);
  Console.WriteLine(await res.Content.ReadAsStringAsync());
  ```
  ```javascript
  const crypto = require("crypto");

  const key = process.env.PAYU_KEY, salt = process.env.PAYU_SALT;
  const vpa = "9999999999@upi";
  const hash = crypto.createHash("sha512").update(`${key}|validateVPA|${vpa}|${salt}`).digest("hex");

  fetch("<redacted URL>", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({ key, command: "validateVPA", var1: vpa, hash })
  }).then(r => r.text()).then(console.log);
  ```
  ```java
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.*;
  import java.nio.charset.StandardCharsets;
  import java.security.MessageDigest;
  import java.util.*;
  import java.util.stream.Collectors;

  public class ValidateVpa {
      public static void main(String[] args) throws Exception {
          String key  = System.getenv("PAYU_KEY");
          String salt = System.getenv("PAYU_SALT");
          String vpa  = "9999999999@upi";

          String raw  = key + "|validateVPA|" + vpa + "|" + salt;
          MessageDigest md = MessageDigest.getInstance("SHA-512");
          byte[] bytes = md.digest(raw.getBytes(StandardCharsets.UTF_8));
          StringBuilder sb = new StringBuilder();
          for (byte b : bytes) sb.append(String.format("%02x", b));
          String hash = sb.toString();

          Map<String, String> p = new LinkedHashMap<>();
          p.put("key", key); p.put("command", "validateVPA");
          p.put("var1", vpa); p.put("hash", hash);

          String body = p.entrySet().stream()
              .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" +
                        URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));

          HttpRequest req = HttpRequest.newBuilder(URI.create("<redacted URL>"))
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(body)).build();
          System.out.println(HttpClient.newHttpClient().send(req, HttpResponse.BodyHandlers.ofString()).body());
      }
  }
  ```
  ```php
  <?php
  $key  = getenv('PAYU_KEY');
  $salt = getenv('PAYU_SALT');
  $vpa  = '9999999999@upi';
  $hash = hash('sha512', "$key|validateVPA|$vpa|$salt");

  $ch = curl_init('<redacted URL>');
  curl_setopt_array($ch, [
      CURLOPT_POST           => true,
      CURLOPT_RETURNTRANSFER => true,
      CURLOPT_POSTFIELDS     => http_build_query([
          'key' => $key, 'command' => 'validateVPA', 'var1' => $vpa, 'hash' => $hash
      ])
  ]);
  echo curl_exec($ch);
  curl_close($ch);
  ```
</Accordion>

<Accordion title="Expected output" icon="fa-reply">
  <Tabs>
    <Tab title="Valid UPI ID">
      ```json
      {
        "status": "SUCCESS",
        "vpa": "9999999999@upi",
        "isVPAValid": 1,
        "isAutoPayVPAValid": 1,
        "payerAccountName": "ABC"
      }
      ```
    </Tab>

    <Tab title="Invalid UPI ID">
      ```json
      {
        "status": "SUCCESS",
        "vpa": "abc@upi",
        "isVPAValid": 0,
        "payerAccountName": "NA"
      }
      ```
    </Tab>
  </Tabs>

  Continue only when `isVPAValid` is `1`. Note that `status` is `SUCCESS` in both cases: it means the API call worked, not that the UPI ID is valid.
</Accordion>

***

## Step 2: Send the payment request

Post the payment details to PayU's `_payment` API with `pg=UPI`, `bankcode=UPI` and the validated `vpa`.

| Environment    | URL                               |
| :------------- | :-------------------------------- |
| **Test**       | `<redacted URL>`                  |
| **Production** | `https://secure.payu.in/_payment` |

<Callout icon="📘" theme="info">
  ### **Note**

  For the **Try It** experience, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted).
</Callout>

#### Mandatory Parameters

| Parameter     | Type & Description                                                                                                                                                                                      | Example                       |
| :------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | :---------------------------- |
| `key`         | `String` — <Glossary>Merchant key</Glossary> provided by PayU.                                                                                                                                          | `JP***g`                      |
| `txnid`       | `String` — Your unique reference for this order. Use a new value for every payment.                                                                                                                     | `ypl938459435`                |
| `amount`      | `String` — Payment amount.                                                                                                                                                                              | `10.00`                       |
| `productinfo` | `String` — Short description of the product.                                                                                                                                                            | `iPhone`                      |
| `firstname`   | `String` — Customer's first name.                                                                                                                                                                       | `Ashish`                      |
| `email`       | `String` — Customer's email address.                                                                                                                                                                    | `test@gmail.com`              |
| `phone`       | `String` — Customer's phone number.                                                                                                                                                                     | `9876543210`                  |
| `pg`          | `String` — Payment category. Must be `UPI`.                                                                                                                                                             | `UPI`                         |
| `bankcode`    | `String` — Must be `UPI` for UPI Collect.                                                                                                                                                               | `UPI`                         |
| `vpa`         | `String` — The customer's validated <Glossary>VPA</Glossary> (UPI ID). For the list of handles, refer to [UPI Handles](doc:upi-handles).                                                                | `9999999999@upi`              |
| `surl`        | `String` — Page PayU sends the customer to when the payment **succeeds**. Must use HTTPS.                                                                                                               | `https://example.com/success` |
| `furl`        | `String` — Page PayU sends the customer to when the payment **fails**. Must use HTTPS.                                                                                                                  | `https://example.com/failure` |
| `hash`        | `String` — <Glossary>SHA-512</Glossary> <Glossary>hash</Glossary>: `sha512(key\|txnid\|amount\|productinfo\|firstname\|email\|udf1\|udf2\|udf3\|udf4\|udf5\|\|\|\|\|\|SALT)`, generated on your server. | `d6a8...f3c2`                 |

#### Optional Parameters

| Parameter     | Type & Description                                                                                                                                        | Example           |
| :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| `lastname`    | `String` — Customer's last name.                                                                                                                          | `Kumar`           |
| `address1`    | `String` — First line of the billing address. Helps with fraud checks and chargebacks.                                                                    | `123 Main Street` |
| `address2`    | `String` — Second line of the billing address.                                                                                                            | `Apt 4B`          |
| `city`        | `String` — Billing city.                                                                                                                                  | `New Delhi`       |
| `state`       | `String` — Billing state.                                                                                                                                 | `Delhi`           |
| `country`     | `String` — Billing country.                                                                                                                               | `India`           |
| `zipcode`     | `String` — Billing PIN code.                                                                                                                              | `110001`          |
| `udf1`–`udf5` | `String` — Fields for your own reference data. They come back unchanged in the response. If you send them, include them in the <Glossary>hash</Glossary>. | `order_ref_123`   |

<Accordion title="Generate the hash" icon="fa-lock">
  <HashingRequestParameters />

  <HashingSample />

  <Callout icon="🚧" theme="warn">
    ### **Critical Rules**

    - Generate the <Glossary>hash</Glossary> on your server. Never put the <Glossary>salt</Glossary> in your web page or app.
    - Use exactly the same values in the hash and in the request, including empty `udf` fields.
  </Callout>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```html
  <form action="<redacted URL>" method="post">
    <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
    <input type="hidden" name="txnid" value="upi_txn_12345" />
    <input type="hidden" name="productinfo" value="iPhone" />
    <input type="hidden" name="amount" value="10.00" />
    <input type="hidden" name="email" value="test@gmail.com" />
    <input type="hidden" name="firstname" value="Ashish" />
    <input type="hidden" name="phone" value="9876543210" />
    <input type="hidden" name="pg" value="UPI" />
    <input type="hidden" name="bankcode" value="UPI" />
    <input type="hidden" name="vpa" value="9999999999@upi" />
    <input type="hidden" name="surl" value="https://example.com/success" />
    <input type="hidden" name="furl" value="https://example.com/failure" />
    <input type="hidden" name="hash" value="YOUR_GENERATED_HASH" />
    <input type="submit" value="Pay" />
  </form>
  ```
  ```curl
  curl -X POST "<redacted URL>" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=YOUR_MERCHANT_KEY" \
    -d "txnid=upi_txn_12345" \
    -d "amount=10.00" \
    -d "productinfo=iPhone" \
    -d "firstname=Ashish" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "pg=UPI" \
    -d "bankcode=UPI" \
    -d "vpa=9999999999@upi" \
    -d "surl=https://example.com/success" \
    -d "furl=https://example.com/failure" \
    -d "hash=YOUR_GENERATED_HASH"
  ```
  ```python
  import requests

  data = {
      "key": "YOUR_MERCHANT_KEY", "txnid": "upi_txn_12345", "amount": "10.00",
      "productinfo": "iPhone", "firstname": "Ashish", "email": "test@gmail.com",
      "phone": "9876543210", "pg": "UPI", "bankcode": "UPI", "vpa": "9999999999@upi",
      "surl": "https://example.com/success", "furl": "https://example.com/failure",
      "hash": "YOUR_GENERATED_HASH",
  }
  r = requests.post("<redacted URL>", data=data)
  print(r.status_code, r.text)
  ```
  ```csharp
  using System.Collections.Generic;
  using System.Net.Http;

  var form = new FormUrlEncodedContent(new Dictionary<string, string> {
      ["key"]         = "YOUR_MERCHANT_KEY",
      ["txnid"]       = "upi_txn_12345",
      ["amount"]      = "10.00",
      ["productinfo"] = "iPhone",
      ["firstname"]   = "Ashish",
      ["email"]       = "test@gmail.com",
      ["phone"]       = "9876543210",
      ["pg"]          = "UPI",
      ["bankcode"]    = "UPI",
      ["vpa"]         = "9999999999@upi",
      ["surl"]        = "https://example.com/success",
      ["furl"]        = "https://example.com/failure",
      ["hash"]        = "YOUR_GENERATED_HASH"
  });
  var res = await new HttpClient().PostAsync("<redacted URL>", form);
  System.Console.WriteLine(await res.Content.ReadAsStringAsync());
  ```
  ```javascript
  const params = new URLSearchParams({
    key: "YOUR_MERCHANT_KEY", txnid: "upi_txn_12345", amount: "10.00",
    productinfo: "iPhone", firstname: "Ashish", email: "test@gmail.com",
    phone: "9876543210", pg: "UPI", bankcode: "UPI", vpa: "9999999999@upi",
    surl: "https://example.com/success", furl: "https://example.com/failure",
    hash: "YOUR_GENERATED_HASH"
  });

  fetch("<redacted URL>", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: params
  }).then(r => r.text()).then(console.log);
  ```
  ```java
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.*;
  import java.nio.charset.StandardCharsets;
  import java.util.*;
  import java.util.stream.Collectors;

  public class UpiCollect {
      public static void main(String[] args) throws Exception {
          Map<String, String> p = new LinkedHashMap<>();
          p.put("key", "YOUR_MERCHANT_KEY"); p.put("txnid", "upi_txn_12345"); p.put("amount", "10.00");
          p.put("productinfo", "iPhone"); p.put("firstname", "Ashish"); p.put("email", "test@gmail.com");
          p.put("phone", "9876543210"); p.put("pg", "UPI"); p.put("bankcode", "UPI");
          p.put("vpa", "9999999999@upi");
          p.put("surl", "https://example.com/success"); p.put("furl", "https://example.com/failure");
          p.put("hash", "YOUR_GENERATED_HASH");
          String body = p.entrySet().stream()
              .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" +
                        URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));
          HttpRequest req = HttpRequest.newBuilder(URI.create("<redacted URL>"))
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(body)).build();
          System.out.println(HttpClient.newHttpClient().send(req, HttpResponse.BodyHandlers.ofString()).body());
      }
  }
  ```
  ```php
  <?php
  $data = [
    'key' => 'YOUR_MERCHANT_KEY', 'txnid' => 'upi_txn_12345', 'amount' => '10.00',
    'productinfo' => 'iPhone', 'firstname' => 'Ashish', 'email' => 'test@gmail.com',
    'phone' => '9876543210', 'pg' => 'UPI', 'bankcode' => 'UPI', 'vpa' => '9999999999@upi',
    'surl' => 'https://example.com/success', 'furl' => 'https://example.com/failure',
    'hash' => 'YOUR_GENERATED_HASH'
  ];
  $ch = curl_init('<redacted URL>');
  curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => http_build_query($data)]);
  echo curl_exec($ch);
  curl_close($ch);
  ```
</Accordion>

**Expected output:** PayU sends a collect request to the customer's UPI app. The customer approves it with their UPI PIN, and PayU then posts the result to your `surl` or `furl`.

***

## Step 3: Check the response

PayU posts the result to your `surl` or `furl` as form data. Before you update the order, check the reverse hash.

<ReverseHashing />

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Accordion title="Expected output" icon="fa-reply">
  <Tabs>
    <Tab title="Success">
      ```json
      {
        "mihpayid": "403993715523409521",
        "mode": "UPI",
        "status": "success",
        "unmappedstatus": "captured",
        "key": "JP***g",
        "txnid": "upi_txn_12345",
        "amount": "10.00",
        "PG_TYPE": "UPI-PG",
        "bank_ref_num": "<UPI reference>",
        "bankcode": "UPI",
        "error": "E000",
        "error_Message": "No Error",
        "hash": "<response hash>"
      }
      ```
    </Tab>

    <Tab title="Failure">
      {/* REVIEW: illustrative failure response. Replace it with a real declined or expired UPI collect response. */}

      ```json
      {
        "mihpayid": "403993715523409522",
        "mode": "UPI",
        "status": "failure",
        "unmappedstatus": "failed",
        "key": "JP***g",
        "txnid": "upi_txn_12346",
        "amount": "10.00",
        "bankcode": "UPI",
        "field9": "<reason, for example declined or expired in the UPI app>",
        "error": "<error code>",
        "error_Message": "<error message>",
        "hash": "<response hash>"
      }
      ```
    </Tab>
  </Tabs>
</Accordion>

<Callout icon="🚧" theme="warn">
  ### **Critical Rules**

  - Mark the order as paid only when `status` is `success` **and** the reverse hash matches.
  - The customer may close the UPI app without approving. Don't wait on the browser: use Step 4 to get the final status.
</Callout>

***

## Step 4: Verify the payment

Browser redirects can be lost or spoofed. Confirm the final status from your server.

<Verify_Payment_Tabs />

***

## Test the integration

| What to test       | Test data        | Expected result                              |
| :----------------- | :--------------- | :------------------------------------------- |
| Valid UPI ID       | `9999999999@upi` | `isVPAValid` is `1`                          |
| Invalid UPI ID     | `abc@upi`        | `isVPAValid` is `0`. Don't send the payment. |
| Successful payment | `9999999999@upi` | `status=success`, reverse hash matches       |

For all test credentials, refer to [Test the Integration](doc:test-integration).

## Recommended integrations for UPI

\- **Recurring payments:** set up UPI Autopay subscriptions. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
\- **Offers:** set up offers for UPI on the Dashboard. For more information, refer to [Offers Dashboard](doc:offers-dashboard).

## Next steps

<Cards columns="3">
  <Card title="UPI Intent Integration" href="/docs/upi-intent-server-to-server">
    The recommended UPI flow for Android and web
  </Card>

  <Card title="Test the Integration" href="/docs/test-integration">
    Test credentials for every payment method
  </Card>

  <Card title="Production Checklist" href="/docs/integration-checklist-merchant-hosted-checkout">
    Steps to go live
  </Card>
</Cards>
