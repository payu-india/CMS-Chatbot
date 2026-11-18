---
title: How Merchant Hosted Checkout Works
excerpt: How a merchant-hosted payment moves from your checkout through PayU and back
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: How Merchant Hosted Checkout Works | PayU Developer Docs
  description: >-
    Merchant Hosted Checkout flow: browser form POST to PayU _payment, bank or UPI authentication, surl/furl callback, SHA-512 hash, and server-side verify.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# How Merchant Hosted Checkout Works

The customer submits payment details on your site. The browser form-posts those details to PayU. PayU sends the customer to the card ACS, the bank's net banking page, the wallet, or the UPI flow. After the bank or app finishes, PayU redirects the customer to your site.

## Architecture Overview

1. The browser posts the payment form directly to PayU. Your page does not send the customer to a PayU-hosted payment page to choose the method.
2. PayU processes the request in its environment, then reaches the card ACS or the bank's net banking page when that method requires it.
3. When the bank-side step finishes, PayU redirects the customer to your `surl` or `furl` and posts the transaction result.

The legacy overview includes the flow diagram and the customer-journey diagram. Those images are the source for the sequence above.

## Endpoints

| Environment | URL |
| --- | --- |
| Test `_payment` | `POST https://test.payu.in/_payment` |
| Production `_payment` | `POST https://secure.payu.in/_payment` |
| Test post-service (BIN sample) | `POST https://test.payu.in/merchant/postservice?form=2` |
| Production post-service (BIN sample) | `POST https://info.payu.in/merchant/postservice?form=2` |
| Production post-service (APIs page) | `POST https://info.payu.in/merchant/postservice.php?form=2` |

<!-- VALIDATION NEEDED: The legacy APIs page writes the post-service path as merchant/postservice.php?form=2. The cards BIN sample and the UPI validateVPA sample use merchant/postservice?form=2 without .php. Verify Payment's shared block uses both forms. Do not pick one URL until the docs team confirms which path is current for each command. -->

## Key Parameters

`pg` selects the payment category. `bankcode` selects the network, bank, or wallet. Other methods add their own fields. The values below are the ones stated on the method pages. Conflicts are flagged. They are not resolved here.

| Parameter | Value in source | Purpose |
| --- | --- | --- |
| pg | CC | Cards |
| bankcode | CC, MAST, AMEX, or VISA in different card samples | Card network or bank code |
| pg | NB in the net banking table. Samples use TESTPG | Net banking |
| bankcode | TESTPGNB in the net banking test sample | Test net banking bank code |
| pg | CASH, or RD for Advantage Club | Wallets |
| bankcode | PAYTM in the Paytm sample. ADVCLUB for Advantage Club | Wallet code |
| pg | UPI | UPI Collect |
| bankcode | UPI | UPI Collect. The legacy overview also names INTENT and UPIDBQR for Intent and QR |
| pg | PAYPAL | PayPal |
| bankcode | PAYPAL | PayPal. The legacy overview table says N/A |
| pg | MC | Pluxee |
| bankcode | SODEXO | Pluxee |

<!-- VALIDATION NEEDED: Cards steps say bankcode=CC, the HTML sample uses MAST, the parameter example is AMEX, and a saved-card sample uses VISA. Net banking steps say pg=NEFT. See the method pages before you copy a sample. -->

## Hash Generation

### Request Hash

The method pages state this formula:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
```

Empty UDF fields stay in the string as empty values between the pipes. Generate this on your server. Append the salt at the end. The algorithm is SHA-512.

<!-- VALIDATION NEEDED: A second Python sample on the legacy overview builds key|txnid|amount|productinfo|firstname|email||||||||||salt and omits the five UDF fields. The legacy APIs page says card and other modes can require a different sequence, and it does not print that sequence. Use the UDF formula from the method pages until the docs team confirms otherwise. -->

<Tabs>
  <Tab title="Node.js">
    ```javascript
    const crypto = require('crypto');

    function generateHash(params, salt) {
        const key = params.key;
        const txnid = params.txnid;
        const amount = params.amount;
        const productinfo = params.productinfo;
        const firstname = params.firstname;
        const email = params.email;
        const udf1 = params.udf1 || '';
        const udf2 = params.udf2 || '';
        const udf3 = params.udf3 || '';
        const udf4 = params.udf4 || '';
        const udf5 = params.udf5 || '';
        const hashString = `${key}|${txnid}|${amount}|${productinfo}|${firstname}|${email}|${udf1}|${udf2}|${udf3}|${udf4}|${udf5}||||||${salt}`;
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

The same sequence is in `<HashingSample />`, which also includes Java, C#, and Python.

<HashingSample />

Post-service commands (`getBinInfo`, `validateVPA`, `verify_payment`, and the other `command` APIs) use a different formula, stated on the legacy APIs page:

```
sha512(key|command|var1|SALT)
```

### Response Hash Verification

PayU returns a hash on the callback. Rebuild it from the response fields and your salt. Accept the payment only when your hash matches the hash in the response.

The UPI Collect page states this order:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<ReverseHashing />

<!-- DOCUMENTATION GAP: The reverse-hash formula is in the source. A full verification function is not in this folder. It is referenced through the ReverseHashing block. Do not invent a code sample here. -->

## Payment Flow — Step by Step

<Accordion title="1. Collect the payment details" icon="fa-circle-1">
  Your checkout collects the fields for the selected method. For cards, that includes the card number, name, expiry, and CVV. For UPI Collect, collect the VPA. For net banking, collect the bank choice that maps to `bankcode`.
</Accordion>

<Accordion title="2. Hash the request on the server" icon="fa-circle-2">
  Your server builds the request hash with the salt and returns only the hash to the page that submits the form.
</Accordion>

<Accordion title="3. The browser posts to _payment" icon="fa-circle-3">
  The form posts `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `pg`, `bankcode`, `surl`, `furl`, `hash`, and the method fields.
</Accordion>

<Accordion title="4. PayU and the bank authenticate" icon="fa-circle-4">
  PayU validates the hash and routes the payment. The customer may see the bank ACS page, a net banking login, a wallet redirect, or a UPI collect request.
</Accordion>

<Accordion title="5. PayU posts the result to surl or furl" icon="fa-circle-5">
  The callback includes `mihpayid`, `status`, `txnid`, `amount`, `hash`, `error`, and `error_Message`, plus method fields such as `mode` and `bankcode`.
</Accordion>

<Accordion title="6. Verify the reverse hash" icon="fa-circle-6">
  Recompute the response hash. Reject the callback when it does not match.
</Accordion>

<Accordion title="7. Verify the payment on the server" icon="fa-circle-7">
  Call `verify_payment` with the `txnid`. The legacy checklist says to confirm the status on the server if the callback fails, and to use webhooks to hear callbacks.
</Accordion>

## PCI-DSS Scope

If you store, process, or transmit cardholder data, the source says you must comply with PCI-DSS. It names the Self-Assessment Questionnaire A-EP and Attestation of Compliance. Merchant Hosted Checkout collects card details on your website, so card collection is in scope. International card transactions must be enabled by writing to the PayU Integration Team at integration@pay.in.

<!-- DOCUMENTATION GAP: The source names SAQ A-EP and links the PCI form. It does not list the questionnaire steps. -->

If you use only UPI and wallets, the source says the website must still be secure. It does not say those modes remove every compliance duty.

## When to Use Merchant Hosted Checkout vs Alternatives

| Scenario | Recommended product |
| --- | --- |
| You want to design the payment form and post the details yourself | Merchant Hosted Checkout |
| You want PayU to collect the payment details on a PayU page | [PayU Hosted Checkout](https://docs.payu.in/docs/payu-hosted-checkout-1) |
| You do not have a website | [Payment Links](https://docs.payu.in/docs/payment-links-dashboard) |
| You are collecting payment inside a native app | [PayU Mobile SDK](https://docs.payu.in/docs/mobile-sdk-integration) |

## Key Concepts

<Accordion title="key" icon="fa-key">
  The merchant identifier PayU gives you. Test and production keys are different.
</Accordion>

<Accordion title="salt" icon="fa-shield-halved">
  The secret used in the hash. It stays on your server.
</Accordion>

<Accordion title="txnid" icon="fa-fingerprint">
  Your unique transaction id. The saved-card parameter text says PayU will not accept a duplicate transaction id.
</Accordion>

<Accordion title="pg and bankcode" icon="fa-credit-card">
  `pg` is the payment category. `bankcode` is the network, bank, or wallet. Values are case-sensitive.
</Accordion>

<Accordion title="surl and furl" icon="fa-link">
  `surl` is the success redirect. `furl` is the failure redirect. PayU posts the response to the URL it redirects to.
</Accordion>

<!-- VALIDATION NEEDED: The net banking and wallets parameter tables in the legacy pages describe furl as the success URL and surl as the failure URL. Cards, UPI Collect, PayPal, and Pluxee describe surl as success and furl as failure. -->

<Accordion title="mihpayid" icon="fa-hashtag">
  PayU's payment id, returned on the callback. Samples on the method pages include it.
</Accordion>

<Accordion title="hash" icon="fa-lock">
  The SHA-512 digest of the request string, and a separate digest PayU returns on the response for you to verify.
</Accordion>
