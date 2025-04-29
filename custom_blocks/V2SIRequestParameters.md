---
name: v2 SI Request Parameters
---
### Body

<Table>
  <thead>
    <tr>
      <th>
        **Parameter**
      </th>

      <th>
        **Description**
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        accountId
         `mandatory`
      </td>

      <td>
        `String`This must contain the key provided by PayU while onboarding.
      </td>
    </tr>

    <tr>
      <td>
        referenceId\
         `mandatory`
      </td>

      <td>
        `String`Reference ID for transaction tracking and this must be unique for every transaction.
      </td>
    </tr>

    <tr>
      <td>
        amount\
         `optional`
      </td>

      <td>
        `String`Amount of the transaction.  

        * \*Note\*\*: This value will not be considered as the transaction. Only the details in the ` order.paymentChargeSpecificationparameter` field will be considered.
      </td>
    </tr>

    <tr>
      <td>
        currency\
         `mandatory`
      </td>

      <td>
        `String`Currency of the transaction (e.g., INR).  By default, **INR** is posted.
      </td>
    </tr>

    <tr>
      <td>
        order\
         `mandatory`
      </td>

      <td>
        `JSON Object`Details about the transaction order including product information, ordered items, user defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)
      </td>
    </tr>

    <tr>
      <td>
        additionalInfo\
         `mandatory`
      </td>

      <td>
        `JSON Object`Additional information including enforced payment methods and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description).  

        * \*Not&#x65;**: The`txnFlow` field in this JSON object must be set to **&#x6E;onseamless\*\*.
      </td>
    </tr>

    <tr>
      <td>
        callBackActions\
         `mandatory`
      </td>

      <td>
        `JSON Object`Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc.  For more information, refer to[ callbackActions object fields description](#callbackactions-object-fields-description)
      </td>
    </tr>

    <tr>
      <td>
        billingDetails\
         `mandatory`
      </td>

      <td>
        `JSON Object`Billing details of the customer including name, address, phone number, email, etc.  For more information, refer to[ billingDetails object fields descriptions](#billingdetails-object-fields-descriptions).
      </td>
    </tr>

    <tr>
      <td>
        siDetails
      </td>

      <td>
        `JSON Object` Subscription or SI details for the consent transaction. For more information, refer to[ siDetails object fields description](#sidetails-object-fields-description).
      </td>
    </tr>
  </tbody>
</Table>
