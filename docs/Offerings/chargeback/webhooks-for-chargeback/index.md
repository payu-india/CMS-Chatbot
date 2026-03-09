---
title: Webhooks for Chargeback
deprecated: false
hidden: false
metadata:
  robots: index
---
Chargeback webhooks provide real-time notifications about important chargeback events, allowing merchants to stay updated and take necessary actions promptly. Webhooks are sent for the following events:

* A new chargeback is created
* Chargeback status is changed
* Chargeback amount is changed

To create webhooks using Dashboard, refer to <Anchor label="Configure Chargeback Webhook" target="_blank" href="https://docs.payu.in/docs/create-a-chargeback-webhook">Configure Chargeback Webhook</Anchor> > <Anchor label="Using Dashboard" target="_blank" href="https://docs.payu.in/docs/create-a-chargeback-webhook#using-dashboard">Using Dashboard</Anchor>. To update or delete an existing webhook, refer to any of the following:

* <Anchor label="Create a New Webhook" target="_blank" href="doc:create-a-new-webhook">Create a New Webhook</Anchor>
* <Anchor label="Update a Webhook" target="_blank" href="https://docs.payu.in/docs/update-a-webhook">Update a Webhook</Anchor>
* <Anchor label="Delete a Webhook" target="_blank" href="https://docs.payu.in/docs/delete-a-webhook-on-dashboard">Delete a Webhook</Anchor>

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

| Field       | Description                                                                                                                                                                                                      |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| type        | Type of transaction  and merchant must include the value as **payments** only.                                                                                                                                   |
| event       | Event type and the merchant must the include the value as **dispute** only.                                                                                                                                      |
| reason_code | Reason for the chargeback. For the list of reason codes, refer to [Reason codes for chargebacks](https://docs.payu.in/docs/webhooks-for-chargeback#reason-codes-for-chargebacks).                                |
| created_at  | Timestamp when the chargeback was created                                                                                                                                                                        |
| updated_at  | Timestamp when the chargeback was last updated                                                                                                                                                                   |
| mid         | PayU Merchant ID                                                                                                                                                                                                 |
| cb_id       | Chargeback ID                                                                                                                                                                                                    |
| txn_id      | This is the PayU transaction ID that is associated with the chargeback.                                                                                                                                          |
| cb_type     | Type of chargeback (for example, "RBI/BO", that is, Reserve Bank of India/Banking Operations)                                                                                                                    |
| due_date    | Due date for the chargeback resolution                                                                                                                                                                           |
| cb_amount   | Amount involved in the chargeback                                                                                                                                                                                |
| cb_status   | Current status of the chargeback. For the possible chargeback status values, refer to [cb_status field values description](https://docs.payu.in/docs/webhooks-for-chargeback#cb_status-field-values-description) |

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

<Callout icon="📘" theme="info">
  **Chargeback reasons**: For chargeback reasons provided by customers while raising chargeback, refer to [Chargeback Reasons](doc:chargeback-reasons).
</Callout>

## Troubleshooting

If you're not receiving webhook notifications:

* Verify that your webhook URL is correct and accessible from the internet
* Check that your endpoint returns a 200 OK response to acknowledge receipt of the webhook
* Ensure your webhook is set to "Active" in the configuration
* Contact PayU support if you continue to experience issues

## FAQs

#### On new status dispute, is the amount already booked from merchant account?  OR **When is the amount charged from the merchant account?** OR **Does Closed Customer Favour mean the amount is debited from merchant account?**

Dependent on the merchant risk score & contract, Merchant accounts are marked as Upfront-Debit or No-Upfront-Debit. So when a new dispute is raised:

* For upfront-debit, the dispute amount will be debited when the dispute (in new Status) is created.
* For no-upfront-debit, the dispute amount will be debited only after the dispute is closed in the customer's favor.

#### Do Closed in Merchant Favour / Closed under Fraud Liability mean the amount is reversed to merchant account?

If the amount is upfront debit merchant then the money will be reversed. Else there is no debit on the merchant account.
