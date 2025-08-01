---
title: Create a Payment Link with SI
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
You can create a payment link with Standing Instruction on PayUBiz Dashboard and send it to your customer. After the customer enters his card details, the Standing Instruction or recurring payment is enabled or registered.

To create a payment link with Standing Instruction on PayUBiz Dashboard:

1. Log on to PayUBiz Dashboard.
2. Select **New Email Invoice** from the menu of the left pane.

   The *New Invoice* popup page is displayed.

<Image align="center" width="552px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayUBizDasgh_Home-2-1024x615.png" />

<Image align="center" width="552px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayUBizDash_New_Email_Invoice_First_Page-1024x733.png" />

3. Provide the the basic details as described in the following table:

| **Field**      | **Description**                                   |
| -------------- | ------------------------------------------------- |
| Name           | Enter the name of your customer.                  |
| Transaction ID | Enter the transaction ID for the transaction.     |
| Email ID       | Enter the customer email ID.                      |
| Description    | Enter the description of the transaction details. |
| Amount         | Enter the transaction amount.                     |
| Mobile No      | Enter the customer’s mobile number.               |

4. Scroll down the *New Invoice* pop-up page to enable the Standing Instructions and provide the additional details.

<Image align="center" width="552px" src="https://devguide.payu.in/wordpress/index.php/wp-json/getobject?keyname=uploads/2022/02/PayuBiz_DB_New_Email_Invoice-1-1024x733.png" />

5. Provide the Standing Instructions details as described in the following table:

<Table>
  <thead>
    <tr>
      <th>
        **Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        SI credential
      </td>

      <td>
        Enter the SI credential provided by PayU to you (merchant).
      </td>
    </tr>

    <tr>
      <td>
        Send Reminder
      </td>

      <td>
        Select this check box and perform the following:  

        * Use the first drop-down list to configure the frequency.  
        * Select the period in the second drop-down list.  
        * Select the period duration in the third drop-down list.
      </td>
    </tr>

    <tr>
      <td>
        Set Expiry
      </td>

      <td>
        Select this check box and perform the following:  

        * Use the date selector to configure the expiry date of the Standing Instruction.  
        * Enter the time of expiry in the second field on the specified date.
      </td>
    </tr>

    <tr>
      <td>
        Enable SI
      </td>

      <td>
        Select this check box to enable Standing Instruction for this transaction.
      </td>
    </tr>

    <tr>
      <td>
        Billing Amount
      </td>

      <td>
        Enter the billing amount that must be collected using Standing Instruction.
      </td>
    </tr>

    <tr>
      <td>
        Billing Currency
      </td>

      <td>
        Select the currency for the transaction.
      </td>
    </tr>

    <tr>
      <td>
        Billing Interval
      </td>

      <td>
        Select the billing interval from the drop-down list.
      </td>
    </tr>

    <tr>
      <td>
        Billing Cycle
      </td>

      <td>
        Select the billing cycle from the drop-down list.
      </td>
    </tr>

    <tr>
      <td>
        Payment Expiry
      </td>

      <td>
        Select the payment expiry date using the date selector.
      </td>
    </tr>
  </tbody>
</Table>

6. Click **Confirm**.
