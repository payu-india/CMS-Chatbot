---
title: Quick Start — Merchant Hosted Checkout
excerpt: Post one test card payment to PayU and verify the callback
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Quick Start — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Post a test card payment to PayU Merchant Hosted Checkout. Generate the SHA-512 hash, handle surl and furl, and verify the payment. Test key and salt only.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">
  Use test credentials only. Do not use live key, salt, or the production URL in this quick start.
</Callout>

# Quick Start — Merchant Hosted Checkout

## What You'll Build

A single test card payment. Your server hashes the request, the browser form-POSTs it to the test `_payment` URL, and your callback checks the reverse hash and calls Verify Payment.

Card collection on your page is in PCI-DSS scope. This quick start uses the test environment.

## Step 1: Get Your Test Credentials

<KeySaltReference />

## Step 2: Generate the Hash

Use this formula. Keep empty `udf` values empty so the pipes stay in place:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
```

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
    $hashString = $params['key'] . '|' . $params['txnid'] . '|' . $params['amount'] . '|' . $params['productinfo'] . '|' .
                  $params['firstname'] . '|' . $params['email'] . '|' . $udf1 . '|' . $udf2 . '|' .
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' . $salt;
    return strtolower(hash('sha512', $hashString));
}
?>
```

  </Tab>
</Tabs>

## Step 3: Post the Card Payment

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |

Post `pg=CC` and the card fields. The cards guide shows two `bankcode` values in its samples.

<!-- VALIDATION NEEDED: The HTML form on the cards page sends bankcode=MAST. The cURL sample on the same page sends bankcode=CC. The overview table also says bankcode=CC. Both samples are shown below. -->

<Accordion title="Form POST" icon="fa-code">

```html
<form action="https://test.payu.in/_payment" method="post">
  <input type="hidden" name="key" value="JP***g" />
  <input type="hidden" name="txnid" value="t6svtqtjRdl34W" />
  <input type="hidden" name="productinfo" value="iPhone" />
  <input type="hidden" name="amount" value="10" />
  <input type="hidden" name="email" value="test@gmail.com" />
  <input type="hidden" name="firstname" value="Ashish" />
  <input type="hidden" name="lastname" value="Kumar" />
  <input type="hidden" name="pg" value="CC" />
  <input type="hidden" name="bankcode" value="MAST" />
  <input type="hidden" name="ccnum" value="5123456789012346" />
  <input type="hidden" name="ccname" value="Ashish Kumar" />
  <input type="hidden" name="ccvv" value="123" />
  <input type="hidden" name="ccexpmon" value="12" />
  <input type="hidden" name="ccexpyr" value="2021" />
  <input type="hidden" name="surl" value="your own success url" />
  <input type="hidden" name="furl" value="your own failure url" />
  <input type="hidden" name="phone" value="9988776655" />
  <input type="hidden" name="hash" value="HASH_GENERATED_ON_SERVER" />
  <input type="submit" value="submit" />
</form>
```

The cards page states that this HTML block is the Merchant Checkout credit-card call for the test environment. Replace the hash with the value from Step 2. Do not put the salt in this page.

</Accordion>

<Accordion title="cURL" icon="fa-code">

```bash
curl -X POST "https://test.payu.in/_payment" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "key=YOUR_MERCHANT_KEY" \
  -d "txnid=TXN_12345" \
  -d "amount=1000.00" \
  -d "productinfo=Product+Description" \
  -d "firstname=Customer+Name" \
  -d "email=customer@example.com" \
  -d "phone=9988776655" \
  -d "pg=CC" \
  -d "bankcode=CC" \
  -d "ccnum=CARD_NUMBER" \
  -d "ccexpmon=MM" \
  -d "ccexpyr=YY" \
  -d "ccvv=CVV" \
  -d "ccname=NAME_ON_CARD" \
  -d "surl=https://yourwebsite.com/success" \
  -d "furl=https://yourwebsite.com/failure" \
  -d "hash=HASH_GENERATED_ON_SERVER"
```

</Accordion>

<!-- DOCUMENTATION GAP: test-integration.md documents test values for net banking, UPI VPAs, EMI cards, and wallets. It does not document a plain credit or debit test card. Do not treat card numbers that appear inside request samples as test credentials. -->

## Step 4: Handle the Callback

PayU redirects the browser to `surl` or `furl` and posts the result. The cards success sample includes `mihpayid`, `mode=CC`, `status=success`, `unmappedstatus=captured`, `txnid`, `amount`, `hash`, `bankcode`, `error=E000`, and `error_Message=No Error`. The failure sample includes `status=failure`, `unmappedstatus=failed`, `error=E1903`, and `error_Message=Authorization failed at Bank`.

Recompute the reverse hash before you update the order:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<Accordion title="Verify the response hash" icon="fa-shield-halved">
  <ReverseHashing />
</Accordion>

## Step 5: Verify the Payment Server-Side

<Accordion title="Verify Payment API" icon="fa-circle-check">
  <Verify_Payment_Tabs />
</Accordion>

The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks for that path. See [Webhooks](doc:webhooks).

## Next Steps

<Cards columns={2}>
  <Card title="Cards" icon="fa-credit-card" href="./integration-guide/build-integration/cards">
    BIN check, saved cards, guest checkout, and 3DS 2.0.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="./integration-guide/test-integration">
    Test key and salt, and test values by method.
  </Card>
</Cards>
