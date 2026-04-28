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

## Sample request

```bash
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

## Sample response

```json
{
  "status": "failure",
  "error": "E700",
  "error_Message": "Validation of secure hash failed",
  "unmappedstatus": "failed",
  "txnid": "txn_10001"
}
```

## Root cause

The hash was not generated from the exact values submitted to PayU.

Common mistakes:

* Using Merchant ID instead of merchant key.
* Using key in place of salt or salt in place of key.
* Missing pipe delimiters for blank `udf1` to `udf5`.
* Generating hash before formatting `amount`, then posting a different value.
* Trimming, encoding, lowercasing, or changing `productinfo`, `firstname`, or `email` after hash generation.
* Using test key with production salt or production key with test salt.
* Generating hash on frontend and exposing salt.

## Debugging guide

1. Log the raw server-side hash string before hashing. Do not log salt in shared logs.

2. Confirm the sequence:

   ```text
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

> **Common Mistake**
>
> `10`, `10.0`, and `10.00` are different strings for hash generation. If you hash `10.00`, post `10.00`.

## Fix checklist

| Check                     | Expected result                                                                           |
| ------------------------- | ----------------------------------------------------------------------------------------- |
| Hash generated on backend | Salt never leaves backend systems.                                                        |
| Exact request values used | Values in hash string match posted values byte-for-byte.                                  |
| Empty fields preserved    | Blank UDF positions remain in the hash string.                                            |
| Environment matches       | Test key/salt only with test endpoint; production key/salt only with production endpoint. |
| Response hash verified    | Order status is updated only after reverse hash validation.                               |

## Related docs

* [Generate Hash for PayU Hosted Checkout](doc:generate-hash-payu-hosted)
* [Generate Hash for Merchant Hosted Checkout](doc:generate-hash-merchant-hosted)
* [Hashing Request and Response for S2S](doc:hashing-request-and-response)
