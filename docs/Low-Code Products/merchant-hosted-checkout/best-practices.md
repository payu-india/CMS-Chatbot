---
title: Best Practices
excerpt: Card data handling, pre-checks, and callback verification for Merchant Hosted Checkout
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Merchant Hosted Checkout Best Practices | PayU Developer Docs
  description: >-
    Best practices for PayU Merchant Hosted Checkout: do not store card data, validate BIN and VPA, send 3DS data, and verify the callback on the server.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Best Practices

These practices come from the Merchant Hosted security list, the integration best-practices list, and the card, UPI, and Pluxee pages. Use them after the payment request itself is in place.

<Cards columns={2}>
  <Card title="Build the Integration" icon="fa-code" href="./integration-guide/build-integration">
    Parameter tables and samples for each payment method.
  </Card>
  <Card title="Test Your Integration" icon="fa-flask" href="./integration-guide/test-integration">
    Test key, salt, and the test values published for each method.
  </Card>
</Cards>

## Card Data Handling

<Accordion title="Use secure input fields" icon="fa-keyboard">
  The legacy best-practices list says to use secure input fields for card details, such as those from a PCI-DSS compliant payment gateway.
</Accordion>

<Accordion title="Do not store sensitive card data" icon="fa-ban">
  Do not store the CVV or the full card number. The Pluxee page also says you must not store the full card number, expiry, or CVV even when the customer consents to save the card.
</Accordion>

<Accordion title="Tokenize instead of storing the PAN" icon="fa-id-card">
  For repeat payments, the source says to use PayU Save Cards or a PCI-DSS tokenization service. The cards page posts `store_card_token`, `storecard_token_type`, and `additional_info` instead of the raw card for a saved card.
</Accordion>

<Accordion title="Encrypt data in transit" icon="fa-lock">
  Use HTTPS and TLS between the customer's browser and your site, and between your server and PayU.
</Accordion>

<Accordion title="Stay inside the stated PCI scope" icon="fa-shield-halved">
  If you store, process, or transmit cardholder data, the source says you must complete PCI-DSS SAQ A-EP. Collecting cards on your site is in that scope. If you use only UPI and wallets, the source still says the website must be secure.
</Accordion>

<Accordion title="Encrypt at rest and run security audits" icon="fa-file-shield">
  The security list says to encrypt sensitive data at rest and to run regular security audits.

  <!-- DOCUMENTATION GAP: The source does not name an algorithm, a key-management practice, or an audit standard. -->
</Accordion>

## Authenticate Before You Post

<Accordion title="Validate the card BIN" icon="fa-credit-card">
  Call `getBinInfo` with the first six digits before a card payment. See [Cards](./integration-guide/build-integration/cards).
</Accordion>

<Accordion title="Send 3DS 2.0 browser data" icon="fa-window-maximize">
  The cards page says PayU supports 3DS 2.0 on Merchant Hosted Checkout and that you send `threeDS2RequestData` with the card request. The sample also includes `txn_s2s_flow=4`.
</Accordion>

<Accordion title="Use Alt ID for guest checkout" icon="fa-user">
  The cards page says plain guest card numbers were not allowed after 31 Oct 2023, and that the replacement is an Alt ID. The three scenarios are on the cards page. Guest checkout has to be enabled by your Key Account Manager or PayU Integration Support.
</Accordion>

<Accordion title="Validate the VPA" icon="fa-at">
  Call `validateVPA` before a UPI Collect payment. UPI Collect in the source is limited to MCC 6012 and 6211.
</Accordion>

<Accordion title="Check the Pluxee balance" icon="fa-wallet">
  Call `check_balance` before a Pluxee `_payment` request and show the balance on your checkout.

  <!-- DOCUMENTATION GAP: The check_balance request body is not in this folder. The Pluxee page links the Fetch Balance API. -->
</Accordion>

<Accordion title="Follow the UPI Collect limits" icon="fa-mobile-screen">
  Web and Android integrations in the source must move to UPI Intent S2S. Seamless form POST does not support Intent. iOS may keep a deeplink and UPI Collect.
</Accordion>

## Hash, Callback, and Verification

<Accordion title="Generate the hash on the server" icon="fa-shield-halved">
  The salt stays on the server. The method pages use:

  ```
  sha512(key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT)
  ```

  <!-- VALIDATION NEEDED: The legacy overview also shows a hash string with no UDF fields. Do not switch formulas until that conflict is resolved. -->
</Accordion>

<Accordion title="Verify the reverse hash before you fulfil" icon="fa-not-equal">
  Rebuild the response hash and compare it with the hash PayU sent. The order printed on the UPI Collect page is:

  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```
</Accordion>

<Accordion title="Do not trust the browser callback alone" icon="fa-plug">
  The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks to hear callbacks. Call `verify_payment` before you fulfil the order.
</Accordion>

<Accordion title="Send real customer fields" icon="fa-user">
  The Collect Payment API introduction and the method parameter tables say `email`, `phone`, and `address1` help with fraud detection and chargebacks, and that you should send the correct values.
</Accordion>

<Accordion title="Keep bankcode exact" icon="fa-font">
  The legacy overview says bank codes are case-sensitive.

  <!-- VALIDATION NEEDED: Wallet cURL samples use pg=cash and bankcode=paytm. -->
</Accordion>

<Accordion title="Restrict IPs and secure webhooks" icon="fa-network-wired">
  The security list names IP address restriction and webhook security.

  <!-- DOCUMENTATION GAP: No allow-list steps and no webhook signing steps are in this folder. -->
</Accordion>

## Next Steps

<Cards columns={2}>
  <Card title="Go-Live Checklist" icon="fa-list-check" href="./integration-guide/go-live-checklist">
    Production key, salt, and endpoint.
  </Card>
  <Card title="Errors and Troubleshooting" icon="fa-triangle-exclamation" href="./errors-and-troubleshooting">
    E000, E1903, and the hash and callback symptoms named in the source.
  </Card>
  <Card title="Cards" icon="fa-credit-card" href="./integration-guide/build-integration/cards">
    BIN, saved cards, Alt ID, and 3DS 2.0.
  </Card>
  <Card title="UPI Collect" icon="fa-mobile-screen" href="./integration-guide/build-integration/upi-collect">
    VPA validation and the NPCI limits.
  </Card>
</Cards>
