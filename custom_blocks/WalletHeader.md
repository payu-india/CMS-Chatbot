---
name: Wallet Header
---
### Header

<Table>
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
        x-api-key
        **mandatory**
      </td>

      <td>
        `String` This is a unique key.
      </td>

      <td>
        7fe1c0de
      </td>
    </tr>

    <tr>
      <td>
        clientId\
        **mandatory**
      </td>

      <td>
        `String` Uniquely identifies the client. During program enrolment each client is provided with a unique client id by Prepaid
      </td>

      <td>
        2000
      </td>
    </tr>

    <tr>
      <td>
        bankId\
        **mandatory**
      </td>

      <td>
        `Numeric` Bank Id is provided by Prepaid Aero during program enrolment to uniquely identify the card issuer.
      </td>

      <td>
        7000
      </td>
    </tr>

    <tr>
      <td>
        entityId\
        **mandatory**
      </td>

      <td>
        `Numeric` Defaults to parent branch i.e., 100
      </td>

      <td>
        100
      </td>
    </tr>

    <tr>
      <td>
        secureCode\
        **mandatory**
      </td>

      <td>
        `String` Uniquely identifies the client on payload level for performing operations.
      </td>

      <td>
        AfYtlO5kqdySIjXyNmGg3F
      </td>
    </tr>
  </tbody>
</Table>
