---
title: Set Up and Configure Webhooks
deprecated: false
hidden: true
metadata:
  robots: index
---
Register a webhook with PayU, select which events you want to receive, and configure your server to handle incoming webhook requests.

***

## Before You Start (Prerequisites)

<Accordion title="Prerequisites" icon="far fa-list-timeline">
  - You have access to your PayU merchant dashboard
  - You have a server endpoint ready to receive webhook notifications
  - Your endpoint can handle HTTP POST requests
  - If you have IP whitelisting enabled at your server, whitelist PayU's IP addresses (see [IP addresses to whitelist](#ip-addresses-to-whitelist) below)
</Accordion>

***

## Endpoint Requirements

Your webhook endpoint must meet these requirements:

<Accordion title="HTTPS and Public Accessibility" icon="far fa-diagram-successor">
  - **URL format**: `https://your-domain.com/your-webhook-endpoint`

  - **Protocol**: HTTPS only (HTTP is not supported in production)

  - **Accessibility**: Publicly accessible from the internet (not localhost or behind a firewall that blocks PayU's IPs)

  <Tabs>
    <Tab title="Valid Webhook URLs (Example)" icon="far fa-link">
      * `https://api.yourcompany.com/webhooks/payu`
      * `https://yourapp.com/payment-notifications`
      * `https://webhooks.yourdomain.in/payu/events`
    </Tab>

    <Tab title="Not Supported (Invalid Example)">
      - `http://` URLs (HTTP is not allowed)
      - `http://localhost:4000/webhook` (not publicly accessible)
      - URLs behind VPN or firewalls that block PayU's IPs
    </Tab>
  </Tabs>
</Accordion>

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

<Accordion title="Response Time and Acknowledgment" icon="far fa-down-left-and-up-right-to-center">
  PayU expects your endpoint to:

  - **Return HTTP status code 200** to acknowledge receipt
  - **Respond within 10 seconds** — if your endpoint times out or returns a non-200 status, PayU considers delivery failed
  - **Defer complex processing** — respond with 200 immediately, then process the event asynchronously (update database, send emails, etc.) in a background job

  <Callout icon="📘" theme="info">
    ### **Note:**

    Any response code other than 200, or a timeout beyond 10 seconds, triggers PayU's retry mechanism.
  </Callout>
</Accordion>

{/* Sourced from docs/payouts/payouts-integration/payouts-webhooks.md */}

<Accordion title="Retry Behavior on Failure" icon="far fa-file-dashed-line">
  If PayU doesn't receive a 200 response within the timeout window, the webhook delivery is retried:

  - **Maximum retry attempts**: 2 additional retries (3 total delivery attempts)
  - **Retry schedule**: PayU retries with exponential backoff

  <Callout icon="📘" theme="info">
    ### **Important:**

    On failure, the webhook is re-tried maximum 2 more times with the same protocol.
  </Callout>
</Accordion>

###

<Accordion title="IP Addresses to Whitelist" icon="far fa-laptop-code">
  All webhook requests originate from PayU's IP addresses. If your server is behind a firewall, whitelist these IPs:

  | **Environment**            | **DC IPs**                                                           | **DR IPs**                                                            |
  | -------------------------- | -------------------------------------------------------------------- | --------------------------------------------------------------------- |
  | **Test Environment**       | <ul><li>180.179.174.1</li><li>3.6.73.183</li><li>3.6.83.44</li></ul> | NA                                                                    |
  | **Production Environment** | <ul><li>3.7.89.1</li><li>3.7.89.2</li><li>3.7.89.3</li></ul>         | <ul><li>52.140.8.88</li><li>52.140.8.89</li><li>52.140.8.64</li></ul> |

  <Accordion title="Additional IPs for Payout Webhooks" icon="far fa-table-rows-add-below">
    **Production:**

    - Existing IPs: 180.179.168.225
    - New IPs: 180.179.168.225, 13.71.57.148, 52.140.8.68, 180.179.174.1

    **Test:**

    - Existing IPs: 180.179.165.250, 13.71.57.148
    - New IPs: 13.235.110.253
  </Accordion>
</Accordion>

***

## Configure webhooks via Dashboard

{/* Sourced from docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/create-a-new-webhook.md */}

To create a new webhook:

1. Log in to the [PayU dashboard](https://onboarding.payu.in/app/account/signin) and click **Developers** from the left menu.


<Image src="https://files.readme.io/ef485a951c6227cfab10d06d5af1c446849bc5e7048a223384c51f5b49bb5e3f-Screenshot_2026-03-02_at_10.15.10_AM.png" alt="PayU Dashboard Developers section for creating a new webhook" align="center" />


2. Go to **Webhooks** tab and click **Create Webhook**.


<Image src="https://files.readme.io/4015a3183106114e615ff8623382b8f290f577054603ecd89f8c3e3cb95ad543-Screenshot_2026-03-02_at_11.04.17_AM.png" alt="PayU Dashboard webhooks - Go to Webhooks tab and click Create Webhook" align="center" />


The **Create Webhook** pop-up menu is displayed.

3. Select **Payments** from the **Type** drop-down list.
4. Select the event type from the **Event** drop-down list. Available options:
   - **Successful** — Payment succeeds
   - **Failed** — Payment fails
   - **Refund** — Refund succeeds or fails
   - **Dispute** — Chargeback or dispute is raised
5. Enter the webhook URL in the **Webhook URL** field. You can enter multiple URLs separated by commas.
6. Click **Create** to create the webhook.


<Image src="https://files.readme.io/296459b395d36d191679019fc9116ce3ceaadb588da7bb86e3cb7be1c4f501fd-Screenshot_2026-03-02_at_11.20.54_AM.png" alt="PayU Dashboard webhooks - Click Create to create a webhook" align="center" />


{/* END */}

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

After creating the webhook, PayU will start sending events to your registered URL(s) whenever the selected event types occur.

> **Multiple URLs**: If you register multiple webhook URLs for the same event type, PayU sends the event to **all** registered URLs. This is useful for redundancy or sending events to multiple systems.

{/* END NEW CONTENT */}

***

## Configure webhooks via API

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

You can also create and manage webhooks programmatically using PayU's Webhook Configuration APIs.

**See the complete API reference:**

- [Webhook Configuration API](ref:webhook-configuration-api) — Create, update, list, and delete webhook endpoints via API

**Common use cases for API configuration:**

- Automating webhook setup as part of merchant onboarding
- Managing webhooks across multiple merchant accounts (for partners or aggregators)
- Rotating webhook URLs or secrets programmatically

Refer to the API documentation for request/response formats, authentication, and parameter details.

{/* END NEW CONTENT */}

***

## Manage existing webhooks

### Update a webhook

{/* Sourced from docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/update-a-webhook.md */}

To update an existing webhook:

1. Navigate to **Developers** > **Webhooks** on the PayU dashboard.
2. Locate the webhook you want to modify.
3. Click the **Edit** icon next to the webhook entry.
4. Modify the webhook URL or event selection as needed.
5. Click **Update** to save your changes.

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

**When to update:**

- Your server's webhook URL changes (domain migration, new endpoint path)
- You want to add or remove event types from an existing webhook
- You need to enable/disable a webhook temporarily without deleting it

{/* END NEW CONTENT */}

### Delete a webhook

{/* Sourced from docs/getting started/payu-dashboard/manage-webhooks-using-dashboard/delete-a-webhook-on-dashboard.md */}

To delete a webhook:

1. Go to the **Developers** > **Webhooks** section.
2. Locate the webhook you want to delete.
3. Click the **Delete** icon (trash icon).
4. Confirm the deletion when prompted.

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

> **Warning**: Deleting a webhook is permanent. PayU will immediately stop sending events to that URL. Make sure you no longer need the webhook before deleting it.

{/* END NEW CONTENT */}

{/* END */}

{/* NEW CONTENT — not sourced from existing docs, needs SME review */}

### Rotate webhook secrets (if applicable)

{/* Webhook secrets and rotation are mentioned in Stripe/Razorpay docs but not confirmed in PayU repo */}

{/* NEEDS VALIDATION: Does PayU provide webhook signing secrets? Is secret rotation supported? */}

{/* If yes, add documentation here. If no, remove this section. */}

{/* END NEW CONTENT */}

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

1. **[Verify Webhook Requests](doc:verify-webhook-requests)** — Implement signature verification to ensure requests are genuinely from PayU
2. **[Handle Webhook Events](doc:handle-webhook-events)** — Learn best practices for processing events, handling duplicates, and managing errors
3. **[Webhook Events Reference](doc:webhook-events-and-sample-payloads)** — Review complete payload structures and parameters for each event type
4. **[Test & Troubleshoot Webhooks](doc:test-troubleshoot-webhooks)** — Test your integration before going live

**Product-specific webhook guides:**

- [Refund Webhooks](doc:webhooks-for-refunds)
- [Chargeback Webhooks](doc:webhooks-for-chargeback)
- [Subscription Webhooks](doc:webhooks-for-subscription)
- [Payout Webhooks](doc:payouts-webhooks)

{/* END NEW CONTENT */}
