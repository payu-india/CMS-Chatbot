---
name: s2s Request params
---
### Body

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "accountId  \n `mandatory`",
    "0-1": "`String` The merchant key provided by PayU during onboarding.",
    "0-2": "MERCHANT123",
    "1-0": "referenceId  \n `mandatory`",
    "1-1": "`String` Reference ID for transaction tracking and this must be unique for every transaction.",
    "1-2": "REF123456",
    "2-0": "amount  \n `optional`",
    "2-1": "`String` Amount of the transaction.  \n**Note**: This value will not be considered as the transaction. Only the details in the `order.paymentChargeSpecificationparameter.price`field will be considered.",
    "2-2": "1000",
    "3-0": "currency  \n `mandatory`",
    "3-1": "`String` Currency of the transaction (e.g., INR).",
    "3-2": "INR",
    "4-0": "paymentMethod  \n `mandatory`",
    "4-1": "`Object` Details about the payment method used. For more information, refer to [paymentMethod object fields description](#paymentmethod-object-fields-description).",
    "4-2": "",
    "5-0": "order  \n `mandatory`",
    "5-1": "`Object` Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)",
    "5-2": "",
    "6-0": "additionalInfo  \n `mandatory`",
    "6-1": "`Object` Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description)",
    "6-2": "",
    "7-0": "callBackActions  \n `mandatory`",
    "7-1": "`Object` Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to [callbackActions object fields description](#callbackactions-object-fields-description)",
    "7-2": " ",
    "8-0": "billingDetails `mandatory`",
    "8-1": "`Object` Billing details of the customer including name, address, phone number, email, etc. For more information, refer to [billingDetails object field descriptions](#billingdetails-object-field-descriptions).",
    "8-2": "",
    "9-0": "deviceInfo  \n`mandatory for S2S`",
    "9-1": "`Object`Device info of the customer.  For more information, refer to[ deviceInfo object field descriptions](#deviceinfo-object-field-descriptions)  .",
    "9-2": ""
  },
  "cols": 3,
  "rows": 10,
  "align": [
    null,
    null,
    null
  ]
}
[/block]