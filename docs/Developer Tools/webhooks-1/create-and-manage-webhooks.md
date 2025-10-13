---
title: Create and manage Webhooks
excerpt: Create and Manage Payments Webhooks from PayU Dashboard
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
PayU allows you to create and manage the following types of Webhooks:

* Payment webhooks - Allows you to receive realtime notification for various events associated with Payments
* Payout Webhooks - Allows you to receive realtime notification for various events associated with Payouts.
* Subscription Webhooks - Allows you to receive realtime notification for various events associated with Subscriptions

## Payment Webhooks

### Payment Events

Following are the list of events that are currently supported for payments:

| Event Name | Description |
| :--------- | :---------- |
| Successful |             |
| Failed     |             |
| Refund     |             |
| Dispute    |             |

### Create a Payment Webhook

## Payouts Webhooks

### Payout Events

Following are the list of events that are currently supported for payouts:

| Event Name                       | Description                                                           |
| -------------------------------- | --------------------------------------------------------------------- |
| `deposit_success`                | Amount is successfully deposited/credited in the account              |
| `transfer_success`               | Transfer is completed successfully                                    |
| `transfer_failed`                | Failure is observed while completing the Transfer                     |
| `transfer_reversed`              | Transfer is reversed by the beneficiary bank                          |
| `smart_send_detail_submitted`    | Customer has filled in the details and submitted successfully         |
| `request_processing_failed`      | Failure is observed while raising a transaction request               |
| `low_balance_alert`              | Payouts account is on low balance                                     |
| `downtime_notification`          | Bank has scheduled downtime                                           |
| `bulk_smart_send_file_processed` | Smart send file upload is processed                                   |
| `transfer_success`               | Signal that a Penny with name match verification has been successful. |
| `smart_send_expired`             | Triggered to notify about the Smart Send link expiration.             |

## Subscription Webhooks

### Subscription Events

| Webhook Types          | Description                                                                                  | Events & Payloads             |
| :--------------------- | :------------------------------------------------------------------------------------------- | :---------------------------- |
| Payment Webhooks       | Allows you to receive realtime notification for various events associated with Payments      | See Payment events & Payloads |
| Payouts Webhooks       | Allows you to receive realtime notification for various events associated with Payouts.      | See Payment events & Payloads |
| Subscriptions Webhooks | Allows you to receive realtime notification for various events associated with Subscriptions | See Payment events & Payloads |
