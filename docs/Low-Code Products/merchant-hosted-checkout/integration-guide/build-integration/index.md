---
title: Build the Integration
excerpt: Choose a payment method and post it to PayU from your checkout
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Build Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Build PayU Merchant Hosted Checkout. Post to _payment with pg and bankcode for cards, net banking, wallets, UPI Collect, PayPal, and Pluxee.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Build the Integration

Collect the payment details on your site, generate the hash on your server, and form-post the request to `_payment`. Each method below has its own `pg`, `bankcode`, and extra fields.

## Endpoints

| Environment | URL |
| --- | --- |
| Test | `POST https://test.payu.in/_payment` |
| Production | `POST https://secure.payu.in/_payment` |

<Callout icon="⚠️" theme="warn">
  BIN lookup (`getBinInfo`), Validate VPA (`validateVPA`), and Verify Payment (`verify_payment`) go to the post-service URL, not to `_payment`. The legacy pages disagree on whether that path includes `.php`. See [How It Works](../../how-it-works).
</Callout>

## Choose a Payment Method

<Cards columns={2}>
  <Card title="Cards" icon="fa-credit-card" href="./cards">
    `pg=CC`. `bankcode` is network-specific. Includes BIN lookup, saved cards, guest Alt ID, and 3DS 2.0.
  </Card>
  <Card title="Net Banking" icon="fa-building-columns" href="./net-banking">
    Parameter table says `pg=NB`. Test samples use `pg=TESTPG` and `bankcode=TESTPGNB`.
  </Card>
  <Card title="Wallets" icon="fa-wallet" href="./wallets">
    `pg=CASH` and a wallet `bankcode`. Advantage Club uses `pg=RD` and `bankcode=ADVCLUB`.
  </Card>
  <Card title="UPI Collect" icon="fa-mobile-screen" href="./upi-collect">
    `pg=UPI`, `bankcode=UPI`, and `vpa`. Validate the VPA first. MCC 6012 and 6211 only.
  </Card>
  <Card title="PayPal" icon="fa-globe" href="./paypal">
    `pg=PAYPAL` and `bankcode=PAYPAL`. Activate PayPal on the Dashboard first.
  </Card>
  <Card title="Pluxee" icon="fa-utensils" href="./pluxee">
    `pg=MC` and `bankcode=SODEXO`. Check the card balance before you post the payment.
  </Card>
</Cards>

These methods are documented outside this folder. The legacy Merchant Hosted pages only link to them:

| Method | Where the steps live |
| --- | --- |
| EMI | [Debit card EMI](https://docs.payu.in/docs/collect-payments-with-emi-using-debit-card), [credit card EMI](https://docs.payu.in/docs/collect-payments-with-emi-using-credit-card), [cardless EMI](https://docs.payu.in/docs/collect-payments-with-cardless-emi-using-merchant-hosted-checkout), [native OTP](https://docs.payu.in/docs/native-otp-flow-integration) |
| BNPL | [Merchant Hosted BNPL workflow](https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted), [Link and Pay](https://docs.payu.in/docs/collect-payments-with-bnpl-using-link-and-pay) |
| EFTNET (NEFT/RTGS) | [EFTNET seamless](https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless) |
| Net Banking TPV | [Net banking TPV](https://docs.payu.in/docs/net-banking-integration-for-tpv) |
| UPI Intent | [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server) |

## Before You Start

<Accordion title="Credentials" icon="fa-key">
  Use the test key and salt while you build. The salt is not a value you put in frontend code.

  <KeySaltReference />
</Accordion>

<Accordion title="Hash generation" icon="fa-shield-halved">
  Request hash, from the method pages:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  Generate it on the server. See [How It Works](../../how-it-works) for the second formula that omits UDF fields.
</Accordion>

<Accordion title="Callback URL requirements" icon="fa-link">
  `surl` and `furl` must be URLs PayU can redirect the customer to. The production checklist says the production site is `https://secure.payu.in/` for the PayU endpoint. Your own callback URLs are on your site. Cards, PayPal, and Pluxee describe `surl` as success and `furl` as failure.
</Accordion>

<Accordion title="Post-payment verification" icon="fa-circle-check">
  Verify every payment on the server with `verify_payment`. The legacy checklist says to confirm the status on the server if the callback fails, and to use webhooks to hear callbacks.
</Accordion>
