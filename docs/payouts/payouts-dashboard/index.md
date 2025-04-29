---
title: Payouts Dashboard
excerpt: ''
deprecated: false
hidden: false
metadata:
  title: Payouts Dashboard
  description: >-
    Discover the powerful features of the PayU Dashboard. Manage your
    transactions, analyze business performance, and access comprehensive
    reporting tools all in one place. Learn how to integrate and optimize your
    merchant services with PayU's intuitive dashboard.
  keywords:
    - PayU Dashboard overview
    - PayU payment dashboard
    - PayU transaction management
    - PayU dashboard features
  robots: index
next:
  description: ''
---
The *Payouts* module of PayU Dashboard is a handy user interface to manage your payouts. You can view, create, and check the statuses of the Payouts corresponding to the accounts you have. Payouts Dashboard is enabled only after the successful activation of Payouts for the specified merchant account.

![](https://devguide.payu.in/wordpress/wp-content/uploads/2021/08/image-203-1024x559.jpg)

The capabilities of Payouts Dashboard are:

* Displays data for all the accounts hosted by you
* Displays Account Balance and Account Statements specific to each account
* Enables you to make a payout without calling any APIs
* Shows summary of all Payouts together or individually as per their statuses
* Allows you to add Maker/Checker flow for heavy transactions

The following table explains the fields available on the dashboard:

<table style={{ border: "0.1rem solid rgb(242, 242, 242)" }}>
  <tbody>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Field Name</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Description</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Additional Information</strong></td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Virtual Account List&nbsp;</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to select the Virtual Accounts associated with a&nbsp;particular&nbsp;merchant whose details you want to view&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>One merchant can have multiple accounts.&nbsp;Each account is linked with a unique Payouts ID.&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Duration</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to select the time period or date range to filter the account and payout details&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Valid values are&nbsp;Today,&nbsp;Yesterday&nbsp;Past 7 days,&nbsp;Past 30 days since onboarding&nbsp;custom range.&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Add Money</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Displays the details corresponding to the virtual account you have selected, such as Account Number, IFSC Code, Beneficiary Name, Account Type&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Displays step-by-step procedure for adding money to the Virtual Account using from merchant’s bank account&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Make a Transfer</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to create a Payouts request.&nbsp;&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>On clicking this button, you are redirected to the <i>Make a Payment</i> web page.&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Account Balance</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Indicates the balance of the virtual account whose details you are viewing&nbsp;&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>–&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Payout Volume</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Indicates the amount of funds sent via Payouts and the number of successful Payouts&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Payouts with status as Success are only considered while displaying this data.&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Account Statement</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to view the details of the financial transactions done corresponding to the account selected&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Additional options like Filter, Duration, and Download are available under this tab.&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Payouts</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to view the details of all the payouts done within a specific duration for a particular virtual account&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Additional options like Filter, Duration, and Download are available under this tab.&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Deposits</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to view the details of transactions done to add money/funds into the virtual account&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Additional options like Filter, Duration, and Download are available under this tab.&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Reversed Payouts</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to view the payouts that are moved into the reversed state&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Additional options like Filter, Duration, and Download are available under this tab&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Pending Approval tab</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to view the payouts that are pending for Maker/Checker Approval&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Maker/Checker Approval workflow is imposed on certain high amount payouts&nbsp;</td>
    </tr>
    <tr>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}><strong>Rejected Payouts tab</strong></td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Used to view the payouts that are cancelled or rejected due to certain conditions or issues&nbsp;</td>
      <td style={{ border: "0.1rem solid rgb(242, 242, 242)", padding: "0.8em" }}>Additional options like Filter, Duration, and Download are available under this tab.&nbsp;</td>
    </tr>
  </tbody>
</table>