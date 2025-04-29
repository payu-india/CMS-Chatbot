---
title: SI Parameter JSON Details
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
The description for the **si\_details** parameter (JSON format):

[block:parameters]
{
  "data": {
    "h-0": "**JSON Field**",
    "h-1": "**Description**",
    "h-2": "**Example**",
    "0-0": "billingCycle  \n**mandatory**",
    "0-1": "Billing Cycle defines whether the customer needs to be charged over Daily, Weekly basis, Monthly or Yearly basis or one time.  ",
    "0-2": "ONCE",
    "1-0": "billingInterval  \n**mandatory**",
    "1-1": "Billing Interval is closely coupled with the **billingCycle** field and denotes at what frequency, the subscription plan needs to be executed. For monthly subscriptions, parameter values need to be sent in the request are:  \n_ billingCycle = MONTHLY  \n_ billingInterval = 1  \nSimilarly, by keeping the following values, customer will be charged once in every 3 days:  \n_ billingCycle = DAILY  \n_ billingInterval = 3",
    "1-2": "_ billingCycle = MONTHLY  \n_ billingInterval = 1 ",
    "2-0": "billingAmount  \n**mandatory**",
    "2-1": "The billing amount is passed in XX. XX format.  \nIn use cases where **billingCycle = ADHOC**, amount passed is treated as maximum amount since billing amount and billing cycle varies as per the usage of the subscription service.  In this case, the merchant is free to charge any amount for customer up to the amount specified in the defined subscription call.  For UPI, **billingAmount** should not be more than INR 15000 as it is the maximum limit allowed for UPI currently.",
    "2-2": "INR 2000",
    "3-0": "billingCurrency  \n**mandatory**",
    "3-1": "This field must be passed as “INR” .",
    "3-2": "INR",
    "4-0": "paymentStartDate  \n**mandatory**",
    "4-1": "The start date of the billing plan is specified in this field with the YYYY-MM-DD format.  \n**Note**: All the subsequent recurring transactions will be processed from this date onwards as per **billingCycle** and **billingInterval** fields combination. This date acts as reference point for recurring payments. **Note**: In case of UPI, send the current date here and any other value will be ignored.",
    "4-2": "2022-02-14",
    "5-0": "paymentEndDate  \n**mandatory**",
    "5-1": "The end date of the billing plan is specified in this field with the YYYY-MM-DD format.  \n**Note**: Pass the correct end date to PayU. Depending upon start date and end date, number of payment iterations are internally calculated and same information is passed to acquirers or banks.",
    "5-2": "2023-01-14",
    "6-0": "siTokenRequestor  \n**mandatory for saved cards**",
    "6-1": "This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of susbcription set. You can include any of the following values::  \n_ **1** : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.  \n_ **2**: PayU will do the authorization on plain card. Later, the same response will be shared to merchant. ",
    "6-2": "1",
    "7-0": "remarks  \n**optional**",
    "7-1": "This field is used to provide remarks on PSP applications during the registration transaction of UPI.  For cards and Net Banking, this parameter has no significance.  Character limit = 50.   \n**Note**: This field is applicable only for UPI.",
    "7-2": "Subscription for a year",
    "8-0": "billingLimit  \n**optional**",
    "8-1": "For UPI, this field is used to decide the period corresponding which the debit from the mandate recurring date can happen and this mandate registration date is confirmed during registration transaction of UPI.  \n **Note**: This field is applicable only for UPI.  \nThe possible values are:  \n_  **ON** = Use this parameter to deduct on a specific date  \n_  **BEFORE** = Use this parameter to deduct before and on a specific date  \n\\*  **AFTER** = Use this parameter to After and on the specific date  \n  \n**Note**: If no value is passed, ‘AFTER’ is considered by default.",
    "8-2": "ON = 2022-02-20",
    "9-0": "billingRule  \n**optional**",
    "9-1": "For UPI, this field is used to decide the limitation on the amount of recurring debit against the mandate amount which is set during registration transaction of UPI.  \n**Note**: This field is applicable only for UPI.  \nThe possible values are:  \n_  **MAX** = This is the maximum amount that a merchant can debit, that is, merchant can debit lesser or equal to this amount for a recurring transaction.  \n_  **EXACT**= This the exact amount that a merchant can debit in recurring debits.  \n  \nNote: If no value is passed, ‘MAX’ is considered by default.",
    "9-2": "MAX = 5000",
    "10-0": "billingDate  \n**optional**",
    "10-1": "**Applicable for UPI only**: This field is used to decide the date/day, basis which the recurring debit should happen. This can be ignored and the debit will happen as per the start date in every cycle.",
    "10-2": "FORTNIGHTLY = 7",
    "11-0": "authpayuid  \n**mandatory for modifying subscription with cards**",
    "11-1": "This field is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount.",
    "11-2": " ",
    "12-0": "action  \n**mandatory for cards**",
    "12-1": "This field is used to modify or delete an existing subscription.",
    "12-2": "modify  \nor  \ndelete"
  },
  "cols": 3,
  "rows": 13,
  "align": [
    null,
    null,
    null
  ]
}
[/block]


> 📘 Recurrence Rule for billingDate parameter
> 
> For WEEKLY
> 
> If the start date (day) = Monday, Rule  
> Value = 1, for Tuesday it is 2.........for  
> Sunday it is 7.
> 
> For FORTNIGHTLY
> 
> For Start Date (1st – 15th) Rule Value  
> = Start Date
> 
> For Start Date (16th – 31th) Rule  
> Value = Start Date – 15
> 
> For MONTHLY and greater than Monthly  
> frequencies
> 
> Rule Value = Start Date
> 
> Possible values : Numeric values ( 1- 31)
> 
> For WEEKLY frequency: 
> 
> If the start date (day) = Monday, rule value = 1.
> 
> If the start date (day) = Tuesday, it is 2.
> 
> ...
> 
> ...
> 
> If the start date (day) = Sunday, it is 7.
> 
> For FORTNIGHTLY frequency
> 
> For Start Date (1st – 15th) Rule Value = Start Date
> 
> For Start Date (16th – 31th) Rule Value = Start Date – 15
> 
> For MONTHLY and greater than monthly frequency
> 
> Rule Value = Start Date, where the possible value is a numeric value between 1- 31

## si\_details Parameter Example Values

For a yearly plan starting from 1st January 2019, having a monthly billing amount INR 100, the plan details:

```plaintext
{“billingAmount”: “100.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billingInterval”: 1,”paymentStartDate”: “2019-09-01″,”paymentEndDate”: “2019-12-01”}
```

In this example, the number of charges executed over recurring against the customer’s payment instrument will be 12, once per month.

For a quarterly plan starting from 20th September 2019 for the next two years, having a billing amount of 5000 INR:

```plaintext
{“billingAmount”: “5000.00”,”billingCurrency”: “INR”,”billingCycle”: “MONTHLY”,”billing interval”: 3,”paymentStartDate”: “2019-09-20″,”paymentEndDate”: “2021-09-20”}
```

In this example, the number of charges executed over recurring against the customer’s payment instrument will be 9, once per 3 months.

## Billing Cycle

The description of the **billingCycle** parameter:

[block:parameters]
{
  "data": {
    "h-0": "**Billing Cycle**",
    "h-1": "**Description**",
    "0-0": "ONCE",
    "0-1": "Used when a merchant wants to execute Split / Partial payment use cases where the partial amount is paid upfront during the Consent transaction and remaining amount needs to be paid on later.  \nWEEKLY is used if the merchant wants to run a bi-weekly subscription then values will be similar to the following, so the customer will be charged once in every 2 weeks.:",
    "1-0": "ADHOC",
    "1-1": "Used in use cases such as post-paid bills where there is no definite billing cycle and billing amount.  \n\\* **billingInterval** = Billing Interval is closely coupled with the value of “billingCycle” and denotes at what frequency, the subscription plan needs to be executed.",
    "2-0": "MONTHLY",
    "2-1": "Used for monthly subscriptions, parameter values that need to be sent in request are:  \n_  billingCycle = MONTHLY   \n_  billingInterval = 1",
    "3-0": "YEARLY",
    "3-1": "Used for yearly subscriptions. parameter values that need to be sent in request are:  \n_  billingCycle = YEARLY  \n_  billingInterval = 1",
    "4-0": "WEEKLY",
    "4-1": "Used for weekly subscriptions. Use the following values to charge the customer once every week:  \n_  billingCycle = WEEKLY  \n_  billingInterval = 1",
    "5-0": "DAILY",
    "5-1": "Used for daily subscriptions.  \nUse the following values to charge the customer once in every 3 days:  \n_  billingCycle = DAILY   \n_  billingInterval = 3"
  },
  "cols": 2,
  "rows": 6,
  "align": [
    null,
    null
  ]
}
[/block]