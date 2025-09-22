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

```swift Swift
//Swift
let siParam = PayUSIParams(billingAmount: <String>,
paymentStartDate: <Date>,
paymentEndDate: <Date>,
billingCycle: <PayUBillingCycle>,
billingInterval: <NSNumber>,
billingLimit: <PayuBillingLimit>,
billingRule: <PayuBillingRule>)
```
```objectivec Objective-C
/* Objective C */
PayUSIParams *siParam = [[PayUSIParams alloc] initWithBillingAmount:<#(NSString * _Nonnull)#>                                                   paymentStartDate:<#(NSDate * _Nonnull)#>                                                     
paymentEndDate:<#(NSDate * _Nonnull)#>                                                       billingCycle:<#(enum PayUBillingCycle)#>                                                    billingInterval:<#(NSNumber * _Nonnull)#>];
```

***

## Step 2: Post parameters

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>

      </th>

      <th>

      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        EnableSI
        `mandatory for SI`
      </td>

      <td>
        `Boolean`: This flag must contain any of the following to indicate if SI or subscriptions is required for the payment link:

        1: The request is eligible for SI

        0: The request is eligible for SI

        * *Note**: If EnableSI=1 in the JSON, the values for all other fields (mandatory) in this JSON must be posted
      </td>
    </tr>

    <tr>
      <td>
        billingAmount
        `mandatory for SI`
      </td>

      <td>
        `String` Contains the billing amount
      </td>
    </tr>

    <tr>
      <td>
        billingCycle
        `mandatory for SI`
      </td>

      <td>
        `String` Billing Cycle defines whether the customer needs to be charged on a Daily, Weekly basis, Monthly, or Yearly basis or one time.
      </td>
    </tr>

    <tr>
      <td>
        billingInterval
        `mandatory for SI`
      </td>

      <td>
        `NSNumber` Billing Interval is closely coupled with the value of “`billingCycle`” and denotes at what frequency, the subscription plan needs to be executed.
      </td>
    </tr>

    <tr>
      <td>
        billingLimit
        `mandatory for SI`
      </td>

      <td>
        `String` The possible values for this parameter are:

        -`ON` = On the specific date

        * `BEFORE` = Before and on the specific date
        * `AFTER` = After and on the specific date
          If no value is passed, then by default this is considered as ‘AFTER’
      </td>
    </tr>

    <tr>
      <td>
        billingRule
        `mandatory for SI`
      </td>

      <td>
        String
        `MAX` = Maximum amount. Lesser than this or equal to this amount can be debited in recurring debits
        `EXACT`= Exact this amount can be debited in recurring debits Note: If no value is passed, then by default this is considered as ‘MAX’.
      </td>
    </tr>

    <tr>
      <td>
        billingCurrency
        `mandatory for SI`
      </td>

      <td>
        `String` Currency in which the amount needs to be collected. By default, it is 'INR'.
      </td>
    </tr>

    <tr>
      <td>
        paymentStartDate
        `mandatory`
      </td>

      <td>
        `Date` Start date of recurring payment.
      </td>
    </tr>

    <tr>
      <td>
        paymentEndDate
        `mandatory`
      </td>

      <td>
        `Date` End Date of recurring payment
      </td>
    </tr>

    <tr>
      <td>
        freeTrial
        `optional`
      </td>

      <td>
        `Boolean` This flag is to indicate any of the following:

        0: This is not a trial subscription. If this parameter is not posted, will be assumed as 0.

        1: This is a trial subscription.
      </td>
    </tr>

    <tr>
      <td>
        isPreAuthTxn
        `mandatory for UPI OTM`
      </td>

      <td>
        `Boolean` This flag is to indicate any of the following:

        0: This is normal SI transaction.

        1: This is a UPI One time mandate transaction.
      </td>
    </tr>
  </tbody>
</Table>
