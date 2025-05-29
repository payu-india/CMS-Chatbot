---
title: Create a Chargeback Webhook
deprecated: false
hidden: false
metadata:
  robots: index
---
Chargeback webhooks provide real-time notifications about important chargeback events, allowing merchants to stay updated and take necessary actions promptly. Webhooks are sent for the following events:

* A new chargeback is created
* Chargeback status is changed
* Chargeback amount is changed

## Prerequisites

Before configuring a chargeback webhook, ensure that:

* You have access to your PayU merchant dashboard
* You have a server endpoint ready to receive webhook notifications
* Your endpoint can handle HTTP POST requests

## Using Dashboard

1. Log in to your PayU merchant dashboard
2. Navigate to the **Settings** tab on the left side
3. Click **Webhooks**.
4. <br />

## Using Chargeback portal

1. Visit [chargeback.payu.in](http://chargeback.payu.in)
2. Log in with your merchant credentials
3. Click on the **Configure Webhooks** button
4. In the configuration form, fill in the following details:
   * **Webhook URL**: Enter the URL where you want to receive webhook payloads
   * **Fields Selection**: Select the fields you want to include in the webhook payload
   * **Activation Status**: Set the webhook as active or inactive using the toggle switch
5. Click on the **Save** button to finalize your webhook configuration