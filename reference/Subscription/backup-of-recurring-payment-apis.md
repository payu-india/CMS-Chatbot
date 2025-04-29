---
title: Backup of Recurring Payment APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# PreDebit Notification API



## var1 JSON Fields Description

The **var1** variable is in JSON format and comprises of the following parameters:

[block:parameters]
{
  "data": {
    "h-0": "**JSON Field**",
    "h-1": "**Description**",
    "0-0": "authpayuid  \n**mandatory**",
    "0-1": "The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. As explained earlier in the document, you need to map this value against customer profile at his end so that correct authPayuid will be passed in the request.",
    "1-0": "requestId  \n**mandatory**",
    "1-1": "Unique request value generated at merchant’s end to distinguish independent request call.",
    "2-0": "debitDate  \n**mandatory for cards and UPI**",
    "2-1": "This parameter contains the date of debit when the recurring would be charged by merchant.  \n\\*In UPI:\\*\\*  \n- For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit.  \n- For Daily and Adhoc frequency, the merchant must send the notification 24 hours before the debit. If the notification is sent after these durations, then the debit will fail.",
    "3-0": "invoiceDisplayNumber  \n**mandatory only for cards**",
    "3-1": "A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant’s panel to the customer. This same value needs to be sent in the recurring api also.",
    "4-0": "amount  \n**mandatory for cards and UPI**",
    "4-1": "The transaction amount which will be deducted from the customer’s payment instrument.  \n**For Cards:**  \n- In case of Fixed billing plan, this amount should be same as  \n  billingAmount sent during Registration transaction.  \n- In case of Adhoc billing plan, this amount should be equal to or lesser than billingAmount sent during the Registration transaction.  \n**\\*Note**: The amount mentioned in the Pre-Debit notification API for UPI should be same as the next execution amount. Else, the next recurring execution request will fail.",
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

## Response Parameters

For more information on response parameters, refer to [Additional Info. for Recurring Payment APIs](ref:additional-info-for-recurring-payment-apis).

## Request Parameters