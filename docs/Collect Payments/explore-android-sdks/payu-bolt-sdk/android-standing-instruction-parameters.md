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

```java Java
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
```kotlin Kotlin
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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Parameter
      </th>

      <th>
        Description
      </th>

      <th>
        Example
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        billingAmount
        `mandatory`
      </td>

      <td>
        `String` Contains the billing amount
      </td>

      <td>
        100.00
      </td>
    </tr>

    <tr>
      <td>
        billingCycle
        `mandatory`
      </td>

      <td>
        `String` Billing Cycle defines whether customer needs to be charged over Daily, Weekly basis, Monthly or Yearly basis or one time,
      </td>

      <td>
        MONTHLY
      </td>
    </tr>

    <tr>
      <td>
        billingInterval
        `mandatory`
      </td>

      <td>
        `Integer` Billing Interval is closely coupled with value of “billingCycle” and denotes at what frequency, the subscription plan needs to be executed.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        billingLimit
        `mandatory`
      </td>

      <td>
        `String` The possible values for this parameter are:

        * ON = On the specific date
        * BEFORE = Before and on the specific date
        * AFTER = After and on the specific date
          If no value is passed, then by default this is considered as ‘AFTER’
      </td>

      <td>
        ON
      </td>
    </tr>

    <tr>
      <td>
        billingRule
        `mandatory`
      </td>

      <td>
        `String`

        MAX = Maximum amount. Lesser than this or equal to this amount can be debited in recurring debits

        EXACT= Exact to this amount can be debited in recurring debits
        `Note`: If no value is passed, then by default this is considered as ‘MAX’
      </td>

      <td>
        MAX
      </td>
    </tr>

    <tr>
      <td>
        billingCurrency
        `mandatory`
      </td>

      <td>
        `String` Currency in which the amount needs to be collected. By default, it is 'INR'.
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        paymentStartDate
        `mandatory`
      </td>

      <td>
        `Date` Start date of recurring payment
      </td>

      <td>
        2022-02-14
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

      <td>
        2023-01-14
      </td>
    </tr>

    <tr>
      <td>
        freeTrial `optional`
      </td>

      <td>
        `Boolean` This flag is to indicate any of the following:

        0: This is not a trial subscription. If this parameter is not posted, will be assumed as 0.

        1: This is a trial subscription.
      </td>

      <td>
        1
      </td>
    </tr>
  </tbody>
</Table>
