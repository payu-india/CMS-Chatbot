---
title: Configure Chargeback Webhook
deprecated: false
hidden: false
metadata:
  robots: index
---
Configure chargeback webhooks to automatically receive instant notifications when chargeback events occur, helping you stay informed and respond quickly to minimize financial impact.

## Prerequisites

Before configuring a chargeback webhook, ensure that:

* You have access to your PayU merchant dashboard
* You have a server endpoint ready to receive webhook notifications
* Your endpoint can handle HTTP POST requests

## Procedure

1. Navigate to the Chargeback dashboard.

   * Log in to PayU Dashboard.
   * Select **Chargeback** on the menu or left-pane.

   The Chargeback dashboard is displayed in a new browser tab.

   <Image align="center" border={true} src="https://files.readme.io/be62517293a9c1574046e96ed0565658547ea12dc73580530e9ee6f3b0ea8828-dashboard_home_chargeback_selection.png" className="border" />
2.    Click **Configure Webhooks** at the top-right corner.
3. Click the **Configure Webhooks** button.

<Image align="center" src="https://files.readme.io/78e3f0f2d0569ee9301008d89f41953d16e6c72b65da19fb9b6b780c425002cf-chargeback_webhooks_page.png" />

4. Click **Edit**.

The _Configure Webhook_ page is displayed.

<Image align="center" src="https://files.readme.io/703624965764d8eac5bc1b230db29779f55b97f8d28f11073e7c60779027ab20-cb_confgure_webhook.png" />

5. In the configuration form, fill in the following details:
   * **Webhook URL**: Enter the URL where you want to receive webhook payloads
   * **Fields Selection**: Select the fields you want to include in the webhook payload
   * **Activation Status**: Set the webhook as active or inactive using the toggle switch
6. Click **Save Configuration** to finalize your webhook configuration

