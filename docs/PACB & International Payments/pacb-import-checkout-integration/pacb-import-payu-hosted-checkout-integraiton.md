---
title: PACB-Import-PayU Hosted Checkout Integraiton
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Minimal technical setup required</Banner>

This page explains how to collect cross-border payments with PayU Hosted Checkout using the `_payment` API. PayU shows the payment page, so you don't handle card or bank details.

<Cards columns="3">
  <Card title="1. Post the Payment Request" href="#step-1-post-the-payment-request-to-payu">
    Post the payment parameters with the cross-border UDFs.
  </Card>

  <Card title="2. Check the Response from PayU" href="#step-2-check-the-response-from-payu">
    Handle the response and check the reverse hash.
  </Card>

  <Card title="3. Verify the Payment" href="#step-3-verify-the-payment">
    Reconcile the transaction details.
  </Card>

  <Card title="4. Update Invoice ID (Conditional)" href="#step-4-update-invoice-id-conditional">
    Add the invoice ID if you didn't send it.
  </Card>

  <Card title="5. Upload Invoices and Shipping Documents" href="#step-5-upload-invoices-and-shipping-documents">
    Required within 10 days of the payment.
  </Card>
</Cards>

***

## Step 1: Post the Payment Request to PayU

Post the payment parameters from the customer's browser to PayU. Calculate the <Glossary>hash</Glossary> on your server first.

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
    <Callout icon="📘" theme="info">
      ### **Note**

      The <Glossary>hash</Glossary> is mandatory. Calculate it correctly and post it to PayU with the request. The <Glossary>udf</Glossary> parameters `udf1` to `udf5` have specific uses for cross-border payments, as described below.
    </Callout>

    #### Mandatory Parameters

    <table>
      <thead>
        <tr>
          <th>
            Parameter
          </th>

          <th>
            Type
          </th>

          <th>
            Description
          </th>

          <th>
            Example
          </th>
        </tr>
      </thead>

      <tbody>
        <tr>
          <td>
            <code>key</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Your <Glossary>merchant</Glossary> key provided by PayU.
          </td>

          <td>
            <code>JPM7Fg</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>txnid</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Your <Glossary>txnid</Glossary> (order ID). If a payment with this ID has already succeeded, reusing the ID fails — send a new one for every payment. Character limit: 25.
          </td>

          <td>
            <code>fd3e847h2</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>amount</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Payment <Glossary>amount</Glossary>.
          </td>

          <td>
            <code>1000.00</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>productinfo</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Name or short description of the goods or services. For physical goods, include all products. Character limit: 100.
          </td>

          <td>
            <code>Time Magazine Subscription</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>email</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Customer's email address. Accuracy matters because <Glossary>fraud_detection</Glossary> relies on it. Character limit: 50.
          </td>

          <td>
            <code>ashish@test.com</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>firstname</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Customer's first name. Character limit: 60.
          </td>

          <td>
            <code>John</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>lastname</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Customer's middle and last name. Character limit: 60.
          </td>

          <td>
            <code>Doe</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>phone</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Customer's phone number, used for <Glossary>fraud_detection</Glossary> detection. Character limit: 50.
          </td>

          <td>
            <code>9843176540</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>zipcode</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Billing postal code. Character limit: 6 digits (India PIN code).
          </td>

          <td>
            <code>110075</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>surl</code>
          </td>

          <td>
            <code>URL</code>
          </td>

          <td>
            <Glossary>surl</Glossary>. PayU redirects the customer here after a successful payment.
          </td>

          <td>
            <code>https://example.com/success</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>furl</code>
          </td>

          <td>
            <code>URL</code>
          </td>

          <td>
            <Glossary>furl</Glossary>. PayU redirects the customer here after a failed payment.
          </td>

          <td>
            <code>https://example.com/failure</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>udf5</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 4. Character limit: 255.
          </td>

          <td>
            <code>INV123456</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>hash</code>
          </td>

          <td>
            <code>String</code>
          </td>

          <td>
            SHA-512 <Glossary>hash</Glossary> of the request. See **Hash generation** below.
          </td>

          <td>
            <code>YOUR_GENERATED_HASH</code>
          </td>
        </tr>
      </tbody>
    </table>

    #### Optional Parameters

    <table>
    <thead><tr><th>Parameter</th><th>Type</th><th>Description</th><th>Example</th></tr></thead>
    <tbody>
    <tr>
      <td><code>address1</code><br /><em>Recommended for higher approval rate</em></td>
      <td><code>String</code></td>
      <td>First line of the <Glossary>billing_address</Glossary>. Used for billing and fraud prevention. Character limit: 255.</td>
      <td><code>123 Main Street</code></td>
    </tr>
    <tr>
      <td><code>address2</code></td>
      <td><code>String</code></td>
      <td>Second line of the billing address. Character limit: 255.</td>
      <td><code>Anytown</code></td>
    </tr>
    <tr>
      <td><code>city</code><br /><em>Recommended for higher approval rate</em></td>
      <td><code>String</code></td>
      <td>Billing city. Character limit: 50.</td>
      <td><code>New Delhi</code></td>
    </tr>
    <tr>
      <td><code>state</code><br /><em>Recommended for higher approval rate</em></td>
      <td><code>String</code></td>
      <td>Billing state or province. Character limit: 50.</td>
      <td><code>Delhi</code></td>
    </tr>
    <tr>
      <td><code>country</code><br /><em>Recommended for higher approval rate</em></td>
      <td><code>String</code></td>
      <td>Billing country as an <Glossary>iso_3166</Glossary> alpha-2 code. Character limit: 2.</td>
      <td><code>IN</code></td>
    </tr>
    <tr>
      <td><code>udf1</code><br /><em>Recommended for higher approval rate</em></td>
      <td><code>String</code></td>
      <td>Buyer's <Glossary>pan</Glossary> (Permanent Account Number, India's main tax ID). Character limit: 10 alphanumeric characters.</td>
      <td><code>ABCDE1234K</code></td>
    </tr>
    <tr>
      <td><code>udf2</code></td>
      <td><code>String</code></td>
      <td>Any extra information about the transaction. Character limit: 255.</td>
      <td><code>Additional transaction data</code></td>
    </tr>
    <tr>
      <td><code>udf3</code><br /><em>Recommended for higher approval rate</em></td>
      <td><code>String</code></td>
      <td>Buyer's date of birth in DD-MM-YYYY format.</td>
      <td><code>02-02-1980</code></td>
    </tr>
    <tr>
      <td><code>udf4</code><br /><em>Mandatory for <Glossary>payment_aggregator</Glossary>s</em></td>
      <td><code>String</code></td>
      <td>End merchant's legal entity name. For <Glossary>upi</Glossary>, this field should not be passed. Character limit: 255.</td>
      <td><code>XYZ Pvt. Ltd.</code></td>
    </tr>
    <tr>
      <td><code>buyer_type_business</code><br /><em>For <Glossary>b2b</Glossary> transactions</em></td>
      <td><code>String</code></td>
      <td>Send <code>1</code> if the buyer is a business. Skip it for individual buyers; the default is <code>0</code>. If you send it, include it in the <Glossary>hash</Glossary>.</td>
      <td><code>1</code></td>
    </tr>
    <tr>
      <td><code>udf_params</code></td>
      <td><code>JSON String</code></td>
      <td>Additional <Glossary>udf</Glossary>s: <code>udf7</code> for the buyer's <Glossary>iec</Glossary> (Import Export Code) and <code>udf8</code> for the <Glossary>awb</Glossary> (airway bill) or consignment number for goods. If you send it, include it in the hash exactly as sent.</td>
      <td><code>{"udf7":"0100000029","udf8":"99953729071"}</code></td>
    </tr>
    </tbody>
    </table>

    <Callout icon="📘" theme="info">
      ### **Note**

      - Send `udf1` to `udf5` as separate parameters. Don't send `udf6`; it's reserved.
      - Fields from `udf7` onwards, such as the IEC and AWB number, go only inside `udf_params`. Ask PayU to enable additional UDFs for your account before you send `udf_params`.
    </Callout>

    #### Hashing

    -
    - Notes: use empty strings for missing fields, compute server-side, lowercase hex

    <Accordion title="Sample Code for Hashing" icon="far fa-code">
      <HashingSample />
    </Accordion>
  </Tab>

  <Tab title="Sample Request">
    ```html
    <form action="https://test.payu.in/_payment" method="post">
      <input type="hidden" name="key" value="JPM7Fg" />
      <input type="hidden" name="txnid" value="payuTestTxn12345" />
      <input type="hidden" name="amount" value="100.00" />
      <input type="hidden" name="productinfo" value="iPhone" />
      <input type="hidden" name="firstname" value="Ashish" />
      <input type="hidden" name="lastname" value="Kumar" />
      <input type="hidden" name="email" value="test@gmail.com" />
      <input type="hidden" name="phone" value="9876543210" />
      <input type="hidden" name="zipcode" value="110075" />
      <input type="hidden" name="surl" value="https://example.com/success" />
      <input type="hidden" name="furl" value="https://example.com/failure" />
      <input type="hidden" name="udf1" value="AELPR1234E" />
      <input type="hidden" name="udf3" value="02-02-1980" />
      <input type="hidden" name="udf4" value="XYZ Pvt. Ltd." />
      <input type="hidden" name="udf5" value="INV123456" />
      <input type="hidden" name="buyer_type_business" value="1" />
      <input type="hidden" name="udf_params" value='{"udf7":"0100000029","udf8":"99953729071"}' />
      <input type="hidden" name="hash" value="YOUR_GENERATED_HASH" />
      <button type="submit">Pay now</button>
    </form>
    ```
    ```curl
    curl -X POST "https://test.payu.in/_payment" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      --data-urlencode 'key=JPM7Fg' \
      --data-urlencode 'txnid=payuTestTxn12345' \
      --data-urlencode 'amount=100.00' \
      --data-urlencode 'productinfo=iPhone' \
      --data-urlencode 'firstname=Ashish' \
      --data-urlencode 'lastname=Kumar' \
      --data-urlencode 'email=test@gmail.com' \
      --data-urlencode 'phone=9876543210' \
      --data-urlencode 'zipcode=110075' \
      --data-urlencode 'surl=https://example.com/success' \
      --data-urlencode 'furl=https://example.com/failure' \
      --data-urlencode 'udf1=AELPR1234E' \
      --data-urlencode 'udf3=02-02-1980' \
      --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
      --data-urlencode 'udf5=INV123456' \
      --data-urlencode 'buyer_type_business=1' \
      --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
      --data-urlencode 'hash=YOUR_GENERATED_HASH'
    ```
    ```python
    import requests

    url = "https://test.payu.in/_payment"

    payload = {
        "key": "JPM7Fg",
        "txnid": "payuTestTxn12345",
        "amount": "100.00",
        "productinfo": "iPhone",
        "firstname": "Ashish",
        "lastname": "Kumar",
        "email": "test@gmail.com",
        "phone": "9876543210",
        "zipcode": "110075",
        "surl": "https://example.com/success",
        "furl": "https://example.com/failure",
        "udf1": "AELPR1234E",
        "udf3": "02-02-1980",
        "udf4": "XYZ Pvt. Ltd.",
        "udf5": "INV123456",
        "buyer_type_business": "1",
        "udf_params": '{"udf7":"0100000029","udf8":"99953729071"}',
        "hash": "YOUR_GENERATED_HASH"
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(url, data=payload, headers=headers)
    print(response.text)
    ```
    ```php
    <?php
    $url = "https://test.payu.in/_payment";

    $payload = http_build_query([
        "key"                 => "JPM7Fg",
        "txnid"               => "payuTestTxn12345",
        "amount"              => "100.00",
        "productinfo"         => "iPhone",
        "firstname"           => "Ashish",
        "lastname"            => "Kumar",
        "email"               => "test@gmail.com",
        "phone"               => "9876543210",
        "zipcode"             => "110075",
        "surl"                => "https://example.com/success",
        "furl"                => "https://example.com/failure",
        "udf1"                => "AELPR1234E",
        "udf3"                => "02-02-1980",
        "udf4"                => "XYZ Pvt. Ltd.",
        "udf5"                => "INV123456",
        "buyer_type_business" => "1",
        "udf_params"          => '{"udf7":"0100000029","udf8":"99953729071"}',
        "hash"                => "YOUR_GENERATED_HASH"
    ]);

    $ch = curl_init($url);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $payload);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: application/x-www-form-urlencoded"]);
    curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    $response = curl_exec($ch);
    curl_close($ch);
    echo $response;
    ```
    ```java
    import java.net.URI;
    import java.net.http.HttpClient;
    import java.net.http.HttpRequest;
    import java.net.http.HttpResponse;
    import java.net.URLEncoder;
    import java.nio.charset.StandardCharsets;
    import java.util.LinkedHashMap;
    import java.util.Map;
    import java.util.StringJoiner;

    public class PayURequest {
        public static void main(String[] args) throws Exception {
            Map<String, String> params = new LinkedHashMap<>();
            params.put("key",                 "JPM7Fg");
            params.put("txnid",               "payuTestTxn12345");
            params.put("amount",              "100.00");
            params.put("productinfo",         "iPhone");
            params.put("firstname",           "Ashish");
            params.put("lastname",            "Kumar");
            params.put("email",               "test@gmail.com");
            params.put("phone",               "9876543210");
            params.put("zipcode",             "110075");
            params.put("surl",                "https://example.com/success");
            params.put("furl",                "https://example.com/failure");
            params.put("udf1",                "AELPR1234E");
            params.put("udf3",                "02-02-1980");
            params.put("udf4",                "XYZ Pvt. Ltd.");
            params.put("udf5",                "INV123456");
            params.put("buyer_type_business", "1");
            params.put("udf_params",          "{\"udf7\":\"0100000029\",\"udf8\":\"99953729071\"}");
            params.put("hash",                "YOUR_GENERATED_HASH");

            StringJoiner sj = new StringJoiner("&");
            for (Map.Entry<String, String> entry : params.entrySet()) {
                sj.add(URLEncoder.encode(entry.getKey(), StandardCharsets.UTF_8)
                    + "=" + URLEncoder.encode(entry.getValue(), StandardCharsets.UTF_8));
            }

            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://test.payu.in/_payment"))
                .header("Content-Type", "application/x-www-form-urlencoded")
                .POST(HttpRequest.BodyPublishers.ofString(sj.toString()))
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

## Step 2: Check the Response from PayU

PayU posts the response to your `surl` or `furl` in form URL-encoded format (`application/x-www-form-urlencoded`). Check the reverse <Glossary>hash</Glossary> before you update the order:

<ReverseHashing />

<Accordion title="Sample response" icon="fa-reply">
  **Parsed response**

  ```plaintext
  [mihpayid] => 403993715525331373
  [mode] => CC
  [status] => success
  [unmappedstatus] => captured
  [key] => JPM7Fg
  [txnid] => payuTestTxn12345
  [amount] => 100.00
  [discount] => 0.00
  [net_amount_debit] => 100
  [addedon] => 2026-02-03 19:06:55
  [productinfo] => iPhone
  [firstname] => Ashish
  [lastname] => Kumar
  [email] => test@gmail.com
  [phone] => 9876543210
  [udf1] => AELPR1234E
  [udf2] =>
  [udf3] => 02-02-1980
  [udf4] => XYZ Pvt. Ltd.
  [udf5] => INV123456
  [hash] => YOUR_RESPONSE_HASH
  [field9] => Transaction Completed Successfully
  [payment_source] => payu
  [PG_TYPE] => CC-PG
  [bank_ref_num] => 450699821592111537
  [bankcode] => CC
  [error] => E000
  [error_Message] => No Error
  ```
</Accordion>

***

## Step 3: Verify the Payment

After you get the response, reconcile the transaction details. You can verify payments in any of these ways:

<Verify_Payment_Tabs />

***

## Step 4: Update Invoice ID (Conditional)

<Update_Invoice_ID />

***

## Step 5: Upload Invoices and Shipping Documents

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  - Upload the invoice within **10 days** of the transaction. If you don't, your next settlement is put on hold.
  - Goods merchants must upload the invoice and the <Glossary>awb</Glossary> separately, so that's two Invoice Upload calls per payment.
</Callout>

<Upload_Invoices />

***

## Next Steps

<Cards columns="3">
  <Card title="Payment Journey & Workflow" href="/docs/workflow-for-cross-border-payments-import">
    How cross-border settlement works.
  </Card>

  <Card title="Merchant Hosted Cards" href="/docs/plain-cards-integration-one-time-pacb">
    Collect card payments on your own page.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
