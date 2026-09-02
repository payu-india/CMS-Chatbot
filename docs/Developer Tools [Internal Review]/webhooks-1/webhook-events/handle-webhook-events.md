---
title: Handle Webhook Events
excerpt: >-
  How to build a reliable PayU webhook handler — acknowledgment behaviour
  and     timeouts, reading the payload envelope, idempotent duplicate handling,
  safe     reprocessing patterns, and multi-merchant routing.
deprecated: false
hidden: true
metadata:
  robots: index
---
Once a webhook is [verified](doc:verify-webhook-requests), your handler has one job: accept it quickly and process its effect exactly once, even if PayU sends it more than once. This page covers how to acknowledge, read the envelope, de-duplicate, and process safely.

This page assumes the request is already verified — do not process an unverified webhook. For verification, see [Verify Webhook Requests](doc:verify-webhook-requests). For the full field-by-field payload catalog, see [Webhook Events Reference](doc:events-and-payloads). For why deliveries fail or how PayU retries at the network level, see [Test & Troubleshoot Webhooks](doc:using-webhook-logs).

## The handler contract

A robust handler follows the same shape regardless of event type:

1. **Read the raw body** (you need it for verification anyway).
2. **Verify** authenticity — see [Verify Webhook Requests](doc:verify-webhook-requests).
3. **Identify** the event and its transaction from the payload.
4. **De-duplicate** — if you've already processed this event, acknowledge and stop.
5. **Acknowledge** with `200 OK` promptly.
6. **Process** the business effect, ideally asynchronously, exactly once.

The ordering of steps 4–6 matters and depends on how fast your processing is; see [Acknowledge fast, process reliably](#acknowledge-fast-process-reliably).

## Acknowledge with 200 OK

PayU treats a webhook as delivered only when your endpoint returns HTTP **200 OK**. Any non-200 response (or a timeout) is treated as a failure and PayU retries the delivery. The response body can be empty or a short acknowledgment — PayU does not parse it.

**Timeout and retry behaviour is product-specific.** Use the value for the webhook family you are integrating:

| Webhook family              | Acknowledge within                    | Retry behaviour on non-200 / timeout                                    |
| --------------------------- | ------------------------------------- | ----------------------------------------------------------------------- |
| Payment / Refund            | Return `200 OK`                       | PayU retries up to **3 times** before flagging the webhook as timed out |
| Payouts                     | Return `200 OK` within **10 seconds** | Retried a maximum of **2 more times**                                   |
| OverWatch monitoring alerts | Respond within **5 seconds**          | Retried on a schedule: immediate, +1 min, +5 min, +15 min               |

<Callout icon="📘" theme="info">
  ### These windows come from separate product pages

  The payments page states "retry 3 times" without an explicit time limit; the payouts page specifies 10 seconds; OverWatch specifies 5 seconds. There is no single repo-wide timeout value. Design your handler to acknowledge in **well under the tightest window that applies to you** (treat a few seconds as the practical ceiling), and confirm the exact SLA for your product with PayU if it is business-critical.
</Callout>

Because retries exist, your handler **must** be idempotent — the same event can legitimately arrive more than once. See [Handle duplicate deliveries idempotently](#handle-duplicate-deliveries-idempotently).

## Acknowledge fast, process reliably

If your processing (updating an order, calling downstream services, sending email) can exceed the acknowledgment window, do not do it inline before responding. Instead:

1. Verify the webhook.
2. Record it durably (e.g. enqueue it or write it to a "received events" table) — keyed for de-duplication (below).
3. Return `200 OK` immediately.
4. Process asynchronously from the queue/table with your own retry and error handling.

This decouples PayU's delivery SLA from your processing time and stops slow downstream work from triggering unnecessary PayU retries. If you can reliably finish processing inside the window, synchronous processing before the `200 OK` is also fine — the key requirement is that you never miss the acknowledgment deadline.

## Read the payload envelope

You need three things out of every payload before processing: **which event** it is, **which transaction/entity** it concerns, and the **status**. The exact fields differ by webhook family (full catalog in [Webhook Events Reference](doc:events-and-payloads)); the routing-relevant fields are:

| Webhook family      | Event/type field      | Primary transaction key                   | Merchant/account key | Status field        |
| ------------------- | --------------------- | ----------------------------------------- | -------------------- | ------------------- |
| Payment             | (Successful / Failed) | `txnid`, `mihpayid`                       | `key`                | `status`            |
| Refund              | `action`              | `mihpayid`, `request_id`, `merchantTxnId` | `key`                | `status`            |
| Dispute             | `event` / `type`      | `cb_id`, `txn_id`                         | `mid`                | `cb_status`         |
| Payout              | `event`               | `payuRefId`, `merchantReferenceId`        | `payoutMerchantId`   | conveyed by `event` |
| Subscription (Zion) | `notificationType`    | `subscriptionId`, `authRefId`             | `merchantId`         | `status`            |

<Callout icon="🚧" theme="warn">
  ### Payment payload format is documented two ways

  One page shows payment webhooks as **form-urlencoded** (`mihpayid=...&status=...&hash=...`), another wraps them in a **JSON envelope** with an `event_payload` object plus delivery metadata (`request_identifier`, `event_type`, `response_code`, …). Refund, dispute, payout and subscription webhooks are documented as JSON. Read your handler's actual `Content-Type` and parse accordingly rather than assuming one format. This ambiguity is flagged in _Gaps / Needs Validation_.
</Callout>

Keep the full field reference on [Webhook Events Reference](doc:events-and-payloads) — this page only covers the fields you route and de-duplicate on.

## Handle duplicate deliveries idempotently

PayU's own docs are explicit: payment systems are asynchronous and you may receive **duplicate callbacks, repeated webhooks, and retries** for the same event. Your handler must ensure a repeated delivery does not cause a second effect (double fulfillment, double refund, duplicate email).

**PayU does not currently document a single global event UUID** for payment/refund/dispute webhooks. De-duplicate on the transaction identifiers PayU does provide, choosing a key that is unique per event you care about:

| Webhook family | Recommended de-duplication key                                                                                |
| -------------- | ------------------------------------------------------------------------------------------------------------- |
| Payment        | `mihpayid` (PayU payment ID) — or your own unique `txnid`                                                     |
| Refund         | `request_id` / `mihpayid`                                                                                     |
| Dispute        | `cb_id` (chargeback ID), optionally combined with `cb_status` if you must process each status transition once |
| Payout         | `payuRefId`                                                                                                   |
| Subscription   | `authRefId` / `subscriptionId` + `notificationType`                                                           |

<Callout icon="📘" theme="info">
  ### Choosing the key

  If you only need to process each transaction's final outcome once, key on the transaction ID alone. If you need to react to each **status change** of the same entity (common for disputes, which move through several `cb_status` values), include the status in the key so distinct transitions aren't collapsed into one — but a re-delivery of the _same_ transition is still caught.
</Callout>

### Safe reprocessing pattern

Persist processed keys durably (a database table with a unique constraint, not just memory) and check before acting. Use the database's uniqueness guarantee as the source of truth so concurrent duplicate deliveries can't both slip through.

{/* NEW CONTENT — the OverWatch page shows an in-memory is_duplicate() sample; the durable/DB-backed pattern below generalises the repo's documented "use DB uniqueness + idempotency key + duplicate detection" best practice into runnable form. Verify table/column choices against your own schema. */}

```python
# Python — durable idempotency using a unique constraint.
# processed_events(event_key TEXT PRIMARY KEY, processed_at TIMESTAMP)

def handle_webhook(body, headers):
    # 1) assume already verified (see Verify Webhook Requests)
    event_key = body["mihpayid"]           # pick per table above

    # 2) claim the event; unique constraint makes this atomic
    try:
        db.execute(
            "INSERT INTO processed_events (event_key, processed_at) VALUES (%s, NOW())",
            (event_key,),
        )
    except UniqueViolation:
        return 200, ""                     # already processed — ack and stop

    # 3) safe to process exactly once
    process_event(body)                    # ideally enqueue for async work
    return 200, ""
```

```javascript
// Node.js — same pattern; rely on a unique index on event_key.
async function handleWebhook(body /* already verified */) {
  const eventKey = body.mihpayid; // pick per table above
  try {
    await db.query(
      "INSERT INTO processed_events(event_key, processed_at) VALUES ($1, NOW())",
      [eventKey],
    );
  } catch (err) {
    if (err.code === "23505") return { status: 200, body: "" }; // duplicate → ack
    throw err;
  }
  await processEvent(body); // ideally enqueue for async processing
  return { status: 200, body: "" };
}
```

PayU's recommended safeguards, which this pattern implements, are: enforce **database uniqueness**, drive fulfillment through an **order state machine**, use **idempotency keys**, and perform **duplicate detection** before processing. Always keep [reverse-hash / signature verification](doc:verify-webhook-requests) as the gate in front of all of this.

## Route by merchant (aggregators and multi-account setups)

If you receive webhooks for more than one merchant/sub-merchant, route on the account identifier in the payload — `key` for payments, `mid` for disputes, `payoutMerchantId` for payouts, `merchantId` for subscriptions. Load the correct credentials (key/salt) for that account **before** verifying, since verification depends on the right salt.

<Callout icon="🚧" theme="warn">
  ### Aggregator verification has one confirmed special case

  The only multi-merchant verification rule confirmed in the repo is for **dispute** webhooks: child-merchant dispute signatures are signed with the **parent aggregator's** key and salt (see [Verify Webhook Requests](doc:verify-webhook-requests#aggregator-child-merchants)). Whether payment/refund reverse-hash verification for a child merchant uses the child's or the parent's salt is **not documented** — confirm with PayU before relying on either. Flagged in _Gaps / Needs Validation_.
</Callout>

## Event ordering

<Callout icon="🚧" theme="warn">
  ### Delivery ordering is not documented

  The repo does **not** state whether PayU delivers webhooks in the order events occurred, and asynchronous retries make out-of-order arrival possible in principle. **Do not assume ordered delivery.** Make each handler decide from the payload's own status rather than from the sequence of arrivals — for example, drive state through an **order/dispute state machine** that ignores backward transitions (a late "created" after a "success" should not overwrite the newer state). Treat the authoritative status as whatever a server-side status query returns when in doubt. This gap is listed in _Gaps / Needs Validation_.
</Callout>

## Handler checklist

- Return `200 OK` well within the tightest applicable timeout; move slow work off the request path.
- Verify before processing; never trust an unverified payload.
- De-duplicate on a durable, uniquely-constrained key — expect retries and repeats.
- Don't assume event ordering; decide state from the payload, guarded by a state machine.
- Route to the right merchant credentials before verifying in multi-account setups.
- For fields and full examples, use [Webhook Events Reference](doc:events-and-payloads); for delivery failures, use [Test & Troubleshoot Webhooks](doc:using-webhook-logs).
