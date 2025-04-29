---
title: '[Backup]Pre-Debit Notification API'
excerpt: predebit
api:
  file: test_si_collection-4.json
  operationId: predebit
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The **Pre-Debit Notification** API allows the merchants to send a pre-debit notification to the customer regarding an upcoming payment which will be deducted from the customer’s account as part of the registration. There is a mandate to send this notification to the customer at least 48 hours before the actual debit, that is, 48 hours before calling the Recurring API.

> 📘 Notes
> 
> - Unless the Pre-Debit notification interface is implemented, the Recurring API will not work, and you will not be able to charge the customer for the given billing cycle.
> - Pre-Debit notification is necessary only for Cards and UPI and works for only these two payment modes

### Environment

| Test Environment       | <https://test.payu.in/_payment>  |
| :--------------------- | :------------------------------- |
| Production Environment | <https://info.payu.in/merchant/> |

## Reference Information for Request Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Reference",
    "0-0": "key",
    "0-1": "For more information on how to generate the Key and Salt, refer to any of the following:  \n  \n- **Production**: [Generate Merchant Key and Salt](doc:generate-merchant-key-and-salt-on-payu-dashboard)  \n- **Test**: [Generate Test Merchant Key and Salt](doc:generate-test-merchant-key-and-salt)",
    "1-0": "hash",
    "1-1": "Hash logic for **\\_payment** API is:  \n`sha512(key\\|command\\|var1\\|salt) sha512\n`"
  },
  "cols": 2,
  "rows": 2,
  "align": [
    "left",
    "left"
  ]
}
[/block]

### var1 JSON Fields Description

For var1 JSON fields description, refer to [Additional Info. for Recurring Payment APIs](ref:additional-info-for-recurring-payment-apis).

## Response Parameters

For more information on response parameters, refer to [Additional Info. for Recurring Payment APIs](ref:additional-info-for-recurring-payment-apis).

## Request Parameters