---
title: Manage Invoice APIs
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
  pages:
    - type: basic
      slug: building-billing-experience-with-zion
      title: Zion Workflow
---
The following APIs are used to manage invoice:

- [Get Invoice API](ref:get-invoice-interfaces-api-zion)
- [Create Invoice API](ref:create-invoice-api-zion)

## Understanding Invoice

Charge requests triggered automatically by Zion against customer’s preferred payment instrument on the billing date are known as invoices. For every plan associated with subscription, Invoices are triggered specific to individual plans and run independently as per the schedule mentioned for that plan.  
This gives lot of flexibility in combining different use cases of billing and create a scalable solution.

```
{
  "subscriptionPlans": [
    {
      "planName": "Premium",
      "totalCount": 12,
      "startDate": "2019-04-01T00:00:00.000Z",
      "billingInterval": 1,
      "billingCycle": "MONTHLY",
      "amount": {
        "value": 200,
        "currency": "INR"
      }
    },
    {
      "planName": "Saver",
      "totalCount": 2,
      "startDate": "2019-05-01T00:00:00.000Z",
      "billingInterval": 2,
      "billingCycle": "MONTHLY",
      "amount": {
        "value": 50,
        "currency": "INR"
      }
    }
  ]
}
```

Plan “_**Saver**_” will start on 1st of May 2019 and trigger 1st invoice or charge worth 50 Rs against customer’s payment instrument. No intervention is required from merchant as well as customer because payment will happen in the background between Customer’s bank and Zion. On 1st of June 2019, another invoice will be triggered worth 50 Rs and then plan “_**Saver**_” will be marked as completed since total count specified was 2.

Plan “_**Premium**_” will start on 1st of April 2019 and triggers 1st invoice or charge worth 200 Rs against customer’s payment instrument. This will continue every month for 200 Rs each for total 12 iterations. On 1st March 2020, it will have its final 12th invoice which will charge customer one last time for 200 Rs and then plan will be stopped automatically

Since no active plan is now present, Subscription will be also marked as “_**Completed**_” and no further invoices are generated for given subscription. So, in total, there will be 14 Invoices generated for given subscription (2 for “Saver” + 12 for “Premium”) before subscription is completed.

As everything is triggered from Zion’s end, merchant must provide a webhook (HTTPS URL from merchant system) where details of Invoices generated are posted back as and when charge requests are made against customer’s payment instruments in terms of notification events mentioned below -

- [Invoice Due](#invoice-due)
- [Invoice Paid](#invoice-paid)
- [Invoice Failed](#invoice-failed)

### Invoice Due 

- Zion looks at start date of every plan associated with the subscription. Say billing date is 5th Oct 2018, then Zion generates an Invoice on 4th Oct 2018 and triggers an event denoted as _**INVOICE\_DUE\_HTTP**_ over merchant’s webhook
- This event is important in case where merchant wants to communicate customer beforehand that payment instrument will be charged on next day

### Invoice Paid

▪ On 5th of Oct 2018, Zion tries to charge customer’s payment instrument as specified in the Plan.

- If payment is successful, then money will be debited from customer’s account. At this step, _**INVOICE\_PAID\_HTTP**_ event is triggered as per Zion terminology.
- If Zion is unable to charge customer’s payment instrument on 5th Oct, it will retry for next 3 days. So, merchant may get this notification for said invoice anywhere between 5th till 8th Oct

### Invoice Failed

- After executing all the retry options, if Zion is still unable to charge customer then

_**INVOICE\_FAILED\_HTTP**_ event is trigged

- Merchant then needs to communicate with customer and request him to make payment manually

> 📘 Notes:
> 
> - It is worth to note that whenever Zion trigger event and connects with merchant’s webhook, it ensures that merchant webhook returns HTTP 200 status. If Zion is unable to receive the same, it will retry the notification 3 more times by assuming that merchant is unable to receive the notification.
> - It is advised that merchant should have unique check for received notification to avoid any data duplication.

### Invoice notification object

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "0-0": "merchantId",
    "0-1": "Merchant key echoed back in the notification",
    "1-0": "subscriptionId",
    "1-1": "Subscription id of the customer echoed back in the notification",
    "2-0": "planId",
    "2-1": "Plan Id associated with the subscription against which invoice is generated and customer account is getting charged",
    "3-0": "invoiceId",
    "3-1": "Invoice Id for the given subscription id and plan id combination. Please note that if there are multiple plan ids associated with single subscription id, then for every plan separate invoice will be generated. So, it is important for merchant to understand which invoice belongs to which plan.",
    "4-0": "authRefId",
    "4-1": "This is nothing but mihpayId of consent transaction id generated by PayU and returned to merchant as a part of success response of the consent transaction.",
    "5-0": "amount",
    "5-1": "Amount node which denotes how much amount charged to the customer",
    "6-0": "value",
    "6-1": "Billing Amount value charged to the customer",
    "7-0": "currency",
    "7-1": "Billing Amount currency charged to the customer",
    "8-0": "paymentStatus",
    "8-1": "Status of the payment or auto debit initiated on customer’s account once invoice is generated and executed. The possible values are:  \n- Due  \n- Paid  \n- Failed",
    "9-0": "subscriberEmail",
    "9-1": "Email ID of the subscriber echoed back in the notification",
    "10-0": "subscriberMobile",
    "10-1": "Mobile id of the subscriber echoed back in the notification",
    "11-0": "notificationType",
    "11-1": "Notification type denotes different events triggered by Zion at different stages of Subscription life cycle. The possible values are:  \n- INVOICE\\_DUE\\_HTTP  \n- INVOICE\\_PAID\\_HTTP  \n- INVOICE\\_FAILED\\_HTTP",
    "12-0": "customParameter",
    "12-1": "Key value pairs associated for extra information with subscription. These details will be returned to merchant in webhook notification against every payment executed from Zion so that merchant can effectively map payment response with its own system."
  },
  "cols": 2,
  "rows": 13,
  "align": [
    null,
    null
  ]
}
[/block]


## Sample notification format

### Event for invoice due

```
{
  "merchantId": "YQeVda",
  "subscriptionId": "5bc35da13114ad3b044eb016",
  "invoiceId": "5c99f0803114ad37b5193c5b",
  "planId": "5bacd71cd3428429e50d922b",
  "authRefId": "1234321",
  "amount": {
    "value": "200.00",
    "currency": "INR"
  },
  "paymentStatus": "Due",
  "subscriberEmail": "pacemaker@gmail.com",
  "subscriberMobile": "9711146946",
  "notificationType": "INVOICE_DUE_HTTP",
  "customParameter": {
    "Policynumber": "12743123111"
  }
}
```

### Event for invoice paid

```
{
"merchantId": "YQeVda",
"subscriptionId": "5bc35da13114ad3b044eb016", "invoiceId": "5c99f0803114ad37b5193c5b", "planId": "5bacd71cd3428429e50d922b", "authRefId": "1234321",
"amount": {
"value": "200.00",
"currency": "INR"
},
"paymentStatus": "Paid",
"subscriberEmail": "pacemaker@gmail.com", "subscriberMobile": "9711146946", "notificationType": "INVOICE_PAID_HTTP", "customParameter": {
"Policynumber": "12743123111"
}
}
```

### Event for invoice failed

```
{
  "merchantId": "YQeVda",
  "subscriptionId": "5bc35da13114ad3b044eb016",
  "invoiceId": "5c99f0803114ad37b5193c5b",
  "planId": "5bacd71cd3428429e50d922b",
  "authRefId": "1234321",
  "amount": {
    "value": "200.00",
    "currency": "INR"
  },
  "paymentStatus": "Failed",
  "subscriberEmail": "pacemaker@gmail.com",
  "subscriberMobile": "9711146946",
  "notificationType": "INVOICE_FAILED_HTTP",
  "customParameter": {
    "Policynumber": "12743123111"
  }
}
```