---
title: Best Practices
excerpt: >-
  Card data, transaction ids, callbacks, and the failure message for Merchant
  Hosted Checkout.
deprecated: false
hidden: true
metadata:
  title: Merchant Hosted Checkout Best Practices
  description: >-
    Best practices for PayU Merchant Hosted Checkout: do not store card data,
    keep txnid unique, verify the callback, and read E1903 as a bank decline.
  keywords:
    - payu merchant hosted best practices
    - payu do not store cvv
    - payu callback verify payment
  robots: index
next:
  description: Explore related information and resources.
---
These practices come from the Merchant Hosted security list and the method pages. Use them after the payment form is in place.

<Cards columns="2">
  <Card title="Build Integration" href="./integration-guide/build-integration" icon="fa-code">
    Parameters, hash, form POST, reverse hash, and Verify Payment.
  </Card>
  <Card title="Test Integration" href="./integration-guide/test-integration" icon="fa-flask">
    Test key, salt, and the test values for each method.
  </Card>
</Cards>

***

## Conversion and UX

<Accordion title="Collect real customer fields" icon="fa-user-pen">
  The source says `email`, `phone`, and `address1` help with fraud detection and chargebacks. Send the real values.
</Accordion>

<Accordion title="Use secure fields for cards" icon="fa-keyboard">
  The integration best-practices list says to use secure input fields for card details and to transmit them over HTTPS.
</Accordion>

<Accordion title="Do not submit the same txnid twice" icon="fa-spinner">
  The saved-card text says PayU will not accept a duplicate transaction id. A second attempt needs a new `txnid` and a new hash.
</Accordion>

***

## Transaction ID Strategy

<Accordion title="Keep every txnid unique" icon="fa-fingerprint">
  `txnid` is your reference for the order. The source says it must be unique and that PayU will not accept a duplicate.

  <!-- DOCUMENTATION GAP: A character limit and a recommended id format are not in the Merchant Hosted pages. -->
</Accordion>

<Accordion title="Use a new txnid after a failure" icon="fa-rotate-right">
  Generate a new `txnid` and a new hash before you post again. Do not reuse the failed attempt's id.
</Accordion>

***

## Handling Pending Payments

<Accordion title="Pending is not defined in this source" icon="fa-clock">
  The test steps say to simulate a pending transaction. They do not say which status value comes back, or whether you may fulfil the order.

  <!-- DOCUMENTATION GAP: Do not copy a NEFT/RTGS pending timeline from PayU Hosted Checkout. It is not in the Merchant Hosted pages. -->
</Accordion>

***

## Callback Resilience

<Accordion title="Verify when the callback does not arrive" icon="fa-satellite-dish">
  The production checklist says to confirm the transaction on the server if the callback fails, and to use webhooks to hear callbacks. Call `verify_payment` with the `txnid`.
</Accordion>

***

## Error Recovery UX

<Accordion title="Use the status values the samples show" icon="fa-triangle-exclamation">
  | What the sample shows | What it means in the source |
  | --- | --- |
  | `status=success`, `error=E000` | No Error |
  | `status=failure`, `error=E1903` | Authorization failed at Bank. `field7` is `AUTHNEGATIVE` |

  <!-- DOCUMENTATION GAP: userCancelled and a pending customer message are not in the Merchant Hosted samples. -->
</Accordion>

***

## Next Steps

<Cards columns="3">
  <Card title="Go-Live Checklist" href="./integration-guide/go-live-checklist" icon="fa-list-check">
    Production key, salt, and endpoint.
  </Card>
  <Card title="Errors and Troubleshooting" href="./errors-and-troubleshooting" icon="fa-circle-xmark">
    Hash, callback, and E1903.
  </Card>
  <Card title="APIs" href="./merchant-hosted-checkout-apis" icon="fa-rectangle-api">
    Collect Payment and Verify Payment.
  </Card>
</Cards>
