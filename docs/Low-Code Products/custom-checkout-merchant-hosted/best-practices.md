---
title: Best Practices
excerpt: How to protect card data, hash on the server, and confirm every payment
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Best Practices — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Merchant Hosted Checkout practices from the source: do not store CVV or the
    full card number, hash on the server, and verify the payment if the callback fails.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Best Practices

These are the practices written in the Merchant Hosted source. You host the form, so card data and the hash are your responsibility. The callback is not the only confirmation.

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameters and samples for each method.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="./integration-guide/test-integration">
    Test credentials the source actually lists.
  </Card>
</Cards>

## Protect Card Data

<Accordion title="Collect and store card data only as the source allows" icon="fa-shield-halved">
  - Use secure input fields for card details. The source points at a PCI-DSS compliant approach for those fields.
  - Encrypt payment data in transit with HTTPS and TLS. The source also says to encrypt sensitive data at rest.
  - Never store the CVV. Never store the full card number on your servers.
  - If a card must be reused, the source says to use tokenization or PayU Save Cards. The Save Cards request is not in this folder. Saved-card fields that are in this folder (`store_card_token`, `storecard_token_type`, `additional_info`) are on the [Cards](./integration-guide/build-integration/cards) page.
  - Pluxee: do not store the full card number, expiry, or CVV even if the customer agrees. Post `save_sodexo_card=1` and later pay with `source_id`.
  - Guest checkout: the source says plain card numbers are replaced by an Alt ID, and it cites 31 October 2023. The three scenarios are on the Cards page.

  <Callout icon="⚠️" theme="warn">
    If you store, process, or transmit cardholder data, the source says you must be PCI-DSS compliant and names SAQ A-EP. If you use only UPI and wallets, the source says to keep the website secure.
  </Callout>
</Accordion>

## Secure the Request

<Accordion title="Hash on the server and verify the response" icon="fa-lock">
  Generate the SHA-512 hash on the server. The salt stays on the server.

  The method pages use:

  ```text
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||Salt)
  ```

  <!-- VALIDATION NEEDED: A second Python sample on the overview uses fewer pipes between email and the salt. Do not switch to that string unless PayU confirms it. -->

  Recreate the reverse hash before you accept the order. The formula on the UPI Collect page is:

  ```text
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  The source also says to implement IP address restriction and to run regular security audits.

  <!-- DOCUMENTATION GAP: The source does not say which IPs to allow, how to restrict them, or what an audit should cover. -->
</Accordion>

## Verify Every Payment

<Accordion title="Do not fulfil from the browser callback alone" icon="fa-circle-check">
  If the callback fails, confirm the transaction on the server with Verify Payment. The source says to use webhooks to hear callbacks.

  The source also says to make sure webhooks are configured, and to check webhook logs when updates are not processed.

  <!-- DOCUMENTATION GAP: This folder does not list webhook events, a signing method, or the Dashboard screen used to subscribe. The PayU Hosted path "Developer → Webhooks" is not in the Merchant Hosted source and is not repeated here. -->
</Accordion>

## Keep the Transaction ID Unique

<Accordion title="One txnid per attempt" icon="fa-fingerprint">
  `txnid` is your id for the payment. The saved-card parameters say it must be unique and that PayU will not accept a duplicate transaction id.

  <!-- DOCUMENTATION GAP: No maximum length, character set, or retry procedure is in this folder. Do not copy a 25-character format from PayU Hosted Checkout. -->
</Accordion>

## Authenticate Before You Post

<Accordion title="Run the pre-step the method page describes" icon="fa-user-check">
  - Cards: you can call `getBinInfo` with the first six digits. For 3DS 2.0, the cards page says to send `threeDS2RequestData`.
  - UPI Collect: validate the VPA first. Collect is only for MCC 6012 and 6211. The NPCI note says seamless form post moves to UPI Intent for Android and desktop web.
  - Pluxee: `check_balance` is recommended before `_payment`.
  - Net banking: `getNetBankingStatus` checks whether the bank is up. The request fields are not in this folder.
</Accordion>

## Send Accurate Checkout Data

<Accordion title="Post the real customer and method values" icon="fa-table">
  The parameter descriptions say `firstname`, `email`, `phone`, and the billing address help fraud detection and chargebacks. The saved-card table says the phone number must be correct.

  `bankcode` is case-sensitive. `pg` and `bankcode` have conflicts between the overview and the method pages. Those conflicts are flagged on the method pages. Do not invent a third value to resolve them.
</Accordion>

## Test Before Production

<Accordion title="Test, then switch credentials" icon="fa-flask">
  Test a successful payment, a failed payment, and a pending payment with the test key and salt. Test each method you will enable. After that, replace the test key and salt, and watch transactions in the first days after go-live.

  The switch steps are on the [Go-Live Checklist](./integration-guide/go-live-checklist).

  <!-- DOCUMENTATION GAP: Pending has no trigger and no sample response in this folder. -->
</Accordion>

## Next Steps

<Cards columns={2}>
  <Card title="Go-Live Checklist" icon="fa-list-check" href="./integration-guide/go-live-checklist">
    Live key, salt, and the production endpoint.
  </Card>
  <Card title="Errors and Troubleshooting" icon="fa-triangle-exclamation" href="./errors-and-troubleshooting">
    E000, E1903, and the failures the source describes without a code.
  </Card>
  <Card title="Cards" icon="fa-credit-card" href="./integration-guide/build-integration/cards">
    Card fields, saved card, Alt ID, and 3DS 2.0.
  </Card>
  <Card title="APIs" icon="fa-rectangle-api" href="./merchant-hosted-checkout-apis">
    _payment and the postservice commands.
  </Card>
</Cards>
