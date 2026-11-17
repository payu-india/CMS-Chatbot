---
title: Go-Live Checklist
excerpt: Switch Checkout Plus from the UAT Bolt script to the production script
deprecated: false
hidden: false
updatedAt: "2026-11-17"
metadata:
  title: Checkout Plus Go-Live Checklist | PayU Developer Docs
  description: >-
    Before live Checkout Plus traffic, switch bolt.min.js to the production
    script host and confirm your handler results, callbacks, and payment verification.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

Complete the production script switch before you send live traffic through Checkout Plus.

<Accordion title="Switch the Bolt script to production" icon="fa-code">

Replace `https://jssdk-uat.payu.in/bolt/bolt.min.js` with `https://jssdk.payu.in/bolt/bolt.min.js`.

</Accordion>

<Accordion title="Update credentials" icon="fa-key">

Pass your live merchant key in the `key` field.

<!-- DOCUMENTATION GAP: The Checkout Plus pages do not describe where to copy the live key and salt, and they do not list a production _payment URL. -->

</Accordion>

<Accordion title="Security" icon="fa-shield-halved">

Card entry stays in the PayU modal. The overview says this keeps PCI-DSS collection off your page.

<!-- DOCUMENTATION GAP: Server-side hash generation, salt handling, and HTTPS for surl and furl are not stated. The launch sample uses http://thirdparty.com for surl and furl. No SAQ type is documented. -->

</Accordion>

<Accordion title="Callback URLs" icon="fa-link">

`surl` and `furl` are mandatory. `surl` is the success response URL. `furl` is the failure response URL.

<!-- DOCUMENTATION GAP: Public HTTPS requirements, and any webhook fallback, are not documented for Checkout Plus. -->

</Accordion>

<Accordion title="Error handling" icon="fa-triangle-exclamation">

Handle `txnStatus` values `SUCCESS`, `FAILED`, and `CANCEL` in `responseHandler`, and handle `catchException`.

The response table says to treat `status` of `failure` or `pending` as a failed transaction.

The API page names Verify Payment (`verify_payment`) for reconciliation. The launch sample does not call it. Do not fulfil an order from the browser handler alone.

<!-- VALIDATION NEEDED: The pending-as-failed instruction conflicts with the usual PayU guidance to verify pending and not treat it as a final failure. Confirm the Checkout Plus rule before go-live copy is treated as final. -->

</Accordion>

<Accordion title="Payment method coverage" icon="fa-credit-card">

The overview lists Credit Card, Debit Card, Net Banking, UPI, Wallet, EMI, and BNPL.

<!-- DOCUMENTATION GAP: No production test matrix is documented for these methods. -->

</Accordion>

<Accordion title="PayU Dashboard access" icon="fa-gauge">

<!-- DOCUMENTATION GAP: Dashboard, settlement, and webhook steps are not documented in the Checkout Plus pages. -->

</Accordion>
