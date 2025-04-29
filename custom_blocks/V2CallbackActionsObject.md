---
name: v2 callbackActions object
---
### callbackActions object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        successAction
         `mandatory`
      </td>

      <td>
        `String`URL to redirect to upon successful payment.
      </td>
    </tr>

    <tr>
      <td>
        failureAction\
         `mandatory`
      </td>

      <td>
        `String`URL to redirect to if the payment is failed.
      </td>
    </tr>

    <tr>
      <td>
        cancelAction\
         `mandatory`
      </td>

      <td>
        `String`URL to redirect to if the transaction is cancelled.
      </td>
    </tr>

    <tr>
      <td>
        codAction\
         `optional`
      </td>

      <td>
        `String`URL to handle Cash on Delivery actions.
      </td>
    </tr>

    <tr>
      <td>
        termAction\
         `optional`
      </td>

      <td>
        `String`URL for completing terms and conditions actions.
      </td>
    </tr>

    <tr>
      <td>
        returnAction\
         `optional`
      </td>

      <td>
        `String`URL to return to after successful payment action is completed.
      </td>
    </tr>
  </tbody>
</Table>
