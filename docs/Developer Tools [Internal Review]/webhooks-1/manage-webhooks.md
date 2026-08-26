---
title: Manage Webhooks
excerpt: Know how to manage your webhooks
deprecated: false
hidden: true
metadata:
  robots: index
---
## Update a Webhook

<Accordion title="When to update" icon="far fa-question">
  - Your server's webhook URL changes (domain migration, new endpoint path)

  - You want to add or remove event types from an existing webhook

  - You need to enable/disable a webhook temporarily without deleting it
</Accordion>

To update an existing webhook:

1. Log in to the [PayU dashboard](https://onboarding.payu.in/app/account/signin) and click **Developers** from the left menu.


   <Image src="https://files.readme.io/ef485a951c6227cfab10d06d5af1c446849bc5e7048a223384c51f5b49bb5e3f-Screenshot_2026-03-02_at_10.15.10_AM.png" alt="PayU Dashboard Developers section for creating a new webhook" align="center" />


2. Got to the **Webhooks&#x20;**&#x74;ab and click the edit icon next to the webhook entry you want to update.

   <Image src="https://files.readme.io/aad8a0d2c89f9979d6ce5f3c1cc2a53860d02d2a4ad1bd866357dd15553fb481-Screenshot_2026-08-26_at_1.56.30_PM.png" border={true} />


3. Modify the webhook URL. You can add multiple URLs separated by comma.

4. Click **Save** to save your changes.

   <Image src="https://files.readme.io/15fc4633f314de0da48635d75ba3089bcf6891053be119c948daa57364336e31-Screenshot_2026-08-26_at_3.01.29_PM.png" border={true} />



***

## Delete a Webhook

To delete a webhook:

1. Log in to the [PayU dashboard](https://onboarding.payu.in/app/account/signin) and click **Developers** from the left menu.

   <Image src="https://files.readme.io/ef485a951c6227cfab10d06d5af1c446849bc5e7048a223384c51f5b49bb5e3f-Screenshot_2026-03-02_at_10.15.10_AM.png" alt="PayU Dashboard Developers section for creating a new webhook" align="center" />

2. Got to the **Webhooks&#x20;**&#x74;ab and click the delete icon next to the webhook entry you want to update.

   <Image src="https://files.readme.io/4afa8c1835ab6e84dea32009b8ccfdc0c03a37ed24225cdc756b8a7fec188df8-Screenshot_2026-08-26_at_3.56.40_PM.png" border={true} />

3. Click **Delete&#x20;**&#x74;o confirm and delete the webhook.

   <Image src="https://files.readme.io/35e90e7f567123cf0b7279e0b324bab1d5031f9704769852315f41e76cdb6d8c-Screenshot_2026-08-26_at_3.57.44_PM.png" border={true} />


<Callout icon="far fa-exclamation" theme="error">
  ### **Watch Out!**

  Deleting a webhook is permanent. PayU will immediately stop sending events to that URL. Make sure you no longer need the webhook before deleting it.
</Callout>

***

## Prepare your endpoint to receive webhooks

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

Once you've registered your webhook URL, your server must be ready to:

1. **Accept POST requests** at the registered endpoint
2. **Parse the JSON or URL-encoded payload** (format depends on event type — see [Webhook Events Reference](doc:webhook-events-and-sample-payloads))
3. **Verify the request is from PayU** (see [Verify Webhook Requests](doc:verify-webhook-requests))
4. **Respond with HTTP 200 immediately** (within 10 seconds)
5. **Process the event asynchronously** (queue it for background processing)

**Example endpoint structure** (pseudocode):

```
POST /webhooks/payu

1. Read raw request body and headers
2. Verify signature (see Verify Webhook Requests page)
3. If signature valid:
     - Save event to processing queue
     - Log event receipt
     - Return 200 OK
4. If signature invalid:
     - Log potential security issue
     - Return 400 Bad Request (do not return 200 for invalid requests)
```

For detailed implementation guidance, see:

- [Verify Webhook Requests](doc:verify-webhook-requests) — Signature validation
- [Handle Webhook Events](doc:handle-webhook-events) — Idempotency, processing patterns, error handling

{/* END NEW CONTENT */}

***

## Monitor webhook delivery

{/* Sourced from docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/using-webhook-logs.md */}

PayU Dashboard provides **Webhook Logs** to help you monitor webhook delivery and troubleshoot issues.

### Access webhook logs

1. Log in to your PayU Dashboard.
2. Navigate to **Developers** > **Webhook Logs** tab.


<Image src="https://files.readme.io/cc515832d3f8778e97a165428b43955af3b2b351d46de834d49435e543e63d3e-dashboard_webhooks_logs.png" alt="PayU Dashboard webhooks - Navigate to Developer > Webhook Logs tab" align="center" border={true} />


The webhook logs display:

- **Timestamp**: Date and time of the webhook delivery attempt
- **Webhook location**: The URL where the webhook was sent
- **Event Type**: The webhook event triggered (e.g., `payment.success`)
- **Status**: Whether the webhook was delivered successfully or failed
- **Response Code**: HTTP status code returned by your server

### Filter and inspect webhooks

3. Filter webhooks using:
   - Date range
   - Customer name
   - Customer email
   - Phone number
4. Click any webhook entry to view full details:
   - Event type, status, URL, timestamp
   - Complete request payload
   - Response code from your server


<Image src="https://files.readme.io/98b5fbb04198a57a6f6e2835c18d63693b68effc2e46bcfd3c66df3acc45cfb9-dashboard_webhooks_logs_details.png" alt="PayU Dashboard webhooks - The webhook details including event type, status, URL, timestamp and payload are displayed." align="center" border={true} />


### Troubleshoot failed webhooks

Check the **Response Code** for clues:

- **500** (or other 5xx): Your server encountered an error — review application logs
- **Timeout**: Your server took longer than 10 seconds to respond — optimize processing or implement async queuing
- **Unable to connect**: PayU couldn't reach your server — verify the URL is publicly accessible and your firewall allows PayU's IPs

For detailed troubleshooting guidance, see [Test & Troubleshoot Webhooks](doc:test-troubleshoot-webhooks).

{/* END */}

***

## Next steps

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

Now that your webhook endpoint is configured:

<Cards>
  <Card title="Manage Webhooks" icon="fa-rocket">

  </Card>

  <Card title="Card Two" icon="fa-code">

  </Card>

  <Card title="Card Three" icon="fa-comments">

  </Card>
</Cards>

1. **Manage Webhooks: ​**
2. **[Handle Webhook Events](doc:handle-webhook-events)** — Learn best practices for processing events, handling duplicates, and managing errors
3. **[Webhook Events Reference](doc:webhook-events-and-sample-payloads)** — Review complete payload structures and parameters for each event type
4. **[Test & Troubleshoot Webhooks](doc:test-troubleshoot-webhooks)** — Test your integration before going live

**Product-specific webhook guides:**

- [Refund Webhooks](doc:webhooks-for-refunds)
- [Chargeback Webhooks](doc:webhooks-for-chargeback)
- [Subscription Webhooks](doc:webhooks-for-subscription)
- [Payout Webhooks](doc:payouts-webhooks)

{/* END NEW CONTENT */}
