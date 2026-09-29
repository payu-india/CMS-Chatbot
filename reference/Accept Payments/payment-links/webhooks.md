---
title: Webhooks
excerpt: >-
  Receive real-time payment success, failure, and pending notifications for
  Payment Links transactions — set up your webhook endpoint and verify the
  signature using your client secret.
deprecated: false
hidden: true
metadata:
  robots: index
---
{/* NEW CONTENT */}

<Banner
  isInline={true}
  message="Integration effort: Developer required — server endpoint and hash verification"
  color="#0066CC"
  textColor="#ffffff"
  fontSize="14px"
  fontWeight="bold"
/>

<Callout icon="📘" theme="info">
  Webhooks notify your server the moment a payment status changes — no polling needed. This page covers webhook setup specifically for Payment Links transactions.
</Callout>

***

## Does Payment Links Support Webhooks?

Yes. When a customer pays via a Payment Link, PayU sends a webhook POST to your registered endpoint — exactly as it does for web checkout transactions. The payload format and events are the same; the only difference is **how you verify the hash** (see [Verify the Webhook Signature](#verify-the-webhook-signature) below).

***

## Step 1 — Register Your Webhook Endpoint

1. Log in to the [PayU Dashboard](https://onboarding.payu.in/).
2. Go to **Settings → Webhooks**.
3. Enter your endpoint URL under **Webhook URL** and click **Save**.

<Callout icon="🚧" theme="warning">
  Your endpoint must be publicly accessible over HTTPS. `localhost` and HTTP URLs will not receive webhooks.
</Callout>

If the **Webhooks** option is not visible in your Dashboard, contact your PayU account manager to have it enabled for your merchant account.

***

## Step 2 — Handle Incoming Webhook Events

PayU sends a **POST** request to your endpoint in `application/x-www-form-urlencoded` format.

### Events

| Event            | When it fires                                               |
| ---------------- | ----------------------------------------------------------- |
| `status=success` | Customer completed payment successfully                     |
| `status=failure` | Payment was declined or failed                              |
| `status=pending` | Payment is in an intermediate state (e.g., bank processing) |

<Callout icon="📘" theme="info">
  Always treat `status=success` as the authoritative confirmation. For `pending`, wait for a follow-up webhook or use the [Fetch Payment Links API](doc:api-fetch) to check the current status.
</Callout>

### Key Payload Fields

The webhook body is URL-encoded. These are the most important fields for Payment Links transactions:

| Field                    | Description                                                         |
| ------------------------ | ------------------------------------------------------------------- |
| `status`                 | `success`, `failure`, or `pending`                                  |
| `txnid`                  | The transaction ID passed when the Payment Link was created         |
| `mihpayid`               | PayU's unique transaction reference — use for refunds and inquiries |
| `amount`                 | Original payment amount from the Payment Link                       |
| `productinfo`            | Description from the Payment Link                                   |
| `firstname`, `email`     | Customer details entered at checkout                                |
| `udf1` – `udf5`          | Custom fields set when the Payment Link was created                 |
| `hash`                   | Webhook signature — must be verified before processing              |
| `bank_ref_num`           | Bank reference number (populated on success)                        |
| `error`, `error_Message` | Error code and description (populated on failure)                   |

For the full parameter reference, see [Webhook Events and Sample Payloads](doc:webhook-events-and-sample-payloads).

### Sample Payload (Success)

```text
status=success
&txnid=PL-ORDER-001
&mihpayid=27553369917
&amount=500.00
&productinfo=Premium+Subscription
&firstname=Rahul+Sharma
&email=rahul%40example.com
&phone=9876543210
&udf1=customer-ref-001
&udf2=
&udf3=
&udf4=
&udf5=
&hash=<sha512_hash>
&bank_ref_num=893847123456
&PG_TYPE=UPI-PG
&error=E000
&error_Message=No+Error
```

***

## Step 3 — Verify the Webhook Signature

<Callout icon="🚧" theme="warning">
  **Payment Links uses&#x20;**`client_secret`**&#x20;for hash verification — not your merchant salt.** This is the same `client_secret` used to generate OAuth2 tokens (see [Authentication](doc:api-auth-token)). Using the wrong secret will cause every hash check to fail.
</Callout>

### Hash Formula

Compute the expected hash using the **reverse** of the payment hash formula:

```
sha512(client_secret|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
```

Compare this to the `hash` field in the webhook payload. If they match, the webhook is authentic.

### Code Examples

<Accordion title="Python" icon="fa-code">
  ```python
  import hashlib

  def verify_payment_links_webhook(payload: dict, client_secret: str) -> bool:
      """
      Verify a PayU Payment Links webhook signature.
      payload: dict of URL-decoded webhook fields
      client_secret: your OAuth2 client_secret (not merchant salt)
      """
      hash_string = (
          client_secret + "|" +
          payload.get("status", "") + "||||||" +
          payload.get("udf5", "") + "|" +
          payload.get("udf4", "") + "|" +
          payload.get("udf3", "") + "|" +
          payload.get("udf2", "") + "|" +
          payload.get("udf1", "") + "|" +
          payload.get("email", "") + "|" +
          payload.get("firstname", "") + "|" +
          payload.get("productinfo", "") + "|" +
          payload.get("amount", "") + "|" +
          payload.get("txnid", "") + "|" +
          payload.get("key", "")
      )
      computed_hash = hashlib.sha512(hash_string.encode("utf-8")).hexdigest()
      return computed_hash == payload.get("hash", "")
  ```
</Accordion>

<Accordion title="Node.js" icon="fa-brands fa-node-js">
  ```javascript
  const crypto = require("crypto");

  function verifyPaymentLinksWebhook(payload, clientSecret) {
    // payload: object of URL-decoded webhook fields
    // clientSecret: your OAuth2 client_secret (not merchant salt)
    const hashString = [
      clientSecret,
      payload.status || "",
      "", "", "", "", "",
      payload.udf5 || "",
      payload.udf4 || "",
      payload.udf3 || "",
      payload.udf2 || "",
      payload.udf1 || "",
      payload.email || "",
      payload.firstname || "",
      payload.productinfo || "",
      payload.amount || "",
      payload.txnid || "",
      payload.key || "",
    ].join("|");

    const computedHash = crypto
      .createHash("sha512")
      .update(hashString)
      .digest("hex");

    return computedHash === payload.hash;
  }
  ```
</Accordion>

<Accordion title="PHP" icon="fa-brands fa-php">
  ```php
  function verifyPaymentLinksWebhook(array $payload, string $clientSecret): bool {
      // $payload: associative array of URL-decoded webhook fields
      // $clientSecret: your OAuth2 client_secret (not merchant salt)
      $hashString = implode("|", [
          $clientSecret,
          $payload["status"] ?? "",
          "", "", "", "", "",
          $payload["udf5"] ?? "",
          $payload["udf4"] ?? "",
          $payload["udf3"] ?? "",
          $payload["udf2"] ?? "",
          $payload["udf1"] ?? "",
          $payload["email"] ?? "",
          $payload["firstname"] ?? "",
          $payload["productinfo"] ?? "",
          $payload["amount"] ?? "",
          $payload["txnid"] ?? "",
          $payload["key"] ?? "",
      ]);
      $computedHash = hash("sha512", $hashString);
      return hash_equals($computedHash, $payload["hash"] ?? "");
  }
  ```
</Accordion>

***

## Step 4 — Respond with HTTP 200

Your endpoint **must return HTTP 200** to acknowledge receipt. If PayU does not receive a 200, it will retry the webhook.

```
HTTP/1.1 200 OK
```

Return 200 **before** running any slow processing (database writes, emails, etc.) to avoid timeouts. Enqueue background work instead.

***

## Retry Behaviour

If your endpoint does not return HTTP 200, PayU retries the webhook automatically. Keep your endpoint idempotent — check whether you have already processed a given `mihpayid` before updating your order state.

***

## Whitelist PayU IP Addresses

If your server is behind a firewall, add PayU's webhook IPs to your allowlist:

| Environment     | IPs                                         |
| --------------- | ------------------------------------------- |
| Test            | `180.179.174.1`, `3.6.73.183`, `3.6.83.44`  |
| Production (DC) | `3.7.89.1`, `3.7.89.2`, `3.7.89.3`          |
| Production (DR) | `52.140.8.88`, `52.140.8.89`, `52.140.8.64` |

***

## Troubleshooting

<Accordion title="Hash verification keeps failing" icon="far fa-circle-xmark">
  The most common cause is using the merchant **salt** instead of the `client_secret`. For Payment Links, hash verification uses `client_secret`.

  Check:

  1. Are you using the correct `client_secret` (the same one used to generate OAuth2 tokens)?
  2. Are you URL-decoding the payload fields before building the hash string? Special characters in `productinfo`, `firstname`, or `email` that aren't decoded will produce a wrong hash.
  3. Are you trimming whitespace from all fields?
  4. Is the `amount` field used exactly as received — including decimal places (e.g., `500.00`, not `500`)?
</Accordion>

<Accordion title="Webhook is not being received at my endpoint" icon="far fa-bell-slash">
  1. **Is the webhook URL registered?** Check **Dashboard → Settings → Webhooks**.
  2. **Is the URL HTTPS and publicly reachable?** Test with a tool like [Webhook.site](https://webhook.site) to confirm PayU can reach your server.
  3. **Is your server behind a firewall?** Whitelist [PayU's IP addresses](#whitelist-payu-ip-addresses).
  4. **Check webhook logs** in the Dashboard under **Developers → Webhook Logs** — failed delivery attempts are listed there.
</Accordion>

<Accordion title="I received a webhook but the status is 'pending'" icon="far fa-clock">
  `pending` means the payment is still being processed by the bank. Do not mark the order as paid yet. PayU will send a follow-up webhook when the status resolves to `success` or `failure`.

  If the payment stays pending for more than a few hours, use the [Fetch Payment Links API](doc:api-fetch) or the [Verify Payment API](doc:verify-payment-api) to check the current status.
</Accordion>

***

## Related Pages

<Cards>
  <Card title="Webhook Events and Sample Payloads" href="doc:webhook-events-and-sample-payloads" icon="fa-code">
    Full payload reference for all webhook event types.
  </Card>

  <Card title="Authentication (Token)" href="doc:api-auth-token" icon="fa-key">
    Get the client_secret and OAuth2 token for Payment Links APIs.
  </Card>

  <Card title="Fetch Payment Links" href="doc:api-fetch" icon="fa-magnifying-glass">
    Poll payment status if you miss a webhook.
  </Card>

  <Card title="Payment Links FAQs" href="doc:payment-links-faqs" icon="fa-circle-question">
    Common questions about Payment Links.
  </Card>
</Cards>
