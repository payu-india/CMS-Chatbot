---
title: Go-Live Checklist
excerpt: What to switch before you accept live Merchant Hosted payments
deprecated: false
hidden: true
updatedAt: "2026-11-18"
metadata:
  title: Go-Live Checklist — Merchant Hosted Checkout | PayU Developer Docs
  description: >-
    Go live with Merchant Hosted Checkout. Switch to the live key and salt, use the production _payment URL, and verify every payment on the server. Then monitor.
  robots: index
agentTools:
  projectIndex: "https://docs.payu.in/llms.txt"
---

# Go-Live Checklist

Complete this before you accept live payments. The list below is the production checklist in the Merchant Hosted source, plus the security points on the overview.

<Accordion title="Update credentials" icon="fa-key">
  Replace the test key and salt with the live key and salt.

  1. Log in to the PayU Dashboard and switch to Live Mode.
  2. Open **Payment Gateway → Web Integration → Key Salt Details**.
  3. Copy the key and salt.
  4. Put them in the payment integration in place of the test key and test salt.
</Accordion>

<Accordion title="Switch the endpoint" icon="fa-server">
  The method pages use `https://secure.payu.in/_payment` for production.

  <!-- VALIDATION NEEDED: The production checklist writes the production endpoint as https://secure.payu.in/ without _payment. The method pages include /_payment. -->
</Accordion>

<Accordion title="Security" icon="fa-shield-halved">
  - Serve the site and the calls to PayU over HTTPS.
  - Generate the hash on the server. Keep the salt off the page.
  - If you store, process, or transmit cardholder data, the source says you must be PCI-DSS compliant and names SAQ A-EP.
  - Do not store the CVV. Do not store the full card number. For Pluxee, do not store the card number, expiry, or CVV even with the customer's consent.
</Accordion>

<Accordion title="Callback URLs" icon="fa-link">
  - `surl` and `furl` must be the URLs where you can read PayU's post.
  - Check the reverse hash before you accept the callback. The source points at the hash guide for this check.
  - If the callback fails, confirm the status on the server. The source says to use webhooks for that.

  <!-- DOCUMENTATION GAP: The checklist does not say the URLs must be publicly reachable, and it does not name webhook events. -->
</Accordion>

<Accordion title="Error handling" icon="fa-triangle-exclamation">
  Verify the response from PayU. Do not treat the browser callback as the only confirmation. Call Verify Payment. The source says to confirm on the server if the callback fails.
</Accordion>

<Accordion title="Payment method coverage" icon="fa-credit-card">
  Test each method you will enable. The overview says to test them before production.

  - PayPal must be activated on the Dashboard.
  - UPI Collect is only for MCC 6012 and 6211, and the NPCI note restricts where Collect can be used.
  - Advantage Club has no test environment in the source. The wallets page says to test it on production.
</Accordion>

<Accordion title="Final verification" icon="fa-list-check">
  The production checklist asks you to confirm all of the following:

  1. The checkout fields on your site are collected and validated.
  2. You have verified the response from PayU.
  3. The callback hash has been checked.
  4. If the callback fails, the status is confirmed on the server, using webhooks and Verify Payment.
  5. The integration points at the production endpoint.
</Accordion>

<Accordion title="PayU Dashboard access" icon="fa-gauge">
  You need Dashboard access to copy the live key and salt, to activate PayPal, and to turn on webhooks. The source does not describe settlement or reporting screens.

  <!-- DOCUMENTATION GAP: Settlement configuration and reporting setup are not in the Merchant Hosted go-live page. -->
</Accordion>
