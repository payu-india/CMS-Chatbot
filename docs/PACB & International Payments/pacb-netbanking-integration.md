---
title: PACB - NetBanking Integration
deprecated: false
hidden: false
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

This page explains how to collect NetBanking payments for cross-border transactions with the server-to-server (S2S) flow.

<Cards columns="3">
  <Card title="1. Post Parameters to PayU" href="#step-1-post-parameters-to-payu">
    Send the NetBanking payment request to PayU.
  </Card>

  <Card title="2. Handle the Initiate Response" href="#step-2-handle-the-initiate-response-from-payu">
    Redirect the customer to their bank.
  </Card>

  <Card title="3. Verify the Payment" href="#step-3-verify-the-payment">
    Confirm the final payment status.
  </Card>

  <Card title="4. Update Invoice ID (Conditional)" href="#step-4-update-invoice-id-conditional">
    Add the invoice ID if you didn't send it.
  </Card>

  <Card title="5. Upload Invoices and Shipping Documents" href="#step-5-upload-invoices-and-shipping-documents">
    Required within 10 days of the payment.
  </Card>
</Cards>

***

## Step 1: Post Parameters to PayU

Post the payment parameters to PayU's `_payment` API to start a NetBanking transaction.

<Accordion title="Environment" icon="fa-server">
  | Environment | URL                               |
  | ----------- | --------------------------------- |
  | Test        | `https://test.payu.in/_payment`   |
  | Production  | `https://secure.payu.in/_payment` |

  **HTTP method:** POST

  **Content type:** `application/x-www-form-urlencoded`
</Accordion>

<Tabs>
  <Tab title="Request Parameters">
    <Accordion title="Mandatory Parameters" icon="fa-table">
      ### Mandatory Parameters

      | Parameter                                    | Type & Description                                                                                                                                                                                                                                            | Example                                     |
      | -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
      | <Glossary>key</Glossary>                     | `String` Merchant <Glossary>key</Glossary> provided by PayU during onboarding.                                                                                                                                                                                | `JPM7Fg`                                    |
      | `txnid`                                      | `String` Unique transaction ID that you generate for the order.                                                                                                                                                                                               | `payuTestTransaction12345`                  |
      | `amount`                                     | `String` Payment amount.                                                                                                                                                                                                                                      | `100.00`                                    |
      | `productinfo`                                | `String` Name or short description of the goods or services. For physical goods, include all products. Character limit: 100.                                                                                                                                  | `iPhone`                                    |
      | `firstname`                                  | `String` Customer's first name. Character limit: 60.                                                                                                                                                                                                          | `Ashish`                                    |
      | `lastname`                                   | `String` Customer's last name. Character limit: 60.                                                                                                                                                                                                           | `Kumar`                                     |
      | `email`                                      | `String` Customer's email address. Character limit: 50.                                                                                                                                                                                                       | `test@gmail.com`                            |
      | `phone`                                      | `String` Customer's phone number.                                                                                                                                                                                                                             | `9876543210`                                |
      | <Glossary>surl</Glossary>                    | `String` Success URL. PayU sends the customer here if the payment succeeds.                                                                                                                                                                                   | `https://example.com/success`               |
      | <Glossary>furl</Glossary>                    | `String` Failure URL. PayU sends the customer here if the payment fails.                                                                                                                                                                                      | `https://example.com/failure`               |
      | `pg`                                         | `String` Payment category. For NetBanking, use `NB`.                                                                                                                                                                                                          | `NB`                                        |
      | `bankcode`                                   | `String` Bank code of the customer's bank. For the list, refer to [Net Banking Codes](https://docs.payu.in/docs/net-banking-codes). For test credentials, refer to [Test Cards, UPI ID and Wallets](https://docs.payu.in/docs/test-cards-upi-id-and-wallets). | `TESTPGNB`                                  |
      | `zipcode`                                    | `String` Customer's PIN code (6 digits).                                                                                                                                                                                                                      | `122018`                                    |
      | `txn_s2s_flow`                               | `String` Set to `4` for the server-to-server flow.                                                                                                                                                                                                            | `4`                                         |
      | `s2s_client_ip`                              | `String` IP address of the customer's device. Used for <Glossary>fraud detection</Glossary>.                                                                                                                                                                  | `10.200.12.12`                              |
      | `s2s_device_info`                            | `String` User agent of the customer's device.                                                                                                                                                                                                                 | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
      | `udf5`                                       | `String` Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 4. Character limit: 255.                                                                                                                  | `INV123456`                                 |
      | `udf4` _(Mandatory for payment aggregators)_ | `String` End merchant's legal entity name. Character limit: 255.                                                                                                                                                                                              | `XYZ Pvt. Ltd.`                             |
      | <Glossary>hash</Glossary>                    | `String` SHA-512 <Glossary>hash</Glossary> of the request. See **Hash generation** below.                                                                                                                                                                     | `YOUR_GENERATED_HASH`                       |
    </Accordion>

    <Accordion title="Optional Parameters" icon="fa-table">
      ### Optional Parameters

      | Parameter                                           | Type & Description                                                                                                                                                                                           | Example                                      |
      | --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
      | `address1` _(Recommended for higher approval rate)_ | `String` First line of the customer's address. Character limit: 100.                                                                                                                                         | `PayU, Bestech Business Tower`               |
      | `address2`                                          | `String` Second line of the customer's address. Character limit: 100.                                                                                                                                        | `Sohna Road`                                 |
      | `city` _(Recommended for higher approval rate)_     | `String` Customer's city. Character limit: 50.                                                                                                                                                               | `Gurgaon`                                    |
      | `state` _(Recommended for higher approval rate)_    | `String` Customer's state. Character limit: 50.                                                                                                                                                              | `Haryana`                                    |
      | `country` _(Recommended for higher approval rate)_  | `String` Customer's country. Character limit: 50.                                                                                                                                                            | `India`                                      |
      | `udf1` _(Recommended for higher approval rate)_     | `String` Buyer's PAN (Permanent Account Number, India's main tax ID). Character limit: 10 alphanumeric characters.                                                                                           | `ABCDE1234K`                                 |
      | `udf2`                                              | `String` Any extra information about the transaction. Character limit: 255.                                                                                                                                  | `-`                                          |
      | `udf3` _(Recommended for higher approval rate)_     | `String` Buyer's date of birth in DD-MM-YYYY format.                                                                                                                                                         | `02-02-1980`                                 |
      | `buyer_type_business` _(B2B transactions)_          | `String` Send `1` if the buyer is a business. Skip it for individual buyers; the default is `0`. If you send it, include it in the <Glossary>hash</Glossary>.                                                | `1`                                          |
      | `udf_params`                                        | `JSON String` Additional UDFs: `udf7` for the buyer's Import Export Code (IEC) and `udf8` for the airway bill (AWB) or consignment number for goods. If you send it, include it in the hash exactly as sent. | `{"udf7":"0100000029","udf8":"99953729071"}` |

      <Callout icon="📘" theme="info">
        ### **Note**

        - Send `udf1` to `udf5` as separate parameters. Don't send `udf6`; it's reserved.
        - Fields from `udf7` onwards, such as the IEC and AWB number, go only inside `udf_params`. Ask PayU to enable additional UDFs for your account before you send `udf_params`.
      </Callout>
    </Accordion>

    #### Hashing

    - **Notes**: use empty strings for missing fields, compute server-side, lowercase hex

    <Accordion title="Hash generation" icon="fa-lock">
      <PACB_Hashing />

      ```plaintext
      key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|salt|additional_charges|buyer_type_business
      ```

      **Case 4 example:** if you pass `api_version=7`, `buyer_type_business` and `udf_params` in the payment request:

      ```plaintext
      key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5|udf6|udf7|udf8|udf9|udf10|si_details|salt|udf_params|buyer_type_business
      ```

      <Callout icon="🚧" theme="warn">
        ### **Critical Rules**

        - Generate the hash on your server only. Never expose your salt in a browser or app.
        - Use the Hash Verification Tool to check your hash. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool).
      </Callout>
    </Accordion>

    <Accordion title="Sample Code for Hashing" icon="far fa-code">
      <HashingSample />
    </Accordion>
  </Tab>

  <Tab title="Sample Request">
    <Accordion title="Sample Request" icon="fa-code">
      ```curl
      curl --location --request POST 'https://test.payu.in/_payment' \
      --header 'Content-Type: application/x-www-form-urlencoded' \
      --data-urlencode 'key=JPM7Fg' \
      --data-urlencode 'txnid=payuTestTransaction12345' \
      --data-urlencode 'amount=100.00' \
      --data-urlencode 'productinfo=Product Info' \
      --data-urlencode 'firstname=Ashish' \
      --data-urlencode 'lastname=Kumar' \
      --data-urlencode 'email=test@payu.in' \
      --data-urlencode 'phone=9988776655' \
      --data-urlencode 'zipcode=122018' \
      --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
      --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
      --data-urlencode 'pg=NB' \
      --data-urlencode 'bankcode=TESTPGNB' \
      --data-urlencode 'txn_s2s_flow=4' \
      --data-urlencode 's2s_client_ip=10.200.12.12' \
      --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
      --data-urlencode 'udf1=AELPR1234E' \
      --data-urlencode 'udf2=' \
      --data-urlencode 'udf3=02-02-1980' \
      --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
      --data-urlencode 'udf5=INV123456' \
      --data-urlencode 'buyer_type_business=1' \
      --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
      --data-urlencode 'hash=YOUR_GENERATED_HASH'
      ```
      ```python
      import hashlib
      import os
      import requests

      SALT = os.environ["PAYU_SALT"]  # Keep the salt on your server only

      params = {
          "key": "JPM7Fg",
          "txnid": "payuTestTransaction12345",
          "amount": "100.00",
          "productinfo": "Product Info",
          "firstname": "Ashish",
          "lastname": "Kumar",
          "email": "test@payu.in",
          "phone": "9988776655",
          "zipcode": "122018",
          "surl": "https://test.payu.in/admin/test_response",
          "furl": "https://test.payu.in/admin/test_response",
          "pg": "NB",
          "bankcode": "TESTPGNB",
          "txn_s2s_flow": "4",
          "s2s_client_ip": "10.200.12.12",
          "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
          "udf1": "AELPR1234E",
          "udf2": "",
          "udf3": "02-02-1980",
          "udf4": "XYZ Pvt. Ltd.",
          "udf5": "INV123456",
          "buyer_type_business": "1",
          "udf_params": '{"udf7":"0100000029","udf8":"99953729071"}',
      }

      hash_fields = ["key", "txnid", "amount", "productinfo", "firstname", "email",
                     "udf1", "udf2", "udf3", "udf4", "udf5"]
      hash_string = ("|".join(params[f] for f in hash_fields) + "||||||" + SALT
                     + "|" + params["udf_params"] + "|" + params["buyer_type_business"])
      params["hash"] = hashlib.sha512(hash_string.encode("utf-8")).hexdigest()

      response = requests.post("https://test.payu.in/_payment", data=params)
      print(response.json())
      ```
      ```php
      <?php
      $salt = getenv('PAYU_SALT'); // Keep the salt on your server only

      $params = [
          'key' => 'JPM7Fg',
          'txnid' => 'payuTestTransaction12345',
          'amount' => '100.00',
          'productinfo' => 'Product Info',
          'firstname' => 'Ashish',
          'lastname' => 'Kumar',
          'email' => 'test@payu.in',
          'phone' => '9988776655',
          'zipcode' => '122018',
          'surl' => 'https://test.payu.in/admin/test_response',
          'furl' => 'https://test.payu.in/admin/test_response',
          'pg' => 'NB',
          'bankcode' => 'TESTPGNB',
          'txn_s2s_flow' => '4',
          's2s_client_ip' => '10.200.12.12',
          's2s_device_info' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
          'udf1' => 'AELPR1234E',
          'udf2' => '',
          'udf3' => '02-02-1980',
          'udf4' => 'XYZ Pvt. Ltd.',
          'udf5' => 'INV123456',
          'buyer_type_business' => '1',
          'udf_params' => '{"udf7":"0100000029","udf8":"99953729071"}',
      ];

      $hashFields = ['key', 'txnid', 'amount', 'productinfo', 'firstname', 'email',
          'udf1', 'udf2', 'udf3', 'udf4', 'udf5'];
      $hashString = implode('|', array_map(fn($f) => $params[$f], $hashFields)) . '||||||' . $salt
          . '|' . $params['udf_params'] . '|' . $params['buyer_type_business'];
      $params['hash'] = hash('sha512', $hashString);

      $ch = curl_init('https://test.payu.in/_payment');
      curl_setopt_array($ch, [
          CURLOPT_POST => true,
          CURLOPT_POSTFIELDS => http_build_query($params),
          CURLOPT_RETURNTRANSFER => true,
      ]);
      echo curl_exec($ch);
      curl_close($ch);
      ```
      ```java
      import java.io.*;
      import java.net.*;
      import java.nio.charset.StandardCharsets;
      import java.security.MessageDigest;
      import java.util.*;

      public class PayUNetBanking {

          private static final String SALT = System.getenv("PAYU_SALT"); // Keep salt server-side only

          public static void main(String[] args) throws Exception {
              Map<String, String> params = new LinkedHashMap<>();
              params.put("key", "JPM7Fg");
              params.put("txnid", "payuTestTransaction12345");
              params.put("amount", "100.00");
              params.put("productinfo", "Product Info");
              params.put("firstname", "Ashish");
              params.put("lastname", "Kumar");
              params.put("email", "test@payu.in");
              params.put("phone", "9988776655");
              params.put("zipcode", "122018");
              params.put("surl", "https://test.payu.in/admin/test_response");
              params.put("furl", "https://test.payu.in/admin/test_response");
              params.put("pg", "NB");
              params.put("bankcode", "TESTPGNB");
              params.put("txn_s2s_flow", "4");
              params.put("s2s_client_ip", "10.200.12.12");
              params.put("s2s_device_info", "Mozilla/5.0 (Windows NT 10.0; Win64; x64)");
              params.put("udf1", "AELPR1234E");
              params.put("udf2", "");
              params.put("udf3", "02-02-1980");
              params.put("udf4", "XYZ Pvt. Ltd.");
              params.put("udf5", "INV123456");
              params.put("buyer_type_business", "1");
              params.put("udf_params", "{\"udf7\":\"0100000029\",\"udf8\":\"99953729071\"}");

              String[] hashFields = {"key", "txnid", "amount", "productinfo", "firstname", "email",
                      "udf1", "udf2", "udf3", "udf4", "udf5"};
              StringBuilder hashInput = new StringBuilder();
              for (String field : hashFields) {
                  hashInput.append(params.getOrDefault(field, "")).append("|");
              }
              hashInput.append("|||||").append(SALT)
                      .append("|").append(params.get("udf_params"))
                      .append("|").append(params.get("buyer_type_business"));

              MessageDigest digest = MessageDigest.getInstance("SHA-512");
              byte[] hashBytes = digest.digest(hashInput.toString().getBytes(StandardCharsets.UTF_8));
              StringBuilder hexHash = new StringBuilder();
              for (byte b : hashBytes) hexHash.append(String.format("%02x", b));
              params.put("hash", hexHash.toString());

              StringJoiner formBody = new StringJoiner("&");
              for (Map.Entry<String, String> entry : params.entrySet()) {
                  formBody.add(URLEncoder.encode(entry.getKey(), "UTF-8") + "="
                          + URLEncoder.encode(entry.getValue(), "UTF-8"));
              }

              URL url = new URL("https://test.payu.in/_payment");
              HttpURLConnection conn = (HttpURLConnection) url.openConnection();
              conn.setRequestMethod("POST");
              conn.setDoOutput(true);
              conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");

              try (OutputStream os = conn.getOutputStream()) {
                  os.write(formBody.toString().getBytes(StandardCharsets.UTF_8));
              }

              BufferedReader reader = new BufferedReader(
                      new InputStreamReader(conn.getInputStream(), StandardCharsets.UTF_8));
              StringBuilder response = new StringBuilder();
              String line;
              while ((line = reader.readLine()) != null) response.append(line);
              System.out.println(response);
          }
      }
      ```
    </Accordion>
  </Tab>
</Tabs>

***

## Step 2: Handle the Initiate Response from PayU

After you post the payment request, PayU returns a JSON response with the transaction status and a form that redirects the customer to their bank.

<Accordion title="Response Parameters" icon="fa-table">
  | Parameter                 | Type & Description                                                                       | Example                                    |
  | ------------------------- | ---------------------------------------------------------------------------------------- | ------------------------------------------ |
  | `metaData`                | `Object` Transaction metadata.                                                           | \-                                         |
  | `metaData.referenceId`    | `String` PayU reference ID for the transaction.                                          | `e1bc7be8c52b8f26...`                      |
  | `metaData.txnId`          | `String` Your transaction ID.                                                            | `payuTestTransaction12345`                 |
  | `metaData.txnStatus`      | `String` Transaction status.                                                             | `pending`                                  |
  | `metaData.unmappedStatus` | `String` Status to drive your flow: `pending`, `captured` or `failed`.                   | `pending`                                  |
  | `metaData.statusCode`     | `String` Error code when the request fails.                                              | `null`                                     |
  | `metaData.message`        | `String` Error message when the request fails.                                           | `null`                                     |
  | `result.acsTemplate`      | `String` Base64-encoded HTML form that redirects the customer to their bank's page.      | `PGh0bWw+PGJvZHk+...`                      |
  | `result.otpPostUrl`       | `String` URL returned by PayU. For NetBanking, redirect the customer with `acsTemplate`. | `https://test.payu.in/ResponseHandler.php` |
</Accordion>

<Accordion title="Success Response" icon="fa-reply">
  ```json
  {
    "metaData": {
      "message": null,
      "referenceId": "e1bc7be8c52b8f269124e723b2d201800a629895299f5628fe168a9c8dc40f5e",
      "statusCode": null,
      "txnId": "payuTestTransaction12345",
      "txnStatus": "pending",
      "unmappedStatus": "pending"
    },
    "result": {
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0i...",
      "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
  }
  ```
</Accordion>

<Accordion title="Error Response — Invalid Bank Code" icon="fa-reply">
  ```json
  {
    "metaData": {
      "message": "Invalid bank code provided.",
      "referenceId": null,
      "statusCode": "E001",
      "txnId": "payuTestTransaction12345",
      "txnStatus": "failed",
      "unmappedStatus": "failed"
    },
    "result": null
  }
  ```
</Accordion>

<Accordion title="Error Response — Hash Mismatch" icon="fa-reply">
  ```json
  {
    "metaData": {
      "message": "Hash value does not match.",
      "referenceId": null,
      "statusCode": "E002",
      "txnId": "payuTestTransaction12345",
      "txnStatus": "failed",
      "unmappedStatus": "failed"
    },
    "result": null
  }
  ```
</Accordion>

<Accordion title="Failure Response — Payment Declined at Bank" icon="fa-reply">
  ```json
  {
    "metaData": {
      "message": "Transaction declined by the bank.",
      "referenceId": "a9cd2ef1b83c4d12a678f902de1c3045b12e3478210f9312ab167c3d8ef20a1c",
      "statusCode": "E501",
      "txnId": "payuTestTransaction12345",
      "txnStatus": "failed",
      "unmappedStatus": "failed"
    },
    "result": null
  }
  ```
</Accordion>

<Accordion title="Handle the Response" icon="fa-info-circle">
  Use `metaData.unmappedStatus` to decide what to do next:

  | Status     | What to do                                                                                                              |
  | ---------- | ----------------------------------------------------------------------------------------------------------------------- |
  | `pending`  | Decode `result.acsTemplate` (base64) and load the HTML form in the customer's browser. It redirects them to their bank. |
  | `captured` | The payment succeeded. No further action is needed.                                                                     |
  | `failed`   | The payment failed. Check `metaData.statusCode` and `metaData.message`, and show an error to the customer.              |

  After the customer completes the payment at their bank, PayU posts the final response to your `surl` or `furl` and to your webhook.
</Accordion>

<Callout icon="👍" theme="success">
  ### **Tips**

  Use the PayU Hash Verification Tool to check the reverse hash in the final response. For more information, refer to [Using PayU Hash Verification Tool](doc:using-payu-hash-verification-tool).
</Callout>

***

## Step 3: Verify the Payment

<PACB_Verify_Payment />

***

## Step 4: Update Invoice ID (Conditional)

<Update_Invoice_ID />

***

## Step 5: Upload Invoices and Shipping Documents

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  - Upload the invoice within **10 days** of the transaction. If you don't, your next settlement is put on hold.
  - Goods merchants must upload the invoice and the airway bill (AWB) separately, so that's two Invoice Upload calls per payment.
</Callout>

<Upload_Invoices />

***

## Error Handling

If you get an error code, refer to [Error Codes](ref:error-codes) for the reason. For errors at each transaction stage, refer to [Transaction Stages - Error References](ref:transaction-stages-error-references-on-field7-field8).

***

## Next Steps

<Cards columns="3">
  <Card title="UPI Intent with S2S" href="/docs/pacb-upi-intent-with-s2s-integration">
    Accept UPI payments.
  </Card>

  <Card title="Plain Cards Integration" href="/docs/plain-cards-integration-one-time-pacb">
    Accept card payments.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
