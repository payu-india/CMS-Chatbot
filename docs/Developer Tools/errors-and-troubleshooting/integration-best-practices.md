---
title: Integration Best Practices
excerpt: >-
  Best practices to prevent PayU payment integration errors across Hosted
  Checkout, Merchant Hosted Checkout, S2S, Webhooks, and other products.
deprecated: false
hidden: true
metadata:
  robots: index
---
Use these best practices to prevent common PayU payment errors before they reach production.

## Generate and Validate Hash Correctly

<Accordion title="Hash Generation Checklist" icon="fa-list">
  * Generate request hashes only on your backend.
  * Use the exact values that will be posted to PayU.
  * Preserve pipe delimiters for blank fields.
  * Keep test and production keys/salts separate.
  * Never send salt to frontend, mobile apps, URLs, logs, or analytics tools.
  * Validate PayU response hash before updating order status.
</Accordion>

<Callout icon="🚧" theme="warn">
  **Watch Out!**

  Hashing `10.00` and posting `10` causes hash validation failure because hashes are generated from strings, not numeric values.
</Callout>

### PayU Hash Generator

<HTMLBlock>{`
			<p>Use this tool to generate the hash by providing the mandatory parameter values depending on the selected logic.</p><br/>
								<style>
                .tooltip-btn {
                    position: relative;
                    background-color: #4CAF50;
                    color: white;
                    padding: 10px 20px;
                    border: none;
                    border-radius: 5px;
                    cursor: pointer;
                    font-weight: bold; /* Added this line */
                }
                .tooltip-btn:hover::after {
                    content: attr(data-tooltip);
                    position: absolute;
                    bottom: 125%;
                    left: 50%;
                    transform: translateX(-50%);
                    background-color: #333;
                    color: white;
                    padding: 5px 10px;
                    border-radius: 4px;
                    white-space: nowrap;
                    font-size: 12px;
                    z-index: 1;
                }
                </style>

                <button onclick="window.open('https://payu-india.github.io/CMS-Chatbot/', '_blank')" 
                        class="tooltip-btn" 
                        data-tooltip="Click to generate hash.">
                    Generate Hash
                </button>
`}</HTMLBlock>

## Separate Frontend and Backend Responsibilities

<Accordion title="Responsibilities" icon="fa-table">

| Responsibility             | Frontend                           | Backend                                |
| -------------------------- | ---------------------------------- | -------------------------------------- |
| Collect customer input     | Yes                                | Optional                               |
| Validate basic form fields | Yes                                | Yes                                    |
| Generate `txnid`           | No                                 | Yes                                    |
| Generate request hash      | No                                 | Yes                                    |
| Store order attempt        | No                                 | Yes                                    |
| Submit to PayU             | Yes, for Hosted Checkout form post | Yes, for S2S and server-mediated flows |
| Verify response hash       | No                                 | Yes                                    |
| Decide final order status  | No                                 | Yes                                    |
| Process webhook            | No                                 | Yes                                    |

</Accordion>

## Handle Retries and Idempotency

<Accordion title="Retries and Idempotency List" icon="fa-list">
  * Use a unique `txnid` for every new payment attempt.
  * Keep a stable merchant order ID in your system and map multiple PayU attempts to it.
  * Do not retry a pending transaction blindly.
  * Before creating a new attempt, check whether the previous attempt succeeded, failed, or is still pending.
  * Make webhook processing idempotent with a unique key such as `mihpayid` + `txnid` + final status.
  * Protect the checkout button from double-click submissions.
  * Do not create duplicate fulfillment on duplicate redirects or duplicate webhooks.
</Accordion>

## Build Clear Status Handling

Recommended merchant-side states:

<Accordion title="Status Handling" icon="fa-table">

| Merchant state      | PayU status / error type                   | Recommended fix                                                          |
| ------------------- | ------------------------------------------ | ------------------------------------------------------------------------ |
| `payment_initiated` | Request created                            | Await redirect, webhook, or status API update before fulfillment.        |
| `payment_pending`   | `status=pending` or `E227`                 | Do not fulfill. Poll/reconcile and wait for webhook/status confirmation. |
| `payment_success`   | `status=success` and hash valid            | Fulfill order after matching `txnid`, `amount`, and response hash.       |
| `payment_failed`    | `status=failure` and final status verified | Show retry options and create a new `txnid` for a new attempt.           |
| `payment_dropped`   | `E231`, timeout, abandoned flow            | Verify final status before retrying or closing the order.                |
| `payment_review`    | Conflicting redirect/webhook/status        | Hold fulfillment and reconcile using Transaction Detail APIs.            |

</Accordion>

## Webhook Handler Checklist

Follow these webhook handler checklist:

<Accordion title="Webhook Handler Checklist" icon="fa-list">
  * Accept `POST`.
  * Accept form data and `application/x-www-form-urlencoded`.
  * Allow PayU webhook IPs.
  * Verify response hash.
  * Persist payload before processing.
  * Return `2xx` after durable receipt.
  * Process fulfillment asynchronously.
  * Make all state updates idempotent.
</Accordion>

## Recurring Payments and SI Checklist

Below are the recurring payments and SI checklist

<Accordion title="Recurring and SI Checklist" icon="fa-list">
  * Validate mandate start and end dates before sending request.
  * Prevent duplicate debit requests for the same mandate cycle.
  * Store `authpayuid` or `authPayuId` against the customer mandate.
  * Reconcile all recurring debits through webhook/status APIs.
  * Treat mandate setup pending states separately from payment pending states.
</Accordion>
