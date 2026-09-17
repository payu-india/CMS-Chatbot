---
title: Testing PayU APIs
deprecated: false
hidden: true
metadata:
  robots: index
---
Always test APIs before going to production. Testing validates hash generation, callbacks, Verify Payment, and product-specific edge cases without moving real money.

## Testing Workflow

Below is the testing workflow:

<Accordion title="1. Test Credentials and Environments" icon="far fa-screwdriver-wrench">
  To begin with you should:

  - Generate Test key and salt from the Dashboard: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)

  - Use Test hosts from [API Environments and Base URLs](doc:api-environments-and-base-urls)

  - Not mix Production keys with Test URLs (or the reverse)
</Accordion>

<Accordion title="2. Test Payment Instruments" icon="far fa-credit-card">
  Test PayU's payment instruments as a next step:

  For checkout and Collect payment testing, use only documented test instruments. Product-specific fixtures may also exist (for example, EMI test cards/wallets in custom blocks used by Affordability docs).
</Accordion>

<Accordion title="3. API Reference Try It Playground" icon="far fa-display-code">
  Most API Reference pages support interactive calls:

  1. Open an operation from [API Reference](ref:introduction-api-reference).
  2. Fill required parameters.
  3. Generate hash when prompted.
  4. Click **Try It**.
  5. Inspect response and copy language bindings as needed.
</Accordion>

<Accordion title="4. Postman and Local Testing" icon="far fa-sign-posts">
  - Use Postman collections where available.

  - Go through the <Anchor target="_blank" href="https://payu-hosted-checkout.readme.io/v1/recipes/curl-walkthrough">cURL mechanics.</Anchor>

  - Keep secrets in Postman environments, not shared collections.
</Accordion>

<Accordion title="5. Validate these in Test" icon="far fa-note-sticky">
  | Area          | Validate                                             |
  | :------------ | :--------------------------------------------------- |
  | Auth          | Correct hash/token per API family                    |
  | Idempotency   | Unique `txnid` per attempt                           |
  | Callbacks     | `surl`/`furl` reachability and reverse hash          |
  | Webhooks      | Event receipt, signature checks, duplicate handling  |
  | Status truth  | Verify Payment matches final business state          |
  | Failure paths | Declines, cancelled payments, missing params         |
  | Refunds       | Full/partial refund behavior where supported in Test |
</Accordion>

<Accordion title="6. Go-Live Readiness" icon="far fa-file-video">
  Before switching to Production:

  - Replace Test host, key, and salt together
  - Re-run smoke tests on Production credentials in a controlled manner
  - Confirm webhook URLs and HTTPS certificates
  - Follow product Integration Checklists in Collect Payments / SDK guides
</Accordion>
