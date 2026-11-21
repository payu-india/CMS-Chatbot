---
title: Test Your Integration
excerpt: Test Checkout Plus with the UAT Bolt script and the published handler statuses
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Test Your Checkout Plus Integration | PayU Developer Docs
  description: >-
    Test a PayU Checkout Plus page with the UAT Bolt script. Check responseHandler
    for SUCCESS, FAILED, and CANCEL, and catchException for SDK exceptions.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

<Callout icon="⚠️" theme="warn">

Use the UAT Bolt script and your test key. Do not point a test page at the production script or a live key.

</Callout>

## Test Credentials

<!-- NEW CONTENT: Checkout Plus does not document key and salt retrieval. This block links to the shared guides. -->

<KeySaltReference />

## Point the Page at the UAT SDK

Load this script while you test:

`https://jssdk-uat.payu.in/bolt/bolt.min.js`

The production script is `https://jssdk.payu.in/bolt/bolt.min.js`. Do not use it for these tests.

## Test Scenarios

<Accordion title="responseHandler with txnStatus SUCCESS" icon="fa-circle-check">

The published handler logs `Your payment has been successful` when `BOLT.response.txnStatus` is `SUCCESS`.

<!-- DOCUMENTATION GAP: No test card, test VPA, or other trigger for a successful payment is documented. -->

</Accordion>

<Accordion title="responseHandler with txnStatus FAILED" icon="fa-xmark">

The published handler logs `Payment failed. Please try again.` when `BOLT.response.txnStatus` is `FAILED`.

<!-- DOCUMENTATION GAP: No input that forces FAILED is documented. -->

</Accordion>

<Accordion title="responseHandler with txnStatus CANCEL" icon="fa-ban">

The published handler logs `Payment failed. Please try again.` when `BOLT.response.txnStatus` is `CANCEL`.

<!-- DOCUMENTATION GAP: The control the customer uses to cancel is not named. -->

</Accordion>

<Accordion title="catchException" icon="fa-triangle-exclamation">

`catchException` captures the transaction message when an exception occurs. The sample logs `Payment failed. Please try again.`

<!-- DOCUMENTATION GAP: No exception catalogue is documented. -->

</Accordion>

<Accordion title="Duplicate txnid" icon="fa-copy">

`txnid` can be used only once. PayU does not accept a duplicate transaction ID.

<!-- DOCUMENTATION GAP: The error code and response body for a duplicate txnid are not documented. -->

</Accordion>

<Accordion title="status pending" icon="fa-clock">

The response parameter table says possible `status` values are `success`, `failure`, and `pending`, and that `failure` or `pending` should be treated as a failed transaction.

<!-- DOCUMENTATION GAP: No test steps are documented for producing pending. -->

<!-- VALIDATION NEEDED: Confirm whether pending must be treated as failed, or verified with verify_payment before a final decision. The Checkout Plus response table states the first rule. -->

</Accordion>

<!-- DOCUMENTATION GAP: A hash-mismatch scenario is not documented for Checkout Plus. No error code for a bad hash is published on these pages. Do not document E501 here unless the docs team adds it from a Checkout Plus source. -->
