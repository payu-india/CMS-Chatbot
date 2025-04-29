---
title: Delete a Saved Card API
excerpt: ''
api:
  file: storecard-2.json
  operationId: delete_payment_instrument
deprecated: false
hidden: true
metadata:
  title: Delete Saved Card API
  description: >-
    Learn how to use the PayU Delete Saved Card API to securely remove stored
    card details. This guide provides detailed instructions, request parameters,
    and sample responses for efficient card management."
  keywords:
    - Delete Saved Card API
    - ' saved card removal'
    - ' delete secure card'
    - ' delete tokenized cards'
    - ' card management'
    - ' delete saved card details'
  robots: index
next:
  description: ''
---
This API is used to delete an existing card stored on PayU Vault.

HTTP Method: **POST**

<GENERALAPIsEnvironment />

<details>
  <summary>Sample Response</summary>

* On successful deletion

```plaintext
{
        status: 1,
        msg: "My_card card deleted successfully",
}
```

* On failure of deletion

```plaintext
{
"status": 0,
"msg": card not found
}
```

</details>

<details>
  <summary>Response parameters</summary>

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
        status
      </td>
      <td>
        The status of the response can be any of the following:\
           -**1**: Success  

        * **0**: Failure
      </td>
      <td>
        1
      </td>
    </tr>
    <tr>
      <td>
        msg
      </td>
      <td>
        The description of the response whether the card details were deleted successfully or not deleted.
      </td>
      <td>
        My\_card deleted successfully
      </td>
    </tr>
  </tbody>
</Table>

</details>

## Request Parameters

<details>
  <summary>Reference info for request parameters</summary>

<KeyHashForGeneralParametersDescription />

</details>