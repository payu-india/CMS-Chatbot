---
title: Merchant Hosted  - Wallets Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Minimal technical setup required</Banner>

Collect payments from leading wallets on your own checkout page. You show the wallets, the customer picks one, and you send the payment to PayU with `pg=CASH` and that wallet's code. PayU then sends the customer to the wallet to approve the payment.

**Steps to integrate**

<Cards columns="3">
  <Card title="1. Send the payment" href="#step-1-send-the-payment-request">
    Post the request with pg=CASH and the wallet code
  </Card>

  <Card title="2. Check the response" href="#step-2-check-the-response">
    Verify the response hash and status
  </Card>

  <Card title="3. Verify the payment" href="#step-3-verify-the-payment">
    Confirm with Verify Payment or webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="📮" theme="info">
  ### **For Developers**

  **Postman collection:** [Merchant Hosted Checkout > Wallets](https://www.postman.com/integratewithpayu-849372/payu-integration-s-workspace/folder/iu0g7es/wallets-integration)
</Callout>

***

## Step 1: Send the payment request

Post the payment details to PayU's `_payment` API with the payment category and the wallet's code.

| Environment    | URL                               |
| :------------- | :-------------------------------- |
| **Test**       | `<redacted URL>`                  |
| **Production** | `https://secure.payu.in/_payment` |

<Callout icon="📘" theme="info">
  ### **Note**

  For the **Try It** experience, refer to [Collect Payment API - Merchant Hosted Checkout](ref:_payment_merchant_hosted).
</Callout>

#### Mandatory Parameters

| Parameter     | Type & Description                                | Example                        |
| ------------- | ------------------------------------------------- | ------------------------------ |
| `key`         | `String` — Your merchant key                      | `JPM7Fg`                       |
| `txnid`       | `String` — Unique transaction ID                  | `wallet_txn_123`               |
| `amount`      | `Decimal` — Payment amount                        | `100.00`                       |
| `productinfo` | `String` — Product description                    | `iPhone 14`                    |
| `firstname`   | `String` — Customer first name                    | `Rajesh`                       |
| `email`       | `String` — Customer email                         | `rajesh@example.com`           |
| `phone`       | `String` — Customer phone                         | `9876543210`                   |
| `pg`          | `String` — Must be `WALLET`                       | `WALLET`                       |
| `bankcode`    | `String` — Wallet code (e.g., `PAYTM`, `PHONEPE`) | `PAYTM`                        |
| `surl`        | `URL` — Success callback URL                      | `https://yoursite.com/success` |
| `furl`        | `URL` — Failure callback URL                      | `https://yoursite.com/failure` |
| `hash`        | `String` — SHA-512 hash                           | `a1b2c3...`                    |

#### Optional Parameters

| Parameter     | Type & Description             | Example        |
| ------------- | ------------------------------ | -------------- |
| `lastname`    | `String` — Customer last name  | `Kumar`        |
| `address1`    | `String` — Address line 1      | `123 MG Road`  |
| `city`        | `String` — City                | `Mumbai`       |
| `state`       | `String` — State               | `Maharashtra`  |
| `country`     | `String` — Country             | `India`        |
| `zipcode`     | `String` — Postal code         | `400001`       |
| `udf1`-`udf5` | `String` — User-defined fields | `custom_value` |

<Accordion title="Generate the hash" icon="fa-lock">
  <HashingRequestParameters />

  <HashingSample />

  <Callout icon="🚧" theme="warn">
    ### **Critical Rules**

    - Generate the hash on your server. Never put the salt in your web page or app.
    - Send `pg` and `bankcode` in upper case, for example `CASH` and `PAYTM`.
  </Callout>
</Accordion>

<Accordion title="Sample request: Paytm" icon="fa-code">
  ```html
  <form action="<redacted URL>" method="post">
    <input type="hidden" name="key" value="YOUR_MERCHANT_KEY" />
    <input type="hidden" name="txnid" value="wallet_txn_12345" />
    <input type="hidden" name="productinfo" value="iPhone" />
    <input type="hidden" name="amount" value="10.00" />
    <input type="hidden" name="email" value="test@gmail.com" />
    <input type="hidden" name="firstname" value="Ashish" />
    <input type="hidden" name="phone" value="9876543210" />
    <input type="hidden" name="pg" value="CASH" />
    <input type="hidden" name="bankcode" value="PAYTM" />
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
    -d "txnid=wallet_txn_12345" \
    -d "amount=10.00" \
    -d "productinfo=iPhone" \
    -d "firstname=Ashish" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "pg=CASH" \
    -d "bankcode=PAYTM" \
    -d "surl=https://example.com/success" \
    -d "furl=https://example.com/failure" \
    -d "hash=YOUR_GENERATED_HASH"
  ```
  ```python
  import requests

  data = {
      "key": "YOUR_MERCHANT_KEY", "txnid": "wallet_txn_12345", "amount": "10.00",
      "productinfo": "iPhone", "firstname": "Ashish", "email": "test@gmail.com",
      "phone": "9876543210", "pg": "CASH", "bankcode": "PAYTM",
      "surl": "https://example.com/success", "furl": "https://example.com/failure",
      "hash": "YOUR_GENERATED_HASH",
  }
  r = requests.post("<redacted URL>", data=data)
  print(r.status_code, r.text)
  ```
  ```javascript
  const params = new URLSearchParams({
    key: "YOUR_MERCHANT_KEY", txnid: "wallet_txn_12345", amount: "10.00",
    productinfo: "iPhone", firstname: "Ashish", email: "test@gmail.com",
    phone: "9876543210", pg: "CASH", bankcode: "PAYTM",
    surl: "https://example.com/success", furl: "https://example.com/failure",
    hash: "YOUR_GENERATED_HASH"
  });

  fetch("<redacted URL>", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: params
  }).then(r => r.text()).then(console.log);
  ```
  ```php
  <?php
  $data = [
    'key' => 'YOUR_MERCHANT_KEY', 'txnid' => 'wallet_txn_12345', 'amount' => '10.00',
    'productinfo' => 'iPhone', 'firstname' => 'Ashish', 'email' => 'test@gmail.com',
    'phone' => '9876543210', 'pg' => 'CASH', 'bankcode' => 'PAYTM',
    'surl' => 'https://example.com/success', 'furl' => 'https://example.com/failure',
    'hash' => 'YOUR_GENERATED_HASH'
  ];
  $ch = curl_init('<redacted URL>');
  curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => http_build_query($data)]);
  echo curl_exec($ch);
  curl_close($ch);
  ```
  ```java
  import java.net.URI;
  import java.net.URLEncoder;
  import java.net.http.*;
  import java.nio.charset.StandardCharsets;
  import java.util.*;
  import java.util.stream.Collectors;

  public class WalletPayment {
      public static void main(String[] args) throws Exception {
          Map<String, String> p = new LinkedHashMap<>();
          p.put("key", "YOUR_MERCHANT_KEY"); p.put("txnid", "wallet_txn_12345"); p.put("amount", "10.00");
          p.put("productinfo", "iPhone"); p.put("firstname", "Ashish"); p.put("email", "test@gmail.com");
          p.put("phone", "9876543210"); p.put("pg", "CASH"); p.put("bankcode", "PAYTM");
          p.put("surl", "https://example.com/success"); p.put("furl", "https://example.com/failure");
          p.put("hash", "YOUR_GENERATED_HASH");
          String body = p.entrySet().stream()
              .map(e -> URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8) + "=" + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8))
              .collect(Collectors.joining("&"));
          HttpRequest req = HttpRequest.newBuilder(URI.create("<redacted URL>"))
              .header("Content-Type", "application/x-www-form-urlencoded")
              .POST(HttpRequest.BodyPublishers.ofString(body)).build();
          System.out.println(HttpClient.newHttpClient().send(req, HttpResponse.BodyHandlers.ofString()).body());
      }
  }
  ```
  ```csharp
  using System.Collections.Generic;
  using System.Net.Http;

  var form = new FormUrlEncodedContent(new Dictionary<string, string> {
      ["key"] = "YOUR_MERCHANT_KEY", ["txnid"] = "wallet_txn_12345", ["amount"] = "10.00",
      ["productinfo"] = "iPhone", ["firstname"] = "Ashish", ["email"] = "test@gmail.com",
      ["phone"] = "9876543210", ["pg"] = "CASH", ["bankcode"] = "PAYTM",
      ["surl"] = "https://example.com/success", ["furl"] = "https://example.com/failure",
      ["hash"] = "YOUR_GENERATED_HASH"
  });
  var res = await new HttpClient().PostAsync("<redacted URL>", form);
  System.Console.WriteLine(await res.Content.ReadAsStringAsync());
  ```
</Accordion>

<Accordion title="Sample request: Advantage Club" icon="fa-code">
  <Callout icon="🚧" theme="warn">
    ### **Watch Out!**

    Advantage Club has no test environment or test credentials. Test it directly in production with a small amount, using your production key and salt.
  </Callout>

  Advantage Club uses `pg=RD` and `bankcode=ADVCLUB`. Everything else is the same as the Paytm request.

  ```curl
  curl -X POST "https://secure.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=YOUR_MERCHANT_KEY" \
    -d "txnid=advclub_txn_001" \
    -d "amount=10.00" \
    -d "productinfo=iPhone" \
    -d "firstname=Ashish" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "pg=RD" \
    -d "bankcode=ADVCLUB" \
    -d "surl=https://example.com/success" \
    -d "furl=https://example.com/failure" \
    -d "hash=YOUR_GENERATED_HASH"
  ```
  ```python
  import requests

  data = {
      "key": "YOUR_MERCHANT_KEY", "txnid": "advclub_txn_001", "amount": "10.00",
      "productinfo": "iPhone", "firstname": "Ashish", "email": "test@gmail.com",
      "phone": "9876543210", "pg": "RD", "bankcode": "ADVCLUB",
      "surl": "https://example.com/success", "furl": "https://example.com/failure",
      "hash": "YOUR_GENERATED_HASH",
  }
  print(requests.post("https://secure.payu.in/_payment", data=data).text)
  ```
  ```javascript
  fetch("https://secure.payu.in/_payment", {
    method: "POST",
    headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: new URLSearchParams({
      key: "YOUR_MERCHANT_KEY", txnid: "advclub_txn_001", amount: "10.00",
      productinfo: "iPhone", firstname: "Ashish", email: "test@gmail.com",
      phone: "9876543210", pg: "RD", bankcode: "ADVCLUB",
      surl: "https://example.com/success", furl: "https://example.com/failure",
      hash: "YOUR_GENERATED_HASH"
    })
  }).then(r => r.text()).then(console.log);
  ```
  ```php
  <?php
  $data = [
    'key' => 'YOUR_MERCHANT_KEY', 'txnid' => 'advclub_txn_001', 'amount' => '10.00',
    'productinfo' => 'iPhone', 'firstname' => 'Ashish', 'email' => 'test@gmail.com',
    'phone' => '9876543210', 'pg' => 'RD', 'bankcode' => 'ADVCLUB',
    'surl' => 'https://example.com/success', 'furl' => 'https://example.com/failure',
    'hash' => 'YOUR_GENERATED_HASH'
  ];
  $ch = curl_init('https://secure.payu.in/_payment');
  curl_setopt_array($ch, [CURLOPT_POST => true, CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POSTFIELDS => http_build_query($data)]);
  echo curl_exec($ch);
  curl_close($ch);
  ```
</Accordion>

**Expected output:** the customer is sent to the wallet to log in and approve the payment.

***

## Step 2: Check the response

After the customer pays, PayU posts the result to your `surl` or `furl` as form data. Before you update the order, check the reverse hash.

<ReverseHashing />

<Accordion title="Expected output" icon="fa-reply">
  <Tabs>
    <Tab title="Success">
      ```json
      {
        "mihpayid": "403993715527518775",
        "mode": "CASH",
        "status": "success",
        "unmappedstatus": "captured",
        "key": "JP***g",
        "txnid": "wallet_txn_12345",
        "amount": "10.00",
        "discount": "0.00",
        "net_amount_debit": "10",
        "addedon": "2026-10-21 17:45:24",
        "productinfo": "iPhone",
        "firstname": "Ashish",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "udf1": "",
        "udf2": "",
        "udf3": "",
        "udf4": "",
        "udf5": "",
        "field9": "Transaction Completed Successfully",
        "payment_source": "payu",
        "PG_TYPE": "CASH-PG",
        "bank_ref_num": "<wallet reference>",
        "bankcode": "PAYTM",
        "error": "E000",
        "error_Message": "No Error",
        "hash": "<response hash>"
      }
      ```

      {/* REVIEW: the original sample showed bankcode=CASH. Confirm whether the response returns the wallet code (for example PAYTM) or CASH. */}
    </Tab>

    <Tab title="Failure">
      {/* REVIEW: illustrative failure response. Replace it with a real failed wallet response. */}

      ```json
      {
        "mihpayid": "403993715527518776",
        "mode": "CASH",
        "status": "failure",
        "unmappedstatus": "failed",
        "key": "JP***g",
        "txnid": "wallet_txn_12346",
        "amount": "10.00",
        "net_amount_debit": "0",
        "bankcode": "PAYTM",
        "field9": "<wallet failure reason>",
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

  Mark the order as paid only when `status` is `success` **and** the reverse hash matches.
</Callout>

***

## Step 3: Verify the payment

Confirm the final status from your server.

<Verify_Payment_Tabs />

***

## Test the integration

| Wallet         | Test details                                        |
| :------------- | :-------------------------------------------------- |
| Paytm          | Mobile `7777777777`, OTP `888888`                   |
| Amazon Pay     | Use your own Amazon account in the test environment |
| Airtel Money   | Use your own mobile number                          |
| Advantage Club | No test environment. Test in production.            |

{/* REVIEW: an internal SDK test-credentials page gives the Paytm test OTP as 489871, not 888888. Confirm the correct OTP before publishing. Also confirm the Airtel Money test steps. */}

For all test credentials, refer to [Test the Integration](doc:test-integration).

## Recommended integrations for wallets

- **Recurring payments:** collect recurring payments with wallets. For more information, refer to [Recurring Payments Integration](doc:introduction-recurring-payments-integration).
- **Offers:** set up offers for wallets on the Dashboard. For more information, refer to [Create an Instant Discount or Cashback Offer](doc:create-an-offer) and [Offers](doc:offers-integration).

## Next steps

<Cards columns="3">
  <Card title="Wallet Codes" href="/docs/wallet-codes">
    Codes to send in bankcode
  </Card>

  <Card title="Test the Integration" href="/docs/test-integration">
    Test credentials for every payment method
  </Card>

  <Card title="Production Checklist" href="/docs/integration-checklist-merchant-hosted-checkout">
    Steps to go live
  </Card>
</Cards>
