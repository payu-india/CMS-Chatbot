---
title: Quick Start — Merchant Hosted Checkout
excerpt: Post one test net-banking payment to PayU and read the callback
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Quick Start — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Make a test Merchant Hosted net-banking payment. Hash on the server, form POST to test.payu.in/_payment with TESTPG, then verify the callback. Use test login.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Use the test key and salt only. Do not use live credentials for this payment.
</Callout>

# Quick Start — Merchant Hosted Checkout

## What You'll Build

A single test net-banking payment. Your page form-posts to `https://test.payu.in/_payment` with `pg=TESTPG` and `bankcode=TESTPGNB`. PayU sends the customer through the test net-banking login, then posts the result back to your `surl` or `furl`.

This path does not collect a card number. Cards, UPI, wallets, and the other methods are in [Build the Integration](./integration-guide/build-integration).

## Step 1: Get Your Test Credentials

<KeySaltReference />

## Step 2: Generate the Hash

On your server, hash the payment fields with SHA-512:

```text
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
```

Keep every pipe, including the empty `udf` segments. The salt stays on the server.

<HashingSample />

<!-- VALIDATION NEEDED: The overview page also contains a shorter Python string, with ten pipes between email and the salt. The net-banking parameter table uses the formula shown above. Use that formula for this quick start. -->

## Step 3: Submit the Payment

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |

The HTML below is the net-banking test form from the source. Replace `key`, `txnid`, the URLs, and `hash` with your own values. The hash in the sample belongs to the sample payload. Regenerate it.

<Tabs>
  <Tab title="Form POST">

```html
<html>
<body>
<form action="https://test.payu.in/_payment" method="post">
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
<input type="hidden" name="hash" value="eabec285da28fd0e3054d41a4d24fe9f7599c9d0b66646f7a9984303fd6124044b6206daf831e9a8bda28a6200d318293a13d6c193109b60bd4b4f8b09c90972" />
<input type="submit" value="submit"> </form>
</body>
</html>
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
  On the test net-banking page use username `payu`, password `payu`, and OTP `123456`.
</Callout>

<!-- VALIDATION NEEDED: This test sample posts pg=TESTPG and bankcode=TESTPGNB. The net-banking parameter description says pg=NB. The step card on that page says pg=NEFT. TESTPG / TESTPGNB are the test values in the sample. This quick start does not state a production bank code, because the source does not give one sample production code. See Net Banking Codes. -->

<!-- VALIDATION NEEDED: The net-banking parameter table describes furl as the success URL and surl as the failure URL. The HTML sample on that page labels surl "your own success url" and furl "your own failure url". This quick start follows the HTML sample. -->

## Step 4: Handle the Callback

PayU posts the result to `surl` or `furl`. The parsed net-banking sample in the source is a success:

```text
mihpayid = 403993715524045752
mode = NB
status = success
unmappedstatus = captured
key = JPM7Fg
txnid = ewP8oRopzdHEtC
amount = 10.00
productinfo = iPhone
firstname = Ashish
email = test@gmail.com
phone = 9876543210
bank_ref_num = 87d3b2a1-5a60-4169-8692-649f61923b3d
bankcode = TESTPGNB
error = E000
error_Message = No Error
```

Before you accept it, recreate the reverse hash:

```text
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<!-- VALIDATION NEEDED: That reverse-hash formula is written on the UPI Collect page and in the shared reverse-hash block. The net-banking page embeds the block and does not restate the formula. -->

<!-- DOCUMENTATION GAP: The Merchant Hosted source has no reverse-hash code sample. Do not add a Node.js or PHP verifier that is not in the source. -->

## Step 5: Verify the Payment Server-Side

<Verify_Payment_Tabs />

## Next Steps

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameters for cards, UPI, wallets, and the other methods.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="./integration-guide/test-integration">
    Test credentials for each method the source actually lists.
  </Card>
</Cards>
