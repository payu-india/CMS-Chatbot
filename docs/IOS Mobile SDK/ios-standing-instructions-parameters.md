---
title: PayU Standing Instructions Parameters
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
## Step 1: Create a SI parameters object

Create a class PayUSIParams object using the code similar to the following:

```Text Swift
//Swift
let siParam = PayUSIParams(billingAmount: <String>,
paymentStartDate: <Date>,
paymentEndDate: <Date>,
billingCycle: <PayUBillingCycle>,
billingInterval: <NSNumber>,
billingLimit: <PayuBillingLimit>,
billingRule: <PayuBillingRule>)
```
```Text Objective-C
/* Objective C */
PayUSIParams *siParam = [[PayUSIParams alloc] initWithBillingAmount:<#(NSString * _Nonnull)#>                                                   paymentStartDate:<#(NSDate * _Nonnull)#>                                                     
paymentEndDate:<#(NSDate * _Nonnull)#>                                                       billingCycle:<#(enum PayUBillingCycle)#>                                                    billingInterval:<#(NSNumber * _Nonnull)#>];
```

***

## Step 2: Post parameters

[block:parameters]
{
  "data": {
    "h-0": "",
    "h-1": "",
    "0-0": "EnableSI  \n`mandatory for SI`",
    "0-1": "`Boolean`: This flag must contain any of the following to indicate if SI or subscriptions is required for the payment link:  \n  \n1: The request is eligible for SI  \n  \n0: The request is eligible for SI  \n  \n**Note**: If EnableSI=1 in the JSON, the values for all other fields (mandatory) in this JSON must be posted",
    "1-0": "billingAmount  \n`mandatory for SI`",
    "1-1": "`String` Contains the billing amount",
    "2-0": "billingCycle  \n`mandatory for SI`",
    "2-1": "`String` Billing Cycle defines whether the customer needs to be charged on a Daily, Weekly basis, Monthly, or Yearly basis or one time.",
    "3-0": "billingInterval  \n`mandatory for SI`",
    "3-1": "`NSNumber` Billing Interval is closely coupled with the value of “`billingCycle`” and denotes at what frequency, the subscription plan needs to be executed.",
    "4-0": "billingLimit  \n`mandatory for SI`",
    "4-1": "`String` The possible values for this parameter are:  \n  \n-`ON` = On the specific date  \n  \n- `BEFORE` = Before and on the specific date\n- `AFTER` = After and on the specific date  \n  If no value is passed, then by default this is considered as ‘AFTER’",
    "5-0": "billingRule  \n`mandatory for SI`",
    "5-1": "String  \n`MAX` = Maximum amount. Lesser than this or equal to this amount can be debited in recurring debits  \n`EXACT`= Exact this amount can be debited in recurring debits Note: If no value is passed, then by default this is considered as ‘MAX’.",
    "6-0": "billingCurrency  \n`mandatory for SI`",
    "6-1": "`String` Currency in which the amount needs to be collected. By default, it is 'INR'.",
    "7-0": "paymentStartDate  \n`mandatory`",
    "7-1": "`Date` Start date of recurring payment.",
    "8-0": "paymentEndDate  \n`mandatory`",
    "8-1": "`Date` End Date of recurring payment",
    "9-0": "freeTrial  \n`optional`",
    "9-1": "`Boolean` This flag is to indicate any of the following:  \n  \n0: This is not a trial subscription. If this parameter is not posted, will be assumed as 0.  \n  \n1: This is a trial subscription.",
    "10-0": "isPreAuthTxn  \n`mandatory for UPI OTM`",
    "10-1": "`Boolean` This flag is to indicate any of the following:  \n  \n0: This is normal SI transaction.  \n  \n1: This is a UPI One time mandate transaction."
  },
  "cols": 2,
  "rows": 11,
  "align": [
    "left",
    "left"
  ]
}
[/block]