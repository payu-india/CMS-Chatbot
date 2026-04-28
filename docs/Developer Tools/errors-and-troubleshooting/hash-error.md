---
title: Invalid Hash Error
excerpt: >-
  Debug and fix PayU invalid hash, hash mismatch, and secure hash validation
  errors.
deprecated: false
hidden: true
metadata:
  description: Debug and fix PayU hash mismatch and secure hash validation errors.
  robots: index
---
Invalid hash errors occur during request validation when PayU receives a `hash` that does not match the hash PayU calculates from the submitted fields.

## When it occurs

<Accordion title="Error Causes" icon="fa-info-circle">
  * Hosted Checkout page shows a hash mismatch or transaction dropped message.
  * Payment request fails before bank redirection.
  * Error code is `E700`.
  * Error description is `SECURE_HASH_FAILURE`.
  * Message is `Validation of secure hash failed`.
</Accordion>

### Example

Here is an example HTML code that generates a hash error. 

<Accordion title="Sample Request" icon="fa-code">
  ```html
  curl -X POST "https://test.payu.in/_payment" \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "key=gtKFFx" \
    -d "txnid=txn_10001" \
    -d "amount=10.00" \
    -d "productinfo=Test Product" \
    -d "firstname=John" \
    -d "email=john@example.com" \
    -d "phone=9999999999" \
    -d "surl=https://example.com/payu/success" \
    -d "furl=https://example.com/payu/failure" \
    -d "hash=bad_hash_value"
  ```
</Accordion>

<Accordion title="Sample Response" icon="fa-code">
  ```json
  {
    "status": "failure",
    "error": "E700",
    "error_Message": "Validation of secure hash failed",
    "unmappedstatus": "failed",
    "txnid": "txn_10001"
  }
  ```
</Accordion>

## Root cause

Lets find the root cause of this error.  Hash was not generated from the exact values submitted to PayU.

<Accordion title="Common Mistakes" icon="fa-warn">
  * Using Merchant ID instead of merchant key.
  * Using key in place of salt or salt in place of key.
  * Missing pipe delimiters for blank `udf1` to `udf5`.
  * Generating hash before formatting `amount`, then posting a different value.
  * Trimming, encoding, lowercasing, or changing `productinfo`, `firstname`, or `email` after hash generation.
  * Using test key with production salt or production key with test salt.
  * Generating hash on frontend and exposing salt.
</Accordion>

## Troubleshooting

Now we know the root cause of the error. Let us see how to troubleshoot the error.

<Accordion title="Troubleshooting Steps" icon="fa-info-circle">
  1. Log the raw server-side hash string before hashing. Do not log salt in shared logs.
  2. Confirm the sequence:

  ```Text Logic
  key|txnid|amount|productinfo|firstname|email|udf1|udf2|udf3|udf4|udf5||||||SALT
  ```

  3. Confirm the posted values exactly match the values in the hash string.
  4. Confirm blank UDF fields are represented by empty positions, not removed.
  5. Confirm the correct environment:
     * Test: test key + test salt + test endpoint.
     * Production: production key + production salt + production endpoint.
  6. Generate SHA-512 in lowercase hexadecimal.
  7. Move hash generation to backend if it is currently generated in browser/mobile code.
  8. Validate response hash before updating order status.
</Accordion>

## PayU Hash Generator

<HTMLBlock>{`
			<p>You can use this tool to generate hash value by providing the mandatory parameter values depending on the logic.</p><br/>
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

<Callout icon="❗️" theme="error">
  **Common Mistakes**

  `10`, `10.0`, and `10.00` are different strings for hash generation. If you hash `10.00`, post `10.00`.
</Callout>

## Fix Checklist

Follow this checklist while fixing the hash error.

<Accordion title="Checklist" icon="fa-list">
  | Check                     | Expected result                                                                           |
  | ------------------------- | ----------------------------------------------------------------------------------------- |
  | Hash generated on backend | Salt never leaves backend systems.                                                        |
  | Exact request values used | Values in hash string match posted values byte-for-byte.                                  |
  | Empty fields preserved    | Blank UDF positions remain in the hash string.                                            |
  | Environment matches       | Test key/salt only with test endpoint; production key/salt only with production endpoint. |
  | Response hash verified    | Order status is updated only after reverse hash validation.                               |
</Accordion>

## Related docs

* [Generate Hash for PayU Hosted Checkout](doc:generate-hash-payu-hosted)
* [Generate Hash for Merchant Hosted Checkout](doc:generate-hash-merchant-hosted)
* [Hashing Request and Response for S2S](doc:hashing-request-and-response)
