---
name: s2s Request params
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

      <th>
        **Example**
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
        `String` The merchant key provided by PayU during onboarding.
      </td>

      <td>
        MERCHANT123
      </td>
    </tr>

    <tr>
      <td>
        referenceId\
         `mandatory`
      </td>

      <td>
        `String` Reference ID for transaction tracking and this must be unique for every transaction.
      </td>

      <td>
        REF123456
      </td>
    </tr>

    <tr>
      <td>
        amount\
         `optional`
      </td>

      <td>
        `String` Amount of the transaction.  

        * \*Note\*\*: This value will not be considered as the transaction. Only the details in the `order.paymentChargeSpecificationparameter.price`field will be considered.
      </td>

      <td>
        1000
      </td>
    </tr>

    <tr>
      <td>
        currency\
         `mandatory`
      </td>

      <td>
        `String` Currency of the transaction (e.g., INR).
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        paymentMethod\
         `mandatory`
      </td>

      <td>
        `Object` Details about the payment method used. For more information, refer to [paymentMethod object fields description](#paymentmethod-object-fields-description).
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        order\
         `mandatory`
      </td>

      <td>
        `Object` Details about the transaction order including product information, ordered items, user-defined fields, and payment charge specifications. For more information, refer to [order object fields description](#order-object-fields-description)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        additionalInfo\
         `mandatory`
      </td>

      <td>
        `Object` Additional information including enforced payment methods, single instalment, virtual payment address (VPA), and various options for user preferences during the transaction. For more information, refer to [additionalInfo object fields description](#additionalinfo-object-fields-description)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        callBackActions\
         `mandatory`
      </td>

      <td>
        `Object` Actions to perform on the payment server in different scenarios. For example, success, failure, cancellation, cash on delivery, etc. For more information, refer to [callbackActions object fields description](#callbackactions-object-fields-description)
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        billingDetails `mandatory`
      </td>

      <td>
        `Object` Billing details of the customer including name, address, phone number, email, etc. For more information, refer to [billingDetails object field descriptions](#billingdetails-object-field-descriptions).
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        deviceInfo\
        `mandatory for S2S`
      </td>

      <td>
        `Object`Device info of the customer.  For more information, refer to[ deviceInfo object field descriptions](#deviceinfo-object-field-descriptions)  .
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>
