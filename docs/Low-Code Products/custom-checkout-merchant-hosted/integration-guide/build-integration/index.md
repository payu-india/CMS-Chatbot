---
title: Build the Integration
excerpt: Choose a payment method and post it to PayU from your checkout
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Build the Merchant Hosted Checkout Integration | PayU Developer Docs
  description: >-
    Build PayU Merchant Hosted Checkout. Endpoints, hash rules, and guides for cards, UPI, net banking, wallets, PayPal, and Pluxee. Use the method navigator.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Build the Integration

Post each payment from your checkout to PayU. The endpoint is shared. `pg`, `bankcode`, and the extra fields change by method.

## Endpoints

| Purpose | Test | Production |
| --- | --- | --- |
| Collect payment | `POST https://test.payu.in/_payment` | `POST https://secure.payu.in/_payment` |
| `getBinInfo` and `validateVPA` samples in this folder | `POST https://test.payu.in/merchant/postservice?form=2` | Cards BIN production: `POST https://info.payu.in/merchant/postservice?form=2` |
| Post-service `command` APIs on the API index | Not stated | `POST https://info.payu.in/merchant/postservice.php?form=2` |

<!-- VALIDATION NEEDED: getBinInfo is documented at /merchant/postservice?form=2. The API index documents command APIs at /merchant/postservice.php?form=2. -->

<Callout icon="⚠️" theme="warn">
  The Advantage Club sample posts to `https://secure.payu.in/_payment`. The wallets guide says Advantage Club has no test environment and no test credentials.
</Callout>

## Choose a Payment Method

<Cards columns={2}>
  <Card title="Cards" icon="fa-credit-card" href="./cards">
    `pg=CC`. BIN check, saved card, guest checkout, and 3DS 2.0.
  </Card>
  <Card title="Net Banking" icon="fa-building-columns" href="./net-banking">
    Bank `bankcode`. Samples use `pg=TESTPG` and `bankcode=TESTPGNB`.
  </Card>
  <Card title="Wallets" icon="fa-wallet" href="./wallets">
    `pg=CASH` and a wallet `bankcode`. Advantage Club uses `pg=RD` and `bankcode=ADVCLUB`.
  </Card>
  <Card title="UPI Collect" icon="fa-mobile-screen" href="./upi-collect">
    `pg=UPI`, `bankcode=UPI`, and the customer VPA. MCC 6012 and 6211 only.
  </Card>
  <Card title="PayPal" icon="fa-globe" href="./paypal">
    `pg=PAYPAL` and `bankcode=PAYPAL`. Activate PayPal in the Dashboard first.
  </Card>
  <Card title="Pluxee" icon="fa-utensils" href="./pluxee">
    `pg=MC` and `bankcode=SODEXO`. Balance check, save card, and `source_id`.
  </Card>
</Cards>

These methods are documented outside this folder. Parameter tables are not copied here because this directory does not contain them.

- UPI Intent: [UPI Intent S2S](https://docs.payu.in/docs/upi-intent-server-to-server). The overview lists `bankcode=INTENT`.
- EMI: [Debit card](doc:collect-payments-with-emi-using-debit-card), [credit card](doc:collect-payments-with-emi-using-credit-card), [cardless EMI](doc:collect-payments-with-cardless-emi-using-merchant-hosted-checkout).
- BNPL: [Merchant Hosted BNPL workflow](https://docs.payu.in/docs/general-flow-bnpl-integration-with-merchant-hosted) and [Link and Pay](https://docs.payu.in/docs/collect-payments-with-bnpl-using-link-and-pay).
- EFTNET (NEFT/RTGS): [EFTNET](https://docs.payu.in/docs/collect-payments-with-eftnet-neftrtgs-seamless/).
- Net banking TPV: [Net Banking TPV](https://docs.payu.in/docs/net-banking-integration-for-tpv/).

## Before You Start

<Accordion title="Credentials" icon="fa-key">
  <KeySaltReference />
</Accordion>

<Accordion title="Hash generation" icon="fa-shield-halved">
  Generate the hash on your server. Do not put the salt in the browser.

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
  ```

  <HashingRequestParameters />
</Accordion>

<Accordion title="Callback URL requirements" icon="fa-link">
  `surl` is the success URL. `furl` is the failure URL. The production checklist expects you to receive the PayU response, verify the reverse hash, and confirm the status on the server if the callback fails.
</Accordion>

<Accordion title="Post-payment verification" icon="fa-circle-check">
  Call `verify_payment` for every payment. The method pages embed the Verify Payment request. The API index hashes post-service commands as `sha512(key|command|var1|SALT)`.
</Accordion>
