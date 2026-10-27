---
title: PACB Import-UPI Intent with S2S Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

This page explains how to collect cross-border UPI payments with the server-to-server UPI Intent flow.

<Cards columns="3">
  <Card title="1. Initiate the Payment" href="#step-1-initiate-the-payment">
    Send the UPI Intent payment request to PayU.
  </Card>

  <Card title="2. Open the Customer's UPI App" href="#step-2-open-the-customers-upi-app">
    Build the UPI deeplink and open it on the customer's device.
  </Card>

  <Card title="3. Check the UPI Transaction Status" href="#step-3-check-the-upi-transaction-status">
    Check the status after the customer pays.
  </Card>

  <Card title="4. Receive the S2S Callback" href="#step-4-receive-the-s2s-callback-from-payu">
    Process the callback PayU sends to your server.
  </Card>

  <Card title="5. Verify the Payment" href="#step-5-verify-the-payment">
    Confirm the final payment status.
  </Card>

  <Card title="6. Update Invoice ID (Conditional)" href="#step-6-update-invoice-id-conditional">
    Add the invoice ID if you didn't send it.
  </Card>

  <Card title="7. Upload Invoices and Shipping Documents" href="#step-7-upload-invoices-and-shipping-documents">
    Required within 10 days of the payment.
  </Card>
</Cards>

<RegisterMerchantPrerequiste />

<Callout icon="❗️" theme="error">
  ### **Important**

  NPCI has disabled UPI Collect, which changes how you integrate UPI:

  - **Android apps:** implement Smart Intent. Refer to [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow), or use the [PayU Android SDKs](doc:explore-android-sdks), which have Smart Intent built in.
  - **iOS apps:** implement the deeplink handling and continue with the UPI flow as it is. For an SDK, refer to [iOS UPI SDK](doc:ios-upi-sdk).
  - **Web:** use the deeplink returned in the API response to generate a QR code that customers scan with their UPI app.

  For built-in Smart Intent support, use the PayU [Android SDKs](doc:explore-android-sdks) or [iOS SDKs](doc:explore-ios-sdks).
</Callout>

{/* REVIEW: the old intent flow diagram was hosted on devguide.payu.in and has been removed. Add an updated diagram. */}

***

## Step 1: Initiate the Payment

Call the `_payment` API from your server with the parameters below.

<PaymentAPIEnvironment />

<Callout icon="📘" theme="info">
  ### **Note**

  - For generic intent, set `bankcode` to `INTENT`.
  - In your own app, you can open the generic intent or a specific app's intent.
  - On mobile web, you can only open the generic intent. To open a specific app on mobile web, you need extra libraries. PayU offers this for Google Pay; refer to the GPay Seamless Integration document.
  - You don't need the customer's UPI ID (VPA) for this flow.
</Callout>

<Tabs>
  <Tab title="Request Parameters">
    For the complete list of parameters, refer to <a href="https://docs.payu.in/reference/_payment_s2s_upi_collection" target="_blank">UPI Collection - S2S</a>.

    #### Mandatory Parameters

    <table>
      <thead>
        <tr>
          <th>
            Parameter
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
            <code>key</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>key</Glossary> Merchant key provided by PayU. To find it, refer to <a href="doc:generate-merchant-key-and-salt-on-payu-dashboard">Access Production Key and Salt</a> or <a href="doc:generate-test-merchant-key-and-salt">Access Test Merchant Key and Salt</a>.
          </td>

          <td>
            <code>JPM7Fg</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>txnid</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>txnid</Glossary> Unique transaction ID: up to 50 characters, letters, numbers and special characters except <code>&gt;</code>, <code>&lt;</code>, <code>=</code>, <code>:</code>, <code>&amp;</code> and <code>'</code>.{/* REVIEW (C25): the Hosted page says 25 characters. */}
          </td>

          <td>
            <code>1234_abcdedf</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>amount</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>amount</Glossary> Payment amount, rounded to two decimal places. Minimum ₹1.00.
          </td>

          <td>
            <code>1000.00</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>phone</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> Customer's 10-digit phone number.
          </td>

          <td>
            <code>9876786756</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>productinfo</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>productinfo</Glossary> Name or short description of the goods or services. For physical goods, include all products. Character limit: 100.
          </td>

          <td>
            iPhone 12
          </td>
        </tr>

        <tr>
          <td>
            <code>firstname</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> Customer's first name. Character limit: 60.
          </td>

          <td>
            Sundar
          </td>
        </tr>

        <tr>
          <td>
            <code>lastname</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> Customer's last name. Character limit: 20.{/* REVIEW (C23): lastname is mandatory here but not on the card pages. */}
          </td>

          <td>
            Teja
          </td>
        </tr>

        <tr>
          <td>
            <code>email</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> Customer's email address.
          </td>

          <td>
            <code>hello@payu.in</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>pg</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>pg</Glossary> Payment category. For UPI Intent, use <code>UPI</code>.
          </td>

          <td>
            <code>UPI</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>bankcode</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>bankcode</Glossary> For UPI Intent, use <code>INTENT</code>.
          </td>

          <td>
            <code>INTENT</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>surl</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>surl</Glossary> Success URL. PayU sends the final response here if the payment succeeds.
          </td>

          <td>
            <code>https://example.com/success</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>furl</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>furl</Glossary> Failure URL. PayU sends the final response here if the payment fails.
          </td>

          <td>
            <code>https://example.com/failure</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>zipcode</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> Customer's PIN code (6 digits).
          </td>

          <td>
            <code>122018</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>txn_s2s_flow</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> Set to <code>4</code>.
          </td>

          <td>
            <code>4</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>s2s_client_ip</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> IP address of the customer's device. Helps with <Glossary>fraud detection</Glossary> and chargebacks, so make sure it's accurate.
          </td>

          <td>
            <code>10.200.12.12</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>s2s_device_info</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> User agent of the customer's device. Helps with fraud detection and chargebacks, so make sure it's accurate.
          </td>

          <td>
            <code>Mozilla/5.0 (Windows NT 10.0; Win64; x64)</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>udf5</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>udf5</Glossary> Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 6. Character limit: 255.
          </td>

          <td>
            <code>INV123456</code>
          </td>
        </tr>

        <tr>
          <td>
            <code>hash</code><br /><code>mandatory</code>
          </td>

          <td>
            <code>String</code> <Glossary>hash</Glossary> SHA-512 hash of the request, used to prevent tampering. See <strong>Hash generation</strong> below.
          </td>

          <td>
            <code>YOUR_GENERATED_HASH</code>
          </td>
        </tr>
      </tbody>
    </table>

    #### Optional Parameters

    <table>
    <thead><tr><th>Parameter</th><th>Description</th><th>Example</th></tr></thead>
    <tbody>
    <tr><td><code>upiAppName</code><br /><code>conditional</code></td><td><code>String</code> For specific intent only: the UPI app the customer picked on your checkout page. Values: <code>phonepe</code>, <code>googlepay</code>, <code>paytm</code>, <code>bhim</code>, <code>cred</code>, <code>amazonpay</code>, <code>whatsapp</code>, or <code>genericintent</code> for any other app.{/* REVIEW: the draft marked this mandatory while describing it as specific-intent only. */}</td><td><code>phonepe</code></td></tr>
    <tr><td><code>address1</code><br /><code>optional</code> (recommended for higher approval rate)</td><td><code>String</code> First line of the customer's address. Character limit: 100.</td><td>PayU, Bestech Business Tower</td></tr>
    <tr><td><code>address2</code><br /><code>optional</code></td><td><code>String</code> Second line of the customer's address. Character limit: 100.</td><td>Sohna Road</td></tr>
    <tr><td><code>city</code><br /><code>optional</code> (recommended for higher approval rate)</td><td><code>String</code> Customer's city. Character limit: 50.</td><td>Gurgaon</td></tr>
    <tr><td><code>state</code><br /><code>optional</code> (recommended for higher approval rate)</td><td><code>String</code> Customer's state. Character limit: 50.</td><td>Haryana</td></tr>
    <tr><td><code>country</code><br /><code>optional</code> (recommended for higher approval rate)</td><td><code>String</code> Customer's country. Character limit: 50.</td><td>India</td></tr>
    <tr><td><code>udf1</code><br /><code>optional</code> (recommended for higher approval rate)</td><td><code>String</code> <Glossary>udf1</Glossary> Buyer's PAN (Permanent Account Number, India's main tax ID). Character limit: 10 alphanumeric characters.</td><td><code>ABCDE1234K</code></td></tr>
    <tr><td><code>udf2</code><br /><code>optional</code></td><td><code>String</code> Any extra information. Character limit: 255.</td><td>-</td></tr>
    <tr><td><code>udf3</code><br /><code>optional</code> (recommended for higher approval rate)</td><td><code>String</code> Buyer's date of birth in DD-MM-YYYY format. Character limit: 255.</td><td><code>02-02-1980</code></td></tr>
    <tr><td><code>udf4</code><br /><code>mandatory for payment aggregators</code></td><td><code>String</code> End merchant's legal entity name. For UPI, this field should not be passed. Character limit: 255.{/* REVIEW (C15): Confluence says "don't pass udf4" applies to UPI Autopay only, and the sample below sends udf4. Confirm the rule for one-time UPI. */}</td><td>XYZ Pvt. Ltd.</td></tr>
    <tr><td><code>buyer_type_business</code><br /><code>optional</code> (B2B transactions)</td><td><code>String</code> Send <code>1</code> if the buyer is a business. Skip it for individual buyers; the default is <code>0</code>. If you send it, include it in the hash.</td><td><code>1</code></td></tr>
    <tr><td><code>udf_params</code><br /><code>optional</code></td><td><code>JSON String</code> Additional UDFs: <code>udf7</code> for the buyer's Import Export Code (IEC) and <code>udf8</code> for the airway bill (AWB) or consignment number for goods. If you send it, include it in the hash exactly as sent.</td><td><code>{"udf7":"0100000029","udf8":"99953729071"}</code></td></tr>
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
    --data-urlencode 'pg=UPI' \
    --data-urlencode 'bankcode=INTENT' \
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
        "pg": "UPI",
        "bankcode": "INTENT",
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
      lastname: "Kumar",
      email: "test@payu.in",
      phone: "9988776655",
      zipcode: "122018",
      surl: "https://test.payu.in/admin/test_response",
      furl: "https://test.payu.in/admin/test_response",
      pg: "UPI",
      bankcode: "INTENT",
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
        'lastname' => 'Kumar',
        'email' => 'test@payu.in',
        'phone' => '9988776655',
        'zipcode' => '122018',
        'surl' => 'https://test.payu.in/admin/test_response',
        'furl' => 'https://test.payu.in/admin/test_response',
        'pg' => 'UPI',
        'bankcode' => 'INTENT',
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
  </Tab>
</Tabs>

<Accordion title="Sample response" icon="fa-reply">
  ```json
  {
    "metaData": {
      "message": null,
      "referenceId": "c99a6455b3e0dc5cd7167ab8c8cc10d2fa153cb509e3f64c6cd0ed9c5b64a8c9",
      "statusCode": null,
      "txnId": "payuTestTransaction12345",
      "txnStatus": "pending",
      "unmappedStatus": "pending"
    },
    "result": {
      "paymentId": "403993715535965242",
      "merchantName": "Test Merchant",
      "merchantVpa": "payutest@hdfcbank",
      "amount": "100.00",
      "intentURIData": "pa=payutest@hdfcbank&pn=TestMerchant&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=100.00&cu=INR&tn=UPIIntent",
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0i...",
      "otpPostUrl": "https://test.payu.in/ResponseHandler.php"
    }
  }
  ```
</Accordion>

***

## Step 2: Open the Customer's UPI App

If `metaData.unmappedStatus` is `pending`, take `result.intentURIData` and add the prefix `upi://pay?`. That gives you the full UPI deeplink:

```plaintext
upi://pay?pa=payutest@hdfcbank&pn=TestMerchant&tr=403993715535965242&tid=PPPL403993715535965242080126220900&am=100.00&cu=INR&tn=UPIIntent
```

Open the deeplink as an intent or a hyperlink on the customer's device. This opens a tray of UPI apps on the device, or a specific app if you chose one. On web, show the deeplink as a QR code instead.

<Callout icon="🚧" theme="warn">
  ### **Critical Rules**

  - Use only the merchant VPA returned in the response. PayU tracks the payment status through it.
  - Don't change the values inside `intentURIData`. The `tid` value lets NPCI block duplicate transactions.
  - Build the deeplink from the response every time; its contents can change.
</Callout>

{/* REVIEW: the draft also described a manual format (pa, pn, tr=referenceId, am). It was removed because intentURIData already contains the full URI and its tr value differs from referenceId. */}

***

## Step 3: Check the UPI Transaction Status

Check the transaction status with the [Verify Payment API](ref:verify_payment_api) (`verify_payment`).

***

## Step 4: Receive the S2S Callback from PayU

PayU also sends a server-to-server callback to your server whenever the transaction status changes.

<Accordion title="How the callback works" icon="fa-code">
  PayU sends the callback to a URL you provide, which PayU configures for your account. The callback is sent as key-value pairs separated by `&`. Unused parameters are sent with empty values.

The parameters are:

```plaintext
mihpayid,mode,status,key,txnid,amount,productinfo,firstname,lastname,address1,address2,city,state,country,zipcode,email,phone,udf1,udf2,udf3,udf4,udf5,udf6,udf7,udf8,udf9,udf10,card_token,card_no,field0,field1,field2,field3,field4,field5,field6,field7,field8,field9,offer,discount,offer_availed,unmappedstatus,hash,bank_ref_no,surl,curl,furl,card_hash
```

{/* REVIEW: the draft's sample callback was a domestic debit-card payment and was removed. Add a UPI Intent callback sample. */}

</Accordion>

***

## Step 5: Verify the Payment

Use webhooks to verify the payment. For sample payloads, refer to [Webhook Events and Sample Payloads](doc:webhook-events-and-sample-payloads).

{/* REVIEW: the draft's sample webhook belonged to a static-QR payment from another merchant and was removed. Add a UPI Intent webhook sample. */}

<Accordion title="Callback response parameters" icon="fa-table">
  | Parameter     | Description                                          |
  | ------------- | ---------------------------------------------------- |
  | `status`      | Transaction status: `success` or `failure`.          |
  | `txnid`       | Your transaction ID.                                 |
  | `mihpayid`    | PayU transaction ID.                                 |
  | `amount`      | Transaction amount.                                  |
  | `productinfo` | Product information.                                 |
  | `hash`        | Response hash. Check it before you update the order. |
</Accordion>

***

## Step 6: Update Invoice ID (Conditional)

<Update_Invoice_ID />

***

## Step 7: Upload Invoices and Shipping Documents

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  - Upload the invoice within **10 days** of the transaction. If you don't, your next settlement is put on hold.
  - Goods merchants must upload the invoice and the airway bill (AWB) separately, so that's two Invoice Upload calls per payment.
</Callout>

<Upload_Invoices />

***

## Next Steps

<Cards columns="3">
  <Card title="NetBanking Integration" href="/docs/netbanking-integration-merchant-hosted-integration-cb">
    Accept NetBanking payments.
  </Card>

  <Card title="UPI Autopay" href="/docs/index">
    Collect recurring UPI payments.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
