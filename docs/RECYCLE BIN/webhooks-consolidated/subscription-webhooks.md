---
title: Subscription Webhooks
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
You can create Webhooks to recieve notifications for Zion Subscription events. 

## Webhook events for Zion Subscription

| Event Name                    | Description                                                                                                                                                                                              |
| :---------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SUBSCRIPTION_DEFINED_HTTP`   | Triggered when a subscription is created into Zion system, the subscription id is generated, and status of the subscription is set as Defined                                                            |
| `SUBSCRIPTION_ENABLED_HTTP`   | Triggered when the customer makes the first successful payment by providing the consent for subsequent payments. This event is also triggered when the `authRefId`gets associated with the subscription. |
| `SUBSCRIPTION_COMPLETED_HTTP` | Triggered when all recurring invoices associated with the plan is paid by the customer.                                                                                                                  |
| `SUBSCRIPTION_CANCELLED_HTTP` | Triggered when a subscription is cancelled. A subscription can be cancelled both by the user and the merchant.                                                                                           |

## Create & Manage Subscription Webhooks

The Subscription Webhook events are currently not available in the PayU Dashboard. To create and edit Subscription Webhooks, write an email to [integration@payu.in.](mailto:integration@payu.in.) 

> ❗️ Subscription Webhooks are currently not available in Test Mode.