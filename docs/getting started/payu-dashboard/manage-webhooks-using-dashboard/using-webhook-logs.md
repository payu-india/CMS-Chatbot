---
title: Using Webhook Logs
deprecated: false
hidden: true
metadata:
  robots: index
---
The **Webhook Logs**  interface allows developers and merchants to monitor webhook delivery attempts and responses for their integration. This helps in troubleshooting and ensuring that critical events are successfully communicated to your server. 

To access the Webhook Logs:

1. Log in to your PayU Dashboard.
2. Navigate to **Developer** > **Webhook Logs** tab. 

<Image align="center" border={true} src="https://files.readme.io/cc515832d3f8778e97a165428b43955af3b2b351d46de834d49435e543e63d3e-dashboard_webhooks_logs.png" className="border" />

The tabulated webhooks logs on the right-pane displays:

* **Timestamp**: Date and time of the webhook attempt.
* **Webhook location**: The URL for which the webhook is created.
* **Event Type**: The webhook event triggered (e.g., `payment.success`).
* **Status**: Indicates whether the webhook was delivered successfully or failed.
* **Response Code**: HTTP status code returned by your server.

3. Filter the webhooks using the following fields:
   * Date Range
   * Customer Name
   * Customer Email
   * Phone Number

## Troubleshooting Failed Webhooks

* Check the **Response Code** for clues (e.g., `500` indicates a server error).
* Ensure your webhook endpoint is reachable and responds within the required timeout.
* Retry failed webhooks manually if supported.