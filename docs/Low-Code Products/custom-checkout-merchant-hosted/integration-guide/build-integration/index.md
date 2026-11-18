---
title: Build the Integration
excerpt: Choose a payment method and post it to PayU _payment
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Build the Merchant Hosted Integration | PayU Developer Docs
  description: >-
    Build PayU Merchant Hosted Checkout. One _payment endpoint, a server-side SHA-512 hash, and a separate parameter set for each payment method. Start here.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Build the Integration

Each payment method is a form POST to the same `_payment` URL. `pg` and `bankcode` change with the method. Some methods need a call before that post.

## Endpoints

| Environment | Collect payment |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

<Callout icon="⚠️" theme="warn">
  Advantage Club wallet samples in the source use the production URL. That page says there is no test environment for Advantage Club. Card BIN lookup and UPI Validate VPA use the postservice URL, not `_payment`. See [APIs](../../merchant-hosted-checkout-apis).
</Callout>

## Choose a Payment Method

<Cards columns={2}>
  <Card title="Cards" icon="fa-credit-card" href="./cards">
    pg CC. Collect the card on your page. Includes saved card, guest checkout, and 3DS 2.0.
  </Card>
  <Card title="UPI Collect" icon="fa-mobile-screen" href="./upi-collect">
    pg UPI, bankcode UPI, plus the customer VPA. Validate the VPA first. MCC 6012 and 6211 only.
  </Card>
  <Card title="UPI Intent" icon="fa-qrcode" href="./upi-intent">
    The source overview gives bankcode INTENT. The page in this folder has no parameter table.
  </Card>
  <Card title="Net Banking" icon="fa-building-columns" href="./net-banking">
    Test sample uses pg TESTPG and bankcode TESTPGNB. Production bank codes are bank-specific.
  </Card>
  <Card title="Net Banking TPV" icon="fa-building-columns" href="./net-banking-tpv">
    Account number and IFSC are mentioned on the overview. This folder has no TPV parameter table.
  </Card>
  <Card title="Wallets" icon="fa-wallet" href="./wallets">
    pg CASH and a wallet bankcode. Advantage Club uses pg RD and bankcode ADVCLUB.
  </Card>
  <Card title="EMI" icon="fa-calendar" href="./emi">
    Eligibility is described. The request parameters are not in this folder.
  </Card>
  <Card title="BNPL" icon="fa-clock" href="./bnpl">
    pg and bankcode depend on the provider. Values are not in this folder.
  </Card>
  <Card title="Pluxee" icon="fa-utensils" href="./pluxee">
    pg MC, bankcode SODEXO. Check the card balance before you debit it.
  </Card>
  <Card title="PayPal" icon="fa-paypal" href="./paypal">
    The PayPal page posts pg PAYPAL and bankcode PAYPAL. Activate PayPal on the Dashboard first.
  </Card>
  <Card title="EFTNET" icon="fa-money-bill-transfer" href="./eftnet">
    NEFT/RTGS. The overview gives two different pg values. No request sample is in this folder.
  </Card>
</Cards>

## Before You Start

<Accordion title="Credentials" icon="fa-key">
  Use the test key and salt until you go live.

  <KeySaltReference />
</Accordion>

<Accordion title="Hash generation" icon="fa-shield-halved">
  Generate the hash on the server:

  ```text
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
  ```

  The salt never goes in the page or the mobile app. See [How It Works](../../how-it-works) for the reverse hash and the conflicting shorter sample.
</Accordion>

<Accordion title="Callback URL requirements" icon="fa-link">
  `surl` is the success URL and `furl` is the failure URL on the cards, PayPal, and Pluxee pages, and in the HTML samples. PayU posts the payment result to the URL it redirects to.

  <!-- VALIDATION NEEDED: The net-banking and wallets parameter tables swap those descriptions. The UPI Collect table describes them correctly and swaps the example URLs. -->
</Accordion>

<Accordion title="Post-payment verification" icon="fa-circle-check">
  Check the reverse hash on the callback. Call Verify Payment from your server for every transaction. The source says to use webhooks when the callback does not arrive.
</Accordion>
