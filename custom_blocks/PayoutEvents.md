---
name: Payout events
---
## Webhook events for Payouts

| Event Name                       | Description                                                                  |
| -------------------------------- | ---------------------------------------------------------------------------- |
| `deposit_success`                | Triggered when the amount is successfully deposited/credited in the account. |
| `transfer_success  `             | Triggered when the transfer is successful.                                   |
| `transfer_failed `               | Triggered when the transfer is failed.                                       |
| `transfer_reversed `             | Triggered when the transafer is reveresed by the bank.                       |
| `smart_send_detail_submitted `   | Triggered when the customer details are submitted successfully.              |
| `request_processing_failed `     | Triggered when failure is observed while raising a transaction request.      |
| `low_balance_alert  `            | Triggered when the Payouts account is on low balance.                        |
| `downtime_notification`          | Triggered when the bank has scheduled downtime.                              |
| `bulk_smart_send_file_processed` | Triggered when smart send file upload is processed.                          |
| `transfer_success`               | Triggered when a Penny with name match verification has been successful.     |
| `smart_send_expired`             | Triggered when a smart send link is expired                                  |
| `smart_send_cancelled`           | Triggered when a smart send link is cancelled                                |
| `smart_send_rejected`            | Triggered when a smart send link is rejected.                                |