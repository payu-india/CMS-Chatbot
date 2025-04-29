---
title: Pre-Debit Notification API
excerpt: predebit
api:
  file: test_si_collection-9.json
  operationId: predebit
deprecated: false
hidden: false
metadata:
  title: Pre Debit Notification API
  description: >-
    Learn how to set up the Pre Debit Notification API using PayU Hosted
    Checkout. This API documentation provides detailed instructions for
    integrating PayU's pre debit notification feature, enabling timely alerts
    and notifications for upcoming transactions.
  keywords:
    - PayU Pre Debit Notification API
    - ' Pre Debit Notification API'
    - PayU pre-debit transaction notification API
    - ' PayU pre debit alerts API'
    - ' Send Notification Before SI'
    - ' SI Notification'
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: using-api-integration-recurring-payments
      title: Using API Integration
    - type: basic
      slug: customer-experience-and-workflow-recurring-payments
      title: Customer Experience and Workflow
---
The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer’s account as part of the registration. There is a mandate to send this notification to the customer at least 48 hours before the actual debit, that is, 48 hours before calling the Recurring API.

> ❗️ Reminder
> 
> - Check the mandate status before calling the **Pre-Debit Notification** API.
> - Unless the Pre-Debit notification API is implemented, the **Recurring Payment Transaction** API will not work, and you will not be able to charge the customer for the given billing cycle.
> - Pre-Debit notification is necessary only for Cards and UPI and works for only these two payment modes

### Environment

|                        |                                  |
| :--------------------- | :------------------------------- |
| Production Environment | <https://info.payu.in/merchant/> |
| Test Environment       | <https://test.payu.in/merchant/> |

<details><summary>Sample request</summary>

```curl
curl --location --request POST 'https://test.info.payu.in/merchant/postservice.php?form=2' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data
'key=JF****g&hash=9f5faabedb7f5d41f519db3a223cf5318ecc0b7e669f49e0a699d4c4879e1ccaed5b99f5cd
8be4f2cbddefe5272ec983abd8f38480d9c2609a29447f750a3158&command=check_action_status_txnid&var
1=7043873219"
```

</details>

<details>  <summary>Sample response</summary>

**Successful sceanario**

```plaintext
{
"status": 1,
"action": "MANDATE_PRE_DEBIT",
"message": "Request Processed Successfully",
“invoiceId”:” ADDA049409”
}
```

**Failure Scenarios**

-  Mandate is active in PayU DB and Pre-Debit gets declined from Bank/NPCI

```plaintext
{
"status":  “QC”   ----- >> Bank/NPCI Error Code
"action": "MANDATE_PRE_DEBIT",
"message": “MANDATE HAS BEEN REVOKED”. ---- >> Description against error code
}
```

Where, the **message** parameter in the response will display error code according to the scenario

- Mandate is already Paused/ Revoked in PayU DB

```plaintext
{
"status": 0,
"action": "MANDATE_PRE_DEBIT",
"message": "Mandate is not active” --- >> Description will change based on Scenario
}
```

Where, the **message** parameter in the response will display according to the scenario.

</details>

<details><summary>Response parameters</summary>

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Description",
    "0-0": "status",
    "0-1": "Status defines acknowledgment from PayU. Possible values are :  \n· **1**- This value indicates that pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete.  \n  \n· **0** – This value indicates pre-debit notification failed to get triggered and merchant should retry after some time to trigger the same or failed to get deleted in case of action delete.",
    "1-0": "action",
    "1-1": "Always returned as “MANDATE\\_PRE\\_DEBIT” to highlight the type of action.",
    "2-0": "message",
    "2-1": "Description of the pre-debit notification process",
    "3-0": "invoiceId  \n`only for cards`",
    "3-1": "This is an acknowledgment ID that a pre debit notification has been sent for processing.",
    "4-0": "invoiceStatus  \n`only for cards`",
    "4-1": "This is the status of the invoice whether it has been charged for recurring or not. Values can be:  \n  \n- Paid\n- Unpaid\n- DeletedSince these statuses come from a third-party vendor, so these can vary if there is an addition of new status at the vendor end",
    "5-0": "approvedStatus  \n`only for cards`",
    "5-1": "This is for cases where the transaction is above 15000 as RBI guideline says approval is required through AFA (Additional Factor authentication). Values can be:  \n  \n- Pending \n- Approved\n- Not\\_applicable  \n  Since these statuses come from third-party vendors, so these can vary if there is an addition of new status at the vendor end."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

## Request parameters

<details><summary>Reference information</summary>

<KeyHashForGeneralParametersDescription />

</details>

<details><summary>Response Parameters var1 JSON fields description</summary>

**Additional information**

[block:parameters]
{
  "data": {
    "h-0": "Parameter Name",
    "h-1": "Description",
    "0-0": "status",
    "0-1": "Status defines acknowledgment from PayU. Possible values are :  \n 1- This value indicates that pre-debit notification is triggered successfully for customer or deleted successfully in case of action delete.  \n· 0 – This value indicates pre-debit notification failed to get triggered and merchant should retry after some time to trigger the same or failed to get deleted in case of action delete.",
    "1-0": "action",
    "1-1": "Always returned as “MANDATE\\_PRE\\_DEBIT” to highlight the type of action.",
    "2-0": "message",
    "2-1": "Description of the pre-debit notification process",
    "3-0": "invoiceId",
    "3-1": "This is an acknowledgment ID that a pre debit notification has been sent for processing.",
    "4-0": "invoiceStatus",
    "4-1": "This is the status of the invoice whether it has been charged for recurring or not. Values can be:  \n  \n- Paid\n- Unpaid\n- Deleted  \n  Since these statuses come from a third-party vendor, so these can vary if there is an addition of new status at the vendor end",
    "5-0": "approvedStatus",
    "5-1": "This is for cases where the transaction is above 15000 as RBI guideline says approval is required through AFA (Additional Factor authentication) Values can be.:  \n  \n- Pending \n- Approved\n- Not\\_applicable  \n  Since these statuses come from third-party vendors, so these can vary if there is an addition of new status at the vendor end."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


**var1 JSON fields description**

The **var1** variable is in JSON format and comprises of the following parameters:

[block:parameters]
{
  "data": {
    "h-0": "JSON Field",
    "h-1": "Description",
    "0-0": "authpayuid  \n**mandatory**",
    "0-1": "The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. As explained earlier in the document, you need to map this value against customer profile at his end so that correct authPayuid will be passed in the request.",
    "1-0": "requestId  \n**mandatory**",
    "1-1": "Unique request value generated at merchant’s end to distinguish independent request call.",
    "2-0": "debitDate  \n**mandatory for cards and UPI**",
    "2-1": "This parameter contains the date of debit when the recurring would be charged by merchant.  \n\\*In UPI:\\*\\*  \n  \n- For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit.\n- For Daily and Adhoc frequency, the merchant must send the notification 24 hours before the debit. If the notification is sent after these durations, then the debit will fail.",
    "3-0": "invoiceDisplayNumber  \n**mandatory only for cards**",
    "3-1": "A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant’s panel to the customer. This same value needs to be sent in the recurring api also.",
    "4-0": "amount  \n**mandatory for cards and UPI**",
    "4-1": "The transaction amount which will be deducted from the customer’s payment instrument.  \n**For Cards:**  \n  \n- In case of Fixed billing plan, this amount should be same as  \n  billingAmount sent during Registration transaction.\n- In case of Adhoc billing plan, this amount should be equal to or lesser than billingAmount sent during the Registration transaction.  \n  **\\*Note**: The amount mentioned in the Pre-Debit notification API for UPI should be same as the next execution amount. Else, the next recurring execution request will fail.",
    "5-0": "action  \n**optional**",
    "5-1": "Any of the following actions can be performed:  \n\\* **Retrieve**: Query the status of the pre-debit notification. Only authpayuid and invoice display numbers are mandatory for this action.  \n\\* **Delete**: Delete the already generated pre debit. Only authpayuid and invoice display numbers are mandatory for this action."
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]


</details>

Use the following sample values while trying out the API:

**Example values for fields in var1**: 

- `authPayuId`: 10731087875
- `requestId`: 23123abut12123osd14
- `debitDate`: 2020-03-20
- `amount`: 100