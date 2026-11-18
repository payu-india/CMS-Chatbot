---
title: Quick Start — Merchant Hosted Checkout
excerpt: Post one net banking test payment and check the callback
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Quick Start — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Post a PayU Merchant Hosted net banking test payment to test.payu.in/_payment with pg=TESTPG, then verify the surl callback and the payment.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Use test credentials only. Never use live credentials in test.
</Callout>

# Quick Start — Merchant Hosted Checkout

## What You'll Build

One net banking test payment. The browser posts to the test `_payment` URL with `pg=TESTPG` and `bankcode=TESTPGNB`. You then check the callback PayU sends to your `surl` or `furl`.

## Step 1: Get Your Test Credentials

Use the test merchant key and test salt. The legacy test page says you must only use the test key and salt for a test transaction.

<KeySaltReference />

## Step 2: Generate the Hash

Build this string and hash it with SHA-512. Keep the salt on the server.

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

<!-- VALIDATION NEEDED: The legacy overview also contains a hash sample with no UDF fields. This quick start follows the formula printed on the net banking parameter table. -->

<Tabs>
  <Tab title="Node.js">
    ```javascript
    const crypto = require('crypto');

    function generateHash(params, salt) {
        const udf1 = params.udf1 || '';
        const udf2 = params.udf2 || '';
        const udf3 = params.udf3 || '';
        const udf4 = params.udf4 || '';
        const udf5 = params.udf5 || '';
        const hashString = `${params.key}|${params.txnid}|${params.amount}|${params.productinfo}|${params.firstname}|${params.email}|${udf1}|${udf2}|${udf3}|${udf4}|${udf5}||||||${salt}`;
        return crypto.createHash('sha512').update(hashString).digest('hex');
    }
    ```
  </Tab>
  <Tab title="PHP">
    ```php
    <?php
    function generateHash($params, $salt) {
        $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
        $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
        $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
        $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
        $udf5 = isset($params['udf5']) ? $params['udf5'] : '';
        $hashString = $params['key'].'|'.$params['txnid'].'|'.$params['amount'].'|'.$params['productinfo'].'|'.$params['firstname'].'|'.$params['email'].'|'.$udf1.'|'.$udf2.'|'.$udf3.'|'.$udf4.'|'.$udf5.'||||||'.$salt;
        return strtolower(hash('sha512', $hashString));
    }
    ?>
    ```
  </Tab>
</Tabs>

## Step 3: Post the Payment

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |

The sample below is the net banking test form from the legacy net banking page. `pg` is `TESTPG` and `bankcode` is `TESTPGNB`.

<Tabs>
  <Tab title="Form POST">
    ```html
    <form action='https://test.payu.in/_payment' method='post'>
    <input type="hidden" name="key" value="JP***g" />
    <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
    <input type="hidden" name="productinfo" value="iPhone" />
    <input type="hidden" name="amount" value="10" />
    <input type="hidden" name="email" value="test@gmail.com" />
    <input type="hidden" name="firstname" value="Ashish" />
    <input type="hidden" name="lastname" value="Kumar" />
    <input type="hidden" name="pg" value="TESTPG" />
    <input type="hidden" name="bankcode" value="TESTPGNB" />
    <input type="hidden" name="surl" value="your own success url" />
    <input type="hidden" name="furl" value="your own failure url" />
    <input type="hidden" name="phone" value="9988776655" />
    <input type="hidden" name="hash" value="generated_on_your_server" />
    <input type="submit" value="submit">
    </form>
    ```
  </Tab>
  <Tab title="cURL">
    ```bash
    curl -X POST "https://test.payu.in/_payment" \
      -H "accept: application/json" \
      -H "Content-Type: application/x-www-form-urlencoded" \
      -d "key=JP***g" \
      -d "txnid=ewP8oRopzdHEtC" \
      -d "amount=10.00" \
      -d "firstname=Ashish" \
      -d "email=test@gmail.com" \
      -d "phone=9876543210" \
      -d "productinfo=iPhone" \
      -d "pg=TESTPG" \
      -d "bankcode=TESTPGNB" \
      -d "surl=https://apiplayground-response.herokuapp.com/" \
      -d "furl=https://apiplayground-response.herokuapp.com/" \
      -d "hash={{hash_value}}"
    ```
  </Tab>
</Tabs>

<Callout icon="📘" theme="info">
  Net banking test login from the legacy test page: username `payu`, password `payu`, OTP `123456`.
</Callout>

## Step 4: Handle the Callback

PayU redirects the customer to `surl` or `furl` and posts the transaction fields. The net banking success sample includes `mihpayid`, `mode=NB`, `status=success`, `unmappedstatus=captured`, `txnid`, `amount`, `bankcode=TESTPGNB`, `error=E000`, and `error_Message=No Error`.

Verify the response hash before you treat the callback as final:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<ReverseHashing />

<!-- DOCUMENTATION GAP: A standalone reverse-hash code sample is not in the net banking page. The formula above is the one printed on the UPI Collect page and in the ReverseHashing block. -->

## Step 5: Verify the Payment Server-Side

The legacy method pages tell you to verify with `verify_payment` and to monitor with webhooks. The shared block below is the source for that call. Do not treat the browser redirect as the only confirmation.

<Verify_Payment_Tabs />

## Next Steps

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameter tables for cards, net banking, wallets, UPI Collect, PayPal, and Pluxee.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="./integration-guide/test-integration">
    Test VPAs, EMI cards, and wallet numbers from the legacy test page.
  </Card>
</Cards>
