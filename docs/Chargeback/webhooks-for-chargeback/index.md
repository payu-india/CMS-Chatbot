---
title: Webhooks for Chargeback
deprecated: false
hidden: true
metadata:
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

| Field        | Description                                    |
| ------------ | ---------------------------------------------- |
| type         | Type of transaction (e.g., "payments")         |
| event        | Event type (e.g., "dispute")                   |
| reason\_code | Reason for the chargeback                      |
| created\_at  | Timestamp when the chargeback was created      |
| updated\_at  | Timestamp when the chargeback was last updated |
| mid          | Merchant ID                                    |
| cb\_id       | Chargeback ID                                  |
| txn\_id      | Transaction ID associated with the chargeback  |
| cb\_type     | Type of chargeback (e.g., "RBI/BO")            |
| due\_date    | Due date for the chargeback resolution         |
| cb\_amount   | Amount involved in the chargeback              |
| cb\_status   | Current status of the chargeback               |

## Chargeback Status Values

The `cb_status` field can have the following values:

* New
* Pending Response
* Pending Doc Review
* Submitted to bank
* Insufficient Document
* Closed Customer Favour
* Closed in merchant favour
* Closed under fraud liability
* Bank Comm Sent

## Reason Codes for Chargebacks

Chargeback reason codes in the payload are descriptive text values, such as:

* Non Receipt of Goods or Services
* Cancelled recurring Transaction
* Fraud - Card Present Environment
* Fraud - Card Not Present Environment
* Product or Services not as described
* Damaged or Defective Product Received
* Customer charged more than once
* Credit not processed
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