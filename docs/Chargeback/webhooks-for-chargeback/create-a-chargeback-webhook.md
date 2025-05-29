---
title: Create a Chargeback Webhook
deprecated: false
hidden: false
metadata:
  robots: index
---
## Prerequisites

Before configuring a chargeback webhook, ensure that:

* You have access to your PayU merchant dashboard
* You have a server endpoint ready to receive webhook notifications
* Your endpoint can handle HTTP POST requests

## Using Dashboard

1. Log on to PayU Dashboard. For more information, refer to [Log in to Dashboard](doc:log-in-to-dashboard).
2. Select **Developers** > **Webhooks tab**.

<Image align="center" src="https://files.readme.io/da995061d23e136d36c3bfe4482a90bfc5d2644e5c8e13b831a304e3ded73100-Screenshot_2024-10-08_at_5.21.21_PM.png" />

    The Create Webhooks page is displayed with the list of webhooks.

2. Click **Create Webhook** on the top-right corner of the *Create Webhooks* page.

   The *Create Webhook* pop-up page is displayed.

<Image align="center" src="https://files.readme.io/b1afa2ecaf68bcc42dcc8906f4d56d12183126483b65652f19417ff9cac243de-Screenshot_2024-10-08_at_5.22.20_PM.png" />

3. Select the **Chargeback** type from the **Type** drop-down list:
4. Select the event type from the **Event** drop-down list.
5. Enter the webhook URL in the **Webhook URL** field.
6. Click **Create** to finish.

> 📘 Reference
>
> To update or delete an existing webhook, refer to:
>
> * [Update a Webhook](doc:update-a-webhook)
> * [Delete a Webhook](doc:delete-a-webhook-on-dashboard)

## Using Chargeback portal

1. Visit [chargeback.payu.in](http://chargeback.payu.in)
2. Log in with your merchant credentials
3. Click the **Configure Webhooks** button.

The *Configure Webhook* page is displayed.

<Image align="center" src="https://files.readme.io/703624965764d8eac5bc1b230db29779f55b97f8d28f11073e7c60779027ab20-cb_confgure_webhook.png" />

1. In the configuration form, fill in the following details:
   * **Webhook URL**: Enter the URL where you want to receive webhook payloads
   * **Fields Selection**: Select the fields you want to include in the webhook payload
   * **Activation Status**: Set the webhook as active or inactive using the toggle switch
2. Click on the **Save** button to finalize your webhook configuration