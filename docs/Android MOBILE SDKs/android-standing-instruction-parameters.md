---
title: Standing Instruction Parameter Details
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
## Step 1: Create a SI Parameters Object

Create a class PayUSIParams object using the code similar to the following

```Text Java
PayUSIParams siDetails  = new PayUSIParams.Builder()
.setIsFreeTrial(true) //set it to true for free trial. Default value is false 
.setBillingAmount("1.0")
.setBillingCycle(PayUBillingCycle.ONCE)     
.setBillingCurrency("INR")
.setBillingInterval(1)
.setPaymentStartDate("2021-12-24")
.setPaymentEndDate("2021-12-31")
.setBillingRule(PayuBillingRule.MAX)
.setBillingLimit(PayuBillingLimit.ON)
.setRemarks("SI Txn")
.build();
```
```Text Kotlin
val siDetails  = PayUSIParams.Builder()
                .setIsFreeTrial(true) //set it to true for free trial. Default value is false
                .setBillingAmount("1.0")
                .setBillingCycle(PayUBillingCycle.ONCE)     
                .setBillingCurrency("INR")
                .setBillingInterval(1)
                .setPaymentStartDate("2021-12-24")
                .setPaymentEndDate("2021-12-31")
                .setBillingRule(PayuBillingRule.MAX)
                .setBillingLimit(PayuBillingLimit.ON)
                .setRemarks("SI Txn")
                .build()
```

## Step 2: Post Parameters

[block:parameters]
{
  "data": {
    "h-0": "Parameter",
    "h-1": "Description",
    "h-2": "Example",
    "0-0": "billingAmount  \n`mandatory`",
    "0-1": "`String` Contains the billing amount",
    "0-2": "100.00",
    "1-0": "billingCycle  \n`mandatory`",
    "1-1": "`String` Billing Cycle defines whether customer needs to be charged over Daily, Weekly basis, Monthly or Yearly basis or one time,",
    "1-2": "MONTHLY",
    "2-0": "billingInterval  \n`mandatory`",
    "2-1": "`Integer` Billing Interval is closely coupled with value of “billingCycle” and denotes at what frequency, the subscription plan needs to be executed.",
    "2-2": "1",
    "3-0": "billingLimit  \n`mandatory`",
    "3-1": "`String` The possible values for this parameter are:  \n  \n- ON = On the specific date  \n- BEFORE = Before and on the specific date  \n- AFTER = After and on the specific date  \n  If no value is passed, then by default this is considered as ‘AFTER’",
    "3-2": "ON",
    "4-0": "billingRule  \n`mandatory`",
    "4-1": "`String`  \n  \nMAX = Maximum amount. Lesser than this or equal to this amount can be debited in recurring debits  \n  \nEXACT= Exact to this amount can be debited in recurring debits  \n`Note`: If no value is passed, then by default this is considered as ‘MAX’",
    "4-2": "MAX",
    "5-0": "billingCurrency  \n`mandatory`",
    "5-1": "`String` Currency in which the amount needs to be collected. By default, it is 'INR'.",
    "5-2": "INR",
    "6-0": "paymentStartDate  \n`mandatory`",
    "6-1": "`Date` Start date of recurring payment",
    "6-2": "2022-02-14",
    "7-0": "paymentEndDate  \n`mandatory`",
    "7-1": "`Date` End Date of recurring payment",
    "7-2": "2023-01-14",
    "8-0": "freeTrial `optional`",
    "8-1": "`Boolean` This flag is to indicate any of the following:  \n  \n0: This is not a trial subscription. If this parameter is not posted, will be assumed as 0.  \n  \n1: This is a trial subscription.",
    "8-2": "1"
  },
  "cols": 3,
  "rows": 9,
  "align": [
    "left",
    "left",
    "left"
  ]
}
[/block]