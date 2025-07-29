---
title: Delete Card API
deprecated: false
hidden: false
metadata:
  robots: index
---
This API is used to delete an existing card stored on PayU Vault.

HTTP Method: **POST**

## Sample request

```
curl --location --request DELETE '<info.storecard.service.url>/storecard/card/v1?userCredential=sms%3A123&cardToken=18c7804aafdac732b5e8&networkTokenissuerToken=null&bankType=null' \
--header 'Content-Type: application/json' \
--header 'mid: 2' \
--data '{"userCredential":"sms:123",
"cardToken" : "1f4463abae4175a70516",
"networkToken" : "4489682380100740",
"issuerToken":"src_wqe47hxfjksor89y4",
"bankType":"SODEXO"
}'
```

## Sample Response
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

## Response parameters
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
          The status of the response can be any of the following:
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


## Request Parameters

<Accordion title="Reference info for request parameters" icon="fa-flask">
  <KeyHashForGeneralParametersDescription />
</Accordion>
