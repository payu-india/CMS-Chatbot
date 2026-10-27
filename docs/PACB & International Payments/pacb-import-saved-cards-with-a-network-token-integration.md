---
title: PACB-Import-Saved Cards with a Network Token Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Developer integration required: server-to-server API</Banner>

This page explains how to collect cross-border card payments with network tokens (Visa or Mastercard tokens). Network tokens are more secure than storing card numbers and can improve approval rates.

<Callout icon="📘" theme="info">
  ### **Prerequisites**

  1. Network token details from your token provider (Visa VTS or Mastercard MDES).
  2. The token details: `last4Digits`, `tavv`, `trid` and `tokenRefNo`.
  3. The token's expiry date, which is different from the card's expiry date.
</Callout>

<Cards columns="3">
  <Card title="1. Post Parameters to PayU" href="#step-1-post-parameters-to-payu">
    Send the network token and cryptogram.
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

***

## Step 1: Post Parameters to PayU

Post the payment parameters to PayU's `_payment` API with the network token details.

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
    | <Glossary>key</Glossary>           | `String` Merchant key provided by PayU during onboarding.                                                                                    | `JPM7Fg`                                    |
    | <Glossary>txnid</Glossary>         | `String` Unique transaction ID that you generate for the order.                                                                              | `payuTestTxn12345`                          |
    | <Glossary>amount</Glossary>        | `String` Payment amount.                                                                                                                     | `100.00`                                    |
    | <Glossary>productinfo</Glossary>   | `String` Name or short description of the goods or services. For physical goods, include all products. Character limit: 100.                 | `iPhone`                                    |
    | <Glossary>firstname</Glossary>     | `String` Customer's first name. Character limit: 60.                                                                                         | `Ashish`                                    |
    | <Glossary>email</Glossary>         | `String` Customer's email address. Character limit: 50.                                                                                      | `test@gmail.com`                            |
    | <Glossary>phone</Glossary>         | `String` Customer's phone number.                                                                                                            | `9876543210`                                |
    | <Glossary>zipcode</Glossary>       | `String` Billing postal code. 6-digit numeric.                                                                                               | `110075`                                    |
    | <Glossary>surl</Glossary>          | `String` Success URL. PayU sends the customer here if the payment succeeds.                                                                  | `https://example.com/success`               |
    | <Glossary>furl</Glossary>          | `String` Failure URL. PayU sends the customer here if the payment fails.                                                                     | `https://example.com/failure`               |
    | `pg`                               | `String` Payment category. For cards, use `CC`.                                                                                              | `CC`                                        |
    | `bankcode`                         | `String` Bank code. Use `CC` for credit cards and `DC` for debit cards.                                                                      | `CC`                                        |
    | `ccexpmon`                         | `String` **Token** expiry month in MM format (01–12). Don't use the card's expiry.                                                           | `09`                                        |
    | `ccexpyr`                          | `String` **Token** expiry year in YYYY format. Don't use the card's expiry.                                                                  | `2030`                                      |
    | `storecard_token_type`             | `String` Token type. Set to `1` for network tokens.                                                                                          | `1`                                         |
    | `store_card_token`                 | `String` Network token (DPAN) from the token provider.                                                                                       | `5506900495826660`                          |
    | `additional_info`                  | `JSON String` Network token cryptogram and details. See **additional_info object** below.                                                    | See below                                   |
    | `txn_s2s_flow`                     | `String` Set to `4` for the server-to-server flow.                                                                                           | `4`                                         |
    | <Glossary>s2s_client_ip</Glossary> | `String` IP address of the customer's device. Used for fraud detection.                                                                      | `10.200.12.12`                              |
    | `s2s_device_info`                  | `String` User agent of the customer's device.                                                                                                | `Mozilla/5.0 (Windows NT 10.0; Win64; x64)` |
    | `udf5`                             | `String` Invoice ID, as shown on the invoice issued to the customer. If you don't have it yet, add it later in Step 4. Character limit: 255. | `INV123456`                                 |
    | <Glossary>hash</Glossary>          | `String` SHA-512 hash of the request. See **Hash generation** below.                                                                         | `YOUR_GENERATED_HASH`                       |

    #### Optional Parameters

    | Parameter                 | Description                                                                                                                                                                                                  | Example                                      |
    | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- |
    | `address1`                | `String` First line of the billing address. Used for billing and fraud prevention. Recommended for higher approval rate. Character limit: 255.                                                               | `123 Main Street`                            |
    | `address2`                | `String` Second line of the billing address. Character limit: 255.                                                                                                                                           | `Anytown`                                    |
    | `city`                    | `String` Billing city. Recommended for higher approval rate. Character limit: 50.                                                                                                                            | `New Delhi`                                  |
    | `state`                   | `String` Billing state or province. Recommended for higher approval rate. Character limit: 50.                                                                                                               | `Delhi`                                      |
    | `country`                 | `String` Billing country as an ISO 3166-1 alpha-2 code. Recommended for higher approval rate. Character limit: 2.                                                                                            | `IN`                                         |
    | `ccvv`                    | `String` CVV: 3 digits (4 for AMEX).                                                                                                                                                                         | `123`                                        |
    | <Glossary>udf1</Glossary> | `String` Buyer's PAN (Permanent Account Number, India's main tax ID). Recommended for higher approval rate. Character limit: 10 alphanumeric characters.                                                     | `ABCDE1234K`                                 |
    | `udf2`                    | `String` Any extra information about the transaction. Character limit: 255.                                                                                                                                  | `Additional transaction data`                |
    | `udf3`                    | `String` Buyer's date of birth in DD-MM-YYYY format. Recommended for higher approval rate.                                                                                                                   | `02-02-1980`                                 |
    | `udf4`                    | `String` End merchant's legal entity name. **Mandatory for payment aggregators.** Character limit: 255.                                                                                                      | `XYZ Pvt. Ltd.`                              |
    | `buyer_type_business`     | `String` Send `1` if the buyer is a business. Skip it for individual buyers; the default is `0`. If you send it, include it in the hash. (B2B transactions)                                                  | `1`                                          |
    | `udf_params`              | `JSON String` Additional UDFs: `udf7` for the buyer's Import Export Code (IEC) and `udf8` for the airway bill (AWB) or consignment number for goods. If you send it, include it in the hash exactly as sent. | `{"udf7":"0100000029","udf8":"99953729071"}` |

    <Accordion title="additional_info object" icon="fa-list">
      | Parameter     | Description                                               | Example                                            |
      | ------------- | --------------------------------------------------------- | -------------------------------------------------- |
      | `last4Digits` | `String` Last 4 digits of the original card number.       | `0008`                                             |
      | `tavv`        | `String` Token cryptogram (TAVV) from the card network.   | `UAQAAAAMKJAQg+w+0IagAAAAAAAA`                     |
      | `trid`        | `String` Token Requestor ID assigned by the card network. | `400000340044`                                     |
      | `tokenRefNo`  | `String` Token reference number from the token provider.  | `DM4MMC1US00000003e1ebda85d81490d97cdc87975c7c3bc` |

      ```json
      {
        "last4Digits": "0008",
        "tavv": "UAQAAAAMKJAQg+w+0IagAAAAAAAA",
        "trid": "400000340044",
        "tokenRefNo": "DM4MMC1US00000003e1ebda85d81490d97cdc87975c7c3bc"
      }
      ```
    </Accordion>

    <Callout icon="🚧" theme="warn">
      ### **Critical Rules**

      - Send the **token** expiry in `ccexpmon` and `ccexpyr`, not the card's expiry.
      - Send the network token (DPAN) in `store_card_token`, never the card number.
      - Generate a fresh `tavv` cryptogram for each transaction.
      - Don't send `user_credentials`. It's only used for PayU tokens.
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
      - For more information, refer to [Generate Hash](doc:generate-hash-merchant-hosted).
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
    --data-urlencode 'ccexpmon=09' \
    --data-urlencode 'ccexpyr=2030' \
    --data-urlencode 'storecard_token_type=1' \
    --data-urlencode 'store_card_token=5506900495826660' \
    --data-urlencode 'additional_info={"last4Digits":"0008","tavv":"UAQAAAAMKJAQg+w+0IagAAAAAAAA","trid":"400000340044","tokenRefNo":"DM4MMC1US00000003e1ebda85d81490d97cdc87975c7c3bc"}' \
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
    import json
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
        "ccexpmon": "09",
        "ccexpyr": "2030",
        "storecard_token_type": "1",
        "store_card_token": "5506900495826660",
        "additional_info": json.dumps({
            "last4Digits": "0008",
            "tavv": "UAQAAAAMKJAQg+w+0IagAAAAAAAA",
            "trid": "400000340044",
            "tokenRefNo": "DM4MMC1US00000003e1ebda85d81490d97cdc87975c7c3bc",
        }),
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
      ccexpmon: "09",
      ccexpyr: "2030",
      storecard_token_type: "1",
      store_card_token: "5506900495826660",
      additional_info: JSON.stringify({
        last4Digits: "0008",
        tavv: "UAQAAAAMKJAQg+w+0IagAAAAAAAA",
        trid: "400000340044",
        tokenRefNo: "DM4MMC1US00000003e1ebda85d81490d97cdc87975c7c3bc",
      }),
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
        'ccexpmon' => '09',
        'ccexpyr' => '2030',
        'storecard_token_type' => '1',
        'store_card_token' => '5506900495826660',
        'additional_info' => json_encode([
            'last4Digits' => '0008',
            'tavv' => 'UAQAAAAMKJAQg+w+0IagAAAAAAAA',
            'trid' => '400000340044',
            'tokenRefNo' => 'DM4MMC1US00000003e1ebda85d81490d97cdc87975c7c3bc',
        ]),
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
    Pay with a card saved in the PayU vault.
  </Card>

  <Card title="Direct Authorization" href="/docs/pacb-direct-authorization-cards-integration">
    Authorize payments you've already authenticated.
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers about UDFs, invoices and settlement.
  </Card>
</Cards>
