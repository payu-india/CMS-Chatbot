---
title: PACB Import-Plain Cards Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

This page explains how to collect plain card payments for <Glossary>cross-border payments</Glossary> with the <Glossary>server-to-server (S2S)</Glossary> flow. This is the standard card flow, without tokenization.

<Cards columns="3">
  <Card title="1. Post Parameters to PayU" href="#step-1-post-parameters-to-payu">
    Send the card payment request to PayU.
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

  - A PayU merchant account enabled for cross-border payments.
  - Your <Glossary>merchant key</Glossary> and <Glossary>salt</Glossary> for the test and production environments.
  - A server that can make S2S calls. Never generate the <Glossary>hash</Glossary> in a browser or app.
</Callout>

***

## Step 1: Post Parameters to PayU

Post the payment parameters to PayU's `_payment` API to start a plain card transaction.

<Callout icon="📘" theme="info">
  ### **Note**

  For more information, refer to <Anchor target="_blank" href="ref:one-time-payment-for-cards-pacb-integration">One-Time Payment for Cards - CB</Anchor>.
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

    | Parameter                          | Description                                                                                                                                  | Example                                     |
    | ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
    | `key`<br />`mandatory`             | `String` <Glossary>Merchant key</Glossary> provided by PayU during onboarding.                                                               | `JPM7Fg`                                    |
    | `txnid`<br />`mandatory`           | `String` Unique <Glossary>transaction ID</Glossary> that you generate for the order.                                                         | `payuTestTxn12345`                          |
    | `amount`<br />`mandatory`          | `String` Payment amount.                                                                                                                     | `100.00`                                    |
    | `productinfo`<br />`mandatory`     | `String` Name or short description of the goods or services. For physical goods, include all products. Character limit: 100.                 | `iPhone`                                    |
    | `firstname`<br />`mandatory`       | `String` Customer's first name. Character limit: 60.                                                                                         | `Ashish`                                    |
    | `email`<br />`mandatory`           | `String` Customer's email address. Character limit: 50.                                                                                      | `test@gmail.com`                            |
    | `phone`<br />`mandatory`           | `String` Customer's phone number.                                                                                                            | `9876543210`                                |
    | `zipcode`<br />`mandatory`         | `String` Billing postal code. Character limit: 6 digits (India PIN code).                                                                    | `110075`                                    |
    | `surl`<br />`mandatory`            | `String` Success URL. PayU sends the customer here if the payment succeeds.                                                                  | `https://example.com/success`               |
    | `furl`<br />`mandatory`            | `String` Failure URL. PayU sends the customer here if the payment fails.                                                                     | `https://example.com/failure`               |
    | `pg`<br />`mandatory`              | `String` Payment category. For cards, use `CC`.                                                                                              | `CC`                                        |
    | `bankcode`<br />`mandatory`        | `String` Bank code. Use `CC` for credit cards and `DC` for debit cards.                                                                      | `CC`                                        |
    | `ccnum`<br />`mandatory`           | `String` Card number: 13–19 digits (15 for AMEX, 13–19 for Maestro). Validate it with the <Glossary>Luhn algorithm</Glossary>.               | `5506900480000008`                          |
    | `ccvv`<br />`mandatory`            | `String` <Glossary>CVV</Glossary>: 3 digits (4 for AMEX).                                                                                    | `123`                                       |
    | `ccname`<br />`mandatory`          | `String` Cardholder name as entered by the customer.                                                                                         | `Test User`                                 |
    | `ccexpmon`<br />`mandatory`        | `String` Card expiry month in MM format (01–12).                                                                                             | `09`                                        |
    | `ccexpyr`<br />`mandatory`         | `String` Card expiry year in YYYY format.                                                                                                    | `2030`                                      |
    | `txn_s2s_flow`<br />`mandatory`    | `String` Set to `4` for the <Glossary>server-to-server (S2S)</Glossary> flow.                                                                | `4`                                         |
    | `s2s_client_ip`<br />`mandatory`   | `String` IP address of the customer's device. Used for <Glossary>fraud detection</Glossary>.                                                 | `10.200.12.12`                              |
    | `s2s_device_info`<br />`mandatory` | `String` User agent of the customer's device.                                                                                                | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
    | `udf5`<br />`mandatory`            | `String` Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 4. Character limit: 255. | `INV123456`                                 |
    | `hash`<br />`mandatory`            | `String` SHA-512 <Glossary>hash</Glossary> of the request. See **Hash generation** below.                                                    | `YOUR_GENERATED_HASH`                       |

    #### Optional Parameters

    | Parameter                                                         | Description                                                                                                                                                                                                                       | Example                                      |
    | ----------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
    | `address1`<br />`optional` (recommended for higher approval rate) | `String` First line of the <Glossary>billing address</Glossary>. Used for billing and <Glossary>fraud detection</Glossary>. Character limit: 255.                                                                                 | `123 Main Street`                            |
    | `address2`<br />`optional`                                        | `String` Second line of the billing address. Character limit: 255.                                                                                                                                                                | `Anytown`                                    |
    | `city`<br />`optional` (recommended for higher approval rate)     | `String` Billing city. Character limit: 50.                                                                                                                                                                                       | `New Delhi`                                  |
    | `state`<br />`optional` (recommended for higher approval rate)    | `String` Billing state or province. Character limit: 50.                                                                                                                                                                          | `Delhi`                                      |
    | `country`<br />`optional` (recommended for higher approval rate)  | `String` Billing country as an ISO 3166-1 alpha-2 code. Character limit: 2.                                                                                                                                                       | `IN`                                         |
    | `udf1`<br />`optional` (recommended for higher approval rate)     | `String` Buyer's <Glossary>PAN</Glossary> (Permanent Account Number, India's main tax ID). Character limit: 10 alphanumeric characters.                                                                                           | `ABCDE1234K`                                 |
    | `udf2`<br />`optional`                                            | `String` Any extra information about the transaction. Character limit: 255.                                                                                                                                                       | `Additional transaction data`                |
    | `udf3`<br />`optional` (recommended for higher approval rate)     | `String` Buyer's date of birth in DD-MM-YYYY format.                                                                                                                                                                              | `02-02-1980`                                 |
    | `udf4`<br />`mandatory for payment aggregators`                   | `String` End merchant's legal entity name. Character limit: 255.                                                                                                                                                                  | `XYZ Pvt. Ltd.`                              |
    | `buyer_type_business`<br />`optional` (B2B transactions)          | `String` Send `1` if the buyer is a business. Skip it for individual buyers; the default is `0`. If you send it, include it in the hash.                                                                                          | `1`                                          |
    | `udf_params`<br />`optional`                                      | `JSON String` Additional UDFs: `udf7` for the buyer's Import Export Code (IEC) and `udf8` for the <Glossary>airway bill (AWB)</Glossary> or consignment number for goods. If you send it, include it in the hash exactly as sent. | `{"udf7":"0100000029","udf8":"99953729071"}` |

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
    --data-urlencode 'address1=123 Main Street' \
    --data-urlencode 'city=New York' \
    --data-urlencode 'state=NY' \
    --data-urlencode 'country=US' \
    --data-urlencode 'zipcode=10001' \
    --data-urlencode 'surl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'furl=https://test.payu.in/admin/test_response' \
    --data-urlencode 'pg=CC' \
    --data-urlencode 'bankcode=CC' \
    --data-urlencode 'ccnum=5506900480000008' \
    --data-urlencode 'ccname=Test User' \
    --data-urlencode 'ccvv=123' \
    --data-urlencode 'ccexpmon=09' \
    --data-urlencode 'ccexpyr=2030' \
    --data-urlencode 'udf1=AELPR1234E' \
    --data-urlencode 'udf2=' \
    --data-urlencode 'udf3=02-02-1980' \
    --data-urlencode 'udf4=XYZ Pvt. Ltd.' \
    --data-urlencode 'udf5=INV123456' \
    --data-urlencode 'buyer_type_business=1' \
    --data-urlencode 'udf_params={"udf7":"0100000029","udf8":"99953729071"}' \
    --data-urlencode 'txn_s2s_flow=4' \
    --data-urlencode 's2s_client_ip=10.200.12.12' \
    --data-urlencode 's2s_device_info=Mozilla/5.0 (Windows NT 10.0; Win64; x64)' \
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
        "address1": "123 Main Street",
        "city": "New York",
        "state": "NY",
        "country": "US",
        "zipcode": "10001",
        "surl": "https://test.payu.in/admin/test_response",
        "furl": "https://test.payu.in/admin/test_response",
        "pg": "CC",
        "bankcode": "CC",
        "ccnum": "5506900480000008",
        "ccname": "Test User",
        "ccvv": "123",
        "ccexpmon": "09",
        "ccexpyr": "2030",
        "udf1": "AELPR1234E",
        "udf2": "",
        "udf3": "02-02-1980",
        "udf4": "XYZ Pvt. Ltd.",
        "udf5": "INV123456",
        "buyer_type_business": "1",
        "udf_params": '{"udf7":"0100000029","udf8":"99953729071"}',
        "txn_s2s_flow": "4",
        "s2s_client_ip": "10.200.12.12",
        "s2s_device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
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
      address1: "123 Main Street",
      city: "New York",
      state: "NY",
      country: "US",
      zipcode: "10001",
      surl: "https://test.payu.in/admin/test_response",
      furl: "https://test.payu.in/admin/test_response",
      pg: "CC",
      bankcode: "CC",
      ccnum: "5506900480000008",
      ccname: "Test User",
      ccvv: "123",
      ccexpmon: "09",
      ccexpyr: "2030",
      udf1: "AELPR1234E",
      udf2: "",
      udf3: "02-02-1980",
      udf4: "XYZ Pvt. Ltd.",
      udf5: "INV123456",
      buyer_type_business: "1",
      udf_params: '{"udf7":"0100000029","udf8":"99953729071"}',
      txn_s2s_flow: "4",
      s2s_client_ip: "10.200.12.12",
      s2s_device_info: "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
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
        'address1' => '123 Main Street',
        'city' => 'New York',
        'state' => 'NY',
        'country' => 'US',
        'zipcode' => '10001',
        'surl' => 'https://test.payu.in/admin/test_response',
        'furl' => 'https://test.payu.in/admin/test_response',
        'pg' => 'CC',
        'bankcode' => 'CC',
        'ccnum' => '5506900480000008',
        'ccname' => 'Test User',
        'ccvv' => '123',
        'ccexpmon' => '09',
        'ccexpyr' => '2030',
        'udf1' => 'AELPR1234E',
        'udf2' => '',
        'udf3' => '02-02-1980',
        'udf4' => 'XYZ Pvt. Ltd.',
        'udf5' => 'INV123456',
        'buyer_type_business' => '1',
        'udf_params' => '{"udf7":"0100000029","udf8":"99953729071"}',
        'txn_s2s_flow' => '4',
        's2s_client_ip' => '10.200.12.12',
        's2s_device_info' => 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
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

<Accordion title="Response parameters" icon="fa-table">
    

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
          <code>metaData</code>
        </td>

        <td>
          <code>Object</code> Transaction metadata.
        </td>

        <td>
          -
        </td>
      </tr>

      <tr>
        <td>
          <code>metaData.referenceId</code>
        </td>

        <td>
          <code>String</code> PayU reference ID. Send it back in later calls, such as Submit OTP.
        </td>

        <td>
          <code>5a3e7cb9884e003d...</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>metaData.txnId</code>
        </td>

        <td>
          <code>String</code> Your transaction ID.
        </td>

        <td>
          <code>payuTestTransaction12345</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>metaData.txnStatus</code>
        </td>

        <td>
          <code>String</code> Transaction status, for example <code>Enrolled</code>.
        </td>

        <td>
          <code>Enrolled</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>metaData.unmappedStatus</code>
        </td>

        <td>
          <code>String</code> Status to drive your flow: <code>pending</code>, <code>captured</code> or <code>failed</code>.
        </td>

        <td>
          <code>pending</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>result.otpPostUrl</code>
        </td>

        <td>
          <code>String</code> URL to post the <Glossary>OTP</Glossary> to.
        </td>

        <td>
          <code>https://test.payu.in/ResponseHandler.php</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>result.acsTemplate</code>
        </td>

        <td>
          <code>String</code> Base64-encoded HTML form that redirects the customer to the bank's page.
        </td>

        <td>
          <code>PGh0bWw+PGJvZHk+...</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>binData.pureS2SSupported</code>
        </td>

        <td>
          <code>Boolean</code> Whether you can collect the OTP on your own page.
        </td>

        <td>
          <code>true</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>binData.issuingBank</code>
        </td>

        <td>
          <code>String</code> Card issuing bank.
        </td>

        <td>
          <code>AXIS</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>binData.category</code>
        </td>

        <td>
          <code>String</code><code>creditcard</code> or <code>debitcard</code>.
        </td>

        <td>
          <code>creditcard</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>binData.cardType</code>
        </td>

        <td>
          <code>String</code> Card network: <code>VISA</code>, <code>MAST</code> or <code>RUPAY</code>.
        </td>

        <td>
          <code>MAST</code>
        </td>
      </tr>

      <tr>
        <td>
          <code>binData.isDomestic</code>
        </td>

        <td>
          <code>Boolean</code> Whether the card was issued in India.
        </td>

        <td>
          <code>true</code>
        </td>
      </tr>
    </tbody>
  </table>
</Accordion>

<Accordion title="Sample response" icon="fa-reply">
  ```json
  {
    "metaData": {
      "message": null,
      "referenceId": "5a3e7cb9884e003dce1f28f965478a9a12fb9244fc15be91b0b3de48763a12e7",
      "statusCode": null,
      "txnId": "payuTestTransaction12345",
      "txnStatus": "Enrolled",
      "unmappedStatus": "pending",
      "resendOtp": {
        "isSupported": true,
        "attemptsLeft": 2
      },
      "submitOtp": {
        "attemptsLeft": 3
      }
    },
    "result": {
      "otpPostUrl": "https://test.payu.in/ResponseHandler.php",
      "acsTemplate": "PGh0bWw+PGJvZHk+PGZvcm0gbmFtZT0icGF5bWVudF9wb3N0IiBpZD0i..."
    },
    "binData": {
      "pureS2SSupported": true,
      "issuingBank": "AXIS",
      "category": "creditcard",
      "cardType": "MAST",
      "isDomestic": true
    }
  }
  ```
</Accordion>

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
  - Goods merchants must upload the invoice and the <Glossary>airway bill (AWB)</Glossary> separately, so that's two Invoice Upload calls per payment.
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
    Save the card while you take the payment.
  </Card>

  <Card title="Saved Cards with a PayU Token" href="/docs/cards-with-payu-tokenization-one-time-pacb">
    Charge a card the customer saved earlier.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
