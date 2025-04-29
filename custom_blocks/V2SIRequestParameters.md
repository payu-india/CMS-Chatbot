---
name: v2 SI Request Parameters
---
### Body

[block:parameters]
{
  "data": {
    "h-0": "**Parameter**",
    "h-1": "**Description**",
    "0-0": "accountId  \n `mandatory`",
    "0-1": "`String`This must contain the key provided by PayU while onboarding.",
    "1-0": "referenceId  \n `mandatory`",
    "1-1": "`String`Reference ID for transaction tracking and this must be unique for every transaction.",
    "2-0": "amount  \n `optional`",
    "2-1": "`String`Amount of the transaction.  \n**Note**: This value will not be considered as the transaction. Only the details in the ` order.paymentChargeSpecificationparameter` field will be considered.",
    "3-0": "currency  \n `mandatory`",
    "3-1": "`String`Currency of the transaction (e.g., INR).  By default, **INR** is posted.",
    "4-0": "order  \n `mandatory`",
    "4-1": "`JSON Object`Details about the transaction order including product information, ordered items, user defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)",
    "5-0": "additionalInfo  \n `mandatory`",
    "5-1": "`JSON Object`Additional information including enforced payment methods and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description).  \n**Note**: The `txnFlow` field in this JSON object must be set to **nonseamless**.",
    "6-0": "callBackActions  \n `mandatory`",
    "6-1": "`JSON Object`Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc.  For more information, refer to[ callbackActions object fields description](#callbackactions-object-fields-description)",
    "7-0": "billingDetails  \n `mandatory`",
    "7-1": "`JSON Object`Billing details of the customer including name, address, phone number, email, etc.  For more information, refer to[ billingDetails object fields descriptions](#billingdetails-object-fields-descriptions).",
    "8-0": "siDetails",
    "8-1": "`JSON Object` Subscription or SI details for the consent transaction. For more information, refer to[ siDetails object fields description](#sidetails-object-fields-description)."
  },
  "cols": 2,
  "rows": 9,
  "align": [
    null,
    null
  ]
}
[/block]