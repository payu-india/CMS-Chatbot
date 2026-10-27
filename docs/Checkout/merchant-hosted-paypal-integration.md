---
title: Merchant Hosted - Paypal Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Minimal technical setup required</Banner>

Accept payments from international customers through PayPal. You can add PayPal to your PayU Hosted Checkout or Merchant Hosted Checkout integration. Customers can choose to pay in their own currency with PayPal Currency Conversion. Payments go to your PayPal account and are settled in INR.

{/* REVIEW: confirm the settlement wording. The page says payments go to the merchant's PayPal account, are settled in INR and follow a T+1 schedule. Confirm all three. */}

## How does my customer pay?

1. The customer chooses **Wallets** on your checkout page.


   <Image src="https://files.readme.io/429e564-payu_payment_pagE_wallets_list.png" align="center" caption="Wallets list" border={true} />


2. The customer chooses **PayPal**.


   <Image src="https://files.readme.io/44bffcc-payu_payment_paypal_page.png" align="center" caption="PayPal option with currency choice" border={true} />


3. The customer chooses a currency and selects **PayPal**, then logs in to PayPal to approve the payment.

4. PayU checks the result with PayPal and posts it to your `<Glossary>surl</Glossary>` or `<Glossary>furl</Glossary>`.

{/* REVIEW: the screenshots show PayU's checkout page. On Merchant Hosted Checkout the wallet list is your own page. Replace them, or add a caption saying they show PayU Hosted Checkout. */}

## Why use PayPal?

<Accordion title="Key benefits" icon="fa-star">
  - **Higher success rates:** up to 20% higher success rates for international payments.
  - **Faster settlement:** payments are settled on a T+1 schedule.
  - **Large customer base:** access to more than 30 crore PayPal users worldwide.
  - **No extra PayU charges:** transaction rates are set by PayPal.
  - **Currency conversion:** customers can pay in their preferred currency instead of INR.

{/* REVIEW: the 20%, T+1 and 30 crore figures aren't in Confluence. Confirm them with the product team, or remove them. Confluence lists USD, EUR, CAD, AED, GBP, AUD, SGD and INR as conversion currencies; consider listing them. */}

</Accordion>

**Steps to integrate**

<Cards columns="3">
  <Card title="1. Send the payment" href="#step-1-send-the-payment-request">
    Post the request with pg=PAYPAL and bankcode=PAYPAL
  </Card>

  <Card title="2. Check the response" href="#step-2-check-the-response">
    Verify the response hash and status
  </Card>

  <Card title="3. Verify the payment" href="#step-3-verify-the-payment">
    Confirm with Verify Payment or webhooks
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

***

## Step 1: Send the payment request

Post the payment details to PayU's `_payment` API with `pg=PAYPAL` and `bankcode=PAYPAL`.

| Environment    | URL                               |
| :------------- | :-------------------------------- |
| **Test**       | `<redacted URL>`                  |
| **Production** | `https://secure.payu.in/_payment` |

<Callout icon="📘" theme="info">
  ### **Note**

  For the **Try It** experience, refer to [Collect Payment API - Wallets](ref:_payment_merchant_hosted_wallets).
</Callout>

<Tabs>
  <Tab title="Mandatory parameters">
    | Parameter                    | Description                                                                                                         |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | :--------------------------- | :------------------------------------------------------------------------------------------------------------------ | ----- | ------ | ----------- | --------- | ----- | ---- | ---- | ---- | ---- | ---- | - | - | - | - | - | ---------------------------------- |
    | `key`                        | `String` Merchant key provided by PayU. For example, `JP***g`.                                                      |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `<Glossary>txnid</Glossary>` | `String` Your unique reference for this order. Use a new value for every payment. For example, `paypal_txn_12345`.  |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `amount`                     | `String` Payment amount in INR. For example, `10.00`.                                                               |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `productinfo`                | `String` Short description of the product. For example, `T-shirt`.                                                  |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `firstname`                  | `String` Customer's first name. For example, `Ankit`.                                                               |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `email`                      | `String` Customer's email address. For example, `test@gmail.com`.                                                   |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `phone`                      | `String` Customer's phone number. For example, `9876543210`.                                                        |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `pg`                         | `String` Payment category. Must be `PAYPAL`.                                                                        |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `bankcode`                   | `String` Must be `PAYPAL`.                                                                                          |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `surl`                       | `String` Page PayU sends the customer to when the payment **succeeds**. For example, `https://example.com/success`. |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `furl`                       | `String` Page PayU sends the customer to when the payment **fails**. For example, `https://example.com/failure`.    |       |        |             |           |       |      |      |      |      |      |   |   |   |   |   |                                    |
    | `hash`                       | `String` \`sha512(key                                                                                               | txnid | amount | productinfo | firstname | email | udf1 | udf2 | udf3 | udf4 | udf5 |   |   |   |   |   | SALT)\`, generated on your server. |
  </Tab>

  <Tab title="Optional parameters">
    | Parameter                                                     | Description                                                                                                                                                      |
    | :------------------------------------------------------------ | :--------------------------------------------------------------------------------------------------------------------------------------------------------------- |
    | `lastname`                                                    | `String` Customer's last name. For example, `Kumar`.                                                                                                             |
    | `address1`, `address2`, `city`, `state`, `country`, `zipcode` | `String` Billing address. Helps with fraud checks and chargebacks. For example, `Mumbai`.                                                                        |
    | `udf1`–`udf5`                                                 | `String` Fields for your own reference data. They come back unchanged in the response. If you send them, include them in the hash. For example, `order_ref_123`. |
  </Tab>
</Tabs>

<Accordion title="Generate the hash" icon="fa-lock">
  <HashingRequestParameters />

  <HashingSample />

  <Callout icon="🚧" theme="warn">
    ### **Critical Rules**

    Generate the hash on your server. Never put the <Glossary>salt</Glossary> in your web page or app.
  </Callout>
</Accordion>

<Accordion title="Sample request" icon="fa-code">
  ```curl
  curl -X POST "<redacted URL>" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=YOUR_MERCHANT_KEY" \
    -d "txnid=paypal_txn_12345" \
    -d "amount=10.00" \
    -d "productinfo=iPhone" \
    -d "firstname=Ashish" \
    -d "email=test@gmail.com" \
    -d "phone=9876543210" \
    -d "pg=PAYPAL" \
    -d "bankcode=PAYPAL" \
    -d "surl=https://example.com/success" \
    -d "furl=https://example.com/failure" \
    -d "hash=YOUR_GENERATED_HASH"
  ```
  ```python
  import requests

  data = {
      "key": "YOUR_MERCHANT_KEY", "txnid": "paypal_txn_12345", "amount": "10.00",
      "productinfo": "iPhone", "firstname": "Ashish", "email": "test@gmail.com",
      "phone": "9876543210", "pg": "PAYPAL", "bankcode": "PAYPAL",
      "surl": "https://example.com/success", "furl": "https://example.com/failure",
      "hash": "YOUR_GENERATED_HASH",
  }
  r = requests.post("<redacted URL>", data=data)
  print(r.status_code, r.text)
  ```
  ```javascript
  const params = new URLSearchParams({
    key: "YOUR_MERCHANT_KEY", txnid: "paypal_txn_12345", amount: "10.00",
    productinfo: "iPhone", firstname: "Ashish", email: "test@gmail.com",
    phone: "9876543210", pg: "PAYPAL", bankcode: "PAYPAL",
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
    'key' => 'YOUR_MERCHANT_KEY', 'txnid' => 'paypal_txn_12345', 'amount' => '10.00',
    'productinfo' => 'iPhone', 'firstname' => 'Ashish', 'email' => 'test@gmail.com',
    'phone' => '9876543210', 'pg' => 'PAYPAL', 'bankcode' => 'PAYPAL',
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

  public class PayPalPayment {
      public static void main(String[] args) throws Exception {
          Map<String, String> p = new LinkedHashMap<>();
          p.put("key", "YOUR_MERCHANT_KEY"); p.put("txnid", "paypal_txn_12345"); p.put("amount", "10.00");
          p.put("productinfo", "iPhone"); p.put("firstname", "Ashish"); p.put("email", "test@gmail.com");
          p.put("phone", "9876543210"); p.put("pg", "PAYPAL"); p.put("bankcode", "PAYPAL");
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
      ["key"] = "YOUR_MERCHANT_KEY", ["txnid"] = "paypal_txn_12345", ["amount"] = "10.00",
      ["productinfo"] = "iPhone", ["firstname"] = "Ashish", ["email"] = "test@gmail.com",
      ["phone"] = "9876543210", ["pg"] = "PAYPAL", ["bankcode"] = "PAYPAL",
      ["surl"] = "https://example.com/success", ["furl"] = "https://example.com/failure",
      ["hash"] = "YOUR_GENERATED_HASH"
  });
  var res = await new HttpClient().PostAsync("<redacted URL>", form);
  System.Console.WriteLine(await res.Content.ReadAsStringAsync());
  ```
</Accordion>

**Expected output:** the customer sees the currency choice, then logs in to <Glossary>PayPal</Glossary> to approve the payment.

***

## Step 2: Check the response

PayU posts the result to your `<Glossary>surl</Glossary>` or `<Glossary>furl</Glossary>` as form data. Before you update the order, check the reverse <Glossary>hash</Glossary>.

<ReverseHashing />

<Accordion title="Expected output" icon="fa-reply">
  <Tabs>
    <Tab title="Success">
      ```json
      {
        "mihpayid": "403993715527518775",
        "mode": "PAYPAL",
        "status": "success",
        "unmappedstatus": "captured",
        "txnid": "paypal_txn_12345",
        "amount": "10.00",
        "PG_TYPE": "PAYPAL-PG",
        "bank_ref_num": "<PayPal reference>",
        "bankcode": "PAYPAL",
        "field4": "0.12",
        "field5": "USD",
        "error": "E000",
        "error_Message": "No Error",
        "hash": "<response hash>"
      }
      ```

`field4` is the amount the customer paid in their chosen currency, and `field5` is that currency.

{/* REVIEW: confirm the meaning of field4 and field5. They match the converted amount and currency in Confluence's currency-conversion contract. */}

    </Tab>
    <Tab title="Failure">
      {/* REVIEW: illustrative failure response. Replace it with a real failed <Glossary>PayPal</Glossary> response. */}

```json
{
  "mihpayid": "403993715527518776",
  "mode": "PAYPAL",
  "status": "failure",
  "unmappedstatus": "failed",
  "txnid": "paypal_txn_12346",
  "amount": "10.00",
  "bankcode": "PAYPAL",
  "field9": "<failure reason>",
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

  Mark the order as paid only when `status` is `success` **and** the reverse <Glossary>hash</Glossary> matches.
</Callout>

***

## Step 3: Verify the payment

Confirm the final status from your server.

<Verify_Payment_Tabs />

## Refunds

<Callout icon="📘" theme="info">
  ### **Important**

  Keep enough balance in your <Glossary>PayPal</Glossary> account before you start a refund. You can refund from the [Refunds Dashboard](doc:refunds-dashboard) or with the [Refund Transaction API](ref:refund_transaction_api).
</Callout>

{/* REVIEW: no PayPal test credentials are documented. Add how merchants test PayPal (for example, a PayPal sandbox account), or say that PayPal must be tested in production. */}

## Next steps

<Cards columns="3">
  <Card title="Test the Integration" href="/docs/test-integration">
    Test credentials for every payment method
  </Card>

  <Card title="Refunds Dashboard" href="/docs/refunds-dashboard">
    Refund PayPal payments
  </Card>

  <Card title="Production Checklist" href="/docs/integration-checklist-merchant-hosted-checkout">
    Steps to go live
  </Card>
</Cards>
