---
title: Using Webhook Logs
deprecated: false
hidden: true
metadata:
  robots: index
  description: >-
    Configure PayU Dashboard webhooks to receive payment, refund, and dispute notifications. Create, update, and monitor webhook events with sample payloads for merchant integrations. Covers Using Webhook Logs.
  keywords:
    - payu dashboard webhooks setup guide
    - configure payment webhooks payu merchant dashboard
    - payu webhook events sample payloads
    - payu dashboard create update webhook
    - payment notification webhook payu dashboard
    - payu webhook logs dashboard guide
    - merchant webhook integration payu dashboard
    - payu dashboard webhook refund dispute events
    - payment gateway webhooks payu vs razorpay cashfree
    - payu dashboard webhook configuration india
---
The **Webhook Logs**  interface allows developers and merchants to monitor webhook delivery attempts and responses for their integration. This helps in troubleshooting and ensuring that critical events are successfully communicated to your server.

To access the Webhook Logs:

1. Log in to your PayU Dashboard.
2. Navigate to **Developer** > **Webhook Logs** tab.

<Image align="center" alt="PayU Dashboard webhooks - Navigate to Developer > Webhook Logs tab" border={true} src="https://files.readme.io/cc515832d3f8778e97a165428b43955af3b2b351d46de834d49435e543e63d3e-dashboard_webhooks_logs.png" className="border" />

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
4. Click any webhook to view the details.

  The webhook details including event type, status, URL, timestamp and payload are displayed.

<Image align="center" alt="PayU Dashboard webhooks - The webhook details including event type, status, URL, timestamp and payload are displayed." border={true} src="https://files.readme.io/98b5fbb04198a57a6f6e2835c18d63693b68effc2e46bcfd3c66df3acc45cfb9-dashboard_webhooks_logs_details.png" className="border" />

## Troubleshooting Failed Webhooks

* Check the **Response Code** for clues (e.g., `500` indicates a server error).
* Ensure your webhook endpoint is reachable and responds within the required timeout.
* Retry failed webhooks manually if supported.
