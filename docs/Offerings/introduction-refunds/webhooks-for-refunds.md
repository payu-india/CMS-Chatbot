---
title: Webhooks for Refunds
deprecated: false
hidden: true
metadata:
  robots: index
---
Configure chargeback webhooks to automatically receive instant notifications when you wish to be notified refunds status. This section describes how to create and configure refund webhooks using any of the following to receive automated notifications:

* [Using Dashboard](#using-dashboard)
* [Using Chargeback portal](#using-chargeback-portal)

## Prerequisites

Before configuring a chargeback webhook, ensure that:

* You have access to your PayU merchant dashboard
* You have a server endpoint ready to receive webhook notifications
* Your endpoint can handle HTTP POST requests

## Using Dashboard

1. Log on to PayU Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard).
2. Select **Developers** > **Webhooks tab**.

<Image align="center" border={false} src="https://files.readme.io/da995061d23e136d36c3bfe4482a90bfc5d2644e5c8e13b831a304e3ded73100-Screenshot_2024-10-08_at_5.21.21_PM.png" />

    The Create Webhooks page is displayed with the list of webhooks.

2. Click **Create Webhook** on the top-right corner of the _Create Webhooks_ page.

   The _Create Webhook_ pop-up page is displayed.

<Image align="center" border={false} src="https://files.readme.io/b1afa2ecaf68bcc42dcc8906f4d56d12183126483b65652f19417ff9cac243de-Screenshot_2024-10-08_at_5.22.20_PM.png" />

3. Select the **Chargeback** type from the **Type** drop-down list:
4. Select any of the following event type from the **Event** drop-down list:
   * A new chargeback is created
   * Chargeback status is changed
   * Chargeback amount is changed
5. Enter the webhook URL in the **Webhook URL** field.
6. Click **Create** to finish.

> 📘 Reference
>
> To update or delete an existing webhook, refer to:
>
> * [Update a Webhook](doc:update-a-webhook)
> * [Delete a Webhook](doc:delete-a-webhook-on-dashboard)

<br />
