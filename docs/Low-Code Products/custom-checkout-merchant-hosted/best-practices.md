---
title: Best Practices
excerpt: Handle card data, validate the method before you post, and verify every callback
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Merchant Hosted Checkout Best Practices | PayU Developer Docs
  description: >-
    Best practices for PayU Merchant Hosted Checkout. Protect card data, validate BIN and VPA, keep txnid unique, and verify every callback on the server.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Best Practices

These practices come from the Merchant Hosted security notes and the method guides. Apply them after the payment request is posting and the callback is wired.

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameters, hash, and samples for each method.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="./integration-guide/test-integration">
    Test key, salt, and method test values.
  </Card>
</Cards>

## Protect Card Data

<Accordion title="Keep card data off your server" icon="fa-shield-halved">
  Use HTTPS between the browser and your site, and between your server and PayU. The overview asks for TLS on data in transit.

  Do not store the CVV. Do not store the full card number on your servers. If you need a card for a later payment, use PayU Save Cards or another PCI-DSS tokenization service. The overview points to the PayU Save Cards docs for that.

  Guest checkout replaces the plain card number with an Alt ID. The cards guide says guest checkout with a plain card number was not allowed after 31 October 2023.

  For Pluxee, do not store the full card number, expiry, or CVV even when the customer agrees to save the card. Post `save_sodexo_card=1` and use the `source_id` PayU returns in `field3` for the next payment.

  Collect card numbers in fields you control, and validate them with the LUHN check named on the cards page.   If you store, process, or transmit cardholder data, complete PCI-DSS SAQ A-EP.

  <!-- DOCUMENTATION GAP: The overview names data encryption at rest, IP address restriction, and regular security audits. It does not describe how to do any of the three. -->
</Accordion>

## Validate Before You Post

<Accordion title="Check the method before _payment" icon="fa-check">
  - Cards: call `getBinInfo` with the first six digits. See [Cards](./integration-guide/build-integration/cards).
  - UPI Collect: call `validateVPA`. Collect is only for MCC 6012 and 6211. See [UPI Collect](./integration-guide/build-integration/upi-collect).
  - Pluxee: call `check_balance` and show the balance before payment. See [Pluxee](./integration-guide/build-integration/pluxee).
  - Net banking: call `getNetBankingStatus` when you need to know the bank is up. See [Net Banking](./integration-guide/build-integration/net-banking).

  Send the customer's real phone number and billing address when you have them. The parameter tables say those fields are used for fraud detection and chargebacks.
</Accordion>

## Transaction ID

<Accordion title="Use a new txnid for every attempt" icon="fa-fingerprint">
  You generate `txnid`. The saved-card parameters say PayU will not accept a duplicate transaction ID. Store the `txnid` you send so you can match it to the callback and to `verify_payment`.

  <!-- DOCUMENTATION GAP: This folder does not state a maximum length, an allowed character set, or a retry flow for txnid. -->
</Accordion>

## Verify Every Outcome

<Accordion title="Trust the payment only after server-side checks" icon="fa-circle-check">
  Generate the request hash on the server. On `surl` or `furl`, recompute the reverse hash before you update the order:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  Then call `verify_payment`. If the browser callback does not arrive, the production checklist says to confirm the status on the server and to use webhooks. See [Webhooks](doc:webhooks).

  Success samples in this folder use `status=success` and `error=E000`. The cards failure sample uses `status=failure` and `error=E1903`.

  <!-- DOCUMENTATION GAP: This folder does not document webhook signatures, idempotency, or the Dashboard screen used to subscribe to webhooks. -->
</Accordion>

## Next Steps

<Cards columns={2}>
  <Card title="Errors and Troubleshooting" icon="fa-triangle-exclamation" href="./errors-and-troubleshooting">
    E000, E1903, and the hash and callback cases named in the source.
  </Card>
  <Card title="Go-Live Checklist" icon="fa-list-check" href="./integration-guide/go-live-checklist">
    Live key, salt, and the production endpoint.
  </Card>
  <Card title="APIs" icon="fa-rectangle-api" href="./merchant-hosted-checkout-apis">
    `_payment` and the post-service commands used in this integration.
  </Card>
</Cards>
