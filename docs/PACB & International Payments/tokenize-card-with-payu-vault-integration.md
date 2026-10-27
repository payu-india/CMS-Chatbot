---
title: Tokenize Card with PayU Vault Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

This page explains how to collect a cross-border card payment and save the card in the PayU vault at the same time. Next time, the customer can pay with the saved card. To charge a saved card, see [Saved Cards with a PayU Token Integration](/docs/cards-with-payu-tokenization-one-time-pacb).

<Cards columns="3">
  <Card title="1. Post Parameters to PayU" href="#step-1-post-parameters-to-payu">
    Send the card details and ask PayU to save the card.
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

  - A PayU merchant account enabled for cross-border payments and card saving.
  - Your merchant key and salt for the test and production environments.
  - The customer's consent to save their card.
  - A unique customer ID that you'll use every time this customer pays.
</Callout>

***

## Step 1: Post Parameters to PayU

Post the full card details to PayU's `_payment` API, with `store_card=1` and the customer's `user_credentials`. PayU takes the payment and saves the card.

<Callout icon="📘" theme="info">
  ### **Note**

  - For more information on cross-border card payments, refer to <Anchor target="_blank" href="ref:one-time-payment-for-cards-pacb-integration">One-Time Payment for Cards - CB</Anchor>.
  - For more information on saving cards with the PayU vault, refer to [Using Card Tokenized with PayU](ref:using-card-tokenized-with-payu).
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

    | Parameter                                  | Description                                                                                                                                                       | Example                                     |
    | ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- |
    | <Glossary>key</Glossary><br />`mandatory`  | `String` Merchant key provided by PayU during onboarding.                                                                                                         | `JPM7Fg`                                    |
    | `txnid`<br />`mandatory`                   | `String` Unique transaction ID that you generate for the order.                                                                                                   | `payuTestTxn12345`                          |
    | `amount`<br />`mandatory`                  | `String` Payment amount.                                                                                                                                          | `100.00`                                    |
    | `productinfo`<br />`mandatory`             | `String` Name or short description of the goods or services. For physical goods, include all products. Character limit: 100.                                      | `iPhone`                                    |
    | `firstname`<br />`mandatory`               | `String` Customer's first name. Character limit: 60.                                                                                                              | `Ashish`                                    |
    | `email`<br />`mandatory`                   | `String` Customer's email address. Character limit: 50.                                                                                                           | `test@gmail.com`                            |
    | `phone`<br />`mandatory`                   | `String` Customer's phone number.                                                                                                                                 | `9876543210`                                |
    | `zipcode`<br />`mandatory`                 | `String` Billing postal code. Character limit: 6 digits (India PIN code).                                                                                         | `110075`                                    |
    | <Glossary>surl</Glossary><br />`mandatory` | `String` Success URL. PayU sends the customer here if the payment succeeds.                                                                                       | `https://example.com/success`               |
    | <Glossary>furl</Glossary><br />`mandatory` | `String` Failure URL. PayU sends the customer here if the payment fails.                                                                                          | `https://example.com/failure`               |
    | `pg`<br />`mandatory`                      | `String` Payment category. For cards, use `CC`.                                                                                                                   | `CC`                                        |
    | `bankcode`<br />`mandatory`                | `String` Bank code. Use `CC` for credit cards and `DC` for debit cards.                                                                                           | `CC`                                        |
    | `ccnum`<br />`mandatory`                   | `String` Card number: 13–19 digits. Validate it with the Luhn algorithm.                                                                                          | `5506900480000008`                          |
    | `ccname`<br />`mandatory`                  | `String` Cardholder name as entered by the customer.                                                                                                              | `Ashish`                                    |
    | `ccvv`<br />`mandatory`                    | `String` CVV entered by the customer: 3 digits (4 for AMEX).                                                                                                      | `123`                                       |
    | `ccexpmon`<br />`mandatory`                | `String` Card expiry month in MM format (01–12).                                                                                                                  | `10`                                        |
    | `ccexpyr`<br />`mandatory`                 | `String` Card expiry year in YYYY format.                                                                                                                         | `2030`                                      |
    | `store_card`<br />`mandatory`              | `String` Set to `1` to save the card in the PayU vault.                                                                                                           | `1`                                         |
    | `user_credentials`<br />`mandatory`        | `String` Identifies the customer the card belongs to, in the format `merchant_key:customer_id`. Use the same value whenever this customer pays with a saved card. | `JPM7Fg:customer_1112`                      |
    | `txn_s2s_flow`<br />`mandatory`            | `String` Set to `4` for the server-to-server flow.                                                                                                                | `4`                                         |
    | `s2s_client_ip`<br />`mandatory`           | `String` IP address of the customer's device. Used for <Glossary>fraud detection</Glossary>.                                                                      | `10.200.12.12`                              |
    | `s2s_device_info`<br />`mandatory`         | `String` User agent of the customer's device.                                                                                                                     | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
    | `udf5`<br />`mandatory`                    | `String` Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 4. Character limit: 255.                      | `INV123456`                                 |
    | <Glossary>hash</Glossary><br />`mandatory` | `String` SHA-512 hash of the request. See **Hash generation** below.                                                                                              | `YOUR_GENERATED_HASH`                       |

    #### Optional Parameters

    | Parameter                                                         | Description                                                                                                                                                                                                  | Example                                      |
    | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
    | `address1`<br />`optional` (recommended for higher approval rate) | `String` First line of the billing address. Used for billing and fraud prevention. Character limit: 255.                                                                                                     | `123 Main Street`                            |
    | `address2`<br />`optional`                                        | `String` Second line of the billing address. Character limit: 255.                                                                                                                                           | `Anytown`                                    |
    | `city`<br />`optional` (recommended for higher approval rate)     | `String` Billing city. Character limit: 50.                                                                                                                                                                  | `New Delhi`                                  |
    | `state`<br />`optional` (recommended for higher approval rate)    | `String` Billing state or province. Character limit: 50.                                                                                                                                                     | `Delhi`                                      |
    | `country`<br />`optional` (recommended for higher approval rate)  | `String` Billing country as an ISO 3166-1 alpha-2 code. Character limit: 2.                                                                                                                                  | `IN`                                         |
    | `udf1`<br />`optional` (recommended for higher approval rate)     | `String` Buyer's PAN (Permanent Account Number, India's main tax ID). Character limit: 10 alphanumeric characters.                                                                                           | `ABCDE1234K`                                 |
    | `udf2`<br />`optional`                                            | `String` Any extra information about the transaction. Character limit: 255.                                                                                                                                  | `Additional transaction data`                |
    | `udf3`<br />`optional` (recommended for higher approval rate)     | `String` Buyer's date of birth in DD-MM-YYYY format.                                                                                                                                                         | `02-02-1980`                                 |
    | `udf4`<br />`mandatory for payment aggregators`                   | `String` End merchant's legal entity name. Character limit: 255.                                                                                                                                             | `XYZ Pvt. Ltd.`                              |
    | `buyer_type_business`<br />`optional` (B2B transactions)          | `String` Send `1` if the buyer is a business. Skip it for individual buyers; the default is `0`. If you send it, include it in the hash.                                                                     | `1`                                          |
    | `udf_params`<br />`optional`                                      | `JSON String` Additional UDFs: `udf7` for the buyer's Import Export Code (IEC) and `udf8` for the airway bill (AWB) or consignment number for goods. If you send it, include it in the hash exactly as sent. | `{"udf7":"0100000029","udf8":"99953729071"}` |

    <Callout icon="📘" theme="info">
      ### **Note**

      - Send `udf1` to `udf5` as separate parameters. Don't send `udf6`; it's reserved.
      - Fields from `udf7` onwards, such as the IEC and AWB number, go only inside `udf_params`. Ask PayU to enable additional UDFs for your account before you send `udf_params`.
      - After the payment succeeds, get the saved card's token with the [Get User Cards API](ref:get_user_cards_api), using the same `user_credentials`.
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
    --data-urlencode 'ccname=Ashish' \
    --data-urlencode 'ccvv=123' \
    --data-urlencode 'ccexpmon=10' \
    --data-urlencode 'ccexpyr=2030' \
    --data-urlencode 'store_card=1' \
    --data-urlencode 'user_credentials=JPM7Fg:customer_1112' \
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
        "ccnum": "5506900480000008",
        "ccname": "Ashish",
        "ccvv": "123",
        "ccexpmon": "10",
        "ccexpyr": "2030",
        "store_card": "1",
        "user_credentials": "JPM7Fg:customer_1112",
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
      ccnum: "5506900480000008",
      ccname: "Ashish",
      ccvv: "123",
      ccexpmon: "10",
      ccexpyr: "2030",
      store_card: "1",
      user_credentials: "JPM7Fg:customer_1112",
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
        'ccnum' => '5506900480000008',
        'ccname' => 'Ashish',
        'ccvv' => '123',
        'ccexpmon' => '10',
        'ccexpyr' => '2030',
        'store_card' => '1',
        'user_credentials' => 'JPM7Fg:customer_1112',
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
  <Card title="Saved Cards with a PayU Token" href="/docs/cards-with-payu-tokenization-one-time-pacb">
    Charge the card you just saved.
  </Card>

  <Card title="Plain Cards Integration" href="/docs/plain-cards-integration-one-time-pacb">
    Take a card payment without saving the card.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
