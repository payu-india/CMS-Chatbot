---
title: How Merchant Hosted Checkout Works
excerpt: See how a payment moves from your page to PayU, through the bank, and back to surl or furl
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: How Merchant Hosted Checkout Works | PayU Developer Docs
  description: >-
    Merchant Hosted Checkout flow, _payment and post-service endpoints, pg and bankcode, and the SHA-512 request and response hashes. Server-side callback checks.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# How Merchant Hosted Checkout Works

You collect payment details on your website. The customer's browser form-POSTs those details to PayU. PayU processes the payment with the bank, card network, UPI app, wallet, PayPal, or Pluxee, then redirects the customer to your site with the result.

## Architecture Overview

1. The customer submits payment on your website. The browser form-POSTs the payment data to PayU.
2. The payment travels through PayU's secured environment before it reaches the card ACS or the bank's net-banking page.
3. After the bank or provider finishes, PayU redirects the customer to your website.

<Image src="https://files.readme.io/4aeeafdbefc392fa362522d8209dc7268178e104e699b067895a3408ff412c42-merchant_hosted_flow.png" alt="Merchant Hosted Checkout architecture from the merchant browser to PayU and the bank, then back" align="center" />

## Endpoints

| Purpose | Test | Production |
| --- | --- | --- |
| Collect payment (`_payment`) | `POST https://test.payu.in/_payment` | `POST https://secure.payu.in/_payment` |
| BIN lookup on the cards guide | `POST https://test.payu.in/merchant/postservice?form=2` | `POST https://info.payu.in/merchant/postservice?form=2` |
| Post-service commands on the API index (`verify_payment` and the other `command` APIs) | Not stated on the API index page | `POST https://info.payu.in/merchant/postservice.php?form=2` |

<!-- VALIDATION NEEDED: The cards guide calls getBinInfo at /merchant/postservice?form=2. The Merchant Hosted API index calls post-service commands at /merchant/postservice.php?form=2. Both URLs are printed here. Confirm which path is correct for each command. -->

The UPI Collect page loads its post-service host from the `GENERALAPIsEnvironment` block. The validate-VPA sample on that page posts to `https://test.payu.in/merchant/postservice?form=2`.

## Key Parameters

| Parameter | Role |
| --- | --- |
| `pg` | Payment category. Examples in this folder: `CC`, `NB` or `TESTPG`, `CASH` or `RD`, `UPI`, `PAYPAL`, `MC`. |
| `bankcode` | Method or bank. Examples: `CC` or a card scheme, `TESTPGNB`, a wallet code, `UPI`, `INTENT`, `UPIDBQR`, `PAYPAL`, `SODEXO`. |
| `ccnum`, `ccname`, `ccvv`, `ccexpmon`, `ccexpyr` | Card or Pluxee card details collected on your page. |
| `vpa` | Customer VPA for UPI Collect. |
| `save_sodexo_card`, `source_id`, `is_check_balance` | Pluxee save-card and repeat-payment fields. |
| `surl`, `furl` | URLs PayU redirects to after success or failure. |
| `hash` | SHA-512 of the request fields and your salt. |

`txnid` is the unique transaction reference you generate. The saved-card parameters say PayU will not accept a duplicate transaction ID.

## Hash Generation

### Request Hash

Every method page in this folder uses this formula:

```
sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
```

Unused `udf1` to `udf5` are empty strings. The six pipes after `udf5` stay in the string. Generate this on your server. The salt is the secret PayU shares with you.

<HashingRequestParameters />

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
    $key = $params['key'];
    $txnid = $params['txnid'];
    $amount = $params['amount'];
    $productinfo = $params['productinfo'];
    $firstname = $params['firstname'];
    $email = $params['email'];
    $udf1 = isset($params['udf1']) ? $params['udf1'] : '';
    $udf2 = isset($params['udf2']) ? $params['udf2'] : '';
    $udf3 = isset($params['udf3']) ? $params['udf3'] : '';
    $udf4 = isset($params['udf4']) ? $params['udf4'] : '';
    $udf5 = isset($params['udf5']) ? $params['udf5'] : '';

    $hashString = $key . '|' . $txnid . '|' . $amount . '|' . $productinfo . '|' .
                  $firstname . '|' . $email . '|' . $udf1 . '|' . $udf2 . '|' .
                  $udf3 . '|' . $udf4 . '|' . $udf5 . '||||||' . $salt;

    return strtolower(hash('sha512', $hashString));
}
?>
```

  </Tab>
  <Tab title="Python">

```python
import hashlib

def generate_hash(params, salt):
    key = params['key']
    txnid = params['txnid']
    amount = params['amount']
    productinfo = params['productinfo']
    firstname = params['firstname']
    email = params['email']
    udf1 = params.get('udf1', '')
    udf2 = params.get('udf2', '')
    udf3 = params.get('udf3', '')
    udf4 = params.get('udf4', '')
    udf5 = params.get('udf5', '')

    hash_string = f"{key}|{txnid}|{amount}|{productinfo}|{firstname}|{email}|{udf1}|{udf2}|{udf3}|{udf4}|{udf5}||||||{salt}"
    return hashlib.sha512(hash_string.encode('utf-8')).hexdigest()
```

  </Tab>
</Tabs>

<!-- VALIDATION NEEDED: The overview page also includes a second Python sample that hashes key|txnid|amount|productinfo|firstname|email||||||||||salt (ten pipes after email, and no udf fields). That sample is not copied here. The formula above matches the method pages and HashingRequestParameters. -->

Post-service commands (`verify_payment`, `getBinInfo`, `validateVPA`, and the other `command` APIs listed on the API index) use a different hash. The API index states:

```
sha512(key|command|var1|SALT)
```

### Response Hash Verification

When PayU posts the result to `surl` or `furl`, verify the hash before you accept the payment. The UPI Collect page and the `ReverseHashing` block use:

```
sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

<ReverseHashing />

The PayPal page does not include its own reverse-hash sample. Use the formula above and confirm it against the hash field PayU posts.

## Payment Flow — Step by Step

<Accordion title="1. Collect the payment details on your page" icon="fa-circle-1">
  The customer chooses a method and enters the details that method needs. Card and Pluxee numbers are entered on your site.
</Accordion>

<Accordion title="2. Hash the request on your server" icon="fa-circle-2">
  Build the request string in the order above, append the salt, and hash it with SHA-512. Put the result in `hash`.
</Accordion>

<Accordion title="3. Form-POST to _payment" icon="fa-circle-3">
  The browser posts `key`, `txnid`, `amount`, `productinfo`, `firstname`, `email`, `phone`, `pg`, `bankcode`, `surl`, `furl`, `hash`, and the method fields.
</Accordion>

<Accordion title="4. The customer authenticates" icon="fa-circle-4">
  For cards, the documented journey continues to the bank ACS page, where the customer enters the OTP. Other methods continue with that provider.
</Accordion>

<Accordion title="5. PayU redirects to surl or furl" icon="fa-circle-5">
  Your page receives the response, including `mihpayid`, `status`, `txnid`, `amount`, `hash`, `error`, and `error_Message`.
</Accordion>

<Accordion title="6. Verify on your server" icon="fa-circle-6">
  Check the reverse hash. Call `verify_payment`. The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks for that callback path.
</Accordion>

## PCI-DSS Scope

If you store, process, or transmit cardholder data, you must comply with PCI-DSS. The overview and the cards guide name the Self-Assessment Questionnaire A-EP and Attestation of Compliance. Collecting card details on your own website for Merchant Hosted Checkout means you are in that scope.

Do not store the CVV. Do not store the full card number on your servers. Pluxee has the same rule for the full card number, expiry, and CVV, even when the customer allows the card to be saved. Repeat Pluxee payments use `source_id`. Guest checkout uses an Alt ID instead of the plain card number.

UPI and wallet integrations still require a secure site. The overview says to use HTTPS when those are the only modes you offer.

## When to Use Merchant Hosted Checkout

Use Merchant Hosted Checkout when you collect payment details on your website and post them to PayU. The overview describes it as a PayU product with its own APIs, separate from simply placing payment elements on a page. PayPal can be used with PayU Hosted Checkout or with Merchant Hosted Checkout. PayPal on this integration is a form POST with `pg=PAYPAL` and `bankcode=PAYPAL`.

<!-- DOCUMENTATION GAP: This folder has no scenario table that maps use cases to PayU Hosted Checkout, Payment Links, or the Mobile SDK. Add that table only from a source that states the recommendation. -->

## UPI Collect Restrictions

<Callout icon="⚠️" theme="warn">
  UPI Collect is allowed only for MCC 6012 and 6211.

  For `txn_s2s_flow = 2` or `txn_s2s_flow = 4`:

  - Android apps implement Smart Intent. See [UPI Smart Intent - Non SDK Flow](doc:upi-smart-intent-non-sdk-flow) or the PayU Android SDKs.
  - iOS can use a deeplink and continue with UPI Collect.
  - Web uses the deeplink from [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server) and shows it as a QR, instead of UPI Collect.
  - Seamless form POST does not support Intent on Android and desktop web. Those merchants migrate to `txn_s2s_flow`.
</Callout>

## Key Concepts

<Accordion title="txnid" icon="fa-fingerprint">
  Your unique reference for the payment. The saved-card parameters say a duplicate transaction ID is not accepted.
</Accordion>

<Accordion title="pg and bankcode" icon="fa-credit-card">
  `pg` is the payment category. `bankcode` is the bank, scheme, wallet, or method. Both are posted on `_payment`.
</Accordion>

<Accordion title="surl and furl" icon="fa-link">
  `surl` is the success URL. `furl` is the failure URL. PayU redirects the customer's browser to one of them and posts the result.
</Accordion>

<Accordion title="mihpayid" icon="fa-hashtag">
  PayU's payment identifier in the callback. Card, UPI, wallet, PayPal, Pluxee, and net-banking samples all return it.
</Accordion>

<Accordion title="hash and salt" icon="fa-shield-halved">
  The request hash is SHA-512 of the payment fields plus your salt. The response hash is the reverse sequence, starting with the salt. You recompute it before trusting the callback.
</Accordion>

<Accordion title="Alt ID" icon="fa-id-card">
  The token that replaces a plain card number for guest checkout. The cards guide describes three ways to provision it.
</Accordion>

<Accordion title="source_id" icon="fa-repeat">
  The Pluxee identifier PayU returns in `field3` after a successful save (`save_sodexo_card=1`). Later payments send it as `source_id` and do not send the card details.
</Accordion>
