---
title: PACB-Saved Cards with a PayU Token Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

This page explains how to collect a cross-border card payment with a PayU token, that is, a card the customer saved earlier in the PayU vault.

**Use this flow when the customer has already saved their card in an earlier payment.**

<Cards columns="3">
  <Card title="1. Post Parameters to PayU" href="#step-1-post-parameters-to-payu">
    Send the PayU token instead of the card details.
  </Card>

  <Card title="2. Handle the Initiate Response" href="#step-2-handle-the-initiate-response-from-payu">
    Handle the response and authenticate the card.
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

<Callout icon="📘" theme="info">
  ### **Prerequisites**

  1. The card was saved in an earlier payment. See [Tokenize Card with PayU Vault Integration](doc:plain-cards-with-tokenization-integration-one-time-pacb).
  2. You have the card's `store_card_token`, retrieved with the [Get User Cards API](ref:get_user_cards_api).
  3. You use the same `user_credentials` value that was used when the card was saved.
</Callout>

***

## Step 1: Post Parameters to PayU

Post the payment parameters to PayU's `_payment` API with the saved PayU token instead of the card details.

<Callout icon="📘" theme="info">
  ### **Note**

  - For more information on cross-border card payments, refer to <Anchor target="_blank" href="ref:one-time-payment-for-cards-pacb-integration">One-Time Payment for Cards - CB</Anchor>.
  - For more information on saved cards in the PayU vault, refer to [Using Card Tokenized with PayU](ref:using-card-tokenized-with-payu).
</Callout>

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
    #### Mandatory Parameters

    | Parameter                                  | Description                                                                                                                                  | Example                                     |
    | ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
    | <Glossary>key</Glossary>                   | `String` Merchant <Glossary>key</Glossary> provided by PayU during onboarding.                                                               | `JPM7Fg`                                    |
    | <Glossary>txnid</Glossary>                 | `String` Unique transaction ID that you generate for the order.                                                                              | `payuTestTxn12345`                          |
    | <Glossary>amount</Glossary>                | `String` Payment amount.                                                                                                                     | `100.00`                                    |
    | <Glossary>productinfo</Glossary>           | `String` Name or short description of the goods or services. For physical goods, include all products. Character limit: 100.                 | `iPhone`                                    |
    | <Glossary>firstname</Glossary>             | `String` Customer's first name. Character limit: 60.                                                                                         | `Ashish`                                    |
    | <Glossary>email</Glossary>                 | `String` Customer's email address. Character limit: 50.                                                                                      | `test@gmail.com`                            |
    | <Glossary>phone</Glossary>                 | `String` Customer's phone number.                                                                                                            | `9876543210`                                |
    | `zipcode`                                  | `String` Billing postal code. 6-digit numeric.                                                                                               | `110075`                                    |
    | <Glossary>surl</Glossary>                  | `String` Success URL. PayU sends the customer here if the payment succeeds.                                                                  | `https://example.com/success`               |
    | <Glossary>furl</Glossary>                  | `String` Failure URL. PayU sends the customer here if the payment fails.                                                                     | `https://example.com/failure`               |
    | `pg`                                       | `String` Payment category. For cards, use `CC`.                                                                                              | `CC`                                        |
    | <Glossary>bankcode</Glossary>              | `String` Bank code. Use `CC` for credit cards and `DC` for debit cards.                                                                      | `CC`                                        |
    | `user_credentials`                         | `String` Format: `merchant_key:customer_id`. Must match the value used when the card was saved.                                              | `JPM7Fg:customer_1112`                      |
    | `storecard_token_type`                     | `String` Token type. Set to `0` for PayU tokens.                                                                                             | `0`                                         |
    | `store_card_token`                         | `String` PayU token, retrieved with the Get User Cards API.                                                                                  | `10a7d7a45b72644460f108`                    |
    | `txn_s2s_flow`                             | `String` Set to `4` for the server-to-server flow.                                                                                           | `4`                                         |
    | `s2s_client_ip`                            | `String` IP address of the customer's device. Used for <Glossary>fraud detection</Glossary>.                                                 | `10.200.12.12`                              |
    | `s2s_device_info`                          | `String` User agent of the customer's device.                                                                                                | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
    | `udf4` `mandatory for payment aggregators` | `String` End merchant's legal entity name. Character limit: 255.                                                                             | `XYZ Pvt. Ltd.`                             |
    | `udf5`                                     | `String` Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 4. Character limit: 255. | `INV123456`                                 |
    | <Glossary>hash</Glossary>                  | `String` SHA-512 hash of the request. See **Hash generation** below.                                                                         | `YOUR_GENERATED_HASH`                       |

    #### Optional Parameters

    | Parameter                                         | Description                                                                                                                                                                                                  | Example                                      |
    | ------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
    | `address1` `recommended for higher approval rate` | `String` First line of the billing address. Used for billing and <Glossary>fraud</Glossary> prevention. Character limit: 255.                                                                                | `123 Main Street`                            |
    | `address2`                                        | `String` Second line of the billing address. Character limit: 255.                                                                                                                                           | `Anytown`                                    |
    | `city` `recommended for higher approval rate`     | `String` Billing city. Character limit: 50.                                                                                                                                                                  | `New Delhi`                                  |
    | `state` `recommended for higher approval rate`    | `String` Billing state or province. Character limit: 50.                                                                                                                                                     | `Delhi`                                      |
    | `country` `recommended for higher approval rate`  | `String` Billing country as an ISO 3166-1 alpha-2 code. Character limit: 2.                                                                                                                                  | `IN`                                         |
    | `ccvv`                                            | `String` CVV entered by the customer: 3 digits (4 for AMEX).                                                                                                                                                 | `123`                                        |
    | `udf1` `recommended for higher approval rate`     | `String` Buyer's PAN (Permanent Account Number, India's main tax ID). Character limit: 10 alphanumeric characters.                                                                                           | `ABCDE1234K`                                 |
    | `udf2`                                            | `String` Any extra information about the transaction. Character limit: 255.                                                                                                                                  | `Additional transaction data`                |
    | `udf3` `recommended for higher approval rate`     | `String` Buyer's date of birth in DD-MM-YYYY format.                                                                                                                                                         | `02-02-1980`                                 |
    | `buyer_type_business` `B2B transactions`          | `String` Send `1` if the buyer is a business. Skip it for individual buyers; the default is `0`. If you send it, include it in the hash.                                                                     | `1`                                          |
    | `udf_params`                                      | `JSON String` Additional UDFs: `udf7` for the buyer's Import Export Code (IEC) and `udf8` for the airway bill (AWB) or consignment number for goods. If you send it, include it in the hash exactly as sent. | `{"udf7":"0100000029","udf8":"99953729071"}` |

    <Callout icon="🚧" theme="warn">
      ### **Important**

      With a PayU token, do **not** send `ccnum`, `ccname`, `ccexpmon`, `ccexpyr` or `additional_info`. PayU gets the card details from the saved token.
    </Callout>

    <Callout icon="📘" theme="info">
      ### **Note**

      - Send `udf1` to `udf5` as separate parameters. Don't send `udf6`; it's reserved.
      - Fields from `udf7` onwards, such as the IEC and AWB number, go only inside `udf_params`. Ask PayU to enable additional UDFs for your account before you send `udf_params`.
    </Callout>

    #### Hashing

    -
    - Notes: use empty strings for missing fields, compute server-side, lowercase hex

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

    <Accordion title="Sample Code for Hashing" icon="far fa-code">
      <HashingSample />
    </Accordion>
  </Tab>

  <Tab title="Sample Request">
    ```curl
    curl --location --request POST 'https://test.payu.in/_payment' \
    --header 'Content-Type: application/x-www-form-urlencoded' \
    --data-urlencode 'key=JPM7Fg' \
    --data-urlencode 'txnid=payuTestTransaction12345' \
    --data-urlencode 'amount=100.00' \
    --data-urlencode 'productinfo=Product Info' \
    --data-urlencode 'firstname=Ashish' \
    --data-urlencode 'email=test@payu.in' \
    --data-urlencode 'phone=9988776655' \
    --data-urlencode 'address1=123 Main Street' \
    --data-urlencode 'city=New York' \
    --data-urlencode 'state=NY' \
    --data-urlencode 'country=US' \
    --data-urlencode 'zipcode=10001' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'pg=CC' \
    --data-urlencode 'bankcode=CC' \
    --data-urlencode 'ccvv=123' \
    --data-urlencode 'user_credentials=JPM7Fg:customer_1112' \
    --data-urlencode 'storecard_token_type=0' \
    --data-urlencode 'store_card_token=10a7d7a45b72644460f108' \
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
        "email": "test@payu.in",
        "phone": "9988776655",
        "address1": "123 Main Street",
        "city": "New York",
        "state": "NY",
        "country": "US",
        "zipcode": "10001",
        "surl": "https://test.payu.in/admin/test_response",
        "furl": "https://test.payu.in/admin/test_response",
        "pg": "CC",
        "bankcode": "CC",
        "ccvv": "123",
        "user_credentials": "JPM7Fg:customer_1112",
        "storecard_token_type": "0",
        "store_card_token": "10a7d7a45b72644460f108",
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
    ```javascript
    const crypto = require("crypto");

    const SALT = process.env.PAYU_SALT; // Keep the salt on your server only

    const params = {
      key: "JPM7Fg",
      txnid: "payuTestTransaction12345",
      amount: "100.00",
      productinfo: "Product Info",
      firstname: "Ashish",
      email: "test@payu.in",
      phone: "9988776655",
      address1: "123 Main Street",
      city: "New York",
      state: "NY",
      country: "US",
      zipcode: "10001",
      surl: "https://test.payu.in/admin/test_response",
      furl: "https://test.payu.in/admin/test_response",
      pg: "CC",
      bankcode: "CC",
      ccvv: "123",
      user_credentials: "JPM7Fg:customer_1112",
      storecard_token_type: "0",
      store_card_token: "10a7d7a45b72644460f108",
      txn_s2s_flow: "4",
      s2s_client_ip: "10.200.12.12",
      s2s_device_info: "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
      udf1: "AELPR1234E",
      udf2: "",
      udf3: "02-02-1980",
      udf4: "XYZ Pvt. Ltd.",
      udf5: "INV123456",
      buyer_type_business: "1",
      udf_params: '{"udf7":"0100000029","udf8":"99953729071"}',
    };

    const hashFields = ["key", "txnid", "amount", "productinfo", "firstname", "email",
      "udf1", "udf2", "udf3", "udf4", "udf5"];
    const hashString = hashFields.map((f) => params[f]).join("|") + "||||||" + SALT
      + "|" + params.udf_params + "|" + params.buyer_type_business;
    params.hash = crypto.createHash("sha512").update(hashString).digest("hex");

    (async () => {
      const res = await fetch("https://test.payu.in/_payment", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: new URLSearchParams(params),
      });
      console.log(await res.json());
    })();
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
        'email' => 'test@payu.in',
        'phone' => '9988776655',
        'address1' => '123 Main Street',
        'city' => 'New York',
        'state' => 'NY',
        'country' => 'US',
        'zipcode' => '10001',
        'surl' => 'https://test.payu.in/admin/test_response',
        'furl' => 'https://test.payu.in/admin/test_response',
        'pg' => 'CC',
        'bankcode' => 'CC',
        'ccvv' => '123',
        'user_credentials' => 'JPM7Fg:customer_1112',
        'storecard_token_type' => '0',
        'store_card_token' => '10a7d7a45b72644460f108',
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
    import java.net.URI;
    import java.net.URLEncoder;
    import java.net.http.HttpClient;
    import java.net.http.HttpRequest;
    import java.net.http.HttpResponse;
    import java.nio.charset.StandardCharsets;
    import java.security.MessageDigest;
    import java.util.LinkedHashMap;
    import java.util.Map;
    import java.util.StringJoiner;

    public class PayUTokenPayment {
        public static void main(String[] args) throws Exception {
            String salt = System.getenv("PAYU_SALT"); // Keep the salt on your server only

            Map<String, String> params = new LinkedHashMap<>();
            params.put("key", "JPM7Fg");
            params.put("txnid", "payuTestTransaction12345");
            params.put("amount", "100.00");
            params.put("productinfo", "Product Info");
            params.put("firstname", "Ashish");
            params.put("email", "test@payu.in");
            params.put("phone", "9988776655");
            params.put("address1", "123 Main Street");
            params.put("city", "New York");
            params.put("state", "NY");
            params.put("country", "US");
            params.put("zipcode", "10001");
            params.put("surl", "https://test.payu.in/admin/test_response");
            params.put("furl", "https://test.payu.in/admin/test_response");
            params.put("pg", "CC");
            params.put("bankcode", "CC");
            params.put("ccvv", "123");
            params.put("user_credentials", "JPM7Fg:customer_1112");
            params.put("storecard_token_type", "0");
            params.put("store_card_token", "10a7d7a45b72644460f108");
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

            String[] hashFields = {"key","txnid","amount","productinfo","firstname","email",
                                   "udf1","udf2","udf3","udf4","udf5"};
            StringJoiner sj = new StringJoiner("|");
            for (String f : hashFields) sj.add(params.get(f));
            String hashInput = sj + "||||||" + salt
                + "|" + params.get("udf_params") + "|" + params.get("buyer_type_business");

            MessageDigest md = MessageDigest.getInstance("SHA-512");
            byte[] digest = md.digest(hashInput.getBytes(StandardCharsets.UTF_8));
            StringBuilder hex = new StringBuilder();
            for (byte b : digest) hex.append(String.format("%02x", b));
            params.put("hash", hex.toString());

            StringJoiner form = new StringJoiner("&");
            for (Map.Entry<String, String> e : params.entrySet())
                form.add(URLEncoder.encode(e.getKey(), StandardCharsets.UTF_8)
                    + "=" + URLEncoder.encode(e.getValue(), StandardCharsets.UTF_8));

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(form.toString()))
                .build();

            HttpResponse<String> response = HttpClient.newHttpClient()
                .send(request, HttpResponse.BodyHandlers.ofString());
            System.out.println(response.body());
        }
    }
    ```
  </Tab>
</Tabs>

***

<PACB_Cards_Step2 />

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

<Callout icon="📘" theme="info">
  ### **Note**

  For the character limit and full description of each parameter, refer to [Additional Info for Payment APIs](ref:addl_info-payment-apis).
</Callout>

***

## Next Steps

<Cards columns="3">
  <Card title="Tokenize Card with PayU Vault" href="/docs/plain-cards-with-tokenization-integration-one-time-pacb">
    Save a card during a payment.
  </Card>

  <Card title="Saved Cards with a Network Token" href="/docs/network-tokens-one-time-payment-pacb">
    Pay with a Visa or Mastercard network token.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
