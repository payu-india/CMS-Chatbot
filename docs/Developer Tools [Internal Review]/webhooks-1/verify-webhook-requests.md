---
title: Verify Webhook Requests
excerpt: >-
  Confirm a webhook genuinely came from PayU and was not tampered with before
  you act on it.
deprecated: false
hidden: true
metadata:
  robots: index
---
Anyone on the internet can send an HTTP POST to your webhook URL. Verifying it is how you prove that the request is from PayU and authentic. We recommend not to mark any order paid, issue a refund, or update a subscription without verifying the webhook.

<Callout icon="far fa-folder-closed" theme="warn">
  ### **Configure and Manage Webhooks**

  For creating and configuring webhook endpoints, see [Set Up & Configure Webhooks](doc:create-and-manage-webhooks). For the full list of events and their fields, see [Webhook Events Reference](doc:events-and-payloads). For delivery problems unrelated to verification (e.g. PayU cannot reach your URL), see [Test & Troubleshoot Webhooks](doc:using-webhook-logs).
</Callout>

***

## Which Verification Method Applies to Your Webhook

PayU does not use a single verification scheme for all webhooks. The method depends on the event family:

| Webhook family                           | Verification method            | Where the proof lives                                                             |
| ---------------------------------------- | ------------------------------ | --------------------------------------------------------------------------------- |
| Payment (`Successful`, `Failed`), Refund | **Reverse hash** (SHA-512)     | `hash` field in the payload body                                                  |
| Dispute / Chargeback                     | **Signature header** (SHA-512) | `X-PayU-Dispute-Webhook-Signature-V2` **HTTP header** (optional, must be enabled) |

***

## Reverse-hash Verification

Payment and refund webhooks carry a `hash` field in the body. PayU computes this hash from the same transaction parameters you originally sent, concatenated **in reverse order** with your merchant salt, using SHA-512. You recompute the same hash locally and compare. If the two match, the payload is authentic and unmodified.

<Accordion title="Reverse-hash Formula" icon="far fa-rotate-reverse">
  ```
  sha512(SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  <Callout icon="far fa-arrow-up-right-and-arrow-down-left-from-center" theme="info">
    ### **Hash Parameters**

    The string always contains exactly five UDF positions between `status` and `email` parameters (the six empty pipes accommodate additional response fields). Use an empty string even if you do not pass any UDF parameters. Never drop a pipe. Refer to the parameter description for more parameter description.
  </Callout>
</Accordion>

Some integrations change the hash formula order. Here is the complete list:

<Tabs>
  <Tab title="Standard Integration">
    **Products:**

    - PayU Hosted Checkout

    **Hash Formula**

    ```text Formula
    SALT|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key
    ```
  </Tab>

  <Tab title="With Additional Charges">
    **Products:**

    ```text Hash Formula
    additional_charges|SALT|status||||||udf5|…|key
    ```
  </Tab>

  <Tab title="With Split Payments">
    **Products:**

    ```text Hash Formula
    SALT|status|splitInfo||||||udf5|…|key
    ```
  </Tab>

  <Tab title="Split Settlements + Additional Charges">
    **Products:**

    ```text Hash Formula
    additional_charges|SALT|status|splitInfo||||||udf5|…|key
    ```
  </Tab>
</Tabs>

<Accordion title="Reverse-hash Formula in Different Language Bindings" icon="far fa-code">
  ```javascript
  // Node.js — reverse-hash verification for a payment/refund webhook
  const crypto = require("crypto");

  function isValidPayuWebhook(body, salt) {
    const udf = (n) => body[`udf${n}`] || "";
    const reverseString = [
      salt, body.status, "", "", "", "", "",
      udf(5), udf(4), udf(3), udf(2), udf(1),
      body.email || "", body.firstname || "", body.productinfo || "",
      body.amount, body.txnid, body.key,
    ].join("|");

    const computed = crypto.createHash("sha512").update(reverseString, "utf8").digest("hex");
    // constant-time comparison
    const a = Buffer.from(computed);
    const b = Buffer.from((body.hash || "").toLowerCase());
    return a.length === b.length && crypto.timingSafeEqual(a, b);
  }
  ```
  ```python
  # Python — reverse-hash verification for a payment/refund webhook
  import hashlib, hmac

  def is_valid_payu_webhook(body: dict, salt: str) -> bool:
      udf = lambda n: body.get(f"udf{n}", "") or ""
      parts = [
          salt, body.get("status", ""), "", "", "", "", "",
          udf(5), udf(4), udf(3), udf(2), udf(1),
          body.get("email", ""), body.get("firstname", ""), body.get("productinfo", ""),
          body.get("amount", ""), body.get("txnid", ""), body.get("key", ""),
      ]
      computed = hashlib.sha512("|".join(parts).encode("utf-8")).hexdigest()
      return hmac.compare_digest(computed, (body.get("hash", "") or "").lower())
  ```
  ```php
  <?php
  // PHP — reverse-hash verification for a payment/refund webhook
  function is_valid_payu_webhook(array $body, string $salt): bool {
      $udf = fn($n) => $body["udf$n"] ?? "";
      $parts = [
          $salt, $body["status"] ?? "", "", "", "", "", "",
          $udf(5), $udf(4), $udf(3), $udf(2), $udf(1),
          $body["email"] ?? "", $body["firstname"] ?? "", $body["productinfo"] ?? "",
          $body["amount"] ?? "", $body["txnid"] ?? "", $body["key"] ?? "",
      ];
      $computed = hash("sha512", implode("|", $parts));
      return hash_equals($computed, strtolower($body["hash"] ?? ""));
  }
  ```
</Accordion>

<Accordion title="Reverse Hashing Steps" icon="far fa-list-ol">
  1. Extract th&#x65;**&#x20;**`hash`**&#x20;**&#x66;ield PayU sent in the payload.
  2. Build the reverse-hash string using the above mentioned formula. Use `""` for any unused UDF and keep every pipe.
  3. Compute SHA-512 over the UTF-8 string.
  4. Compare your computed digest to the `hash` from the payload. If they are equal, the webhook is authentic.
</Accordion>

<Callout icon="📘" theme="info">
  ### PayU SDK Github Resource for Hashing:

  The PayU Node SDK exposes a Hash API that performs reverse hashing for you. See the [PayU node SDK README](https://github.com/payu-india/payu-sdk-node/blob/main/README.md).
</Callout>

### Reverse-hash Verification Tool

<br />

Before wiring this into code, you can confirm a single payload using the PayU's [Hash Verification Tool](doc:using-payu-hash-verification-tool)

<br />

Paste the callback body, parse the fields, enter your salt, and compare th&#x65;**&#x20;Calculated Hash** against the **Response Hash**. This is the fastest way to tell whether a mismatch is a data problem or a code problem.

***

## Dispute signature verification

Dispute (chargeback) webhooks can carry cryptographic signatures in HTTP **headers** rather than a hash in the body. This is a **different mechanism** from reverse hashing — do not apply the reverse-hash logic above to dispute webhooks.

<Callout icon="📘" theme="info">
  ### Signing is opt-in

  Signed dispute webhooks are **not enabled by default**. If the signature headers are absent, the webhook is not necessarily invalid — signing may simply not be turned on for your account. To enable it, contact your PayU Key Account Manager (KAM) or [PayU Support](https://help.payu.in).
</Callout>

### Headers

| Header                                       | Meaning                                                 |
| -------------------------------------------- | ------------------------------------------------------- |
| `X-PayU-Dispute-Webhook-Signature-V1`        | SHA-512 digest, version 1                               |
| `X-PayU-Dispute-Webhook-Signature-V2`        | SHA-512 digest, version 2 — **verify against this one** |
| `X-PayU-Dispute-Webhook-Signature-Algorithm` | `SHA512`                                                |

### The signed string

PayU builds one UTF-8 string, pipe-delimited, with no leading or trailing pipe, hashes it with SHA-512, and sends the lowercase-hex digest in the headers:

```
<merchantKey>|<txn_id>|<cb_amount>|<cb_id>|<cb_type>|<cb_status>|<merchantSalt>
```

- Only these six values plus the salt participate — other body fields (`type`, `event`, `mid`, `reason_code`, …) do not.
- `merchantSalt` is always the **last** segment.
- `cb_status` may be a **mapped** value at signing time. In PayU's worked example the body contains `"cb_status":"Pending Response"` but the signed string uses `PendingResponse` (spaces removed). If verification fails on the raw JSON value, apply PayU's signing-time mapping or confirm it with support.

### Steps

1. Read the **raw** body bytes and parse JSON from that buffer — do not re-serialize the body to build the signed string.
2. Take `txn_id`, `cb_amount`, `cb_id`, `cb_type` as they appear; resolve `cb_status` to its signed form.
3. Concatenate: `merchantKey|txn_id|cb_amount|cb_id|cb_type|cb_status|merchantSalt`.
4. Compute SHA-512 over the UTF-8 string, lowercase hex.
5. Compare to `X-PayU-Dispute-Webhook-Signature-V2` using a **constant-time** comparison (`hmac.compare_digest` in Python, `crypto.timingSafeEqual` on equal-length buffers in Node.js). Match → accept; otherwise reject.

### Aggregator (child) merchants

If you are an aggregator, dispute webhooks for a child merchant are signed with the **parent aggregator's** merchant key (first segment) and the parent's `merchantSalt` (last segment) — not the child's. Build the string with the parent's credentials.

### Quick reference

- **Algorithm:** SHA-512, lowercase hex
- **Header to verify:** `X-PayU-Dispute-Webhook-Signature-V2`
- **Delimiter:** `|`
- **Order:** `merchantKey` → `txn_id` → `cb_amount` → `cb_id` → `cb_type` → `cb_status` → `merchantSalt` (last)

***

## IP allowlisting (secondary hardening)

IP allowlisting is a **defense-in-depth** measure, not a replacement for hash/signature verification. Its main purpose: if your webhook URL sits behind a firewall, allowlist PayU's source IPs so deliveries are not blocked. It also lets you drop traffic from unexpected sources early.

Treat IPs as **subject to change** and always keep hash/signature verification as your primary control.

<Callout icon="🚧" theme="warn">
  ### The published IP lists are inconsistent across the current docs

  Different existing pages label the same addresses (for example the `3.7.89.x` range) as **Test** on one page and **Production** on another, and the payout IP set differs again. Because an incorrect allowlist can silently drop live webhooks, this page intentionally does **not** reproduce a single list. Confirm the current, authoritative IP set with PayU before allowlisting, and see _Gaps / Needs Validation_ in the accompanying audit notes. The canonical list should live on [Set Up & Configure Webhooks](doc:create-and-manage-webhooks) once reconciled.
</Callout>

***

## Verification is failing — common causes

Work down this list; these account for most mismatches.

1. **Wrong or swapped key/salt.** The single most common cause of hash mismatch is an incorrect merchant key — for example inserting the MID instead of the merchant **key**, or swapping **key** and **salt** positions in the string. Double-check both, and that you are using the credentials for the correct environment (Test vs Production).
2. **Body mutated before hashing.** A framework or middleware that JSON-parses and re-serializes (re-ordering keys, changing number/string formatting, trimming whitespace) will change the bytes you hash. Capture the **raw** body and hash that, before any parsing layer touches it.
3. **Missing or misplaced pipes / UDFs.** The reverse-hash string must keep **exactly five UDF positions** and all delimiters, even when UDFs are empty. Dropping a pipe or omitting an empty UDF shifts every field and breaks the hash.
4. **Encoding issues.** Hash over the **UTF-8** bytes. For payment/refund webhooks delivered as `application/x-www-form-urlencoded`, URL-decode values before building the string; mismatched decoding (or double-decoding) changes the input.
5. **Case or field mismatch on the digest.** Compare against a **lowercase hex** digest. Compare the computed value to the exact `hash`/signature PayU sent.
6. **Dispute&#x20;**`cb_status`**&#x20;mapping.** For dispute signatures, the signed `cb_status` may differ from the raw JSON value (e.g. `Pending Response` → `PendingResponse`). Apply the signing-time mapping.
7. **Applying the wrong method.** Reverse hashing is for payment/refund webhooks (hash in body); signature-header verification is for dispute webhooks (header). Using one scheme on the other family will always fail.

<Callout icon="🚧" theme="warn">
  ### Not all "verification" advice in older docs is correct

  A generic HMAC-SHA256 sample appears on the OverWatch monitoring-alerts page. That is **not** the scheme PayU uses for payment or dispute webhooks — use the reverse-hash and dispute-signature methods on this page. (Flagged for cleanup; see the duplicate-content list in the audit notes.)
</Callout>

If the request is genuinely reaching you but you still cannot make the hash match, verify one payload by hand with the [Hash Verification Tool](doc:using-payu-hash-verification-tool). If webhooks are **not arriving at all**, that is a delivery problem, not a verification problem — see [Test & Troubleshoot Webhooks](doc:using-webhook-logs).

## After verification

Once a webhook is verified, hand it to your handler for parsing, acknowledgment, idempotency, and processing. Continue to [Handle Webhook Events](doc:events-and-payloads).
