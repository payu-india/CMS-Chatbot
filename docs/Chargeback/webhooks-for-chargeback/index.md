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

| Field        | Description                                                                                                                                                      |
| ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type         | Type of transaction (e.g., "payments")                                                                                                                           |
| event        | Event type (e.g., "dispute")                                                                                                                                     |
| reason\_code | Reason for the chargeback                                                                                                                                        |
| created\_at  | Timestamp when the chargeback was created                                                                                                                        |
| updated\_at  | Timestamp when the chargeback was last updated                                                                                                                   |
| mid          | Merchant ID                                                                                                                                                      |
| cb\_id       | Chargeback ID                                                                                                                                                    |
| txn\_id      | Transaction ID associated with the chargeback. This is merchant transaction ID or PayU transaction ID.                                                           |
| cb\_type     | Type of chargeback (e.g., "RBI/BO")                                                                                                                              |
| due\_date    | Due date for the chargeback resolution                                                                                                                           |
| cb\_amount   | Amount involved in the chargeback                                                                                                                                |
| cb\_status   | Current status of the chargeback. For the possible chargeback status values, refer to [cb\_status field values description](#cb_status-field-values-description) |

### cb\_status field values description

The `cb_status` or chargeback status field can have the following values:

| Chargeback Status            | Description                                                                                                                                                                                                                                                                                                                |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| New                          | This chargeback status shows that a new chargeback has been initiated by the customer basis the chargeback reason.                                                                                                                                                                                                         |
| Pending Response             | This chargeback status shows that the chargeback is awaiting merchant response, that is, to accept, partially accept or decline with evidence.                                                                                                                                                                             |
| Pending Doc Review           | This chargeback status shows that merchant has submitted their response, and the response are being reviewed by the PayU Chargeback team.                                                                                                                                                                                  |
| Submitted to Bank            | This chargeback status indicates that the PayU Chargeback team has completed their review and forwarded the evidence to the bank for representment.                                                                                                                                                                        |
| Insufficient Document        | This chargeback status shows that the PayU Chargeback team has reviewed the evidence documents and is requesting the merchant for additional documents for representment or the correct document based on the chargeback team's comment.                                                                                   |
| Closed Customer Favour       | This chargeback status shows that the chargeback has been closed in the customer's favour. The merchant will lose the chargeback amount to the customer.                                                                                                                                                                   |
| Closed in Merchant Favour    | This chargeback status shows that the chargeback has been closed in the merchant's favour. The chargeback amount will be reversed back to the merchant account.                                                                                                                                                            |
| Closed under Fraud Liability | This chargeback status shows the chargeback has been closed since the transaction has been identified as fraudulent. Moreover, PayU will cover the chargeback amount under the fraud liability program so the chargeback amount will be reversed back to the merchant account/will not debited from the merchants account. |

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