---
title: Webhooks for Refunds
deprecated: false
hidden: false
metadata:
  robots: index
---
Configure refund webhooks to automatically receive instant notifications when refunds status has changed. This section describes how to create and configure refund webhooks using any of the following to receive automated notifications.

<Callout icon="📘" theme="info">
  **Prerequiistes**: Before configuring a refund event webhook, ensure that:

  * You have access to your PayU merchant dashboard
  * You have a server endpoint ready to receive webhook notifications
  * Your endpoint can handle HTTP POST requests
</Callout>

To create a refund webhook:

1. Log on to PayU Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard).
2. Select **Developers** > **Webhooks** tab.

<Image align="center" border={true} src="https://files.readme.io/da995061d23e136d36c3bfe4482a90bfc5d2644e5c8e13b831a304e3ded73100-Screenshot_2024-10-08_at_5.21.21_PM.png" className="border" />

    The Create Webhooks page is displayed with the list of webhooks.

2. Click **Create Webhook** on the top-right corner of the _Create Webhooks_ page.

   The _Create Webhook_ pop-up page is displayed.

<Image align="center" border={true} width="250px" src="https://files.readme.io/612e76546ff3f39c8b70d45cc4c6aa31a37a8ed189936fb7f58d89752740e65d-webhook_payment_refund_event.png" className="border" />

2. Select the **Payment** type from the **Type** drop-down list:
3. Select **Refund** as type from the **Event** drop-down list:
4. Enter the webhook URL in the **Webhook URL** field.
5. Click **Create** to finish.

<Callout icon="📘" theme="info">
  **References**: 

  * **Sample webhook response**: For sample webhook responses, refer to [Refund Status Callback](ref:refund-status-callback).
  * **Update or delete a webhook**: To update or delete an existing webhook, refer to:
    * [Update a Webhook](doc:update-a-webhook)
    * [Delete a Webhook](doc:delete-a-webhook-on-dashboard)
</Callout>

<br />
