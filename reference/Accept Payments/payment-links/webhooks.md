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



When a customer pays via a Payment Link, PayU sends a webhook POST to your registered endpoint. Webhooks notify your server the moment a payment status changes.

***

## Step 1: Register Your Webhook Endpoint

1. Log in to the [PayU Dashboard](https://onboarding.payu.in/).
2. Go to **Settings → Webhooks**.
3. Enter your endpoint URL under **Webhook URL** and click **Save**.

<Callout icon="🚧" theme="warning">
  Your endpoint must be publicly accessible over HTTPS. `localhost` and HTTP URLs will not receive webhooks.
</Callout>

If the **Webhooks** option is not visible in your Dashboard, contact your PayU account manager to have it enabled for your merchant account.

***

## Step 2: Handle Incoming Webhook Events

PayU sends a **POST** request to your endpoint in the `application/x-www-form-urlencoded` format. Refer to the Webhook Events and Payloads page for webhook events and sample payloads.

***

## Step 3: Verify the Webhook Signature

<Callout icon="🚧" theme="warning">
  ### **Note:**

  Payment Links uses `client_secret` for hash verificatio&#x6E;**.** This is the same `client_secret` used to generate OAuth2 tokens (see [Authentication](doc:api-auth-token)). Using the wrong secret will cause every hash check to fail.
</Callout>

<Accordion title="Hash Formula" icon="fad fa-folder-minus">
  Compute the expected hash using the **reverse** of the payment hash formula:

  ```
  sha512(client_secret|status||||||udf5|udf4|udf3|udf2|udf1|email|firstname|productinfo|amount|txnid|key)
  ```

  Compare this to the `hash` field in the webhook payload. If they match, the webhook is authentic.
</Accordion>

***

## Errors and Troubleshooting

<Accordion title="Hash Verification Keeps Failing" icon="far fa-circle-xmark">
  The most common cause is using the merchant **salt** instead of the `client_secret`. For Payment Links, hash verification uses `client_secret`.

  Check:

  1. Are you using the correct `client_secret` (the same one used to generate OAuth2 tokens)?
  2. Are you URL-decoding the payload fields before building the hash string? Special characters in `productinfo`, `firstname`, or `email` that aren't decoded will produce a wrong hash.
  3. Are you trimming whitespace from all fields?
  4. Is the `amount` field used exactly as received — including decimal places (e.g., `500.00`, not `500`)?
</Accordion>

<Accordion title="I am not Receiving the Webhook" icon="far fa-bell-slash">
  1. **Is the webhook URL registered?** Check **Dashboard → Settings → Webhooks**.
  2. **Is the URL HTTPS and publicly reachable?** Test with a tool like [Webhook.site](https://webhook.site) to confirm PayU can reach your server.
  3. **Is your server behind a firewall?** Whitelist PayU's IP addresses.
  4. **Check webhook logs** in the Dashboard under **Developers → Webhook Logs&#x20;**&#x66;o&#x72;**&#x20;**&#x66;ailed delivery attempts.
</Accordion>

<Accordion title="I Received a Webhook But the Status is Pending" icon="far fa-clock">
  `pending` means the payment is still being processed by the bank. Do not mark the order as paid yet. PayU will send a follow-up webhook when the status resolves to `success` or `failure`.

  If the payment stays pending for more than a few hours, use the [Fetch Payment Links API](doc:api-fetch) or the [Verify Payment API](doc:verify-payment-api) to check the current status.
</Accordion>

***

## Related Pages

<Cards>
  <Card title="Webhook Events and Payloads" href="https://docs.payu.in/docs/webhook-events" icon="fa-code" target="_blank">
    Full payload reference for all webhook event types.
  </Card>

  <Card title="Authentication" href="https://docs.payu.in/reference/payment-links-authentication" icon="fa-key" target="_blank">
    Get the client_secret and OAuth2 token for Payment Links APIs.
  </Card>

  <Card title="Fetch All Payment Links" href="https://docs.payu.in/reference/fetch-all-payment-links" icon="fa-magnifying-glass" target="_blank">
    Poll payment status if you miss a webhook.
  </Card>

  <Card title="Payment Links FAQs" href="https://docs.payu.in/docs/payment-links-faqs" icon="fa-circle-question" target="_blank">
    Common questions about Payment Links.
  </Card>
</Cards>
