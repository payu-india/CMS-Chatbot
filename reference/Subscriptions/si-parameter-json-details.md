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

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        **JSON Field**
      </th>

      <th>
        **Description**
      </th>

      <th>
        **Example**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        billingCycle
        **mandatory**
      </td>

      <td>
        Billing Cycle defines whether the customer needs to be charged over Daily, Weekly basis, Monthly or Yearly basis or one time.  
      </td>

      <td>
        ONCE
      </td>
    </tr>

    <tr>
      <td>
        billingInterval
        **mandatory**
      </td>

      <td>
        Billing Interval is closely coupled with the **billingCycle** field and denotes at what frequency, the subscription plan needs to be executed. For monthly subscriptions, parameter values need to be sent in the request are:

        - billingCycle = MONTHLY
        - billingInterval = 1
          Similarly, by keeping the following values, customer will be charged once in every 3 days:
        - billingCycle = DAILY
        - billingInterval = 3
      </td>

      <td>
        - billingCycle = MONTHLY
        - billingInterval = 1 
      </td>
    </tr>

    <tr>
      <td>
        billingAmount<br />**mandatory**
      </td>

      <td>
        The billing amount is passed in XX. By default, the amount passed is treated as maximum amount which means the merchant is free to charge any amount for customer up to the amount specified in the defined subscription call.  <br />**Note**: For UPI, **billingAmount** should not be more than INR 15000 as it is the maximum limit allowed for UPI currently.
      </td>

      <td>
        INR 2000
      </td>
    </tr>

    <tr>
      <td>
        billingCurrency<br />**mandatory**
      </td>

      <td>
        This field must be passed as “INR” .
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        paymentStartDate<br />**mandatory**
      </td>

      <td>
        The start date of the billing plan is specified in this field with the YYYY-MM-DD format.

        - _Note_\*: All the subsequent recurring transactions will be processed from this date onwards as per**billingCycle**and**billingInterval**fields combination. This date acts as reference point for recurring payments.**Note**: In case of UPI, send the current date here and any other value will be ignored.
      </td>

      <td>
        2022-02-14
      </td>
    </tr>

    <tr>
      <td>
        paymentEndDate<br />**mandatory**
      </td>

      <td>
        The end date of the billing plan is specified in this field with the YYYY-MM-DD format.

        - _Note_\*: Pass the correct end date to PayU. Depending upon start date and end date, number of payment iterations are internally calculated and same information is passed to acquirers or banks.
      </td>

      <td>
        2023-01-14
      </td>
    </tr>

    <tr>
      <td>
        siTokenRequestor<br />**mandatory for saved cards**
      </td>

      <td>
        This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of subscription set. You can include any of the following values::

        - **1** : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.
        - **2**: PayU will do the authorization on plain card. Later, the same response will be shared to merchant.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        remarks<br />**optional**
      </td>

      <td>
        This field is used to provide remarks on PSP applications during the registration transaction of UPI.  For cards and Net Banking, this parameter has no significance.  Character limit = 50. 

        - _Note_\*: This field is applicable only for UPI.
      </td>

      <td>
        Subscription for a year
      </td>
    </tr>

    <tr>
      <td>
        billingLimit<br />**optional**
      </td>

      <td>
        For UPI, this field is used to decide the period corresponding which the debit from the mandate recurring date can happen and this mandate registration date is confirmed during registration transaction of UPI.

        - _Note_\*: This field is applicable only for UPI.<br />The possible values are:
        - **ON** = Use this parameter to deduct on a specific date
        - **BEFORE** = Use this parameter to deduct before and on a specific date
        - **AFTER** = Use this parameter to After and on the specific date
        - _Note_\*: If no value is passed, ‘AFTER’ is considered by default.
      </td>

      <td>
        ON=2022-02-20<br />OR
        BEFORE= 2022-02-20
        OR
        AFTER=2022-02-20
      </td>
    </tr>

    <tr>
      <td>
        billingRule<br />**optional**
      </td>

      <td>
        For UPI, this field is used to decide the limitation on the amount of recurring debit against the mandate amount which is set during registration transaction of UPI.

        - _Note_\*: This field is applicable only for UPI.<br />The possible values are:
        - **MAX** = This is the maximum amount that a merchant can debit, that is, merchant can debit lesser or equal to this amount for a recurring transaction.
        - **EXACT**= This the exact amount that a merchant can debit in recurring debits.

        Note: If no value is passed, ‘MAX’ is considered by default.
      </td>

      <td>
        MAX=5000<br />OR
        EXACT=5000
      </td>
    </tr>

    <tr>
      <td>
        billingDate<br />**optional**
      </td>

      <td>
        - _Applicable for UPI only_\*: This field is used to decide the date/day, basis which the recurring debit should happen. This can be ignored and the debit will happen as per the start date in every cycle.
      </td>

      <td>
        billingDate=1
      </td>
    </tr>

    <tr>
      <td>
        authpayuid<br />**mandatory for modifying subscription with cards**
      </td>

      <td>
        This field is used only to modify an existing subscription/consent. Modification means modifying billing details like startDate, endDate, billing cycle, billing interval, billing amount.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        action<br />**mandatory for cards**
      </td>

      <td>
        This field is used to modify or delete an existing subscription.
      </td>

      <td>
        modify<br />or
        delete
      </td>
    </tr>
  </tbody>
</Table>

<Callout icon="📘" theme="info">
  ### Recurrence Rule for billingDate parameter

  For WEEKLY

  If the start date (day) = Monday, Rule<br />Value = 1, for Tuesday it is 2.........for
  Sunday it is 7.

  For FORTNIGHTLY

  For Start Date (1st – 15th) Rule Value<br />= Start Date

  For Start Date (16th – 31th) Rule<br />Value = Start Date – 15

  For MONTHLY and greater than Monthly<br />frequencies

  Rule Value = Start Date

  Possible values : Numeric values ( 1- 31)

  For WEEKLY frequency: 

  If the start date (day) = Monday, rule value = 1.

  If the start date (day) = Tuesday, it is 2.

  ...

  ...

  If the start date (day) = Sunday, it is 7.

  For FORTNIGHTLY frequency

  For Start Date (1st – 15th) Rule Value = Start Date

  For Start Date (16th – 31th) Rule Value = Start Date – 15

  For MONTHLY and greater than monthly frequency

  Rule Value = Start Date, where the possible value is a numeric value between 1- 31
</Callout>

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

<Table>
  <thead>
    <tr>
      <th>
        **Billing Cycle**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        ONCE
      </td>

      <td>
        Used when a merchant wants to execute Split / Partial payment use cases where the partial amount is paid upfront during the Consent transaction and remaining amount needs to be paid on later.
        WEEKLY is used if the merchant wants to run a bi-weekly subscription then values will be similar to the following, so the customer will be charged once in every 2 weeks.:
      </td>
    </tr>

    <tr>
      <td>
        ADHOC
      </td>

      <td>
        Used in use cases such as post-paid bills where there is no definite billing cycle and billing amount.

        - **billingInterval** = Billing Interval is closely coupled with the value of “billingCycle” and denotes at what frequency, the subscription plan needs to be executed.
      </td>
    </tr>

    <tr>
      <td>
        MONTHLY
      </td>

      <td>
        Used for monthly subscriptions, parameter values that need to be sent in request are:

        - billingCycle = MONTHLY 
        - billingInterval = 1
      </td>
    </tr>

    <tr>
      <td>
        YEARLY
      </td>

      <td>
        Used for yearly subscriptions. parameter values that need to be sent in request are:

        - billingCycle = YEARLY
        - billingInterval = 1
      </td>
    </tr>

    <tr>
      <td>
        WEEKLY
      </td>

      <td>
        Used for weekly subscriptions. Use the following values to charge the customer once every week:

        - billingCycle = WEEKLY
        - billingInterval = 1
      </td>
    </tr>

    <tr>
      <td>
        DAILY
      </td>

      <td>
        Used for daily subscriptions.<br />Use the following values to charge the customer once in every 3 days:

        - billingCycle = DAILY 
        - billingInterval = 3
      </td>
    </tr>
  </tbody>
</Table>

<br />
