---
title: '[Review]Authenticating the webhook signature - Chargeback'
deprecated: false
hidden: true
metadata:
  robots: index
---
PayU can optionally send cryptographic signatures on dispute (chargeback) webhooks so you can confirm the request came from PayU and that the signed fields were not altered in transit. The request body remains JSON; signatures are delivered in HTTP headers.

**Enabling signed webhooks:** Signing is not on by default for every account. If signature headers are missing, the webhook may still be valid—signing simply is not enabled. To enable signed dispute webhooks, contact your PayU Key Account Manager.

### Headers

When signing is enabled, each POST includes these headers in addition to the usual ones:

| Header                                       | Description               |
| -------------------------------------------- | ------------------------- |
| `X-PayU-Dispute-Webhook-Signature-V1`        | SHA-512 digest, version 1 |
| `X-PayU-Dispute-Webhook-Signature-V2`        | SHA-512 digest, version 2 |
| `X-PayU-Dispute-Webhook-Signature-Algorithm` | `SHA512`                  |

### String that PayU signs

PayU builds a single UTF-8 string, then hashes it with SHA-512 and sends the digest as lowercase hexadecimal in the signature headers.

**Pieces, in order, separated only by the pipe character `|` (no leading or trailing pipe):**

1. **merchantKey** — Your PayU merchant key (same as for PayU API integrations).
2. **txn_id** — PayU transaction ID.
3. **cb_amount** — Chargeback amount.
4. **cb_id** — Chargeback ID.
5. **cb_type** — Chargeback type.
6. **cb_status** — Chargeback status used for signing (PayU may apply a **mapped** value for signing; see below).
7. **merchantSalt** — Your merchant salt (final segment only).

Template:

```text
<merchantKey>|<txn_id>|<cb_amount>|<cb_id>|<cb_type>|<cb_status>|<merchantSalt>
```

**Fields in the JSON vs fields in the signature:** The JSON body can include whatever fields you configured for the webhook (for example `type`, `event`, `mid`, `reason_code`). Only the values above participate in the signed string, in this fixed order.

**Merchant salt at the end:** **`merchantSalt`** is always the **last** segment—append it after `cb_status` with a single `|` before it. There is no trailing pipe after the salt.

**Field values:** Use the same lexical values as in the JSON for `txn_id`, `cb_amount`, `cb_id`, and `cb_type` (for example `cb_amount` as a string like `1500.0`, not a currency-formatted label). For **`cb_status`**, PayU’s merchant guide states the signed value is a mapped form. In PayU’s worked example, the JSON contains `"cb_status":"Pending Response"` while the string that is hashed uses `PendingResponse` (spaces removed for signing). Build the segment PayU uses for your status so it matches the digest; if verification fails while using the raw JSON string, apply PayU’s signing-time mapping for `cb_status` or confirm the mapping with PayU support.

### Verification steps

1. Read the **raw** HTTP body bytes and parse JSON from that buffer (do not re-serialize the body to compute the signature).
2. From the parsed JSON, take `txn_id`, `cb_amount`, `cb_id`, and `cb_type` as they appear in the payload. Resolve **`cb_status`** to the value PayU signs (see above).
3. Concatenate, then append **merchantSalt** as the final segment: `merchantKey + "|" + txn_id + "|" + cb_amount + "|" + cb_id + "|" + cb_type + "|" + cb_status + "|" + merchantSalt`.
4. Compute **SHA-512** over the UTF-8 encoding of that string. Encode the digest as **lowercase hex**.
5. Compare that digest to **`X-PayU-Dispute-Webhook-Signature-V2`** using a **constant-time** comparison (for example `hmac.compare_digest` in Python or `crypto.timingSafeEqual` on equal-length buffers in Node.js). If they match, accept the webhook; otherwise reject it.

### Aggregator (child) merchants

If you are an aggregator with child merchants, dispute webhooks for a child are signed with the **parent aggregator’s merchant key** as the first segment and the parent’s **merchantSalt** appended last. Build the string with the parent’s key and salt, not the child’s.

### Quick reference

* **Algorithm:** SHA-512, lowercase hex.
* **Header to verify:** `X-PayU-Dispute-Webhook-Signature-V2`.
* **Delimiter:** `|` (pipe).
* **Order:** `merchantKey` → `txn_id` → `cb_amount` → `cb_id` → `cb_type` → `cb_status` → append **`merchantSalt`** last.

### Example

Body (abbreviated):

```json
{
  "txn_id": "403993715515239610",
  "cb_amount": "1500.0",
  "cb_id": "987",
  "cb_type": "Chargeback",
  "cb_status": "Pending Response"
}
```

With `merchantKey` `JBZaLc`, `merchantSalt` `awdgfjrfjk`, and the signing-time `cb_status` value `PendingResponse`, the string that is hashed is:

```text
JBZaLc|403993715515239610|1500.0|987|Chargeback|PendingResponse|awdgfjrfjk
```

The values of `X-PayU-Dispute-Webhook-Signature-V1` and `X-PayU-Dispute-Webhook-Signature-V2` are SHA-512 digests of that exact string.
