---
title: Webhooks for Chargeback
deprecated: false
hidden: false
metadata:
  title: Webhooks for Chargeback
  description: >-
    Set up PayU chargeback webhooks for real-time notifications. Receive instant
    updates on chargeback events, status changes, and dispute modifications via
    webhook integration
  keywords:
    - chargeback webhooks
    - PayU webhooks
    - real-time chargeback notifications
    - chargeback status updates
    - webhook integration
    - dispute notifications
    - payment webhook
  robots: index
---
Chargeback webhooks provide real-time notifications about important chargeback events, allowing merchants to stay updated and take necessary actions promptly. Webhooks are sent for the following events:

* A new chargeback is created
* Chargeback status is changed
* Chargeback amount is changed

To create webhooks using Dashboard, refer to [Create a Chargeback Webhook](doc:create-a-chargeback-webhook) > [Using Dashboard](doc:create-a-chargeback-webhook#using-dashboard). To update or delete an existing webhook, refer to:

* [Update a Webhook](doc:update-a-webhook)
* [Delete a Webhook](doc:delete-a-webhook-on-dashboard)

## Understanding payload

When a chargeback event occurs, PayU will send a POST request to your configured URL with a JSON payload similar to the following:

```json
{
  "type": "payments",
  "event": "dispute",
  "reason_code": "Fraud - Card Present Environment",
  "created_at": "2025-01-15T21:28:25.000+05:30",
  "updated_at": "2025-05-27T22:08:16.000+05:30",
  "mid": "2",
  "cb_id": 1761758,
  "txn_id": "999000000000468",
  "cb_type": "RBI/BO",
  "due_date": "2025-03-31",
  "cb_amount": "1.0",
  "cb_status": "Bank Comm Sent"
}
```

### Fields in the payload

| Field       | Description                                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type        | Type of transaction  and merchant must include the value as **payments** only.                                                                                   |
| event       | Event type and the merchant must the include the value as **dispute** only.                                                                                      |
| reason_code | Reason for the chargeback. For the list of reason codes, refer to [Reason codes for chargebacks](doc:reason-codes-for-chargebacks).                              |
| created_at  | Timestamp when the chargeback was created                                                                                                                        |
| updated_at  | Timestamp when the chargeback was last updated                                                                                                                   |
| mid         | PayU Merchant ID                                                                                                                                                 |
| cb_id       | Chargeback ID                                                                                                                                                    |
| txn_id      | Transaction ID associated with the chargeback. This is merchant transaction ID or PayU transaction ID.                                                           |
| cb_type     | Type of chargeback (for example, "RBI/BO", that is, Reserve Bank of India/Banking Operations)                                                                    |
| due_date    | Due date for the chargeback resolution                                                                                                                           |
| cb_amount   | Amount involved in the chargeback                                                                                                                                |
| cb_status   | Current status of the chargeback. For the possible chargeback status values, refer to [cb\_status field values description](#cb_status-field-values-description) |

### cb_status field values description

The `cb_status` or chargeback status field can have the following values:

| Chargeback Status            | Description                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New                          | It indicates that a new chargeback has been initiated by the customer basis the chargeback reason.                                                                                                                                                                                                                     |
| Pending Response             | It indicates that the chargeback is awaiting merchant response, that is, to accept, partially accept or decline with evidence.                                                                                                                                                                                         |
| Pending Doc Review           | It indicates that merchant has submitted their response, and the response are being reviewed by the PayU Chargeback team.                                                                                                                                                                                              |
| Submitted to Bank            | It indicates that the PayU Chargeback team has completed their review and forwarded the evidence to the bank for representment.                                                                                                                                                                                        |
| Insufficient Document        | It indicates that the PayU Chargeback team has reviewed the evidence documents and is requesting the merchant for additional documents for representment or the correct document based on the Chargeback team's comment.                                                                                               |
| Closed Customer Favour       | It indicates that that the chargeback has been closed in the customer's favour. The merchant will lose the chargeback amount to the customer.                                                                                                                                                                          |
| Closed in Merchant Favour    | It indicates that the chargeback has been closed in the merchant's favour. The chargeback amount will be reversed back to the merchant account.                                                                                                                                                                        |
| Closed under Fraud Liability | It indicates that the chargeback has been closed since the transaction has been identified as fraudulent. Moreover, PayU will cover the chargeback amount under the fraud liability program so the chargeback amount will be reversed back to the merchant account or will not be debited from the merchant's account. |

## Reason codes for chargebacks

Chargeback reason codes in the payload are descriptive text values, such as:

* Non Receipt of Goods or Services
* Cancelled recurring Transaction
* Fraud - Card Present Environment
* Fraud - Card Not Present Environment
* Product or Services not as described
* Damaged or Defective Product received
* Customer charged more than once
* Credit not Processed
* Incorrect amount charged
* Customer paid by other means
* Customer request copy
* Legal process or Fraud analysis
* Cardholder Does Not Recognize the Transaction
* Technical - Late presentment
* Fraud - No Authorization
* Pre-Compliance Chargeback
* Customer Dispute Transaction
* Retrieval Request
* RFI - Request for proof of order fulfillment
* Others - Not specified anywhere
* Arbitration Chargeback
* Compliance Chargeback
* Net-Banking Dispute
* Technical-Decline Authorization
* Non Fulfillment of Retrieval Request
* Fraud-others
* Technical-Others
* Account Debited but confirmation not received at merchant location

## Troubleshooting

If you're not receiving webhook notifications:

* Verify that your webhook URL is correct and accessible from the internet
* Check that your endpoint returns a 200 OK response to acknowledge receipt of the webhook
* Ensure your webhook is set to "Active" in the configuration
* Contact PayU support if you continue to experience issues
