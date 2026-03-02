---
title: Create a New Webhook
excerpt: >-
  Learn how to create a new webhook in the PayU dashboard. Step-by-step guide to
  set up payment webhooks, configure events, and receive real-time payment
  notifications from PayU.
deprecated: false
hidden: false
metadata:
  title: Create a New Webhook | PayU Dashboard
  description: ''
  keywords:
    - Create webhook PayU dashboard
    - PayU webhook setup
    - PayU payment webhooks
    - Configure webhook PayU
    - PayU dashboard webhook
    - Create Webhook using Dashboard
    - Webhook using Dashboard
    - PayU webhook URL
    - PayU payment event webhook
    - Set up PayU webhooks
  robots: index
next:
  description: ''
---
You can create as many webhooks as per your requirements and monitor the response from PayU. This section describes how to create webhook for payments.

To create a new webhook:

1. Log in to the [PayU dashboard](https://onboarding.payu.in/app/account/signin) and click **Developers** from the left menu.

<Image align="center" src="https://files.readme.io/ef485a951c6227cfab10d06d5af1c446849bc5e7048a223384c51f5b49bb5e3f-Screenshot_2026-03-02_at_10.15.10_AM.png" />

2. Go to **Webhooks** tab and click **Create Webhook**.

<Image align="center" src="https://files.readme.io/4015a3183106114e615ff8623382b8f290f577054603ecd89f8c3e3cb95ad543-Screenshot_2026-03-02_at_11.04.17_AM.png" />

    The **Create Webhook** pop-up menu is displayed.

3. Select **Payments** from the **Type** drop-down list.
4. Select the event type from the **Event** drop-down list. Below are the available options:
   * **Successful**
   * **Failed**
   * **Refund**
   * **Dispute**
5. Enter the webhook URL in the **Webhook URL** field. You can multiple URLs separated by commas.
6. Click **Create** to create a webhook.

<Image align="center" src="https://files.readme.io/296459b395d36d191679019fc9116ce3ceaadb588da7bb86e3cb7be1c4f501fd-Screenshot_2026-03-02_at_11.20.54_AM.png" />