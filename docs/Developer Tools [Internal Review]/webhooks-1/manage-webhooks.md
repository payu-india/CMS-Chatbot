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

   <Image src="https://files.readme.io/ef485a951c6227cfab10d06d5af1c446849bc5e7048a223384c51f5b49bb5e3f-Screenshot_2026-03-02_at_10.15.10_AM.png" alt="PayU Dashboard Developers section for creating a new webhook" align="center" border={true} />

2. Got to the **Webhooks&#x20;**&#x74;ab and click the delete icon next to the webhook entry you want to update.

   <Image src="https://files.readme.io/4afa8c1835ab6e84dea32009b8ccfdc0c03a37ed24225cdc756b8a7fec188df8-Screenshot_2026-08-26_at_3.56.40_PM.png" border={true} />

3. Click **Delete&#x20;**&#x74;o confirm and delete the webhook.

   <Image src="https://files.readme.io/35e90e7f567123cf0b7279e0b324bab1d5031f9704769852315f41e76cdb6d8c-Screenshot_2026-08-26_at_3.57.44_PM.png" border={true} />


<Callout icon="far fa-exclamation" theme="error">
  ### **Watch Out!**

  Deleting a webhook is permanent. PayU immediately stops sending events to that URL. Make sure you no longer need the webhook before deleting it.
</Callout>

***

## Webhook Logs

PayU Dashboard provides **Webhook Logs** to help you monitor webhook delivery and troubleshoot issues.

To access webhook logs:

1. Log in to the [PayU dashboard](https://onboarding.payu.in/app/account/signin) and click **Developers** from the left menu.

   <Image src="https://files.readme.io/ef485a951c6227cfab10d06d5af1c446849bc5e7048a223384c51f5b49bb5e3f-Screenshot_2026-03-02_at_10.15.10_AM.png" alt="PayU Dashboard Developers section for creating a new webhook" align="center" border={true} />

2. Go to **Webhook Logs** tab. It display:
   - **Timestamp**: Date and time of the webhook delivery attempt
   - **Webhook location**: The URL where the webhook was sent
   - **Event Type**: The webhook event triggered (e.g., `payment.success`)
   - **Status**: Whether the webhook was delivered successfully or failed
   - **Response Code**: HTTP status code returned by your server


<Image src="https://files.readme.io/cc515832d3f8778e97a165428b43955af3b2b351d46de834d49435e543e63d3e-dashboard_webhooks_logs.png" alt="PayU Dashboard webhooks - Navigate to Developer > Webhook Logs tab" align="center" border={true} />


3. Click any webhook entry to view full details:
   - **Event Type**, **Status**, **URL**, and **Time**
   - Complete request payload
   - Response code from your server


<Image src="https://files.readme.io/98b5fbb04198a57a6f6e2835c18d63693b68effc2e46bcfd3c66df3acc45cfb9-dashboard_webhooks_logs_details.png" alt="PayU Dashboard webhooks - The webhook details including event type, status, URL, timestamp and payload are displayed." align="center" border={true} />
