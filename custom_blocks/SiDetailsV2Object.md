---
name: siDetails v2 object
---
### siDetails object fields description

<Table>
  <thead>
    <tr>
      <th>
        Field
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
        billingCycle
        `mandatory`
      </td>

      <td>
        The frequency of the billing, indicating how often the payment occurs.
      </td>

      <td>
        MONTHLY
      </td>
    </tr>

    <tr>
      <td>
        billingAmount\
        `mandatory`
      </td>

      <td>
        The amount to be billed for each cycle.
      </td>

      <td>
        1.00
      </td>
    </tr>

    <tr>
      <td>
        billingCurrency\
        `mandatory`
      </td>

      <td>
        The currency in which the billing amount is denominated.
      </td>

      <td>
        INR
      </td>
    </tr>

    <tr>
      <td>
        billingInterval\
        `mandatory`
      </td>

      <td>
        The interval between billing cycles, specified in terms of the cycle frequency.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        paymentStartDate\
        `mandatory`
      </td>

      <td>
        The date when the payment cycle begins.
      </td>

      <td>
        2020-09-16
      </td>
    </tr>

    <tr>
      <td>
        paymentEndDate\
        `mandatory`
      </td>

      <td>
        The date when the payment cycle ends.
      </td>

      <td>
        2020-10-16
      </td>
    </tr>

    <tr>
      <td>
        siTokenRequestor\
        `optional`
      </td>

      <td>
        This is optional and is only needed before 30th September, 2022 to activate new mandate setups in a controlled manner than activating it completely on all users. This involves creating token at the time of susbcription set. You can include any of the following values::\
        1 : PayU will tokenise the card and share it in same subscription setup call with issuers for subscription setup.\
        2: PayU will do the authorization on plain card. Later, the same response will be shared to merchant.
      </td>

      <td>
        1
      </td>
    </tr>

    <tr>
      <td>
        authpayuid\
        `mandatory for modifying subscription`
      </td>

      <td>
        An identifier used for the authorization of payments via PayU.
      </td>

      <td>

      </td>
    </tr>

    <tr>
      <td>
        action\
        `mandatory for cards`
      </td>

      <td>
        This field is used to modify or delete an existing subscription.
      </td>

      <td>

      </td>
    </tr>
  </tbody>
</Table>
