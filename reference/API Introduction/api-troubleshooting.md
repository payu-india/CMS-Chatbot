---
title: API Troubleshooting
deprecated: false
hidden: true
metadata:
  robots: index
---
Diagnose the most common PayU API integration failures. For exhaustive list of payment error codes, refer to the [Error Codes](ref:error-codes) page.

## Quick Triage Checklist

Go through this checklist before analysing the errors:

<Accordion title="Checklist" icon="far fa-table-list">
  - [x] Are you calling the correct **API family** and **base URL**?
  - [x] Are key, salt, and host all from the **same environment** (Test vs Production)?
  - [x] Is the **hash/token** generated with the documented formula for this request?
  - [x] Is `txnid` unique for a new payment?
  - [x] Did you validate reverse hash and then **Verify Payment**?
</Accordion>

## Issues and Troubleshooting

These are the common issues you may get while working with our APIs.

<Accordion title="Hash Mismatch" icon="far fa-hashtag-lock">
  **Reason:**

  - Wrong salt for the key

  - Incorrect pipe-separated field order

  - Missing empty UDF placeholders

  - Feature fields (SI/TPV/split/offers) omitted from hash input

  - `api_version`-dependent fields not included

  **Recommended Fix**

  - Go through the [Generate Hash](doc:hashing-request-and-response) document for correct ways of generating a hash value.

  - Use [Hash Verification Tool](doc:using-payu-hash-verification-tool) for easy hash generation.

  - Compare against [API Authentication and Security.](doc:api-authentication-and-security)
</Accordion>

<Accordion title="Wrong Environment or Base URL" icon="far fa-arrow-up-from-dotted-line">
  **Symptoms**

  - Auth failures

  - Unexpected HTML/login responses

  - Works in docs Try It but fails in your code (or reverse)

  **Recommended Fix**

  - Go through the [API Environments and Base URLs](doc:api-environments-and-base-urls) document to make sure you are using the correct environment and the respective base URL.

  - Ensure general APIs use `postservice.php?form=2`

  - Ensure `_payment` calls use `/_payment` and not the general API host
</Accordion>

<Accordion title="Callback (surl/furl) Not Received" icon="far fa-link-horizontal">
  **Reason:**

  - URL not publicly reachable

  - HTTPS/certificate issues

  - Firewall blocking PayU posts

  - App expecting JSON while receiving form POST

  **Recommended Fix:**

  - Test with a public HTTPS endpoint

  - Log raw body/headers temporarily in Test

  - Go through the [Handling Web Checkout](doc:handling-web-checkout) document for ways to handle web checkouts.

  - Validate using webhooks and Verify Payment API additional validation.
</Accordion>

<Accordion title="Payment in the Pending Status" icon="far fa-airplay">
  **Possible Reasons**

  - Customer dropped off before completing bank/UPI journey
  - Async authorization still in progress
  - Callback missed and status never reconciled

  **Recommended Fix:**

  - Poll the [Verify Payment](ref:verify_payment_api) API

  - Wait/retry according to product guidance for that payment mode

  - Use webhooks for later terminal updates
</Accordion>

<Accordion title="Duplicate txnid" icon="far fa-display-chart-up-circle-dollar">
  **Recommended Fix:**

  - Generate a new `txnid` for each new attempt

  - If the previous attempt result is unknown, verify that `txnid` before creating another payment
</Accordion>

<Accordion title="OAuth Token Errors (Payouts/Partner)" icon="far fa-circle-half-stroke-horizontal">
  **Possible Reason**

  - Wrong token URL (UAT vs Production)

  - Expired token

  - Incorrect client/merchant credentials

  - Calling resource API without token

  **Recommended Fix:**

  - Regenerate token via the product token API

  - Confirm hosts in the environments page
</Accordion>

## Escalation information to collect

Ensure you have these before contacting the [PayU Support:](https://help.payu.in)

- Environment used (Test or Production)
- Merchant key (not salt)
- `txnid` / `mihpayid` / request IDs
- Approximate timestamp (with timezone)
- API endpoint called
- Sanitized request/response (secrets removed)
- Whether callback/webhook was received
