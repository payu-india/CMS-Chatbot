---
title: Backup of Recurring Payment APIs
excerpt: ''
deprecated: false
hidden: true
metadata:
  title: ''
  description: ''
  robots: index
next:
  description: ''
---
# PreDebit Notification API

## var1 JSON Fields Description

The **var1** variable is in JSON format and comprises of the following parameters:

<Table>
  <thead>
    <tr>
      <th>
        **JSON Field**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        authpayuid
        **mandatory**
      </td>

      <td>
        The value of mihpayid returned in the payment response of Registration transaction when transaction is successfully completed. As explained earlier in the document, you need to map this value against customer profile at his end so that correct authPayuid will be passed in the request.
      </td>
    </tr>

    <tr>
      <td>
        requestId\
        **mandatory**
      </td>

      <td>
        Unique request value generated at merchant’s end to distinguish independent request call.
      </td>
    </tr>

    <tr>
      <td>
        debitDate\
        **mandatory for cards and UPI**
      </td>

      <td>
        This parameter contains the date of debit when the recurring would be charged by merchant.  

        * In UPI:\*\*  
        * For all frequencies (other than Daily and Adhoc), the merchant must send the notification 48 hours before the debit.  
        * For Daily and Adhoc frequency, the merchant must send the notification 24 hours before the debit. If the notification is sent after these durations, then the debit will fail.
      </td>
    </tr>

    <tr>
      <td>
        invoiceDisplayNumber\
        **mandatory only for cards**
      </td>

      <td>
        A unique display number by merchant for every subsequent invoice/recurring charge. This can be displayed on the merchant’s panel to the customer. This same value needs to be sent in the recurring api also.
      </td>
    </tr>

    <tr>
      <td>
        amount\
        **mandatory for cards and UPI**
      </td>

      <td>
        The transaction amount which will be deducted from the customer’s payment instrument.\
        **For Cards:**  

        * In case of Fixed billing plan, this amount should be same as\
          billingAmount sent during Registration transaction.  
        * In case of Adhoc billing plan, this amount should be equal to or lesser than billingAmount sent during the Registration transaction.  
        * \*\*Note\*\*: The amount mentioned in the Pre-Debit notification API for UPI should be same as the next execution amount. Else, the next recurring execution request will fail.
      </td>
    </tr>

    <tr>
      <td>
        action\
        **optional**
      </td>

      <td>
        Any of the following actions can be performed:  

        * **Retrieve**: Query the status of the pre-debit notification. Only authpayuid and invoice display numbers are mandatory for this action.  
        * **Delete**: Delete the already generated pre debit. Only authpayuid and invoice display numbers are mandatory for this action.
      </td>
    </tr>
  </tbody>
</Table>

## Response Parameters

For more information on response parameters, refer to [Additional Info. for Recurring Payment APIs](ref:additional-info-for-recurring-payment-apis).

## Request Parameters
