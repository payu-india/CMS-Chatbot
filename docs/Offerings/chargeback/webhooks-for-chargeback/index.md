---
title: Webhooks for Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
Chargeback webhooks provide real-time notifications about important chargeback events, allowing merchants to stay updated and take necessary actions promptly. Webhooks are sent for the following events:

* A new chargeback is created
* Chargeback status is changed
* Chargeback amount is changed

To create webhooks using Dashboard, refer to <Anchor label="Configure Chargeback Webhook" target="_blank" href="https://docs.payu.in/docs/create-a-chargeback-webhook">Configure Chargeback Webhook</Anchor> > <Anchor label="Using Dashboard" target="_blank" href="https://docs.payu.in/docs/create-a-chargeback-webhook#using-dashboard">Using Dashboard</Anchor>. To update or delete an existing webhook, refer to any of the following:

* <Anchor label="Create a New Webhook" target="_blank" href="doc:create-a-new-webhook">Create a New Webhook</Anchor>
* <Anchor label="Update a Webhook" target="_blank" href="https://docs.payu.in/docs/update-a-webhook">Update a Webhook</Anchor>
* <Anchor label="Delete a Webhook" target="_blank" href="https://docs.payu.in/docs/delete-a-webhook-on-dashboard">Delete a Webhook</Anchor>

## Understanding payload

When a chargeback event occurs, PayU will send a POST request to your configured URL with a JSON payload similar to the following:

```json
{
  "type": "payments",
  "event": "dispute",
  "reason_code": "Fraud - Card Present Environment",
  "created_at": "2025-01-15T21:28:25.000+05:30",
  "updated_at": "2025-05-27T22:08:16.000+05:30",
  "mid": "2",
  "cb_id": 1761758,
  "txn_id": "999000000000468",
  "cb_type": "RBI/BO",
  "due_date": "2025-03-31",
  "cb_amount": "1.0",
  "cb_status": "Bank Comm Sent"
}
```

### Fields in the payload

| Field       | Description                                                                                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type        | Type of transaction  and merchant must include the value as **payments** only.                                                                                                                                   |
| event       | Event type and the merchant must the include the value as **dispute** only.                                                                                                                                      |
| reason_code | Reason for the chargeback. For the list of reason codes, refer to [Reason codes for chargebacks](https://docs.payu.in/docs/webhooks-for-chargeback#reason-codes-for-chargebacks).                                |
| created_at  | Timestamp when the chargeback was created                                                                                                                                                                        |
| updated_at  | Timestamp when the chargeback was last updated                                                                                                                                                                   |
| mid         | PayU Merchant ID                                                                                                                                                                                                 |
| cb_id       | Chargeback ID                                                                                                                                                                                                    |
| txn_id      | This is the PayU transaction ID that is associated with the chargeback.                                                                                                                                          |
| cb_type     | Type of chargeback (for example, "RBI/BO", that is, Reserve Bank of India/Banking Operations)                                                                                                                    |
| due_date    | Due date for the chargeback resolution                                                                                                                                                                           |
| cb_amount   | Amount involved in the chargeback                                                                                                                                                                                |
| cb_status   | Current status of the chargeback. For the possible chargeback status values, refer to [cb_status field values description](https://docs.payu.in/docs/webhooks-for-chargeback#cb_status-field-values-description) |

### cb_status field values description

The `cb_status` or chargeback status field can have the following values:

| Chargeback Status            | Description                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New                          | It indicates that a new chargeback has been initiated by the customer basis the chargeback reason.                                                                                                                                                                                                                     |
| Pending Response             | It indicates that the chargeback is awaiting merchant response, that is, to accept, partially accept or decline with evidence.                                                                                                                                                                                         |
| Pending Doc Review           | It indicates that merchant has submitted their response, and the response are being reviewed by the PayU Chargeback team.                                                                                                                                                                                              |
| Submitted to Bank            | It indicates that the PayU Chargeback team has completed their review and forwarded the evidence to the bank for representment.                                                                                                                                                                                        |
| Insufficient Document        | It indicates that the PayU Chargeback team has reviewed the evidence documents and is requesting the merchant for additional documents for representment or the correct document based on the Chargeback team's comment.                                                                                               |
| Closed Customer Favour       | It indicates that that the chargeback has been closed in the customer's favour. The merchant will lose the chargeback amount to the customer.                                                                                                                                                                          |
| Closed in Merchant Favour    | It indicates that the chargeback has been closed in the merchant's favour. The chargeback amount will be reversed back to the merchant account.                                                                                                                                                                        |
| Closed under Fraud Liability | It indicates that the chargeback has been closed since the transaction has been identified as fraudulent. Moreover, PayU will cover the chargeback amount under the fraud liability program so the chargeback amount will be reversed back to the merchant account or will not be debited from the merchant's account. |

<Callout icon="📘" theme="info">
  **Chargeback reasons**: For chargeback reasons provided by customers while raising chargeback, refer to [Chargeback Reasons](doc:chargeback-reasons).
</Callout>

## Troubleshooting

If you're not receiving webhook notifications:

* Verify that your webhook URL is correct and accessible from the internet
* Check that your endpoint returns a 200 OK response to acknowledge receipt of the webhook
* Ensure your webhook is set to "Active" in the configuration
* Contact PayU support if you continue to experience issues

## FAQs

#### On new status dispute, is the amount already booked from merchant account?  OR **When is the amount charged from the merchant account?** OR **Does Closed Customer Favour mean the amount is debited from merchant account?**

Dependent on the merchant risk score & contract, Merchant accounts are marked as Upfront-Debit or No-Upfront-Debit. So when a new dispute is raised:

* For upfront-debit, the dispute amount will be debited when the dispute (in new Status) is created.
* For no-upfront-debit, the dispute amount will be debited only after the dispute is closed in the customer's favor.

#### Do Closed in Merchant Favour / Closed under Fraud Liability mean the amount is reversed to merchant account?

If the amount is upfront debit merchant then the money will be reversed. Else there is no debit on the merchant account.
## Signature on Webhook Header

PayU can optionally send cryptographic signatures on dispute (chargeback) webhooks so you can confirm the request came from PayU and that the signed fields were not altered in transit. The request body remains JSON; signatures are delivered in HTTP headers.

**Enabling signed webhooks:** Signing is not on by default for every account. If signature headers are missing, the webhook may still be valid—signing simply is not enabled. To enable signed dispute webhooks, contact your PayU Key Account Manager (KAM) or contact <Anchor label="PayU Support" target="_blank" href="https://help.payu.in">PayU Support</Anchor>.

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

### Sample Payload with Signature

```json
HTTP/1.1 200 OK
Content-Type: application/json
x-payu-dispute-webhook-signature-algorithm: SHA512
x-payu-dispute-webhook-signature-v2: 14221c99eab16d43512461dfee4ac102cb0a9d358a723aaa824147537bdf7de712c3a639950b74f50194525ae206ddc70f1dbd4382060d224a2e217d39bec
x-payu-dispute-webhook-signature-v1: 14221c99eab16d43512461dfee4ac102cb0a9d358a723aaa824147537bdf7de712c3a639950b74f50194525ae206ddc70f1dbd4382060d224a2e2b1d39bec

 
{
  "type": "payments",
  "event": "dispute",
  "created_at": "2025-12-16T16:00:56.000+05:30",
  "updated_at": "2026-05-06T15:34:57.000+05:30",
  "mid": "8235901",
  "cb_id": 2042053,
  "txn_id": "26431197092",
  "cb_type": "Arbitration",
  "due_date": "2026-03-05",
  "cb_amount": "2.0",
  "cb_status": "Pending Response",
  "reason_code": "Fraud -  Card Present Environment"
}

 
```

<br />
