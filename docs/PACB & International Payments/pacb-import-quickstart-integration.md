---
title: PACB Import - QuickStart Integration
deprecated: false
hidden: true
metadata:
  robots: index
---
<Banner color="#FFC107">Minimal technical setup required</Banner>

This quick start gets you from zero to your first **test** cross-border import payment. You send the customer to PayU Hosted Checkout, where they pay in INR with an Indian card, NetBanking or UPI. PayU then settles the payment to you in your currency.

<Callout icon="📘" theme="info">
  ### **Note**

  This page covers the shortest path: PayU Hosted Checkout with the mandatory cross-border fields only. For every parameter, the optional B2B and Import/Export Code fields, and invoice uploads, refer to [PayU Hosted Payment Integration](/docs/cb-integration-non-seamless).
</Callout>

<Cards columns="3">
  <Card title="1. Get your test credentials" href="#step-1-get-your-test-credentials">
    Get your test key and salt
  </Card>

  <Card title="2. Build the request" href="#step-2-build-the-payment-request">
    Add the cross-border UDFs
  </Card>

  <Card title="3. Generate the hash" href="#step-3-generate-the-hash-on-your-server">
    Sign the request on your server
  </Card>

  <Card title="4. Send the customer to PayU" href="#step-4-post-the-request-to-payu">
    Post the form to `_payment`
  </Card>

  <Card title="5. Check the response" href="#step-5-check-the-response">
    Verify the reverse hash
  </Card>
</Cards>

***

## Before you begin

<Callout icon="📘" theme="info">
  ### **Prerequisites**

  - A PayU merchant account **enabled for Cross-Border Payments – Import**. Contact your PayU Key Account Manager if it isn't enabled yet.
  - Your test **key** and **salt**.
  - A server that can generate a SHA-512 hash. Never generate the hash in the browser or app.
  - Two HTTPS pages on your site to receive the result: a success URL (`surl`) and a failure URL (`furl`).
  - The buyer's details for each payment: PAN, date of birth and an invoice ID.
</Callout>

|                 | **Test**                        | **Production**                    |
| :-------------- | :------------------------------ | :-------------------------------- |
| **Payment URL** | `https://test.payu.in/_payment` | `https://secure.payu.in/_payment` |
| **Credentials** | Test key and salt               | Live key and salt                 |

***

## Step 1: Get your test credentials

<Accordion title="Find your key and salt" icon="fa-key">
  1. Log in to the PayU Dashboard and switch to **Test mode**.
  2. Copy your **Key** and **Salt**.
  3. Store the salt only on your server, for example in an environment variable such as `PAYU_SALT`.

  **Expected output:** a test key (for example, `JPM7Fg`) and a test salt saved on your server.
</Accordion>

<Callout icon="❗️" theme="error">
  ### **Confidential!**

  The salt is a secret. Don't put it in HTML, JavaScript, mobile apps or a public code repository.
</Callout>

***

## Step 2: Build the payment request

<Accordion title="Mandatory parameters" icon="fa-table">
  Cross-border payments use the standard PayU fields **plus** buyer details in the UDF fields.

  | **Parameter** | **Description**                                                                                                                               |
  | :------------ | :-------------------------------------------------------------------------------------------------------------------------------------------- |
  | `key`         | `String` Your merchant key. For example, `JPM7Fg`.                                                                                            |
  | `txnid`       | `String` A unique ID for this order, up to 25 characters. Use a new value for every attempt. For example, `PACBTEST0001`.                     |
  | `amount`      | `String` The amount in INR. For example, `100.00`.                                                                                            |
  | `productinfo` | `String` A short description of the goods or services, up to 100 characters. For example, `Annual software licence`.                          |
  | `firstname`   | `String` The buyer's first name. For example, `Ashish`.                                                                                       |
  | `lastname`    | `String` The buyer's last name. For example, `Kumar`.                                                                                         |
  | `email`       | `String` The buyer's email address. For example, `ashish@example.com`.                                                                        |
  | `phone`       | `String` The buyer's phone number. For example, `9876543210`.                                                                                 |
  | `zipcode`     | `String` The buyer's 6-digit PIN code. For example, `110075`.                                                                                 |
  | `surl`        | `String` The page PayU sends the buyer to after a successful payment. For example, `https://example.com/success`.                             |
  | `furl`        | `String` The page PayU sends the buyer to after a failed payment. For example, `https://example.com/failure`.                                 |
  | `udf1`        | `String` The buyer's PAN. Recommended for a higher approval rate. For example, `ABCDE1234K`.                                                  |
  | `udf3`        | `String` The buyer's date of birth in DD-MM-YYYY format. Recommended for a higher approval rate. For example, `02-02-1980`.                   |
  | `udf4`        | `String` The end merchant's legal entity name. Mandatory if you're a payment aggregator. Don't send it for UPI. For example, `XYZ Pvt. Ltd.`. |
  | `udf5`        | `String` The invoice ID shown on the invoice you issue to the buyer. For example, `INV123456`.                                                |
  | `hash`        | `String` The SHA-512 hash you generate in Step 3.                                                                                             |

  {/* REVIEW: C16 is open – confirm the DOB format for udf3. C23 is open – confirm whether lastname is mandatory for every payment method. */}

  **Expected output:** a set of parameters ready to hash.
</Accordion>

<Callout icon="👍" theme="info">
  ### **Tips**

  - Keep `udf2` empty in this quick start. If a UDF has no value, still include it as an empty value in the hash.
  - Keep the same invoice ID in `udf5` that you'll upload after the payment.
</Callout>

***

## Step 3: Generate the hash on your server

<Accordion title="Hash formula" icon="fa-hashtag">
  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||salt)
  ```

  There are exactly five empty fields (`||||||`) between `udf5` and `salt`.

  ```javascript Node.js
  const crypto = require('crypto');

  function generateHash(p) {
    const hashString = [
      p.key, p.txnid, p.amount, p.productinfo, p.firstname, p.email,
      p.udf1 || '', p.udf2 || '', p.udf3 || '', p.udf4 || '', p.udf5 || '',
      '', '', '', '', '',
      process.env.PAYU_SALT
    ].join('|');
    return crypto.createHash('sha512').update(hashString).digest('hex');
  }
  ```

  ```php PHP
  <?php
  function generateHash($p) {
      $hashString = implode('|', [
          $p['key'], $p['txnid'], $p['amount'], $p['productinfo'], $p['firstname'], $p['email'],
          $p['udf1'] ?? '', $p['udf2'] ?? '', $p['udf3'] ?? '', $p['udf4'] ?? '', $p['udf5'] ?? '',
          '', '', '', '', '',
          getenv('PAYU_SALT')
      ]);
      return strtolower(hash('sha512', $hashString));
  }
  ```

  ```python Python
  import hashlib, os

  def generate_hash(p):
      hash_string = "|".join([
          p["key"], p["txnid"], p["amount"], p["productinfo"], p["firstname"], p["email"],
          p.get("udf1", ""), p.get("udf2", ""), p.get("udf3", ""), p.get("udf4", ""), p.get("udf5", ""),
          "", "", "", "", "",
          os.environ["PAYU_SALT"],
      ])
      return hashlib.sha512(hash_string.encode("utf-8")).hexdigest()
  ```

  **Expected output:** a 128-character lowercase hexadecimal string.
</Accordion>

<Callout icon="🚧" theme="warn">
  ### **Critical Rules**

  - Hash the values exactly as you post them. For example, `100.00` and `100` give different hashes.
  - If you later add optional fields such as `buyer_type_business` or `udf_params`, they change the hash formula. Follow the hashing section in [PayU Hosted Payment Integration](/docs/cb-integration-non-seamless).
  - To check your hash, use the [PayU Hash Verification Tool](doc:using-payu-hash-verification-tool).
</Callout>

***

## Step 4: Post the request to PayU

<Accordion title="Sample request" icon="fa-code">
  Post the parameters as an HTML form from the buyer's browser. PayU then shows its checkout page.

  ```html HTML
  <form action="https://test.payu.in/_payment" method="post">
    <input type="hidden" name="key" value="JPM7Fg" />
    <input type="hidden" name="txnid" value="PACBTEST0001" />
    <input type="hidden" name="amount" value="100.00" />
    <input type="hidden" name="productinfo" value="Annual software licence" />
    <input type="hidden" name="firstname" value="Ashish" />
    <input type="hidden" name="lastname" value="Kumar" />
    <input type="hidden" name="email" value="ashish@example.com" />
    <input type="hidden" name="phone" value="9876543210" />
    <input type="hidden" name="zipcode" value="110075" />
    <input type="hidden" name="surl" value="https://example.com/success" />
    <input type="hidden" name="furl" value="https://example.com/failure" />
    <input type="hidden" name="udf1" value="ABCDE1234K" />
    <input type="hidden" name="udf2" value="" />
    <input type="hidden" name="udf3" value="02-02-1980" />
    <input type="hidden" name="udf4" value="XYZ Pvt. Ltd." />
    <input type="hidden" name="udf5" value="INV123456" />
    <input type="hidden" name="hash" value="<hash_from_your_server>" />
    <input type="submit" value="Pay now" />
  </form>
  ```

  ```curl cURL
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    --data-urlencode "key=JPM7Fg" \
    --data-urlencode "txnid=PACBTEST0001" \
    --data-urlencode "amount=100.00" \
    --data-urlencode "productinfo=Annual software licence" \
    --data-urlencode "firstname=Ashish" \
    --data-urlencode "lastname=Kumar" \
    --data-urlencode "email=ashish@example.com" \
    --data-urlencode "phone=9876543210" \
    --data-urlencode "zipcode=110075" \
    --data-urlencode "surl=https://example.com/success" \
    --data-urlencode "furl=https://example.com/failure" \
    --data-urlencode "udf1=ABCDE1234K" \
    --data-urlencode "udf2=" \
    --data-urlencode "udf3=02-02-1980" \
    --data-urlencode "udf4=XYZ Pvt. Ltd." \
    --data-urlencode "udf5=INV123456" \
    --data-urlencode "hash=<hash_from_your_server>"
  ```

  **Expected output:** PayU's checkout page opens. Choose a payment method and complete the test payment, using test card or NetBanking details from [Test Cards, UPI and Wallets](/docs/test-cards-upi-id-and-wallets).

  {/* REVIEW: confirm the slug of the test credentials page. */}
</Accordion>

***

## Step 5: Check the response

PayU posts the result to your `surl` or `furl` as form data. Before you update the order, check that the response came from PayU.

<Accordion title="Verify the reverse hash" icon="fa-shield-halved">
  ```
  sha512(salt|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  ```javascript Node.js
  const crypto = require('crypto');

  function isValidResponse(r) {
    const hashString = [
      process.env.PAYU_SALT, r.status,
      '', '', '', '', '',
      r.udf5 || '', r.udf4 || '', r.udf3 || '', r.udf2 || '', r.udf1 || '',
      r.email, r.firstname, r.productinfo, r.amount, r.txnid, r.key
    ].join('|');
    const expected = crypto.createHash('sha512').update(hashString).digest('hex');
    return expected === r.hash;
  }
  ```

  {/* REVIEW: if the response contains additional_charges, the reverse hash starts with additional_charges|salt|... Confirm the reverse hash when udf_params or buyer_type_business is sent. */}
</Accordion>

<Accordion title="Sample responses" icon="fa-reply">
  Shown parsed as JSON.

  {/* REVIEW: illustrative values. Replace them with real one-time Hosted Checkout responses. */}

  <Tabs>
    <Tab title="Success">
      ```json
      {
        "mihpayid": "403993715525331373",
        "mode": "CC",
        "status": "success",
        "unmappedstatus": "captured",
        "key": "JPM7Fg",
        "txnid": "PACBTEST0001",
        "amount": "100.00",
        "productinfo": "Annual software licence",
        "firstname": "Ashish",
        "email": "ashish@example.com",
        "udf1": "ABCDE1234K",
        "udf2": "",
        "udf3": "02-02-1980",
        "udf4": "XYZ Pvt. Ltd.",
        "udf5": "INV123456",
        "field9": "Transaction Completed Successfully",
        "error": "E000",
        "error_Message": "No Error",
        "hash": "<response hash>"
      }
      ```
    </Tab>

    <Tab title="Failure">
      ```json
      {
        "mihpayid": "403993715525331374",
        "mode": "CC",
        "status": "failure",
        "unmappedstatus": "failed",
        "key": "JPM7Fg",
        "txnid": "PACBTEST0002",
        "amount": "100.00",
        "udf5": "INV123456",
        "field9": "Transaction declined due to either incorrect cvv/expiry or card validation failure",
        "error": "E1632",
        "error_Message": "Transaction declined due to either incorrect cvv/expiry or card validation failure",
        "hash": "<response hash>"
      }
      ```
    </Tab>
  </Tabs>

  **Expected output:** the reverse hash matches, and `status` is `success` with `unmappedstatus` set to `captured`.
</Accordion>

<Callout icon="🚧" theme="warn">
  ### **Watch Out!**

  Browser redirects can be spoofed. Before you ship goods or deliver a service, confirm the status with the [Verify Payment API](ref:verify-payment-api) or a webhook.
</Callout>

***

## After the payment: upload the invoice

Cross-border import payments need the buyer's invoice. Goods merchants also need the airway bill (AWB). Upload them within 10 days of the payment, using the steps in [PayU Hosted Payment Integration](/docs/cb-integration-non-seamless). If they're missing, your next settlement can be put on hold.

{/* REVIEW: C22 is open – confirm the per-transaction limit before adding it to this page. */}

***

## Common first-time errors

| **Problem**                                       | **Likely cause**                                                                                           | **Fix**                                                                                          |
| :------------------------------------------------ | :--------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------- |
| "Invalid hash" or checksum error on the PayU page | The field order is wrong, the empty fields are missing, or the posted values differ from the hashed values | Rebuild the hash string using the formula in Step 3 and check it with the Hash Verification Tool |
| "Invalid key"                                     | You used a live key on `test.payu.in`, or a test key on production                                         | Match the key to the environment                                                                 |
| "Transaction ID already used"                     | The `txnid` was used before                                                                                | Generate a new `txnid` for every attempt                                                         |
| Cross-border option not available                 | Your account isn't enabled for Cross-Border Payments – Import                                              | Ask your PayU Key Account Manager to enable it                                                   |
| The reverse hash doesn't match                    | The fields are in the wrong order, or the wrong salt was used                                              | Use the reverse order in Step 5 and the salt for the same environment                            |

***

## Next Steps

<Cards columns="3">
  <Card title="Full Hosted integration" href="/docs/cb-integration-non-seamless">
    Optional fields, B2B buyers, invoice ID update and invoice upload
  </Card>

  <Card title="How it works" href="/docs/workflow-for-cross-border-payments-import">
    Understand the payment, settlement and invoice flow
  </Card>

  <Card title="FAQs" href="/docs/faqs-for-cross-border-payments">
    Answers on currencies, settlement and documents
  </Card>
</Cards>
